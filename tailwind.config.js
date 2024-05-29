/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        acrylic: '#5CCDF1',
        acrylic_green: '#A1E6E8',
        purple: '#585D87',
        shadow: '#474C72',
      }
    },
  },
  plugins: [],
}