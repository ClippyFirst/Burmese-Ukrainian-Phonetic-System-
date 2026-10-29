import { resolve } from "node:path";
import { defineConfig } from "vite";

export default defineConfig({
  base: "./",
  build: {
    target: "es2022",
    // Keep the methodology page in the production artifact; Playwright validates it via preview.
    rollupOptions: {
      input: {
        main: resolve(process.cwd(), "index.html"),
        system: resolve(process.cwd(), "system.html"),
      },
    },
  },
});
