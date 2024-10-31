/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      './templates/index.html',
      './templates/**/*.html',
    ],
    theme: {
      colors: {
          'main': '#1C1F26',
          'secondary': '#2A3B36',
          'accent': '#E4B7A0',
      },
    extend: {},
    },
    plugins: [],
}

