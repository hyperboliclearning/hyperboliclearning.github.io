const outlineLinks = [...document.querySelectorAll('.sticky-outline a[href^="#"]')];
const outlineSections = outlineLinks.map(link => document.getElementById(link.hash.slice(1)));
let outlineFramePending = false;

function updateOutline() {
  let current = 0;
  outlineSections.forEach((section, index) => {
    if (section && section.getBoundingClientRect().top <= 130) current = index;
  });
  outlineLinks.forEach((link, index) => {
    if (index === current) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  });
  outlineFramePending = false;
}

if (outlineLinks.length) {
  window.addEventListener('scroll', () => {
    if (outlineFramePending) return;
    outlineFramePending = true;
    requestAnimationFrame(updateOutline);
  }, { passive: true });
  window.addEventListener('resize', updateOutline);
  window.addEventListener('load', updateOutline);
  updateOutline();
}
