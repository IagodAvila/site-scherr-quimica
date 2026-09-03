# -*- coding: utf-8 -*-
import io, os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paginas_conteudo import PAGES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://scherr.com.br'
ORG  = BASE + '/#organization'

def esc(t):
    return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

HEADER = '''<header class="sticky top-0 z-50 bg-white/85 backdrop-blur border-b border-border">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
    <a href="/" class="flex items-center gap-2" aria-label="Scherr Química - Início">
      <img src="/assets/logo-scherr-horizontal.png" alt="Scherr Química" width="738" height="220" class="h-14 w-auto" />
    </a>
    <nav class="hidden lg:flex items-center gap-8 text-base font-bold">
      <a href="/#areas-atuacao" class="header-nav-link hover:text-primary">Áreas de Atuação</a>
      <a href="/#servicos" class="header-nav-link hover:text-primary">Serviços</a>
      <a href="/#sobre" class="header-nav-link hover:text-primary">Sobre</a>
      <a href="/#parceiros" class="header-nav-link hover:text-primary">Parceiros</a>
      <a href="/#contato" class="header-nav-link hover:text-primary">Contato</a>
    </nav>
    <a href="/#contato" class="button-zoom hidden lg:inline-flex items-center px-4 py-2 rounded-lg bg-primary text-primary-foreground text-sm font-semibold hover:opacity-90 transition">Fale Conosco</a>
    <button id="mobileMenuButton" type="button" class="button-zoom lg:hidden inline-flex h-10 w-10 items-center justify-center rounded-lg border border-border bg-background text-foreground transition hover:bg-accent" aria-label="Abrir menu" aria-controls="mobileMenu" aria-expanded="false">
      <i data-lucide="menu" class="icon"></i>
    </button>
  </div>
  <div id="mobileMenu" class="hidden border-t border-border bg-white lg:hidden">
    <nav class="mx-auto flex max-w-7xl flex-col gap-1 px-4 py-4 text-base font-semibold sm:px-6">
      <a href="/#areas-atuacao" class="rounded-lg px-3 py-3 transition hover:bg-accent hover:text-primary">Áreas de Atuação</a>
      <a href="/#servicos" class="rounded-lg px-3 py-3 transition hover:bg-accent hover:text-primary">Serviços</a>
      <a href="/#sobre" class="rounded-lg px-3 py-3 transition hover:bg-accent hover:text-primary">Sobre</a>
      <a href="/#parceiros" class="rounded-lg px-3 py-3 transition hover:bg-accent hover:text-primary">Parceiros</a>
      <a href="/#contato" class="rounded-lg px-3 py-3 transition hover:bg-accent hover:text-primary">Contato</a>
      <a href="/#contato" class="button-zoom mt-2 inline-flex items-center justify-center rounded-lg bg-primary px-4 py-3 text-sm font-semibold text-primary-foreground transition hover:opacity-90">Fale Conosco</a>
    </nav>
  </div>
</header>'''

FOOTER_TPL = '''<footer class="bg-foreground text-white py-12">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div class="grid md:grid-cols-3 gap-8">
      <div class="text-center">
        <div class="bg-white inline-flex p-2 rounded-lg"><img src="/assets/logo-scherr-horizontal.png" alt="Scherr Química" width="738" height="220" class="h-12 w-auto" /></div>
        <p class="mx-auto mt-4 max-w-xs text-sm opacity-70">Especialistas em tratamento de água industrial desde 1993. Nova Lima, MG.</p>
      </div>
      <div>
        <h2 class="font-semibold mb-3">Soluções</h2>
        <ul class="space-y-2 text-sm opacity-80">
{footer_links}
        </ul>
      </div>
      <div>
        <h2 class="font-semibold mb-3">Contato</h2>
        <div class="flex flex-col gap-2">
          <a href="mailto:scherr@scherr.com.br" class="inline-flex items-center gap-2 text-sm opacity-80 hover:opacity-100">
            <i data-lucide="mail" class="icon"></i>
            scherr@scherr.com.br
          </a>
          <a href="tel:+5531992247394" class="inline-flex items-center gap-2 text-sm opacity-80 hover:opacity-100">
            <i data-lucide="phone" class="icon"></i>
            +55 31 99224-7394
          </a>
          <a href="tel:+5531992064484" class="inline-flex items-center gap-2 text-sm opacity-80 hover:opacity-100">
            <i data-lucide="phone" class="icon"></i>
            +55 31 99206-4484
          </a>
          <a href="/#contato" class="inline-flex items-center gap-2 text-sm opacity-80 hover:opacity-100">
            <i data-lucide="map-pin" class="icon"></i>
            Av. Canadá, 283 - Nova Lima, MG
          </a>
        </div>
      </div>
    </div>
    <div class="mt-10 pt-6 border-t border-white/10 text-sm opacity-60 text-center">
      © <span id="year"></span> Scherr Química Ltda. Todos os direitos reservados.
    </div>
  </div>
</footer>'''

WHATSAPP = '''<a href="https://wa.me/5531992247394?text=Olá%20gostaria%20de%20mais%20informações%20sobre%20os%20serviços%20da%20Scherr%20Química." target="_blank" rel="noopener noreferrer" class="button-zoom fixed bottom-[calc(1rem+env(safe-area-inset-bottom))] right-4 z-[100] flex h-12 w-12 items-center justify-center rounded-full bg-[#25D366] text-white shadow-lg transition sm:bottom-6 sm:right-6 sm:h-14 sm:w-14" aria-label="Falar pelo WhatsApp">
  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 sm:h-7 sm:w-7" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
    <path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232"/>
  </svg>
</a>'''


# dimensoes reais dos arquivos em assets/ - width/height precisa bater com a imagem,
# senao o aspect-ratio informado ao navegador esta errado.
DIMS = {
    'hero-water-treatment.jpg':    (1400, 933),
    'services-lab-testing.jpg':    (1600, 480),
    'partners-water-drop.jpg':     (1600, 640),
    'about-industrial-valves.jpg': (1200, 900),
}

def build(page, others):
    url = '%s/%s/' % (BASE, page['slug'])

    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": ["LocalBusiness", "ProfessionalService"], "@id": ORG,
       "name": "Scherr Química Ltda", "alternateName": "Scherr", "url": BASE + "/",
       "image": BASE + "/assets/logo-scherr-horizontal.png",
       "logo": BASE + "/assets/logo-scherr-horizontal.png",
       "telephone": "+55 31 3297-6161", "email": "scherr@scherr.com.br",
       "foundingDate": "1993",
       "address": {"@type": "PostalAddress", "streetAddress": "Av. Canadá, 283",
                   "addressLocality": "Nova Lima", "addressRegion": "MG", "addressCountry": "BR"},
       "areaServed": [{"@type": "AdministrativeArea", "name": "Minas Gerais"},
                      {"@type": "Country", "name": "Brasil"}]},
      {"@type": "WebPage", "@id": url + "#webpage", "url": url,
       "name": page['title'], "description": page['desc'], "inLanguage": "pt-BR",
       "isPartOf": {"@id": BASE + "/#website"},
       "breadcrumb": {"@id": url + "#breadcrumb"}, "about": {"@id": url + "#service"}},
      {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Áreas de Atuação", "item": BASE + "/#areas-atuacao"},
        {"@type": "ListItem", "position": 3, "name": page['nav'], "item": url}]},
      {"@type": "Service", "@id": url + "#service", "name": page['service_name'],
       "serviceType": page['service_name'], "description": page['lead'],
       "url": url, "provider": {"@id": ORG},
       "areaServed": [{"@type": "AdministrativeArea", "name": "Minas Gerais"},
                      {"@type": "Country", "name": "Brasil"}],
       "hasOfferCatalog": {"@type": "OfferCatalog", "name": page['prod_h2'],
         "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Product", "name": i}}
                             for i in page['prod_items']]}},
      {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in page['faq']]},
    ]}

    problem_cards = '\n'.join(
      '''      <article class="bg-card border border-border rounded-2xl p-6 shadow-card">
        <h3 class="text-lg font-semibold">%s</h3>
        <p class="mt-2 text-sm text-muted-foreground leading-relaxed">%s</p>
      </article>''' % (esc(t), esc(d)) for t, d in page['problem_items'])

    how_steps = '\n'.join(
      '''      <li class="bg-card border border-border rounded-2xl p-6 shadow-card">
        <div class="grid place-items-center h-9 w-9 rounded-lg bg-primary/10 text-primary font-bold text-sm">%d</div>
        <h3 class="mt-4 text-lg font-semibold">%s</h3>
        <p class="mt-2 text-sm text-muted-foreground leading-relaxed">%s</p>
      </li>''' % (i + 1, esc(t), esc(d)) for i, (t, d) in enumerate(page['how_items']))

    prod_lis = '\n'.join(
      '          <li class="flex items-start gap-3"><i data-lucide="check-circle-2" class="icon text-primary mt-1 shrink-0"></i><span>%s</span></li>' % esc(i)
      for i in page['prod_items'])

    result_cards = '\n'.join(
      '''      <div class="bg-secondary/50 rounded-2xl p-6">
        <h3 class="font-semibold">%s</h3>
        <p class="mt-2 text-sm text-muted-foreground leading-relaxed">%s</p>
      </div>''' % (esc(t), esc(d)) for t, d in page['results_items'])

    faq_items = '\n'.join(
      '''      <details class="group bg-card border border-border rounded-2xl p-6 shadow-card">
        <summary class="cursor-pointer list-none font-semibold flex items-start justify-between gap-4">
          <span>%s</span>
          <i data-lucide="chevron-down" class="icon shrink-0 mt-1 text-primary transition-transform group-open:rotate-180"></i>
        </summary>
        <p class="mt-3 text-muted-foreground leading-relaxed">%s</p>
      </details>''' % (esc(q), esc(a)) for q, a in page['faq'])

    related = '\n'.join(
      '''      <a href="/%s/" class="group bg-card border border-border rounded-2xl p-6 shadow-card hover:shadow-elegant hover:-translate-y-1 transition-all duration-300">
        <div class="grid place-items-center h-11 w-11 rounded-xl bg-primary/10 text-primary group-hover:bg-primary group-hover:text-white transition-colors">
          <i data-lucide="%s" class="icon" style="font-size:1.375rem"></i>
        </div>
        <h3 class="mt-4 font-semibold">%s</h3>
        <span class="mt-3 inline-flex items-center gap-1.5 text-sm font-semibold text-primary">Ver página <i data-lucide="arrow-right" class="icon transition-transform group-hover:translate-x-1"></i></span>
      </a>''' % (o['slug'], o['icon'], esc(o['h1'])) for o in others)

    footer_links = '\n'.join(
      '          <li><a href="/%s/" class="hover:opacity-100 transition">%s</a></li>' % (p['slug'], esc(p['nav']))
      for p in PAGES)

    return '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<meta name="author" content="Scherr Química Ltda" />
<link rel="canonical" href="{url}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="{base}/assets/{img}" />
<meta property="og:image:alt" content="{img_alt}" />
<meta property="og:site_name" content="Scherr Química" />
<meta property="og:locale" content="pt_BR" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{desc}" />
<meta name="twitter:image" content="{base}/assets/{img}" />
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg" />
<link rel="icon" type="image/png" href="/assets/favicon-32x32.png" sizes="32x32" />
<link rel="icon" type="image/png" href="/assets/favicon-16x16.png" sizes="16x16" />
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />
<link rel="manifest" href="/site.webmanifest" />
<script type="application/ld+json">
{ld}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" media="print" onload="this.media='all'" />
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" /></noscript>
<link rel="stylesheet" href="/assets/app.css" />
<link rel="stylesheet" href="/style.css" />
</head>
<body class="bg-background text-foreground">

{header}

<main>
<!-- Hero -->
<section id="topo" class="relative overflow-hidden bg-secondary/40">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-10 sm:py-14 lg:py-20">
    <nav aria-label="Você está aqui" class="mb-6 text-sm text-muted-foreground">
      <ol class="flex flex-wrap items-center gap-2">
        <li><a href="/" class="hover:text-primary transition">Início</a></li>
        <li aria-hidden="true">/</li>
        <li><a href="/#areas-atuacao" class="hover:text-primary transition">Áreas de Atuação</a></li>
        <li aria-hidden="true">/</li>
        <li><span aria-current="page" class="text-foreground font-medium">{nav}</span></li>
      </ol>
    </nav>
    <div class="grid lg:grid-cols-2 gap-10 lg:gap-12 items-center">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-accent text-accent-foreground text-xs font-semibold mb-5">
          <i data-lucide="{icon}" class="icon"></i> Áreas de Atuação
        </div>
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight leading-[1.15]">{h1}</h1>
        <p class="mt-6 text-lg text-muted-foreground max-w-xl leading-relaxed">{lead}</p>
        <div class="mt-8 flex flex-wrap gap-4">
          <a href="/#contato" class="button-zoom inline-flex items-center gap-2 px-6 py-3 rounded-lg bg-primary text-primary-foreground font-semibold shadow-elegant hover:opacity-90 transition">
            Solicite um Orçamento <i data-lucide="send" class="icon"></i>
          </a>
          <a href="https://wa.me/5531992247394" target="_blank" rel="noopener noreferrer" class="button-zoom inline-flex items-center gap-2 px-6 py-3 rounded-lg border border-border bg-background font-semibold hover:bg-accent transition">
            Falar com um técnico
          </a>
        </div>
      </div>
      <div class="rounded-2xl overflow-hidden shadow-elegant">
        <img src="/assets/{img}" alt="{img_alt}" width="{img_w}" height="{img_h}" fetchpriority="high" class="w-full h-56 sm:h-72 lg:h-80 object-cover" />
      </div>
    </div>
  </div>
</section>

<!-- Problema -->
<section id="problema" class="py-16 sm:py-20">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mb-10">
      <h2 class="text-2xl sm:text-3xl font-bold">{problem_h2}</h2>
      <p class="mt-4 text-muted-foreground leading-relaxed">{problem_p}</p>
    </div>
    <div class="grid md:grid-cols-2 gap-6">
{problem_cards}
    </div>
  </div>
</section>

<!-- Como tratamos -->
<section id="como-tratamos" class="py-16 sm:py-20 bg-secondary/40">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mb-10">
      <p class="text-sm font-semibold text-primary uppercase tracking-wider mb-2">Metodologia</p>
      <h2 class="text-2xl sm:text-3xl font-bold">{how_h2}</h2>
    </div>
    <ol class="grid md:grid-cols-2 gap-6">
{how_steps}
    </ol>
  </div>
</section>

<!-- Produtos -->
<section id="produtos" class="py-16 sm:py-20">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 grid lg:grid-cols-2 gap-10 lg:gap-12">
    <div>
      <p class="text-sm font-semibold text-primary uppercase tracking-wider mb-2">Produtos</p>
      <h2 class="text-2xl sm:text-3xl font-bold">{prod_h2}</h2>
      <ul class="mt-6 space-y-3 text-muted-foreground leading-relaxed">
{prod_lis}
      </ul>
    </div>
    <div class="bg-card border border-border rounded-2xl p-6 sm:p-8 shadow-card self-start">
      <h2 class="text-xl font-semibold">O que está incluso no atendimento</h2>
      <ul class="mt-5 space-y-3 text-sm text-muted-foreground leading-relaxed">
        <li class="flex items-start gap-3"><i data-lucide="flask-conical" class="icon text-primary mt-1 shrink-0"></i><span>Análises de água, análises de depósito e contagem microbiológica em laboratório químico próprio</span></li>
        <li class="flex items-start gap-3"><i data-lucide="activity" class="icon text-primary mt-1 shrink-0"></i><span>Determinação das taxas de corrosão e deposição em corpos de prova de aço carbono, ligas de cobre e admiralty</span></li>
        <li class="flex items-start gap-3"><i data-lucide="file-text" class="icon text-primary mt-1 shrink-0"></i><span>Relatórios periódicos de avaliação do tratamento e inspeções com registros fotográficos e filmagens</span></li>
        <li class="flex items-start gap-3"><i data-lucide="wrench" class="icon text-primary mt-1 shrink-0"></i><span>Tanques de dosagem e de estocagem, bombas dosadoras, drenos e descargas automáticas em regime de comodato</span></li>
        <li class="flex items-start gap-3"><i data-lucide="microscope" class="icon text-primary mt-1 shrink-0"></i><span>Montagem de laboratório na planta, com infraestrutura, aparelhagem e analista</span></li>
        <li class="flex items-start gap-3"><i data-lucide="truck" class="icon text-primary mt-1 shrink-0"></i><span>Transporte de produtos e de pessoal operacional e técnico</span></li>
      </ul>
      <a href="/#servicos" class="mt-6 inline-flex items-center gap-2 text-sm font-semibold text-primary hover:underline">
        Ver todos os serviços <i data-lucide="arrow-right" class="icon"></i>
      </a>
    </div>
  </div>
</section>

<!-- Resultados -->
<section id="resultados" class="py-16 sm:py-20 bg-secondary/40">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mb-10">
      <p class="text-sm font-semibold text-primary uppercase tracking-wider mb-2">Resultados</p>
      <h2 class="text-2xl sm:text-3xl font-bold">O que o programa entrega na operação</h2>
    </div>
    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
{result_cards}
    </div>
  </div>
</section>

<!-- FAQ -->
<section id="faq" class="py-16 sm:py-20">
  <div class="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
    <div class="mb-10">
      <p class="text-sm font-semibold text-primary uppercase tracking-wider mb-2">Dúvidas frequentes</p>
      <h2 class="text-2xl sm:text-3xl font-bold">Perguntas sobre {frase}</h2>
    </div>
    <div class="space-y-4">
{faq_items}
    </div>
  </div>
</section>

<!-- Outras áreas -->
<section id="outras-areas" class="py-16 sm:py-20 bg-secondary/40">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mb-10">
      <p class="text-sm font-semibold text-primary uppercase tracking-wider mb-2">Outras áreas de atuação</p>
      <h2 class="text-2xl sm:text-3xl font-bold">Soluções completas em tratamento de água industrial</h2>
    </div>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
{related}
    </div>
  </div>
</section>

<!-- CTA -->
<section id="orcamento" class="py-16 sm:py-20">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div class="relative rounded-2xl overflow-hidden shadow-elegant bg-gradient-hero p-8 sm:p-12 text-primary-foreground">
      <h2 class="text-2xl sm:text-3xl font-bold max-w-2xl">Precisa de {frase} na sua planta?</h2>
      <p class="mt-4 max-w-2xl opacity-95 leading-relaxed">Nossa equipe técnica avalia o seu sistema e apresenta o programa químico adequado. Atendemos indústrias em Minas Gerais desde 1993, a partir de Nova Lima.</p>
      <div class="mt-8 flex flex-wrap gap-4">
        <a href="/#contato" class="button-zoom inline-flex items-center gap-2 px-6 py-3 rounded-lg bg-white text-primary font-semibold hover:opacity-90 transition">
          Solicite um Orçamento <i data-lucide="send" class="icon"></i>
        </a>
        <a href="tel:+5531992247394" class="button-zoom inline-flex items-center gap-2 px-6 py-3 rounded-lg border border-white/40 font-semibold hover:bg-white/10 transition">
          <i data-lucide="phone" class="icon"></i> +55 (31) 99224-7394
        </a>
      </div>
    </div>
  </div>
</section>
</main>

{footer}

<script defer src="https://unpkg.com/lucide@1.28.0/dist/umd/lucide.min.js"></script>
<script defer src="/script.js?v=20260903-seo"></script>
{whatsapp}
</body>
</html>
'''.format(
    title=esc(page['title']), desc=esc(page['desc']), url=url, base=BASE,
    img=page['img'], img_alt=esc(page['img_alt']),
    img_w=DIMS[page['img']][0], img_h=DIMS[page['img']][1],
    ld=json.dumps(ld, ensure_ascii=False, indent=2),
    header=HEADER, nav=esc(page['nav']), frase=esc(page['frase']),
    icon=page['icon'], h1=esc(page['h1']), lead=esc(page['lead']),
    problem_h2=esc(page['problem_h2']), problem_p=esc(page['problem_p']),
    problem_cards=problem_cards, how_h2=esc(page['how_h2']), how_steps=how_steps,
    prod_h2=esc(page['prod_h2']), prod_lis=prod_lis, result_cards=result_cards,
    faq_items=faq_items, related=related,
    footer=FOOTER_TPL.format(footer_links=footer_links), whatsapp=WHATSAPP)


for page in PAGES:
    others = [p for p in PAGES if p['slug'] != page['slug']]
    html = build(page, others)
    d = os.path.join(ROOT, page['slug'])
    os.makedirs(d, exist_ok=True)
    io.open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(html)
    import re
    words = len(re.sub(r'<script.*?</script>', ' ', html, flags=re.S).replace('<', ' <').split())
    print('%-46s %6d bytes' % (page['slug'] + '/index.html', len(html)))
