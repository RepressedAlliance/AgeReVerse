"""Read a game's explicitly scoped terminology; never rewrite dialogue."""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import re
import tomllib

ROOT = Path(__file__).resolve().parents[2]
MUV_LUV_GAMES = {**{g: "AGE2" for g in ("tda00", "tda01", "tda02", "tda03", "imperial-capital-burns")},
                 **{g: "rUGP" for g in ("photonflowers", "photonmelodies")}}
GAMES = {**MUV_LUV_GAMES, "kiminozo": "AGE2"}
COLUMNS = ["jp", "cn", "context"]
BASELINE_COLUMNS = ["jp", "cn", "status", "chapter", "source", "source_row", "source_status", "occurrences", "basis"]
BASELINE_GROUPS = ("current", "reference", "candidate", "question", "excluded", "noise")


def read_table(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != COLUMNS:
            raise ValueError(f"Unexpected terminology columns: {path}")
        result = {}
        for row in reader:
            if set(row) != set(COLUMNS) or not all(row.values()):
                raise ValueError(f"Missing/extra terminology cells: {path}")
            if row["jp"] in result:
                raise ValueError(f"Duplicate JP key: {path}: {row['jp']}")
            if any(ord(char) < 32 for value in row.values() for char in value):
                raise ValueError(f"Control character in terminology: {path}")
            result[row["jp"]] = row
        return result


def load_game(game: str, root: Path = ROOT) -> dict[str, dict[str, str]]:
    """Load this game's table and only its explicitly applicable common table."""
    if game not in GAMES:
        raise ValueError(f"Unknown game: {game}")
    folder = root / GAMES[game] / "games" / game
    manifest = tomllib.loads((folder / "project.toml").read_text(encoding="utf-8"))
    expected = {}
    if game in MUV_LUV_GAMES:
        expected["terminology_common_authority"] = root / "localization/glossaries/muv-luv.ja-zh-Hans.csv"
    elif "terminology_common_authority" in manifest:
        raise ValueError(f"Unreviewed common terminology scope: {game}")
    expected["terminology_authority"] = root / "localization/glossaries" / f"{game}.ja-zh-Hans.csv"
    result = {}
    for key, correct_path in expected.items():
        path = (folder / manifest[key]).resolve()
        if path != correct_path.resolve():
            raise ValueError(f"Wrong scope in {game}: {key}")
        for jp, row in read_table(path).items():
            if jp in result and result[jp]["cn"] != row["cn"]:
                raise ValueError(f"Unreviewed common/game conflict: {game}: {jp}")
            result[jp] = dict(row, scope="common" if key.endswith("common_authority") else game)
    return result


def candidate_terms(text: str, glossary: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    """Longest-first candidates only. Context still needs human judgement."""
    if not glossary:
        return []
    patterns = []
    for jp in sorted(glossary, key=lambda value: (-len(value), value)):
        left = r"(?<![ァ-ヿA-Za-z])" if re.match(r"[ァ-ヿA-Za-z]", jp) else ""
        right = r"(?![ァ-ヿA-Za-z])" if re.search(r"[ァ-ヿA-Za-z]$", jp) else ""
        patterns.append(left + re.escape(jp) + right)
    return [glossary[m.group()] for m in re.finditer("|".join(patterns), text)]


def read_baseline(game: str, root: Path = ROOT) -> list[dict[str, str]]:
    if game not in GAMES:
        raise ValueError(f"Unknown game: {game}")
    folder = root / GAMES[game] / "games" / game
    manifest = tomllib.loads((folder / "project.toml").read_text(encoding="utf-8"))
    path = (folder / manifest["terminology_baseline"]).resolve()
    if path != (folder / "terminology/baseline.ja-zh-Hans.csv").resolve():
        raise ValueError(f"Wrong baseline scope: {game}")
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != BASELINE_COLUMNS:
            raise ValueError(f"Unexpected baseline columns: {path}")
        rows = list(reader)
    identities = set()
    for row in rows:
        if set(row) != set(BASELINE_COLUMNS) or any(value is None for value in row.values()):
            raise ValueError(f"Missing/extra baseline cells: {path}")
        if not all(row[key].strip() for key in ("jp", "status", "chapter", "source", "source_row", "basis")):
            raise ValueError(f"Missing baseline evidence fields: {path}")
        if row["status"] not in ("confirmed", "contextual", "candidate", "question", "excluded"):
            raise ValueError(f"Unknown baseline status: {path}: {row['status']}")
        identity = (row["source"], row["source_row"])
        if identity in identities:
            raise ValueError(f"Duplicate baseline source row: {path}: {identity}")
        identities.add(identity)
        if any(ord(char) < 32 for value in row.values() for char in value):
            raise ValueError(f"Control character in baseline: {path}")
    return rows


def baseline_group(row: dict[str, str]) -> str:
    """Group for reading only; never change a source's recorded status."""
    if row["source"].startswith("current-glossary-") or row["source"] == "kiminozo-glossary-20261009":
        return "current"
    if row["status"] == "excluded":
        return "excluded"
    if any(marker in row["basis"] for marker in ("类别：ordinary_katakana_or_sound", "类别：regex_address_false_positive")):
        return "noise"
    if row["status"] in ("candidate", "question"):
        return row["status"]
    return "reference"


def baseline_consistency_errors(terms: dict[str, dict[str, str]], rows: list[dict[str, str]]) -> list[str]:
    """Check current translation AND scope, not only the existence of a JP key."""
    current = {row["jp"]: row for row in rows if baseline_group(row) == "current"}
    errors = []
    for jp, term in terms.items():
        row = current.get(jp)
        if row is None:
            errors.append(f"缺少现行采用记录：{jp}")
        elif row["cn"] != term["cn"] or not row["basis"].startswith(term["context"]):
            errors.append(f"现行译法或使用限制未同步：{jp}")
        elif row["status"] != "confirmed":
            errors.append(f"现行采用记录状态不符：{jp}")
    for jp in current.keys() - terms.keys():
        errors.append(f"现行采用记录已不在本作术语表：{jp}")
    if len(current) != sum(baseline_group(row) == "current" for row in rows):
        errors.append("同一日文有多条现行采用记录，请合并当前决定并保留历史来源")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("game", choices=GAMES)
    parser.add_argument("--term", help="Exact JP key to inspect, not a replacement command")
    parser.add_argument("--baseline", action="store_true", help="Read current decisions alongside historical baseline evidence")
    parser.add_argument("--group", choices=BASELINE_GROUPS, help="Filter baseline records; requires --baseline")
    parser.add_argument("--check-baseline", action="store_true", help="Check current translations and scopes against the baseline")
    args = parser.parse_args()
    if args.group and not args.baseline:
        parser.error("--group requires --baseline")
    if args.baseline or args.check_baseline:
        own = read_table(ROOT / "localization/glossaries" / f"{args.game}.ja-zh-Hans.csv")
        rows = read_baseline(args.game)
        if args.check_baseline:
            errors = baseline_consistency_errors(own, rows)
            print(json.dumps({"game": args.game, "errors": errors}, ensure_ascii=False))
            raise SystemExit(bool(errors))
        selected = [dict(row, record_group=baseline_group(row)) for row in rows
                    if (not args.term or row["jp"] == args.term) and
                    (not args.group or baseline_group(row) == args.group)]
        selected.sort(key=lambda row: row["record_group"] != "current")
        result = {"game": args.game, "records": len(rows), "unique_jp_spellings": len({row["jp"] for row in rows}),
                  "groups": dict(Counter(baseline_group(row) for row in rows))}
        if args.term:
            result.update(current_term=own.get(args.term), evidence=selected)
        elif args.group:
            result.update(evidence=selected)
        print(json.dumps(result, ensure_ascii=False))
        return
    result = load_game(args.game)
    print(json.dumps(result.get(args.term) if args.term else
                     {"game": args.game, "effective_terms": len(result)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
