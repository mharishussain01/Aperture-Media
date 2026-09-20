#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aperture Media: static site generator.

    python3 build.py            # writes the deployable site to ../site
    python3 build.py --local    # same, but links end in index.html so pages open by double-click

Content lives in content.py. Styles and scripts live in assets/.
"""
import html, json, math, shutil, sys, datetime
from pathlib import Path
from content import *

HERE = Path(__file__).parent
LOCAL = "--local" in sys.argv
OUT = HERE.parent / ("site-local" if LOCAL else "site")
YEAR = datetime.date.today().year
esc = lambda s: html.escape(str(s), quote=True)

# ------------------------------------------------------------------ art (flat, top-down food illustrations)
ART = {
"pizza": """<circle cx="100" cy="100" r="86" fill="#f5f6f1"/><circle cx="100" cy="100" r="74" fill="#e9a652"/>
<circle cx="100" cy="100" r="65" fill="#e8452c"/><circle cx="100" cy="100" r="60" fill="#ffe39a"/>
<g fill="#c22b1e"><circle cx="78" cy="78" r="10"/><circle cx="124" cy="72" r="10"/><circle cx="134" cy="114" r="10"/><circle cx="92" cy="130" r="10"/><circle cx="64" cy="108" r="9"/><circle cx="104" cy="99" r="8"/></g>
<g fill="#2f8f5b"><ellipse cx="102" cy="58" rx="10" ry="5" transform="rotate(30 102 58)"/><ellipse cx="146" cy="92" rx="10" ry="5" transform="rotate(-40 146 92)"/><ellipse cx="72" cy="132" rx="10" ry="5" transform="rotate(50 72 132)"/><ellipse cx="118" cy="140" rx="9" ry="4.5" transform="rotate(-20 118 140)"/></g>""",
"ramen": """<circle cx="100" cy="100" r="86" fill="#f5f6f1"/><circle cx="100" cy="100" r="76" fill="#12112e"/><circle cx="100" cy="100" r="68" fill="#e9a652"/>
<g fill="none" stroke="#ffe9a8" stroke-width="5" stroke-linecap="round"><path d="M46 104c20-26 40 26 60 0s30-22 46 0"/><path d="M50 122c20-26 40 26 60 0s26-18 38 0"/><path d="M54 86c20-26 40 26 60 0s22-18 34 0"/></g>
<ellipse cx="76" cy="74" rx="18" ry="14" fill="#fff"/><circle cx="76" cy="74" r="7" fill="#ffb020"/>
<rect x="124" y="56" width="22" height="32" rx="3" fill="#1c3b2c" transform="rotate(14 135 72)"/>
<g fill="#6cc24a"><circle cx="112" cy="124" r="4"/><circle cx="122" cy="130" r="4"/><circle cx="102" cy="132" r="4"/><circle cx="96" cy="66" r="4"/></g>""",
"burger": """<circle cx="100" cy="100" r="86" fill="#f5f6f1"/>
<path d="M44 96c0-36 24-52 56-52s56 16 56 52z" fill="#e9a652"/>
<g fill="#fff4d6"><ellipse cx="80" cy="66" rx="5" ry="2.6" transform="rotate(-20 80 66)"/><ellipse cx="104" cy="58" rx="5" ry="2.6"/><ellipse cx="126" cy="72" rx="5" ry="2.6" transform="rotate(25 126 72)"/><ellipse cx="94" cy="82" rx="5" ry="2.6" transform="rotate(10 94 82)"/></g>
<path d="M38 100c8 9 14-5 22 3s14-5 22 3 14-5 22 3 14-5 22 3 14-5 22 3v6H38z" fill="#5dbb63"/>
<path d="M42 108h116l-12 16-12-8-12 8-12-8-12 8-12-8-12 8-12-8z" fill="#ffd35c"/>
<rect x="40" y="112" width="120" height="20" rx="10" fill="#5a2e1b"/>
<path d="M44 136h112v4c0 10-10 16-22 16H66c-12 0-22-6-22-16z" fill="#e9a652"/>""",
"drink": """<circle cx="100" cy="100" r="86" fill="#f5f6f1"/><circle cx="100" cy="100" r="76" fill="#ff8fab"/>
<g fill="#fff" opacity=".6"><rect x="52" y="60" width="30" height="30" rx="7" transform="rotate(-14 67 75)"/><rect x="60" y="118" width="28" height="28" rx="7" transform="rotate(20 74 132)"/><rect x="122" y="128" width="26" height="26" rx="7" transform="rotate(-8 135 141)"/></g>
<circle cx="116" cy="86" r="34" fill="#ffd35c"/><circle cx="116" cy="86" r="27" fill="#ffe9a8"/>
<g stroke="#ffd35c" stroke-width="3"><path d="M116 59v54M92.6 72.5l46.8 27M92.6 99.5l46.8-27"/></g>
<path d="M62 152 108 62" stroke="#1e1b5c" stroke-width="8" stroke-linecap="round"/>""",
"donut": """<circle cx="100" cy="100" r="86" fill="#f5f6f1"/><circle cx="100" cy="100" r="66" fill="#e9a652"/><circle cx="100" cy="100" r="57" fill="#ff5a87"/><circle cx="100" cy="100" r="19" fill="#f5f6f1"/>
<g stroke-width="4" stroke-linecap="round"><path d="M70 74l8-4" stroke="#ffd35c"/><path d="M118 62l8 5" stroke="#fff"/><path d="M138 96l8-2" stroke="#ffd35c"/><path d="M134 128l6 6" stroke="#fff"/><path d="M96 142l4 8" stroke="#ffd35c"/><path d="M62 118l-8 4" stroke="#fff"/><path d="M84 58l-2-8" stroke="#bde7cf"/><path d="M148 116l6-2" stroke="#bde7cf"/><path d="M112 146l-4-6" stroke="#bde7cf"/></g>""",
"coffee": """<circle cx="100" cy="100" r="86" fill="#f5f6f1"/><circle cx="100" cy="100" r="72" fill="#dfe1ec"/>
<rect x="138" y="90" width="34" height="20" rx="10" fill="#fff"/><circle cx="100" cy="100" r="54" fill="#fff"/><circle cx="100" cy="100" r="45" fill="#6b3f2a"/>
<path d="M100 128c-24-15-30-28-21-37 8-7 17-3 21 5 4-8 13-12 21-5 9 9 3 22-21 37z" fill="#f5e6d0"/>""",
}
TILE_BG = {"butter": "#ffd35c", "radish": "#ff5a87", "blue": "#2b2782", "lilac": "#d6d2ff", "mint": "#bde7cf", "peach": "#ffcba6"}

def art(name):
    return f'<svg viewBox="0 0 200 200" aria-hidden="true" focusable="false">{ART[name]}</svg>'

def tile(name, color, cls="", style=""):
    st = f' style="{style}"' if style else ""
    return f'<div class="tile t-{color} {cls}"{st} aria-hidden="true">{art(name)}</div>'

PLAY = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 1.5v13l11-6.5z" fill="#12112e"/></svg>'

def mark():
    pts = "16,8 22.9,12 22.9,20 16,24 9.1,20 9.1,12"
    return (f'<svg viewBox="0 0 32 32" aria-hidden="true" focusable="false"><circle class="m-disc" cx="16" cy="16" r="15" fill="#1e1b5c"/>'
            f'<polygon class="m-hex" points="{pts}" fill="#ffd35c"/></svg>')

def iris(art_name="pizza"):
    lines = []
    for k in range(6):
        a = math.radians(-90 + 60 * k)
        b = a + math.radians(40)
        x1, y1 = 50 + 40 * math.cos(a), 50 + 40 * math.sin(a)
        x2, y2 = 50 + 49 * math.cos(b), 50 + 49 * math.sin(b)
        lines.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"/>')
    return (f'<div class="iris" role="img" aria-label="A camera aperture opening to reveal a pizza seen from above">'
            f'<div class="iris__disc"></div>'
            f'<svg class="iris__lines" viewBox="0 0 100 100" aria-hidden="true" stroke="rgba(255,255,255,.22)" stroke-width=".35">{"".join(lines)}</svg>'
            f'<div class="iris__view">{art(art_name)}</div></div>')

# ------------------------------------------------------------------ page context + shell
class Ctx:
    def __init__(self, path, absolute=False):
        self.path = path                      # e.g. "about/" or "case-studies/ember-and-oak/"
        self.depth = 0 if path == "" else path.strip("/").count("/") + 1
        self.absolute = absolute

    @property
    def root(self):
        if self.absolute: return "/"
        return "../" * self.depth if self.depth else "./"

    def L(self, target):
        p = self.root + target
        if LOCAL and (target == "" or target.endswith("/")): p += "index.html"
        return p

    def asset(self, target): return self.root + "assets/" + target

NAV = [("Home", "", ""), ("About", "about/", "about"), ("Services", "services/", "services"), ("Work", "work/", "work"),
       ("Case Studies", "case-studies/", "case-studies"), ("Insights", "insights/", "insights"), ("Contact", "contact/", "contact")]

def header(c, current):
    items = []
    for label, target, key in NAV:
        cur = ' aria-current="page"' if key == current else ""
        items.append(f'<li><a href="{c.L(target)}"{cur}>{label}</a></li>')
    return f'''<header class="site-header"><div class="wrap site-header__bar">
<a class="logo" href="{c.L("")}" aria-label="Aperture Media, home">{mark()}<span><strong>Aperture</strong> <span>Media</span></span></a>
<nav class="nav" id="site-nav" aria-label="Main"><ul>{"".join(items)}</ul>
<a class="btn btn--butter nav__cta" href="{c.L("contact/")}">Start a project</a></nav>
<a class="btn header-cta" href="{c.L("contact/")}">Start a project</a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
</div></header>'''

def footer(c):
    soc = "".join(f'<li><a href="{esc(u)}" rel="noopener" target="_blank">{esc(n)}</a></li>' for n, u in SITE["socials"])
    svc = "".join(f'<li><a href="{c.L("services/")}#{s["slug"]}">{esc(s["title"].split(" and ")[0])}</a></li>' for s in SERVICES[:6])
    return f'''<footer class="site-footer"><div class="wrap">
<div class="footer__top">
<div><p class="footer__big">Let’s make something people stop for.</p><a class="btn btn--butter" href="{c.L("contact/")}">Start a project</a></div>
<div class="footer__col"><h2>Explore</h2><ul>
<li><a href="{c.L("about/")}">About</a></li><li><a href="{c.L("services/")}">Services</a></li><li><a href="{c.L("work/")}">Work</a></li>
<li><a href="{c.L("case-studies/")}">Case studies</a></li><li><a href="{c.L("clients/")}">Clients</a></li><li><a href="{c.L("insights/")}">Insights</a></li><li><a href="{c.L("contact/")}">Contact</a></li></ul></div>
<div class="footer__col"><h2>Services</h2><ul>{svc}<li><a href="{c.L("services/")}">All services</a></li></ul></div>
<div class="footer__col"><h2>Get in touch</h2><ul>
<li><a href="mailto:{esc(SITE["email"])}">{esc(SITE["email"])}</a></li><li><a href="tel:{esc(SITE["phone"].replace(" ", ""))}">{esc(SITE["phone"])}</a></li>
<li><a href="{esc(SITE["whatsapp"])}" rel="noopener" target="_blank">WhatsApp</a></li></ul>
<ul style="margin-top:1rem">{soc}</ul></div>
</div>
<div class="footer__bottom"><span>© {YEAR} Aperture Media. All rights reserved.</span><a href="{c.L("privacy/")}">Privacy policy</a></div>
</div></footer>'''

def shell(c, *, title, desc, body, current="", jsonld=None, og_type="website", robots=None):
    full_title = title if c.path == "" else f"{title} | Aperture Media"
    canon = SITE["url"].rstrip("/") + "/" + c.path
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    rb = f'<meta name="robots" content="{robots}">' if robots else ""
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
{rb}<link rel="canonical" href="{esc(canon)}">
<meta name="theme-color" content="#1e1b5c">
<meta property="og:site_name" content="Aperture Media"><meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(full_title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(canon)}"><meta property="og:image" content="{esc(SITE["url"].rstrip("/"))}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{c.asset("favicon.svg")}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,300..800&family=Instrument+Sans:wght@400..700&display=swap">
<link rel="stylesheet" href="{c.asset("css/styles.css")}">
<script>document.documentElement.className="js";</script>
{ld}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{header(c, current)}
<main id="main">
{body}
</main>
{footer(c)}
<script src="{c.asset("js/main.js")}" defer></script>
</body>
</html>
'''

# ------------------------------------------------------------------ shared components
def cta_panel(c, heading="Have a menu, a product or a brand to grow?", text="Tell us what you are working on. We will come back with ideas, not a template."):
    return f'''<section class="section"><div class="wrap"><div class="cta-panel"><h2>{esc(heading)}</h2><p>{esc(text)}</p>
<div class="btn-row" style="margin:0"><a class="btn" href="{c.L("contact/")}">Start a project</a><a class="btn btn--ghost" href="mailto:{esc(SITE["email"])}">{esc(SITE["email"])}</a></div></div></div></section>'''

def card(c, p, chip=False):
    cats = " ".join(p["cats"])
    return f'''<a class="card" href="{c.L("case-studies/" + p["slug"] + "/")}" data-cats="{cats}">
{tile(p["art"], p["tile"])}<div class="card__meta"><h3>{esc(p["name"])}</h3><p>{esc(p["kind"])}. {esc(p["tagline"])}</p></div></a>'''

def reel_list(items, label="Short-form video samples", note=True):
    hint = "<!-- To use real video, replace the illustration inside .reel__screen with: <video src=\"your-file.mp4\" poster=\"poster.jpg\" controls playsinline muted preload=\"none\"></video> -->\n" if note else ""
    lis = "".join(f'''<li class="reel"><figure style="margin:0"><div class="reel__screen t-{col}">{art(a)}<span class="reel__play">{PLAY}</span></div><figcaption>{esc(t)}</figcaption></figure></li>''' for t, a, col in items)
    return f'{hint}<ul class="reels" tabindex="0" role="region" aria-label="{esc(label)}">{lis}</ul>'

def before_after():
    return f'''<div class="ba">
<div class="tile t-peach ba__pane ba__pane--after" aria-hidden="true">{art("donut")}</div>
<div class="tile t-peach ba__pane ba__pane--before" aria-hidden="true">{art("donut")}</div>
<span class="ba__tag ba__tag--before">Before</span><span class="ba__tag ba__tag--after">After</span>
<span class="ba__line" aria-hidden="true"></span>
<input type="range" min="0" max="100" value="50" aria-label="Drag to compare the before and after versions of the Glaze Lab feed">
</div>'''

# ------------------------------------------------------------------ pages
def page_home(c):
    L = c.L
    clients = "".join(f"<li>{esc(n)}</li>" for n, _, _ in CLIENTS[:6])
    rows = "".join(f'''<li><a class="svc-row" href="{L("services/")}#{s["slug"]}"><h3>{esc(s["title"])}</h3><p>{esc(s["short"])}</p>{tile(s["art"], s["tile"], "mini")}</a></li>''' for s in SERVICES)
    featured = "".join(card(c, p) for p in [PROJECTS[0], PROJECTS[3], PROJECTS[4]])
    stats = "".join(f'<div><p class="stat__num">{esc(v)}</p><p class="stat__label">{esc(l)}</p></div>' for v, l in STATS)
    why = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in WHY)
    quotes = "".join(f'<figure class="quote"><blockquote>“{esc(q)}”</blockquote><figcaption><b>{esc(r)}</b>{esc(co)}</figcaption></figure>' for q, r, co in TESTIMONIALS)
    body = f'''
<section class="hero"><div class="wrap">
<div class="hero__grid"><div>
<h1><span>Content that stops the scroll.</span><span>Brands that stay remembered.</span></h1>
<p class="lead">Aperture Media is a creative and social media marketing agency. We create, edit, publish and grow, with a special eye for food, restaurant, product and lifestyle brands.</p>
<div class="btn-row"><a class="btn" href="{L("contact/")}">Start a project</a><a class="btn btn--ghost" href="{L("work/")}">See our work</a></div>
</div>{iris()}</div>
<div class="trust"><p>Recent clients</p><ul>{clients}</ul></div>
</div></section>

<section class="section"><div class="wrap">
<div class="head"><h2>We do more than manage social media.</h2></div>
<p class="lead">We shoot the content, shape the brand, plan the strategy and run the channels, so everything your audience sees is consistent and worth following.</p>
<div class="pillars">
<div class="pillar"><h3>Create</h3><p>Photo and video built for the feed: Reels, TikToks, stills, stories and campaigns.</p></div>
<div class="pillar"><h3>Build</h3><p>Brand identity, voice and content systems that make every post recognizable.</p></div>
<div class="pillar"><h3>Grow</h3><p>Strategy, ads, creators and analytics that turn attention into customers.</p></div>
</div></div></section>

<section class="section section--tight"><div class="wrap">
<div class="head"><h2>Everything your feed needs, under one roof.</h2></div>
<ul class="svc-list">{rows}</ul>
<div class="btn-row"><a class="btn btn--ghost" href="{L("services/")}">Explore all services</a></div>
</div></section>

<section class="section section--mist"><div class="wrap">
<div class="head"><h2>Recent work</h2><p>Restaurants, products and brands that we helped stand out.</p></div>
<div class="work-grid work-grid--featured">{featured}</div>
<div class="btn-row"><a class="btn" href="{L("work/")}">View all work</a><a class="btn btn--ghost" href="{L("case-studies/")}">Read case studies</a></div>
</div></section>

<section class="section section--blue"><div class="wrap">
<div class="head"><h2>Made for the scroll.</h2><p>Short-form video is our home ground. A few of the formats we make.</p></div>
{reel_list(REELS)}
</div></section>

<section class="section"><div class="wrap split">
<div><h2>Why brands choose Aperture.</h2><p class="lead">Serious craft, a simple process and people who care how it turns out.</p>
<div class="btn-row"><a class="btn btn--ghost" href="{L("about/")}">About us</a></div></div>
<ul class="why-list">{why}</ul></div></section>

<section class="section section--blue"><div class="wrap"><div class="stats">{stats}</div></div></section>

<section class="section section--mist"><div class="wrap">
<div class="head"><h2>What clients say</h2></div>
<div class="quotes">{quotes}</div></div></section>

{cta_panel(c)}'''
    ld = [{"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Aperture Media",
           "description": "Creative and social media marketing agency for food brands, restaurants and businesses across industries.",
           "url": SITE["url"], "email": SITE["email"], "sameAs": [u for _, u in SITE["socials"]],
           "serviceType": [s["title"] for s in SERVICES]}]
    return dict(title="Aperture Media | Social media marketing and content agency",
                desc="Aperture Media creates content, builds brands and runs social media for food brands, restaurants and businesses across industries.",
                body=body, current="", jsonld=ld)

def page_about(c):
    L = c.L
    approach = [("Start with the audience", "Who are we trying to reach, what do they care about and where do they spend time? Every plan starts there."),
                ("Make it look and feel like you", "A recognizable style, voice and rhythm, so people know it is you before they see the name."),
                ("Publish with intent", "Every post has a job: to introduce, to convince, to remind or to invite."),
                ("Measure, then improve", "We report in plain language and use what we learn to make the next round better.")]
    ap = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in approach)
    principles = [("Make it crave-able", "Food should look the way it tastes. We chase light, texture, sound and the exact moment it looks best."),
                  ("Show the real thing", "Real kitchens, real hands, real people. Polished where it helps, honest where it counts."),
                  ("Design for the thumb", "Content lives on a phone. We frame, cut and write for a small screen and a fast scroll.")]
    pr = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in principles)
    team = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in TEAM)
    diff = ["We make the content and manage the channels, not just one or the other.", "Deep experience in food, restaurant, product and lifestyle content.",
            "Strategy, creative and reporting in one place, with one point of contact.", "Formats built for how people scroll now: short, vertical and sound-on.",
            "Clear plans, honest numbers and no jargon."]
    df = "".join(f"<li>{esc(t)}</li>" for t in diff)
    body = f'''
<section class="page-head"><div class="wrap"><h1>We make brands worth following.</h1>
<p class="lead">Aperture Media is a creative and social media marketing agency. We create the content, shape the brand and run the channels for restaurants, food brands and businesses across industries.</p></div></section>

<section class="section section--tight"><div class="wrap split"><h2>Our story</h2><div class="stack">
<p class="lead">Aperture Media started behind a camera, filming food.</p>
<p>Making content for our own audience taught us what makes people stop, watch and get hungry: the light, the sound, the timing and a clear point of view.</p>
<p>Brands began asking us to do the same for them. Today we do far more than film dishes. We build strategies, shape brand identities and manage channels for restaurants first and, more and more, for businesses in every industry.</p></div></div></section>

<section class="section section--tight section--mist"><div class="wrap split"><div><h2>Our approach to marketing</h2></div><ul class="why-list">{ap}</ul></div></section>

<section class="section"><div class="wrap"><div class="mv">
<div><h3>Mission</h3><p>To help businesses communicate with their audience through powerful, honest and beautifully made content.</p></div>
<div><h3>Vision</h3><p>A digital world where every good brand looks as good online as it does in real life.</p></div></div></div></section>

<section class="section section--blue"><div class="wrap"><div class="head"><h2>Our creative philosophy</h2></div><ul class="principles">{pr}</ul></div></section>

<section class="section"><div class="wrap"><div class="head"><h2>The team</h2><p>A small, focused crew that shoots, edits, plans and reports.</p></div><ul class="team">{team}</ul></div></section>

<section class="section section--tight section--mist"><div class="wrap split"><div><h2>What makes Aperture different</h2></div><ul class="diff">{df}</ul></div></section>

{cta_panel(c, "Want to work with people who care how it looks?", "Send us a few details and we will be in touch.")}'''
    return dict(title="About", desc="Meet Aperture Media: a creative and social media marketing agency creating content, building brands and managing channels for food brands and businesses.",
                body=body, current="about")

def page_services(c):
    L = c.L
    idx = "".join(f'<li><a href="#{s["slug"]}">{esc(s["title"])}</a></li>' for s in SERVICES)
    blocks = []
    for s in SERVICES:
        items = "".join(f"<li>{esc(i)}</li>" for i in s["items"])
        blocks.append(f'''<article class="svc-block" id="{s["slug"]}"><div class="svc-block__text"><h2>{esc(s["title"])}</h2><p class="lead">{esc(s["body"])}</p>
<ul class="ticks">{items}</ul><p class="fit"><b>Great for:</b> {esc(s["fit"])}</p>
<div class="btn-row" style="margin-top:1rem"><a class="btn" href="{L("contact/")}">Start a project</a></div></div>
{tile(s["art"], s["tile"], "", "--ar:4/5")}</article>''')
    steps = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in PROCESS)
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in FAQ)
    body = f'''
<section class="page-head"><div class="wrap"><h1>Services built around your feed.</h1>
<p class="lead">From strategy and shooting to editing, ads and reporting. Pick one service or let us run the whole thing.</p></div></section>

<section class="section section--tight"><div class="wrap svc-layout"><ul class="svc-index" aria-label="Services">{idx}</ul><div>{"".join(blocks)}</div></div></section>

<section class="section section--blue"><div class="wrap"><div class="head"><h2>How we work</h2></div><ol class="steps">{steps}</ol></div></section>

<section class="section"><div class="wrap split"><div><h2>Questions we hear a lot</h2></div><div class="faq">{faq}</div></div></section>

{cta_panel(c)}'''
    ld = [{"@context": "https://schema.org", "@type": "ItemList", "name": "Aperture Media services",
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["title"]} for i, s in enumerate(SERVICES)]}]
    return dict(title="Services", desc="Social media management, strategy, content creation, video production, editing, photography, advertising, brand strategy and influencer marketing from Aperture Media.",
                body=body, current="services", jsonld=ld)

def page_work(c):
    L = c.L
    filt = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{esc(v)}</button>' for k, v in WORK_FILTERS)
    cards = "".join(card(c, p) for p in PROJECTS)
    photos = "".join(f'''<figure style="margin:0">{tile(a, col, "", f"--ar:{ar}")}<figcaption class="muted" style="margin-top:.5rem;font-size:.95rem">{esc(t)}</figcaption></figure>''' for t, a, col, ar in PHOTOS)
    body = f'''
<section class="page-head"><div class="wrap"><h1>Work that makes people hungry.</h1>
<p class="lead">Restaurants, products and brands we have helped look better, reach further and sell more. Open any project for the full case study.</p></div></section>

<section class="section section--tight"><div class="wrap">
<div class="filters" data-filters role="group" aria-label="Filter projects">{filt}</div>
<p class="visually-hidden" role="status" aria-live="polite" data-filter-status></p>
<div class="work-grid">{cards}</div></div></section>

<section class="section section--blue" id="reels"><div class="wrap"><div class="head"><h2>Reels and short-form video</h2><p>Hooks, pace and sound designed for the first two seconds.</p></div>
{reel_list(REELS + REELS[:1])}</div></section>

<section class="section" id="photography"><div class="wrap"><div class="head"><h2>Photography</h2><p>Menus, products, interiors and lifestyle images ready for social, web and print.</p></div>
<div class="gallery" style="align-items:start">{photos}</div></div></section>

<section class="section section--mist" id="before-after"><div class="wrap split"><div><h2>Social media transformation</h2>
<p class="lead">Glaze Lab’s feed, before and after. Drag the slider to compare.</p>
<div class="btn-row"><a class="btn" href="{L("case-studies/glaze-lab/")}">Read the case study</a></div></div>{before_after()}</div></section>

{cta_panel(c, "Want results like these?", "Tell us about your brand and what you want to achieve.")}'''
    return dict(title="Our work", desc="Restaurant and food content, product photography, brand campaigns, Reels and social media transformations by Aperture Media.",
                body=body, current="work")

def page_case_index(c):
    rows = []
    for p in PROJECTS:
        rows.append(f'''<li><a class="post-row" href="{c.L("case-studies/" + p["slug"] + "/")}"><div class="post-row__meta">{esc(p["kind"])}</div>
<div><h2>{esc(p["name"])}</h2><p>{esc(p["tagline"])}</p><p class="card__result">{esc(p["results"][0][0])} {esc(p["results"][0][1])}</p></div></a></li>''')
    body = f'''
<section class="page-head"><div class="wrap"><h1>Case studies</h1>
<p class="lead">The challenge, the strategy, the content and the results behind selected projects.</p></div></section>
<section class="section section--tight"><div class="wrap"><ul class="post-list">{"".join(rows)}</ul></div></section>
{cta_panel(c)}'''
    return dict(title="Case studies", desc="Detailed case studies from Aperture Media: challenges, strategy, content produced, execution and results.", body=body, current="case-studies")

def page_case(c, i):
    p = PROJECTS[i]; nxt = PROJECTS[(i + 1) % len(PROJECTS)]; L = c.L
    content = "".join(f"<li>{esc(t)}</li>" for t in p["content"])
    steps = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in p["steps"])
    res = "".join(f'<div><p class="stat__num">{esc(v)}</p><p class="stat__label">{esc(l)}</p></div>' for v, l in p["results"])
    photos = [(p["art"], p["tile"], "1"), (p["art"], "butter", "4/5"), (p["art"], "lilac", "4/5"), (p["art"], "mint", "1")]
    gal = "".join(tile(a, col, "", f"--ar:{ar}") for a, col, ar in photos)
    reels = reel_list([(f"{p['name']} · Reel {n}", p["art"], col) for n, col in ((1, p["tile"]), (2, "butter"), (3, "lilac"), (4, "mint"))], f"{p['name']} short-form video samples", note=False)
    ba = f'<section class="section section--mist"><div class="wrap split"><div><h2>Before and after</h2><p class="lead">The feed before we started, and after.</p></div>{before_after()}</div></section>' if p["slug"] == "glaze-lab" else ""
    body = f'''
<div class="wrap">
<section class="cs-hero"><div><p class="crumbs"><a href="{L("case-studies/")}">Case studies</a> / {esc(p["name"])}</p>
<h1>{esc(p["name"])}</h1><p class="lead">{esc(p["tagline"])}</p></div>{tile(p["art"], p["tile"], "", "--ar:5/4")}</section>
<dl class="facts"><div><dt>Client</dt><dd>{esc(p["name"])}, {esc(p["kind"].lower())}</dd></div><div><dt>Services</dt><dd>{esc(", ".join(p["services"]))}</dd></div><div><dt>Platforms</dt><dd>{esc(p["platforms"])}</dd></div></dl>
<section class="cs-block"><h2>The client</h2><p>{esc(p["client"])}</p></section>
<section class="cs-block"><h2>The challenge</h2><p>{esc(p["challenge"])}</p></section>
<section class="cs-block"><h2>The strategy</h2><p>{esc(p["strategy"])}</p></section>
<section class="cs-block"><h2>Content produced</h2><ul class="ticks" style="margin:0">{content}</ul></section>
<section class="cs-block"><h2>Campaign execution</h2><ol class="cs-steps">{steps}</ol></section>
</div>
<section class="section section--blue" style="margin-top:2rem"><div class="wrap"><div class="head"><h2>Results</h2></div><div class="stats">{res}</div></div></section>
<section class="section"><div class="wrap"><div class="head"><h2>Visuals and video</h2></div>{reels}<div class="gallery" style="margin-top:1.5rem">{gal}</div></div></section>
{ba}
<section class="section section--tight"><div class="wrap split"><h2>The outcome</h2><p class="lead">{esc(p["outcome"])}</p></div></section>
<section class="section section--tight section--mist"><div class="wrap"><a class="next-project" href="{L("case-studies/" + nxt["slug"] + "/")}"><p style="margin:0">Next case study</p><h2>{esc(nxt["name"])}</h2></a></div></section>
{cta_panel(c, "Want a result like this for your brand?")}'''
    ld = [{"@context": "https://schema.org", "@type": "CreativeWork", "name": f"{p['name']} case study", "about": p["kind"],
           "creator": {"@type": "Organization", "name": "Aperture Media"}, "description": p["tagline"]}]
    return dict(title=f"{p['name']} case study", desc=f"{p['name']}: {p['tagline']} {p['challenge'][:110]}…", body=body, current="case-studies", jsonld=ld)

def page_clients(c):
    lis = []
    for n, k, slug in CLIENTS:
        if slug:
            lis.append(f'<li><a class="client" href="{c.L("case-studies/" + slug + "/")}"><b>{esc(n)}</b><span>{esc(k)}. Read the case study</span></a></li>')
        else:
            lis.append(f'<li><div class="client client--static"><b>{esc(n)}</b><span>{esc(k)}</span></div></li>')
    quotes = "".join(f'<figure class="quote"><blockquote>“{esc(q)}”</blockquote><figcaption><b>{esc(r)}</b>{esc(co)}</figcaption></figure>' for q, r, co in TESTIMONIALS)
    body = f'''
<section class="page-head"><div class="wrap"><h1>Brands we work with.</h1>
<p class="lead">Restaurants, food and drink brands, hospitality and lifestyle businesses. Food is our home ground, and the same craft works across industries.</p></div></section>
<section class="section section--tight"><div class="wrap"><ul class="client-grid">{"".join(lis)}</ul></div></section>
<section class="section section--mist"><div class="wrap"><div class="head"><h2>In their words</h2></div><div class="quotes">{quotes}</div></div></section>
{cta_panel(c, "Want to see your brand here?")}'''
    return dict(title="Clients", desc="Restaurants, food and drink brands, hospitality and lifestyle businesses that work with Aperture Media.", body=body, current="")

def fmt_date(d):
    return datetime.date.fromisoformat(d).strftime("%B %-d, %Y")

def page_insights(c):
    rows = "".join(f'''<li><a class="post-row" href="{c.L("insights/" + a["slug"] + "/")}"><div class="post-row__meta">{esc(a["cat"])}<br>{esc(fmt_date(a["date"]))}</div>
<div><h2>{esc(a["title"])}</h2><p>{esc(a["excerpt"])}</p></div></a></li>''' for a in ARTICLES)
    body = f'''
<section class="page-head"><div class="wrap"><h1>Insights</h1>
<p class="lead">Practical thinking on social media, content, branding and what is changing in food marketing.</p></div></section>
<section class="section section--tight"><div class="wrap"><ul class="post-list">{rows}</ul></div></section>
{cta_panel(c, "Want this thinking applied to your brand?")}'''
    return dict(title="Insights", desc="Marketing insights, social media tips, content strategy, branding advice and industry trends from Aperture Media.", body=body, current="insights")

def page_article(c, a):
    paras = "".join(f"<p>{esc(t)}</p>" for t in a["body"][:2])
    paras2 = "".join(f"<p>{esc(t)}</p>" for t in a["body"][2:])
    pts = "".join(f"<li>{esc(t)}</li>" for t in a["points"])
    more = "".join(f'<li><a class="post-row" href="{c.L("insights/" + o["slug"] + "/")}"><div class="post-row__meta">{esc(o["cat"])}</div><div><h2>{esc(o["title"])}</h2></div></a></li>' for o in ARTICLES if o is not a)
    body = f'''
<article class="section article"><p class="crumbs"><a href="{c.L("insights/")}">Insights</a> / {esc(a["cat"])}</p>
<h1>{esc(a["title"])}</h1><p class="article__meta">{esc(fmt_date(a["date"]))} · {esc(a["read"])} read</p>
{paras}<aside class="callout"><h2>Key takeaways</h2><ul class="ticks">{pts}</ul></aside>{paras2}
<div class="btn-row"><a class="btn" href="{c.L("contact/")}">Talk to us about your content</a></div></article>
<section class="section section--tight section--mist"><div class="wrap"><div class="head"><h2>Keep reading</h2></div><ul class="post-list">{more}</ul></div></section>'''
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "datePublished": a["date"],
           "author": {"@type": "Organization", "name": "Aperture Media"}, "description": a["excerpt"]}]
    return dict(title=a["title"], desc=a["excerpt"], body=body, current="insights", jsonld=ld, og_type="article")

def page_contact(c):
    short = {"video-production": "Video and Reels", "brand-strategy": "Brand strategy", "influencer-marketing": "Influencer marketing",
             "growth-analysis": "Growth analysis", "social-media-advertising": "Social ads"}
    svc_checks = "".join(f'<label><input type="checkbox" name="services" value="{esc(s["title"])}"><span>{esc(short.get(s["slug"], s["title"]))}</span></label>' for s in SERVICES)
    budgets = ["Not sure yet", "Under $1,000 per month", "$1,000 to $2,500 per month", "$2,500 to $5,000 per month", "$5,000+ per month", "One-off project"]
    opts = "".join(f'<option value="{esc(b)}">{esc(b)}</option>' for b in budgets)
    ep = SITE["form_endpoint"]
    action = ep if ep else c.L("thanks/")
    netlify = "" if ep else ' data-netlify="true" netlify-honeypot="bot-field"'
    soc = "".join(f'<li><a href="{esc(u)}" rel="noopener" target="_blank">{esc(n)}</a></li>' for n, u in SITE["socials"])
    body = f'''
<section class="section"><div class="wrap contact-grid">
<div><h1 style="font-size:var(--step-4)">Start a project.</h1>
<p class="lead">Tell us about your brand, what you want to achieve and where you are now. We reply within one business day.</p>
<ul class="contact-list">
<li><small>Email</small><a href="mailto:{esc(SITE["email"])}">{esc(SITE["email"])}</a></li>
<li><small>Phone</small><a href="tel:{esc(SITE["phone"].replace(" ", ""))}">{esc(SITE["phone"])}</a></li>
<li><small>WhatsApp</small><a href="{esc(SITE["whatsapp"])}" rel="noopener" target="_blank">Message us on WhatsApp</a></li></ul>
<ul class="socials" aria-label="Social media">{soc}</ul></div>

<form class="form" name="contact" method="POST" action="{esc(action)}" data-contact-form data-endpoint="{esc(ep)}" data-email="{esc(SITE["email"])}"{netlify} novalidate>
<input type="hidden" name="form-name" value="contact">
<p class="hp" aria-hidden="true"><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<div class="form__row">
<div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
<div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div></div>
<div class="form__row">
<div class="field"><label for="f-phone">Phone or WhatsApp</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
<div class="field"><label for="f-company">Company or brand</label><input id="f-company" name="company" autocomplete="organization"></div></div>
<div class="field"><fieldset><legend>Services you need</legend><div class="checks">{svc_checks}</div></fieldset></div>
<div class="field"><label for="f-budget">Budget range</label><select id="f-budget" name="budget">{opts}</select></div>
<div class="field"><label for="f-details">Project details</label><textarea id="f-details" name="details" required placeholder="What are you working on, and what would success look like?"></textarea></div>
<p class="form-status" role="status" tabindex="-1" hidden></p>
<button class="btn" type="submit">Send project details</button>
<p class="form-note">We use your details only to reply to this enquiry. See our <a class="link" href="{c.L("privacy/")}">privacy policy</a>.</p>
</form></div></section>'''
    return dict(title="Contact", desc="Start a project with Aperture Media. Tell us about your brand and goals and we will reply within one business day.", body=body, current="contact")

def page_thanks(c):
    body = f'''<section class="section"><div class="wrap page-head"><h1>Thank you.</h1>
<p class="lead">We have your project details and will reply within one business day.</p>
<div class="btn-row"><a class="btn" href="{c.L("work/")}">See our work</a><a class="btn btn--ghost" href="{c.L("")}">Back to home</a></div></div></section>'''
    return dict(title="Thank you", desc="Your message has been sent.", body=body, current="", robots="noindex")

def page_privacy(c):
    body = f'''<section class="section"><div class="prose"><h1 style="font-size:var(--step-3)">Privacy policy</h1>
<p><em>Template text. Have it reviewed against the laws that apply to your business before launch.</em></p>
<h2>What we collect</h2><p>When you send the contact form we collect the details you enter: your name, email address, phone number, company, services of interest, budget range and message.</p>
<h2>How we use it</h2><p>We use these details only to reply to your enquiry and to prepare a proposal. We do not sell your information.</p>
<h2>Who can see it</h2><p>Your enquiry is handled by our team and by the service that processes our website form. We may share information where the law requires it.</p>
<h2>Cookies and analytics</h2><p>This site does not set tracking cookies by default. If we add analytics, we will update this page.</p>
<h2>Your rights</h2><p>You can ask us to show, correct or delete the information we hold about you by emailing <a class="link" href="mailto:{esc(SITE["email"])}">{esc(SITE["email"])}</a>.</p>
<p>Last updated: {datetime.date.today().strftime("%B %-d, %Y")}</p></div></section>'''
    return dict(title="Privacy policy", desc="How Aperture Media handles the information you send through this website.", body=body, current="")

def page_404(c):
    body = f'''<section class="section notfound"><div class="wrap">{iris("donut").replace("A camera aperture opening to reveal a pizza seen from above", "A camera aperture opening on a doughnut")}
<h1 style="font-size:var(--step-3)">This page is out of frame.</h1><p style="margin-inline:auto">The page you are looking for has moved or does not exist.</p>
<div class="btn-row" style="justify-content:center"><a class="btn" href="{c.L("")}">Back to home</a><a class="btn btn--ghost" href="{c.L("work/")}">See our work</a></div></div></section>'''
    return dict(title="Page not found", desc="Page not found.", body=body, current="", robots="noindex")

# ------------------------------------------------------------------ build
def write(path, html_text):
    dest = OUT / path / "index.html" if path and not path.endswith(".html") else OUT / (path or "index.html")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html_text, encoding="utf-8")

def main():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(HERE / "assets", OUT / "assets")
    pages = [("", page_home), ("about/", page_about), ("services/", page_services), ("work/", page_work),
             ("case-studies/", page_case_index), ("clients/", page_clients), ("insights/", page_insights),
             ("contact/", page_contact), ("thanks/", page_thanks), ("privacy/", page_privacy)]
    for i, p in enumerate(PROJECTS): pages.append((f"case-studies/{p['slug']}/", lambda c, i=i: page_case(c, i)))
    for a in ARTICLES: pages.append((f"insights/{a['slug']}/", lambda c, a=a: page_article(c, a)))
    urls = []
    for path, fn in pages:
        c = Ctx(path); d = fn(c)
        write(path, shell(c, **d))
        if d.get("robots") != "noindex": urls.append(path)
    c404 = Ctx("404.html", absolute=True); c404.depth = 0
    write("404.html", shell(c404, **page_404(c404)))

    base = SITE["url"].rstrip("/")
    today = datetime.date.today().isoformat()
    sm = "".join(f"<url><loc>{base}/{u}</loc><lastmod>{today}</lastmod></url>" for u in urls)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n")
    (OUT / "_headers").write_text("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n")
    (OUT / ".nojekyll").write_text("")
    print(f"Built {len(pages) + 1} pages into {OUT}")

if __name__ == "__main__":
    main()
