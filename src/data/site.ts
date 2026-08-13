// All structured content for the CME site, drawn from the source materials.
// Ported verbatim from the previous Python generator (scripts/sitegen/data.py).
import studentsData from './students.json';

export interface Seminar {
  term: string;
  sem: string;
  topic: string;
  guide: string;
}
export interface Student {
  name: string;
  batch: string;
  email: string;
  seminars: Seminar[];
  featured: Seminar | null;
  topic_count: number;
}

// Student cohort — parsed from the seminar sheet (scripts/parse_data.py -> data.json).
export const STUDENTS: Student[] = studentsData as Student[];

export const DEPT = {
  name: 'Centre for Multidisciplinary Education',
  abbr: 'CME',
  former: 'Centre for Liberal Education (CLE)',
  institute: 'Indian Institute of Technology Bombay',
  incharge: 'Prof. Rajesh Zele',
  incharge_email: 'rajeshzele@iitb.ac.in',
  tagline: 'Design your own degree.',
};

// ---- headline stats ----
export const STATS = [
  { num: 6, suf: '', lbl: 'Foundation areas every student explores' },
  { num: 4, suf: '', lbl: 'Bachelor of Science concentrations to graduate in' },
  { num: 260, suf: '', lbl: 'Credits across a fully individualised curriculum' },
];

// ---- why CME ----
export const WHY = [
  { ic: 'heart', t: 'Follow your passion',
    d: 'Build a degree around what genuinely drives you - not a template handed down by a single department. Your curiosity sets the direction.' },
  { ic: 'grid', t: 'Freedom across every department',
    d: 'Choose electives and even core courses from any department at IIT Bombay - CSE, EE, Mechanical, Mathematics, Humanities, Design, Management and more.' },
  { ic: 'user', t: '1-on-1 faculty advisor',
    d: 'A dedicated Faculty Advisor (FacAd) guides you every semester and approves your individual Plan of Study, so freedom never means drift.' },
  { ic: 'route', t: 'An individualised curriculum',
    d: 'No two CME students follow the same path. Your combination of courses, seminars and projects is uniquely yours.' },
  { ic: 'flask', t: 'Research from your third semester',
    d: 'Work directly with professors on 4-credit Seminars from Sem 3, growing into full 6-credit research Projects in your final year.' },
  { ic: 'globe', t: 'A globally recognised BS',
    d: 'Graduate with a Bachelor of Science - the global standard for science & engineering at MIT, Stanford and Harvard - with a declared specialisation.' },
];

// ---- foundation baskets (with real course codes from the structure slides) ----
export interface Basket {
  key: string; hue: string; ic: string; name: string; blurb: string;
  courses: [string, string][];
}
export const FOUNDATION: Basket[] = [
  { key: 'hum', hue: '--hue-hum', ic: 'book', name: 'Humanities & Social Sciences',
    blurb: 'Language, literature and the study of society and the human condition.',
    courses: [['HS1xx', 'Any HSS course beyond the first year'], ['HS213', 'Language and Literature']] },
  { key: 'des', hue: '--hue-des', ic: 'palette', name: 'Design',
    blurb: 'Design thinking, product design and how people interact with technology.',
    courses: [['DE250', 'Design Thinking for Innovation'], ['DE344', 'Simple Product Design'],
              ['DE346', 'Human–Computer Interaction']] },
  { key: 'mgmt', hue: '--hue-mgmt', ic: 'briefcase', name: 'Management',
    blurb: 'Management, marketing, finance and the practice of building ventures.',
    courses: [['SOM101', 'Introduction to Management'], ['MG401', 'Marketing Management'],
              ['MG403', 'Accounting and Finance'], ['MG405', 'Project Management'],
              ['ENT101', 'Innovation & Entrepreneurship'], ['ENT613', 'Social Enterprises & Inclusive Business']] },
  { key: 'eco', hue: '--hue-eco', ic: 'chart', name: 'Economics',
    blurb: 'Economic reasoning, decision theory and the forces shaping markets.',
    courses: [['EC101', 'Economics'], ['EC403', 'Decision Theory & Information'],
              ['EC411', 'Indian Economy'], ['EC416', 'Energy Economics'], ['EC457', 'Managerial Economics']] },
  { key: 'env', hue: '--hue-env', ic: 'leaf', name: 'Environmental & Rural Studies',
    blurb: 'Sustainability, environment and technology for development.',
    courses: [['ES203', 'Water & Wastewater Engineering'], ['ES317', 'Air Pollution Science & Engineering'],
              ['ES321', 'Energy & Environmental Sustainability'], ['TD602', 'Soil, Land Use, GIS & Agriculture'],
              ['TD626', 'Technology, Society & Development'], ['TD638', 'Development Perspectives']] },
  { key: 'eng', hue: '--hue-eng', ic: 'cog', name: 'Engineering',
    blurb: 'A foundation in core engineering - any introductory course beyond the first year.',
    courses: [['DIC', 'Any core engineering course, e.g.'], ['AE / BB / CE', 'CL, CS, EE, EN, ME, MM 1xx introductory courses']] },
];

// ---- semester credit grid (from the structure slides) ----
export const CURRIC_HEAD = ['Track', 'Sem 3', 'Sem 4', 'Sem 5', 'Sem 6', 'Sem 7', 'Sem 8'];
// each cell: [label, type] type in found|elec|sem|proj|es|none
export type Cell = [string, string];
export const CURRIC_ROWS: (string | Cell)[][] = [
  ['1', ['Foundation', 'found'], ['Foundation', 'found'], ['Elective', 'elec'], ['Elective', 'elec'], ['Elective', 'elec'], ['Elective', 'elec']],
  ['2', ['Foundation', 'found'], ['Foundation', 'found'], ['Elective', 'elec'], ['Elective', 'elec'], ['Elective', 'elec'], ['Elective', 'elec']],
  ['3', ['Foundation', 'found'], ['Foundation', 'found'], ['Elective', 'elec'], ['Elective', 'elec'], ['Elective', 'elec'], ['Elective', 'elec']],
  ['4', ['ES250 & HS250', 'es'], ['Elective', 'elec'], ['Elective', 'elec'], ['Elective', 'elec'], ['Elective', 'elec'], ['Elective', 'elec']],
  ['5', ['Elective', 'elec'], ['Elective', 'elec'], ['Elective', 'elec'], ['Elective', 'elec'], ['Project', 'proj'], ['Project', 'proj']],
  ['6', ['Seminar', 'sem'], ['Seminar', 'sem'], ['Seminar', 'sem'], ['Seminar', 'sem'], ['-', 'none'], ['-', 'none']],
];

export const CREDIT_RULES: [string, string, string][] = [
  ['cap', 'Max 30 core credits from a single department', 'At most five UG “core” (compulsory) courses from any one department - keeping the degree genuinely multidisciplinary. There is no cap on electives.'],
  ['layers', 'First year + CME = 260 credits', '64 credits carried from the first year plus 196 across Semesters 3–8, all chosen in consultation with your Faculty Advisor.'],
  ['flask', 'Seminars grow into Projects', 'Four 4-credit research Seminars from Sem 3–6, followed by two 6-credit Projects in Sem 7–8, each with a guide of your choice and mid-term & end-term presentations.'],
  ['cog', 'Hands-on credit slots', 'LAB, SLP, PT and Work Visits contribute up to 18 credits and can replace any three elective slots - for students who learn by building.'],
];

// ---- concentrations ----
export interface Concentration { key: string; hue: string; deg: string; ic: string; d: string; fields: string[]; }
export const CONCENTRATIONS: Concentration[] = [
  { key: 'eng', hue: '--hue-eng', deg: 'BS in Engineering Sciences', ic: 'cog',
    d: 'For students who want deep engineering ability without being boxed into one branch - spanning computation, electronics, robotics, controls and beyond.',
    fields: ['Computer Science', 'Signal Processing', 'Robotics', 'Controls Theory', 'Microprocessors', 'Digital Systems'] },
  { key: 'nat', hue: '--hue-eco', deg: 'BS in Natural Sciences', ic: 'atom',
    d: 'For the mathematically and scientifically curious - probability, analysis, optimisation and the physical sciences underpinning modern research.',
    fields: ['Probability & Random Processes', 'Linear Algebra', 'Optimization', 'Real & Complex Analysis', 'Quantum Mechanics', 'Differential Equations'] },
  { key: 'soc', hue: '--hue-hum', deg: 'BS in Social Sciences', ic: 'scale',
    d: 'For those drawn to economics, policy and the systems that shape society - from public policy to the economics of healthcare and development.',
    fields: ['Public Policy in Practice', 'State, Market & Public Policy', 'Economics in Healthcare', 'Behavioural Economics', 'Development Studies'] },
  { key: 'art', hue: '--hue-des', deg: 'BS in Art & Design', ic: 'palette',
    d: 'For makers and storytellers - human-centred design, interaction, creative technology and the craft of building things people love.',
    fields: ['Design Thinking', 'Human–Computer Interaction', 'Product Design', 'Digital Lives', 'Creative Technology'] },
];

// ---- IDPC faculty (2026 team) — [name, dept, photo slug, website] ----
export type Faculty = [string, string, string, string];
export const FACULTY: Faculty[] = [
  ['Suyash Awate', 'Computer Science & Engineering', 'suyash-awate', 'https://www.cse.iitb.ac.in/~suyash/'],
  ['Prasad Bokil', 'Industrial Design Centre', 'prasad-bokil', 'https://www.prasadbokil.com/'],
  ['Rohan Chinchwadkar', 'Shailesh J. Mehta School of Management', 'rohan-chinchwadkar', 'https://www.som.iitb.ac.in/prof-rohan-chinchwadkar/'],
  ['Arindam Chowdhury', 'Chemistry', 'arindam-chowdhry', 'https://www.chem.iitb.ac.in/~arindam/'],
  ['Girish Dalvi', 'Industrial Design Centre', 'girish-dalvi', 'https://www.idc.iitb.ac.in/people/faculty/dalvi-girish'],
  ['Ashutosh Gandhi', 'Metallurgical Engg. & Materials Science', 'ashutosh-gandhi', 'https://www.iitb.ac.in/mems/en/prof-ashutosh-s-gandhi'],
  ['Prasanna Gandhi', 'Mechanical Engineering', 'prasanna-gandhi', 'https://www.me.iitb.ac.in/~gandhi/'],
  ['Neeta Kanekar', 'Biosciences & Bioengineering', 'neeta-kanekar', 'https://www.bio.iitb.ac.in/people/faculty/kanekar-n/'],
  ['Malhar Kulkarni', 'Humanities & Social Sciences', 'malhar-kulkarni', 'https://homepages.iitb.ac.in/~malhar/'],
  ['Archak Mittal', 'Civil Engineering', 'archak-mittal', 'https://homepages.iitb.ac.in/~archak/'],
  ['Swati Patankar', 'Biosciences & Bioengineering', 'swati-patankar', 'https://www.bio.iitb.ac.in/people/faculty/patankar-s/'],
  ['Amber Shrivastava', 'Mechanical Engineering', 'amber-shrivastava', 'https://homepages.iitb.ac.in/~ashrivastava.me/'],
];

// ---- companies (user-ordered, biggest first) + real logo where available ----
// logo: filename in img/logos, or null -> wordmark
// `square`: emblem-style logos (roughly as tall as they are wide) — they get a
// larger cap in the marquee so they don't read as tiny next to the wordmarks.
// `flagship`: the widely recognised names, shown on the home-page teaser row.
export interface Company { n: string; logo: string | null; cat: string; square?: boolean; flagship?: boolean; }
export const COMPANIES: Company[] = [
  { n: 'Coinbase', flagship: true, logo: 'coinbase.svg', cat: 'Tech / AI' },
  { n: 'Expedia Group', flagship: true, logo: 'expedia.svg', cat: 'Tech / AI' },
  { n: 'Deloitte', flagship: true, logo: 'deloitte.svg', cat: 'Consulting' },
  { n: 'Visa', flagship: true, logo: 'visa.svg', cat: 'Tech / AI' },
  { n: 'Otsuka', flagship: true, logo: 'otsuka.svg', cat: 'AI Engineering' },
  { n: 'Layer10', logo: null, cat: 'AI Engineering' },
  { n: 'BharatGen', flagship: true, logo: 'bharatgen.png', cat: 'AI Engineering' },
  { n: 'Terrastack', logo: 'terrastack.svg', cat: 'Tech / AI' },
  { n: 'Juspay', flagship: true, logo: 'juspay.svg', cat: 'Tech / AI' },
  { n: 'NoQs', square: true, logo: 'noqs.svg', cat: 'Startup' },
  { n: 'Autowhat', square: true, logo: 'autowhat.png', cat: 'Startup' },
  { n: 'Axalon Systems', logo: 'axalon.png', cat: 'Startup' },
  { n: 'Sunjewels', square: true, logo: 'sunjewels.svg', cat: "Founder's Office" },
  { n: 'Lifebound Technologies', logo: 'lifebound.png', cat: 'Startup' },
  { n: 'Mercedes-Benz', flagship: true, square: true, logo: 'mercedes.svg', cat: 'Core / SDE' },
  { n: 'Jaguar Land Rover', flagship: true, logo: 'jlr.svg', cat: 'Core / SDE' },
  { n: 'HAL', flagship: true, logo: 'hal.png', cat: 'Data / Core' },
  { n: 'Cars24', flagship: true, logo: 'cars24.png', cat: 'Tech / AI' },
];

export interface PlacementRole { ic: string; t: string; d: string; roles: string[]; }
export const PLACEMENT_ROLES: PlacementRole[] = [
  { ic: 'sparkle', t: 'Tech, AI & Software', d: 'Software Development Engineers and AI Engineers.',
    roles: ['SDE - Visa, Expedia, Mercedes-Benz, Jaguar Land Rover, Terrastack', 'AI Engineer - Otsuka (Japan), Layer10, BharatGen', 'Engineering - Coinbase, Hushh AI'] },
  { ic: 'chart', t: 'Consulting, Strategy & Data', d: 'Analytical and strategic roles across firms and startups.',
    roles: ['Consultant - Deloitte', 'Strategy & Ops - BatterySmart', 'Data Analyst Trainee - HAL', 'Analytics - Cars24'] },
  { ic: 'bulb', t: "Founder's Office & Ventures", d: 'Early-stage, high-ownership roles at fast-moving startups.',
    roles: ["Founder's Office - SunJewels", 'Product & Growth - Lifebound Technologies', 'Startup roles - NoQs, Autowhat, Axalon Systems'] },
];

// ---- example / featured seminars (curated multidisciplinary showcase) ----
export interface FeaturedSeminar { topic: string; who: string; batch: string; hue: string; field: string; }
export const FEATURED_SEMINARS: FeaturedSeminar[] = [
  { topic: 'Physics-Informed Neural Networks', who: 'Yuvraj Parekh', batch: '2023', hue: '--hue-eng', field: 'AI × Physics' },
  { topic: "Quantum Entanglement and Bell's Inequalities", who: 'Punit Ranawat', batch: '2024', hue: '--hue-eco', field: 'Quantum Physics' },
  { topic: 'Computational Aspects of Hindustani Classical Music & Raga Recognition', who: 'Rushikesh Shinde', batch: '2023', hue: '--hue-des', field: 'AI × Music' },
  { topic: 'Archaeology and Other Sciences: A Bidirectional Exchange of Methods', who: 'Jennifer Esbel Mary', batch: '2024', hue: '--hue-hum', field: 'Archaeology × Science' },
  { topic: "Hilbert's Programme, Gödel and the Limits of Formalising Mathematics", who: 'Nidhish Sahni', batch: '2024', hue: '--hue-eco', field: 'Logic & Mathematics' },
  { topic: 'Game-Theoretic Approaches to Multi-Agent Reinforcement Learning', who: 'Priyansh Jhanwar', batch: '2023', hue: '--hue-eng', field: 'AI × Game Theory' },
  { topic: 'From Potential to Price: How VCs Value Early-Stage Startups', who: 'Kabir Dodai', batch: '2024', hue: '--hue-mgmt', field: 'Finance × Ventures' },
  { topic: 'Role of Cinema in Cultural Representation', who: 'Kusum Rathore', batch: '2024', hue: '--hue-hum', field: 'Media & Culture' },
  { topic: 'Kolmogorov–Arnold Networks: A Literature Review', who: 'Chaitanya Deshkar', batch: '2023', hue: '--hue-eng', field: 'Machine Learning' },
];

// ---- admissions ----
export interface AdmissionStep { yr: string; t: string; d: string; }
export const ADMISSION_STEPS: AdmissionStep[] = [
  { yr: 'END OF SEM 2', t: 'Complete your first year', d: 'Finish the first year in any undergraduate programme at IIT Bombay with a CPI above 6.0 and zero backlogs. The process begins before the end of your second semester.' },
  { yr: 'APPLICATION', t: 'Express your interest', d: 'Sign up for the CME interviews. Appearing is not a binding commitment - you keep full freedom to decide later, in your own time and with your family.' },
  { yr: 'SELECTION', t: 'Interview & holistic review', d: 'The IDPC faculty select students through a ~10–15 minute conversational interview and an overall review of your academic performance - looking for curiosity, not a rehearsed plan.' },
  { yr: 'TRANSITION', t: 'An official branch change', d: 'Selected students formally move to CME - a 100% official branch change. You adopt the CME curriculum and begin designing your individual path with a Faculty Advisor.' },
];

export const ADMISSION_CRITERIA: [string, string, string][] = [
  ['cap', 'Completed first year', 'Open to students from every undergraduate department after their first year at IIT Bombay.'],
  ['chart', 'CPI above 6.0', 'A cumulative performance index above 6.0, with zero active backlogs at the time of applying.'],
  ['chat', 'Conversational interview', 'A short, friendly interview with CME faculty - evaluation-focused but relaxed. Be yourself and answer honestly.'],
  ['shield', 'The 25% safeguard', 'No parent department can lose more than 25% of its sanctioned strength. If your application is declined solely due to this cap, your CPI is not used as a cut-off for others.'],
];

// ---- FAQ (condensed & faithful to the Freshers FAQ) ----
export const FAQ: [string, string[]][] = [
  ['Is CME an add-on programme - or a real branch change?',
   ['CME is a 100% official branch change. You transition entirely out of your parent department and become a full-time student of the Centre for Multidisciplinary Education, following the CME curriculum from then on.']],
  ['How many courses can I take from a single department?',
   ['To keep the degree genuinely multidisciplinary, you can take at most five UG core (compulsory) courses - 30 credits - from any single department.',
    'There is no cap on electives: you can register for as many elective courses from a department as you like.']],
  ['What degree will I receive, and is a BS inferior to a BTech?',
   ['You graduate with a BS in your chosen specialisation - Engineering Sciences, Natural Sciences, Social Sciences, or Art & Design.',
    'It is not inferior. The BS is the global standard for science & engineering degrees at top universities (MIT, Stanford, Harvard); BTech is largely an Indian naming convention. For research, global mobility and top PhD programmes, a BS with a declared specialisation is highly advantageous.']],
  ['How do companies view CME for placements and internships?',
   ['For most modern technology, AI and strategy roles, recruiters prioritise your skills, projects and interview performance over the branch name. Core-engineering recruiters weigh the branch a little more.',
    'CME students have already interned across Coinbase, Visa, Expedia, Deloitte, Otsuka and more - on the strength of their skills and portfolios.']],
  ["How do I make sure I don't lose focus?",
   ['The flexibility is balanced by real structure: a 1-on-1 Faculty Advisor must approve your Plan of Study, you work toward a defined concentration, and mandatory Seminars (Sem 3–6) and Projects (Sem 7–8) push you to build deep expertise in a chosen domain.']],
  ['What are the honest trade-offs of joining CME?',
   ['You are graded alongside the majors whose courses you take - there is no separate curve for CME students.',
    'With a small cohort you build your own academic and social network rather than inheriting a 150-person department block.',
    'You own your timetable, secure instructor consent for advanced courses, and drive your own progression. CME rewards a proactive, self-driven mindset.']],
  ['If I sit for the interview, am I locked in?',
   ['No. Appearing for the interview or expressing interest is not binding. You have ample time to weigh your options and discuss with your family before the branch change is finalised. A dedicated Parent Orientation session addresses questions about the degree, placements and structure.']],
];

export const NAV: [string, string][] = [
  ['about', 'About'],
  ['curriculum', 'Curriculum'],
  ['concentrations', 'Concentrations'],
  ['people', 'Faculty'],
  ['students', 'Students'],
  ['placements', 'Placements'],
  ['admissions', 'Admissions'],
];
