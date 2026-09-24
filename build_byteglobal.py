#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_byteglobal.py — Byte Global Technologies Pvt. Ltd. corporate website.
Enterprise, AI-first, blue/navy/white. Generates a multi-page static site into
/mnt/user-data/outputs/byteglobal/. Logo assets live in assets/ (user-provided,
cleaned). Content follows the brief; no invented clients/stats/awards — anything
unverified is a clearly marked CMS placeholder.
"""
import os

OUT = "/mnt/user-data/outputs/byteglobal"
os.makedirs(OUT, exist_ok=True)
os.makedirs(os.path.join(OUT,"services"), exist_ok=True)

import base64
def _datauri(fname, mime="image/png"):
    with open(os.path.join(OUT,"assets",fname),"rb") as f:
        return f"data:{mime};base64,"+base64.b64encode(f.read()).decode()
LOGO_WORD  = _datauri("byte-word.png")
LOGO_LIGHT = _datauri("byte-word-light.png")
FAVICON    = _datauri("favicon.png")

import urllib.parse
SITE = "www.byteglobal.in"
EMAIL = "info@byteglobal.in"
PHONE = "+91 81435 97569"
LEGAL = "BYTEGLOBAL TECHNOLOGIES PRIVATE LIMITED"
BRAND = "Byte Global Technologies"
OFFICES = ["Hyderabad"]
ADDRESS_LINES = ["604, 7th Floor","DSL Abacus IT Park","Uppal Nagole Road, Uppal","Hyderabad – 500039","Telangana, India"]
ADDRESS_INLINE = "604, 7th Floor, DSL Abacus IT Park, Uppal Nagole Road, Uppal, Hyderabad – 500039, Telangana, India"
CIN = "U62013TS2026PTC216655"
GSTIN = "36AAOCB7734K1Z4"
UDYAM = "UDYAM-TS-09-0267216"
COMPANY_TYPE = "Private Limited Company"
_addr_q = urllib.parse.quote("DSL Abacus IT Park, Uppal Nagole Road, Uppal, Hyderabad 500039, Telangana, India")
MAPS_DIR = "https://www.google.com/maps/dir/?api=1&destination=" + _addr_q
MAPS_EMBED = "https://maps.google.com/maps?q=" + _addr_q + "&z=15&output=embed"
# Verified physical office; the entries below are GLOBAL MARKETS (reach), not offices.
MARKETS = [("India","IN"),("Germany","DE"),("UAE","AE"),("United Kingdom","GB"),
           ("United States","US"),("Singapore","SG"),("Australia","AU")]

CSS = r"""
:root{
  --navy:#061B49; --blue:#0B4DBB; --bright:#1769E0;
  --white:#FFFFFF; --bg:#F5F8FC; --ink:#111827; --mute:#475569;
  --line:#E2E8F2; --line-2:#EDF2F9; --card:#FFFFFF;
  /* logo accents — sampled from the B */
  --red:#E1493A; --yellow:#F0BB25; --green:#46A45B; --accent-blue:#4B84E3;
  --red-s:#FBEBE9; --yellow-s:#FDF4DD; --green-s:#E8F4EC; --accent-blue-s:#E9F0FC;
  --r:10px; --r-lg:14px;
  --shadow:0 1px 2px rgba(6,27,73,.04),0 8px 30px -18px rgba(6,27,73,.22);
  --shadow-lg:0 30px 70px -34px rgba(6,27,73,.35);
  --maxw:1200px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:'Inter',system-ui,-apple-system,sans-serif;font-size:17px;line-height:1.65;
  -webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:'Manrope','Inter',sans-serif;line-height:1.1;letter-spacing:-.02em;margin:0;color:var(--navy)}
h1{font-size:clamp(2.5rem,5.4vw,4.6rem);font-weight:800}
h2{font-size:clamp(2rem,3.6vw,3.25rem);font-weight:800}
h3{font-size:1.35rem;font-weight:700;letter-spacing:-.01em}
h4{font-size:1.05rem;font-weight:700}
p{margin:0 0 1rem}
a{color:inherit;text-decoration:none}
img,svg{display:block;max-width:100%}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 28px}
.section{padding:104px 0}
.section.tight{padding:72px 0}
.lead{font-size:1.2rem;color:var(--mute);max-width:60ch}
.center{text-align:center}
.center .lead{margin-left:auto;margin-right:auto}
.dark{background:var(--navy);color:#E8EEF9}
.dark h1,.dark h2,.dark h3,.dark h4{color:#fff}
.soft{background:var(--white)}

.eyebrow{font-size:.78rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  color:var(--bright);margin:0 0 16px;display:inline-flex;align-items:center;gap:10px}
.eyebrow::before{content:"";width:22px;height:2px;background:currentColor}
.dark .eyebrow{color:#7FB0FF}

/* buttons */
.btn{display:inline-flex;align-items:center;gap:9px;font-weight:600;font-size:.98rem;
  padding:14px 26px;border-radius:var(--r);border:1px solid transparent;cursor:pointer;
  transition:transform .16s ease,box-shadow .16s ease,background .16s,color .16s,border-color .16s}
.btn:hover{transform:translateY(-1px)}
.btn-primary{background:var(--blue);color:#fff;box-shadow:0 12px 26px -14px var(--blue)}
.btn-primary:hover{background:var(--bright)}
.btn-outline{border-color:var(--line);color:var(--navy);background:#fff}
.btn-outline:hover{border-color:var(--bright);color:var(--bright)}
.dark .btn-outline{border-color:rgba(255,255,255,.28);color:#fff;background:transparent}
.dark .btn-outline:hover{border-color:#fff}
.btn .arr{transition:transform .18s}
.btn:hover .arr{transform:translateX(3px)}

/* header */
header.site{position:fixed;top:0;left:0;right:0;z-index:100;transition:background .3s,box-shadow .3s,border-color .3s;
  border-bottom:1px solid transparent}
header.site.solid{background:rgba(255,255,255,.9);backdrop-filter:blur(14px);
  border-bottom-color:var(--line);box-shadow:0 1px 0 rgba(6,27,73,.03)}
.nav{display:flex;align-items:center;justify-content:space-between;height:78px;gap:20px}
.brand img{height:38px;width:auto}
.brand .lg-light{display:none}
.menu{display:flex;align-items:center;gap:2px}
.menu a{padding:10px 14px;border-radius:8px;font-size:.95rem;font-weight:500;color:var(--navy);
  transition:color .15s,background .15s}
.menu a:hover,.menu a.active{color:var(--bright);background:var(--bg)}
header.site:not(.solid) .menu a{color:var(--navy)}
.nav-cta{display:flex;align-items:center;gap:10px}
.burger{display:none;width:44px;height:44px;border:1px solid var(--line);border-radius:9px;background:#fff;
  cursor:pointer;flex-direction:column;align-items:center;justify-content:center;gap:5px}
.burger span{width:20px;height:2px;background:var(--navy);transition:.25s}
.burger.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.burger.open span:nth-child(2){opacity:0}
.burger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.spacer{height:78px}
.menu.drawer{display:none}

@media(max-width:1040px){
  .menu:not(.drawer),.nav-cta .btn{display:none}
  .burger{display:flex}
  .menu.drawer{display:flex;position:fixed;inset:78px 0 0 0;background:#fff;flex-direction:column;
    align-items:stretch;padding:22px 28px;gap:4px;transform:translateX(100%);transition:transform .3s ease;z-index:99;overflow:auto}
  .menu.drawer.open{transform:none}
  .menu.drawer a{padding:16px;font-size:1.1rem;border-bottom:1px solid var(--line-2);border-radius:0}
  .menu.drawer .btn{display:inline-flex;margin-top:16px;justify-content:center}
}

/* footer */
footer.site{background:var(--navy);color:#B9C6DE;padding:76px 0 34px}
.foot-top{display:grid;grid-template-columns:1.7fr 1fr 1fr 1fr 1fr;gap:36px}
footer .brand img{height:34px;margin-bottom:16px}
footer h5{font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;color:#7E90B4;margin:0 0 16px;font-weight:700;font-family:'Inter'}
footer .fcol a{display:block;color:#B9C6DE;padding:5px 0;font-size:.93rem}
footer .fcol a:hover{color:#fff}
.foot-desc{max-width:34ch;font-size:.95rem;color:#93A2C4}
.foot-bar{display:flex;justify-content:space-between;flex-wrap:wrap;gap:14px;margin-top:52px;padding-top:24px;
  border-top:1px solid rgba(255,255,255,.1);font-size:.85rem;color:#7E90B4}
.foot-bar .legal a{margin-left:18px;color:#93A2C4}
.foot-bar .legal a:hover{color:#fff}
@media(max-width:900px){.foot-top{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.foot-top{grid-template-columns:1fr}}

/* reveal */
.reveal{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none}}

/* grids + cards */
.grid{display:grid;gap:22px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
@media(max-width:960px){.g3,.g4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.g2,.g3,.g4{grid-template-columns:1fr}}

.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r-lg);padding:30px;
  transition:transform .2s,border-color .2s,box-shadow .2s}
.card:hover{transform:translateY(-4px);border-color:#CBD9EE;box-shadow:var(--shadow-lg)}
.card p{color:var(--mute);margin:0;font-size:.97rem}
.card h3{margin:16px 0 10px}

.num{font-family:'Space Mono','Manrope',monospace;font-size:.8rem;color:var(--mute);font-weight:700}
.ic{width:46px;height:46px;border-radius:10px;display:grid;place-items:center;background:var(--bg);
  border:1px solid var(--line);color:var(--bright)}
.ic svg{width:24px;height:24px}

/* page hero */
.phero{padding:150px 0 80px;background:linear-gradient(180deg,#fff, var(--bg));border-bottom:1px solid var(--line)}
.phero h1{max-width:18ch}
.phero .lead{margin-top:18px}

/* trust strip */
.trust{border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:#fff}
.trust .wrap{display:flex;align-items:center;gap:28px;flex-wrap:wrap;padding-top:22px;padding-bottom:22px}
.trust .t-label{font-size:.85rem;color:var(--mute);font-weight:500}
.trust .t-markets{display:flex;gap:10px;flex-wrap:wrap;margin-left:auto}
.chip{display:inline-flex;align-items:center;gap:7px;font-size:.85rem;font-weight:600;color:var(--navy);
  border:1px solid var(--line);border-radius:30px;padding:6px 14px;background:#fff}
.chip .fl{font-size:.9rem}

/* stat */
.stat .n{font-family:'Manrope';font-size:clamp(2.4rem,4vw,3.4rem);font-weight:800;color:var(--blue);letter-spacing:-.03em}
.stat .l{color:var(--mute);font-size:.92rem;margin-top:2px}

/* four-color hairline accent */
.bar4{height:4px;border-radius:4px;background:linear-gradient(90deg,var(--red) 0 25%,var(--yellow) 25% 50%,var(--green) 50% 75%,var(--accent-blue) 75% 100%)}
:focus-visible{outline:2px solid var(--bright);outline-offset:3px;border-radius:6px}
"""

# ---------------------------------------------------------------- ICONS (inline)
def I(p): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
ICONS = {
 "ai": I('<path d="M12 3v3M12 18v3M3 12h3M18 12h3"/><rect x="7" y="7" width="10" height="10" rx="2"/><path d="M10 10h4v4h-4z"/>'),
 "code": I('<path d="M8 6l-5 6 5 6M16 6l5 6-5 6"/>'),
 "cloud": I('<path d="M17.5 19a4.5 4.5 0 0 0 0-9 6 6 0 0 0-11.7 1.5A3.5 3.5 0 0 0 6 19z"/><path d="M9 15l2 2 4-4"/>'),
 "shield": I('<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>'),
 "talent": I('<circle cx="9" cy="8" r="3"/><path d="M4 20a5 5 0 0 1 10 0"/><path d="M16 6a3 3 0 0 1 0 6M20 20a5 5 0 0 0-4-4.9"/>'),
 "learn": I('<path d="M3 7l9-4 9 4-9 4z"/><path d="M7 10v5c0 1 2 2 5 2s5-1 5-2v-5"/>'),
 "transform": I('<path d="M4 7h12l-3-3M20 17H8l3 3"/>'),
 "globe2": I('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'),
 "check": I('<path d="M20 6L9 17l-5-5"/>'),
 "bank": I('<path d="M3 10l9-6 9 6M5 10v8M9 10v8M15 10v8M19 10v8M3 20h18"/>'),
 "health": I('<path d="M12 21s-7-4.5-9-9a4.5 4.5 0 0 1 9-2 4.5 4.5 0 0 1 9 2c-2 4.5-9 9-9 9z"/>'),
 "factory": I('<path d="M3 21V9l6 4V9l6 4V5l6 3v13z"/>'),
 "cart": I('<circle cx="9" cy="20" r="1"/><circle cx="18" cy="20" r="1"/><path d="M3 4h2l2.5 12h11l2-8H6"/>'),
 "edu": I('<path d="M3 7l9-4 9 4-9 4z"/><path d="M21 7v6"/><path d="M7 10v4c0 1 2 2 5 2s5-1 5-2v-4"/>'),
 "signal": I('<path d="M5 12a10 10 0 0 1 14 0M8 15a6 6 0 0 1 8 0"/><circle cx="12" cy="18" r="1"/>'),
 "gov": I('<path d="M3 21h18M5 21V10M19 21V10M4 10l8-6 8 6M9 21v-6h6v6"/>'),
 "truck": I('<path d="M3 6h11v9H3zM14 9h4l3 3v3h-7z"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/>'),
 "energy": I('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'),
 "spark": I('<path d="M12 3v6M12 15v6M3 12h6M15 12h6"/>'),
}

# ---------------------------------------------------------------- DATA: SERVICES
SERVICES = [
 ("artificial-intelligence","Artificial Intelligence","ai",
  "Identify, implement and scale practical AI — from generative systems to enterprise integration.",
  ["Generative AI","AI Automation","AI Consulting","AI Strategy","AI Integration"],
  "Explore AI Solutions",
  "Most organisations know AI matters but struggle to move from experiments to production value.",
  "We start with a use-case audit, prove value on a scoped pilot, then integrate and scale with the right guardrails, evaluation and governance.",
  ["Generative AI apps & copilots","Intelligent process automation","AI strategy & readiness","Model integration & MLOps","AI-powered analytics"]),
 ("software-engineering","Software Engineering","code",
  "Web, mobile, enterprise and SaaS products engineered to scale — tested, observable, maintainable.",
  ["Web Applications","Mobile Applications","Enterprise Software","SaaS Products","Custom Development"],
  "Discuss Your Build",
  "Teams need to ship reliable software fast without accumulating the debt that slows them later.",
  "Product-minded engineering with clean architecture, automated testing and CI/CD from day one.",
  ["Web & mobile applications","Enterprise & SaaS platforms","API & microservice design","Modernisation & re-platforming","Quality engineering"]),
 ("cloud-infrastructure","Cloud & Infrastructure","cloud",
  "Cloud architecture, migration and DevOps you can reason about — and roll back.",
  ["Cloud Migration","DevOps","Managed Cloud Services","Infrastructure Modernization","Cloud Optimization"],
  "Modernise Your Cloud",
  "Legacy infrastructure and unmanaged cloud spend hold back reliability and growth.",
  "We design resilient architectures, migrate with zero-downtime patterns, and automate operations with IaC and observability.",
  ["Cloud migration & landing zones","DevOps & CI/CD automation","Managed cloud operations","Cost & performance optimisation","Reliability & disaster recovery"]),
 ("cybersecurity","Cybersecurity","shield",
  "Security as a property of the system — assessment, compliance and continuous defence.",
  ["Security Assessment","Compliance","SOC Support","Vulnerability Management","Cybersecurity Consulting"],
  "Strengthen Security",
  "Threats evolve faster than most security programs can keep up with.",
  "Assess, remediate and monitor — building security into the SDLC and standing up continuous detection.",
  ["Security assessments & pen testing","Compliance & governance","SOC & managed detection","Vulnerability management","Security consulting & training"]),
 ("talent-solutions","Talent Solutions","talent",
  "The right people, faster — IT staffing, executive hiring and GCC recruitment at global scale.",
  ["IT Staffing","GCC Recruitment","Executive Hiring","Contract Staffing","Technology Talent"],
  "Find Your Talent",
  "Hiring skilled technology talent quickly — and keeping it — is a persistent bottleneck.",
  "A structured pipeline — discover, assess, match, deploy, support — backed by a global talent network.",
  ["IT & contract staffing","GCC & captive-centre hiring","Executive & leadership search","Technology talent pods","Onboarding & retention support"]),
 ("learning-development","Learning & Development","learn",
  "Build the workforce you need — corporate training, campus hiring and upskilling.",
  ["Corporate Training","Campus Hiring","Internship Programs","Skill Development","Workforce Upskilling"],
  "Build Your Workforce",
  "Skills gaps widen as technology moves faster than traditional training can follow.",
  "Role-based, hands-on learning paths that turn potential into production-ready capability.",
  ["Corporate & technical training","Campus hiring programs","Structured internships","Skill development tracks","Workforce upskilling"]),
 ("digital-transformation","Digital Transformation","transform",
  "Technology, people, process, data and AI — combined into scalable transformation programs.",
  ["Business Consulting","Process Automation","Data Analytics","UI/UX Design","Digital Strategy"],
  "Start Your Transformation",
  "Point solutions rarely add up to real transformation without a connecting strategy.",
  "We assess, strategise, design, build, integrate and scale — aligning technology with business outcomes.",
  ["Business & digital strategy","Process automation","Data & analytics","Experience & UI/UX design","Change enablement"]),
 ("overseas-recruitment","Overseas Recruitment","globe2",
  "End-to-end cross-border placement — global sourcing, visa support and international hiring.",
  ["Global Talent Sourcing","Work Visa Support","International Recruitment","End-to-End Placement","Cross-Border Talent Solutions"],
  "Hire Across Borders",
  "Cross-border hiring is slowed by sourcing, compliance and visa complexity.",
  "A single partner for the whole journey — sourcing, assessment, visa support and relocation.",
  ["Global talent sourcing","Work-visa & mobility support","International recruitment","End-to-end placement","Cross-border compliance"]),
]

INDUSTRIES = [
 ("Banking & Financial Services","bank","Secure, scalable and compliant technology and talent for modern financial operations."),
 ("Healthcare","health","Technology and talent solutions for secure, data-driven and scalable healthcare operations."),
 ("Manufacturing","factory","Connected, automated and intelligent systems for the modern factory floor."),
 ("Retail & E-commerce","cart","Digital commerce, data and AI that turn customer experience into growth."),
 ("Education","edu","Platforms, talent and transformation for learning at scale."),
 ("Telecommunications","signal","Resilient infrastructure and intelligent operations for connectivity providers."),
 ("Government & Public Sector","gov","Trusted, accessible and secure digital services for citizens."),
 ("Logistics & Supply Chain","truck","Visibility, automation and analytics across the supply chain."),
 ("Energy & Utilities","energy","Smart, sustainable and reliable systems for energy and utilities."),
]

WHY = ["AI-Driven Innovation","Enterprise-Ready Solutions","Experienced Technology Professionals",
 "Faster Talent Acquisition","Flexible Engagement Models","Global Delivery Capability",
 "Customer-Centric Approach","Long-Term Strategic Partnerships"]

ENGAGE = [
 ("Dedicated Teams","A cross-functional team that works as an extension of yours."),
 ("Project-Based Development","Fixed-scope delivery against clear outcomes and milestones."),
 ("Staff Augmentation","Add vetted specialists to your existing team, fast."),
 ("Managed Services","We run it end-to-end against agreed service levels."),
 ("Consulting","Strategy, architecture and advisory from senior practitioners."),
 ("Recruitment Solutions","Permanent, contract and cross-border hiring at scale."),
]

INSIGHTS = [
 ("Artificial Intelligence","Moving AI from pilot to production","A practical view on the operating model, evaluation and governance that turn AI experiments into durable value."),
 ("Cloud","Designing cloud you can roll back","Resilience patterns and the guardrails that keep migrations calm and reversible."),
 ("Cybersecurity","Security as a system property","Why building security into the SDLC beats bolting it on afterwards."),
 ("Digital Transformation","Transformation that actually connects","Aligning technology, people and process so point solutions add up to change."),
 ("Talent","Hiring technology talent, faster","How a structured pipeline shortens time-to-hire without lowering the bar."),
 ("Recruitment","The cross-border hiring playbook","Sourcing, compliance and mobility, handled end-to-end."),
]

JOBS = [
 ("Senior AI Engineer","Hyderabad","Full-time","Engineering","5+ yrs"),
 ("Cloud Solutions Architect","Hyderabad","Full-time","Cloud","7+ yrs"),
 ("Cybersecurity Consultant","Hyderabad","Full-time","Security","4+ yrs"),
 ("Full-Stack Developer","Hyderabad / Remote","Full-time","Engineering","3+ yrs"),
 ("Technical Recruiter","Hyderabad","Full-time","Talent","2+ yrs"),
 ("UI/UX Designer","Hyderabad","Full-time","Design","3+ yrs"),
]
print("data ready:",len(SERVICES),"services,",len(INDUSTRIES),"industries")

# ---------------------------------------------------------------- SHARED LAYOUT
NAV = [("index.html","Home"),("about.html","About"),("services.html","Services"),
       ("industries.html","Industries"),("talent.html","Talent Solutions"),
       ("global-presence.html","Global Presence"),("insights.html","Insights"),("contact.html","Contact")]

def rel(depth): return "../" if depth else ""

def head(title, desc, active, depth=0):
    p = rel(depth)
    menu = "".join(f'<a href="{p}{h}"'+(' class="active"' if h==active else '')+f'>{n}</a>' for h,n in NAV)
    schema = ('{"@context":"https://schema.org","@type":"Organization",'
      f'"name":"{BRAND}","legalName":"{LEGAL}",'
      f'"url":"https://{SITE}","email":"{EMAIL}","telephone":"{PHONE}","slogan":"Building What\'s Next",'
      '"description":"AI-first technology, talent and digital transformation company.",'
      '"address":{"@type":"PostalAddress","streetAddress":"604, 7th Floor, DSL Abacus IT Park, Uppal Nagole Road, Uppal",'
      '"addressLocality":"Hyderabad","addressRegion":"Telangana","postalCode":"500039","addressCountry":"IN"},'
      f'"identifier":[{{"@type":"PropertyValue","name":"CIN","value":"{CIN}"}},'
      f'{{"@type":"PropertyValue","name":"GSTIN","value":"{GSTIN}"}},'
      f'{{"@type":"PropertyValue","name":"Udyam","value":"{UDYAM}"}}]}}')
    return f"""<!doctype html><html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:type" content="website"><meta property="og:url" content="https://{SITE}/">
<link rel="canonical" href="https://{SITE}/">
<link rel="icon" href="{FAVICON}" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&family=Space+Mono:wght@700&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{schema}</script>
</head>
<body>
<header class="site" id="hdr"><div class="wrap"><nav class="nav">
  <a class="brand" href="{p}index.html" aria-label="Byte Global Technologies home">
    <img class="lg-dark" src="{LOGO_WORD}" alt="Byte Global Technologies">
  </a>
  <div class="menu" id="menu">{menu}</div>
  <div class="nav-cta">
    <a class="btn btn-primary" href="{p}contact.html">Talk to Our Experts</a>
    <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</nav></div></header>
<div class="menu drawer" id="drawer">{menu}<a class="btn btn-primary" href="{p}contact.html">Talk to Our Experts</a></div>
<div class="spacer"></div>
"""

def footer(depth=0):
    p = rel(depth)
    svc = "".join(f'<a href="{p}services/{s[0]}.html">{s[1]}</a>' for s in SERVICES[:6])
    ind = "".join(f'<a href="{p}industries.html">{i[0].split(" & ")[0].split(" (")[0]}</a>' for i in INDUSTRIES[:6])
    glob = "".join(f'<a href="{p}global-presence.html">{m[0]}</a>' for m in MARKETS)
    comp = "".join(f'<a href="{p}{h}">{n}</a>' for h,n in [("about.html","About"),("careers.html","Careers"),("insights.html","Insights"),("contact.html","Contact")])
    return f"""
<footer class="site"><div class="wrap">
  <div class="foot-top">
    <div class="fcol">
      <a class="brand" href="{p}index.html"><img src="{LOGO_LIGHT}" alt="Byte Global Technologies"></a>
      <p class="foot-pos">AI-First · Talent · Transformation</p>
      <p class="foot-desc">Building What's Next — with AI, talent and technology.</p>
      <address class="foot-addr">{'<br>'.join(ADDRESS_LINES)}</address>
      <p class="foot-contact"><a href="mailto:{EMAIL}">{EMAIL}</a><br>
        <a href="tel:{PHONE.replace(' ','')}">{PHONE}</a><br>
        <a href="https://{SITE}">{SITE}</a></p>
    </div>
    <div class="fcol"><h5>Company</h5>{comp}</div>
    <div class="fcol"><h5>Services</h5>{svc}</div>
    <div class="fcol"><h5>Industries</h5>{ind}</div>
    <div class="fcol"><h5>Global</h5>{glob}</div>
  </div>
  <div class="foot-bar">
    <span>© 2026 Byte Global Technologies Private Limited. All Rights Reserved.</span>
    <span class="legal"><a href="#">Privacy Policy</a><a href="#">Terms &amp; Conditions</a><a href="#">Cookie Policy</a><a href="{p}contact.html">Contact</a></span>
  </div>
</div></footer>
<script>{JS}</script>
</body></html>"""

def write(name, body):
    with open(os.path.join(OUT,name),"w") as f: f.write(body)
    print("wrote",name)

JS = """
var _yr=document.getElementById('yr'); if(_yr)_yr.textContent=new Date().getFullYear();
(function(){
  var h=document.getElementById('hdr');
  function s(){h.classList.toggle('solid',window.scrollY>24);}
  window.addEventListener('scroll',s,{passive:true});s();
  var b=document.getElementById('burger'),d=document.getElementById('drawer');
  b&&b.addEventListener('click',function(){var o=d.classList.toggle('open');b.classList.toggle('open',o);b.setAttribute('aria-expanded',o);document.body.style.overflow=o?'hidden':'';});
  d&&d.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){d.classList.remove('open');b.classList.remove('open');document.body.style.overflow='';});});
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
  // counters
  function run(el){var t=+el.dataset.count,suf=el.dataset.suffix||'',dur=1400,st=null;
    function f(ts){st=st||ts;var p=Math.min((ts-st)/dur,1);el.textContent=Math.round(p*t)+suf;if(p<1)requestAnimationFrame(f);}requestAnimationFrame(f);}
  var co=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){run(e.target);co.unobserve(e.target);}});},{threshold:.5});
  document.querySelectorAll('[data-count]').forEach(function(el){co.observe(el);});
})();
"""
print("layout ready")

# ---------------------------------------------------------------- WORLD MAP + HERO
with open(os.path.join(os.path.dirname(__file__),"world_paths.txt")) as f:
    WORLD_PATHS = f.read().strip()
import ast
with open(os.path.join(os.path.dirname(__file__),"world_nodes.txt")) as f:
    WORLD_NODES = ast.literal_eval(f.read().strip())

MARKET_INFO = {
 "India":"Registered office and primary delivery in Hyderabad, Telangana. Engineering, AI and talent.",
 "Germany":"European presence for technology and cross-border talent solutions.",
 "UAE":"Middle East market for technology delivery and recruitment.",
 "United Kingdom":"UK market for consulting, engineering and talent.",
 "United States":"US market for AI, software and enterprise partnerships.",
 "Singapore":"APAC hub for delivery and regional talent.",
 "Australia":"Australia market for technology and talent solutions.",
}

def world_map(depth=0, interactive=True):
    nodes_svg=""; dots=""
    # connection arcs from India hub to all others
    hub = next(n for n in WORLD_NODES if n[0]=="India")
    arcs=""
    for name,x,y in WORLD_NODES:
        if name=="India": continue
        mx,my=(hub[1]+x)/2,(hub[2]+y)/2 - abs(x-hub[1])*0.18-14
        arcs+=f'<path class="arc" d="M{hub[1]} {hub[2]} Q{mx:.0f} {my:.0f} {x} {y}"/>'
    palette = {"India":"#E1493A","Germany":"#F0BB25","United Kingdom":"#46A45B",
               "United States":"#4B84E3","UAE":"#E1493A","Singapore":"#46A45B","Australia":"#4B84E3"}
    for name,x,y in WORLD_NODES:
        big = "hub" if name=="India" else ""
        col = palette.get(name,"#4B84E3")
        nodes_svg+=(f'<g class="node {big}" tabindex="0" role="button" data-name="{name}" '
                    f'data-info="{MARKET_INFO[name]}" transform="translate({x},{y})">'
                    f'<circle class="pulse" r="3" style="fill:{col}"/>'
                    f'<circle class="dotc" r="3.4" style="fill:{col}"/>'
                    f'<text x="0" y="-9">{name}</text></g>')
    panel = ('<div class="map-panel" id="mapPanel" hidden><div class="mp-name"></div>'
             '<div class="mp-info"></div></div>') if interactive else ""
    return f"""
<div class="worldmap">
  <svg viewBox="0 0 1000 500" preserveAspectRatio="xMidYMid meet" aria-label="Global presence map">
    <g class="land"><path d="{WORLD_PATHS}"/></g>
    <g class="arcs">{arcs}</g>
    <g class="nodes">{nodes_svg}</g>
  </svg>
  {panel}
</div>"""

CSS += r"""
.worldmap{position:relative}
.worldmap svg{width:100%;height:auto}
.worldmap .land path{fill:#13315F;stroke:#2C5091;stroke-width:.5}
.soft .worldmap .land path,.phero .worldmap .land path{fill:#C6D6EF;stroke:#AFC5E6;stroke-width:.5}
.worldmap .arc{fill:none;stroke:#1769E0;stroke-width:1.2;opacity:.55;
  stroke-dasharray:6 6;animation:dash 22s linear infinite}
.soft .worldmap .arc,.phero .worldmap .arc{stroke:#0B4DBB;opacity:.45}
@keyframes dash{to{stroke-dashoffset:-400}}
.worldmap .node text{font-family:'Inter';font-size:11px;font-weight:600;fill:#CFE0FF;text-anchor:middle;
  opacity:0;transition:opacity .2s;pointer-events:none}
.soft .worldmap .node text,.phero .worldmap .node text{fill:var(--navy)}
.worldmap .node:hover text,.worldmap .node:focus text,.worldmap .node.hub text{opacity:1}
.worldmap .node .dotc{fill:#1769E0;cursor:pointer}
.worldmap .node.hub .dotc{fill:#EA4335;r:4.4}
.worldmap .node .pulse{fill:#1769E0;opacity:.5;animation:pl 2.4s ease-out infinite}
.worldmap .node.hub .pulse{fill:#EA4335}
@keyframes pl{0%{r:3;opacity:.6}100%{r:16;opacity:0}}
.map-panel{position:absolute;top:14px;left:14px;background:#fff;border:1px solid var(--line);border-radius:12px;
  padding:16px 18px;max-width:280px;box-shadow:var(--shadow-lg)}
.dark .map-panel{background:#0A2151;border-color:#173A7A;color:#D6E1F5}
.map-panel .mp-name{font-family:'Manrope';font-weight:800;color:var(--navy);margin-bottom:4px}
.dark .map-panel .mp-name{color:#fff}
.map-panel .mp-info{font-size:.9rem;color:var(--mute)}
.dark .map-panel .mp-info{color:#AEBFDD}

/* hero */
.hero{position:relative;overflow:hidden;background:
   radial-gradient(1200px 600px at 80% -10%, #0C2A63 0%, transparent 60%), var(--navy)}
.hero .wrap{position:relative;z-index:2}
.hero-canvas{position:absolute;inset:0;z-index:1;opacity:.9}
.hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center;padding:96px 0 104px}
@media(max-width:960px){.hero-grid{grid-template-columns:1fr;padding:64px 0 76px}}
.hero h1{color:#fff}
.hero .kicker{display:inline-flex;gap:8px;align-items:center;color:#8FB6FF;font-weight:700;font-size:.78rem;
  letter-spacing:.16em;text-transform:uppercase;border:1px solid rgba(255,255,255,.16);border-radius:30px;padding:7px 14px;margin-bottom:22px}
.hero p.lead{color:#C6D4EE;margin-top:20px}
.hero-cta{display:flex;gap:14px;flex-wrap:wrap;margin-top:30px}
.hero-tri{margin-top:26px;font-size:.85rem;color:#8497BE;font-weight:600;letter-spacing:.02em}
.hero-tri b{color:#CFE0FF}
.hero-visual{position:relative;z-index:2}
"""

HERO_CANVAS_JS = """
document.querySelectorAll('.js-net').forEach(function(c){
  if(window.matchMedia('(prefers-reduced-motion:reduce)').matches)return;
  var x=c.getContext('2d'),W,H,DPR=Math.min(devicePixelRatio||1,2),cx,cy,R,pts=[],rot=0;
  function size(){W=c.clientWidth;H=c.clientHeight;c.width=W*DPR;c.height=H*DPR;x.setTransform(DPR,0,0,DPR,0,0);
    cx=W*0.72;cy=H*0.46;R=Math.min(W,H)*0.42;build();}
  function build(){pts=[];var N=150;for(var i=0;i<N;i++){var yv=1-(i/(N-1))*2,rr=Math.sqrt(1-yv*yv),
    th=i*2.399963;pts.push([Math.cos(th)*rr,yv,Math.sin(th)*rr]);}}
  function frame(){
    x.clearRect(0,0,W,H);rot+=0.0016;
    var proj=[];
    for(var i=0;i<pts.length;i++){var p=pts[i],
      X=p[0]*Math.cos(rot)-p[2]*Math.sin(rot),Z=p[0]*Math.sin(rot)+p[2]*Math.cos(rot),Y=p[1];
      var sx=cx+X*R,sy=cy+Y*R,dep=(Z+1)/2;proj.push([sx,sy,dep]);}
    for(var i=0;i<proj.length;i++){for(var j=i+1;j<proj.length;j++){
      var a=proj[i],b=proj[j],dx=a[0]-b[0],dy=a[1]-b[1],d=dx*dx+dy*dy;
      if(d<2600){var al=(1-d/2600)*0.28*Math.min(a[2],b[2]);
        x.strokeStyle='rgba(90,150,240,'+al+')';x.lineWidth=.6;
        x.beginPath();x.moveTo(a[0],a[1]);x.lineTo(b[0],b[1]);x.stroke();}}}
    for(var i=0;i<proj.length;i++){var p=proj[i];
      x.beginPath();x.arc(p[0],p[1],1.1+p[2]*1.5,0,6.28);
      x.fillStyle='rgba(120,175,255,'+(0.25+p[2]*0.6)+')';x.fill();}
    requestAnimationFrame(frame);
  }
  size();addEventListener('resize',size);frame();
});
(function(){ // world map interaction
  var panel=document.getElementById('mapPanel');if(!panel)return;
  document.querySelectorAll('.worldmap .node').forEach(function(n){
    function show(){panel.hidden=false;panel.querySelector('.mp-name').textContent=n.dataset.name;
      panel.querySelector('.mp-info').textContent=n.dataset.info;}
    n.addEventListener('click',show);n.addEventListener('focus',show);
    n.addEventListener('mouseenter',show);
  });
})();
"""
print("map + hero components ready")

# ---------------------------------------------------------------- REUSABLE BLOCKS
def trust_strip(depth=0):
    chips="".join(f'<span class="chip">{m[0]}</span>' for m in MARKETS)
    return f"""<section class="trust"><div class="wrap">
      <span class="t-label">Delivering technology and talent solutions across global markets</span>
      <div class="t-markets">{chips}</div></div></section>"""

def services_grid(depth=0, limit=None):
    p=rel(depth); items=SERVICES if limit is None else SERVICES[:limit]
    cards=""
    for i,s in enumerate(items):
        chips="".join(f'<span class="pill-s">{c}</span>' for c in s[4][:3])
        cards+=f"""<a class="svc-card reveal {CYCLE[i%4]}" href="{p}services/{s[0]}.html">
          <div class="svc-top"><span class="ic {CYCLE[i%4]}">{ICONS[s[2]]}</span><span class="num">{i+1:02d}</span></div>
          <h3>{s[1]}</h3><p>{s[3]}</p>
          <div class="svc-tags">{chips}</div>
          <span class="svc-more">Learn more <span class="arr">&rarr;</span></span></a>"""
    return f'<div class="svc-grid">{cards}</div>'

def cta_band(depth=0, title="Let's build what's next together.", sub="Talk to our experts about your technology and talent goals."):
    p=rel(depth)
    return f"""<section class="section"><div class="wrap"><div class="ctaband reveal">
      <div><h2>{title}</h2><p class="lead" style="color:#C6D4EE">{sub}</p></div>
      <a class="btn btn-primary" href="{p}contact.html">Talk to Our Experts <span class="arr">&rarr;</span></a>
    </div></div></section>"""

CSS += r"""
.svc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
@media(max-width:1040px){.svc-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.svc-grid{grid-template-columns:1fr}}
.svc-card{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:26px;display:flex;flex-direction:column;
  transition:transform .2s,border-color .2s,box-shadow .2s}
.svc-card:hover{transform:translateY(-5px);border-color:#C3D5EF;box-shadow:var(--shadow-lg)}
.svc-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:18px}
.svc-card h3{font-size:1.16rem;margin:0 0 8px}
.svc-card p{color:var(--mute);font-size:.94rem;margin:0 0 14px}
.svc-tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px}
.pill-s{font-size:.72rem;font-weight:600;color:var(--blue);background:var(--bg);border:1px solid var(--line);border-radius:20px;padding:4px 10px}
.svc-more{margin-top:auto;font-weight:600;font-size:.9rem;color:var(--bright)}
.svc-card:hover .arr{transform:translateX(3px)}

.ctaband{background:linear-gradient(120deg,var(--blue),var(--navy));border-radius:20px;padding:52px;color:#fff;
  display:flex;align-items:center;justify-content:space-between;gap:30px;flex-wrap:wrap}
.ctaband h2{color:#fff;max-width:20ch}

.split{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
@media(max-width:900px){.split{grid-template-columns:1fr;gap:36px}}
.statgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:26px}
@media(max-width:700px){.statgrid{grid-template-columns:1fr 1fr}}

.ind-card{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:26px;transition:.2s}
.ind-card:hover{transform:translateY(-4px);border-color:#C3D5EF;box-shadow:var(--shadow-lg)}
.ind-card .ic{margin-bottom:16px}
.ind-card h3{font-size:1.1rem;margin:0 0 8px}
.ind-card p{color:var(--mute);font-size:.92rem;margin:0}

.why-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
@media(max-width:900px){.why-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:520px){.why-grid{grid-template-columns:1fr}}
.why-item{display:flex;gap:12px;align-items:flex-start;background:#fff;border:1px solid var(--line);border-radius:12px;padding:18px}
.why-item .wk{width:26px;height:26px;border-radius:7px;background:#E7F0FF;color:var(--blue);display:grid;place-items:center;flex:none}
.why-item .wk svg{width:16px;height:16px}
.why-item span.wt{font-weight:600;font-size:.95rem;color:var(--navy)}

.pipeline{display:flex;align-items:stretch;gap:0;flex-wrap:wrap}
.pipe{flex:1;min-width:150px;background:#fff;border:1px solid var(--line);padding:22px;position:relative}
.pipe:not(:last-child){border-right:none}
.pipe .ps{font-family:'Space Mono';font-size:.72rem;color:var(--bright);font-weight:700}
.pipe h4{margin:8px 0 6px;font-size:1.02rem}
.pipe p{font-size:.86rem;color:var(--mute);margin:0}
.pipe:first-child{border-radius:12px 0 0 12px}.pipe:last-child{border-radius:0 12px 12px 0}
@media(max-width:760px){.pipe{min-width:100%;border-right:1px solid var(--line)!important;border-radius:0!important}}

.journey{display:grid;grid-template-columns:repeat(6,1fr);gap:12px}
@media(max-width:900px){.journey{grid-template-columns:repeat(3,1fr)}}
@media(max-width:520px){.journey{grid-template-columns:1fr 1fr}}
.jstep{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.14);border-radius:12px;padding:18px;text-align:center}
.jstep .jn{font-family:'Space Mono';font-size:.72rem;color:#7FB0FF}
.jstep h4{color:#fff;font-size:1rem;margin:6px 0 0}

.ai-caps{display:flex;flex-wrap:wrap;gap:10px}
.ai-caps .cap{border:1px solid rgba(255,255,255,.2);border-radius:30px;padding:9px 16px;font-size:.9rem;font-weight:600;color:#DCE7FB}

/* brand-colour accents (from the B) */
.ic.c-red{background:var(--red-s);color:var(--red);border-color:transparent}
.ic.c-yellow{background:var(--yellow-s);color:#C7920A;border-color:transparent}
.ic.c-green{background:var(--green-s);color:var(--green);border-color:transparent}
.ic.c-blue{background:var(--accent-blue-s);color:var(--accent-blue);border-color:transparent}
.svc-card.c-red:hover{border-color:var(--red)} .svc-card.c-yellow:hover{border-color:var(--yellow)}
.svc-card.c-green:hover{border-color:var(--green)} .svc-card.c-blue:hover{border-color:var(--accent-blue)}
.svc-card{border-top:3px solid transparent}
.svc-card.c-red{border-top-color:var(--red)} .svc-card.c-yellow{border-top-color:var(--yellow)}
.svc-card.c-green{border-top-color:var(--green)} .svc-card.c-blue{border-top-color:var(--accent-blue)}
.ind-card .ic.c-red,.ind-card .ic.c-yellow,.ind-card .ic.c-green,.ind-card .ic.c-blue{border:none}
.why-item .wk.c-red{background:var(--red-s);color:var(--red)}
.why-item .wk.c-yellow{background:var(--yellow-s);color:#C7920A}
.why-item .wk.c-green{background:var(--green-s);color:var(--green)}
.why-item .wk.c-blue{background:var(--accent-blue-s);color:var(--accent-blue)}
.stat.c-red .n{color:var(--red)} .stat.c-yellow .n{color:#D89B06}
.stat.c-green .n{color:var(--green)} .stat.c-blue .n{color:var(--accent-blue)}
.pipe .ps.c-red{color:var(--red)} .pipe .ps.c-yellow{color:#C7920A}
.pipe .ps.c-green{color:var(--green)} .pipe .ps.c-blue{color:var(--accent-blue)}
.pill-s.c-red{color:var(--red);background:var(--red-s);border-color:transparent}
.pill-s.c-blue{color:var(--accent-blue);background:var(--accent-blue-s);border-color:transparent}
/* dark-section coloured chips keep contrast */
.dark .ai-caps .cap:nth-child(4n+1){border-color:var(--red);color:#F6B8B0}
.dark .ai-caps .cap:nth-child(4n+2){border-color:var(--yellow);color:#F3D889}
.dark .ai-caps .cap:nth-child(4n+3){border-color:var(--green);color:#A6D6B3}
.dark .ai-caps .cap:nth-child(4n+4){border-color:var(--accent-blue);color:#AEC8F4}
"""
CYCLE = ["c-red","c-yellow","c-green","c-blue"]

CSS += r"""
.foot-pos{font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:#7FB0FF;font-weight:700;margin:0 0 10px}
.foot-addr{font-style:normal;color:#93A2C4;font-size:.9rem;line-height:1.6;margin:0 0 12px}
.foot-contact{margin:0;font-size:.9rem;line-height:1.7}
.foot-contact a{color:#B9C6DE}.foot-contact a:hover{color:#fff}
/* corporate credentials */
.creds{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden}
@media(max-width:700px){.creds{grid-template-columns:1fr 1fr}}
@media(max-width:420px){.creds{grid-template-columns:1fr}}
.creds .cell{background:#fff;padding:18px 20px}
.creds .ck{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);font-weight:600;margin-bottom:5px}
.creds .cv{font-family:'Space Mono',monospace;font-weight:700;color:var(--navy);font-size:.92rem;word-break:break-word}
/* office block */
.office{display:grid;grid-template-columns:1fr 1.2fr;gap:0;border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;background:#fff}
@media(max-width:820px){.office{grid-template-columns:1fr}}
.office .oinfo{padding:34px}
.office .oinfo .ol{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--bright);font-weight:700;margin-bottom:10px}
.office address{font-style:normal;color:var(--mute);line-height:1.7;margin:8px 0 20px}
.office .omap{min-height:320px;border:0;width:100%;height:100%;filter:grayscale(.2)}
.office .omap-wrap{background:var(--bg);position:relative;min-height:320px}
.office .omap{position:relative;z-index:2}
.omap-fallback{position:absolute;inset:0;z-index:1;display:flex;gap:14px;align-items:center;justify-content:center;
  padding:24px;text-align:left;color:var(--mute);background:
  repeating-linear-gradient(0deg,var(--line-2) 0 1px,transparent 1px 42px),
  repeating-linear-gradient(90deg,var(--line-2) 0 1px,transparent 1px 42px),var(--bg)}
.omap-fallback strong{color:var(--navy)}
.omap-fallback a{color:var(--bright);font-weight:600}
.omap-fallback .ic{flex:none}
"""

def corp_credentials(depth=0):
    rows=[("Legal Name",LEGAL),("CIN",CIN),("GSTIN",GSTIN),("Udyam Registration",UDYAM),
          ("Company Type",COMPANY_TYPE),("Primary Location","Hyderabad, Telangana, India")]
    cells="".join(f'<div class="cell"><div class="ck">{k}</div><div class="cv">{v}</div></div>' for k,v in rows)
    return f'<div class="creds">{cells}</div>'

def office_block():
    return f"""<div class="office">
      <div class="oinfo">
        <div class="ol">Registered &amp; Principal Office</div>
        <h3>{BRAND} Pvt. Ltd.</h3>
        <address>{'<br>'.join(ADDRESS_LINES)}</address>
        <a class="btn btn-primary" href="{MAPS_DIR}" target="_blank" rel="noopener">Get Directions <span class="arr">&rarr;</span></a>
      </div>
      <div class="omap-wrap">
        <div class="omap-fallback"><span class="ic">{ICONS["gov"]}</span><div><strong>Uppal, Hyderabad</strong><br><a href="{MAPS_DIR}" target="_blank" rel="noopener">Open in Google Maps &rarr;</a></div></div>
        <iframe class="omap" src="{MAPS_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Byte Global Technologies — Hyderabad office map"></iframe>
      </div>
    </div>"""
print("blocks ready")

# ---------------------------------------------------------------- HOME
def page_home():
    b = head("Byte Global Technologies — Building What's Next",
             "AI-first global technology, talent and digital transformation company. Software, cloud, cybersecurity, talent solutions and overseas recruitment.","index.html")
    # hero
    b += f"""
<section class="hero">
  <canvas class="hero-canvas js-net"></canvas>
  <div class="wrap"><div class="hero-grid">
    <div class="reveal">
      <span class="kicker">AI-First · Talent · Transformation</span>
      <h1>Building What's Next with AI, Talent &amp; Technology</h1>
      <p class="lead">Empowering businesses worldwide with intelligent technology, exceptional talent and innovative solutions to accelerate growth.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="contact.html">Talk to Our Experts <span class="arr">&rarr;</span></a>
        <a class="btn btn-outline" href="services.html">Explore Our Services</a>
      </div>
      <div class="hero-tri"><b>Technology</b> • <b>Talent</b> • <b>Transformation</b></div>
    </div>
    <div class="hero-visual reveal">{world_map(interactive=False)}</div>
  </div></div>
</section>
{trust_strip()}
"""
    # about + stats
    b += f"""
<section class="section soft"><div class="wrap split">
  <div class="reveal">
    <div class="eyebrow">About Byte Global</div>
    <h2>Technology That Moves Business Forward</h2>
    <p class="lead" style="margin-top:18px">Byte Global Technologies combines intelligent technology, skilled professionals and strategic transformation capabilities to help organizations build, scale and evolve.</p>
    <p style="color:var(--mute)">We work across technology, AI, cloud, cybersecurity, talent, digital transformation, learning and global recruitment — as one partner, not eight vendors.</p>
    <a class="btn btn-outline" href="about.html" style="margin-top:8px">More about us</a>
  </div>
  <div class="reveal"><div class="statgrid">
    <div class="stat c-red"><div class="n"><span data-count="10" data-suffix="+">10+</span></div><div class="l">Technology Capabilities</div></div>
    <div class="stat c-yellow"><div class="n"><span data-count="8" data-suffix="+">8+</span></div><div class="l">Core Service Areas</div></div>
    <div class="stat c-green"><div class="n"><span data-count="7">7</span></div><div class="l">Global Markets</div></div>
    <div class="stat c-blue"><div class="n">360°</div><div class="l">Technology &amp; Talent Solutions</div></div>
  </div>
  <div class="bar4" style="margin-top:26px"></div></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="center reveal" style="max-width:720px;margin:0 auto 48px">
    <div class="eyebrow" style="justify-content:center">Our Core Services</div>
    <h2>Eight ways we help you build, scale and evolve</h2>
  </div>
  {services_grid()}
</div></section>

<section class="section soft"><div class="wrap">
  <div class="center reveal" style="max-width:720px;margin:0 auto 48px">
    <div class="eyebrow" style="justify-content:center">Industries We Serve</div>
    <h2>Deep expertise across regulated, complex sectors</h2>
  </div>
  <div class="grid g3">
"""
    for i,(name,ic,desc) in enumerate(INDUSTRIES):
        b+=f'<div class="ind-card reveal"><span class="ic {CYCLE[i%4]}">{ICONS[ic]}</span><h3>{name}</h3><p>{desc}</p></div>'
    b+="""</div></div></section>"""

    # AI-first dark section
    caps=["Generative AI","AI Automation","AI Consulting","AI Integration","AI Strategy","AI-Powered Analytics"]
    b+=f"""
<section class="section dark"><div class="wrap split">
  <div class="reveal">
    <div class="eyebrow">AI-First</div>
    <h2>AI is changing business.<br>We help you build for it.</h2>
    <p class="lead" style="color:#C6D4EE;margin-top:18px">From generative AI and intelligent automation to enterprise AI integration, Byte Global helps organizations identify, implement and scale practical AI opportunities.</p>
    <div class="ai-caps" style="margin:22px 0 26px">{''.join(f'<span class="cap">{c}</span>' for c in caps)}</div>
    <a class="btn btn-primary" href="services/artificial-intelligence.html">Explore AI Solutions <span class="arr">&rarr;</span></a>
  </div>
  <div class="reveal"><canvas class="hero-canvas js-net" style="position:relative;height:360px;border:1px solid rgba(255,255,255,.12);border-radius:16px"></canvas></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="center reveal" style="max-width:720px;margin:0 auto 44px">
    <div class="eyebrow" style="justify-content:center">Why Partner With Byte?</div>
    <h2>Built for outcomes, engaged for the long term</h2>
  </div>
  <div class="why-grid">
    {''.join(f'<div class="why-item reveal"><span class="wk {CYCLE[i%4]}">{ICONS["check"]}</span><span class="wt">{w}</span></div>' for i,w in enumerate(WHY))}
  </div>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="center reveal" style="max-width:760px;margin:0 auto 40px">
    <div class="eyebrow" style="justify-content:center">Global Presence</div>
    <h2>Connecting businesses with technology and talent across borders</h2>
  </div>
  <div class="reveal">{world_map()}</div>
</div></section>

<section class="section soft"><div class="wrap">
  <div class="reveal" style="max-width:640px;margin-bottom:40px">
    <div class="eyebrow">People. Technology. Possibility.</div>
    <h2>A talent ecosystem built to move fast</h2>
    <p class="lead" style="margin-top:16px">From IT staffing to executive and cross-border hiring, we run a structured pipeline that finds the right people and keeps them.</p>
  </div>
  <div class="pipeline reveal">
    {''.join(f'<div class="pipe"><div class="ps {CYCLE[i%4]}">0{i+1}</div><h4>{s}</h4><p>{d}</p></div>' for i,(s,d) in enumerate([("Discover","Source from a global talent network."),("Assess","Vet for skills, fit and reliability."),("Match","Align talent to your exact needs."),("Deploy","Onboard and integrate quickly."),("Support","Retain with ongoing enablement.")]))}
  </div>
  <div style="margin-top:26px"><a class="btn btn-primary" href="talent.html">Find Your Talent <span class="arr">&rarr;</span></a></div>
</div></section>
{cta_band()}
"""
    b += footer()
    write("index.html", b)

# ---------------------------------------------------------------- SERVICES OVERVIEW + DETAIL
def page_services():
    b=head("Services — Byte Global Technologies","AI, software engineering, cloud, cybersecurity, talent solutions, learning, digital transformation and overseas recruitment.","services.html")
    b+=f"""<section class="phero"><div class="wrap reveal">
      <div class="eyebrow">Our Core Services</div>
      <h1>Technology and talent, engineered for outcomes</h1>
      <p class="lead">Eight capabilities delivered as one partnership — from AI and software to global recruitment.</p>
    </div></section>
    <section class="section"><div class="wrap">{services_grid()}</div></section>
    <section class="section soft"><div class="wrap">
      <div class="center reveal" style="max-width:700px;margin:0 auto 44px"><div class="eyebrow" style="justify-content:center">Engagement Models</div><h2>Flexible ways to work together</h2></div>
      <div class="grid g3">{''.join(f'<div class="card reveal"><h3>{t}</h3><p>{d}</p></div>' for t,d in ENGAGE)}</div>
      <div class="center" style="margin-top:32px"><a class="btn btn-primary" href="contact.html">Discuss Your Requirements <span class="arr">&rarr;</span></a></div>
    </div></section>
    {cta_band()}"""
    b+=footer(); write("services.html",b)

def page_service_detail(s):
    slug,name,ic,tag,chips,ctatext,problem,approach,caps=s
    others="".join(f'<a class="pill-s" href="{o[0]}.html">{o[1]}</a>' for o in SERVICES if o[0]!=slug)
    capli="".join(f'<li>{ICONS["check"]}<span>{c}</span></li>' for c in caps)
    industries="".join(f'<span class="chip">{i[0].split(" & ")[0]}</span>' for i in INDUSTRIES[:6])
    b=head(f"{name} — Byte Global Technologies", tag, "Services", depth=1)
    b+=f"""<section class="phero"><div class="wrap reveal" style="max-width:820px">
      <div class="eyebrow"><span class="ic" style="width:34px;height:34px">{ICONS[ic]}</span> Service</div>
      <h1>{name}</h1><p class="lead">{tag}</p>
      <div style="margin-top:22px"><a class="btn btn-primary" href="../contact.html">{ctatext} <span class="arr">&rarr;</span></a></div>
    </div></section>
    <section class="section"><div class="wrap split">
      <div class="reveal"><div class="eyebrow">The challenge</div><h2 style="font-size:2rem">Problem statement</h2>
        <p class="lead" style="margin-top:14px">{problem}</p>
        <div class="eyebrow" style="margin-top:30px">Our approach</div><p style="color:var(--mute);font-size:1.05rem">{approach}</p></div>
      <div class="reveal"><div class="card"><h3>Capabilities</h3><ul class="capli">{capli}</ul></div></div>
    </div></section>
    <section class="section soft"><div class="wrap">
      <div class="split">
        <div class="reveal"><div class="eyebrow">Industries served</div><h2 style="font-size:1.9rem">Where this delivers value</h2>
          <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:18px">{industries}</div>
          <div class="eyebrow" style="margin-top:34px">Engagement models</div>
          <p style="color:var(--mute)">Dedicated teams, project-based delivery, staff augmentation, managed services or consulting — matched to your goals.</p></div>
        <div class="reveal"><div class="card"><h3>Why Byte Global</h3>
          <ul class="capli">{''.join(f'<li>{ICONS["check"]}<span>{w}</span></li>' for w in WHY[:5])}</ul></div></div>
      </div>
    </div></section>
    <section class="section tight"><div class="wrap reveal">
      <div class="eyebrow">Explore more services</div>
      <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:12px">{others}</div>
    </div></section>
    {cta_band(depth=1, title=ctatext+" with Byte Global.")}"""
    b+=footer(depth=1)
    with open(os.path.join(OUT,"services",f"{slug}.html"),"w") as f: f.write(b)
    print("wrote services/"+slug+".html")

CSS += r"""
.capli{list-style:none;margin:0;padding:0}
.capli li{display:flex;gap:12px;align-items:center;padding:11px 0;border-top:1px solid var(--line-2);color:var(--navy);font-weight:500}
.capli li:first-child{border-top:none}
.capli li svg{width:18px;height:18px;color:var(--green);flex:none}
"""

# ---------------------------------------------------------------- INDUSTRIES / TALENT / GLOBAL
def page_industries():
    b=head("Industries — Byte Global Technologies","Technology and talent solutions across banking, healthcare, manufacturing, retail, education, telecom, government, logistics and energy.","industries.html")
    b+=f"""<section class="phero"><div class="wrap reveal"><div class="eyebrow">Industries We Serve</div>
      <h1>Solutions shaped by the sectors we serve</h1><p class="lead">Regulated, complex and fast-moving — we bring the right technology and talent to each.</p></div></section>
    <section class="section"><div class="wrap"><div class="grid g3">
    {''.join(f'<div class="ind-card reveal"><span class="ic {CYCLE[i%4]}">{ICONS[ic]}</span><h3>{n}</h3><p>{d}</p></div>' for i,(n,ic,d) in enumerate(INDUSTRIES))}
    </div></div></section>{cta_band()}"""
    b+=footer(); write("industries.html",b)

def page_talent():
    b=head("Talent Solutions — Byte Global Technologies","IT staffing, contract and executive hiring, GCC recruitment and cross-border talent — discover, assess, match, deploy, support.","Talent Solutions")
    steps=[("Discover","Source from a global talent network."),("Assess","Vet for skills, fit and reliability."),("Match","Align talent to your exact needs."),("Deploy","Onboard and integrate quickly."),("Support","Retain with ongoing enablement.")]
    svcs=["IT Staffing","Contract Staffing","Executive Hiring","GCC Recruitment","Global Talent Sourcing","Overseas Recruitment"]
    b+=f"""<section class="phero"><div class="wrap reveal"><div class="eyebrow">People. Technology. Possibility.</div>
      <h1>The talent to build what's next</h1><p class="lead">A structured pipeline and a global network — so you get the right people, faster, and keep them longer.</p>
      <div style="margin-top:22px"><a class="btn btn-primary" href="contact.html">Find Your Talent <span class="arr">&rarr;</span></a></div></div></section>
    <section class="section"><div class="wrap">
      <div class="grid g3" style="margin-bottom:52px">{''.join(f'<div class="card reveal"><h3>{s}</h3><p>Specialised {s.lower()} backed by rigorous assessment and a global bench.</p></div>' for s in svcs)}</div>
      <div class="reveal"><div class="eyebrow">The pipeline</div><h2 style="font-size:2rem;margin-bottom:24px">Discover → Assess → Match → Deploy → Support</h2></div>
      <div class="pipeline reveal">{''.join(f'<div class="pipe"><div class="ps {CYCLE[i%4]}">0{i+1}</div><h4>{s}</h4><p>{d}</p></div>' for i,(s,d) in enumerate(steps))}</div>
    </div></section>{cta_band(title="Find your next hire with Byte Global.")}"""
    b+=footer(); write("talent.html",b)

def page_global():
    b=head("Global Presence — Byte Global Technologies","Delivering technology and talent across India, Germany, UAE, UK, USA, Singapore and Australia.","Global Presence")
    cards="".join(f"""<div class="card reveal"><h3>{m[0]}</h3><p>{MARKET_INFO[m[0]]}</p>
      <a class="svc-more" href="contact.html" style="margin-top:14px;display:inline-block">Contact this market <span class="arr">&rarr;</span></a></div>""" for m in MARKETS)
    b+=f"""<section class="phero"><div class="wrap reveal"><div class="eyebrow">Global Presence</div>
      <h1>Connecting businesses across borders</h1><p class="lead">Headquartered in Hyderabad, India, with reach across global markets. Select a market to see how we serve it.</p></div></section>
    <section class="section"><div class="wrap reveal">
      <div class="eyebrow">Office · India</div><h2 style="font-size:2rem;margin-bottom:24px">Our headquarters</h2>
      {office_block()}
    </div></section>
    <section class="section soft"><div class="wrap">
      <div class="center reveal" style="max-width:720px;margin:0 auto 40px"><div class="eyebrow" style="justify-content:center">Global Markets</div>
      <h2>Global reach, delivered from India</h2>
      <p class="lead" style="margin:14px auto 0">The locations below are markets we serve, not separate offices. Our registered office is in Hyderabad, India.</p></div>
      <div class="reveal">{world_map()}</div></div></section>
    <section class="section"><div class="wrap">
      <div class="reveal" style="margin-bottom:26px"><div class="eyebrow">Global Markets</div><h2 style="font-size:2rem">Where we operate</h2></div>
      <div class="grid g3">{cards}</div></div></section>{cta_band()}"""
    b+=footer(); write("global-presence.html",b)

# ---------------------------------------------------------------- INSIGHTS / CAREERS / ABOUT / CONTACT
def page_insights():
    b=head("Insights — Byte Global Technologies","Perspectives on AI, cloud, cybersecurity, digital transformation, talent and recruitment.","Insights")
    cards=""
    for cat,title,desc in INSIGHTS:
        cards+=f"""<article class="card reveal"><span class="pill-s">{cat}</span>
          <h3 style="margin:14px 0 8px">{title}</h3><p>{desc}</p>
          <div class="ins-foot"><span class="num">CMS · Draft</span><a class="svc-more" href="#">Read Article <span class="arr">&rarr;</span></a></div></article>"""
    b+=f"""<section class="phero"><div class="wrap reveal"><div class="eyebrow">Insights &amp; Resources</div>
      <h1>Ideas on technology, talent and transformation</h1>
      <p class="lead">Articles below are structured placeholders ready for your team to publish through a CMS.</p></div></section>
    <section class="section"><div class="wrap"><div class="grid g3">{cards}</div></div></section>{cta_band()}"""
    b+=footer(); write("insights.html",b)

CSS += r""".ins-foot{display:flex;justify-content:space-between;align-items:center;margin-top:18px;padding-top:14px;border-top:1px solid var(--line-2)}
.job{display:grid;grid-template-columns:2fr 1fr 1fr 1fr auto;gap:16px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:12px;padding:20px 24px;margin-bottom:12px}
.job h4{margin:0;font-size:1.05rem}.job .jm{font-size:.88rem;color:var(--mute)}
@media(max-width:760px){.job{grid-template-columns:1fr 1fr;gap:8px}.job .japply{grid-column:1/-1}}
.cform{display:grid;gap:16px}.cform .two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:560px){.cform .two{grid-template-columns:1fr}}
.cform label{font-size:.78rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--mute);display:block;margin-bottom:6px}
.cform input,.cform select,.cform textarea{width:100%;background:#fff;border:1px solid var(--line);border-radius:10px;padding:13px 14px;color:var(--ink);font-family:inherit;font-size:.98rem}
.cform input:focus,.cform select:focus,.cform textarea:focus{outline:none;border-color:var(--bright);box-shadow:0 0 0 3px rgba(23,105,224,.12)}
.contact-grid{display:grid;grid-template-columns:1.3fr .9fr;gap:44px;align-items:start}
@media(max-width:860px){.contact-grid{grid-template-columns:1fr}}
.cinfo .row{display:flex;gap:14px;align-items:flex-start;padding:16px 0;border-top:1px solid var(--line-2)}
.cinfo .row:first-child{border-top:none}.cinfo .ic{flex:none}
.cinfo .row a,.cinfo .row span.v{color:var(--navy);font-weight:600}
.success{background:#ECFDF3;border:1px solid #ABEFC6;color:#067647;border-radius:10px;padding:14px 16px;font-weight:600;display:none}
"""

def page_careers():
    b=head("Careers — Byte Global Technologies","Build your career in technology, AI, engineering, consulting and talent — with global opportunities.","careers.html")
    jobs=""
    for t,loc,typ,dept,exp in JOBS:
        jobs+=f"""<div class="job reveal"><div><h4>{t}</h4><div class="jm">{dept}</div></div>
          <div class="jm">{loc}</div><div class="jm">{typ}</div><div class="jm">{exp}</div>
          <a class="btn btn-outline japply" href="contact.html">Apply</a></div>"""
    b+=f"""<section class="phero"><div class="wrap reveal"><div class="eyebrow">Careers</div>
      <h1>Build your career with Byte</h1><p class="lead">Work on technology, AI, engineering, consulting and talent — with opportunities across our global markets.</p>
      <div style="margin-top:22px"><a class="btn btn-primary" href="#roles">Explore Open Positions <span class="arr">&rarr;</span></a></div></div></section>
    <section class="section" id="roles"><div class="wrap">
      <div class="reveal" style="margin-bottom:26px"><div class="eyebrow">Open positions</div><h2 style="font-size:2rem">Roles we're hiring for</h2>
      <p style="color:var(--mute);max-width:60ch">The listings below are placeholders — connect your ATS or CMS to publish live roles.</p></div>
      {jobs}
    </div></section>{cta_band(title="Don't see your role? Introduce yourself.")}"""
    b+=footer(); write("careers.html",b)

def page_about():
    b=head("About — Byte Global Technologies","A global technology, talent and digital-transformation company. AI-first, enterprise-ready, globally delivered.","about.html")
    journey=["Assess","Strategize","Design","Build","Integrate","Scale"]
    b+=f"""<section class="phero"><div class="wrap reveal" style="max-width:820px"><div class="eyebrow">About Byte Global</div>
      <h1>Technology that moves business forward</h1>
      <p class="lead">Byte Global Technologies combines intelligent technology, skilled professionals and strategic transformation capabilities to help organizations build, scale and evolve.</p></div></section>
    <section class="section"><div class="wrap split">
      <div class="reveal"><div class="eyebrow">What we do</div><h2 style="font-size:2rem">One partner across the stack</h2>
        <p class="lead" style="margin-top:14px">We work across technology, AI, cloud, cybersecurity, talent, digital transformation, learning and global recruitment.</p>
        <p style="color:var(--mute)">The result is fewer handoffs, tighter alignment and outcomes that connect — instead of a patchwork of point vendors.</p></div>
      <div class="reveal"><div class="statgrid">
        <div class="stat c-red"><div class="n"><span data-count="10" data-suffix="+">10+</span></div><div class="l">Technology Capabilities</div></div>
        <div class="stat c-yellow"><div class="n"><span data-count="8" data-suffix="+">8+</span></div><div class="l">Core Service Areas</div></div>
        <div class="stat c-green"><div class="n"><span data-count="7">7</span></div><div class="l">Global Markets</div></div>
        <div class="stat c-blue"><div class="n">360°</div><div class="l">Technology &amp; Talent</div></div>
      </div><div class="bar4" style="margin-top:24px"></div></div>
    </div></section>
    <section class="section dark"><div class="wrap">
      <div class="reveal" style="max-width:680px;margin-bottom:36px"><div class="eyebrow">Digital Transformation</div>
      <h2>Transform today. Compete tomorrow.</h2>
      <p class="lead" style="color:#C6D4EE;margin-top:16px">We combine technology, people, process, data and AI into scalable transformation programs.</p></div>
      <div class="journey reveal">{''.join(f'<div class="jstep"><div class="jn">0{i+1}</div><h4>{s}</h4></div>' for i,s in enumerate(journey))}</div>
    </div></section>
    <section class="section"><div class="wrap">
      <div class="center reveal" style="max-width:700px;margin:0 auto 40px"><div class="eyebrow" style="justify-content:center">Why Partner With Byte?</div><h2>What sets us apart</h2></div>
      <div class="why-grid">{''.join(f'<div class="why-item reveal"><span class="wk {CYCLE[i%4]}">{ICONS["check"]}</span><span class="wt">{w}</span></div>' for i,w in enumerate(WHY))}</div>
    </div></section>
    <section class="section soft"><div class="wrap">
      <div class="split" style="align-items:start">
        <div class="reveal"><div class="eyebrow">Company Information</div>
          <h2 style="font-size:2rem">Who we are</h2>
          <p class="lead" style="margin-top:16px">Byte Global Technologies Private Limited is a technology and services company focused on AI, software engineering, cloud and infrastructure, cybersecurity, talent solutions, learning and development, digital transformation, and overseas recruitment.</p>
          <p style="color:var(--mute)">Our registered and principal place of business is in Hyderabad, Telangana, India.</p>
        </div>
        <div class="reveal"><div class="eyebrow">Corporate Information</div>
          <h2 style="font-size:2rem;margin-bottom:18px">Credentials</h2>
          {corp_credentials()}
        </div>
      </div>
    </div></section>{cta_band()}"""
    b+=footer(); write("about.html",b)

def page_contact():
    b=head("Contact — Byte Global Technologies","Talk to our experts about AI, technology and talent. Registered office in Hyderabad, Telangana, India.","contact.html")
    svc_opts="".join(f"<option>{s[1]}</option>" for s in SERVICES)
    ctry_opts="".join(f"<option>{m[0]}</option>" for m in MARKETS)
    b+=f"""<section class="phero"><div class="wrap reveal"><div class="eyebrow">Contact</div>
      <h1>Let's Build What's Next Together</h1><p class="lead">Connect with Byte Global Technologies to discuss AI, technology, talent and digital transformation opportunities.</p></div></section>
    <section class="section"><div class="wrap contact-grid">
      <div class="reveal"><form class="cform" onsubmit="event.preventDefault();document.getElementById('ok').style.display='block';this.reset();">
        <div class="two"><div><label>Full Name</label><input required placeholder="Your name"></div><div><label>Work Email</label><input type="email" required placeholder="you@company.com"></div></div>
        <div class="two"><div><label>Phone</label><input placeholder="+91 …"></div><div><label>Company</label><input placeholder="Company name"></div></div>
        <div class="two"><div><label>Country</label><select>{ctry_opts}<option>Other</option></select></div><div><label>Service Required</label><select>{svc_opts}</select></div></div>
        <div class="two"><div><label>Budget Range</label><select><option>To be discussed</option><option>&lt; $25k</option><option>$25k–$100k</option><option>$100k–$500k</option><option>$500k+</option></select></div><div><label>Project / Requirement</label><input placeholder="Short summary"></div></div>
        <div><label>Message</label><textarea rows="5" placeholder="How can we help?"></textarea></div>
        <div id="ok" class="success">Thank you. Our team will get back to you shortly.</div>
        <button class="btn btn-primary" type="submit">Send Inquiry <span class="arr">&rarr;</span></button>
        <p class="num" style="color:var(--mute)">Demo form — connect to your backend or a form service before going live.</p>
      </form></div>
      <div class="reveal"><div class="card cinfo">
        <div class="row"><span class="ic">{ICONS["gov"]}</span><div><div class="num">Registered Office</div><address style="font-style:normal;color:var(--navy);font-weight:600;line-height:1.6">{'<br>'.join(ADDRESS_LINES)}</address></div></div>
        <div class="row"><span class="ic">{ICONS["spark"]}</span><div><div class="num">Email</div><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
        <div class="row"><span class="ic">{ICONS["signal"]}</span><div><div class="num">Phone</div><a href="tel:{PHONE.replace(' ','')}">{PHONE}</a></div></div>
        <div class="row"><span class="ic">{ICONS["globe2"]}</span><div><div class="num">Website</div><a href="https://{SITE}">{SITE}</a></div></div>
        <div style="display:flex;gap:10px;margin-top:18px">
          <a class="btn btn-primary" href="{MAPS_DIR}" target="_blank" rel="noopener" style="flex:1;justify-content:center">Get Directions</a>
          <a class="btn btn-outline" href="https://wa.me/{PHONE.replace(' ','').replace('+','')}" target="_blank" rel="noopener" style="flex:1;justify-content:center">WhatsApp</a>
        </div>
      </div></div>
    </div></section>
    <section class="section tight soft"><div class="wrap reveal">
      <div class="eyebrow">Visit us</div><h2 style="font-size:2rem;margin-bottom:24px">Our Hyderabad office</h2>
      {office_block()}
    </div></section>
    <section class="section tight"><div class="wrap reveal">
      <div class="eyebrow">Corporate Information</div><h2 style="font-size:1.7rem;margin-bottom:20px">Company credentials</h2>
      {corp_credentials()}
    </div></section>"""
    b+=footer(); write("contact.html",b)

def main():
    page_home(); page_services()
    for s in SERVICES: page_service_detail(s)
    page_industries(); page_talent(); page_global()
    page_insights(); page_careers(); page_about(); page_contact()
    print("\nBUILD COMPLETE →", OUT)

if __name__=="__main__":
    main()
