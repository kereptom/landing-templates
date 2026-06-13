#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder for the landing-page template gallery.
Source of truth = this file (framework CSS+JS, THEMES, renderers) + content/NN.json.
Output = self-contained, copy-paste-ready templates/NN-slug/index.html.
No em dashes anywhere (global rule).
"""
import json, os, html, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(ROOT, "build", "content")
TPL_DIR = os.path.join(ROOT, "templates")
_LANG = "cs"

# ---------------------------------------------------------------------------
# FONTS (safe Google Fonts axis specs)
# ---------------------------------------------------------------------------
FONTS = {
 "inter_tight":("Inter+Tight:wght@400..800",'"Inter Tight", system-ui, sans-serif'),
 "inter":("Inter:wght@400..800",'"Inter", system-ui, sans-serif'),
 "space_grotesk":("Space+Grotesk:wght@400..700",'"Space Grotesk", system-ui, sans-serif'),
 "sora":("Sora:wght@400..800",'"Sora", system-ui, sans-serif'),
 "archivo":("Archivo:wght@400..800",'"Archivo", system-ui, sans-serif'),
 "manrope":("Manrope:wght@400..800",'"Manrope", system-ui, sans-serif'),
 "jakarta":("Plus+Jakarta+Sans:wght@400..800",'"Plus Jakarta Sans", system-ui, sans-serif'),
 "outfit":("Outfit:wght@400..800",'"Outfit", system-ui, sans-serif'),
 "figtree":("Figtree:wght@400..800",'"Figtree", system-ui, sans-serif'),
 "libre_franklin":("Libre+Franklin:wght@400..800",'"Libre Franklin", system-ui, sans-serif'),
 "schibsted":("Schibsted+Grotesk:wght@400..800",'"Schibsted Grotesk", system-ui, sans-serif'),
 "bricolage":("Bricolage+Grotesque:wght@400..800",'"Bricolage Grotesque", system-ui, sans-serif'),
 "quicksand":("Quicksand:wght@400..700",'"Quicksand", system-ui, sans-serif'),
 "unbounded":("Unbounded:wght@400..700",'"Unbounded", system-ui, sans-serif'),
 "fraunces":("Fraunces:ital,opsz,wght@0,9..144,400..800;1,9..144,400",'"Fraunces", Georgia, serif'),
 "playfair":("Playfair+Display:ital,wght@0,400..800;1,400..600",'"Playfair Display", Georgia, serif'),
 "source_serif":("Source+Serif+4:ital,opsz,wght@0,8..60,400..600;1,8..60,400",'"Source Serif 4", Georgia, serif'),
 "newsreader":("Newsreader:ital,opsz,wght@0,6..72,400..600;1,6..72,400",'"Newsreader", Georgia, serif'),
 "lora":("Lora:ital,wght@0,400..700;1,400..600",'"Lora", Georgia, serif'),
 "bodoni":("Bodoni+Moda:ital,opsz,wght@0,6..96,400..700;1,6..96,400",'"Bodoni Moda", Georgia, serif'),
 "jetbrains":("JetBrains+Mono:wght@400..600",'"JetBrains Mono", ui-monospace, monospace'),
 "space_mono":("Space+Mono:wght@400;700",'"Space Mono", ui-monospace, monospace'),
}

def _hex2rgb(h): h=h.lstrip("#"); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def _rgb2hex(t): return "#%02x%02x%02x"%tuple(max(0,min(255,int(round(v)))) for v in t)
def mix(a,b,t):
    ra,rb=_hex2rgb(a),_hex2rgb(b); return _rgb2hex(tuple(ra[i]*t+rb[i]*(1-t) for i in range(3)))

def mk(slug,name,subj,lang,disp,body,mono,c1,*,c2=None,c3=None,paper="#ffffff",ink="#15151b",
       dark=False,radius=1.0,bodyclass="",divider=None,divink="#ffffff"):
    if c2 is None: c2=mix(c1,"#ffffff",0.74)
    if c3 is None: c3=mix(c1,"#000000",0.80)
    df,bf,mf=FONTS[disp],FONTS[body],FONTS[mono]
    frags=[]
    for fr in (df[0],bf[0],mf[0]):
        if fr not in frags: frags.append(fr)
    font="&family=".join(frags)
    papersoft=mix(paper,ink,0.965 if not dark else 0.93)
    soft=mix(c1,paper,0.13 if not dark else 0.18)
    line=mix(c1,paper,0.30 if not dark else 0.42)
    ink2=mix(ink,paper,0.74); ink3=mix(ink,paper,0.50)
    rule=mix(ink,paper,0.12); rulesoft=mix(ink,paper,0.06)
    if divider is None: divider=f"linear-gradient(120deg,{c2} 0%,{c1} 55%,{c3} 100%)"
    return dict(slug=slug,name=name,subject=subj,lang=lang,font=font,display=df[1],serif=bf[1],mono=mf[1],
        c1=c1,c2=c2,c3=c3,soft=soft,line=line,paper=paper,papersoft=papersoft,ink=ink,ink2=ink2,ink3=ink3,
        rule=rule,rulesoft=rulesoft,divider=divider,divider_ink=divink,dark=dark,radius=radius,bodyclass=bodyclass)

# ---------------------------------------------------------------------------
# THEMES (one per template, different industry + look)
# ---------------------------------------------------------------------------
THEMES = [
 mk("01-nimbus-saas","Nimbus","Projektový SaaS","en","jakarta","source_serif","jetbrains","#6d4aff",paper="#ffffff",ink="#16131f",radius=1.4),
 mk("02-pulsefit","PulseFit","Fitness aplikace","en","sora","source_serif","jetbrains","#15c264",paper="#ffffff",ink="#0f1c14",radius=1.6),
 mk("03-zrnko-kavarna","Zrnko","Kavárna a pražírna","cs","fraunces","lora","jetbrains","#a8642a",paper="#fdf9f2",ink="#211913",radius=1.2),
 mk("04-hajek-advokat","Hájek & partneři","Advokátní kancelář","cs","libre_franklin","source_serif","jetbrains","#1f3a63",paper="#ffffff",ink="#101722",radius=0.4),
 mk("05-remeslo-plus","Řemeslo+","Řemeslník a instalatér","cs","inter_tight","source_serif","jetbrains","#f2682c",paper="#ffffff",ink="#1c140e",radius=1.0),
 mk("06-brightsmile","BrightSmile","Zubní ordinace","en","manrope","source_serif","jetbrains","#14b3c4",paper="#ffffff",ink="#0c1c20",radius=1.6),
 mk("07-domov-reality","Domov","Realitní kancelář","cs","outfit","lora","jetbrains","#2f7d57",paper="#ffffff",ink="#11201a",radius=0.8),
 mk("08-bistro-oliva","Bistro Oliva","Restaurace","cs","playfair","newsreader","jetbrains","#7b1e34",paper="#fdf7f4",ink="#1c1213",radius=0.6),
 mk("09-frame-studio","Frame Studio","Fotograf","en","archivo","source_serif","space_mono","#141417",paper="#ffffff",ink="#141417",radius=0.2,bodyclass="em-solid"),
 mk("10-studio-vlna","Studio Vlna","Kreativní agentura","cs","space_grotesk","source_serif","space_mono","#e0249a",paper="#ffffff",ink="#1c1019",radius=1.5),
 mk("11-chainly","Chainly","Web3 a blockchain","en","space_grotesk","source_serif","jetbrains","#1fd1c4",paper="#0a0f14",ink="#e6f3f1",dark=True,radius=0.8,bodyclass="em-solid"),
 mk("12-penize-fintech","Peníze","Fintech a platby","cs","inter_tight","source_serif","jetbrains","#2f6bff",paper="#ffffff",ink="#0f1626",radius=1.0),
 mk("13-learnly","Learnly","Online kurzy","en","figtree","source_serif","jetbrains","#5b6cf0",paper="#ffffff",ink="#13141f",radius=1.4),
 mk("14-calm-yoga","Calm","Jóga a wellness","en","quicksand","lora","jetbrains","#6fae87",paper="#fbfaf6",ink="#16201a",radius=2.0),
 mk("15-ironhouse","IronHouse","Posilovna","cs","archivo","source_serif","space_mono","#e23b2e",paper="#101012",ink="#ededef",dark=True,radius=0.5,bodyclass="em-solid"),
 mk("16-lesk-kadernictvi","Lesk","Kadeřnictví a beauty","cs","jakarta","newsreader","jetbrains","#d6446e",paper="#fdf7f9",ink="#20141a",radius=1.5),
 mk("17-sharp-barber","Sharp","Holičství","en","bricolage","source_serif","space_mono","#c8932a",paper="#16130e",ink="#f1e9da",dark=True,radius=0.6),
 mk("18-stavby-cz","Stavby CZ","Stavební firma","cs","libre_franklin","source_serif","jetbrains","#4a6275",paper="#f7f8f9",ink="#11161b",radius=0.4),
 mk("19-sparkle-cleaning","Sparkle","Úklidové služby","en","manrope","source_serif","jetbrains","#2aa7e0",paper="#ffffff",ink="#0d1a22",radius=1.6),
 mk("20-tlapka-pet","Tlapka","Péče o mazlíčky","cs","quicksand","source_serif","jetbrains","#ff6b5e",paper="#fffaf7",ink="#201513",radius=2.0),
 mk("21-wander-travel","Wander","Cestovní kancelář","en","sora","lora","jetbrains","#f2683c",paper="#fffaf5",ink="#201410",radius=1.4),
 mk("22-summit-event","Summit","Konference a eventy","en","space_grotesk","source_serif","jetbrains","#2f6bff",paper="#0a0d14",ink="#e8ecf6",dark=True,radius=0.8,bodyclass="em-solid"),
 mk("23-mikrofon-podcast","Mikrofon","Podcast","cs","schibsted","source_serif","space_mono","#d6a019",paper="#fffdf6",ink="#1e1a10",radius=1.2),
 mk("24-inbox-newsletter","Inbox","Newsletter a média","en","archivo","source_serif","jetbrains","#e23b2e",paper="#ffffff",ink="#16110f",radius=0.4,bodyclass="em-solid"),
 mk("25-shoptik-eshop","Shoptik","E-shop platforma","cs","sora","source_serif","jetbrains","#7b2ff7",paper="#ffffff",ink="#150f24",radius=1.2),
 mk("26-cortex-ai","Cortex","AI nástroj","en","space_grotesk","source_serif","jetbrains","#2dd4bf",paper="#0c1116",ink="#eef2f6",dark=True,radius=0.6,bodyclass="em-solid"),
 mk("27-slunce-solar","Slunce","Solární energetika","cs","inter_tight","source_serif","jetbrains","#3f9e44",paper="#ffffff",ink="#13200f",radius=1.0),
 mk("28-autohub","AutoHub","Autosalon","en","archivo","source_serif","space_mono","#d24a2a",paper="#0e0e10",ink="#ededf0",dark=True,radius=0.5,bodyclass="em-solid"),
 mk("29-prostor-interier","Prostor","Interiérový design","cs","fraunces","lora","jetbrains","#9c7a55",paper="#fbf8f3",ink="#1c170f",radius=0.5),
 mk("30-forever-wedding","Forever","Svatební agentura","en","playfair","newsreader","jetbrains","#c77f99",paper="#fdf8f6",ink="#1d1418",radius=1.0),
 mk("31-pohyb-fyzio","Pohyb","Fyzioterapie","cs","manrope","source_serif","jetbrains","#0e9e8e",paper="#f6fbfa",ink="#0d1f1c",radius=1.4),
 mk("32-metrica","Metrica","Produktová analytika","en","inter","source_serif","jetbrains","#1f6feb",paper="#ffffff",ink="#0f1722",radius=0.8),
 mk("33-saldo-ucetni","Saldo","Účetnictví","cs","libre_franklin","source_serif","jetbrains","#20406b",paper="#ffffff",ink="#101722",radius=0.5),
 mk("34-echo-music","Echo","Hudební kapela","en","unbounded","source_serif","space_mono","#b32fe0",paper="#0a070f",ink="#f0e8f6",dark=True,radius=1.0,bodyclass="em-solid"),
 mk("35-pomahame-nezisk","Pomáháme","Nezisková organizace","cs","outfit","lora","jetbrains","#2c8a5a",paper="#ffffff",ink="#11201a",radius=1.4),
 mk("36-estate-lux","Estate","Luxusní reality","en","bodoni","lora","jetbrains","#b08d4f",paper="#0d0c0a",ink="#f1ece0",dark=True,radius=0.3),
]

# ---------------------------------------------------------------------------
# ICONS (lucide-style, for feature cards / lists)
# ---------------------------------------------------------------------------
ICONS = {
 "zap":'<path d="M13 2 3 14h8l-1 8 10-12h-8l1-8z"/>',
 "shield":'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "bolt":'<path d="M13 2 3 14h8l-1 8 10-12h-8l1-8z"/>',
 "chart":'<path d="M3 3v18h18"/><rect x="7" y="11" width="3" height="7"/><rect x="12" y="7" width="3" height="11"/><rect x="17" y="4" width="3" height="14"/>',
 "trend":'<path d="M16 7h6v6"/><path d="m22 7-8.5 8.5-5-5L2 17"/>',
 "users":'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9"/><path d="M16 3.1A4 4 0 0 1 16 11"/>',
 "user":'<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "calendar":'<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
 "lock":'<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 "globe":'<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18 14 14 0 0 1 0-18z"/>',
 "heart":'<path d="M19 14c1.5-1.5 3-3.3 3-5.5A4.5 4.5 0 0 0 12 5 4.5 4.5 0 0 0 2 8.5c0 2.2 1.5 4 3 5.5l7 7z"/>',
 "star":'<path d="m12 3 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 17l-5.2 2.8 1-5.8L3.5 9.2l5.9-.9z"/>',
 "check":'<path d="M20 6 9 17l-5-5"/>',
 "rocket":'<path d="M5 13c-2 1-3 5-3 5s4-1 5-3"/><path d="M15 7a8 8 0 0 1 5-2 8 8 0 0 1-2 5l-7 7-3-3z"/><circle cx="15" cy="9" r="1"/>',
 "phone":'<path d="M5 3h4l2 5-3 2a13 13 0 0 0 6 6l2-3 5 2v4a2 2 0 0 1-2 2A18 18 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
 "mail":'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 "map":'<path d="M12 21s-7-6.5-7-12a7 7 0 0 1 14 0c0 5.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "sparkle":'<path d="M12 3v6M12 15v6M3 12h6M15 12h6M6 6l3 3M15 15l3 3M18 6l-3 3M9 15l-3 3"/>',
 "leaf":'<path d="M11 20A7 7 0 0 1 4 13c0-6 7-10 16-10 0 8-4 15-9 17z"/><path d="M4 21c3-4 6-6 10-7"/>',
 "tool":'<path d="M14 7a4 4 0 0 0-5 5l-6 6 3 3 6-6a4 4 0 0 0 5-5l-3 3-3-3z"/>',
 "camera":'<rect x="3" y="7" width="18" height="13" rx="2"/><circle cx="12" cy="13" r="3.5"/><path d="M8 7l2-3h4l2 3"/>',
 "cart":'<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M3 4h2l2.5 12.5h11L21 8H6"/>',
 "gift":'<rect x="3" y="9" width="18" height="12" rx="1"/><path d="M3 13h18M12 9v12"/><path d="M12 9C9 9 7 7 8 5s4 0 4 4c0-4 3-6 4-4s-1 4-4 4z"/>',
 "play":'<circle cx="12" cy="12" r="9"/><path d="m10 8 6 4-6 4z"/>',
 "cpu":'<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 2v2M15 2v2M9 20v2M15 20v2M2 9h2M2 15h2M20 9h2M20 15h2"/>',
 "doc":'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8M8 17h6"/>',
 "home":'<path d="m3 11 9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 "scissors":'<circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><path d="M8 8 20 18M8 16 20 6"/>',
 "wrench":'<path d="M14 7a4 4 0 0 0-5 5l-6 6 3 3 6-6a4 4 0 0 0 5-5l-3 3-3-3z"/>',
 "sun":'<circle cx="12" cy="12" r="4.5"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
 "target":'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
 "chart":'<path d="M3 3v18h18"/><rect x="7" y="11" width="3" height="7"/><rect x="12" y="7" width="3" height="11"/><rect x="17" y="4" width="3" height="14"/>',
 "globe":'<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18 14 14 0 0 1 0-18z"/>',
}

# abstract inline illustration for hero/split panels (themed via var(--c-1))
def _ill(body, sw=6):
    return (f'<svg class="ill" viewBox="0 0 240 200" fill="none" stroke="var(--c-1)" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')
ILLUS = {
 "network": _ill('<circle cx="120" cy="100" r="20"/><circle cx="40" cy="50" r="13"/><circle cx="200" cy="55" r="13"/><circle cx="50" cy="160" r="13"/><circle cx="195" cy="155" r="13"/><path d="M104 88 53 60M136 90 188 62M106 114 60 150M134 113 182 145"/>'),
 "growth": _ill('<path d="M30 170h180M30 170V40"/><rect x="55" y="120" width="26" height="50"/><rect x="100" y="92" width="26" height="78"/><rect x="145" y="60" width="26" height="110"/><path d="M50 110 95 80l30 18 60-50"/><path d="M165 48h22v22" stroke-width="5"/>'),
 "shield": _ill('<path d="M120 30 50 56v52c0 44 70 74 70 74s70-30 70-74V56z"/><path d="m92 104 20 20 40-44"/>'),
 "layers": _ill('<path d="m120 36 86 44-86 44-86-44z"/><path d="m34 118 86 44 86-44M34 152l86 44 86-44" stroke-width="5"/>'),
 "target": _ill('<circle cx="110" cy="105" r="62"/><circle cx="110" cy="105" r="36"/><circle cx="110" cy="105" r="10"/><path d="m150 65 40-40M178 25h12v12" stroke-width="5"/>'),
 "chat": _ill('<rect x="34" y="44" width="120" height="84" rx="14"/><path d="M64 128v22l26-22"/><path d="M62 74h64M62 98h40"/><circle cx="170" cy="140" r="30"/><path d="M158 140h24M170 128v24" stroke-width="5"/>'),
 "people": _ill('<circle cx="80" cy="74" r="22"/><path d="M44 150a36 36 0 0 1 72 0"/><circle cx="158" cy="84" r="18"/><path d="M128 150a30 30 0 0 1 60 0"/>'),
 "spark": _ill('<path d="M120 40v40M120 120v40M40 100h40M160 100h40M70 50l28 28M170 150l-28-28M170 50l-28 28M70 150l28-28"/><circle cx="120" cy="100" r="16"/>'),
 "phone": _ill('<rect x="78" y="26" width="84" height="148" rx="16"/><path d="M104 40h32"/><circle cx="120" cy="156" r="6"/><path d="M96 70h48M96 92h48M96 114h30"/>'),
 "leaf": _ill('<path d="M130 40c-50 6-86 44-86 92 0 8 1 16 4 24 8-44 44-78 90-86-30 18-52 48-58 84 50-2 96-40 96-96 0-8-2-16-6-22z"/>'),
 "house": _ill('<path d="M40 100 120 40l80 60"/><path d="M58 88v74h124V88"/><rect x="100" y="118" width="40" height="44"/>'),
 "cart": _ill('<path d="M30 44h26l22 88h84l22-66H66"/><circle cx="92" cy="160" r="12"/><circle cx="160" cy="160" r="12"/>'),
 "globe": _ill('<circle cx="120" cy="100" r="74"/><path d="M46 100h148M120 26v148"/><path d="M120 26c-34 22-34 126 0 148M120 26c34 22 34 126 0 148"/><path d="M58 64c40 22 84 22 124 0M58 136c40-22 84-22 124 0"/>'),
 "chart": _ill('<path d="M40 40v120h160"/><path d="M58 150 98 104l30 20 52-70"/><path d="M168 54h22v22" stroke-width="5"/>'),
}

# ---------------------------------------------------------------------------
# SECTION RENDERERS
# ---------------------------------------------------------------------------
def icon(k, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24">{ICONS.get(k, ICONS["check"])}</svg>'

def r_nav(s):
    links = "".join(f'<a href="#{i}">{l}</a>' for i, l in enumerate(s["links"]))
    return (f'<header class="nav" id="nav"><div class="container nav-in">'
            f'<a class="brand" href="#top"><span class="brand-dot"></span>{s["brand"]}</a>'
            f'<nav class="nav-links">{links}</nav>'
            f'<div class="nav-cta"><a class="btn btn-sm" href="#cta">{s["cta"]}</a>'
            f'<button class="burger" aria-label="Menu" onclick="document.getElementById(\'nav\').classList.toggle(\'open\')"><span></span><span></span><span></span></button></div>'
            f'</div></header>')

def r_hero(s):
    ill = ILLUS.get(s.get("illus", "network"), ILLUS["network"])
    return (f'<section class="hero" id="top"><div class="container hero-in">'
            f'<div class="hero-copy"><span class="eyebrow">{s.get("eyebrow","")}</span>'
            f'<h1>{s["h1"]}</h1><p class="lede">{s.get("sub","")}</p>'
            f'<div class="hero-cta"><a class="btn btn-primary" href="#cta">{s.get("cta","")}</a>'
            f'<a class="btn btn-ghost" href="#features">{s.get("cta2","")}</a></div></div>'
            f'<div class="hero-art"><div class="art-panel">{ill}</div></div>'
            f'</div></section>')

def r_logos(s):
    items = "".join(f'<span>{x}</span>' for x in s["items"])
    return (f'<section class="logos"><div class="container"><p class="logos-label">{s.get("label","")}</p>'
            f'<div class="logos-row">{items}</div></div></section>')

def r_features(s):
    cards = "".join(
        f'<div class="feature"><div class="feat-ic">{icon(ic)}</div><h3>{t}</h3><p>{x}</p></div>'
        for ic, t, x in s["cards"])
    return (f'<section class="section" id="features"><div class="container">'
            f'<div class="head"><h2>{s["h2"]}</h2><p>{s.get("sub","")}</p></div>'
            f'<div class="features">{cards}</div></div></section>')

def r_stats(s):
    cells = "".join(f'<div><div class="stat-n">{n}</div><div class="stat-l">{l}</div></div>' for n, l in s["items"])
    return f'<section class="stats"><div class="container stats-row">{cells}</div></section>'

def r_split(s, flip):
    ill = ILLUS.get(s.get("illus", "layers"), ILLUS["layers"])
    bl = "".join(f'<li>{icon("check","li-ic")}<span>{b}</span></li>' for b in s.get("bullets", []))
    art = f'<div class="split-art"><div class="art-panel">{ill}</div></div>'
    copy = (f'<div class="split-copy"><span class="eyebrow">{s.get("eyebrow","")}</span>'
            f'<h2>{s["h2"]}</h2><p>{s.get("text","")}</p><ul class="ticks">{bl}</ul></div>')
    inner = (copy + art) if not flip else (art + copy)
    return f'<section class="section split{" flip" if flip else ""}"><div class="container split-in">{inner}</div></section>'

def r_steps(s):
    cells = "".join(
        f'<div class="step"><div class="step-n">{i+1}</div><h3>{t}</h3><p>{x}</p></div>'
        for i, (t, x) in enumerate(s["steps"]))
    return (f'<section class="section steps-wrap"><div class="container">'
            f'<div class="head"><h2>{s["h2"]}</h2><p>{s.get("sub","")}</p></div>'
            f'<div class="steps">{cells}</div></div></section>')

def r_testimonial(s):
    return (f'<section class="section quote-wrap"><div class="container quote-in">'
            f'<div class="quote-mark">&ldquo;</div><blockquote>{s["quote"]}</blockquote>'
            f'<div class="quote-by"><strong>{s.get("author","")}</strong><span>{s.get("role","")}</span></div>'
            f'</div></section>')

def r_pricing(s):
    cards = ""
    for t in s["tiers"]:
        feats = "".join(f'<li>{icon("check","li-ic")}<span>{f}</span></li>' for f in t.get("features", []))
        feat = " featured" if t.get("featured") else ""
        badge = (f'<span class="badge">{"Doporučeno" if _LANG=="cs" else "Popular"}</span>') if t.get("featured") else ""
        cards += (f'<div class="price-card{feat}">{badge}<div class="price-name">{t["name"]}</div>'
                  f'<div class="price-amt">{t["price"]}<span>{t.get("period","")}</span></div>'
                  f'<ul class="ticks">{feats}</ul><a class="btn {"btn-primary" if t.get("featured") else "btn-ghost"}" href="#cta">{t.get("cta","")}</a></div>')
    return (f'<section class="section pricing-wrap" id="pricing"><div class="container">'
            f'<div class="head"><h2>{s["h2"]}</h2><p>{s.get("sub","")}</p></div>'
            f'<div class="pricing">{cards}</div></div></section>')

def r_faq(s):
    items = "".join(
        f'<details class="faq-i"><summary>{q}<span class="faq-x">+</span></summary><p>{a}</p></details>'
        for q, a in s["items"])
    return (f'<section class="section faq-wrap" id="faq"><div class="container narrow">'
            f'<div class="head"><h2>{s["h2"]}</h2></div><div class="faq">{items}</div></div></section>')

def r_cta(s):
    return (f'<section class="cta" id="cta"><div class="container cta-in">'
            f'<h2>{s["h2"]}</h2><p>{s.get("sub","")}</p>'
            f'<a class="btn btn-light" href="#top">{s.get("button","")}</a></div></section>')

def r_footer(s):
    cols = ""
    for col in s["columns"]:
        head, *links = col
        ls = "".join(f'<a href="#">{l}</a>' for l in links)
        cols += f'<div class="fcol"><div class="fhead">{head}</div>{ls}</div>'
    return (f'<footer class="footer"><div class="container foot-in">'
            f'<div class="fbrand"><a class="brand" href="#top"><span class="brand-dot"></span>{s["brand"]}</a>'
            f'<p>{s.get("tagline","")}</p></div><div class="fcols">{cols}</div></div>'
            f'<div class="container foot-bar">{s.get("copyright","")}</div></footer>')

RENDER = {
 "nav": r_nav, "hero": r_hero, "logos": r_logos, "features": r_features, "stats": r_stats,
 "split1": lambda s: r_split(s, False), "split2": lambda s: r_split(s, True),
 "steps": r_steps, "testimonial": r_testimonial, "pricing": r_pricing, "faq": r_faq,
 "cta": r_cta, "footer": r_footer,
}

# ---------------------------------------------------------------------------
# CSS  ({V} placeholders filled from theme)
# ---------------------------------------------------------------------------
CSS = r"""
:root{
  --c-1:{c1}; --c-2:{c2}; --c-3:{c3}; --accent-soft:{soft}; --accent-line:{line};
  --paper:{paper}; --paper-soft:{papersoft}; --ink:{ink}; --ink-2:{ink2}; --ink-3:{ink3};
  --rule:{rule}; --rule-soft:{rulesoft}; --grad:{divider}; --r:{radius};
  --display:{display}; --serif:{serif}; --mono:{mono};
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:70px}
body{background:var(--paper);color:var(--ink);font-family:var(--serif);line-height:1.6;-webkit-font-smoothing:antialiased}
img,svg{display:block;max-width:100%}
a{color:inherit;text-decoration:none}
h1,h2,h3,.brand,.btn,.eyebrow,.stat-n,.price-amt,.step-n,.logos-label{font-family:var(--display)}
.container{max-width:1160px;margin:0 auto;padding:0 24px}
.container.narrow{max-width:780px}
em{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
body.em-solid em{background:none;-webkit-text-fill-color:var(--c-1);color:var(--c-1)}
.eyebrow{display:inline-block;font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:.1em;color:var(--c-1);background:var(--accent-soft);border:1px solid var(--accent-line);padding:6px 14px;border-radius:999px;margin-bottom:20px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-weight:600;font-size:16px;padding:13px 26px;border-radius:calc(11px*var(--r));border:1px solid transparent;cursor:pointer;transition:transform .15s,box-shadow .2s,background .2s;white-space:nowrap}
.btn-sm{padding:9px 18px;font-size:14.5px}
.btn-primary{background:var(--grad);color:#fff;box-shadow:0 8px 22px -8px var(--c-1)}
body.em-solid .btn-primary{background:var(--c-1)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 14px 30px -10px var(--c-1)}
.btn-ghost{background:transparent;border-color:var(--rule);color:var(--ink)}
.btn-ghost:hover{border-color:var(--c-1);color:var(--c-1)}
.btn-light{background:#fff;color:#111;box-shadow:0 10px 30px -12px rgba(0,0,0,.5)}
.btn-light:hover{transform:translateY(-2px)}
.nav{position:sticky;top:0;z-index:50;background:color-mix(in srgb, var(--paper) 82%, transparent);backdrop-filter:saturate(180%) blur(16px);border-bottom:1px solid transparent;transition:border-color .2s,box-shadow .2s}
.nav.scrolled{border-bottom-color:var(--rule);box-shadow:0 4px 20px -16px rgba(0,0,0,.4)}
.nav-in{display:flex;align-items:center;justify-content:space-between;height:64px}
.brand{display:inline-flex;align-items:center;gap:10px;font-weight:700;font-size:19px;letter-spacing:-.01em}
.brand-dot{width:18px;height:18px;border-radius:6px;background:var(--grad);flex:none}
.nav-links{display:flex;gap:30px;font-family:var(--display);font-weight:500;font-size:15px}
.nav-links a{color:var(--ink-2)}
.nav-links a:hover{color:var(--c-1)}
.nav-cta{display:flex;align-items:center;gap:10px}
.burger{display:none;flex-direction:column;gap:4px;background:none;border:none;padding:8px;cursor:pointer}
.burger span{width:22px;height:2px;background:var(--ink);border-radius:2px}
.hero{padding:clamp(48px,8vw,96px) 0 clamp(40px,6vw,80px)}
.hero-in{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center}
.hero h1{font-size:clamp(38px,5.6vw,64px);font-weight:800;letter-spacing:-.03em;line-height:1.04;margin-bottom:20px}
.lede{font-size:clamp(17px,2.1vw,21px);color:var(--ink-2);max-width:34ch;margin-bottom:30px}
.hero-cta{display:flex;gap:14px;flex-wrap:wrap}
.art-panel{background:var(--accent-soft);border:1px solid var(--accent-line);border-radius:calc(24px*var(--r));padding:clamp(28px,5vw,54px);display:flex;align-items:center;justify-content:center}
.art-panel .ill{width:100%;max-width:340px;height:auto}
.logos{padding:30px 0 10px}
.logos-label{text-align:center;font-size:12.5px;font-weight:600;text-transform:uppercase;letter-spacing:.12em;color:var(--ink-3);margin-bottom:18px}
.logos-row{display:flex;flex-wrap:wrap;justify-content:center;gap:14px 42px;font-family:var(--display);font-weight:700;font-size:20px;color:var(--ink-3);opacity:.8}
.section{padding:clamp(56px,8vw,108px) 0}
.head{text-align:center;max-width:680px;margin:0 auto clamp(36px,5vw,56px)}
.head h2{font-size:clamp(28px,4.2vw,44px);font-weight:800;letter-spacing:-.025em;line-height:1.1;margin-bottom:14px}
.head p{font-size:clamp(16px,1.9vw,19px);color:var(--ink-2)}
.features{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.feature{background:var(--paper-soft);border:1px solid var(--rule);border-radius:calc(16px*var(--r));padding:28px 26px;transition:transform .18s,box-shadow .2s,border-color .2s}
.feature:hover{transform:translateY(-4px);box-shadow:0 18px 40px -22px rgba(0,0,0,.4);border-color:var(--accent-line)}
.feat-ic{width:48px;height:48px;border-radius:calc(12px*var(--r));background:var(--accent-soft);display:flex;align-items:center;justify-content:center;margin-bottom:18px}
.feat-ic .ic{width:24px;height:24px;stroke:var(--c-1);fill:none;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.feature h3{font-size:19px;font-weight:700;margin-bottom:8px;letter-spacing:-.01em}
.feature p{font-size:15.5px;color:var(--ink-2)}
.stats{padding:clamp(28px,4vw,40px) 0}
.stats-row{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;background:var(--accent-soft);border:1px solid var(--accent-line);border-radius:calc(20px*var(--r));padding:clamp(26px,4vw,40px)}
.stats-row>div{text-align:center}
.stat-n{font-size:clamp(30px,4vw,46px);font-weight:800;letter-spacing:-.02em;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent;line-height:1}
body.em-solid .stat-n{background:none;-webkit-text-fill-color:var(--c-1);color:var(--c-1)}
.stat-l{font-size:14px;color:var(--ink-2);margin-top:8px}
.split-in{display:grid;grid-template-columns:1fr 1fr;gap:clamp(36px,6vw,72px);align-items:center}
.split.flip .split-art{order:-1}
.split h2{font-size:clamp(26px,3.6vw,38px);font-weight:800;letter-spacing:-.02em;line-height:1.12;margin-bottom:16px}
.split p{font-size:17px;color:var(--ink-2);margin-bottom:22px}
.ticks{list-style:none;display:flex;flex-direction:column;gap:13px}
.ticks li{display:flex;gap:12px;align-items:flex-start;font-size:16px;color:var(--ink-2)}
.li-ic{width:22px;height:22px;flex:none;stroke:var(--c-1);fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;margin-top:1px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.step{text-align:center;padding:0 10px}
.step-n{width:54px;height:54px;border-radius:50%;background:var(--grad);color:#fff;font-weight:800;font-size:22px;display:flex;align-items:center;justify-content:center;margin:0 auto 18px}
body.em-solid .step-n{background:var(--c-1)}
.step h3{font-size:19px;font-weight:700;margin-bottom:8px}
.step p{font-size:15.5px;color:var(--ink-2)}
.quote-in{max-width:840px;margin:0 auto;text-align:center;position:relative}
.quote-mark{font-family:var(--display);font-size:90px;line-height:.6;color:var(--accent-line);margin-bottom:8px}
.quote-in blockquote{font-family:var(--serif);font-size:clamp(22px,3.2vw,32px);font-weight:500;line-height:1.4;letter-spacing:-.01em;margin-bottom:24px}
.quote-by strong{font-family:var(--display);font-size:17px}
.quote-by span{display:block;color:var(--ink-3);font-size:14.5px;margin-top:3px}
.pricing{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;align-items:start}
.price-card{position:relative;background:var(--paper-soft);border:1px solid var(--rule);border-radius:calc(18px*var(--r));padding:30px 26px;display:flex;flex-direction:column;gap:18px}
.price-card.featured{border-color:var(--c-1);box-shadow:0 24px 50px -28px var(--c-1);transform:scale(1.03)}
.badge{position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:var(--grad);color:#fff;font-family:var(--display);font-size:12px;font-weight:600;padding:5px 14px;border-radius:999px}
body.em-solid .badge{background:var(--c-1)}
.price-name{font-family:var(--display);font-weight:700;font-size:18px}
.price-amt{font-size:40px;font-weight:800;letter-spacing:-.02em;line-height:1}
.price-amt span{font-family:var(--serif);font-size:15px;font-weight:400;color:var(--ink-3);letter-spacing:0}
.price-card .ticks{gap:11px}
.price-card .ticks li{font-size:15px}
.price-card .btn{width:100%;margin-top:6px}
.faq{display:flex;flex-direction:column;gap:12px}
.faq-i{border:1px solid var(--rule);border-radius:calc(12px*var(--r));background:var(--paper-soft);padding:0 22px}
.faq-i summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:18px 0;font-family:var(--display);font-weight:600;font-size:17px}
.faq-i summary::-webkit-details-marker{display:none}
.faq-x{font-family:var(--display);font-size:22px;color:var(--c-1);transition:transform .2s;flex:none}
.faq-i[open] .faq-x{transform:rotate(45deg)}
.faq-i p{color:var(--ink-2);font-size:15.5px;padding:0 0 18px}
.cta{background:var(--grad);color:#fff;text-align:center}
body.em-solid .cta{background:var(--c-1)}
.cta-in{padding:clamp(56px,8vw,96px) 0;max-width:720px;margin:0 auto}
.cta h2{font-size:clamp(28px,4.4vw,46px);font-weight:800;letter-spacing:-.02em;color:#fff;margin-bottom:14px}
.cta p{font-size:clamp(16px,2vw,20px);color:rgba(255,255,255,.88);margin-bottom:30px}
.footer{background:var(--paper-soft);border-top:1px solid var(--rule);padding-top:clamp(48px,6vw,72px)}
.foot-in{display:grid;grid-template-columns:1.4fr 2fr;gap:40px;padding-bottom:40px}
.fbrand p{color:var(--ink-3);font-size:15px;margin-top:14px;max-width:32ch}
.fcols{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.fhead{font-family:var(--display);font-weight:700;font-size:14px;text-transform:uppercase;letter-spacing:.05em;color:var(--ink);margin-bottom:14px}
.fcol a{display:block;color:var(--ink-2);font-size:15px;padding:5px 0}
.fcol a:hover{color:var(--c-1)}
.foot-bar{border-top:1px solid var(--rule);padding:22px 0 40px;color:var(--ink-3);font-size:13.5px;font-family:var(--mono)}
@media (max-width:880px){
  .nav-links{display:none}
  .nav.open .nav-links{display:flex;position:absolute;top:64px;left:0;right:0;flex-direction:column;background:var(--paper);border-bottom:1px solid var(--rule);padding:16px 24px;gap:14px}
  .burger{display:flex}
  .hero-in,.split-in,.foot-in{grid-template-columns:1fr}
  .split.flip .split-art{order:0}
  .hero-art{order:-1;max-width:420px}
  .features,.steps,.pricing{grid-template-columns:1fr}
  .stats-row{grid-template-columns:repeat(2,1fr)}
  .fcols{grid-template-columns:repeat(3,1fr)}
  .price-card.featured{transform:none}
}
@media (max-width:520px){ .fcols{grid-template-columns:1fr} .stats-row{grid-template-columns:1fr} }
"""

JS = r"""
const nav=document.getElementById('nav');
const onScroll=()=>nav&&nav.classList.toggle('scrolled',window.scrollY>8);
window.addEventListener('scroll',onScroll,{passive:true});onScroll();
document.querySelectorAll('.nav-links a, .nav-cta a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')));
"""

PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='9' fill='{favhex}'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={font}&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body class="{bodyclass}">
{sections}
<script>{js}</script>
</body>
</html>"""


def build_css(t):
    out = CSS
    for k in ("c1","c2","c3","soft","line","paper","papersoft","ink","ink2","ink3","rule","rulesoft","divider","display","serif","mono"):
        out = out.replace("{"+k+"}", t[k])
    out = out.replace("{radius}", str(t.get("radius", 1)))
    return out


def render_page(theme, content):
    global _LANG
    _LANG = content.get("lang", "cs")
    secs = "\n".join(RENDER[s["type"]](s) for s in content["sections"] if s["type"] in RENDER)
    return (PAGE
        .replace("{lang}", content.get("lang", "cs"))
        .replace("{title}", html.escape(content.get("title", theme["name"])))
        .replace("{desc}", html.escape(content.get("desc", "")))
        .replace("{favhex}", theme["c1"].replace("#", "%23"))
        .replace("{font}", theme["font"])
        .replace("{css}", build_css(theme))
        .replace("{bodyclass}", theme.get("bodyclass", ""))
        .replace("{sections}", secs)
        .replace("{js}", JS))


def build_one(theme):
    jp = os.path.join(CONTENT_DIR, theme["slug"].split("-")[0] + ".json")
    with open(jp, encoding="utf-8") as f:
        content = json.load(f)
    outdir = os.path.join(TPL_DIR, theme["slug"])
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_page(theme, content))
    return len(content["sections"])


if __name__ == "__main__":
    built = 0
    for t in THEMES:
        jp = os.path.join(CONTENT_DIR, t["slug"].split("-")[0] + ".json")
        if not os.path.exists(jp):
            print("skip (no content):", t["slug"]); continue
        n = build_one(t); built += 1
        print(f"built {t['slug']}: {n} sections")
    print(f"\nTotal landing pages built: {built}")
