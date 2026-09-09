/* The SVG is the geometry source and static fallback. Canvas deforms the strands,
   not the portrait, with a traveling wave whose first 160 scene units stay fixed. */
(() => {
  'use strict';
  const hero = document.querySelector('.mind-hero');
  const scene = hero?.querySelector('.mind-scene');
  const svg = scene?.querySelector('.mind-lines');
  if (!svg || !window.ResizeObserver || !window.IntersectionObserver) return;
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  canvas.className = 'mind-flow';
  canvas.setAttribute('aria-hidden', 'true');
  hero.insertBefore(canvas, scene);

  const paths = [...svg.querySelectorAll('.thread')];
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  let strands = [], scale = 1, offsetX = 0, offsetY = 0, ratio = 1;
  let threadOpacity = 0, thoughtOpacity = 0, gradient;
  let frame = 0, previousTime = 0, elapsed = 0, visible = false;

  function resize() {
    const bounds = hero.getBoundingClientRect();
    const art = scene.getBoundingClientRect();
    if (!bounds.width || !bounds.height) return;
    ratio = Math.min(devicePixelRatio || 1, 2);
    canvas.width = Math.ceil(bounds.width * ratio);
    canvas.height = Math.ceil(bounds.height * ratio);
    scale = art.width / svg.viewBox.baseVal.width;
    offsetX = art.left - bounds.left;
    offsetY = art.top - bounds.top;
    const styles = getComputedStyle(scene);
    threadOpacity = Number(styles.getPropertyValue('--thread-opacity'));
    thoughtOpacity = Number(styles.getPropertyValue('--thought-opacity'));
    // Sample only as far as the viewport can see, with ample deformation overscan.
    // The underlying SVG continues another 10,000 units, so no path endpoint is visible.
    const reach = (Math.hypot(bounds.width, bounds.height) + art.width) / scale + 500;
    strands = paths.map(path => {
      const length = Math.min(path.getTotalLength(), reach);
      const steps = Math.ceil(length / 28);
      const points = [];
      for (let j = 0; j <= steps; j++) {
        const distance = length * j / steps;
        const point = path.getPointAtLength(distance);
        const before = path.getPointAtLength(Math.max(0, distance - 1));
        const after = path.getPointAtLength(Math.min(length, distance + 1));
        const dx = after.x - before.x, dy = after.y - before.y;
        const tangent = Math.hypot(dx, dy) || 1;
        const ramp = Math.min(1, Math.max(0, (distance - 160) / 650));
        points.push({x: point.x, y: point.y, nx: -dy / tangent, ny: dx / tangent,
          distance, amplitude: 48 * ramp * ramp * (3 - 2 * ramp)});
      }
      return {points, colour: path.getAttribute('stroke'), width: Number(path.getAttribute('stroke-width')),
        drawn: new Float32Array(points.length * 2)};
    });
    ctx.setTransform(ratio * scale, 0, 0, ratio * scale, ratio * offsetX, ratio * offsetY);
    gradient = ctx.createLinearGradient(0, 300, 1125, 2550);
    gradient.addColorStop(0, '#a88ae0');
    gradient.addColorStop(.5, '#5b3a93');
    gradient.addColorStop(1, '#f07ba6');
    paint();
    hero.classList.add('flow-ready');
    sync();
  }

  function trace(strand, reverse = false, move = true) {
    const points = strand.drawn;
    const first = reverse ? points.length - 2 : 0;
    if (move) ctx.moveTo(points[first], points[first + 1]);
    else ctx.lineTo(points[first], points[first + 1]);
    for (let j = first; reverse ? j >= 0 : j < points.length; j += reverse ? -2 : 2) {
      ctx.lineTo(points[j], points[j + 1]);
    }
  }

  function paint() {
    if (!strands.length) return;
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.setTransform(ratio * scale, 0, 0, ratio * scale, ratio * offsetX, ratio * offsetY);
    strands.forEach((strand, index) => {
      strand.points.forEach((p, j) => {
        const phase = p.distance * Math.PI * 2 / 850 - elapsed * 1.6 + index * .008;
        const displacement = motion.matches ? 0 : p.amplitude *
          (Math.sin(phase) + .24 * Math.sin(phase * .57 - elapsed * .45));
        strand.drawn[j * 2] = p.x + p.nx * displacement;
        strand.drawn[j * 2 + 1] = p.y + p.ny * displacement;
      });
    });
    ctx.beginPath();
    trace(strands[0]);
    trace(strands[strands.length - 1], true, false);
    ctx.closePath();
    ctx.globalAlpha = thoughtOpacity;
    ctx.fillStyle = gradient;
    ctx.fill();
    ctx.globalAlpha = threadOpacity;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    strands.forEach(strand => {
      ctx.beginPath();
      trace(strand);
      ctx.strokeStyle = strand.colour;
      ctx.lineWidth = strand.width;
      ctx.stroke();
    });
  }

  function tick(now) {
    frame = 0;
    if (previousTime) elapsed += Math.min((now - previousTime) / 1000, .1);
    previousTime = now;
    paint();
    frame = requestAnimationFrame(tick);
  }

  function sync() {
    cancelAnimationFrame(frame);
    frame = 0;
    previousTime = 0;
    if (visible && !document.hidden && !motion.matches && strands.length) frame = requestAnimationFrame(tick);
    else if (motion.matches) paint();
  }
  new ResizeObserver(resize).observe(hero);
  // The scene changes width at a breakpoint independently of the hero's height.
  new ResizeObserver(resize).observe(scene);
  new IntersectionObserver(entries => { visible = entries[0].isIntersecting; sync(); }).observe(hero);
  document.addEventListener('visibilitychange', sync);
  motion.addEventListener('change', sync);
  resize();
})();
