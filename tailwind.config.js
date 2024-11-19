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
      spacing: {
        '10p': '10%', // Custom spacing for margin-top
        '5p': '5%',  // Custom spacing for margin-left
        '33vh': '33vh', // Custom height
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('flowbite/plugin'),
    function ({ addUtilities }) {
      const newUtilities = {
        '.masthead': {
          marginTop: '10px',
          overflow: 'hidden',
          position: 'relative',
          display: 'inline-block',
          height: '33vh',
          width: '100%',
        },
        '.masthead-text': {
          backgroundColor: '#445261',
          color: 'white',
          position: 'relative',
        },
        '.masthead-image': {
          position: 'relative',
          overflow: 'hidden',
        },
        '.masthead-image::after': {
          content: '""',
          position: 'absolute',
          top: '0',
          right: '90%',
          height: '100%',
          width: '150%',
          background: '#445261',
          transform: 'skew(15deg)',
          zIndex: '100',
        },
        '.brand': {
          fontFamily: 'Lato, sans-serif',
          fontSize: '1.4rem',
          fontWeight: '700',
          color: '#4A4A4F',
        },
        '.red-o': {
          color: '#E84610',
        },
        '.thin': {
          fontWeight: '300',
        },
        '.light-bg': {
          backgroundColor: '#fff',
        },
        '.dark-bg': {
          backgroundColor: '#445261',
        },
        '.main-bg': {
          backgroundColor: '#F9FAFC',
        },
        '.card': {
          border: 'none',
          backgroundColor: 'transparent',
        },
        '.image-container': {
          position: 'relative',
        },
        '.image-flash': {
          position: 'absolute',
          bottom: '5%',
          minWidth: '30%',
          left: '-2px',
          backgroundColor: '#188181',
        },
        '.scale': {
          width: '100%',
          height: 'auto',
        },
        '.author': {
          color: 'white',
          margin: '4px',
          textTransform: 'uppercase',
        },
        '.post-link': {
          textDecoration: 'none',
          color: '#445261',
        },
        '.post-link:hover, .page-link': {
          color: '#E84610',
        },
        '.post-title': {
          marginTop: '10%',
          marginLeft: '5%',
        },
        '.post-subtitle': {
          marginLeft: '5%',
          color: 'lightgray',
        },
        '.btn-signup, .btn-edit': {
          backgroundColor: '#188181',
          color: '#fff',
        },
        '.btn-signup:hover, .btn-signup:active': {
          backgroundColor: '#fff',
          color: '#23BBBB',
        },
        '.link': {
          color: '#23BBBB',
          textDecoration: 'none',
        },
        '.link:hover, .link:active': {
          color: '#445261',
          textDecoration: 'underline',
        },
        '.btn-like': {
          color: '#E84610',
          border: 'none',
          background: 'transparent',
        },
        '.btn-delete': {
          color: '#fff',
          background: '#E84610',
        },
        '.btn-like:hover, .btn-like:active': {
          color: '#E84610',
          background: 'transparent',
          border: 'none',
        },
        '.faded': {
          color: 'rgb(172, 175, 175)',
        },
        '.approval': {
          color: 'rgb(222, 146, 168)',
        },
      };

      addUtilities(newUtilities, ['responsive', 'hover']);
    },
  ],
};
