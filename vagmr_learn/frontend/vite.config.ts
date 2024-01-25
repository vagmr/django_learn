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
        entryFileNames: `static/js/[hash].js`,
        chunkFileNames: `static/js/[hash].js`,
        assetFileNames: ({ name }) => {
          if (/\.(gif|jpe?g|png|svg)$/.test(name ?? '')) {
            return 'static/images/[hash][extname]';
          }
          if (/\.(css)$/.test(name ?? '')) {
            return 'static/css/[hash][extname]';
          }
          return 'static/[hash][extname]';
        }
      }
    }
  }
});