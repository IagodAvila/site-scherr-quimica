# -*- coding: utf-8 -*-
import io, os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paginas_conteudo import PAGES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://scherr.com.br'
ORG  = BASE + '/#organization'

# Descricao institucional unica, a mesma usada no Perfil da Empresa no Google.
ORG_DESC = (
    "A Scherr Química atua no tratamento de água industrial desde 1993 e tem sede em Nova Lima (MG). Fornecemos produtos químicos e assistência técnica para geradores de vapor (caldeiras), torres de resfriamento, água gelada, efluentes industriais, óleo combustível e sistemas de abrandamento e desmineralização. Temos laboratório químico próprio para análises de água e de depósito, contagem microbiológica e determinação de taxas de corrosão em corpos de prova. O atendimento inclui relatórios periódicos, inspeções, limpezas químicas em caldeiras, trocadores de calor e torres, e equipamentos de dosagem em comodato. Empresa certificada NSF e ganhadora do Prêmio Fornecedores Vale na categoria Meio Ambiente."
)

def esc(t):
    return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

HEADER = '''<header class="sticky top-0 z-50 border-b border-fio bg-papel/95 backdrop-blur">
  <div class="mx-auto flex h-16 max-w-6xl items-center justify-between px-5 sm:px-8">
    <a href="/" class="flex items-center" aria-label="Scherr Química - Início">
      <img src="/assets/logo-scherr-horizontal.png" alt="Scherr Química" width="738" height="220" class="h-11 w-auto" />
    </a>
    <nav class="hidden items-center gap-7 text-sm font-medium lg:flex">
      <a href="/#areas-atuacao" class="header-nav-link">Áreas de atuação</a>
      <a href="/#servicos" class="header-nav-link">Serviços</a>
      <a href="/#sobre" class="header-nav-link">Sobre</a>
      <a href="/#setores" class="header-nav-link">Setores</a>
      <a href="/#contato" class="header-nav-link">Contato</a>
    </nav>
    <a href="/#contato" class="acao acao-varre varre-escuro hidden bg-verde px-4 py-2 text-sm font-semibold text-white lg:inline-flex">Solicitar avaliação</a>
    <button id="mobileMenuButton" type="button" class="acao inline-flex h-10 w-10 items-center justify-center border border-fio-forte text-tinta hover:bg-superficie lg:hidden" aria-label="Abrir menu" aria-controls="mobileMenu" aria-expanded="false">
      <svg data-icone="abrir" class="icon h-5 w-5" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      <svg data-icone="fechar" class="icon h-5 w-5" viewBox="0 0 24 24" aria-hidden="true" hidden><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
  <div id="mobileMenu" class="border-t border-fio bg-papel lg:hidden" hidden>
    <nav class="mx-auto flex max-w-6xl flex-col px-5 sm:px-8">
      <a href="/#areas-atuacao" class="border-b border-fio py-4 font-medium">Áreas de atuação</a>
      <a href="/#servicos" class="border-b border-fio py-4 font-medium">Serviços</a>
      <a href="/#sobre" class="border-b border-fio py-4 font-medium">Sobre</a>
      <a href="/#setores" class="border-b border-fio py-4 font-medium">Setores</a>
      <a href="/#contato" class="border-b border-fio py-4 font-medium">Contato</a>
      <a href="/#contato" class="acao acao-varre varre-escuro my-4 bg-verde px-4 py-3 text-center font-semibold text-white">Solicitar avaliação</a>
    </nav>
  </div>
</header>'''

FOOTER_TPL = '''<footer class="bg-verde-fundo text-sobre-verde">
  <div class="mx-auto max-w-6xl px-5 py-14 sm:px-8">
    <div class="grid gap-10 md:grid-cols-3">
      <div>
        <div class="inline-flex bg-white p-2"><img src="/assets/logo-scherr-horizontal.png" alt="Scherr Química" width="738" height="220" class="h-10 w-auto" /></div>
        <p class="mt-5 max-w-xs text-sm text-sobre-verde-dim">Tratamento de água industrial desde 1993. Sede em Nova Lima, MG.</p>
      </div>
      <div>
        <h2 class="font-mono text-xs text-sobre-verde-dim">ÁREAS DE ATUAÇÃO</h2>
        <ul class="mt-4 grid gap-2 text-sm">
{footer_links}
        </ul>
      </div>
      <div>
        <h2 class="font-mono text-xs text-sobre-verde-dim">CONTATO</h2>
        <ul class="mt-4 grid gap-2 text-sm">
          <li><a href="mailto:scherr@scherr.com.br" class="hover:text-verde-claro">scherr@scherr.com.br</a></li>
          <li><a href="tel:+5531992247394" class="hover:text-verde-claro">+55 (31) 99224-7394</a></li>
          <li><a href="tel:+5531992064484" class="hover:text-verde-claro">+55 (31) 99206-4484</a></li>
          <li class="text-sobre-verde-dim">Av. Canadá, 283 — Nova Lima, MG</li>
        </ul>
      </div>
    </div>
    <p class="mt-12 border-t border-white/15 pt-6 text-sm text-sobre-verde-dim">© <span id="year"></span> Scherr Química Ltda. Todos os direitos reservados.</p>
  </div>
</footer>'''

WHATSAPP = '''<a href="https://wa.me/5531992247394?text=Olá%20gostaria%20de%20mais%20informações%20sobre%20os%20serviços%20da%20Scherr%20Química." target="_blank" rel="noopener noreferrer" class="acao fixed bottom-[calc(1rem+env(safe-area-inset-bottom))] right-4 z-[100] flex h-12 w-12 items-center justify-center rounded-full bg-verde text-white shadow-lg hover:bg-verde-fundo sm:bottom-6 sm:right-6 sm:h-14 sm:w-14" aria-label="Falar pelo WhatsApp">
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
       "description": ORG_DESC,
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
      '''      <div class="linha-spec border-b border-fio py-5">
        <dt class="text-lg font-semibold">%s</dt>
        <dd class="mt-2 max-w-medida text-sm text-aco">%s</dd>
      </div>''' % (esc(t), esc(d)) for t, d in page['problem_items'])

    how_steps = '\n'.join(
      '''      <li class="linha-spec grid grid-cols-[36px_minmax(0,1fr)] gap-x-4 border-b border-fio py-5">
        <span class="font-mono text-xs text-verde-texto">%02d</span>
        <span>
          <span class="block text-lg font-semibold">%s</span>
          <span class="mt-2 block max-w-medida text-sm text-aco">%s</span>
        </span>
      </li>''' % (i + 1, esc(t), esc(d)) for i, (t, d) in enumerate(page['how_items']))

    prod_lis = '\n'.join(
      '          <li class="border-b border-fio py-3 text-sm">%s</li>' % esc(i)
      for i in page['prod_items'])

    result_cards = '\n'.join(
      '''      <div class="linha-spec border-b border-fio py-5">
        <dt class="font-semibold">%s</dt>
        <dd class="mt-2 text-sm text-aco">%s</dd>
      </div>''' % (esc(t), esc(d)) for t, d in page['results_items'])

    faq_items = '\n'.join(
      '''      <details class="group border-b border-fio py-5">
        <summary class="flex cursor-pointer list-none items-start justify-between gap-4 text-lg font-semibold">
          <span>%s</span>
          <svg class="icon mt-1.5 h-4 w-4 shrink-0 text-verde-texto transition-transform group-open:rotate-180" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
        </summary>
        <p class="mt-3 max-w-medida text-sm text-aco">%s</p>
      </details>''' % (esc(q), esc(a)) for q, a in page['faq'])

    related = '\n'.join(
      '''      <a href="/%s/" class="linha-area group grid grid-cols-[52px_minmax(0,1fr)] items-baseline gap-x-5 border-b border-fio py-5 sm:grid-cols-[64px_minmax(0,1fr)]">
        <span class="cod font-mono text-xs text-verde-texto">%s</span>
        <span>
          <span class="block text-lg font-semibold group-hover:text-verde-texto">%s</span>
          <span class="mt-1 block max-w-medida text-sm text-aco">%s</span>
        </span>
      </a>''' % (o['slug'], o['cod'], esc(o['h1']), esc(o['params'])) for o in others)

    footer_links = '\n'.join(
      '          <li><a href="/%s/" class="link-desliza hover:text-verde-claro">%s</a></li>' % (q['slug'], esc(q['nav']))
      for q in PAGES)

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
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" media="print" onload="this.media=\'all\'" />
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" /></noscript>
<link rel="stylesheet" href="/assets/app.css?v=20260903-motion2" />
<link rel="stylesheet" href="/style.css?v=20260903-motion2" />
</head>
<body class="bg-papel text-tinta">

<a href="#conteudo" class="sr-only focus:not-sr-only focus:absolute focus:z-[200] focus:m-3 focus:bg-tinta focus:px-4 focus:py-2 focus:text-sobre-verde">Pular para o conteúdo</a>

{header}

<main id="conteudo">

<section id="topo" class="bg-verde-fundo">
  <div class="mx-auto max-w-6xl px-5 py-12 sm:px-8 sm:py-16">
    <nav aria-label="Você está aqui" class="text-xs text-sobre-verde-dim">
      <ol class="flex flex-wrap items-center gap-2">
        <li><a href="/" class="hover:text-verde-claro">Início</a></li>
        <li aria-hidden="true">/</li>
        <li><a href="/#areas-atuacao" class="hover:text-verde-claro">Áreas de atuação</a></li>
        <li aria-hidden="true">/</li>
        <li><span aria-current="page" class="text-sobre-verde">{nav}</span></li>
      </ol>
    </nav>
    <div class="mt-8 grid gap-10 lg:grid-cols-[minmax(0,520px)_minmax(0,1fr)] lg:items-center lg:gap-14">
      <div>
        <p class="font-mono text-xs text-verde-claro">{cod}</p>
        <h1 class="entra mt-3 text-3xl font-bold text-sobre-verde sm:text-4xl">{h1}</h1>
        <p class="entra entra-2 mt-5 max-w-medida text-base text-sobre-verde-dim">{lead}</p>
        <div class="entra entra-3 mt-8 flex flex-wrap gap-3">
          <a href="/#contato" class="acao acao-varre varre-verde bg-white px-5 py-3 font-semibold text-verde-fundo">Solicitar avaliação técnica</a>
          <a href="https://wa.me/5531992247394" target="_blank" rel="noopener noreferrer" class="acao acao-contorno border border-sobre-verde-dim/50 px-5 py-3 font-semibold text-sobre-verde">Falar com um técnico</a>
        </div>
        <p class="mt-8 font-mono text-xs text-sobre-verde-dim">PARÂMETROS DE CONTROLE · {params}</p>
      </div>
      <div class="zoom-suave entra entra-4"><img src="/assets/{img}" alt="{img_alt}" width="{img_w}" height="{img_h}" fetchpriority="high" class="h-56 w-full object-cover sm:h-72 lg:h-80" /></div>
    </div>
  </div>
</section>

<section id="problema" class="mx-auto max-w-6xl px-5 py-16 sm:px-8 sm:py-20">
  <h2 class="max-w-medida text-2xl font-bold">{problem_h2}</h2>
  <p class="mt-4 max-w-medida text-aco">{problem_p}</p>
  <dl class="mt-10 grid border-t-[3px] border-verde md:grid-cols-2 md:gap-x-12">
{problem_cards}
  </dl>
</section>

<section id="como-tratamos" class="border-t border-fio bg-superficie">
  <div class="mx-auto max-w-6xl px-5 py-16 sm:px-8 sm:py-20">
    <h2 class="max-w-medida text-2xl font-bold">{how_h2}</h2>
    <ol class="mt-10 grid border-t-[3px] border-verde md:grid-cols-2 md:gap-x-12">
{how_steps}
    </ol>
  </div>
</section>

<section id="produtos" class="border-t border-fio">
  <div class="mx-auto grid max-w-6xl gap-12 px-5 py-16 sm:px-8 sm:py-20 lg:grid-cols-2 lg:gap-16">
    <div>
      <h2 class="max-w-medida text-2xl font-bold">{prod_h2}</h2>
      <ul class="mt-8 border-t-[3px] border-verde">
{prod_lis}
      </ul>
    </div>
    <div>
      <h2 class="max-w-medida text-2xl font-bold">O que acompanha o fornecimento</h2>
      <ul class="mt-8 border-t-[3px] border-verde text-sm">
        <li class="border-b border-fio py-3">Análises de água, de depósito e contagem microbiológica em laboratório próprio</li>
        <li class="border-b border-fio py-3">Taxas de corrosão e deposição em corpos de prova de aço carbono, ligas de cobre e admiralty</li>
        <li class="border-b border-fio py-3">Relatórios periódicos de avaliação e inspeções com registro fotográfico</li>
        <li class="border-b border-fio py-3">Tanques, bombas dosadoras e descargas automáticas em regime de comodato</li>
        <li class="border-b border-fio py-3">Montagem de laboratório na planta, com aparelhagem e analista</li>
        <li class="border-b border-fio py-3">Transporte de produto e de pessoal operacional e técnico</li>
      </ul>
      <a href="/#servicos" class="mt-6 inline-block font-semibold text-verde-texto hover:underline">Ver todos os serviços</a>
    </div>
  </div>
</section>

<section id="resultados" class="border-t border-fio bg-superficie">
  <div class="mx-auto max-w-6xl px-5 py-16 sm:px-8 sm:py-20">
    <h2 class="max-w-medida text-2xl font-bold">O que o programa entrega na operação</h2>
    <dl class="mt-10 grid border-t-[3px] border-verde md:grid-cols-2 md:gap-x-12">
{result_cards}
    </dl>
  </div>
</section>

<section id="faq" class="border-t border-fio">
  <div class="mx-auto max-w-3xl px-5 py-16 sm:px-8 sm:py-20">
    <h2 class="text-2xl font-bold">Perguntas sobre {frase}</h2>
    <div class="mt-10 border-t-[3px] border-verde">
{faq_items}
    </div>
  </div>
</section>

<section id="outras-areas" class="border-t border-fio bg-superficie">
  <div class="mx-auto max-w-6xl px-5 py-16 sm:px-8 sm:py-20">
    <h2 class="max-w-medida text-2xl font-bold">Outras áreas de atuação</h2>
    <div class="lista-areas mt-10 border-t-[3px] border-verde">
{related}
    </div>
  </div>
</section>

<section id="orcamento" class="bg-verde-fundo">
  <div class="mx-auto max-w-6xl px-5 py-16 sm:px-8 sm:py-20">
    <h2 class="max-w-medida text-2xl font-bold text-sobre-verde">Precisa de {frase} na sua planta?</h2>
    <p class="mt-4 max-w-medida text-sobre-verde-dim">Nossa equipe técnica avalia o seu sistema e apresenta o programa químico adequado. Atendemos indústrias em Minas Gerais desde 1993. Nossa sede fica em Nova Lima.</p>
    <div class="mt-8 flex flex-wrap gap-3">
      <a href="/#contato" class="acao acao-varre varre-verde bg-white px-5 py-3 font-semibold text-verde-fundo">Solicitar avaliação técnica</a>
      <a href="tel:+5531992247394" class="acao acao-contorno border border-sobre-verde-dim/50 px-5 py-3 font-semibold text-sobre-verde">+55 (31) 99224-7394</a>
    </div>
  </div>
</section>
</main>

{footer}

<script defer src="/script.js?v=20260903-verde"></script>
{whatsapp}
</body>
</html>
'''.format(
    title=esc(page['title']), desc=esc(page['desc']), url=url, base=BASE,
    img=page['img'], img_alt=esc(page['img_alt']),
    img_w=DIMS[page['img']][0], img_h=DIMS[page['img']][1],
    ld=json.dumps(ld, ensure_ascii=False, indent=2),
    header=HEADER, nav=esc(page['nav']), frase=esc(page['frase']),
    cod=page['cod'], params=esc(page['params']),
    h1=esc(page['h1']), lead=esc(page['lead']),
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
