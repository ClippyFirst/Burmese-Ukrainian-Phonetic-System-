import { resolve } from "node:path";
import { defineConfig } from "vite";

export default defineConfig({
  base: "./",
  build: {
    target: "es2022",
    rollupOptions: {
      input: {
        main: resolve(process.cwd(), "index.html"),
        system: resolve(process.cwd(), "system.html"),
      },
    },
  },
});
