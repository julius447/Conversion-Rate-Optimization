# VarProcess — `our-process` (4-stegs "Så funkar det")

Used on: **212 pages** (verified in `data/block-map.json`): elektriker-i 56 · elinstallation-i 56 · eljour-i 56 · service 22 · elektriker-for-x 13 · page 9 (startsidan + pillar-sidorna /elektriker/, /eljour/, /elservice/, /elinstallation/, /laddbox/, /laddboxar/, /batterilagring/, /solcellsbatterier/). **Not** used on: laddbox-i (56), produktsidor (26), lead magnets (7), artiklar (11), team (6).
Funnel position(s): **mid-page, position 6–7 av ~17–22 block** on nearly every template (service = pos 6/18, alla fyra geo-CPT + elektriker-för-X = pos 7, page-kategorin 4–10). On **132/212 pages the very next block is MainContact** (elektriker-i, elinstallation-i, elektriker-för-X, 7 pillar pages) — i.e. it is the last thing the visitor reads before the site's strongest form. On eljour-i (56) it is followed by BlueCTA (form first at pos 12/21); on service (22) by MainCTA (form at pos 10/18).

Live copy verified 2026-08-02 (anti-theatre):

- **/elektriker/akersberga/** (geo-variant): "Så funkar det — Vår steg-för-steg-process när du anlitar Ampys behöriga elektriker!" → "1. Samtal med elektriker — Fyll i formuläret så ringer vår lokala elektriker upp dig snarast." → "2. Offert & tidsförslag — Vi går igenom dina behov och skickar en tydlig offert samt ett tidsförslag." → "3. Bokning bekräftad — Vi skickar din bekräftelse samt formulär för ditt ROT avdrag." → "4. Installation utförd — Du får rapport på utfört arbete samt slutfaktura med avdragen ROT!"
- **/eljour/akersberga/** (jour-variant, brödtext anpassad): "Din guide för hjälp av Ampys akuta jourmontör!" → "…ringer vår jourhavande elektriker i Åkersberga upp dig direkt." → "Vi ser över ärendet och skickar direkt ett prisförslag för din akuta hjälp." → "…frågor för ditt försäkringsärende." → "Du får rapport på utfört jourarbete samt faktura med eventuell försäkringsavdrag."
- **/elservice/armatur/ + startsidan** (snapshot `data/pages/home.html`, samma strängar live): "Ampy's steg-för-steg-lista som beskriver hela installationsprocessen…" → "2. … **Vi går vi igenom** dina behov och skickar en transparent offert och tidsförslag." → "3. … **Vi skickar vi ut** en bekräftelse samt ett ROT formulär för smidig hantering" (utan slutpunkt).

Markup/responsive (verified in `home.html`): `<section class="our-process">` → H2 (gradient, `--aptext-2xl`) → intro-text → CSS-grid `1fr 1fr 1fr 1fr`; **≤780px: 2×2; ≤480px: 1 kolumn, 4 rader** (`@media`-regler på `.brxe-uwuxym`). Ikoner = inline-SVG `height: 99px`. Stegen är H3 under block-H2 (korrekt hierarki). Hela containern bär `data-interaction-hidden-on-load="1"` + enterView-fadeIn — innehållet är dolt tills JS kör animationen.

## What it does well
- **The four steps ARE the real process, in the right order** — samtal → offert → bekräftelse → arbete + slutfaktura. Steg 4 säger uttryckligen "slutfaktura med avdragen ROT", dvs. **du betalar efter utfört arbete och avdraget är redan draget**. Det svarar direkt på svenska husägares topp-oro (Byggahus/Reddit: prisöverraskningar, "hur funkar ROT i praktiken") och sänker MECLABS *a* (anxiety) precis där den ska sänkas.
- **Placement is fundamentally correct on 132/212 pages**: anxiety-reduktion omedelbart före MainContact-formuläret — process → löfte → formulär är läroboks-sekvensering (MECLABS: sänk *a* och höj *i−f* närmast asken).
- Eljour-varianten har **anpassad brödtext** (jourhavande, försäkringsärende i st.f. ROT) — templaten är inte blint klonad.
- Ljust, lugnt block mellan mörka sektioner; numrerade steg + ikon per steg = skannbart (NN/g: users scan, numbered steps aid comprehension).
- Steg 3-varianten på startsidan länkar till /rot-avdrag-2026/ och /gron-teknik-2026/ — intern länkning bevarad.

## Issues

**VP-1 · P1 · TIMELINE-VAKUUM: inga tider i processen, och den motsäger blocket direkt under.** Desktop+mobil. Steg 1 lovar "snarast" (geo) / ingenting (service). Tre centimeter längre ner lovar MainContacts vänsterpanel **"Vi ringer dig inom 24 timmar"**. Den konkreta siffran finns alltså på sajten men inte i processblocket — och två olika löften om samma sak sida vid sida underminerar båda (message match gäller även internt; Cialdini consistency). Inga förväntningar heller på tid-till-offert eller tid-till-installation, vilket är exakt den "hur länge får jag vänta"-osäkerhet blocket finns för att döda. Byggahus-orons kärna ("kommer de svara, hur lång tid tar det") lämnas obesvarad.

**VP-2 · P1 · PRISTRANSPARENS-STEGET SAKNAS.** "Tydlig offert" (geo) / "transparent offert" (service) säger inte det kunden behöver veta: **är offerten kostnadsfri, och är priset fast eller löpande?** Konsumentverkets råd (skriftlig offert) och Byggahus-tråden (fast vs. uppskattat pris, materialpåslag) är precis vad en riskavert 45–60-åring letar efter här. Ordet "kostnadsfri" finns i hero och form-CTA men aldrig i processteget där offerten introduceras. MECLABS *v* (value clarity) lämnas på bordet i det enda block vars jobb är att förklara affären.

**VP-3 · P1 · COPYFEL I 23+ SIDORS VARIANT (service + startsida/pillars).** "**Vi går vi igenom**", "**Vi skickar vi ut**", engelsk genitiv "**Ampy's**" (sv: Ampys), steg 3 utan slutpunkt. Dubbelfel i två av fyra steg i ett block vars enda funktion är att signalera ordning och noggrannhet — för en publik som ska anlita firman för *noggrannhet*. Trust-damaging (basic credibility convention: språkfel sänker upplevd professionalism — NN/g credibility guidelines). Geo-varianten är redan korrekt; felen ligger i service/page-instansen. Desktop+mobil identiskt.

**VP-4 · P2 · "FYLL I FORMULÄRET" PEKAR PÅ ETT FORMULÄR SOM INTE ÄR DÄR.** Steg 1 instruerar "Fyll i formuläret så ringer…". På 132 sidor är formuläret nästa block — funkar. Men på **service (22 sidor)** kommer MainCTA + FAQ före formuläret, och på **eljour-i (56 sidor)** ligger formuläret 5 block bort (pos 12/21) bakom BlueCTA, VissteDuAtt och FAQ. Instruktionen refererar antingen till hero-formuläret (som mobilanvändaren scrollat förbi för länge sedan) eller ingenting synligt (Jakob's law/expectation mismatch). Mobil förvärrar: 1-kolumns-stacken gör avståndet ännu längre.

**VP-5 · P2 · ELJOUR-VARIANTEN HAR FEL PROCESS FÖR AKUT INTENT.** Rubrikerna är kvar från installations-mallen: "2. Offert & tidsförslag" och "4. **Installation** utförd" på en sida vars besökare har ett *pågående elfel*. Unbounce home-services-benchmark: urgent/repair-sidor konverterar på RING, inte formulär — men steg 1 säger även här "Fyll i formuläret". En akut process är Ring → svar direkt → felsökning på plats → jourpris/försäkring — inte offert→bokning→installation. Brödtexten är halvanpassad, skelettet är inte. (Även "eventuell försäkringsavdrag" → "eventuellt".)

**VP-6 · P2 · DUBBEL PROCESS BACK-TO-BACK PÅ 132 SIDOR.** MainContacts fotopanel har en EGEN 3-stegsprocess ("Skicka in dina uppgifter → Vi ringer dig inom 24 timmar → Kostnadsfri rådgivning av elektriker"). Besökaren ser alltså 4 steg + 3 steg i följd, med olika stegantal, olika löften (snarast vs 24h) och delvis samma innehåll. Redundansen kostar skärmyta (särskilt mobil, där det blir ~7 staplade steg före formulärfälten) och skapar mikro-förvirring i stället för förstärkning.

**VP-7 · P3 · INNEHÅLLET ÄR JS-GATED (`data-interaction-hidden-on-load="1"` + enterView-fadeIn).** Med ~9–10s lab-LCP-flaggan riskerar anxiety-reduktionsblocket att vara osynligt/opacity-0 för långsamma enheter och utan JS. HYPOTES: att ta bort fade-gaten förbättrar upplevd hastighet och synlighet av trust-innehåll på låg-presterande mobiler — mätbart via Clarity-scrolldjup mot blocket. (Selektorn styr h1–h6 identiskt i icon-boxen — städa samtidigt.)

**VP-8 · P3 · Mobil ≤480px: 4 staplade kort med 99px-ikoner = hög kolumn** som skjuter MainContact-formuläret långt ner; ikonvärdet per pixel är lågt på mobil. 2×2-tabletläget är bra; mobilen kan komprimeras (mindre ikon, tightare gap) utan innehållsförlust.

## Recommended changes (concrete; copy-pattern direction, not final copy)
1. **Sätt tider i stegen och synka med MainContact** (VP-1): steg 1 ska bära den redan ägda siffran — mönster: "…så ringer vår elektriker upp dig **inom 24 timmar**" (samma siffra överallt; candour: bara om löftet är owner-bekräftat hållbart). Steg 2: ange typisk tid-till-offert om ägaren kan stå för den, annars utelämna hellre än "snarast".
2. **Gör steg 2 till pristransparens-steget** (VP-2): mönster "**Kostnadsfri offert** — skriftlig, med fast pris där det går, inga påslag du inte sett" (endast påståenden ägaren bekräftar; Konsumentverket-ankaret får gärna ekas). Detta är blockets största outnyttjade konverteringshävstång.
3. **Rätta service/page-variantens språkfel omedelbart** (VP-3): "Vi går igenom…", "Vi skickar ut…", "Ampys", punkt på steg 3. 15 min arbete, 23+ sidor, noll risk.
4. **Villkora steg 1-verbet på blockets grannskap** (VP-4): där MainContact inte är nästa block → "Ring oss eller fyll i formuläret längre ner" eller ankarlänk som scrollar till formuläret.
5. **Egen jour-process för eljour-i** (VP-5): Ring → vi svarar & bedömer → på plats + felsökning → åtgärd + faktura/försäkring. Steg 1 = RING (tel-länk), inte formulär. Rubriker, inte bara brödtext.
6. **Slå ihop de dubbla processerna** (VP-6): antingen låt VarProcess vara den enda processen (MainContact-panelen visar då citat + betyg + "3 000+"-raden) eller reducera VarProcess till rubrik + 4 komprimerade steg utan ikonhöjd på mobil. A/B-bart.
7. Ta bort fade-gaten (VP-7) och komprimera mobil-stacken (VP-8).

Bevarande: inget SEO-innehåll raderas — alla ändringar är omformulering/omsekvensering; interna länkar (ROT/Grön Teknik) behålls i steg 3.

## Test hypotheses (A/B)
- HYPOTES 1: Steg 2 som "Kostnadsfri offert med fast pris"-steg (mot dagens "tydlig offert") ökar form-starts på geo-sidor, mätt per 1000 sessioner (MECLABS *v*↑, *a*↓).
- HYPOTES 2: "inom 24 timmar" i steg 1 (synkat med MainContact) ökar submits jämfört med "snarast" (konsistent, konkret löfte).
- HYPOTES 3: På eljour-i ökar en ring-först jour-process telefonklick vs dagens installationsprocess (Unbounce urgent-benchmark).

## Priority score (arithmetic)
Pages affected **212** × funnel position **2** (mid-page, pre-form anxiety block) × expected effect **2** (medium — copy/sequencing fixes on the last block before the primary form on 132 pages; no structural rebuild) = **212 × 2 × 2 = 848**.
Priority: **P1** — inga konverteringsblockerande buggar, men trust-skadande språkfel (VP-3) och den saknade pris/tids-transparensen sitter i sajtens mest replikerade pre-form-yta; fixarna är billiga och bör in i månad 1. (VP-3 ensam är veckor-1-kandidat: 23 sidor, 15 minuter.)
