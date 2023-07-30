import React from 'react';
import ReactDOM from 'react-dom/client';
import { HashRouter } from 'react-router-dom';
import App from './App';
import 'reset-css';
import 'normalize.css';
import './index.scss';

ReactDOM.createRoot(document.getElementById('root')).render(
  <HashRouter>
      <App />
  </HashRouter>
);
