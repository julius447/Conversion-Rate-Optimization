# Spec — Eljour-kitet (sticky call-bar · two-lane kontakt · symptomblock-polish)

Build-spec för de tre komponenter som gör eljour-ytan (geo `eljour-i-{ort}` + pillar `eljour`) call-first. Bygger på designauditen `research/design/eljour-design.md` (fynd E-01…E-12, direktiv 1–10). Detta dokument översätter direktiven till Bricks-byggbara specar: zoner, elementlista, storlekar, tokens, states, mobil+desktop-anatomi, copy-mönster (svenska, ampy-röst), candour-grindar. Ingen ny research — ren konstruktion.

**Grundpremiss (från E-01/E-02/E-04):** ytan är urgent-intent (husägare 22:30, elfel). De två konverteringarna är RING (010-265 79 79 / `tel:+46102657979`) och FORMULÄR (→ /thank-you). På denna yta är **samtal primärt, formulär sekundärt** — dagens design har det omvänt.

---

## 0. Delade tokens (gäller alla tre komponenter)

Reuse ap*-skalan + de befintliga Ampy-tokens. Endast EN ny semantisk token behövs; allt annat finns.

| Token (semantisk) | Värde | Not |
|---|---|---|
| `--ampy-teal` | `#00a991` | Ampy-accent. **Får ej bära vit text** (klarar ej 4.5:1 mot vitt). Används för glow, prickar, ikoner, hover-ringar — aldrig som knappyta med vit text. |
| `--ampy-midnight` | `#090b32` | Rubriker, mörk text. |
| `--eljour-emergency-green` | *återanvänd exakt värdet på den befintliga `Ring eljouren`-knappen i symptomkortet* (djup pin-/skogsgrön, ca `#0d5b46`) | **Builder: sampla den redan pixelgodkända knappen — pick INTE ett nytt värde.** Detta är sidans bästa element (auditen "rör inte"). Vit text mot den passerar 4.5:1. |
| `--sev-akut` | röd `#e5484d` (prick + pill-text), pill-bg `#fdeceb` | Severity: Akut. Befintlig. |
| `--sev-varning` | amber `#d9a300` (prick + pill-text), pill-bg `#fbf3dc` | Severity: Varning. Befintlig. |
| Font | Outfit (viktledd: 400 body, 600 semibold, 700 rubrik) | Ingen annan familj. |
| Radie | knappar `ap-radius-lg` (~14px), kort `ap-radius-xl` (~20px) | Matcha befintliga kort. |

**Kanonisk nödknapp (definieras en gång, används i alla tre komponenter + hero + MainCTA + BlåCTA — direktiv 1):**
- Yta: `--eljour-emergency-green` solid. Vit text `#ffffff`.
- Innehåll (i denna ordning): verb-label **"Ring eljouren"** 17px/600 · mellanslag · numret **"010-265 79 79"** 17px/700 · flex-spacer · telefonglyf (outline, vit) höger i en subtil rund vit-alpha platta (12% vit).
- Höjd ≥ 56px. Full bredd i sin container. Radie `ap-radius-lg`.
- **Glow-prick:** liten teal (`--ampy-teal`) puls-prick centrerad under/på knappens nederkant — signalerar "liv/öppet". Behåll exakt som idag.
- Hela ytan är `<a href="tel:+46102657979">`. `aria-label="Ring Ampy eljour 010 265 79 79"`.
- States: rest (solid). Hover (desktop): ljushet +6%, glow-radie växer. Press: scale .98. Focus-visible: 2px teal outline + 2px offset.

---

## 1. Sticky mobile call-bar

Löser E-04 (ingen persistent ring-affordans) + direktiv 3. **Endast mobil/`<= 900px`.** Desktop har two-lane synligt hela heron — ingen sticky där (undvik dubbla fixerade element).

### Zoner & anatomi (mobil)
Ett enda fixerat fält, botten av viewporten, full bredd. Tre horisontella zoner i en flexrad:

```
┌──────────────────────────────────────────────┐  ← 64px hög, --eljour-emergency-green
│ [📞glyf]  Ring eljouren            ● öppen nu │
│           010-265 79 79                        │
└──────────────────────────────────────────────┘  + safe-area-inset-bottom (env)
```

| Zon | Element | Storlek/token |
|---|---|---|
| Vänster (fast) | Telefonglyf, vit outline, i 40px rund vit-alpha platta (12%) | ikon 22px |
| Mitten (flex-grow) | Rad 1: **"Ring eljouren"** 15px/600 vit. Rad 2: **"010-265 79 79"** 17px/700 vit. Radhöjd tight (1.15) | två rader vänsterställda |
| Höger (fast) | Live-mikrostatus: teal puls-prick 8px + **"öppen nu"** 12px/600 i teal-ljus (`#7fe3d0` mot mörkgrön, verifiera 4.5:1 — annars vit 12px) | vertikalt centrerad |

- **Bakgrund/kontrast:** `--eljour-emergency-green` solid. Sidans bakgrund är ljus (`#eef1fb`-ish) eller navy hero — mörkgrön baren separerar mot båda. Tunn topp-hairline: 1px vit-alpha 8% + drop-shadow uppåt `0 -4px 20px rgba(9,11,50,.18)` så den lyfter från innehållet.
- **Höjd:** 64px innehållshöjd + `padding-bottom: env(safe-area-inset-bottom)` (iOS home-indikator). Total tap-yta hela baren; effektiv tap-target ≥ 56px i tummens primärzon.
- **En handling.** Hela baren är `tel:`-länken. INGEN form-knapp i baren — det är exakt det som skiljer den från sticky-headerns "Gratis rådgivning"-pill (direktiv 4). Om två handlingar krävs: höger-zonens "öppen nu" förblir status, ej knapp.

### Appear-behavior (states)
1. **Dold** vid sidladdning (hero-nödknappen syns redan — ingen dubblering ovanför fold).
2. **Slide-in** (translateY 100%→0, 180ms ease-out) när hero-CTA:n scrollat ur bild (IntersectionObserver på hero-lane-1, eller scrollY > herohöjd). 
3. **Persistent** resten av sidan.
4. **Undvik krock:** när sidans egen bottenformulär-knapp ("Boka rådgivning") är i viewport → baren kan döljas (slide-out) så den inte ligger ovanpå submit-knappen; annars stannar den. Enkel regel om IO känns dyrt: dölj baren när `footer`/`.bottenformular` skär viewportens nedre 40%.
5. **En-fixerat-element-regel:** sticky-headern (topp) + call-baren (botten) får samsas, men ALDRIG två bottenfixerade lager. Om cookie-remnant/chatt-bubbla finns, call-baren vinner nederkanten.

### Candour-grind
- "öppen nu" endast om jouren FAKTISKT är dygnet-runt-bemannad (auditens reassurance-bullet "Jour dygnet runt, året om" är ägargodkänd → OK). Om jour har öppettider: byt till statisk "Dygnet runt" utan live-prick.
- Inget "svarar inom X sek" i baren om ej mätt.

---

## 2. Two-lane kontakt-block

Löser E-01/E-02/E-03/E-10 + direktiv 2 & 10. Detta är **kanon-mönstret för ALLA eljour-CTA-band** (hero, MainCTA, bottenband): Lane 1 = samtal (dominant), Lane 2 = formulär/återuppringning (subordinerad). Ersätter dagens inverterade viktning (grön gradient-formknapp stor, blek ice-blå ringknapp liten).

### Anatomi — mobil (390px), staplad
Ordning uppifrån (matchar 22:30-mentaliteten):

```
grön eyebrow   "Eljour i {ort}"
H1             "Akut elfel i {ort}? Ring så rycker vi ut."
live-pill      ● Jour öppen just nu          ← flyttad UPP hit (E-02: realtidsförsäkran = starkaste motivator)
── LANE 1 (dominant) ─────────────────
[ Ring eljouren  010-265 79 79   📞 ]        ← kanonisk nödknapp, full bredd, ≥56px
── reassurance-rad ───────────────────
🕐 Jour dygnet runt  ·  ⏱ på plats inom en timme
🛡 behörig elektriker, inte en växel  ·  🏷 tydligt pris, inga dolda avgifter
── LANE 2 (ghost) ────────────────────
Hellre bli uppringd?  Fyll i formuläret ↓    ← textlänk/outline, scrollar till formulär
```

- **Lane 1 (samtal):** kanonisk nödknapp (§0). Full bredd. Detta är blockets tyngdpunkt — störst yta, mörkgrön, högst kontrast.
- **Live-pill:** grön-ljus pill `● Jour öppen just nu`, prick teal-puls. Placeras OVANFÖR lane 1 (idag ligger den nere i symptomkortet). 13px/600, midnight-grön text.
- **Reassurance-rad:** de fyra befintliga bulletsen (candour-perfekta — auditen "rör inte texten"). Mobil: 2×2 grid eller staplad lista, ikon 18px teal + 14px text. Svarar visuellt "kommer någon nu?".
- **Lane 2 (formulär):** låg vikt. Ghost/text: `Hellre bli uppringd? Fyll i formuläret ↓`, teal understruken länk 15px, scrollar (`href="#offert-form"`) till formuläret längre ned. INGEN grön fylld knapp här (det stjäl från lane 1).
- **Formuläret** demoteras UNDER symptomtriagen (direktiv 2), inte ovanför den.

### Anatomi — desktop (1440px), tvåspalt
Behåll den befintliga balanserade tvåspalten MEN korrigera viktningen:

```
┌ vänster (58%) ──────────────┐  ┌ höger (42%) ───────────┐
│ eyebrow                      │  │  Formulärkort           │
│ H1                           │  │  "Hellre bli uppringd?" │  ← formuläret får finnas
│ live-pill ● öppen just nu    │  │  namn/tel/postnr/GDPR   │     men rubriken ramar in
│ [ Ring eljouren 010-… 📞 ]   │  │  [ Boka rådgivning ]    │     det som ANDRAHANDS-val
│  ← lane 1, dominant, ≥56px   │  │                         │
│ 🕐 ⏱ 🛡 🏷 reassurance 2×2   │  │                         │
└──────────────────────────────┘  └─────────────────────────┘
```

- Vänsterspalten bär samtalet (lane 1) + reassurance. Höger bär formuläret men under rubrik **"Hellre bli uppringd? Vi ringer upp dig."** — så formuläret framstår som alternativ, inte huvudväg.
- Formulär-submit byter copy till **"Boka rådgivning"** (behåll) men grön-gradienten nedtonas till teal-outline eller lugnare fyllning så den inte konkurrerar visuellt med lane 1:s mörkgröna. Nödknappen ska vinna första blicken (E-02).

### Mobil-ordning (kritisk, E-12)
1. eyebrow → 2. H1 → 3. live-pill → 4. **lane 1 (ring)** → 5. reassurance → 6. lane 2 (ghost form-länk) → 7. [symptomtriage, komponent 3] → 8. formulärkort. Samtal före formulär, alltid.

### Copy-mönster (svenska, ampy-röst — du-tilltal, ärlig)
- H1 geo: **"Akut elfel i {ort}? Ring så rycker vi ut."** (numret som `tel:` i lane 1, inte i H1 — H1 ska inte bära ett nummer som inte är klickbart).
- Lane 1 label: **"Ring eljouren  010-265 79 79"**.
- Lane 2: **"Hellre bli uppringd? Fyll i formuläret ↓"** / desktop-rubrik **"Hellre bli uppringd? Vi ringer upp dig."**
- Live-pill: **"● Jour öppen just nu"** (candour: endast om sant, se §1-grind).
- Reassurance (oförändrad): "Jour dygnet runt, året om." · "Målsättning att vara på plats inom en timme." · "Prata med en av våra behöriga elektriker, inte en växel." · "Tydligt pris innan vi rycker ut, inga dolda avgifter." — behåll ordagrant ("Målsättning"/"innan vi rycker ut" är candour-hedges, rör dem inte.)

### Candour-grind
- **Ta bort "5.0 på Google ★★★★★"-raden ur heron** (E-08/direktiv 8) → så nödknappen blir fokus (samma princip som homepage-MainCTA: ta bort 5.0-raden, CTA blir hela fokuset). Betyget behålls på EN plats nedströms (MainCTA), och endast om ägaren bekräftar 5,0 som aktuellt — annars stjärnor + "Betyg på Google" utan siffra.
- "på plats inom en timme" behåll **"Målsättning att…"** — aldrig som garanti.

---

## 3. Symptomblock-polish

Löser E-05/E-06/E-07/E-10 + direktiv 5–7. Bygger PÅ det som redan är bra (auditens "rör inte"): severity-färgkodning (röd Akut/amber Varning), den candour-kalibrerade nivåsättningen (Strömavbrott = Varning), desktop-tvåpanelen, reassurance-bullets. Polishen gör accordionen till **triage** i stället för FAQ.

### Vad som är bra idag och BEHÅLLS
- Rubrik "Är något fel med elen? **Tryck på det du upplever.**" (behåll).
- Reassurance-kortet med kanonisk nödknapp + glow-prick (sidans bästa element).
- Severity-pills (Akut röd / Varning amber) + färgprick per rad.
- "Se fler tecken (6) ▾" progressiv upplysning (behåll).
- 1800-bränder-statraden med "Källa: Elsäkerhetsverket" (behåll text — bara rama in, se nedan).
- Desktop-tvåpanel (reassurance-kort | accordion sida vid sida).

### Polish A — severity-sortera + gruppera (E-05)
Idag är ordningen osorterad (Varning, Varning, Varning, Akut, Varning, Akut, Akut) → panikanvändaren får ingen "börja här". Ny ordning:

```
🔴 Ring direkt         ← subrubrik, sev-akut röd, 13px/700 versal-lite
   ● Brännlukt eller rök            Akut  ⌄
   ● Surrar/knäpper i elcentralen   Akut  ⌄
   ● Laddboxen blir varm            Akut  ⌄
🟠 Boka snarast        ← subrubrik, sev-varning amber
   ● Säkring löser ut               Varning ⌄
   ● Strömavbrott                   Varning ⌄
   ● Jordfelsbrytare löser ut       Varning ⌄
   ● Flimrande ljus                 Varning ⌄
   ── Se fler tecken (6) ⌄
```

- Akut-gruppen först. Två tunna gruppsubrubriker med severity-färg. Detta ger den stressade en prioritetsledning utan att dramatisera (candour: Varning-gruppen heter "Boka snarast", inte "Fara").

### Polish B — höj tap-affordansen (E-05)
- Hela raden tryckbar (idag ser den ut som statisk FAQ-lista). Lägg synligt press/hover-state: rad-bg → ljus severity-tint 6% på hover/press.
- Chevron: större (från tunn 14px grå → 20px) och i **severity-färgen** (röd på Akut-rader, amber på Varning) i stället för neutral grå — så färgen driver ögat.
- Rad-höjd ≥ 56px (tumvänligt). Prick 10px vänster, label 16px/600 midnight, pill höger, chevron ytterst höger.
- `role="button"`, `aria-expanded`, tangentbords-toggle.

### Polish C — expanderad rad bär rätt nästa steg (E-06/direktiv 5)
Färgen ska driva LAYOUTEN, inte bara vara en tagg:
- **Expanderad Akut-rad:** kort förklaring (1–2 rader, candour) + **inbäddad kanonisk nödknapp** ("Det här kan vara farligt — ring nu · 010-265 79 79"). Ex. Brännlukt/rök-raden: expandera → visa 1800-bränder-statraden HÄR (kontextuellt exakt, E-10/direktiv 7) + nödknapp + en 112-först-hedge om akut fara ("Ser du lågor eller rök som sprider sig — ring 112 först.").
- **Expanderad Varning-rad:** kort förklaring + sekundär **"Boka en elektriker →"** (ghost/outline, scrollar till formuläret). Inte nödknappen — Varning ≠ ring-nu.

### Polish D — rama in 1800-statraden (E-10/direktiv 7)
Två alternativ (builder väljer ett):
1. **Flytta in** statraden i den expanderade "Brännlukt eller rök"-Akut-raden (rekommenderat — kontextuellt exakt).
2. Om den stannar under kortet: ge den ett tunt **vänster-border-kort**, 3px amber (`--sev-varning`) accent, ljus bg, 14px grå text, källhänvisning ordagrant. Aldrig röd/skrik — understated fear är candour-linjen.

### Polish E — ta bort "1000+ Nöjda kunder"-kortet (E-07/direktiv 6 — candour BLOCK)
- Det cyan "1000+ / Nöjda kunder"-kortet direkt efter symptomblocket är **bannad påstådd fakta** (ej ägar-bekräftat aktuellt) OCH fel innehåll på akut-yta.
- **Ersätt platsen** (mellan triage och MainCTA) med en snabbhets-/behörighetsrad — det en akut kund faktiskt vill verifiera:
  > **"Auktoriserad elfirma · Behöriga jourmontörer · Tydligt pris innan utryckning"**
  - Tre chip/pills i rad (desktop) / staplade (mobil), 14px, teal check-ikon, midnight text, ljus bg. Ingen siffra som inte är verifierad.
- Flytta 25+/20+-stat-trion till om-oss (E-11) — generiska planned-purchase-argument hör inte på akut-sida.

### Mobil stack-ordning i symptomblocket (E-12)
Idag: reassurance-paragraf + nödknapp ligger OVANPÅ den tappbara listan → löftet ("tryck") och objektet (listan) åtskilda av ett helt kort. Fix på mobil:
```
H2 "Är något fel med elen? Tryck på det du upplever."
[ severity-sorterad accordion — DIREKT under rubriken ]   ← objektet möter löftet
── (kollapsat, litet) reassurance-kort + nödknapp under listan
```
- Alternativt (om reassurance-kortet måste stå kvar överst): komprimera det till en rad + nödknapp, max ~180px höjd, så listan syns inom skärm 1. Behåll desktop-tvåpanelen orörd (den läser bra sida-vid-sida).

### Copy-mönster (svenska, ampy-röst)
- Gruppsubrubriker: **"Ring direkt"** (Akut) / **"Boka snarast"** (Varning).
- Akut-expansion CTA: **"Det här kan vara farligt — ring nu · 010-265 79 79"**.
- 112-hedge (endast Brännlukt/rök + ev. Surrar/knäpper): **"Ser du lågor eller rök som sprider sig — ring 112 först."**
- Varning-expansion CTA: **"Boka en elektriker →"**.
- Snabbhetsraden (ersätter 1000+): **"Auktoriserad elfirma · Behöriga jourmontörer · Tydligt pris innan utryckning"**.

### Candour-grind
- Ingen "1000+ kunder", ingen "5.0" som påstådd fakta.
- Severity-nivåer oförändrade (Strömavbrott = Varning, inte Akut — behåll den ärliga kalibreringen).
- 1800-statraden ordagrant med källa. Inga uppräknade skräckstatistik utöver den befintliga.
- "Målsättning att vara på plats inom en timme" — aldrig garanti.

---

## Reasoned against existing blocks (vad kitet ersätter/kompletterar)

| Kit-komponent | Ersätter / rör | Kompletterar / bevarar | Varför (fynd) |
|---|---|---|---|
| **Sticky call-bar** | NYTT lager. Konkurrerar EJ med sticky-header (topp) — den bär formulär-CTA "Gratis rådgivning", baren bär SAMTAL. | Sticky-headern behålls; på eljour-mallar bör dess pill dock bli dubbel (ring + form, direktiv 4). | E-04: ingen persistent ring-affordans idag; enda persistenta CTA leder till formulär. |
| **Two-lane kontakt** | Ersätter hero-knapparnas inverterade viktning (grön gradient-form stor + blek ice-blå ring liten). Ersätter MainCTA:s bleka ring-knapp + BlåCTA:s svarta med kanonisk nödknapp (direktiv 1/3/10). | Behåller formulärkortet (demoterat), reassurance-bullets, Edvin-fotot i MainCTA. | E-02/E-03: fyra visuella språk för samma samtalsknapp; svagaste vikten på viktigaste handlingen. |
| **Symptom-polish** | Omsorterar accordion (severity-grupperad), tar bort "1000+"-kortet, flyttar 25+/20+ till om-oss, ramar in 1800-raden. | Behåller nödknapp+glow, severity-färg, "Se fler tecken", desktop-tvåpanel, rubrik, reassurance-bullets, statkälla. | E-05/E-06/E-07/E-10/E-11/E-12. |

**Samverkan:** Two-lane definierar den kanoniska nödknappen → sticky call-baren och symptomblockets Akut-expansion återanvänder EXAKT samma knapp → ett enda samtalsspråk över hela ytan (direktiv 1). Sticky-baren och two-lane visar aldrig samtidigt samma sak dubbelt: baren är dold ovanför fold (hero-lane-1 syns), tänds först när heron scrollat ur bild.

## Vad som INTE ska röras (skydda)
- Den kanoniska mörkgröna nödknappen med glow-prick (sampla, pick inte om).
- Live-pillen "● Jour öppen just nu" (flytta upp, behåll design).
- De fyra reassurance-bullets (behåll text ordagrant).
- Severity-färgkodning + candour-kalibrering (Strömavbrott = Varning).
- Edvin-fotot i MainCTA.
- 1800-bränder-raden med "Källa: Elsäkerhetsverket" (behåll text; bara rama in/flytta).
- Desktop-tvåpanelen i symptomblocket.
- Pillars vita hero med skogsstuga-bild (awareness-ton).
