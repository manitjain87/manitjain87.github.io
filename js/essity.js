// ── Scroll progress bar ───────────────────────────────────
const progressBar = document.getElementById('scroll-progress');
if (progressBar) {
  window.addEventListener('scroll', () => {
    const doc = document.documentElement;
    const pct = (doc.scrollTop / (doc.scrollHeight - doc.clientHeight)) * 100;
    progressBar.style.width = pct + '%';
  }, { passive: true });
}

// ── Active nav link via IntersectionObserver ──────────────
(function () {
  const navLinks = document.querySelectorAll('nav a[href^="#"]');
  const sections = document.querySelectorAll('section[id]');

  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        navLinks.forEach(a => a.classList.remove('active'));
        const active = document.querySelector(`nav a[href="#${e.target.id}"]`);
        if (active) active.classList.add('active');
      }
    });
  }, { rootMargin: '-35% 0px -60% 0px' });

  sections.forEach(s => io.observe(s));
})();

// ── Scroll reveal ─────────────────────────────────────────
(function () {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.08 });

  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
})();

// ── Writing section: drag-to-scroll + arrow buttons ───────
(function () {
  const row = document.getElementById('writing-scroll');
  const prevBtn = document.getElementById('scroll-prev');
  const nextBtn = document.getElementById('scroll-next');
  if (!row || !prevBtn || !nextBtn) return;

  const cardWidth = () => {
    const card = row.querySelector('.writing-card');
    if (!card) return 300;
    return card.offsetWidth + 16;
  };

  const updateButtons = () => {
    prevBtn.disabled = row.scrollLeft <= 4;
    nextBtn.disabled = row.scrollLeft >= row.scrollWidth - row.clientWidth - 4;
  };

  prevBtn.addEventListener('click', () => {
    row.scrollBy({ left: -cardWidth(), behavior: 'smooth' });
  });

  nextBtn.addEventListener('click', () => {
    row.scrollBy({ left: cardWidth(), behavior: 'smooth' });
  });

  row.addEventListener('scroll', updateButtons, { passive: true });
  updateButtons();

  // Drag to scroll
  let isDown = false;
  let startX = 0;
  let scrollStart = 0;

  row.addEventListener('mousedown', e => {
    isDown = true;
    row.classList.add('dragging');
    startX = e.pageX - row.offsetLeft;
    scrollStart = row.scrollLeft;
  });

  document.addEventListener('mouseup', () => {
    isDown = false;
    row.classList.remove('dragging');
  });

  row.addEventListener('mousemove', e => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - row.offsetLeft;
    row.scrollLeft = scrollStart - (x - startX);
  });

  // Suppress click after drag
  row.addEventListener('click', e => {
    if (Math.abs(row.scrollLeft - scrollStart) > 4) e.preventDefault();
  }, { capture: true });
})();
