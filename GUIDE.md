# Průvodce sekcemi

Obsah každé stránky je jeden JSON soubor `build/content/NN.json`:

```json
{ "lang": "cs", "title": "Titulek do záložky", "desc": "popis pro SEO",
  "sections": [ {"type":"nav", ...}, {"type":"hero", ...} ] }
```

Pořadí a sada sekcí je pevná (13 sekcí ve stejném pořadí ve všech šablonách):
`nav, hero, logos, features, stats, split1, split2, steps, testimonial, pricing,
faq, cta, footer`. Vyměňujete jen texty. Každý `h1` a `h2` musí mít právě jeden
`<em>výraz</em>` (akcentní barva). Nikdy nepoužívejte znak dlouhé pomlčky (em dash).

## nav
```json
{"type":"nav","brand":"Značka","links":["Funkce","Ceník","FAQ","Kontakt"],"cta":"Vyzkoušet"}
```

## hero
`illus` viz seznam dole.
```json
{"type":"hero","eyebrow":"Ukázková šablona","h1":"Velký <em>slib</em>.","sub":"Jedna věta navíc.","cta":"Hlavní akce","cta2":"Vedlejší akce","illus":"network"}
```

## logos
```json
{"type":"logos","label":"Důvěřují nám","items":["Alfa","Beta","Gama","Delta","Epsilon"]}
```

## features
Šest karet, každá `[ikona, nadpis, text]`.
```json
{"type":"features","h2":"Vše na <em>jednom místě</em>.","sub":"Podtitul.","cards":[
  ["zap","Rychlé","Text."],["shield","Bezpečné","Text."],["users","Týmové","Text."],
  ["chart","Přehledné","Text."],["lock","Soukromé","Text."],["sparkle","Chytré","Text."]]}
```

## stats
Čtyři dvojice `[číslo, popisek]`.
```json
{"type":"stats","items":[["12k+","klientů"],["98%","spokojených"],["4,9","hodnocení"],["24/7","podpora"]]}
```

## split1 a split2 (text + ilustrace, střídavě)
`split1` má ilustraci vpravo, `split2` vlevo. `bullets` = 3 řetězce.
```json
{"type":"split1","eyebrow":"Krok","h2":"Od A k <em>Z</em>.","text":"Odstavec.","bullets":["Bod jedna","Bod dva","Bod tři"],"illus":"growth"}
```

## steps
Tři kroky `[nadpis, text]`.
```json
{"type":"steps","h2":"Začněte ve <em>třech krocích</em>.","sub":"Podtitul.","steps":[["Krok 1","Text."],["Krok 2","Text."],["Krok 3","Text."]]}
```

## testimonial
```json
{"type":"testimonial","quote":"Text citátu.","author":"Jméno","role":"Role, Firma"}
```

## pricing
Tři tarify, právě jeden `featured: true` (zvýrazní se a dostane odznak).
```json
{"type":"pricing","h2":"Jednoduchý <em>ceník</em>.","sub":"Podtitul.","tiers":[
  {"name":"Start","price":"0 Kč","period":"/ měsíc","features":["A","B","C","D"],"cta":"Začít","featured":false},
  {"name":"Tým","price":"299 Kč","period":"/ měsíc","features":["A","B","C","D"],"cta":"Vyzkoušet","featured":true},
  {"name":"Firma","price":"na míru","period":"","features":["A","B","C","D"],"cta":"Kontakt","featured":false}]}
```

## faq
Pět dvojic `[otázka, odpověď]` (nativní rozbalování).
```json
{"type":"faq","h2":"Časté <em>dotazy</em>.","items":[["Otázka?","Odpověď."],["...","..."]]}
```

## cta
```json
{"type":"cta","h2":"Připraveni <em>začít</em>?","sub":"Podtitul.","button":"Hlavní akce"}
```

## footer
Tři sloupce, každý `[nadpis, odkaz, odkaz, odkaz, odkaz]`.
```json
{"type":"footer","brand":"Značka","tagline":"Krátký popis (ukázková značka).","columns":[
  ["Produkt","Funkce","Ceník","Novinky","Stav"],
  ["Firma","O nás","Kariéra","Blog","Kontakt"],
  ["Právní","Soukromí","Podmínky","Cookies","Bezpečnost"]],"copyright":"// ukázková šablona s dummy obsahem"}
```

---

## Klíče ikon (features, list)
```
zap shield bolt chart trend users user clock calendar lock globe heart star
check rocket phone mail map sparkle leaf tool camera cart gift play cpu doc
home scissors wrench sun target
```

## Klíče ilustrací (hero, split1, split2)
```
network growth shield layers target chat people spark phone leaf house cart globe chart
```

## Přidání ikony nebo ilustrace
V `build/build.py`: ikona do `ICONS` (viewBox 0 0 24 24, jen tahy),
ilustrace do `ILLUS` přes `_ill(body)` (viewBox 0 0 240 200, barva `var(--c-1)`).
Pak `python3 build/build.py`.
