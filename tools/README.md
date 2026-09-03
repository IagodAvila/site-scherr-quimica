# tools/

As 6 páginas de serviço (`/tratamento-de-agua-de-caldeiras/`, etc.) são **geradas**,
não editadas à mão — elas compartilham header, rodapé, CTA e JSON-LD.

- `paginas_conteudo.py` — o conteúdo de cada página (títulos, textos, FAQ). **Edite aqui.**
- `gerar_paginas.py` — o template. Regrava os `*/index.html`.

Para alterar o texto de uma página, ou o header/rodapé de todas:

```sh
python3 tools/gerar_paginas.py   # regrava as 6 páginas
npm run build:css                # Tailwind varre ./*.html e ./*/*.html
```

Editar um `*/index.html` diretamente funciona, mas a alteração se perde
na próxima execução do gerador.
