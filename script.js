const services = [
  { icon: "flame", title: "Tratamento de Água de Geradores de Vapor", desc: "Tratamento completo da água de caldeiras — externo, interno e da rede de vapor condensado — com ganho de eficiência e economia de combustível." },
  { icon: "droplets", title: "Tratamento de Água Clarificada", desc: "Otimização da troca térmica, maximização dos ciclos de concentração e proteção contra incrustação e corrosão em torres de resfriamento." },
  { icon: "droplets", title: "Tratamento de Água e Resfriamento", desc: "Soluções completas em produtos químicos e assistência técnica para tratamento de água industrial, resfriamento e geração de água gelada. Protegemos seus equipamentos contra incrustação, corrosão e deposição." },
  { icon: "wrench", title: "Tratamento de Efluentes Industriais", desc: "Coagulantes, floculantes e polímeros para tratamento físico-químico de efluentes industriais com foco ambiental." },
  { icon: "fuel", title: "Tratamento de Óleo e Combustível", desc: "Linha completa para tratamento de óleo combustível e equipe técnica preparada para indicar o produto ideal para cada caso." },
  { icon: "flask-conical", title: "Abrandadores e Desmineralizadores", desc: "Produtos e suporte técnico para sistemas de abrandamento, desmineralização e geração de água de alta pureza." },
];

const svcGrid = document.getElementById("services-grid");
if (svcGrid) {
  services.forEach((service) => {
    const card = document.createElement("div");
    card.className = "group bg-card border border-border rounded-2xl p-6 shadow-card hover:shadow-elegant hover:-translate-y-1 transition-all duration-300";
    card.innerHTML = `
      <div class="grid place-items-center h-12 w-12 rounded-xl bg-primary/10 text-primary group-hover:bg-primary group-hover:text-white transition-colors">
        <i data-lucide="${service.icon}" class="icon" style="font-size:1.5rem"></i>
      </div>
      <h3 class="mt-5 text-lg font-semibold">${service.title}</h3>
      <p class="mt-2 text-sm text-muted-foreground leading-relaxed">${service.desc}</p>`;
    svcGrid.appendChild(card);
  });
}

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
