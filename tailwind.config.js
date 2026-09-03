/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./*/*.html", "./script.js"],
  theme: {
    extend: {
      colors: {
        background: "#ffffff",
        foreground: "#0e1a14",
        card: "#ffffff",
        "card-foreground": "#0e1a14",
        primary: { DEFAULT: "#1e7a4d", foreground: "#ffffff" },
        secondary: { DEFAULT: "#eef7f1", foreground: "#274c3a" },
        muted: { DEFAULT: "#eef7f1", foreground: "#5d6f65" },
        accent: { DEFAULT: "#d6ecdd", foreground: "#274c3a" },
        border: "#e2eee6",
        ring: "#1e7a4d",
      },
      boxShadow: {
        elegant: "0 20px 60px -20px rgba(30,122,77,.25)",
        card: "0 4px 20px -4px rgba(30,122,77,.1)",
      },
      backgroundImage: {
        "gradient-hero": "linear-gradient(135deg,#1e7a4d 0%,#3aae74 100%)",
      },
    },
  },
  plugins: [],
};
