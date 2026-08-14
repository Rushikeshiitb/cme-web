// Map a page slug to its clean route, honouring astro.config `base`.
// index -> "/", everything else -> "/<slug>".
import { SITE_LOCK } from '~/data/site';

const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');

export function homeHref(): string {
  return BASE ? `${BASE}/` : '/';
}

export function href(slug: string): string {
  // home-only lock (data/site.ts): every internal link points at the home page, so
  // nothing in the nav, footer or page body can reach a page that isn't ready yet.
  if (SITE_LOCK.homeOnly) return homeHref();
  const path = slug === 'index' ? '/' : `/${slug}`;
  return BASE ? `${BASE}${path === '/' ? '/' : path}` : path;
}
