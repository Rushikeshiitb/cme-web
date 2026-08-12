# CME — Centre for Multidisciplinary Education, IIT Bombay

A modern, thorough website for the **Centre for Multidisciplinary Education (CME)** at IIT Bombay
(formerly the Centre for Liberal Education, CLE).

It is built on the **same stack as the EE department site (ee.iitb.ac.in): [Astro](https://astro.build)
+ [Tailwind CSS](https://tailwindcss.com) on the [AstroWind](https://github.com/onwidget/astrowind)
template**, and outputs a fast, fully self-contained **static site** — fonts, logos and images are
all hosted locally, so there are no external calls in the browser.

> **Design note.** The CME visual design is preserved exactly as before. AstroWind/Tailwind provide the
> toolchain and project structure; the pages themselves render the original CME design system
> (`public/assets/css/styles.css` + the components in `src/components/cme/`), so the site looks
> byte-for-byte identical to the previous build while running on the new stack.

## What's inside

Nine pages, each assembled from the structured content in `src/data/`:

| Page | Route | What it covers |
|------|-------|----------------|
| **Home** | `/` | The idea, headline stats, why CME, foundation preview, concentrations, featured seminars, recruiters, faculty |
| **About** | `/about` | The idea & philosophy, CLE → CME history, who it's for, honest trade-offs, leadership |
| **Curriculum** | `/curriculum` | Six foundation baskets (with real course codes), the Sem 3–8 credit map, credit rules, seminars → projects |
| **Concentrations** | `/concentrations` | The four BS degrees — Engineering, Natural, Social Sciences, Art & Design |
| **Faculty** | `/people` | The full IDPC Team 2026 (12 faculty, with photos) + the Faculty Advisor system |
| **Students** | `/students` | Featured seminars + a searchable directory of all 27 students and their seminar topics |
| **Placements** | `/placements` | Internship stats, a prestige-ranked recruiter wall, role breakdown, higher-studies angle |
| **Admissions** | `/admissions` | Eligibility, the 4-step process & timeline, reassurances, and an honest FAQ |
| **Contact** | `/contact` | Faculty in-charge, location, quick links |

### Design
- **Type system** (self-hosted): Fraunces (editorial display serif) · Inter (body) · Space Grotesk
  (brand + numbers) · JetBrains Mono (labels).
- **Light + dark themes** with a toggle (respects the OS preference, remembers your choice).
- A single **warm brown/gold accent** (an IIT-Bombay-flavoured identity), carried consistently through
  the brand mark, section accents, gradient headline words and the curriculum.
- Scroll-reveal animations, animated stat counters, a header that solidifies on scroll, a searchable
  student directory, and an FAQ accordion, all in **dependency-free vanilla JS**
  (`public/assets/js/main.js`). CSS/JS are content-hash versioned (`?v=…`) to avoid stale caches.

## Project layout

```
dept-web/
├── package.json / astro.config.ts / tsconfig.json   # AstroWind (Astro 6 + Tailwind 4) toolchain
├── vendor/                     # AstroWind integration (reads src/config.yaml)
├── src/
│   ├── config.yaml             # site metadata + toggles (blog app disabled)
│   ├── navigation.ts           # CME header + footer links
│   ├── pages/                  # one .astro file per route (the 9 CME pages) + 404
│   ├── layouts/
│   │   ├── Base.astro          # ← CME page shell (original <head>, header, footer)
│   │   └── Layout / PageLayout / … .astro   # AstroWind layouts (available, unused by CME pages)
│   ├── components/
│   │   ├── cme/                # ← the CME design components (Header, Footer, Icon, Hero, …)
│   │   ├── CustomStyles.astro  # AstroWind theme tokens themed to CME
│   │   └── widgets / common / ui   # AstroWind's component library (available for future use)
│   ├── data/
│   │   ├── site.ts             # all structured CME content
│   │   ├── students.json       # the student cohort (generated — see below)
│   │   └── post/               # (empty) AstroWind blog collection, disabled
│   ├── lib/                    # CME helpers: icons, nav/asset URLs, hashing, text
│   └── assets/styles/tailwind.css   # Tailwind entry (part of the stack)
├── public/
│   └── assets/{css,js,fonts,img}    # the original CME stylesheet, JS, fonts, images (served verbatim)
├── scripts/parse_data.py       # parses the seminar xlsx → src/data/students.json
└── dist/                       # ← the generated website (deploy this) — created by `npm run build`
```

## Running it

Requires **Node.js ≥ 22.12**.

```bash
cd dept-web
npm install        # on this machine the global npm cache is root-owned; if install
                   # fails with EACCES, add:  --cache "$(pwd)/.npm-cache"

npm run dev        # dev server → http://localhost:4321
npm run build      # build the static site into dist/
npm run preview    # preview the built site
```

To edit content, change `src/data/site.ts` (or the pages in `src/pages/`); the dev server hot-reloads.

### Updating the student data

`src/data/students.json` is generated from the seminar workbook. Re-run only when the source changes:

```bash
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python scripts/parse_data.py                       # writes src/data/students.json
```

## Deploying

`npm run build` produces a complete static website in `dist/`. Upload its contents to any static host.
If the site is served from a sub-path, set `base` in `src/config.yaml` and rebuild — links and asset
URLs are base-aware.

## Credits & notes
- Faculty photos are extracted from the official CME 2026 structure slides.
- IIT Bombay campus photography is from Wikimedia Commons.
- Company logos are shown for identification of recruiters only and remain the property of their
  respective owners.
- Student names, batches, seminar topics and institute email IDs are included as agreed.
- Toolchain based on the open-source [AstroWind](https://github.com/onwidget/astrowind) template (MIT).
