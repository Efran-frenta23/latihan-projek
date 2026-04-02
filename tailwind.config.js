/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./image/templates/**/*.html",
    "./**/templates/**/*.html",
  ],
  theme: {
    extend: {
      animation: {
        'fade-in': 'fadeIn 0.3s ease-in-out',
        'slide-up': 'slideUp 0.4s ease-out',
        'scale-in': 'scaleIn 0.2s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        scaleIn: {
          '0%': { transform: 'scale(0.95)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
      },
      colors: {
        yellow: {
          50: '#fefce8',
          100: '#fef9c3',
          200: '#fef08a',
          300: '#fde047',
          400: '#facc15',
          500: '#eab308',
          600: '#ca8a04',
          700: '#a16207',
          800: '#854d0e',
          900: '#713f12',
        },
      },
    },
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: [
      {
        light: {
          ...require("daisyui/src/theming/themes")["light"],
          primary: "#eab308",
          "primary-content": "#ffffff",
          secondary: "#fef08a",
          accent: "#facc15",
          neutral: "#fefce8",
          "base-100": "#ffffff",
          "base-200": "#fef9c3",
          "base-300": "#fefce8",
          info: "#0ea5e9",
          success: "#22c55e",
          warning: "#f59e0b",
          error: "#ef4444",
        },
      },
      {
        yellow: {
          ...require("daisyui/src/theming/themes")["light"],
          primary: "#ca8a04",
          "primary-content": "#ffffff",
          secondary: "#fde047",
          accent: "#facc15",
          neutral: "#fefce8",
          "base-100": "#ffffff",
          "base-200": "#fef9c3",
          "base-300": "#fefce8",
          info: "#0ea5e9",
          success: "#22c55e",
          warning: "#f59e0b",
          error: "#ef4444",
        },
      },
    ],
    darkTheme: "light",
    base: true,
    styled: true,
    utils: true,
    prefix: "",
    logs: true,
    themeRoot: ":root",
  },
}

