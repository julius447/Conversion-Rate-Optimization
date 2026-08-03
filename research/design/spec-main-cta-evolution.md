# MainCTA-evolutionen — den finaliserade ring-flaggskepps-specen

Detta är **produktions-specen** som ersätter "PhoneBand"-idén. Den bygger vidare på audit-filen
`research/design/call-cta-design.md` (fynd-ID:n CTA-01…CTA-08 återanvänds, upprepas inte). Målet, i ägarens
egna ord: *"Tar vi bort '5.0 på Google' blir CTA-knappen hela fokuset. DET är conversion rate optimization."*
Här är det utfört, element för element, byggbart i Bricks utan fler frågor.

Scope: **MainCTA** blir Ampys enda ring-flaggskepp (`main-cta-`, block-inventarium §5). **BlueCTA**
(`blue-cta-`, §7) och **MikroCTA** (`mikro_cta`, §6) får sitt slutgiltiga, designmotiverade öde nedan.

Tokens: alla värden är riktiga ap*-tokens från `.claude/skills/ampy-design-system/tokens.md`. Teal
`--apteal-core #00a991`, midnatt `--apmidnight-blue #090b32`, teal-bright `#1cc4af` (hover), grön
`#39c281`, off-white `#f5f9ff`, Outfit (Black `.apfont-900` / Medium 500 / Light 300). Inga em-streck i UI.

---

## Vad ögat möter (mobil) — nuläget som specen rättar

Källa: `svc-elcentral--mobile--08` (hela bandet i en tile), `pillar-elektriker--mobile--14/15`.
Uppifrån och ned i det vita kortet:

1. **Fullbredds teal-porträtt** av en leende blond kille i svart ampy-tröja, ~**55 %** av kortets höjd.
   Ett ansikte i den storleken är kortets absoluta blickmagnet (CTA-01).
2. **H2**, centrerad, två rader: "Prata med en elektriker" (midnatt) + "inom 60 sekunder!" (teal). Mår bra.
3. **Paragraf**, 4 rader, mellangrå, centrerad ("Känn dig trygg med kunnig hjälp … guidar dig till en
   säker, smidig lösning.").
4. **Ring-knapp**, helbredd: **cyan/teal-gradient pill, mörk marinblå text**, vit rund telefon-chip **höger**,
   mjuk glow. Detta är exakt samma pill som navknapparna "Till Belysning" / "Till Smarta hem" / "Läs mer"
   som ligger överallt (`svc-elcentral--desktop--10`, `pillar--mobile--15`) — **färgtvilling, låg salience**
   (CTA-03).
5. **"G 5,0 på Google ★★★★★"** (guldstjärnor), centrerad — **sista blickvilan**, glimmar, stjäl fokus
   (CTA-02) och är en oankrad candour-liability (inget recensionsantal).

Blickordning idag: **ansikte → rubrik → paragraf → (scrolla) → svag knapp → guldstjärnor**. Knappen ligger
~1,3 skärmhöjder ned, inklämd mellan två fokustjuvar (CTA-04). Den viktigaste ring-knappen på sajten ser ut
som en låg-intents navlänk.

## Vad ögat möter (desktop) — nuläget

MainCTA desktop = textstack vänster, teamfoto med våg-overlay höger (~40–45 %). Sida-vid-sida gör fotot
mindre kväljande än mobilens topp-placering, men samma två kärnfel kvarstår: cyan-gradientknappen =
färgtvilling med nav, och 5,0-raden hänger kvar. På `pillar-elektriker` renderas dessutom **både** MainCTA
och BlueCTA (`--desktop--10`, svart pill mot cyan) → **två ringband på samma sida**, rå upprepning (CTA-05).

BlueCTA:s svarta pill mot cyan är samtidigt **sajtens högsta knappkontrast** — beviset att systemet redan
äger en primär-knapp-look. Den looken ska koloniseras in i MainCTA.

---

## Fynd (finaliserade — hänvisar till call-cta-design.md)

| ID | Slutdom |
|----|---------|
| CTA-01 | Fotot krymps från dominant (~55 %) → **stödelement**. Ansikte kvar (värme + E-E-A-T) men får aldrig äga kortet. |
| CTA-02 | **5,0-guldraden BORT ur MainCTA.** Dubbelvinst: knappen blir terminal blickvila + oankrad candour-risk försvinner. |
| CTA-03 | Knappen **omfärgas cyan-gradient → solid midnatt `#090b32`** (BlueCTA:s bevisade look), chip flyttas höger→**vänster**. Slutar vara navtvilling. |
| CTA-04 | Efter 01+02 åker knappen upp ~1 skärm → in i första tumzonen. |
| CTA-05 | På sidor med MainCTA v2 **droppas BlueCTA** (samma phone-ask). |
| CTA-06 | **MikroCTA retireras** (dess dubbel-ask duplicerar Hero_2). |
| CTA-07 | Knapptext-alternativ "Ring en elektriker" A/B-testas; numret behålls som canonical (destination + trust). |
| CTA-08 | Cross-note: i kvarvarande dubbel-ask-band (Hero_2/footer-seo) demoteras Ring till ghost/outline så en väg är primär. |

---

## Den förädlade MainCTA — full byggspec

### Canonical-beslut (en byggbar sanning)
- **Mobil = Riktning A** (inset-porträtt över rubrik). **Desktop = Riktning C** (split: text vänster / foto höger).
- **Knapp = solid midnatt `#090b32`**, vit text, **teal `#00a991` telefon-chip vänster**. Motiv: på det vita
  kortet ger midnatt högst luminanskontrast, ekar BlueCTA:s bevisade primär-look, och håller teal som accent
  (chippen) i stället för att bränna teal på hela ytan. Teal-fylld pill = dokumenterat färg-alternativ (Riktning-not).
- **5,0-raden finns inte.** Knappen ÄR sista elementet.

### Zoner & elementlista — MOBIL (390px, kort = `--apradius-l` 16–20px, vitt, padding `--apspace-xl` 24–32px)

| # | Zon | Element | Token / storlek | Not |
|---|-----|---------|-----------------|-----|
| 1 | Topp, centrerad | **Inset-porträtt** (namngiven elektriker, E-E-A-T — t.ex. Edvin) | rund **104 px**, 2px `#ffffff`-ring + mjuk skugga; teal-tonad bakgrundsplatta bakom | **Stöd, ej dominant.** Ersätter fullbreddsfotot (CTA-01). |
| 2 | Rubrikzon | **H2** "Prata med en elektriker **inom 60 sekunder**" | Outfit **500**, `--aptext-2xl`, lh 1.2, centrerad. "Prata med en elektriker" = `#090b32`; "inom 60 sekunder" = `#00a991` | "!" valfritt (metered). "60 sekunder" = **[GAP]-gated**, se candour. |
| 3 | Brödtext | **Paragraf 2–3 rader** | Outfit **300**, `--aptext-m`, färg `#4a4d68`, centrerad, max ~34ch | Kortad från 4 → 3 rader: *"Känn dig trygg med kunnig hjälp, precis när du behöver den. Prata direkt med en erfaren elektriker som guidar dig rätt."* |
| 4 | CTA (terminal) | **Ring-knapp** `<a href="tel:+46102657979">` | helbredd 100 % (max 420px), höjd **64px**, `--apradius-full`; fyll `#090b32`; text "Ring 010-265 79 79" Outfit **500** `--aptext-l` `#ffffff`; **teal chip 44px vänster**, vit telefon-ikon; skugga sm | **Enda knappen. Sajtens hetaste element i bandet.** |

**Borttaget:** fullbreddsfoto (→ inset), 5,0-guldrad. **Fokusflöde efter:** porträtt (litet) → rubrik →
(kort) paragraf → **KNAPP (terminal, hetast)**. Exakt "CTA-knappen blir hela fokuset."

### Zoner & elementlista — DESKTOP (kort centrerat, max ~1120px, 2-kol)

| Kol | Bredd | Innehåll |
|-----|-------|----------|
| **Vänster** | ~62 % | H2 (vänsterställd, samma färgdelning), paragraf 2–3 rader, **Ring-knapp auto-bredd** (min 320px, ej helbredd), chip vänster, `#090b32`. |
| **Höger** | ~38 % (cap) | **Porträtt/teamfoto** med befintlig våg-overlay, **höjd cap ~360px**, `--apradius-l`. Kontrollerad — får ej dominera textkolumnen. |

Ingen 5,0-rad. Knappen är kolumnens och kortets tyngdpunkt.

### States (gäller båda breakpoints)
- **Default:** `#090b32`, skugga sm, chip `#00a991`.
- **Hover:** fyll → `#0d1247`; chip → teal-bright `#1cc4af`; `translateY(-2px)`; mjuk teal glow-ring.
- **Active:** `translateY(0)`, tightare skugga.
- **Focus-visible (a11y):** 3px `#00a991` outline, offset 2px.
- **Chip-puls:** valfri, EN diskret puls; av vid `prefers-reduced-motion`.
- Endast knappen är länk (`tel:`), inte hela kortet. Riktig `<a>` för tap-to-call.

### Copy-mönster (svenska, ampy-röst — du-tilltal, ärligt, ej superlativ-fluff)
- **Rubrik canonical:** "Prata med en elektriker **inom 60 sekunder**" (behåll teal-pop på tidslöftet).
- **Rubrik-fallback (om 60-sek ej ägarbekräftad):** "Prata direkt med en elektriker" (inget tidsanspråk).
- **Knapp canonical:** "Ring 010-265 79 79". **A/B-alternativ (CTA-07):** "Ring en elektriker".
- **Paragraf:** behåll rösten och tryggheten, korta bara längden. Byt aldrig register.

### Candour-gates (blockerande)
1. **"5,0 på Google ★★★★★" — struken ur MainCTA.** Oankrad (inget recensionsantal) = bannad om ej
   ägarbekräftad aktuell. Ankrat proof ("5 av 5 · Betyg på Google" + riktiga recensioner) bor redan i
   testimonials + main-contact — MainCTA behöver det inte.
2. **"inom 60 sekunder" = [GAP].** Får bara stå om ägaren bekräftar att det är en verklig, typisk svarstid
   (SLA). Obekräftat → använd fallback-rubriken. Hitta aldrig på en svarstid vi inte kan stå för.
3. **Numret "010-265 79 79" = [FACT]** — ok.
4. Ingen urgency/scarcity/countdown tillkommer. Värme grundad i sanning, inte press.

---

## Divergenta riktningar (husregel: 3 versioner — bygg alla för pixel-QA)

**A — "Ansiktet krymper, knappen vinner" (CANONICAL mobil, lägst risk).**
Inset-porträtt 104px över rubriken, 5,0-raden borta, midnatt-knapp. Värmen kvar via ansiktet i litet format;
knappen blir terminal. Pixel-nära dagens block → snabbast till Bricks.

**B — "Ren typografisk ring-inbjudan" (prestanda-fallback, inget foto).**
Stryk porträttet helt: teal telefon-glyf (32px) → H2 → 2 rader → stor midnatt-knapp. Renast fokus, snabbast
tumzon, **lättast LCP** — relevant givet ~9–10 s lab-LCP-flaggen. Tappar mänsklig värme; kör om A känns tung
eller om sidan redan bär mycket bild.

**C — "Split: ansikte vänster, ask höger" (CANONICAL desktop).**
Foto vänster/höger ~38 %, text + midnatt-knapp i textkolumnen, ingen 5,0. Trygg mellanform mellan "kallt
formblock" och "varmt ringband". Bäst där MainCTA ersätter både sig själv OCH en droppad BlueCTA.

**Tre invarianter i alla tre:** (1) ingen 5,0-rad, (2) solid högkontrast-knapp (`#090b32`) ≠ navfärg,
(3) EN enda ask (phone-only). Dokumenterat färg-alt: teal-fylld `#00a991` pill med vit text i stället för midnatt.

---

## BlueCTA & MikroCTA — slutgiltigt öde (designmotiverat)

### BlueCTA (`blue-cta-`) → **BEHÅLL MED ÄNDRINGAR, omprofilerad**
- **Roll:** den *lätta, ansiktslösa* phone-strippen för sidor som INTE bär MainCTA v2. Dess svarta-pill-mot-cyan
  är sajtens bevisade primär-look och är **DNA-källan** till MainCTA v2:s knapp — så inget värde tappas när
  den dras från MainCTA-sidor.
- **Regel:** BlueCTA och MainCTA v2 får **aldrig** ligga på samma sida (CTA-05). Där båda skulle rendera
  (t.ex. `pillar-elektriker`) → **droppa BlueCTA**.
- **Liten ändring:** justera pill från ren svart → `--apmidnight-blue #090b32` så knapparna delar exakt token
  över hela sajten (system-konsistens). Chip vänster, som idag.

### MikroCTA (`mikro_cta`) → **RETIRERA (kill)**
- Dess dubbel-ask (Kostnadsfri rådgivning + Ring) på fotobakgrund **duplicerar Hero_2:s dubbel-ask** utan
  nytt visuellt jobb; två knappar delar vikt → ingen vinner (CTA-06), och den gröna formvägen slår ihjäl
  ring-vägen (CTA-08).
- Behövs ett **bild-backat** ringband någonstans → det jobbet gör nu **MainCTA v2** (ett ansikte, en knapp).
  MikroCTA fyller ingen lucka som inte redan är täckt. Avveckla.

---

## Per-template-placering (byggmatris)

| Template | Ring-flaggskepp | BlueCTA | MikroCTA | Formkraft | Not |
|----------|-----------------|---------|----------|-----------|-----|
| **Home** | — | ✅ mid-page (lätt strip) | ✗ | Hero-1 + main-contact botten | Undvik stackning; home är redan CTA-tät. |
| **Service (svc-*)** | ✅ MainCTA v2, mid/låg | ✗ drop | ✗ kill | Hero_2 topp + main-contact botten | Ring-flaggskeppet mellan SEO-innehåll och formavslut. |
| **Geo (elektriker-i-*)** | ✅ MainCTA v2, mid | ✗ drop | ✗ kill | Hero_2 + main-contact | Kommersiell publik → behåll formvägarna, MainCTA = call-alternativet. |
| **Pillar (elektriker)** | ✅ MainCTA v2 (EN gång) | ✗ drop (fixar dubbletten) | ✗ | main-contact botten | Idag: MainCTA m14 + BlueCTA d10 → nu bara MainCTA v2. |
| **Produkt (EV/batteri)** | ✅ MainCTA v2, låg | ✗ | ✗ | expert-CTA-kort + popup + main-contact | En ring-yta räcker; MainCTA v2 sist före certifikat/footer. |
| **Artikel** | — | ✅ smal strip mid/slut | ✗ | review-CTA + main-contact | Ingen plats för stort ansiktskort mitt i brödtext → BlueCTA. |
| **Om oss** | — | (visual-cta finns) | ✗ | main-contact | Utanför scope; ingen ändring. |

---

## Reasoned against existing blocks (obligatoriskt)

- **vs Hero_2 (§1):** Hero_2 = form-först, dubbel CTA, sidtopp, kommersiell. MainCTA v2 = phone-only, varm,
  mid/låg, för besökaren som ännu inte vill fylla formulär. **Distinkt jobb.** Lägg ALDRIG en grön
  "Kostnadsfri rådgivning"-knapp i MainCTA — det återinför grön/cyan-tvillingen (CTA-08) och dödar ring-fokuset.
- **vs main-contact (§4):** main-contact = form-motorn + ankrat proof + 3 steg, sidbotten. MainCTA v2 = den
  lättare, mänskliga, ring-nu-vägen tidigare i scrollen. **Komplementära** (call-väg vs form-väg), ej dubblett.
- **vs BlueCTA (§7):** samma ask (phone), men BlueCTA = lättare typografisk strip utan ansikte. MainCTA v2
  **ersätter** den där båda skulle möts; BlueCTA överlever bara på ansiktslösa sidor och **ärver ut** sin pill
  till MainCTA v2.
- **vs MikroCTA (§6):** dubbel-ask på fotobg = redundant med Hero_2 → **killad**. MainCTA v2 är det
  enda-ask bild-backade bandet som tar över rollen.
- **vs footer-seo (§16):** behåller sitt CTA-par men (cross-note CTA-08) **demotera Ring till ghost/outline**
  så en väg är primär — MainCTA v2 äger "ring"-identiteten högre upp; footer-seo ska inte re-slåss om den.
- **vs navknapparna ("Läs mer"/"Till X"):** det var precis dessa cyan-pillar MainCTA:s knapp var tvilling med.
  Midnatt-omfärgningen (CTA-03) **bryter tvillingskapet** — ring-knappen läser nu som primär, navknapparna
  förblir sekundära. Detta är hela poängen med omfärgningen.

---

## Vad som INTE ska röras
- **Rubriken "Prata med en elektriker inom 60 sekunder"** (villkorat 60-sek-[GAP]) — nyttolöfte + tidsangivelse
  + teal-pop. Rör inte copy eller tealen.
- **Paragrafens ton** — lugn, du-tilltal, trygghetsförankrad. Korta bara längden, byt inte rösten.
- **BlueCTA:s högkontrast-pill-koncept** — det är mönstret som koloniseras in i MainCTA; behåll det.
- **main-contact-blocket** — starkaste konverteringsytan; dess ankrade proof + 3-steg + form rörs inte.
- **Att MainCTA är phone-only** — det ÄR dess distinkta jobb. Ingen form-CTA får smyga in.
- **Att MainCTA bär ett mänskligt ansikte** (i litet format) — värmen är rätt för publiken 35–65; bara
  storleken ändras, inte närvaron (utom i Riktning B).
