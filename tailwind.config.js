/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./*/*.html", "./script.js"],
  theme: {
    extend: {
      colors: {
        // Verde amostrado do logo (#00A068). O antigo primary #1e7a4d era uma
        // versão dessaturada da cor real da marca.
        verde: { DEFAULT: "#00A068", texto: "#06774E", claro: "#2FD08C", fundo: "#05372A" },
        tinta: "#0E1F19",
        aco: { DEFAULT: "#56675F", claro: "#8A9A92" },
        ambar: "#D98A1F",
        papel: "#F4F6F4",
        superficie: "#FFFFFF",
        fio: { DEFAULT: "#CFD8D3", forte: "#A9B7B0" },
        "sobre-verde": { DEFAULT: "#E9F3EE", dim: "#9DC6B4" },
      },
      fontFamily: {
        sans: ['Archivo', 'Helvetica Neue', 'Arial', 'sans-serif'],
        mono: ['"IBM Plex Mono"', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      fontSize: {
        // escala modular 1,25 sobre base 17px
        xs: ["13px", { lineHeight: "1.45" }],
        sm: ["15px", { lineHeight: "1.5" }],
        base: ["17px", { lineHeight: "1.55" }],
        lg: ["21px", { lineHeight: "1.4" }],
        xl: ["27px", { lineHeight: "1.25" }],
        "2xl": ["34px", { lineHeight: "1.12" }],
        "3xl": ["42px", { lineHeight: "1.06" }],
        "4xl": ["53px", { lineHeight: "1.03" }],
      },
      maxWidth: { medida: "66ch" },
    },
  },
  plugins: [],
};
