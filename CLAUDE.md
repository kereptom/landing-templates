# CLAUDE.md  (read this first, then stop)

Knihovna landing-page šablon. **36 hotových responzivních stránek na jednom enginu.**
Tahle stránka je celý kontext, který potřebuješ. Needituj a nečti všechno, najdi
si v tabulce dole to jedno číslo (`NN`) a jdi rovnou na jeho soubory.

## Jak to funguje (30 sekund)

- `templates/NN-slug/index.html` jsou **vygenerované výstupy**. NIKDY je needituj ručně.
- Zdroj pravdy = `build/build.py` (engine + CSS/JS + `THEMES` + renderery sekcí) a
  `build/content/NN.json` (obsah jedné stránky, čistá data).
- Build: `python3 build/build.py` přepíše VŠECHNY `templates/*/index.html`.
  Galerie: `python3 build/gallery.py` přepíše kořenový `index.html`.

## Nejčastější úkol: upravit jednu stránku

1. Najdi `NN` v tabulce dole (uživatel ti řekne značku nebo obor).
2. Obsah (texty, ceny, sekce): edituj jen `build/content/NN.json`. Sekce a jejich
   tvar jsou v `GUIDE.md` (otevři jen když potřebuješ shape). Stránka má 13 sekcí
   v pevném pořadí: nav, hero, logos, features, stats, split1, split2, steps,
   testimonial, pricing, faq, cta, footer.
3. Vzhled (barvy, fonty, radius, styl karet): edituj `mk("NN-slug", ...)` v `THEMES`
   v `build/build.py`. `mk()` dopočítá odstíny, stačí `c1`, paper/ink, `dark`,
   `radius`, `bodyclass`.
4. Spusť `python3 build/build.py`. Hotovo.
5. Deploy (jen na vyžádání): `vercel deploy --prod --yes` z kořene projektu.
   Web: https://28landingtemplates.vercel.app  GitHub: kereptom/landing-templates

## Co NEČÍST (šetři tokeny)

- Neotevírej všech 36 `templates/*/index.html` ani všech 36 `content/*.json`.
  Pracuj jen s tím jedním `NN`, které uživatel zadal.
- Nechoď do jiných projektů. Engine je samostatný.
- `README.md` = přehled, `GUIDE.md` = schéma sekcí. Čti je cíleně, ne pro orientaci.

## Pravidla (tvrdá)

- Obsah je ZÁMĚRNĚ ukázkový (dummy). Drž ten styl, pokud uživatel nechce reálná data.
- NIKDY dlouhou pomlčku (em dash, U+2014). Místo ní `:` `,` `.` nebo závorku.
- Každý h1 a h2 obsahuje právě jeden `<em>…</em>` (akcent).
- Ikony jen z `ICONS`, ilustrace jen z `ILLUS` (v `build/build.py`, seznam v `GUIDE.md`).
- pricing: právě jeden tarif `featured: true`.

## Engine: pár faktů

- 13 sekcí (viz výše). Responzivní (mobilní menu, sekce se skládají), sticky nav,
  FAQ přes nativní `<details>`, inline SVG ikony i ilustrace barvené přes téma.
- Témata: světlá i tmavá (`dark=True`), `radius` škáluje rohy, `bodyclass` může být
  `em-solid` (plný akcent místo gradientu).
- Vše inline: vygenerovaný HTML je samostatný (CSS+JS uvnitř), bez závislostí.

## Index šablon (NN -> slug)

| NN | slug | značka | obor | jazyk | režim |
|----|------|--------|------|-------|-------|
| 01 | `01-nimbus-saas` | Nimbus | Projektový SaaS | en | light |
| 02 | `02-pulsefit` | PulseFit | Fitness aplikace | en | light |
| 03 | `03-zrnko-kavarna` | Zrnko | Kavárna a pražírna | cs | light |
| 04 | `04-hajek-advokat` | Hájek & partneři | Advokátní kancelář | cs | light |
| 05 | `05-remeslo-plus` | Řemeslo+ | Řemeslník a instalatér | cs | light |
| 06 | `06-brightsmile` | BrightSmile | Zubní ordinace | en | light |
| 07 | `07-domov-reality` | Domov | Realitní kancelář | cs | light |
| 08 | `08-bistro-oliva` | Bistro Oliva | Restaurace | cs | light |
| 09 | `09-frame-studio` | Frame Studio | Fotograf | en | light |
| 10 | `10-studio-vlna` | Studio Vlna | Kreativní agentura | cs | light |
| 11 | `11-chainly` | Chainly | Web3 a blockchain | en | dark |
| 12 | `12-penize-fintech` | Peníze | Fintech a platby | cs | light |
| 13 | `13-learnly` | Learnly | Online kurzy | en | light |
| 14 | `14-calm-yoga` | Calm | Jóga a wellness | en | light |
| 15 | `15-ironhouse` | IronHouse | Posilovna | cs | dark |
| 16 | `16-lesk-kadernictvi` | Lesk | Kadeřnictví a beauty | cs | light |
| 17 | `17-sharp-barber` | Sharp | Holičství | en | dark |
| 18 | `18-stavby-cz` | Stavby CZ | Stavební firma | cs | light |
| 19 | `19-sparkle-cleaning` | Sparkle | Úklidové služby | en | light |
| 20 | `20-tlapka-pet` | Tlapka | Péče o mazlíčky | cs | light |
| 21 | `21-wander-travel` | Wander | Cestovní kancelář | en | light |
| 22 | `22-summit-event` | Summit | Konference a eventy | en | dark |
| 23 | `23-mikrofon-podcast` | Mikrofon | Podcast | cs | light |
| 24 | `24-inbox-newsletter` | Inbox | Newsletter a média | en | light |
| 25 | `25-shoptik-eshop` | Shoptik | E-shop platforma | cs | light |
| 26 | `26-cortex-ai` | Cortex | AI nástroj | en | dark |
| 27 | `27-slunce-solar` | Slunce | Solární energetika | cs | light |
| 28 | `28-autohub` | AutoHub | Autosalon | en | dark |
| 29 | `29-prostor-interier` | Prostor | Interiérový design | cs | light |
| 30 | `30-forever-wedding` | Forever | Svatební agentura | en | light |
| 31 | `31-pohyb-fyzio` | Pohyb | Fyzioterapie | cs | light |
| 32 | `32-metrica` | Metrica | Produktová analytika | en | light |
| 33 | `33-saldo-ucetni` | Saldo | Účetnictví | cs | light |
| 34 | `34-echo-music` | Echo | Hudební kapela | en | dark |
| 35 | `35-pomahame-nezisk` | Pomáháme | Nezisková organizace | cs | light |
| 36 | `36-estate-lux` | Estate | Luxusní reality | en | dark |
