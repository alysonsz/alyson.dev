// Progressive enhancement: content and disclosures work without JavaScript.
const year = document.querySelector('#year');
if (year) year.textContent = new Date().getFullYear();
const links = [...document.querySelectorAll('.topbar nav a')];
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      for (const link of links) {
        if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      }
    }
  }, {rootMargin: '-15% 0px -65% 0px', threshold: 0});
  document.querySelectorAll('#inicio, #trabalho, #trajetoria, #contato').forEach(section => observer.observe(section));
}
const previewToggle = document.querySelector('#preview-toggle');
previewToggle?.addEventListener('click', () => {
  const showCapture = previewToggle.getAttribute('aria-pressed') !== 'true';
  previewToggle.setAttribute('aria-pressed', String(showCapture));
  previewToggle.textContent = showCapture ? 'Ver site ao vivo' : 'Ver captura';
  document.querySelector('#landing-live').hidden = showCapture;
  document.querySelector('#landing-capture').hidden = !showCapture;
});
