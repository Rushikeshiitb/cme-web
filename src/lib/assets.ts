// Content-hash of the CSS + JS, appended to their URLs as ?v= so browsers always
// fetch the current version after a rebuild (md5 of styles.css + main.js, 8 hex chars).
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { resolve } from 'node:path';

export function assetVersion(): string {
  const h = createHash('md5');
  for (const rel of ['css/styles.css', 'js/main.js']) {
    try {
      // Astro's build runs from the project root, so resolve against cwd().
      h.update(readFileSync(resolve(process.cwd(), 'public/assets', rel)));
    } catch {
      /* asset missing at build time — skip */
    }
  }
  return h.digest('hex').slice(0, 8);
}

// Base-aware URL for a file under public/ (honours astro.config `base`).
const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');
export function asset(path: string): string {
  return `${BASE}/${path.replace(/^\//, '')}`;
}
