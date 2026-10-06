(() => {
  const ns = 'http://www.w3.org/2000/svg';
  const hyperbolicColor = '#c0392b';
  const euclideanColor = '#222222';
  const plot = { left: 58, right: 464, top: 20, bottom: 250 };

  function add(parent, tag, attributes = {}, text) {
    const element = document.createElementNS(ns, tag);
    Object.entries(attributes).forEach(([name, value]) => element.setAttribute(name, value));
    if (text !== undefined) element.textContent = text;
    parent.appendChild(element);
    return element;
  }

  document.querySelectorAll('[data-geometry-chart]').forEach(panel => {
    const area = panel.dataset.geometryChart === 'area';
    const svg = panel.querySelector('svg');
    const slider = panel.querySelector('input');
    const coordinate = panel.querySelector('.chart-coordinate');
    const play = panel.querySelector('.chart-play');
    const xmax = area ? 5 : 1;
    const ymax = area ? 500 : 8;
    const px = x => plot.left + x / xmax * (plot.right - plot.left);
    const py = y => plot.bottom - y / ymax * (plot.bottom - plot.top);
    const hyperbolicArea = r => 4 * Math.PI * Math.sinh(r / 2) ** 2;
    const distance = rho => Math.log1p(rho) - Math.log1p(-rho);
    const primary = area ? hyperbolicArea : distance;
    const secondary = area ? r => Math.PI * r * r : rho => rho;

    for (let i = 0; i <= (area ? 5 : 4); i++) {
      const y = area ? i * 100 : i * 2;
      add(svg, 'line', { x1: plot.left, x2: plot.right, y1: py(y), y2: py(y), class: 'chart-grid' });
      add(svg, 'text', { x: plot.left - 8, y: py(y) + 4, 'text-anchor': 'end', class: 'chart-label' }, y);
    }
    for (let i = 0; i <= 5; i++) {
      const x = xmax * i / 5;
      add(svg, 'text', { x: px(x), y: plot.bottom + 20, 'text-anchor': 'middle', class: 'chart-label' }, area ? x : x.toFixed(1));
    }
    add(svg, 'line', { x1: plot.left, x2: plot.left, y1: plot.top, y2: plot.bottom, class: 'chart-axis' });
    add(svg, 'line', { x1: plot.left, x2: plot.right, y1: plot.bottom, y2: plot.bottom, class: 'chart-axis' });
    add(svg, 'text', { x: 16, y: 135, transform: 'rotate(-90 16 135)', 'text-anchor': 'middle', class: 'chart-label' }, area ? 'Disk area' : 'Distance from origin');
    add(svg, 'text', { x: 260, y: 292, 'text-anchor': 'middle', class: 'chart-label' }, area ? 'Geodesic radius r' : 'Poincaré coordinate norm ρ');

    function curve(fn, max, color) {
      const points = Array.from({ length: 500 }, (_, i) => {
        const x = max * i / 499;
        return `${i ? 'L' : 'M'}${px(x).toFixed(2)},${py(fn(x)).toFixed(2)}`;
      }).join(' ');
      add(svg, 'path', { d: points, stroke: color, class: 'chart-curve' });
    }
    curve(primary, area ? 5 : 0.999, hyperbolicColor);
    curve(secondary, xmax, euclideanColor);
    add(svg, 'text', { x: 74, y: 37, fill: hyperbolicColor, 'font-size': 12 }, 'Hyperbolic');
    add(svg, 'text', { x: 74, y: 55, fill: euclideanColor, 'font-size': 12 }, 'Euclidean');
    if (!area) {
      add(svg, 'line', { x1: px(1), x2: px(1), y1: plot.top, y2: plot.bottom, stroke: '#94a3b8', 'stroke-dasharray': '5 4' });
    }
    const guide = add(svg, 'line', { y1: plot.top, y2: plot.bottom, class: 'chart-guide' });
    const marker = add(svg, 'circle', { r: 5, fill: hyperbolicColor, class: 'chart-marker' });
    const secondMarker = add(svg, 'circle', { r: 5, fill: euclideanColor, class: 'chart-marker' });
    const hitbox = add(svg, 'rect', { x: plot.left, y: plot.top, width: plot.right - plot.left, height: plot.bottom - plot.top, class: 'chart-hitbox' });
    let frame = null;
    let startTime;
    let startValue;

    function update(value) {
      value = Math.max(0, Math.min(Number(slider.max), value));
      value = Number(value.toFixed(area ? 2 : 3));
      slider.value = String(value);
      coordinate.textContent = value.toFixed(area ? 2 : 3);
      guide.setAttribute('x1', px(value));
      guide.setAttribute('x2', px(value));
      marker.setAttribute('cx', px(value));
      marker.setAttribute('cy', py(primary(value)));
      secondMarker.setAttribute('cx', px(value));
      secondMarker.setAttribute('cy', py(secondary(value)));
      if (area) {
        panel.querySelector('[data-value="hyperbolic"]').textContent = hyperbolicArea(value).toFixed(2);
        panel.querySelector('[data-value="euclidean"]').textContent = (Math.PI * value * value).toFixed(2);
      } else {
        panel.querySelector('[data-value="distance"]').textContent = distance(value).toFixed(3);
        panel.querySelector('[data-value="euclidean-distance"]').textContent = secondary(value).toFixed(3);
      }
    }

    function pause() {
      if (frame !== null) cancelAnimationFrame(frame);
      frame = null;
      play.textContent = 'Play';
      play.setAttribute('aria-pressed', 'false');
    }
    function animate(time) {
      if (startTime === undefined) startTime = time;
      const max = Number(slider.max);
      update((startValue + (time - startTime) / 12000 * max) % max);
      frame = requestAnimationFrame(animate);
    }
    play.addEventListener('click', () => {
      if (frame !== null) return pause();
      startTime = undefined;
      startValue = Number(slider.value);
      play.textContent = 'Pause';
      play.setAttribute('aria-pressed', 'true');
      frame = requestAnimationFrame(animate);
    });
    slider.addEventListener('input', () => { pause(); update(Number(slider.value)); });
    function point(event) {
      const rect = svg.getBoundingClientRect();
      const x = (event.clientX - rect.left) / rect.width * 480;
      pause();
      update((x - plot.left) / (plot.right - plot.left) * xmax);
    }
    hitbox.addEventListener('pointermove', event => {
      if (event.pointerType === 'mouse' || event.buttons) point(event);
    });
    hitbox.addEventListener('pointerdown', point);
    document.addEventListener('visibilitychange', () => { if (document.hidden) pause(); });
    update(Number(slider.value));
  });
})();
