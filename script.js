const services = [
  { icon: "flame", title: "Tratamento de Água de Geradores de Vapor", desc: "Tratamento completo da água de caldeiras — externo, interno e da rede de vapor condensado — com ganho de eficiência e economia de combustível." },
  { icon: "droplets", title: "Tratamento de Água Clarificada", desc: "Otimização da troca térmica, maximização dos ciclos de concentração e proteção contra incrustação e corrosão em torres de resfriamento." },
  { icon: "droplets", title: "Tratamento de Água e Resfriamento", desc: "Soluções completas em produtos químicos e assistência técnica para tratamento de água industrial, resfriamento e geração de água gelada. Protegemos seus equipamentos contra incrustação, corrosão e deposição." },
  { icon: "wrench", title: "Tratamento de Efluentes Industriais", desc: "Coagulantes, floculantes e polímeros para tratamento físico-químico de efluentes industriais com foco ambiental." },
  { icon: "fuel", title: "Tratamento de Óleo e Combustível", desc: "Linha completa para tratamento de óleo combustível e equipe técnica preparada para indicar o produto ideal para cada caso." },
  { icon: "flask-conical", title: "Abrandadores e Desmineralizadores", desc: "Produtos e suporte técnico para sistemas de abrandamento, desmineralização e geração de água de alta pureza." },
];

const testimonials = [
  { name: "Carlos Mendes", role: "Gerente Industrial", text: "A Scherr Acqua transformou nossa operação. Os produtos são de alta qualidade e o atendimento técnico é excepcional. Reduzimos custos com manutenção das caldeiras significativamente." },
  { name: "Patrícia Souza", role: "Engenheira de Processos", text: "Parceria de anos. A equipe está sempre pronta para nos atender, com profissionais altamente qualificados e produtos que realmente entregam o resultado prometido." },
  { name: "Roberto Almeida", role: "Diretor de Operações", text: "Recomendo fortemente. O acompanhamento técnico em campo e o laboratório próprio fazem toda a diferença. Nossos sistemas nunca operaram tão bem." },
];

const svcGrid = document.getElementById("services-grid");
services.forEach(s => {
  const el = document.createElement("div");
  el.className = "group bg-card border border-border rounded-2xl p-6 shadow-card hover:shadow-elegant hover:-translate-y-1 transition-all duration-300";
  el.innerHTML = `
    <div class="grid place-items-center h-12 w-12 rounded-xl bg-primary/10 text-primary group-hover:bg-primary group-hover:text-white transition-colors">
      <i data-lucide="${s.icon}" class="icon" style="font-size:1.5rem"></i>
    </div>
    <h3 class="mt-5 text-lg font-semibold">${s.title}</h3>
    <p class="mt-2 text-sm text-muted-foreground leading-relaxed">${s.desc}</p>`;
  svcGrid.appendChild(el);
});

const tGrid = document.getElementById("testimonials-grid");
testimonials.forEach(t => {
  const el = document.createElement("div");
  el.className = "bg-card border border-border rounded-2xl p-6 shadow-card";
  el.innerHTML = `
    <div class="flex gap-1 text-primary">
      ${'<i data-lucide="star" class="icon" style="fill:currentColor"></i>'.repeat(5)}
    </div>
    <p class="mt-4 text-muted-foreground leading-relaxed">"${t.text}"</p>
    <div class="mt-6 pt-4 border-t border-border">
      <div class="font-semibold">${t.name}</div>
      <div class="text-sm text-muted-foreground">${t.role}</div>
    </div>`;
  tGrid.appendChild(el);
});

document.getElementById("year").textContent = new Date().getFullYear();

document.getElementById("contactForm").addEventListener("submit", (e) => {
  e.preventDefault();
  const f = e.target;
  const name = f.name.value.trim();
  const email = f.email.value.trim();
  const phone = f.phone.value.trim();
  const message = f.message.value.trim();
  const msg = document.getElementById("formMsg");
  if (!name || !email || !message) {
    msg.textContent = "Preencha todos os campos obrigatórios.";
    msg.classList.remove("hidden");
    return;
  }
  const subject = encodeURIComponent(`Contato do site - ${name}`);
  const body = encodeURIComponent(`Nome: ${name}\nEmail: ${email}\nTelefone: ${phone}\n\n${message}`);
  window.location.href = `mailto:scherr@scherr.com.br?subject=${subject}&body=${body}`;
  msg.textContent = "Abrindo seu cliente de email...";
  msg.classList.remove("hidden");
});

if (window.lucide) lucide.createIcons();
