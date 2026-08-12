// Map a page slug to its clean route, honouring astro.config `base`.
// index -> "/", everything else -> "/<slug>".
const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');

export function href(slug: string): string {
  const path = slug === 'index' ? '/' : `/${slug}`;
  return BASE ? `${BASE}${path === '/' ? '/' : path}` : path;
}
