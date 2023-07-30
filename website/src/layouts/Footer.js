import React from 'react';
import { css } from '@emotion/react';

const Footer = () => {

  return (
    <footer>
      <nav>
        <div>{new Date().getFullYear()} &copy; your copyright</div>
      </nav>
    </footer>
  );
};

export default Footer;
