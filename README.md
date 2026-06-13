# Landing-page šablony

Knihovna **36 hotových landing pages** postavených na jednom sdíleném enginu.
Každá stránka je **samostatný responzivní HTML soubor** (veškerý CSS i JS uvnitř),
takže ji stačí zkopírovat, otevřít v prohlížeči a nasadit. Žádný build za běhu,
žádné závislosti.

> **Pozor:** všechny šablony obsahují **ukázkový (dummy) obsah**. Názvy značek,
> čísla i citace jsou smyšlené a slouží jen k předvedení vizuálních stylů.
> Před reálným použitím obsah nahraďte vlastním.

Živá galerie: viz `index.html` (po nasazení na Vercel kořen webu).

## Co každá stránka obsahuje (13 sekcí)

nav (sticky), hero, logos (důvěřují nám), features (6 karet s ikonami),
stats (4 čísla), split1 a split2 (text + ilustrace, střídavě), steps (3 kroky),
testimonial (citát), pricing (3 tarify, prostřední zvýrazněný), faq (5 otázek,
nativní rozbalování), cta (barevný pruh), footer (3 sloupce odkazů).

Responzivní (mobilní menu, sekce se skládají pod sebe), sticky nav se stínem při
scrollu, FAQ přes nativní `<details>`, inline SVG ikony i ilustrace barvené přes
téma. Žádný obrázkový asset.

## Struktura repozitáře

```
28_landing_templates/
├── index.html                 # galerie všech šablon (kořen webu)
├── README.md / GUIDE.md / CLAUDE.md
├── templates/NN-slug/index.html   # 36 hotových, samostatných stránek
├── gallery/shots/             # náhledy do galerie (PNG)
└── build/
    ├── build.py               # engine + THEMES + renderery sekcí
    ├── gallery.py             # generátor galerie
    └── content/NN.json        # obsah jedné stránky (data, ne kód)
```

Stránky v `templates/` jsou **vygenerované výstupy**. Zdroj pravdy je
`build/build.py` (engine + témata) a `build/content/*.json` (obsah).

## Tři způsoby použití

1. **Jen použít:** otevřete `templates/<slug>/index.html`. Hotovo, funguje offline.
2. **Vyměnit obsah:** upravte `build/content/NN.json` (schéma viz `GUIDE.md`) a
   spusťte `python3 build/build.py`. Vznikne nový samostatný HTML.
3. **Nový vzhled:** upravte řádek `mk("NN-slug", ...)` v `THEMES` v
   `build/build.py` (barva `c1`, fonty, `radius`, `bodyclass`). Pomocník `mk()`
   dopočítá odstíny. Galerii obnovíte přes `python3 build/gallery.py`.

## Nasazení (Vercel)

Čistě statické. `vercel deploy --prod`. Kořen = galerie, stránky na
`/templates/<slug>/index.html`.

## Pravidla stylu

- Jeden akcentní výraz na nadpis přes `<em>…</em>` (dostane barvu tématu).
- Ikony, ilustrace = jen klíče ze sad `ICONS` a `ILLUS` v `build/build.py`
  (seznam i v `GUIDE.md`).
- Nikdy znak dlouhé pomlčky (em dash, U+2014). Místo něj `:` `,` `.` nebo závorku.
