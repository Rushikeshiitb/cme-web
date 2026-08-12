#!/usr/bin/env python3
"""Parse the Seminar Details workbook into a clean consolidated student dataset."""
import openpyxl, json, re, os, collections

XLSX = "imp-files/Seminar Details.xlsx"
# Student dataset consumed by the Astro site (src/data/site.ts imports it).
OUT = "src/data/students.json"

# sheet -> (batch, term label, semester)
SHEETS = {
    "23 Aut 24-25": ("2023", "Autumn '24", "Sem 3"),
    "23 Spr 24-25": ("2023", "Spring '25", "Sem 4"),
    "23 Aut 25-26": ("2023", "Autumn '25", "Sem 5"),
    "23 Spr 25-26": ("2023", "Spring '26", "Sem 6"),
    "24 Aut 25-26": ("2024", "Autumn '25", "Sem 3"),
    "24 Spr 25-26": ("2024", "Spring '26", "Sem 4"),
}

def clean(v):
    if v is None: return ""
    s = str(v).strip().replace("\n", " ")
    return re.sub(r"\s+", " ", s)

def norm_name(n):
    return re.sub(r"\s+", " ", n.strip().title())

wb = openpyxl.load_workbook(XLSX, data_only=True)
students = collections.OrderedDict()  # roll/name -> record

for sheet, (batch, term, sem) in SHEETS.items():
    ws = wb[sheet]
    rows = [[clean(c) for c in r] for r in ws.iter_rows(values_only=True)]
    # find header row
    hdr_i = next(i for i, r in enumerate(rows) if r and r[0].upper() == "NAME")
    hdr = [h.upper() for h in rows[hdr_i]]
    def col(*names):
        for nm in names:
            if nm in hdr: return hdr.index(nm)
        return None
    ci = {
        "name": col("NAME"), "email": col("EMAILS", "EMAIL"),
        "facad": col("FACAD"), "guide": col("GUIDE"), "topic": col("TOPIC"),
    }
    for r in rows[hdr_i + 1:]:
        if not r or not r[ci["name"]]: continue
        nm = r[ci["name"]]
        if nm.lower() in ("third year students", "second year students"): continue
        name = norm_name(nm)
        key = name.lower().replace(" ", "")
        # merge Chaitanya Deshkar variants
        key = key.replace("chaitanyajayantdeshkar", "chaitanyadeshkar")
        email = r[ci["email"]].lower() if ci["email"] is not None else ""
        # sheet 23 Aut 24-25 has no TOPIC col; GUIDE col holds the topic there
        topic = ""
        if ci["topic"] is not None:
            topic = r[ci["topic"]]
        guide = r[ci["guide"]] if ci["guide"] is not None else ""
        facad = r[ci["facad"]] if ci["facad"] is not None else ""
        if sheet == "23 Aut 24-25":
            # columns: NAME, Emails, FACAD, GUIDE(=topic), ...
            topic = guide
            guide = ""
        rec = students.setdefault(key, {
            "name": name, "batch": batch, "email": "", "seminars": []
        })
        if email and "@" in email and not rec["email"]:
            rec["email"] = email
        # keep name with fullest form
        if len(name) > len(rec["name"]):
            rec["name"] = name
        topic = topic.strip()
        # skip placeholder topics
        low = topic.lower()
        if topic and low not in ("na", "evm", "rl") or (topic and sem):
            pass
        rec["seminars"].append({
            "term": term, "sem": sem, "topic": topic,
            "guide": re.sub(r"^Prof\.?\s*", "", guide).strip(),
        })

# order seminars by semester number, keep only ones with a topic for display but retain all
sem_order = {"Sem 3": 3, "Sem 4": 4, "Sem 5": 5, "Sem 6": 6}
data = []
for rec in students.values():
    rec["seminars"].sort(key=lambda s: sem_order.get(s["sem"], 0))
    # featured topic = latest non-empty meaningful topic
    feats = [s for s in rec["seminars"] if s["topic"] and s["topic"].lower() not in ("evm", "rl", "na")]
    rec["featured"] = feats[-1] if feats else (rec["seminars"][-1] if rec["seminars"] else None)
    rec["topic_count"] = len([s for s in rec["seminars"] if s["topic"]])
    data.append(rec)

# sort: 2023 batch first (seniors), then by name
data.sort(key=lambda r: (r["batch"], r["name"]))

os.makedirs("scripts", exist_ok=True)
with open(OUT, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Parsed {len(data)} students")
for r in data:
    print(f"  [{r['batch']}] {r['name']:26s} — {r['topic_count']} topics — feat: {r['featured']['topic'][:55] if r['featured'] and r['featured']['topic'] else '—'}")
