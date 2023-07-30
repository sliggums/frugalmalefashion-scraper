import React, { useMemo } from 'react';
import { css, Global } from '@emotion/react';
import AppRouter from './routes';
import AppLayout from './layouts/AppLayout';

function App() {
  return (
    <>
      <Global
        styles={css`
          

          body {
            color: var(--text-primary);
            background: var(--bg);
            transition-duration: 0.3s;
            transition-timing-function: ease;
            transition-property: border, background, color;
          }

          main {
            flex: 1;
            margin: 0 auto;
            max-width: 1280px;
            display: flex;
            flex-direction: column;
          }
        `}
      />

      <AppLayout>
        <AppRouter />
      </AppLayout>
    </>
  );
}

export default App;
