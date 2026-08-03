# Startsidan — designaudit (hela flödet, runt den låsta heron)

Scope: hela homepage-flödet som DESIGN, pixel för pixel, mobil (780px-tiles, DSF2) + desktop (1440px). Heron är ägar-låst → jag reviderar runt den. Round-1-struktur (HP-01…HP-13 i `templates/homepage.md`, ServiceRouter i `missing/block-service-router.md`) är kontext, upprepas ej — det här lägret är designfinessen: vad som stjäl fokus, vad som förtjänar sina pixlar, element för element.

Tiles lästa: mobil 01–27 (två capture-pass av samma sida — pass 1 = 01–11 med **tomma produktbilder** = lazy-load ej triggad, pass 2 = 12–27 med bilder laddade), desktop 01–12 (hela flödet syns). Kända sekvensen: Header → Hero-1(låst) → **MiniMenu** → ProductGrid(batterier) → **BlueCTA** → ProductGrid(laddboxar) → Testimonials → **ServiceGrid** → **MainCTA** → VarProcess → MainContact → **MapBlock** → **News** → Prefooter/Footer.

---

## Vad ögat möter (mobil)

- **Skärm 1 (hero, låst):** vit ampy-logga, grön "Gratis rådgivning"-pill med lysande grön prick, hamburgare. Dusk-foto av trähus. Vit H1 "Elinstallationer i hemmet, gjort ordentligt." → grå-vit paragraf → grön-gradient "Kostnadsfri rådgivning ↗". Lugnt, en handling. Bra.
- **Skärm 2 (MiniMenu, del 1):** navy proof-list "5,0 på Google ★★★★★ / Över 3 000 installationer per år" → navy H2 "Din elektriker för hela hemmet" centrerad → grå paragraf → **första fotokortet: mörkt dusk-foto, vit centrerad etikett "Elservice", teal "Läs mer →"-pill under etiketten**. Samma blå-dusk-palett som heron — känns som *mer hero*, inte en ny sektion.
- **Skärm 3–4 (MiniMenu forts.):** kortet "Laddbox" och "Batterilagring" är i pass 1 **helt tomma mörknavyrutor** med bara ett ord + en teal pill svävande i mitten. Noll scent om vad som finns bakom. Tre nästan-fullskärmshöga rutor.
- **Skärm 4–11 (ProductGrid):** rubrik "Våra hembatterier och laddboxar – installerat & klart med **50 %** Grön Teknik-avdrag" → ström av produktkort. Varje kort ≈ en hel viewport: badge (BÄSTSÄLJARE navy / SUPERKAMPANJ grön / NYHET teal) uppe till höger → **stor tom vit bildyta** (pass 1) → 2-cells specrad (batteri-ikon "3-fas" | blixt "15.36–61.44 kWh") → namn (Dyness Stack100 Pro) → 3–4 raders beskrivning → hårlinje → **"Fr. 34 900 kr" centrerad, stor fet** → **jättelik ljust-cyan "Läs mer"-knapp, full bredd, ~64px hög**. Det första priset ögat möter på hela sidan är **34 900 kr**.
- Mitt i gridden (efter batterierna): **BlueCTA** — cyan-gradient-kort, "Prata med en **elektriker!**" (ordet + utropstecknet **understruket**), grå paragraf, svart "Ring 010-265 79 79"-knapp med vit telefon-chip. Sedan fyra laddbox-kort med samma grammatik (Fr. 4 490 kr, ljust-cyan Läs mer).
- Mobil-capturen når aldrig förbi produktgridden (pass 2 börjar om på heron) — men desktop visar resten.

## Vad ögat möter (desktop)

- **Hero (låst):** OBS annan copy än mobil — H1 "**Framtidens elinstallationer för ditt hem!**" + "Vi är Sveriges modernaste elfirma…". Trust-rad nere till höger. (Mobil säger "Elinstallationer i hemmet, gjort ordentligt.") Copy-mismatch mobil/desktop — flaggas, men heron är låst.
- **MiniMenu:** tre *lika stora* dusk-foton (hus / bil+laddbox mot träpanel / hus med gräsmatta) med vit centrerad etikett + teal "Läs mer →" mitt i kortet. Läses som ett **fotogalleri/affischtrio**, inte en tjänstemeny.
- **ProductGrid:** 4 batterikort i rad (bilderna syns nu) → **BlueCTA som full-bredds cyan-band** (text vänster, svart Ring-knapp höger) → 4 laddboxkort. Ljust-cyan "Läs mer"-knappen är det ljusaste, största elementet i varje kort; priset är den tyngsta texten.
- **Testimonials:** navy-gradient-kort i Splide, äkta namn + månad (Daniel Hellström, Josephine Lundqvist…), mint-stjärnor, "5 av 5 · Betyg på Google". Stark. (V1 låst per minne.)
- **ServiceGrid:** rubrik "Vårt utbud av elinstallationer – installerat & klart **med 30 %** ROT-avdrag" → 6 kort med **riktiga funktionsfoton** (taklampa, öppen elcentral, kök, luftvärmepump, hus, spotlights) + **beskrivande etikett + "Till Belysning ↗"**. Detta är den *bättre routern* — och den ligger på plats 8.
- **MainCTA:** vitt kort, H2 "Prata med en elektriker **inom 60 sekunder!**" (teal) → paragraf → ljust-cyan "Ring 010-265 79 79"-knapp → **under den: "G 5,0 på Google ★★★★★" guld-rad**. Höger: Edvin på teal-panel. Detta är blocket ägardoktrinen pekar på.
- **VarProcess** "Så funkar det" — 4 rena linje-ikon-steg. Bra.
- **MainContact** — navy fotopanel vänster (citat, 5 av 5, "3 000+ genomförda") / formulär höger (Förnamn/Efternamn/E-post/Telefon/Adress/Meddelande, teal "Gratis rådgivning ↗"). Starkast.
- **MapBlock** — cyan-band, **20 vita likadana ort-pillar i 4×5-rutnät** (alla Stockholm) + navy "Osäker ifall vi finns där du bor? Kontakta oss ↗" + **abstrakt hexagon-klunga** till höger (läses INTE som Sverige).
- **News** "Nyheter och artiklar!" — 3 kort, **alla tre nästan identiska elcentral-foton, alla daterade "juni 14, 2026"**, navy-outline "Läs artikel".
- **Prefooter** cyan "Populära kategorier" (5 kolumner) → **navy footer** (5.0-stjärnor, adress, bokning@ampy.se).

---

## Fynd

**HD-01 · MiniMenu läses som dekoration, inte "välj din tjänst".** Tre orsaker, alla visuella: (a) *lika-tredjedels-billing* ger Elservice (prio #1) exakt samma vikt som två produktkategorier — priordoktrinen syns inte; (b) fotona är stämnings-dusk-landskap (hus i skymning) — atmosfär, inte funktion; en villaägare kan inte utläsa vad "Elservice" täcker ur ett skymningsfoto; (c) centrerad etikett + generisk "Läs mer" = affisch, inte router. Ingen ikon, ingen underetikett, noll scent. Bevis: sidan innehåller redan den bättre routern (ServiceGrid, plats 8) med funktionsfoto + beskrivande etikett — MiniMenu är den sämre kopian ovanför. Mobil pass 1: tre **tomma navyrutor** med ett ord = maximal dekoration, noll scent på första scroll. (Kontext HP-13.)

**HD-02 · "Läs mer"-knappen är kortets tyngsta element men lägst värde.** I varje produktkort (mobil + desktop) är den ljust-cyana "Läs mer"-pillen störst och ljusast — men handlingen är att *lämna startsidan* till en produktsida (noll konvertering). Den slår ut både namn och pris i hierarki. Åtta sådana knappar = ett hav av ljust-cyan nedför hela gridden. Fel element vinner ögat. (Kontext HP-02: 8 utgångar före all proof.)

**HD-03 · Priset är typograferat som rubrik → förstärker det fientliga ankaret.** "Fr. 34 900 kr" står ensamt på egen rad, centrerat, ~28px fet, med stor luft runt — visuellt en headline. Det gör att **34 900–36 250 kr blir det första och starkast satta prissignalen** på sidan, för en besökare vars jobb kostar ~3 500 kr. Designen *förstärker* HP-01-ankaret istället för att dämpa det.

**HD-04 · Specchips (3-fas, kWh) är ingenjörsspråk för fel publik.** "3-fas" / "15.36–61.44 kWh" i chip-raden säger ingenting till en 35–65 husägare som ska ha en taklampa — det är auktoritets-cosplay som bara adderar brus och förstärker "det här är en butik för solcellsfolk, inte min elektriker".

**HD-05 · Badge-färgerna är osammanhängande och den skrikigaste färgen säljer lägst prio.** BÄSTSÄLJARE = navy pill, SUPERKAMPANJ = **klart grön** pill, NYHET = teal-gradient pill. Tre färger, tre emfaser, tävlar överst i varje kort. Den gröna SUPERKAMPANJ är sidans lystaste färgruta — och den sitter på **batterier** (prio #3). (Candour: SUPERKAMPANJ/BÄSTSÄLJARE saknar substantiering, ⚑.)

**HD-06 · Tom produktbild på first paint = trasigt intryck ×8.** Mobil pass 1 (tiles 4–8, 16) renderar korten som **höga vita rutor med bara en svävande badge + pris** — bilden lazy-laddar. På en sida med ~9–10s lab-LCP betyder det att gridden målas som 8 tomma boxar. Ser oklart/ofärdigt ut i prime-thumb-zonen. (Kontext HP-12.)

**HD-07 · BlueCTA: understruket "elektriker!" = falsk länk-affordans.** Understrykningen (~2px linje under ordet + utropstecknet) läses som en hyperlänk — men inget där är klickbart; den riktiga länken är den separata svarta Ring-knappen. En besökare kan trycka på ordet och inget händer. Understrykning-som-emfas är dessutom ett daterat ordbehandlar-grepp; systemet använder vikt/gradient för emfas, inte understrykning. Den svarta Ring-knappen däremot är blockets starkaste element och är korrekt.

**HD-08 · Två Ring-knappar, två olika behandlingar.** BlueCTA:s Ring-knapp är **svart, hög kontrast** (stark). MainCTA:s Ring-knapp är **ljust-cyan gradient** (svag). Samma primära handling (ring) ser olika ut på samma sida → den viktigaste call-affordansen har ingen kanonisk form. Den svarta är den starkare.

**HD-09 · MainCTA: 5.0-raden stjäl fokus från Ring-knappen (ägardoktrinens frö).** Under Ring-knappen sitter "G 5,0 på Google ★★★★★" i guld — direkt konkurrent om ögat, precis under den enda handlingen. Tar man bort den blir Ring-knappen hela fokuset. Dessutom teal-highlightar rubriken "**inom 60 sekunder!**" — den mest osäkra claimen (SLA?) får mest visuell emfas (HP-08). Ge inte ett overifierat tal spotlight.

**HD-10 · Teal är tapet, inte accent.** Teal/cyan förekommer på: hero-CTA (grön-teal-gradient), MiniMenu-pillar (teal), produkt-"Läs mer" (ljust-cyan), BlueCTA-band (cyan), ServiceGrid-pillar (cyan), MainCTA-fotopanel (teal), contact-knapp (teal), MapBlock-band (cyan), prefooter (cyan). Spritt över minst tre nyanser (grön-teal / ren teal / ljust-cyan) i **stora ytor**. Token-guardrailen (teal ensam som accent) bryts — när allt är teal är inget teal. Den primära handlingen har ingen färgmässig ensamrätt.

**HD-11 · Färgrytmen har inga semantiska förankringar.** Sektionsbakgrunder: hero(mörk) → offwhite → offwhite → **cyan(BlueCTA)** → offwhite → offwhite → offwhite → offwhite → vit → vit → **cyan(MapBlock)** → vit → **cyan(prefooter)** → navy(footer). Cyan-banden (3 st) och navy-momenten (testimonialkort, contact-panel, map-subkort, footer) dyker upp utan logik — "här är ett färgat band". Lugnt för publiken (bra), men monotont-med-slumpvis-cyan. Cyan borde reserveras för EN betydelse (t.ex. "prata med oss"-moment), inte strös ut.

**HD-12 · MapBlock: 20 identiska pillar + hex-blob = brus, och metaforen faller.** 20 vita likadana ort-pillar (4×5) ger ögat ingenstans att landa och är 20 lågvärdes-interna länkar på en icke-geo-startsida. "Sverige-kartan" är en abstrakt navy-hexagon-klunga som **inte** läses som Sverige — ren dekoration. Copyn säger "hela Sverige" medan varje pill är Stockholm (HP-09) → det visuella underminerar claimen dubbelt. Navy "Kontakta oss"-subkortet är det enda som fungerar.

**HD-13 · News: dubblerade foton + dubblerat datum = ser ofärdigt ut.** Kort 1 och 3 är **samma elcentral-foto**, kort 2 nästan samma, alla tre daterade "juni 14, 2026". För en 35–65-publik är slarv en workmanship-proxy (samma logik som typo-fyndet HP-06) — upprepningen läses som platshållare/auto-genererat och skadar färskhets-signalen blocket finns till för.

**HD-14 · MiniMenu upprepar heron visuellt.** Sidans två första skärmar är samma blå-dusk-fotopalett (hero-dusk-hus → tre dusk-fotokort). MiniMenu känns inte som en ny sektion utan som en förlängning av heron → ingen "nu byter vi från löfte till meny"-signal. Det som sitter under den låsta heron måste vara tydligt underordnat OCH tydligt en ny sektion — inte ett tredje skymningsfoto.

---

## Omdesign-direktiv (numrerade, konkreta)

1. **Döda den dekorativa MiniMenu:n; promotera ServiceGrid-grammatiken uppåt till ServiceRouter (plats 3).** Behåll ROT-hook-rubriken. Använd ServiceGrids befintliga mönster — **funktionsfoto av den faktiska saken + beskrivande etikett + "Till {tjänst} ↗"** — inte dusk-landskap + "Läs mer". (Se ServiceRouter-vikt nedan + divergenta riktningar.)
2. **Demota produkt-"Läs mer"-knappen.** Ersätt den jättelika ljust-cyana pillen med en **låg-emfas textlänk/ghost-knapp** ("Se {produkt} →"), så priset och namnet får vinna kortet — och så att teal återvinns till den enda primära handlingen. Gäller om ProductGrid över huvud taget behålls på startsidan (round-1 ersätter den med kompakt ProduktTeaser, plats 7).
3. **Avrubrificera priset.** "Fr. 34 900 kr" ska INTE vara kortets tyngsta typografi. Mindre grad, vänsterställ, para ihop med "efter avdrag"-caveat på samma rad. I ProduktTeaser: pris som bildtext, inte headline. (Dämpar HD-03/HP-01-ankaret.)
4. **Ta bort specchips (3-fas/kWh) från startsidans kort.** De hör hemma på produktsidan. Ersätt med en mänsklig one-liner om det behövs ("Passar villa & radhus").
5. **En badge-standard eller inga badges.** Om badges behålls: EN form, EN dämpad färg (navy outline), och aldrig den skrikgröna på lägst-prio-produkt. Helst: ta bort SUPERKAMPANJ/BÄSTSÄLJARE på startsidan (candour ⚑).
6. **Kanonisk Ring-knapp = den svarta hög-kontrast-varianten.** Byt MainCTA:s ljust-cyana Ring-knapp till samma svarta behandling som BlueCTA. Samma primära handling ska se likadan ut överallt (HD-08).
7. **BlueCTA: ta bort understrykningen** under "elektriker!". Använd vikt eller teal-ord för emfas — aldrig understrykning (falsk länk). Behåll den svarta Ring-knappen exakt.
8. **MainCTA: ta bort "5,0 på Google"-raden under Ring-knappen** → knappen blir hela fokuset (ägardoktrinen, HD-09). De-emfasera "inom 60 sekunder" tills SLA:t är ägar-verifierat (HP-08).
9. **Reservera teal för EN sak: primär handling.** Alla dekorativa teal-ytor (produktknappar, MiniMenu-pillar) ned till neutral/navy. Cyan-banden får EN betydelse — gör dem till "prata med oss"-moment, inte slumpvisa avdelare (HD-10/HD-11).
10. **MapBlock: skär pillarna till 6–8 + "fler orter i hela Sverige →", byt hex-blobben** mot en dämpad äkta Sverige-silhuett med prickar (eller släpp grafiken helt). Behåll navy Kontakta-oss-subkortet. Vid post-form-slot ska blocket vara **tyst**, inte ett skrikigt cyan-brus. (Löser HD-12 + HP-09 visuellt.)
11. **News: unika foton + unika datum** per kort, annars läses blocket som platshållare (HD-13). Designen i övrigt (outline-knapp, låg plats) är korrekt — rör inte den.
12. **Lös lazy-load-tomheten (HD-06):** LQIP/skeleton eller eager-load de första kort som ligger i/nära första scroll, så inget renderar som en tom vit ruta på en 9–10s-LCP-sida.

---

## Divergenta riktningar — ServiceRouter (den stora interventionen)

**Vad måste visuellt ändras när ServiceRouter ersätter ProductGrid, och vilken vikt ska den ha mot den låsta heron:**

Heron är sidans tyngsta element (full-bleed dusk-foto, ~48px vit H1, EN teal-gradient-CTA). ServiceRouter är den nya primära beslutsytan på plats 3. Krav på dess vikt:
- **Näst tyngst — men aldrig en andra hero.** Ingen full-bleed-fotografi som rivaliserar heron. Lägg routern på **offwhite (#f5f9ff)** = en palett-reset som signalerar "nu går vi från känsla till funktionell meny" (löser HD-14; ingen tredje dusk-bild).
- **Typografiskt underordnad:** ROT-hook-rubriken behålls men på H2-skala (~32px), navy på ljust — tydligt under hero-H1.
- **Prio syns på en blick:** tjänsterna (rad 1, prio #1) får full billing; Laddbox+Batterilagring (rad 2) är **slimmade, halvhöga, 2-up, synligt underordnade** — inte lika-tredjedels med tjänsterna (dagens MiniMenu-fel).
- **En accentfärg:** kortlänkarna använder SAMMA teal som hero-CTA, men litet — inget andra hav av ljust-cyan.
- Netto: hero = emotionell full-bleed-tungviktare; ServiceRouter = den funktionella, ljusare, strukturerade menyn direkt under, andra i hierarkin, omisskännligt en *router* för att varje kort svarar "vad behöver du?" med en bild av den faktiska saken + en klar-svensk etikett. Den ska kännas som heronns praktiska svar — inte ett galleri.

**Riktning A — "Ikon-router" (lugnast, snabbast, mest läsbar för 35–65).** Rad 1: 6 flata kort på vitt, EN linje-ikon per tjänst (lampa / elcentral / laddkontakt / kök / förstoringsglas för felsökning+eljour / +), fet navy-etikett, one-line scent-underetikett ("Elcentral — byte & uppgradering"), teal chevron. Rad 2: 2 slimmade kategori-remsor. Snabbast att måla (SVG, noll bildvikt = direkt HP-12-speed-vinst), maximal läsbarhet, noll webshop-känsla. Risk: mindre varm/visuell.

**Riktning B — "Foto-router" (återbruk av sidans egen vinnande pattern) — REKOMMENDERAD default.** Flytta upp ServiceGrids exakta grammatik: 6 kort, riktigt funktionsfoto av tinget (fotona finns redan — taklampa, öppen elcentral, kök, luftvärmepump, smarta hem, spotlights), beskrivande etikett + "Till {tjänst} ↗". Rad 2 slimmad. Varm, konkret scent, on-brand, **lägst designrisk** (mönstret är redan bevisat på samma sida). Detta = döda den dekorativa dusk-MiniMenu:n och låt den beprövade routern ta plats 3.

**Riktning C — "Behov-router / jobb-väljare" (testkandidat, matchar round-1:s "Jobb-först").** Rad 1 = kompakta chips formulerade som JOBB i kundens ord ("Elfel eller felsökning", "Byta elcentral", "Sätta upp belysning", "Installera laddbox", "Batterilagring", "Något annat") som antingen deep-linkar eller för-fyller det inline-formuläret. Högst intent-capture, mest candour-linjerad (talar husägarens språk, inte produktnamn). Kräver ny komponent + chipsen bor i routern (inte i heron — respekterar låset). Kör som test, inte default.

---

## Kept-block × ny slot — vad måste visuellt ändras (mot round-1-sekvensen)

| Block | Ny slot (round-1) | Vad DESIGNEN måste göra i den nya slotten |
|---|---|---|
| Testimonials | 4 (direkt efter router, före hårt ask) | Rör ej kortdesignen (V1 låst). Bara badge får recensions-antal (copy HP-04). Stark — den bär proof-lagret routern lämnar över till. |
| VarProcess | 5 (före telefon-asket) | Behåll ren linje-ikon-design. Bara typo-fix (HP-06). |
| MainCTA | 6 (telefon, nu förtjänad) | Ta bort 5.0-raden (HD-09), byt till svart kanonisk Ring-knapp (HD-06/08). Kortkompositionen med Edvin behålls — "mår skitbra". |
| ProduktTeaser (ersätter ProductGrid×2 + BlueCTA) | 7 | Ny lättviktsdesign: 2 kompakta kort, laddbox FÖRST, pris som bildtext + "efter avdrag"-caveat, ghost-länk, INGA specchips, INGA badges (HD-02/03/04/05). Slutar 8 tunga kort → speedvinst. |
| MainContact | 9 (avslutet) | Behåll tvåpanels-mönstret + teal submit (starkast). Fält-trim är strukturellt (HP-05). |
| MapBlock | 10 (post-form reassurance) | Tyst, inte skrikigt cyan: 6–8 orter + "fler orter →", äkta Sverige-silhuett eller ingen grafik, behåll Kontakta-oss-subkort (HD-12). |
| News | 11 | Unika foton + datum (HD-13). Annars orörd. |

---

## Vad som INTE ska röras (skydda det som funkar)

- **Den låsta heron** (ägar-canon) inkl. dess trust-rad. (Copy-mismatch mobil/desktop noteras som owner-verify — inte en redesign.)
- **Testimonials-blockets design** — V1 låst; 12 äkta namn/daterade recensioner, navy-kort, mint-stjärnor. Sidans starkaste proof. Bara badge-copy (antal) ändras.
- **VarProcess "Så funkar det"** 4-stegs linje-ikon-design — ren, ljus, rätt vikt. Bara typo.
- **MainContact:s tvåpanels-mönster** (navy fotopanel + citat + 5 av 5 + 3000+ / formulär + teal "Gratis rådgivning"). Fält-trim ≠ restyling.
- **MainCTA:s kortkomposition** (Edvin på teal, H2, Ring) — behåll; bara 5.0-raden bort + Ring-knappen unifieras.
- **Den svarta Ring-knappen i BlueCTA** — den kanoniska starka call-knappen. Propagera den, ändra den inte.
- **ServiceGrids beskrivande-etikett + funktionsfoto-grammatik** — sidans GODA router-pattern. Bevara och promotera det; uppfinn inte om det.
- **Header + Footer** (globala, utanför homepage-scope; footer-5.0 är en separat candour-item).
