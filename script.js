const yearElement = document.getElementById("year");
if (yearElement) {
  yearElement.textContent = new Date().getFullYear();
}

const mobileMenuButton = document.getElementById("mobileMenuButton");
const mobileMenu = document.getElementById("mobileMenu");

if (mobileMenuButton && mobileMenu) {
  const iconAbrir = mobileMenuButton.querySelector("[data-icone='abrir']");
  const iconFechar = mobileMenuButton.querySelector("[data-icone='fechar']");

  const setMobileMenuOpen = (isOpen) => {
    mobileMenu.hidden = !isOpen;
    mobileMenuButton.setAttribute("aria-expanded", String(isOpen));
    mobileMenuButton.setAttribute("aria-label", isOpen ? "Fechar menu" : "Abrir menu");
    if (iconAbrir) iconAbrir.hidden = isOpen;
    if (iconFechar) iconFechar.hidden = !isOpen;
  };

  mobileMenuButton.addEventListener("click", () => setMobileMenuOpen(mobileMenu.hidden));
  mobileMenu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => setMobileMenuOpen(false));
  });
  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !mobileMenu.hidden) {
      setMobileMenuOpen(false);
      mobileMenuButton.focus();
    }
  });
  window.addEventListener("resize", () => {
    if (window.innerWidth >= 1024) setMobileMenuOpen(false);
  });
}

const contactForm = document.getElementById("contactForm");
if (contactForm) {
  const feedback = document.getElementById("formMsg");

  const showFeedback = (text, tone) => {
    feedback.textContent = text;
    feedback.hidden = false;
    feedback.classList.remove("text-aco", "text-ambar");
    feedback.classList.add(tone === "error" ? "text-ambar" : "text-aco");
  };

  contactForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const form = event.target;
    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const phone = form.phone.value.trim();
    const message = form.message.value.trim();

    if (!name || !email || !message) {
      showFeedback("Preencha nome, email e mensagem para enviar.", "error");
      return;
    }

    const subject = encodeURIComponent(`Contato do site - ${name}`);
    const body = encodeURIComponent(`Nome: ${name}\nEmail: ${email}\nTelefone: ${phone}\n\n${message}`);
    window.location.href = `mailto:scherr@scherr.com.br?subject=${subject}&body=${body}`;
    showFeedback("Abrindo seu programa de email com a mensagem pronta.", "info");
  });
}
