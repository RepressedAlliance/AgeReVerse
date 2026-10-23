/* Apply the reviewed state effects to a common normal/hover SVG mask. */
const fs = require('node:fs');
const path = require('node:path');
const sharp = require(process.argv[4] || 'sharp');

function distances(mask, width, height) {
  const horizontal = new Float32Array(width * height);
  const result = new Float32Array(width * height);
  for (let y = 0; y < height; y++) {
    let last = -10000;
    for (let x = 0; x < width; x++) {
      if (mask[(y * width + x) * 4 + 3] > 127) last = x;
      horizontal[y * width + x] = (x - last) ** 2;
    }
    last = 10000;
    for (let x = width - 1; x >= 0; x--) {
      if (mask[(y * width + x) * 4 + 3] > 127) last = x;
      horizontal[y * width + x] = Math.min(horizontal[y * width + x], (last - x) ** 2);
    }
  }
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      let best = 1600;
      for (let yy = Math.max(0, y - 40); yy < Math.min(height, y + 41); yy++) {
        best = Math.min(best, horizontal[yy * width + x] + (yy - y) ** 2);
      }
      result[y * width + x] = Math.max(0, Math.sqrt(best) - .5);
    }
  }
  return result;
}

(async () => {
  const rows = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const output = process.argv[3];
  for (const row of rows) {
    const [width, height] = row.size;
    const mask = await sharp(path.join(output, row.key + '.svg'), {density: 288})
      .resize(width, height).ensureAlpha().raw().toBuffer();
    const field = row.hover ? distances(mask, width, height) : null;
    const pixels = Buffer.alloc(width * height * 4);
    const quantize = row.quantization === 'truncate' ? Math.floor : Math.round;
    for (let i = 0; i < width * height; i++) {
      const ink = mask[i * 4 + 3] / 255;
      let opacity = 0, premultiplied = [0, 0, 0];
      if (row.hover) {
        const t = Math.min(row.profile.length - 1, field[i] * 2);
        const index = Math.floor(t), fraction = t - index;
        const a = row.profile[index], b = row.profile[Math.min(index + 1, row.profile.length - 1)];
        opacity = a[0] * (1 - fraction) + b[0] * fraction;
        premultiplied = [1, 2, 3].map(c => a[c] * (1 - fraction) + b[c] * fraction);
      }
      const alpha = ink + (1 - ink) * opacity;
      pixels[i * 4 + 3] = quantize(Math.max(0, Math.min(1, alpha)) * 255);
      for (let c = 0; c < 3; c++) {
        const value = alpha ? (ink + (1 - ink) * premultiplied[c]) / Math.max(alpha, 1e-8) : 1;
        pixels[i * 4 + c] = quantize(Math.max(0, Math.min(1, value)) * 255);
      }
    }
    await sharp(pixels, {raw: {width, height, channels: 4}}).png()
      .toFile(path.join(output, row.key + '.png'));
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
