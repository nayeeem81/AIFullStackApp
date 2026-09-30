import { defineConfig } from 'vite';
import plugin from '@vitejs/plugin-react';

// https://vitejs.dev
export default defineConfig({
    plugins: [plugin()],
    server: {
        port: 58612, // Keeps your custom Visual Studio assigned port
        // Inside your frontend/vite.config.js proxy block:
        server: {
            proxy: {
                '/api': {
                    target: 'http://127.0.0.1:8000', // <-- Ensure this points to your FastAPI port (usually 8000)
                    changeOrigin: true,
                    secure: false,
                }
            }
        }

    }
});
