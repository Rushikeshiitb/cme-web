"""Shared layout components: head, header, footer, and small helpers."""
from .icons import icon
from .data import DEPT, NAV

# Inline brand mark — six discipline strands converging to one node.
MARK = '''<svg class="mark" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<rect x="2" y="2" width="96" height="96" rx="24" fill="#0C1020"/>
<g stroke-width="4.4" fill="none" stroke-linecap="round">
<path d="M50 50 C 30 30, 24 26, 20 22" stroke="#E4572E"/>
<path d="M50 50 C 34 24, 40 18, 42 14" stroke="#7C3AED"/>
<path d="M50 50 C 62 26, 66 20, 70 15" stroke="#D6910A"/>
<path d="M50 50 C 74 34, 80 30, 84 26" stroke="#0E9F6E"/>
<path d="M50 50 C 74 66, 80 74, 82 80" stroke="#0E8FA5"/>
<path d="M50 50 C 30 70, 24 76, 21 82" stroke="#2563EB"/>
</g>
<circle cx="50" cy="50" r="8.5" fill="#FAF8F3"/><circle cx="50" cy="50" r="4" fill="#0C1020"/></svg>'''

FAVICON = ("data:image/svg+xml,"
           "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
           "%3Crect width='100' height='100' rx='24' fill='%230C1020'/%3E"
           "%3Cg stroke-width='5' fill='none' stroke-linecap='round'%3E"
           "%3Cpath d='M50 50 30 22' stroke='%23E4572E'/%3E%3Cpath d='M50 50 42 14' stroke='%237C3AED'/%3E"
           "%3Cpath d='M50 50 70 15' stroke='%23D6910A'/%3E%3Cpath d='M50 50 84 26' stroke='%230E9F6E'/%3E"
           "%3Cpath d='M50 50 82 80' stroke='%230E8FA5'/%3E%3Cpath d='M50 50 21 82' stroke='%232563EB'/%3E%3C/g%3E"
           "%3Ccircle cx='50' cy='50' r='9' fill='%23FAF8F3'/%3E%3C/svg%3E")


def brand(footer=False):
    return (f'<a class="brand" href="index.html" aria-label="CME home">{MARK}'
            f'<span>{DEPT["abbr"]}<small>IIT BOMBAY</small></span></a>')


def header(active):
    links = "".join(
        '<a href="{}.html"{}>{}</a>'.format(
            slug, ' class="active" aria-current="page"' if slug == active else "", label)
        for slug, label in NAV)
    mlinks = "".join(
        '<a href="{}.html"{}><span>{:02d}</span>{}</a>'.format(
            slug, ' class="active" aria-current="page"' if slug == active else "", i + 1, label)
        for i, (slug, label) in enumerate([("index", "Home")] + list(NAV)))
    toggle = (f'<button class="theme-toggle" data-theme-toggle aria-label="Toggle colour theme">'
              f'{icon("moon","moon")}{icon("sun","sun")}</button>')
    return f'''<header class="site-header">
  <nav class="nav container-wide" aria-label="Primary">
    {brand()}
    <div class="nav-links">{links}</div>
    <div class="nav-actions">
      {toggle}
      <a class="nav-cta" href="admissions.html">Apply {icon("arrow","",1.9)}</a>
      <button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false">{icon("menu")}</button>
    </div>
  </nav>
</header>
<div class="mobile-menu" id="mobileMenu">{mlinks}
  <a href="admissions.html" style="color:var(--accent)"><span>→</span>Apply to CME</a>
</div>'''


def footer():
    prog = "".join(f'<a href="{s}.html">{l}</a>' for s, l in
                   [("about", "About CME"), ("curriculum", "Curriculum & Structure"),
                    ("concentrations", "BS Concentrations"), ("admissions", "Admissions")])
    comm = "".join(f'<a href="{s}.html">{l}</a>' for s, l in
                   [("people", "IDPC Faculty"), ("students", "Students & Seminars"),
                    ("placements", "Placements"), ("contact", "Contact")])
    ext = (f'<a href="https://www.iitb.ac.in" target="_blank" rel="noopener">IIT Bombay {icon("external","",1.6)}</a>'
           f'<a href="https://www.cse.iitb.ac.in" target="_blank" rel="noopener">Academic Rulebook {icon("external","",1.6)}</a>'
           f'<a href="mailto:{DEPT["incharge_email"]}">Email the office {icon("external","",1.6)}</a>')
    return f'''<footer class="site-footer">
  <div class="footer-spectrum spectrum-bar" style="border-radius:0"></div>
  <div class="container-wide">
    <div class="footer-top">
      <div class="footer-brand">
        {brand(footer=True)}
        <p>An initiative of IIT Bombay giving students the freedom to design their own multidisciplinary degree across every department.</p>
      </div>
      <div class="footer-col"><h5>Programme</h5>{prog}</div>
      <div class="footer-col"><h5>Community</h5>{comm}</div>
      <div class="footer-col"><h5>Resources</h5>{ext}</div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="yr">2026</span> {DEPT["name"]}, {DEPT["institute"]}. Formerly the {DEPT["former"]}.</span>
      <span>Faculty in-charge · {DEPT["incharge"]}</span>
    </div>
  </div>
</footer>'''


def page(slug, title, desc, body, active=None, head_extra=""):
    active = active if active is not None else slug
    full_title = f"{title} · CME, IIT Bombay" if slug != "index" else f"CME · {DEPT['name']}, IIT Bombay"
    return f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0C1020">
<link rel="icon" href="{FAVICON}">
<link rel="preload" href="assets/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/fraunces-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/styles.css">
<script>(function(){{try{{var t=localStorage.getItem('cme-theme');if(t)document.documentElement.setAttribute('data-theme',t);else if(matchMedia('(prefers-color-scheme:dark)').matches)document.documentElement.setAttribute('data-theme','dark');}}catch(e){{}}}})();</script>
{head_extra}
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/js/main.js" defer></script>
<script>document.getElementById('yr').textContent=new Date().getFullYear();</script>
</body>
</html>'''


# ---------- content helpers ----------
def eyebrow(text, center=False):
    return f'<span class="eyebrow{" center" if center else ""}">{text}</span>'


def section_head(eb, title, sub="", center=False, grad_word=""):
    cls = " center" if center else ""
    h = title
    if grad_word and grad_word in title:
        h = title.replace(grad_word, f'<span class="grad-text">{grad_word}</span>')
    s = f'<p class="lead">{sub}</p>' if sub else ""
    return (f'<div class="section-head{cls} reveal">{eyebrow(eb, center)}'
            f'<h2 class="section-title">{h}</h2>{s}</div>')


_AV_HUES = ["--hue-hum", "--hue-des", "--hue-mgmt", "--hue-eco", "--hue-env", "--hue-eng", "--accent"]


def avatar_hue(name):
    return _AV_HUES[sum(ord(c) for c in name) % len(_AV_HUES)]


def initials(name):
    parts = [p for p in name.split() if p]
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()
