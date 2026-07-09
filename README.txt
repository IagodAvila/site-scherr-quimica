Site estático Scherr Acqua
==========================

Este pacote é 100% HTML/CSS/JavaScript puro — pode ser hospedado em
qualquer servidor comum (Apache, Nginx, hospedagem compartilhada,
GitHub Pages, Netlify, S3, etc.).

Arquivos:
- index.html    Página principal
- script.js     Renderização dos cards e formulário
- assets/       Logo e imagem do hero

Uso:
1. Envie a pasta inteira para a raiz (public_html) do seu servidor.
2. Acesse pelo domínio.

Notas:
- Tailwind CSS e ícones Lucide são carregados via CDN. É necessário
  acesso à internet no navegador do visitante.
- Se preferir uma versão totalmente offline, gere um CSS local do
  Tailwind (tailwindcss CLI) e baixe o Lucide como arquivo local.
- O formulário de contato abre o cliente de e-mail do visitante
  (mailto:). Para envio direto por servidor, integre um endpoint
  próprio (PHP, Formspree, etc.).
