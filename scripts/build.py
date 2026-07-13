#!/usr/bin/env python3
"""CME site generator — assembles all pages into site/*.html."""
import os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from sitegen.icons import icon
from sitegen.components import (page, eyebrow, section_head, avatar_hue, initials, MARK)
from sitegen import data as D

OUT = os.path.join(os.path.dirname(__file__), "..", "site")
esc = html.escape


# ---------------- shared blocks ----------------
def stat_strip():
    cells = ""
    for s in D.STATS:
        suf = f'<span class="suf">{s["suf"]}</span>' if s["suf"] else ""
        cells += (f'<div class="stat reveal"><div class="num"><span data-count="{s["num"]}">0</span>{suf}</div>'
                   f'<div class="lbl">{s["lbl"]}</div></div>')
    return f'<div class="stats">{cells}</div>'


def logo_wall(companies, ranked=False):
    cells = ""
    for i, c in enumerate(companies):
        rank = f'<span class="rank">{i+1:02d}</span>' if ranked else ""
        if c["logo"]:
            inner = f'<img src="assets/img/logos/{c["logo"]}" alt="{esc(c["n"])} logo" loading="lazy">'
        else:
            words = c["n"].split()
            first = words[0]
            rest = " " + " ".join(words[1:]) if len(words) > 1 else ""
            inner = f'<span class="wordmark"><span class="accent">{first}</span>{rest}</span>'
        cells += f'<div class="logo-cell reveal">{rank}{inner}</div>'
    return f'<div class="logo-wall">{cells}</div>'


def cta_band():
    return f'''<section class="section"><div class="container">
  <div class="cta-band reveal">
    <div class="hero-bg"><div class="mesh m1"></div><div class="mesh m2"></div></div>
    {eyebrow("Admissions open after Year 1", True)}
    <h2 class="section-title" style="margin-top:18px;max-width:760px;margin-inline:auto">Ready to design a degree that looks like <span class="grad-text">you</span>?</h2>
    <p class="lead" style="max-width:560px;margin:20px auto 0">Complete your first year, keep your curiosity, and bring it to CME. The interview is a conversation — not an exam.</p>
    <div class="hero-cta" style="justify-content:center;margin-top:34px">
      <a class="btn btn-accent btn-lg" href="admissions.html">Explore admissions {icon("arrow")}</a>
      <a class="btn btn-ghost btn-lg" href="contact.html" style="background:transparent;color:var(--paper);border-color:rgba(255,255,255,.3)">Talk to us {icon("chat")}</a>
    </div>
  </div>
</div></section>'''


def page_hero(eb, title, lead, crumb):
    return f'''<section class="page-hero"><div class="hero-bg"><div class="mesh m1"></div><div class="mesh m2"></div></div><div class="hero-grid"></div>
  <div class="container">
    <div class="breadcrumb reveal"><a href="index.html">Home</a> {icon("arrow","",1.6)} <span>{crumb}</span></div>
    {eyebrow(eb)}
    <h1 class="reveal" data-d="1">{title}</h1>
    <p class="lead reveal" data-d="2">{lead}</p>
  </div>
</section>'''


# ---------------- HOME ----------------
def home():
    hero = f'''<section class="hero"><div class="hero-bg"><div class="mesh m1"></div><div class="mesh m2"></div><div class="mesh m3"></div></div><div class="hero-grid"></div>
  <div class="container">
    <div class="reveal"><span class="hero-badge">{icon("sparkle","",1.6)} Formerly the Centre for Liberal Education <b>now CME</b></span></div>
    <h1 class="display reveal" data-d="1" style="margin-top:26px">Design your<br>own <span class="grad-text serif-em">degree.</span></h1>
    <p class="lead reveal" data-d="2">The Centre for Multidisciplinary Education at IIT Bombay lets you choose your own coursework across <strong>every department</strong> — and graduate with a Bachelor of Science built entirely around your curiosity.</p>
    <div class="hero-cta reveal" data-d="3">
      <a class="btn btn-primary btn-lg" href="about.html">What is CME? {icon("arrow")}</a>
      <a class="btn btn-ghost btn-lg" href="curriculum.html">See the structure {icon("layers")}</a>
    </div>
    <div style="margin-top:clamp(48px,7vw,88px)">{stat_strip()}</div>
  </div>
</section>'''

    intro = f'''<section class="section"><div class="container">
  <div class="split">
    <div class="reveal">
      {eyebrow("The idea")}
      <h2 class="section-title" style="margin:18px 0 22px">One institute.<br>Every discipline. <span class="serif-em grad-text">Your path.</span></h2>
      <p class="lead">CME is an initiative of IIT Bombay for students who refuse to be boxed into a single branch. After your first year, you join CME and gain the freedom to assemble courses — electives <em>and</em> core courses — from any department.</p>
      <p style="margin-top:16px">A dedicated Faculty Advisor helps you turn that freedom into a coherent, rigorous plan. The result is a degree as individual as you are, inspired by the flexible models of MIT and Harvard.</p>
      <div class="badge-row" style="margin-top:26px">
        <span class="mini-badge">{icon("cap")} 100% official branch change</span>
        <span class="mini-badge">{icon("globe")} Globally recognised BS</span>
        <span class="mini-badge">{icon("user")} 1-on-1 faculty advisor</span>
      </div>
    </div>
    <div class="reveal" data-d="1">
      <div class="media-frame" style="aspect-ratio:4/3">
        <img src="assets/img/campus/main-building.jpg" alt="IIT Bombay Main Building" loading="lazy">
        <span class="tag">{icon("pin","",1.6)} IIT Bombay · Powai</span>
      </div>
    </div>
  </div>
</div></section>'''

    why_cards = ""
    for i, w in enumerate(D.WHY):
        why_cards += (f'<div class="why-card reveal" data-d="{(i%3)+1}"><div class="card-ic">{icon(w["ic"])}</div>'
                      f'<div class="idx">0{i+1}</div><h3>{w["t"]}</h3><p>{w["d"]}</p></div>')
    why = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  {section_head("Why CME", "Freedom, with a compass.", "Radical academic flexibility, held together by mentorship, structure and purpose.", grad_word="compass")}
  <div class="grid g-3">{why_cards}</div>
</div></section>'''

    # foundation preview
    fcards = ""
    for i, b in enumerate(D.FOUNDATION):
        fcards += (f'<div class="card disc reveal" data-d="{(i%3)+1}" style="--c:var({b["hue"]})">'
                   f'<div class="card-ic">{icon(b["ic"])}</div><span class="credits">6 CREDITS</span>'
                   f'<h3 style="margin-top:8px">{b["name"]}</h3><p>{b["blurb"]}</p></div>')
    foundation = f'''<section class="section"><div class="container">
  {section_head("Foundation", "Six areas. One well-rounded mind.", "Before you specialise, you earn six credits in each of six foundation areas — a genuine grounding across the sciences, humanities and design.")}
  <div class="grid g-3">{fcards}</div>
  <div style="margin-top:36px" class="reveal"><a class="btn btn-ghost" href="curriculum.html">Explore the full curriculum {icon("arrow")}</a></div>
</div></section>'''

    # concentrations preview
    ccards = ""
    for i, c in enumerate(D.CONCENTRATIONS):
        fields = "".join(f"<span>{f}</span>" for f in c["fields"][:4])
        ccards += (f'<div class="conc reveal" data-d="{(i%2)+1}" style="--c:var({c["hue"]})"><div class="glow"></div>'
                   f'<div class="card-ic" style="background:color-mix(in srgb,var({c["hue"]}) 14%,transparent);color:var({c["hue"]})">{icon(c["ic"])}</div>'
                   f'<span class="deg" style="margin-top:16px;display:block">{c["deg"]}</span>'
                   f'<h3>{c["deg"].replace("BS in ","")}</h3><p>{c["d"]}</p><div class="fields">{fields}</div></div>')
    conc = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  {section_head("Concentrations", "Four ways to graduate.", "Every CME student earns a Bachelor of Science in one of four concentrations — chosen through the electives you love.", grad_word="graduate")}
  <div class="grid g-2">{ccards}</div>
</div></section>'''

    # featured seminars
    scards = ""
    for i, s in enumerate(D.FEATURED_SEMINARS[:6]):
        scards += (f'<div class="sem-feat reveal" data-d="{(i%3)+1}" style="--c:var({s["hue"]})"><div class="barcode" style="background:linear-gradient(90deg,var({s["hue"]}),var(--accent))"></div>'
                   f'<span class="eyebrow">{s["field"]}</span>'
                   f'<p class="quote">{esc(s["topic"])}</p>'
                   f'<div class="meta"><div class="avatar" style="width:34px;height:34px;font-size:.8rem;background:var({s["hue"]})">{initials(s["who"])}</div>'
                   f'<div><div style="font-weight:600;font-size:.9rem">{s["who"]}</div><div style="font-size:.78rem;color:var(--ink-3);font-family:var(--ff-mono)">Batch of {s["batch"]}</div></div></div></div>')
    seminars = f'''<section class="section"><div class="container">
  {section_head("Student research", "Seminars that cross every border.", "From reinforcement learning to raga recognition, from quantum entanglement to archaeology — a glimpse of where CME curiosity goes.", grad_word="border")}
  <div class="grid g-3">{scards}</div>
  <div style="margin-top:36px" class="reveal"><a class="btn btn-ghost" href="students.html">Meet the students & browse seminars {icon("arrow")}</a></div>
</div></section>'''

    # placements teaser
    placements = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  {section_head("Where CME goes", "From this classroom to those companies.", "CME students intern where the best of tech, finance and research recruit — on the strength of their skills and portfolios.")}
  {logo_wall(D.COMPANIES[:12])}
  <div style="margin-top:36px" class="reveal"><a class="btn btn-ghost" href="placements.html">See internships & roles {icon("arrow")}</a></div>
</div></section>'''

    # faculty teaser
    faces = ""
    for i, (name, dept, slug) in enumerate(D.FACULTY[:8]):
        faces += (f'<div class="fac reveal" data-d="{(i%4)+1}"><div class="ph"><img src="assets/img/faculty/{slug}.jpg" alt="{esc(name)}" loading="lazy">'
                  f'<span class="dept">{esc(dept.split("&")[0].strip()[:22])}</span></div>'
                  f'<div class="nm">{esc(name)}</div></div>')
    faculty = f'''<section class="section"><div class="container">
  {section_head("The people", "Mentored by twelve departments at once.", "The Inter-Departmental Programme Committee (IDPC) brings together faculty from across IIT Bombay to guide every CME student.")}
  <div class="faculty-grid">{faces}</div>
  <div style="margin-top:36px" class="reveal"><a class="btn btn-ghost" href="people.html">Meet the full IDPC team {icon("arrow")}</a></div>
</div></section>'''

    body = hero + intro + why + foundation + conc + seminars + placements + faculty + cta_band()
    return page("index", "Home",
                "The Centre for Multidisciplinary Education (CME) at IIT Bombay lets students design their own degree across every department and graduate with a Bachelor of Science.",
                body)


# ---------------- ABOUT ----------------
def about():
    hero = page_hero("About CME", 'A centre built on a simple, radical idea: <span class="grad-text serif-em">let students choose.</span>',
                     "CME gives IIT Bombay's most curious students the freedom — and the structure — to build a degree across every discipline.", "About")

    story = f'''<section class="section"><div class="container">
  <div class="split">
    <div class="reveal prose">
      {eyebrow("The idea")}
      <h2 class="section-title" style="margin:16px 0 20px">Freedom to follow your curiosity</h2>
      <p>The Centre for Multidisciplinary Education is an initiative of IIT Bombay for students who want more than one department can offer. After completing the first year in any undergraduate programme, students join CME and gain the freedom to choose their own coursework — electives and even core courses — from <strong>any</strong> department in the institute.</p>
      <p>It is a fully individualised education: your interests define your curriculum, your Faculty Advisor keeps it rigorous, and your research seminars and projects give it depth. You graduate not with a generic template, but with a degree that is unmistakably yours.</p>
    </div>
    <div class="reveal" data-d="1">
      <div class="note" style="margin-bottom:16px"><strong>Formerly CLE.</strong> CME was earlier known as the Centre for Liberal Education. The curriculum has evolved considerably, but the core idea is unchanged — a liberal, multidisciplinary education for a new kind of graduate.</div>
      <div class="feat-list">
        <li><div class="ic">{icon("globe")}</div><div><h4>Inspired by MIT & Harvard</h4><p>Modelled on the flexible, exploration-first education of the world's leading universities.</p></div></li>
        <li><div class="ic">{icon("cap")}</div><div><h4>A real branch change</h4><p>Not a minor or an honour — a 100% official transition into a full-fledged programme.</p></div></li>
        <li><div class="ic">{icon("atom")}</div><div><h4>Analytical by design</h4><p>Interdisciplinary exposure builds stronger quantitative and reasoning skills than a single-track programme.</p></div></li>
      </div>
    </div>
  </div>
</div></section>'''

    pull = f'''<section class="section-sm"><div class="container">
  <p class="pullquote reveal">“Students have the freedom to choose all of their courses — electives and even the core courses of every department — while being mentored by <span class="grad-text">renowned professors</span> across the institute.”</p>
</div></section>'''

    who = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  {section_head("Who CME is for", "Built for the self-driven.", "CME rewards curiosity, initiative and a clear sense of what excites you — while being honest about the trade-offs.", grad_word="self-driven")}
  <div class="grid g-2">
    <div class="card reveal"><div class="card-ic" style="background:color-mix(in srgb,var(--hue-eco) 14%,transparent);color:var(--hue-eco)">{icon("check")}</div><h3>CME is a great fit if you…</h3>
      <ul class="disc" style="border:0;padding:0;background:none;margin-top:14px">
        <li>{icon("check","",2)}<span>Have interests that spill across departments — AI and healthcare, policy and tech, biology and computation.</span></li>
        <li>{icon("check","",2)}<span>Enjoy owning your schedule and taking initiative to secure the courses you want.</span></li>
        <li>{icon("check","",2)}<span>Want to work closely with professors on research from early on.</span></li>
        <li>{icon("check","",2)}<span>Are aiming for top global Master's or PhD programmes.</span></li>
      </ul>
    </div>
    <div class="card reveal" data-d="1"><div class="card-ic" style="background:color-mix(in srgb,var(--hue-hum) 14%,transparent);color:var(--hue-hum)">{icon("scale")}</div><h3>Be honest with yourself about…</h3>
      <ul class="disc" style="border:0;padding:0;background:none;margin-top:14px">
        <li>{icon("arrow","",2)}<span>Academic competitiveness — you're graded alongside the majors whose courses you take.</span></li>
        <li>{icon("arrow","",2)}<span>A smaller cohort — you build your own network rather than inheriting a department block.</span></li>
        <li>{icon("arrow","",2)}<span>Administrative ownership — you assemble your timetable and secure instructor consent yourself.</span></li>
        <li>{icon("arrow","",2)}<span>A proactive mindset — flexibility rewards those who use it deliberately.</span></li>
      </ul>
    </div>
  </div>
</div></section>'''

    leadership = f'''<section class="section"><div class="container">
  <div class="split rev">
    <div class="reveal">
      {eyebrow("Leadership")}
      <h2 class="section-title" style="margin:16px 0 18px">Guided by the IDPC</h2>
      <p class="lead">CME is run by an Inter-Departmental Programme Committee — twelve faculty members drawn from Computer Science, Design, Management, Chemistry, Mechanical, Civil, Biosciences, Humanities and more.</p>
      <p style="margin-top:14px">Together they design the curriculum, advise students one-on-one, and open doors to courses and research across the entire institute. It is, quite literally, an education mentored by a dozen departments at once.</p>
      <div style="margin-top:26px"><a class="btn btn-primary" href="people.html">Meet the faculty {icon("arrow")}</a></div>
    </div>
    <div class="reveal" data-d="1">
      <div class="card" style="padding:30px;border-color:var(--accent)">
        <span class="eyebrow">Faculty in-charge</span>
        <h3 style="font-family:var(--ff-display);font-size:1.7rem;margin:14px 0 4px">{D.DEPT["incharge"]}</h3>
        <p style="font-family:var(--ff-mono);font-size:.8rem;color:var(--ink-3)">CME · IIT BOMBAY</p>
        <p style="margin-top:16px">Leading the Centre for Multidisciplinary Education and its incoming-student orientation for 2026.</p>
        <a class="btn btn-ghost" style="margin-top:18px" href="mailto:{D.DEPT['incharge_email']}">{icon("mail")} {D.DEPT['incharge_email']}</a>
      </div>
    </div>
  </div>
</div></section>'''

    body = hero + story + pull + who + leadership + cta_band()
    return page("about", "About",
                "About the Centre for Multidisciplinary Education (CME) at IIT Bombay — its idea, philosophy, history as the former CLE, and leadership.",
                body)


# ---------------- CURRICULUM ----------------
def curriculum():
    hero = page_hero("Curriculum & Structure", 'A curriculum with <span class="grad-text serif-em">no two alike.</span>',
                     "Six foundation areas, a spine of electives, and research seminars that grow into projects — 260 credits, entirely your own.", "Curriculum")

    fcards = ""
    for i, b in enumerate(D.FOUNDATION):
        courses = "".join(f'<li><code>{esc(code)}</code><span>{esc(nm)}</span></li>' for code, nm in b["courses"])
        fcards += (f'<div class="card disc reveal" data-d="{(i%3)+1}" style="--c:var({b["hue"]})">'
                   f'<div class="card-ic">{icon(b["ic"])}</div><span class="credits">6 CREDITS · ONE BASKET</span>'
                   f'<h3 style="margin-top:8px">{b["name"]}</h3><p>{b["blurb"]}</p><ul>{courses}</ul></div>')
    foundation = f'''<section class="section"><div class="container">
  {section_head("Foundation courses", "Start wide: six baskets, six credits each.", "Every CME student is exposed to all six foundation areas before specialising — and none of these courses need prerequisites, so you can genuinely explore.")}
  <div class="grid g-3">{fcards}</div>
</div></section>'''

    # credit grid
    def cell(c):
        label, cr, typ = c
        if typ == "none":
            return '<td style="opacity:.35">—</td>'
        cls = {"found": "pill-found", "elec": "pill-elec", "sem": "pill-sem", "proj": "pill-proj", "es": "pill-found"}.get(typ, "pill-elec")
        return f'<td><span class="cell"><span class="pill {cls}">{label}</span><span class="cr">{cr}</span></span></td>'
    rows = ""
    for r in D.CURRIC_ROWS:
        rows += "<tr><td>" + r[0] + "</td>" + "".join(cell(c) for c in r[1:]) + "</tr>"
    thead = "".join(f"<th>{h}</th>" for h in D.CURRIC_HEAD)
    totals = "".join(f'<td style="font-family:var(--ff-mono);font-weight:600;color:var(--accent)">{t}</td>' for t in D.CURRIC_TOTALS[1:])
    grid = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  {section_head("The semester map", "Semesters 3 to 8, credit by credit.", "Foundation courses front-load your exploration; electives and research fill the later years. First year (64 credits) + this map = 260 credits total.")}
  <div class="curric-wrap reveal">
    <table class="curric">
      <thead><tr>{thead}</tr></thead>
      <tbody>{rows}
        <tr style="border-top:2px solid var(--line)"><td>Total</td>{totals}</tr>
      </tbody>
    </table>
  </div>
  <div class="badge-row" style="margin-top:22px">
    <span class="mini-badge"><span class="pill pill-found" style="padding:2px 8px">Foundation</span></span>
    <span class="mini-badge"><span class="pill pill-elec" style="padding:2px 8px">Elective</span></span>
    <span class="mini-badge"><span class="pill pill-sem" style="padding:2px 8px">Seminar</span></span>
    <span class="mini-badge"><span class="pill pill-proj" style="padding:2px 8px">Project</span></span>
  </div>
</div></section>'''

    rules_cards = ""
    for i, (ic, t, d) in enumerate(D.CREDIT_RULES):
        rules_cards += (f'<div class="card reveal" data-d="{(i%2)+1}"><div class="card-ic">{icon(ic)}</div>'
                        f'<h3>{t}</h3><p>{d}</p></div>')
    rules = f'''<section class="section"><div class="container">
  {section_head("The rules that keep it rigorous", "Flexible, not formless.", "A few clear guardrails ensure freedom always adds up to a coherent, credible degree.", grad_word="formless")}
  <div class="grid g-2">{rules_cards}</div>
</div></section>'''

    research = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  <div class="split">
    <div class="reveal">
      {eyebrow("Research")}
      <h2 class="section-title" style="margin:16px 0 20px">Seminars that become <span class="serif-em grad-text">projects</span></h2>
      <p class="lead">From your third semester, research is woven into the degree. You choose a guide, dive deep into a domain, and present your work at mid-term and end-term reviews.</p>
      <div class="journey" style="margin-top:32px">
        <div class="step reveal"><div class="stepno">S3–6</div><div><span class="yr">FOUR SEMESTERS · 4 CREDITS EACH</span><h3>Research Seminars</h3><p>A literature-driven deep dive each semester, guided by a professor of your choice — building the skill of independent research.</p></div></div>
        <div class="step reveal" data-d="1"><div class="stepno">S7–8</div><div><span class="yr">FINAL YEAR · 6 CREDITS EACH</span><h3>Research Projects</h3><p>Two full-scale projects that let you contribute original work — several CME papers have been accepted at ML and quantitative-finance conferences.</p></div></div>
      </div>
    </div>
    <div class="reveal" data-d="1">
      <div class="note"><strong>Minors are welcome.</strong> You can pursue a Minor from another department under standard institute rules — with no double-counting between Minor and Foundation courses, and from an area other than your concentration.</div>
      <div class="card" style="margin-top:16px"><div class="card-ic">{icon("target")}</div><h3>Availability of courses</h3><p>High-demand electives are allocated centrally by CPI or lottery, just like every student. For advanced or departmental core courses you secure the instructor's consent — with guidance from your FacAd and the CME team.</p></div>
    </div>
  </div>
</div></section>'''

    body = hero + foundation + grid + rules + research + cta_band()
    return page("curriculum", "Curriculum",
                "The CME curriculum at IIT Bombay: six foundation baskets, a semester-by-semester credit map, research seminars and projects, and the rules that keep it rigorous.",
                body)


# ---------------- CONCENTRATIONS ----------------
def concentrations():
    hero = page_hero("BS Concentrations", 'Four degrees. <span class="grad-text serif-em">One spectrum.</span>',
                     "Your electives shape your specialisation. Every CME student graduates with a Bachelor of Science in one of four concentrations.", "Concentrations")

    cards = ""
    for i, c in enumerate(D.CONCENTRATIONS):
        fields = "".join(f"<span>{f}</span>" for f in c["fields"])
        cards += (f'<div class="conc reveal" data-d="{(i%2)+1}" style="--c:var({c["hue"]});min-height:320px"><div class="glow"></div>'
                  f'<div class="card-ic" style="background:color-mix(in srgb,var({c["hue"]}) 14%,transparent);color:var({c["hue"]})">{icon(c["ic"])}</div>'
                  f'<span class="deg" style="margin-top:18px;display:block">{c["deg"]}</span>'
                  f'<h3>{c["deg"].replace("BS in ","")}</h3><p>{c["d"]}</p><div class="fields">{fields}</div></div>')
    grid = f'''<section class="section"><div class="container">
  {section_head("The four concentrations", "Choose where you go deep.", "You still explore the whole institute — but your electives converge on one of these, and your degree names it.")}
  <div class="grid g-2">{cards}</div>
</div></section>'''

    spectrum = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  {section_head("The multidisciplinary spectrum", "Not a silo — a spectrum.", "A CME concentration is a centre of gravity, not a cage. Most students blend fields across it.", center=True, grad_word="spectrum")}
  <div class="reveal" style="max-width:820px;margin:0 auto;text-align:center">
    <div class="spectrum-bar" style="height:8px;margin-bottom:26px"></div>
    <p class="lead">A quant-leaning student might pair Probability and Optimization with Corporate Finance and a CS minor. A designer might weave Human–Computer Interaction with cognitive science and machine learning. The concentration is simply the story your transcript tells.</p>
  </div>
</div></section>'''

    minor = f'''<section class="section"><div class="container">
  <div class="cta-band on-surface reveal" style="background:var(--surface);border:1px solid var(--line)">
    <div style="max-width:760px;margin:0 auto">
      {eyebrow("Minors", True)}
      <h2 class="section-title" style="margin:16px 0 14px">Add a Minor on top</h2>
      <p class="lead">CME students already pursue Minors in Computer Science, Electrical Engineering and Data Science. Standard institute rules apply — with no double-counting between Minor and Foundation courses, and from an area other than your concentration.</p>
    </div>
  </div>
</div></section>'''

    body = hero + grid + spectrum + minor + cta_band()
    return page("concentrations", "Concentrations",
                "The four Bachelor of Science concentrations at CME, IIT Bombay: Engineering Sciences, Natural Sciences, Social Sciences, and Art & Design.",
                body)


# ---------------- PEOPLE ----------------
def people():
    hero = page_hero("The IDPC Faculty", 'Mentored by <span class="grad-text serif-em">twelve departments.</span>',
                     "The Inter-Departmental Programme Committee brings together faculty from across IIT Bombay to design the curriculum and advise every CME student one-on-one.", "Faculty")

    incharge = f'''<section class="section-sm"><div class="container">
  <div class="card reveal" style="border-color:var(--accent);display:flex;gap:24px;align-items:center;flex-wrap:wrap">
    <div class="avatar" style="width:64px;height:64px;font-size:1.4rem;background:linear-gradient(135deg,var(--accent),var(--hue-des))">{initials(D.DEPT["incharge"])}</div>
    <div style="flex:1;min-width:220px"><span class="eyebrow">Faculty in-charge</span><h3 style="font-family:var(--ff-display);font-size:1.5rem;margin-top:8px">{D.DEPT["incharge"]}</h3><p style="margin-top:4px">Leading the Centre for Multidisciplinary Education and the 2026 incoming-student orientation.</p></div>
    <a class="btn btn-ghost" href="mailto:{D.DEPT['incharge_email']}">{icon("mail")} Email</a>
  </div>
</div></section>'''

    faces = ""
    for i, (name, dept, slug) in enumerate(D.FACULTY):
        faces += (f'<div class="fac reveal" data-d="{(i%4)+1}"><div class="ph"><img src="assets/img/faculty/{slug}.jpg" alt="{esc(name)}" loading="lazy">'
                  f'<span class="dept">{esc(dept)}</span></div>'
                  f'<div class="nm">{esc(name)}</div><div class="role">{esc(dept)}</div></div>')
    grid = f'''<section class="section" style="padding-top:clamp(24px,4vw,40px)"><div class="container">
  {section_head("IDPC Team 2026", "The committee behind your degree.", "Twelve faculty members from Computer Science, Design, Management, Chemistry, Mechanical, Civil, Biosciences, Materials and Humanities.")}
  <div class="faculty-grid">{faces}</div>
</div></section>'''

    facad = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  <div class="split">
    <div class="reveal">{eyebrow("Faculty advisors")}
      <h2 class="section-title" style="margin:16px 0 18px">Every student, one dedicated advisor</h2>
      <p class="lead">Beyond the committee, each CME student is paired with a Faculty Advisor (FacAd) who approves their individual Plan of Study and mentors them each semester.</p>
      <p style="margin-top:14px">Students also choose research guides across the institute — from Mathematics and Computer Science to Management, Biosciences and Design — for their seminars and projects.</p>
    </div>
    <div class="reveal" data-d="1"><div class="grid g-2" style="gap:14px">
      <div class="mini-badge" style="justify-content:center;padding:18px">{icon("user")} 1-on-1 mentorship</div>
      <div class="mini-badge" style="justify-content:center;padding:18px">{icon("book")} Approves your Plan of Study</div>
      <div class="mini-badge" style="justify-content:center;padding:18px">{icon("flask")} Guides seminars & projects</div>
      <div class="mini-badge" style="justify-content:center;padding:18px">{icon("compass")} Advises course choices</div>
    </div></div>
  </div>
</div></section>'''

    body = hero + incharge + grid + facad + cta_band()
    return page("people", "Faculty",
                "The IDPC Team 2026 — twelve faculty members from across IIT Bombay who run the Centre for Multidisciplinary Education.",
                body, active="people")


# ---------------- STUDENTS ----------------
def students():
    hero = page_hero("Students & Seminars", 'Curiosity, <span class="grad-text serif-em">on the record.</span>',
                     "Meet the CME cohort and browse the research seminars they've presented — a living map of where multidisciplinary freedom actually leads.", "Students")

    # featured seminars grid
    scards = ""
    for i, s in enumerate(D.FEATURED_SEMINARS):
        scards += (f'<div class="sem-feat reveal" data-d="{(i%3)+1}" style="--c:var({s["hue"]})"><div class="barcode" style="background:linear-gradient(90deg,var({s["hue"]}),var(--accent))"></div>'
                   f'<span class="eyebrow">{s["field"]}</span><p class="quote">{esc(s["topic"])}</p>'
                   f'<div class="meta"><div class="avatar" style="width:34px;height:34px;font-size:.8rem;background:var({s["hue"]})">{initials(s["who"])}</div>'
                   f'<div><div style="font-weight:600;font-size:.9rem">{s["who"]}</div><div style="font-size:.78rem;color:var(--ink-3);font-family:var(--ff-mono)">Batch of {s["batch"]}</div></div></div></div>')
    featured = f'''<section class="section"><div class="container">
  {section_head("Featured seminars", "A few we're especially proud of.", "Handpicked from across the cohort — spanning AI, quantum physics, music, mathematics, finance and the humanities.")}
  <div class="grid g-3">{scards}</div>
</div></section>'''

    # directory
    b2023 = sum(1 for s in D.STUDENTS if s["batch"] == "2023")
    b2024 = sum(1 for s in D.STUDENTS if s["batch"] == "2024")
    cards = ""
    for st in D.STUDENTS:
        hue = avatar_hue(st["name"])
        feat = st.get("featured")
        topic = esc(feat["topic"]) if feat and feat["topic"] else "Seminar in progress"
        guide = feat["guide"] if feat and feat.get("guide") else ""
        guide_line = f'<span>Guide · {esc(guide)}</span>' if guide else "<span></span>"
        email = st.get("email", "")
        mail = f'<a href="mailto:{esc(email)}">{icon("mail","",1.6)} Email</a>' if email else "<span></span>"
        search = esc((st["name"] + " " + topic + " " + (guide or "")).lower())
        cards += (f'<article class="stu" data-student data-batch="{st["batch"]}" data-search="{search}">'
                  f'<div class="stu-head"><div class="avatar" style="background:var({hue})">{initials(st["name"])}</div>'
                  f'<div><div class="nm">{esc(st["name"])}</div><div class="batch">BATCH OF {st["batch"]} · {st["topic_count"]} SEMINAR{"S" if st["topic_count"]!=1 else ""}</div></div></div>'
                  f'<div class="stu-topic"><span class="k">Latest seminar</span>{topic}</div>'
                  f'<div class="stu-foot">{guide_line}{mail}</div></article>')
    directory = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  {section_head("The cohort", "Every student, every seminar.", f"Browse all {len(D.STUDENTS)} CME students across the 2023 and 2024 batches. Search by name or topic, or filter by batch.")}
  <div class="student-tools reveal">
    <button class="filter-btn active" data-filter="all">All · {len(D.STUDENTS)}</button>
    <button class="filter-btn" data-filter="2023">2023 batch · {b2023}</button>
    <button class="filter-btn" data-filter="2024">2024 batch · {b2024}</button>
    <div class="search-box">{icon("search")}<input id="stuSearch" type="search" placeholder="Search name or topic…" aria-label="Search students"></div>
  </div>
  <div class="stu-grid">{cards}</div>
  <p id="stuEmpty" style="display:none;text-align:center;color:var(--ink-3);padding:40px">No students match your search.</p>
</div></section>'''

    body = hero + featured + directory + cta_band()
    return page("students", "Students",
                "Meet the CME student cohort at IIT Bombay and browse their research seminars — from reinforcement learning and quantum physics to music, finance and archaeology.",
                body)


# ---------------- PLACEMENTS ----------------
def placements():
    hero = page_hero("Internships & Placements", 'The résumé, <span class="grad-text serif-em">not the branch.</span>',
                     "For modern tech, AI and strategy roles, recruiters hire on skills and portfolio. CME students have already turned that into offers at some of the world's best companies.", "Placements")

    stats = f'''<section class="section-sm"><div class="container">
  <div class="stats">
    <div class="stat reveal"><div class="num"><span data-count="12">0</span></div><div class="lbl">Students in the current cohort</div></div>
    <div class="stat reveal" data-d="1"><div class="num"><span data-count="9">0</span></div><div class="lbl">Actively sought internships</div></div>
    <div class="stat reveal" data-d="2"><div class="num"><span data-count="7">0</span></div><div class="lbl">Secured internship roles</div></div>
    <div class="stat reveal" data-d="3"><div class="num"><span data-count="78">0</span><span class="suf">%</span></div><div class="lbl">Conversion for those who applied</div></div>
  </div>
</div></section>'''

    wall = f'''<section class="section"><div class="container">
  {section_head("Where CME interns", "Recruited by the best.", "Ordered by scale and prestige — the companies where CME students have interned so far.")}
  {logo_wall(D.COMPANIES, ranked=True)}
  <p style="margin-top:16px;font-size:.82rem;color:var(--ink-3)" class="reveal">Logos are shown for identification of recruiters only and remain the property of their respective owners.</p>
</div></section>'''

    role_cards = ""
    for i, r in enumerate(D.PLACEMENT_ROLES):
        rl = "".join(f'<li>{icon("check","",2)}<span>{esc(x)}</span></li>' for x in r["roles"])
        role_cards += (f'<div class="card disc reveal" data-d="{(i%3)+1}" style="--c:var(--accent)"><div class="card-ic">{icon(r["ic"])}</div>'
                       f'<h3>{r["t"]}</h3><p>{r["d"]}</p><ul style="margin-top:14px">{rl}</ul></div>')
    roles = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  {section_head("The roles", "From SDE to Founder's Office.", "CME students land across the spectrum of high-quality roles — technical, analytical and entrepreneurial.")}
  <div class="grid g-3">{role_cards}</div>
</div></section>'''

    higher = f'''<section class="section"><div class="container">
  <div class="split">
    <div class="reveal">{eyebrow("Higher studies")}
      <h2 class="section-title" style="margin:16px 0 18px">A launchpad for research</h2>
      <p class="lead">CME is a strong advantage for Master's and PhD applications. Working with multiple professors, taking advanced cross-departmental electives and building a unique research portfolio are exactly the qualities top global universities look for.</p>
      <p style="margin-top:14px">Students have already had research papers accepted at prestigious conferences in Machine Learning and Quantitative Finance.</p>
    </div>
    <div class="reveal" data-d="1"><p class="pullquote" style="font-size:clamp(1.3rem,2.6vw,2rem)">A BS with a declared specialisation is the <span class="grad-text">global standard</span> for research and top-tier PhD programmes.</p></div>
  </div>
</div></section>'''

    body = hero + stats + wall + roles + higher + cta_band()
    return page("placements", "Placements",
                "CME internships and placements at IIT Bombay — students have interned at Coinbase, Visa, Expedia, Deloitte, Otsuka and more across tech, consulting and startups.",
                body)


# ---------------- ADMISSIONS ----------------
def admissions():
    hero = page_hero("Admissions", 'Bring your <span class="grad-text serif-em">curiosity.</span>',
                     "Admission to CME opens after your first year at IIT Bombay. The process is holistic, the interview is a conversation, and the decision stays yours.", "Admissions")

    crit_cards = ""
    for i, (ic, t, d) in enumerate(D.ADMISSION_CRITERIA):
        crit_cards += (f'<div class="card reveal" data-d="{(i%4)+1}"><div class="card-ic">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></div>')
    criteria = f'''<section class="section"><div class="container">
  {section_head("Eligibility", "Who can apply.", "Open to every first-year undergraduate at IIT Bombay who meets a few clear criteria.")}
  <div class="grid g-4">{crit_cards}</div>
</div></section>'''

    steps = ""
    for i, s in enumerate(D.ADMISSION_STEPS):
        steps += (f'<div class="step reveal" data-d="{(i%3)+1}"><div class="stepno">{i+1}</div>'
                  f'<div><span class="yr">{s["yr"]}</span><h3>{s["t"]}</h3><p>{s["d"]}</p></div></div>')
    process = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  <div class="split">
    <div>{section_head("The process", "Four steps, no surprises.", "From finishing your first year to an official branch change.")}
      <div class="note reveal"><strong>The interview is chill.</strong> Roughly 10–15 minutes, conversational, and evaluation-focused. Not much prep is expected — the panel looks for intellectual curiosity and a clear reason for wanting a flexible curriculum, not a rehearsed three-year plan.</div>
    </div>
    <div class="journey reveal" data-d="1">{steps}</div>
  </div>
</div></section>'''

    reassure = f'''<section class="section"><div class="container">
  <div class="grid g-3">
    <div class="card reveal"><div class="card-ic">{icon("route")}</div><h3>Not a point of no return</h3><p>Appearing for the interview isn't binding. You have time to weigh your options and talk it through with your family before anything is finalised.</p></div>
    <div class="card reveal" data-d="1"><div class="card-ic">{icon("users")}</div><h3>Parent orientation</h3><p>A dedicated session addresses parents' questions about the BS degree's validity, placements and academic structure — transparently.</p></div>
    <div class="card reveal" data-d="2"><div class="card-ic">{icon("shield")}</div><h3>The 25% safeguard</h3><p>No department loses more than 25% of its strength to CME. If you're declined solely due to this cap, your CPI isn't held against other applicants.</p></div>
  </div>
</div></section>'''

    # FAQ
    faq_items = ""
    for q, ans in D.FAQ:
        ans_html = "".join(f"<p>{a}</p>" for a in ans)
        faq_items += (f'<div class="faq-item"><button class="faq-q">{esc(q)}<span class="pm"></span></button>'
                      f'<div class="faq-a"><div class="faq-a-inner">{ans_html}</div></div></div>')
    faq = f'''<section class="section" style="background:var(--surface-2)"><div class="container" style="max-width:900px">
  {section_head("Questions & answers", "The honest FAQ.", "Straight answers on the degree, placements, workload and the real trade-offs — adapted from the CME Freshers guide.", grad_word="honest")}
  <div class="reveal">{faq_items}</div>
</div></section>'''

    body = hero + criteria + process + reassure + faq + cta_band()
    return page("admissions", "Admissions",
                "How to join CME at IIT Bombay: eligibility (CPI above 6.0 after first year), the interview process, timeline, and an honest FAQ.",
                body)


# ---------------- CONTACT ----------------
def contact():
    hero = page_hero("Contact", 'Let&rsquo;s <span class="grad-text serif-em">talk.</span>',
                     "Questions about the programme, the curriculum, or applying? Reach the CME office at IIT Bombay.", "Contact")

    cards = f'''<section class="section"><div class="container">
  <div class="grid g-2">
    <div class="contact-card reveal"><div class="ic">{icon("user")}</div><div><h4>Faculty in-charge</h4><p>{D.DEPT["incharge"]}</p><a href="mailto:{D.DEPT['incharge_email']}">{D.DEPT['incharge_email']}</a></div></div>
    <div class="contact-card reveal" data-d="1"><div class="ic">{icon("pin")}</div><div><h4>Where we are</h4><p>Centre for Multidisciplinary Education,<br>IIT Bombay, Powai, Mumbai 400076, India</p></div></div>
    <div class="contact-card reveal"><div class="ic">{icon("cap")}</div><div><h4>Prospective students</h4><p>Finishing your first year? Start with admissions.</p><a href="admissions.html">See how to apply →</a></div></div>
    <div class="contact-card reveal" data-d="1"><div class="ic">{icon("globe")}</div><div><h4>The institute</h4><p>An initiative of IIT Bombay.</p><a href="https://www.iitb.ac.in" target="_blank" rel="noopener">iitb.ac.in →</a></div></div>
  </div>
</div></section>'''

    quick = f'''<section class="section" style="background:var(--surface-2)"><div class="container">
  {section_head("Explore more", "Find what you need.", "", center=True)}
  <div class="grid g-4">
    <a class="card reveal" href="about.html"><div class="card-ic">{icon("compass")}</div><h3>About CME</h3><p>The idea and philosophy.</p></a>
    <a class="card reveal" data-d="1" href="curriculum.html"><div class="card-ic">{icon("layers")}</div><h3>Curriculum</h3><p>Structure & credits.</p></a>
    <a class="card reveal" data-d="2" href="students.html"><div class="card-ic">{icon("flask")}</div><h3>Students</h3><p>Cohort & seminars.</p></a>
    <a class="card reveal" data-d="3" href="placements.html"><div class="card-ic">{icon("briefcase")}</div><h3>Placements</h3><p>Where CME interns.</p></a>
  </div>
</div></section>'''

    body = hero + cards + quick
    return page("contact", "Contact",
                "Contact the Centre for Multidisciplinary Education (CME) at IIT Bombay — faculty in-charge, location, and how to apply.",
                body)


# ---------------- build ----------------
PAGES = {
    "index": home, "about": about, "curriculum": curriculum, "concentrations": concentrations,
    "people": people, "students": students, "placements": placements,
    "admissions": admissions, "contact": contact,
}


def build():
    os.makedirs(OUT, exist_ok=True)
    for slug, fn in PAGES.items():
        out = os.path.join(OUT, f"{slug}.html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(fn())
        print(f"  wrote {slug}.html")
    print(f"Built {len(PAGES)} pages into {os.path.relpath(OUT)}")


if __name__ == "__main__":
    build()
