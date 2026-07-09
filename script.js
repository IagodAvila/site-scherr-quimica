const yearElement = document.getElementById("year");
if (yearElement) {
  yearElement.textContent = new Date().getFullYear();
}

const contactForm = document.getElementById("contactForm");
if (contactForm) {
  contactForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const form = event.target;
    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const phone = form.phone.value.trim();
    const message = form.message.value.trim();
    const feedback = document.getElementById("formMsg");

    if (!name || !email || !message) {
      feedback.textContent = "Preencha todos os campos obrigatórios.";
      feedback.classList.remove("hidden");
      return;
    }

    const subject = encodeURIComponent(`Contato do site - ${name}`);
    const body = encodeURIComponent(`Nome: ${name}\nEmail: ${email}\nTelefone: ${phone}\n\n${message}`);

    window.location.href = `mailto:scherr@scherr.com.br?subject=${subject}&body=${body}`;
    feedback.textContent = "Abrindo seu cliente de email...";
    feedback.classList.remove("hidden");
  });
}

if (window.lucide) {
  lucide.createIcons();
}
