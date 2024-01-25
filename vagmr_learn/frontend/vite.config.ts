import { defineConfig, Plugin } from 'vite';
import react from '@vitejs/plugin-react-swc';
import { resolve } from 'path';


// Vite configuration
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'), // Entry HTML file
      },
      output: {
        entryFileNames: `static/js/[name]-[hash].js`,
        chunkFileNames: `static/js/[name]-[hash].js`,
        assetFileNames: ({ name }) => {
          if (/\.(gif|jpe?g|png|svg)$/.test(name ?? '')) {
            return 'static/images/[name]-[hash][extname]';
          }
          if (/\.(css)$/.test(name ?? '')) {
            return 'static/css/[name]-[hash][extname]';
          }
          // Other static assets
          return 'static/[name]-[hash][extname]';
        }
      }
    }
  }
});