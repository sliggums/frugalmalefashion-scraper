module.exports = {
  env: {
    node: true,
    browser: true,
  },
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
  plugins: ['react', 'react-hooks'],
  rules: {
    'no-console': 1,
    'no-unused-vars': 0,
    'react/prop-types': 0,
    'react/no-unknown-property': ['error', { ignore: ['css'] }],
  },
};
