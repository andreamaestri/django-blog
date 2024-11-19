/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './blog/templates/**/*.html',
    './blog/**/*.py',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        'main-bg': '#F9FAFC',
        'brand-gray': '#4A4A4F',
        'brand-red': '#E84610',
        'dark-bg': '#445261',
        'flash-bg': '#188181',
        'masthead-bg': '#445261',
        'link-normal': '#445261',
        'link-hover': '#E84610',
        'btn-bg': '#188181',
        'btn-hover-bg': '#fff',
        'btn-hover-text': '#23BBBB',
        'like-red': '#E84610',
        'delete-bg': '#E84610',
        'link-color': '#23BBBB',
        'subtitle-gray': 'lightgray',
        'faded': 'rgb(172, 175, 175)',
        'approval': 'rgb(222, 146, 168)',
      },
      fontFamily: {
        'lato': ['Lato', 'sans-serif'],
      },
      fontSize: {
        'brand': '1.4rem',
      },
      skew: {
        '15': '15deg',
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
  ],
};
