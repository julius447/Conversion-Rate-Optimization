# SPEC — ServiceRouter (startsida) + Artikelns konverteringskort

**Status:** Buildable spec. Finaliserar två interventioner från round 2-designauditerna till produktion:
1. **ServiceRouter** — ersätter den dekorativa dusk-MiniMenu:n (`ampy-elfirma`) på plats 3 under den låsta heron, plus den **slimmade produktraden** som ersätter ProductGrid×2 + BlueCTA. Källa: `research/design/homepage-design.md` (HD-01…HD-14, direktiv 1–12, riktning A/B/C).
2. **Artikelns inline-CTA** ("Skicka en bild") + **Nästa steg-slutkortet** — de två konverteringsaffordanser artikelmallen saknar. Källa: `research/design/article-design.md` (AD-01…AD-07, direktiv 1–8, riktning A/B/C).

En Bricks-byggare ska kunna bygga varje block härifrån utan fler frågor: zoner, elementlista, storlekar/tokens, states, mobil+desktop-anatomi, svensk copy, candour-grindar.

**Källa i pixlar (verifierat mot tiles):** `home` desktop 02 (MiniMenu = det som rivs), `home` desktop 06 (ServiceGrid = mönstret som promoveras), `home` desktop 07–08 (ProductGrid + BlueCTA), `artikel-elcentral` mobil 03 (Snabbt svar-DNA), desktop 06 (tom högerspalt + räkneexempel-punktlista). Struktur-kontext (ej upprepad): HP-01…HP-13 (`research/templates/homepage.md`, `research/missing/block-service-router.md`); ART-01…ART-08 (`research/templates/articles.md`, `research/blocks/article-blocks.md`).

**Token-konvention:** samma DNA som `spec-hero-system.md`. Där px anges men exakt ap*-tokennamn är osäkert: `[token-GAP → ampy-design-system äger]`.

---

## 0. Delad token- & primitiv-DNA (gäller båda blocken)

### Färg
| Roll | Värde | Användning |
|---|---|---|
| `--ap-midnight` | `#090b32` | Nästa-steg-plattans grundyta; navy etiketter/rubriker på ljust. ALDRIG `#010328` (token-defekt). |
| `--ap-offwhite` | `#f5f9ff` | ServiceRouter-sektionens bakgrund (palett-reset mot heron). |
| `--ap-teal` | `#00a991` | **Reserverad för EN sak: den enda accenten.** Stripe, chevron, primär knapp-fyll, eyebrow-versal, aktiv TOC-pill. Ej på vit knapp-yta (klarar ej 4.5:1 mot vitt). |
| `--ap-teal-tint` | `#ECFBF7` | Inline-CTA-kortets bakgrund; TOC aktiv-pill-fyll. Ljus teal-dimma — stannar i artikelns ljusa register. |
| `--ap-teal-ink` | `#00806f` | Teal-text/ikon på ljus/vit yta där `#00a991` fallerar AA (≈4.6:1 mot vitt). |
| `--ap-white` | `#ffffff` | Kortytor, text på midnight. |
| `--ap-ink` | `#090b32` | Brödtext/rubriker på ljust (navy). |
| `--ap-ink-soft` | `#4a4f6a` | Sekundär brödtext/scent-underetikett på ljust. |
| `--ap-ink-on-navy` | `#c9d4e0` | Bröd/microtext på midnight (WCAG AA, ej ren grå). |
| `--ap-hairline` | `rgba(9,11,50,.10)` | Kortkant/avdelare på ljust. |

**Candour-färgregel (löser HD-05/HD-10):** ingen skrikgrön "SUPERKAMPANJ"-pill, ingen navy "BÄSTSÄLJARE", ingen ljust-cyan hav-knapp propageras hit. Teal förekommer i **små ytor** (stripe, chevron, EN knapp), aldrig som tapet.

### Typografi (Outfit)
| Element | Storlek mobil / desktop | Vikt | Färg |
|---|---|---|---|
| Sektions-H2 (router-rubrik) | 28px / 32px, lh 1.12 | 700 | `--ap-ink`, ROT/Grön-nyckelord i teal (behåll befintlig gradient-emfas) |
| Kort-etikett (tjänstenamn) | 19px / 20px | 600 | `--ap-ink` |
| Scent-underetikett | 14px / 15px, lh 1.4 | 400 | `--ap-ink-soft` |
| Länk-affordans ("Till X") | 14px / 15px, versal ej | 600 | `--ap-teal-ink` |
| Eyebrow (kort-CTA) | 12px / 13px, versal-spärrad `letter-spacing:.09em` | 600 | `--ap-teal-ink` |
| CTA-kort H3 | 19px / 22px, lh 1.2 | 700 | navy (inline) / vit (Nästa steg) |
| CTA-kort bröd | 16px / 17px, lh 1.55 | 400 | `--ap-ink-soft` (inline) / `--ap-ink-on-navy` (Nästa steg) |
| Knapp-label | 16px / 16px | 600 | per knapp |
| Trust-microrad | 13px | 500 | `--ap-ink-soft` / `--ap-ink-on-navy` |

### Spacing / form
- Kort-radius: `--ap-radius-l ~20px` (matchar Snabbt svar + ServiceGrid). Router-sektionens inre gutter: desktop 24px kort-gap, mobil 16px.
- Knapp-höjd: **52px desktop / 56px mobil**, radius `--ap-radius-m ~14px`, full bredd mobil.
- Sektions-vertikalmarginal: 72px desktop / 48px mobil.
- Inline-CTA-kortets stripe: **4px** teal vänster; Snabbt svar-stripe är ~6px → inline-CTA är medvetet tunnare (underordnad, en paus ej en vägg).

### Delade knapp-primitiver (biblioteket — en gång, återanvänds)
1. **`btn-primary-teal`** — solid `--ap-teal`-fyll, vit text (fyllytan klarar vit text AA), radius 14px, 52/56px. Den enda fyllda knappen per block.
2. **`btn-ring-dark`** — **den kanoniska Ring-knappen** (kanon från BlueCTA, HD-08): mörk `--ap-midnight`-yta, vit text, vit telefon-chip vänster. Ersätter ALLA ljust-cyana Ring-gradienter. På midnight-platta blir varianten `btn-ring-ghost` (transparent, 1px vit @40%-kant, vit text).
3. **`link-quiet`** — ren textlänk + chevron `↗`/`→`, `--ap-teal-ink`, understruken vid hover. **Ersätter det ljust-cyana pill-havet** (HD-02). Router-kortens affordans + tertiärlänkar.

**Regel som binder båda blocken (löser HD-02/HD-08/HD-10):** *ett block bär exakt EN fylld/mörk knapp som primär handling; router-korten bär ingen knapp alls — hela kortet är länkytan + en `link-quiet`.* Teal är accent, aldrig yta.

---

# DEL A — ServiceRouter (startsida, plats 3)

## A.1 Vad ögat möter idag (verifierat, ej upprepat i djup)
- **Rivs (home desktop 02):** MiniMenu = tre *lika stora* dusk-fotokort (hus / bil+laddbox / hus), **vit centrerad etikett** mitt i fotot, teal "Läs mer →"-pill svävande i mitten. Läses som affischtrio, inte tjänstemeny (HD-01/HD-14). Mobil pass 1: tre tomma navyrutor med ett ord (HD-06).
- **Promoveras (home desktop 06):** ServiceGrid = 6 kort med **riktiga funktionsfoton** (taklampa, öppen elcentral, kök…), **vänsterställd etikett + scent-paragraf + "Till {tjänst} ↗"** — men idag med en jättelik ljust-cyan pill (HD-02, ska demoteras) och på plats 8.
- **ServiceRouter = ServiceGrids grammatik, promoverad till plats 3, med demoterad länk-affordans + prio-viktad layout + palett-reset.**

## A.2 Systemroll & vikt mot den låsta heron
Heron = sidans tyngsta element (full-bleed dusk-foto, ~48px vit H1, EN teal-gradient-CTA). ServiceRouter = näst tyngst, **men aldrig en andra hero** (HD-14):
- **Bakgrund `--ap-offwhite`** (ej dusk-foto) = palett-reset "nu går vi från känsla till funktion".
- **Rubrik på H2-skala** (32px navy), tydligt under hero-H1.
- **Prio syns på en blick:** rad 1 = tjänster (prio #1) full billing; rad 2 = Laddbox + Batterilagring slimmade, halvhöga, 2-up, synligt underordnade.
- **EN accent (teal), små ytor.** Inget andra ljust-cyan-hav.

## A.3 Zon-anatomi

```
┌─ SECTION .service-router  (bg --ap-offwhite, pad-y 72/48) ───────────┐
│  [A] Rubrikzon  (centrerad, max-width 760px)                         │
│      H2 "Vad behöver du hjälp med?" + ROT-hook-underrad              │
│  [B] Tjänsteroutern  (rad 1 — PRIO #1, full billing)                 │
│      desktop: grid 3×2 (6 kort) · mobil: 1-kol staplat               │
│      [kort] foto 16:10 → etikett → scent → link-quiet "Till X ↗"     │
│  [C] Produktraden  (rad 2 — slimmad, underordnad)                    │
│      desktop: grid 1fr 1fr (2 kort, halvhöjd) · mobil: 1-kol         │
│      Laddbox FÖRST, Batterilagring efter (prio-ordning)              │
└──────────────────────────────────────────────────────────────────────┘
```

### [A] Rubrikzon
- **H2** (element: `heading`, tag h2): "Vad behöver du hjälp med?" — 32/28px, 700, navy, centrerad.
- **Underrad** (element: `text`): behåll ROT-hooken men som stödrad, ej egen rubrik: "Allt inom el för hemmet — installerat & klart, ofta med **30 % ROT-avdrag**." 16px, `--ap-ink-soft`, "30 % ROT-avdrag" i `--ap-teal-ink` 600. Max-width 620px, centrerad.
- Marginal H2→grid: 40/28px.

### [B] Tjänste-kort (rad 1) — elementlista per kort
Wrapper: `<a class="sr-card" href="{tjänst-url}">` — **hela kortet är länken** (större tap-target än en pill; löser HD-02). Kort = vit `--ap-white`, radius 20px, 1px `--ap-hairline`, skugga `0 6px 24px rgba(9,11,50,.06)`, hover: skugga → `0 12px 32px rgba(9,11,50,.10)` + translateY(-2px), 160ms.

| # | Element | Spec |
|---|---|---|
| 1 | Funktionsfoto | `img`, aspect 16:10, `object-fit:cover`, radius 20px top (kortets övre hörn), **riktigt foto av tinget** (återbruk ServiceGrids: taklampa / öppen elcentral / kök / luftvärmepump / smart hem / spotlights). `loading` = eager för de 2 första korten (nära första scroll, löser HD-06), lazy resten. `alt` = tjänstenamn. |
| 2 | Etikett | `heading` h3, vänsterställd, 20px 600 navy, pad 20px 20px 4px. |
| 3 | Scent-underetikett | `text`, 15px 400 `--ap-ink-soft`, **1 rad som säger vad tjänsten TÄCKER i kundens ord** (ej produktnamn). Pad 0 20px. |
| 4 | Länk-affordans | `link-quiet`: "Till {tjänst}" + teal `↗`, 15px 600 `--ap-teal-ink`, pad 12px 20px 20px. **Ingen fylld pill.** Understruken vid hover (kort-hover triggar även denna). |

**6 tjänster (prio-ordnade, tjänst > laddbox > batteri-doktrinen syns):**
| Kort | Etikett | Scent (kundens ord) | URL |
|---|---|---|---|
| 1 | Elfel & felsökning | Något som inte funkar? Vi hittar felet och åtgärdar. | `/elservice/felsokning/` `[URL-GAP verify]` |
| 2 | Byta elcentral | Gammalt proppskåp? Ny central enligt dagens krav. | `/elservice/byta-elcentral/` |
| 3 | Belysning | Spotlights, taklampor och design som funkar. | `/elservice/belysning/` |
| 4 | Kök & vitvaror | Säkra uttag och anslutning för spis, diskmaskin, ugn. | `/elservice/kok/` |
| 5 | Ladda bilen | Laddbox hemma, installerad och klar. | `/laddboxar/` |
| 6 | Solel & batteri | Lagra din solel och kapa effekttopparna. | `/solcellsbatteri/` |

> Not: kort 5–6 kan alternativt lyftas ut ur tjänsteroutern och BARA bo i produktraden [C] (undviker dubblering laddbox/batteri i både rad 1 och rad 2). **Default: håll rad 1 = de 4 rena tjänsterna + "Ladda bilen" + "Solel & batteri" som JOBB-formuleringar; låt [C] vara PRODUKT-teasern (pris/modell).** Se A.6 reasoned-against.

### [C] Produktrad (rad 2) — slimmad ProduktTeaser
Ersätter ProductGrid×2 (8 tunga kort) + BlueCTA. **Halvhöjd, 2-up, synligt underordnad** (HD:s prio-krav). Ingen specchip (3-fas/kWh bort, HD-04), inga badges (HD-05), pris **avrubrificerat** (HD-03).

Wrapper: `<a class="pr-card" href="{url}">`, horisontellt kort desktop (foto vänster 40% / text höger), staplat mobil.

| # | Element | Spec |
|---|---|---|
| 1 | Foto | Produktbild, 40% bredd desktop / full mobil, radius 20px, eager (nära scroll). |
| 2 | Kategori-etikett | h3, 18px 600 navy: "Laddbox" / "Solcellsbatteri". |
| 3 | Scent | 15px `--ap-ink-soft`, 1 rad: "Från {modell} — installerat & klart." |
| 4 | Pris (avrubrificerat) | **`text`, 15px 500 navy, INLINE med caveat, vänsterställt:** "Fr. 4 490 kr *efter Grön Teknik-avdrag*". Caveat 13px `--ap-ink-soft`. INTE 28px centrerad headline. |
| 5 | Länk | `link-quiet` "Se laddboxar →". Ingen ljust-cyan pill. |

**Prio-ordning i raden:** Laddbox (prio #2) **först/vänster**, Solcellsbatteri (prio #3) efter. (Battery-default-nedviktning per CLAUDE.md §0.6.)

## A.4 States
- **Kort default / hover / focus-visible:** hover = translateY(-2px) + fördjupad skugga; `:focus-visible` = 2px `--ap-teal` outline offset 2px (tangentbord). Hela `<a>` fokuserbart.
- **Foto-laddning:** LQIP/skeleton `--ap-hairline`-ton bakom varje `img` tills laddad (löser HD-06 — aldrig tom vit ruta på 9–10s-LCP-sida). De 2 första korten eager.
- **Reduced-motion:** `prefers-reduced-motion` → ingen translateY, bara skugg-övergång.

## A.5 Responsiv anatomi
- **Desktop (≥1024px):** [B] grid `repeat(3,1fr)` gap 24px, 2 rader. [C] grid `1fr 1fr` gap 24px, kort horisontella (foto vänster).
- **Surfplatta (768–1023px):** [B] `repeat(2,1fr)`; [C] behåller `1fr 1fr` men kort får stapla foto/text.
- **Mobil (≤767px):** [B] 1-kolumn, kort staplade (foto topp → text). [C] 1-kolumn, Laddbox överst. Sektionspadding-y 48px. Kort-tap-target hela ytan ≥88px höjd.
- **Ingen** full-bleed, inget dusk-foto, ingen centrerad-etikett-i-foto (dödar MiniMenu-affischen).

## A.6 Reasoned against — vad ServiceRouter ersätter och varför designen vinner
| Ersätter | Varför den nya designen konverterar bättre |
|---|---|
| **MiniMenu (`ampy-elfirma`)** dusk-affischtrio | (a) Palett-reset offwhite ≠ tredje dusk-foto → läses som NY sektion, ej hero-förlängning (HD-14). (b) Funktionsfoto av tinget + scent-rad = besökaren vet vad "Byta elcentral" täcker på en blick (dusk-landskap gjorde inte det, HD-01). (c) Vänsterställd etikett + `link-quiet` ↗ = router-grammatik, ej affisch. (d) Prio-viktad 6+2-layout gör tjänst>laddbox>batteri synligt (lika-tredjedels dolde det). |
| **ProductGrid ×2 (8 kort)** | 8 nästan-fullskärmshöga kort med 34 900 kr som sidans första prissignal (HP-01/HD-03) → ersätts av 2 slimmade teasers, pris avrubrificerat + caveat, laddbox först. Massiv speed-vinst (8→2 tunga bildkort, HP-12). |
| **BlueCTA** (understruket "elektriker!") | Falsk länk-affordans (HD-07) + redundant Ring mitt i grid. Ring-handlingen kanoniseras till `btn-ring-dark` och bor i MainCTA (plats 6, förtjänad). BlueCTA:s enda goda del — den svarta Ring-knappen — lever vidare som primitiv, inte som eget block. |
| **8× ljust-cyan "Läs mer"-pill** | Fel element vann kortet (störst+ljusast, lägst värde, HD-02). `link-quiet` demoterar handlingen "lämna startsidan"; hela kortet blir länken → större target, lägre visuell tyngd, teal återvunnet till EN accent (HD-10). |

## A.7 Candour-grindar (ServiceRouter)
- Inga "SUPERKAMPANJ"/"BÄSTSÄLJARE"/"NYHET"-badges (osubstansierat, ⚑ HD-05) — bort.
- Pris **alltid** med "efter Grön Teknik-avdrag"-caveat på samma rad — aldrig naket lockpris.
- Ingen "5.0"/recensions-siffra i routern (proof-lagret bärs av Testimonials plats 4).
- Scent-copy = sant om vad tjänsten täcker, ampy-röst du-tilltal, ingen brådska/scarcity.
- URL-scent: `[URL-GAP]` för `/elservice/felsokning/` verifieras mot sitemap före bygg.

## A.8 Divergenta riktningar — ServiceRouter (från HD-riktning A/B/C)
- **Riktning A — Ikon-router (lugnast, snabbast).** Rad 1 = 6 flata kort på vitt, EN linje-ikon per tjänst (lampa/elcentral/laddkontakt/kök/förstoringsglas/blixt), fet navy-etikett, scent-underrad, teal chevron. **Noll bildvikt (SVG) = direkt LCP-vinst.** Risk: mindre varm. *Använd om speed-budget är hård.*
- **Riktning B — Foto-router (REKOMMENDERAD default, specad ovan).** ServiceGrids beprövade funktionsfoto-grammatik promoverad. Varm, konkret scent, lägst designrisk (mönstret finns redan på sidan).
- **Riktning C — Behov/jobb-router (testkandidat).** Rad 1 = kompakta chips i kundens ord ("Elfel eller felsökning", "Byta elcentral"…) som deep-linkar ELLER för-fyller inline-formuläret. Högst intent-capture, mest candour-linjerad. Kräver ny chip-komponent. **Kör som A/B mot B, ej default.**

## A.9 Vad som INTE ska röras (Del A)
- **Den låsta heron** + dess trust-rad (ägar-canon).
- **ServiceGrids funktionsfoto + scent-etikett-grammatik** — det GODA mönstret; bevara & promotera, uppfinn inte om.
- **Testimonials (plats 4), VarProcess (5), MainContact (9)** — starka, utanför detta blocks scope.
- **Den svarta Ring-knappen** — kanoniseras som `btn-ring-dark`-primitiv, ändras ej.

---

# DEL B — Artikelns konverteringskort

## B.1 Vad ögat möter idag (verifierat)
- **Snabbt svar-DNA (mobil 03):** vitt kort, ~6px grön→teal vänsterstripe, grön bock, `SNABBT SVAR`-eyebrow spärrad versal, bold "Sammanfattning:"/"Nyckelpunkter:" + navy punktlista. Mallens bästa element — **nya korten talar dess språk men inverterar signalen (handling, ej info).**
- **Tom kanal (mobil hela 49 884px):** noll ring/form i brödtexten (AD-01). **Desktop (tile 06):** hela högra ~30%-spalten tom vit yta efter att TOC tar slut (AD-01 desktop).
- **Fel CTA i bästa slot (AD-02):** enda stylade CTA-kortet = Google-review-ask efter FAQ — exporterar varmaste trafiken bort.
- **Tre nya affordanser byggs:** (1) inline-CTA mitt i texten, (2) Nästa steg-slutkort i review-slotten, (3) persistent högerräls-kort på desktop.

## B.2 Block 1 — INLINE-CTA "Skicka en bild" (teal-tint-panel)

**Placering:** direkt efter första pristabellen (~25–35 % scroll-djup, där prisnyfikenheten toppar). I brödtextens kolumn (65% desktop / full mobil).

**Designsignal (löser AD-01):** native till Snabbt svar men **invers** — ljus teal-tint, ej vitt; en PAUS, ej en vägg. Medvetet KORTARE än Snabbt svar.

```
┌─ .article-inline-cta  (bg --ap-teal-tint, 4px teal vänsterstripe, radius 20px) ─┐
│  KOSTNADSFRI BEDÖMNING            ← eyebrow, teal versal-spärrad               │
│  Osäker på just ditt proppskåp?   ← H3, navy 700                              │
│  Skicka ett par skarpa bilder på din central — du får en kostnadsfri          │
│  bedömning och ett prisförslag inom två arbetsdagar.   ← 1 brödrad, navy-soft  │
│  [ Skicka en bild ]               ← EN knapp, btn-primary-teal                 │
└────────────────────────────────────────────────────────────────────────────────┘
```

| # | Element | Spec |
|---|---|---|
| 1 | Wrapper | `<div class="article-inline-cta">`, bg `--ap-teal-tint`, **4px** `--ap-teal` vänsterstripe (ej 6px — underordnad Snabbt svar), radius 20px, inre padding 24px, vertikal marginal 48–56px (isolerar som paus). **Vänsterställt, aldrig centrerat.** |
| 2 | Eyebrow | `text`, "KOSTNADSFRI BEDÖMNING", 12px 600 `--ap-teal-ink` versal-spärrad `.09em` — samma stil som `SNABBT SVAR`. |
| 3 | H3 | `heading` h3 (semantisk nivå matchar omgivande h2/h3), "Osäker på just ditt proppskåp?", 20/19px 700 navy. |
| 4 | Bröd | `text`, 1 rad (max 2), 16px 400 `--ap-ink-soft`, lh 1.55. |
| 5 | Knapp | `btn-primary-teal` "Skicka en bild" → `/offert?arende=byta-elcentral&fokus=bild` (formulär förifyllt "Byta elcentral", bild-upload i fokus). **Ett enda lågfriktionssteg — inget telefonnummer här** (Baymard: färre synliga fält). Desktop auto-bredd vänster; **mobil full bredd, ≥44px tap.** |

**States:** knapp hover = teal −8% lightness; `:focus-visible` 2px navy outline; reduced-motion = ingen transform. Kortet ärver ingen enterView-fade som döljer det (måste finnas på first paint — konverteringsyta får aldrig lazy-döljas).

**Höjd:** medvetet 3–4 rader → läser som paus, ej vägg.

## B.3 Block 2 — NÄSTA STEG-slutkort (midnight-platta)

**Placering:** efter FAQ, **tar review-CTA:ns slot** (AD-02). Detta kort FÅR bära mest visuell vikt i end-zonen — det är beslutspunktens primära ask.

```
┌─ .article-next-step  (bg --ap-midnight, radius 20px, pad 40/28px) ──────────┐
│  NÄSTA STEG                       ← eyebrow, teal versal                     │
│  Vill du ha ett fast pris på ditt elcentralbyte?   ← H3 VIT 700             │
│  Berätta om ditt skåp så återkommer vi med en kostnadsfri offert — du       │
│  ligger aldrig ute med pengarna.        ← bröd, --ap-ink-on-navy            │
│  [ Få en kostnadsfri offert ]   [ Ring 010-265 79 79 ]   ← 2 knappar        │
│  Räkna själv i Elcentral-kollen →       ← tertiär link-quiet (vit @70%)     │
│  ─────────────────────────────────────                                      │
│  Registrerad hos Elsäkerhetsverket · ROT förräknat på fakturan ·           │
│  Fast pris i offerten               ← trust-fot, 13px, INGEN 5.0-siffra     │
└──────────────────────────────────────────────────────────────────────────────┘
```

| # | Element | Spec |
|---|---|---|
| 1 | Wrapper | `<div class="article-next-step">`, bg `--ap-midnight` (aldrig `#010328`), full kolumnbredd, radius 20px, padding 40px desktop / 28px mobil. Den mörka plattan = end-zonens visuella ankare, maximal separation från vita brödkort. |
| 2 | Eyebrow | "NÄSTA STEG", 12px 600 `--ap-teal` versal-spärrad. (Teal klarar AA mot midnight.) |
| 3 | H3 | VIT 700, 22/19px: "Vill du ha ett fast pris på ditt elcentralbyte?" |
| 4 | Bröd | 1–2 rader, `--ap-ink-on-navy` 16px, lh 1.55: "Berätta om ditt skåp så återkommer vi med en kostnadsfri offert — du ligger aldrig ute med pengarna." |
| 5 | Primär knapp | `btn-primary-teal` "Få en kostnadsfri offert" → `/offert?arende=byta-elcentral`. |
| 6 | Sekundär knapp | `btn-ring-ghost` (transparent, 1px vit @40%, vit text, vit telefon-chip) "Ring 010-265 79 79" → `tel:+46102657979`. |
| 7 | Tertiär länk | `link-quiet` vit @70% "Räkna själv i Elcentral-kollen →" → `/elcentral-kollen/`. |
| 8 | Trust-fot | `text`, 13px `--ap-ink-on-navy`, hårlinje-avdelare ovanför: "Registrerad hos Elsäkerhetsverket · ROT förräknat på fakturan · Fast pris i offerten". **Ingen 5.0-siffra** — per doktrinens seed: ta bort ratingraden så knapparna blir hela fokuset. |

**Knapp-layout:** desktop = knapp 5 + 6 sida vid sida (row, gap 12px), länk 7 under; mobil = staplat full bredd (primär överst), 56px höjd, ≥44px tap.

**States:** primär hover = teal −8%; ghost hover = kant vit @70% + yta `rgba(255,255,255,.06)`; focus-visible = 2px teal outline. Ingen brådsketimer, ingen countdown (candour).

## B.4 Block 3 — Persistent högerräls-kort (desktop, löser AD-01-desktop + AD-05-tomränna)

**Placering:** desktop högerspalt (~30%), från ~20 % scroll och nedåt, **efter att TOC-kortet tar slut** (fyller den tomma vita rännan, tile 06/15–20). `position: sticky; top: 8rem`.

| # | Element | Spec |
|---|---|---|
| 1 | Wrapper | Kondenserad vertikal Nästa-steg: litet `--ap-midnight`-kort, radius 16px, padding 20px, max-width ~300px (spaltbredd). |
| 2 | Avatar | Edvin-miniatyr (Faktagranskad-av-personen), rund 40px, top. |
| 3 | Rubrik | "Prata med en elektriker", vit 600 17px. |
| 4 | Bröd | 1 rad `--ap-ink-on-navy` 14px: "Skicka en bild på ditt skåp — Edvin läser den samma dag." |
| 5 | Primär knapp | `btn-primary-teal` full bredd "Få offert" → `/offert`. |
| 6 | Tel-länk | `link-quiet` vit "010-265 79 79" → tel. |

**Sichtbarhet:** ENDAST ≥1024px (spalten finns bara på desktop). **Mobil-motsvarighet:** valfri tunn sticky bottenbar (1 rad: "Få offert" + tel-ikon) som **experiment, ej default** — mobilbrödtextens inline-CTA (B.2) bär huvudlasten där.

**States:** sticky får inte överlappa footer — `bottom`-gräns via container. Reduced-motion oförändrat (sticky ≠ animation).

## B.5 Reasoned against — vad de nya korten ersätter/kompletterar
| Ersätter/kompletterar | Varför designen vinner |
|---|---|
| **Review-CTA (Google-ask) i bästa slot** | Exporterade varmaste trafiken till Google.com och bad fel publik (läsare ≠ recensent, AD-02). Nästa-steg-midnight-plattan tar slotten med en offert/ring-ask; review demoteras UNDER den, kund-gate:ad ("Har vi hjälpt dig tidigare?"). |
| **Tom desktop-högerränna** (AD-01/AD-05) | ~70% oanvänd premium-yta efter TOC → persistent sticky Nästa-steg-kort = konvertering + Edvin-trust exakt där "kan jag lita på dem?"-beteendet uppstår (Clarity: kontakt→Om-oss). |
| **Noll affordans i brödtexten** (AD-01) | Inline-CTA vid prisnyfikenhetens topp (MECLABS: m+v toppar vid pris, i=0 idag). Teal-tint-paus native till Snabbt svar men invers signal. |
| **Snabbt svar-kortets stripe-tjocklek** | Inline-CTA:s 4px < Snabbt svars 6px = medveten underordning (info-kortet ska förbli det tyngsta vita elementet; CTA:t är en lätt paus). |

## B.6 Candour-grindar (Del B)
- **Ingen 5.0-siffra i konverterings-korten** (inline eller Nästa steg) — ratingen bor ENDAST i den demoterade review-kontexten, förankrad "5.0 · {N} omdömen på Google" med antal (owner-verify current), aldrig i tävlan med asken.
- Trust-fot = **candour-sanna** claims som svarar Byggahus-oron (Elsäkerhetsverket-registrering, ROT på fakturan, fast pris) — inga fabricerade tal.
- Inline-CTA "inom två arbetsdagar" = SLA-claim → `[GAP → owner-verify]` innan live (om ej bekräftat: "så snart vi kan").
- Ingen brådska/countdown/scarcity. Ampy-röst du-tilltal, konsultativt register — bevarar artikelns anti-sälj-moat.
- Bevara "När vi avråder från byte — komplettering räcker"-sektionen orörd (varumärkets moat i artikelform).

## B.7 Divergenta riktningar — Nästa steg-slutkortet (från AD-riktning A/B/C)
- **Riktning A — Midnight-platta (REKOMMENDERAD default, specad B.3).** Ankare/premium, tillhör MainCTA-familjen, maximal separation från vita brödkort. Risk: mörkt band kan kännas "annons" → motverkas av candour-copy utan brådska.
- **Riktning B — Mjuk teal-tint-panel (default för INLINE B.2, alternativ för slutet).** Ljus `--ap-teal-tint`, stannar i artikelns ljusa register, minst "annons-ig". Risk: lägre visuell vikt vid beslutspunkten än A.
- **Riktning C — Split-kort med riktig elektriker (high-effort testkandidat).** Vänster Edvins ansikte + mänsklig utfästelse ("Jag läser din bild samma dag — Edvin, kvalitetsansvarig"); höger mini-lead-teaser (namn/telefon/postnr) som postar lead inline. Maximal trust, svarar "kan jag lita på dem?". Risk: tyngst att bygga + formfriktion vid beslutspunkt → A/B mot A.
- **Default-mix:** B för inline (~30% djup, tyst), A för Nästa steg (ankare), C som A/B-test mot A i slutslotten.

## B.8 Vad som INTE ska röras (Del B)
- **Snabbt svar-kortet** — mallens bästa element; exportera dess DNA, ändra ej det.
- **Bylinens innehåll + `Verifierad av expert`-pill + `17 min läsning`** — E-E-A-T starkt; rör bara avatar-mappning/mobilluft (separat fynd AD-05), ej substans.
- **Brödtextens rytm** — Outfit, navy `#090b32`, lh ~1.7, teal inline-länkar. Krymp/färga ej.
- **Desktop-prismatrisen** (ren 4-kolumn) — endast mobilreflowen är ett separat fynd (AD-03), ej dessa kort.
- **Citatet från Edvin** + anti-sälj-sektionen — varumärkets moat.
- **Den förankrade "5.0 · {N} omdömen"-notationen** — behåll mönstret, endast i demoterad review-kontext.

---

## C. Bygg-ordning & beroenden (för Bricks-byggaren)
1. Definiera de 3 delade primitiverna EN gång (`btn-primary-teal`, `btn-ring-dark`/`btn-ring-ghost`, `link-quiet`) + de 3 nya CSS-vars (`--ap-teal-tint`, `--ap-teal-ink`, `--ap-offwhite`) — gäller båda blocken + propageras till MainCTA/BlueCTA-fixarna.
2. **Del A** som ny Bricks-sektion `service-router` (villkor: `post_url == site_url`, ersätter `ampy-elfirma`-sektionen på plats 3; ProduktTeaser [C] ersätter ProductGrid×2 + BlueCTA på plats 7).
3. **Del B** som 3 återanvändbara Bricks-block insprängda i artikel-CPT-mallen: inline-CTA (shortcode/block insatt efter första tabell), Nästa steg (efter FAQ), högerräls-kort (i högerspaltens sticky-container).
4. Öppna `[GAP]`: verifiera `/elservice/felsokning/`-URL, "inom två arbetsdagar"-SLA, aktuellt recensions-antal `{N}`, och att `/offert`-formuläret tar `?arende=`+`&fokus=bild`-parametrarna.
