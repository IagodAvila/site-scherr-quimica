const yearElement = document.getElementById("year");
if (yearElement) {
  yearElement.textContent = new Date().getFullYear();
}

const mobileMenuButton = document.getElementById("mobileMenuButton");
const mobileMenu = document.getElementById("mobileMenu");

if (mobileMenuButton && mobileMenu) {
  const setMobileMenuOpen = (isOpen) => {
    mobileMenu.classList.toggle("hidden", !isOpen);
    mobileMenuButton.setAttribute("aria-expanded", String(isOpen));
    mobileMenuButton.setAttribute("aria-label", isOpen ? "Fechar menu" : "Abrir menu");

    const icon = mobileMenuButton.querySelector("[data-lucide]");
    if (icon) {
      icon.setAttribute("data-lucide", isOpen ? "x" : "menu");
      if (window.lucide) {
        lucide.createIcons();
      }
    }
  };

  mobileMenuButton.addEventListener("click", () => {
    setMobileMenuOpen(mobileMenu.classList.contains("hidden"));
  });

  mobileMenu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => setMobileMenuOpen(false));
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth >= 1024) {
      setMobileMenuOpen(false);
    }
  });
}

const contactForm = document.getElementById("contactForm");
if (contactForm) {
  const feedback = document.getElementById("formMsg");

  const showFeedback = (text, tone) => {
    feedback.textContent = text;
    feedback.classList.remove("hidden", "text-muted-foreground", "text-red-600");
    feedback.classList.add(tone === "error" ? "text-red-600" : "text-muted-foreground");
  };

  contactForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const form = event.target;
    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const phone = form.phone.value.trim();
    const message = form.message.value.trim();

    if (!name || !email || !message) {
      showFeedback("Preencha todos os campos obrigatórios.", "error");
      return;
    }

    const subject = encodeURIComponent(`Contato do site - ${name}`);
    const body = encodeURIComponent(`Nome: ${name}\nEmail: ${email}\nTelefone: ${phone}\n\n${message}`);

    window.location.href = `mailto:scherr@scherr.com.br?subject=${subject}&body=${body}`;
    showFeedback("Abrindo seu cliente de email...", "info");
  });
}

if (window.lucide) {
  lucide.createIcons();
}
