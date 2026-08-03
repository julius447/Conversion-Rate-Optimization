# AlternativHero-ytor: hubbar, pelare, magneter (design-audit, round 2)

Fyra ytor, granskade pixel för pixel ur den svenska husägarens perspektiv (35–65, lugn, verifieringssökande):
**hub-laddboxar** (produktkatalog), **pillar-elektriker** (Hero-1-pelare), **pillar-batterilagring** (Hero_2-pelare, mörk),
**magnet-energikalkylator** (det nakna verktyget). Fokus enligt doktrinen: vad som stjäl fokus, vad som förtjänar sina
pixlar, element för element. Referens till block-inventory-nummer (02-block-inventory.md) där relevant.

Genomgående tokens som gäller: teal #00a991, midnatt #090b32, Outfit. Candour-grinden oförändrad.

---

## 1. hub-laddboxar — AltHero + naken produktkatalog

### Vad ögat möter (mobil)
Tile 01: header → **mörk midnattsblå AltHero-kort** (Block 3, `laddbox-hero`). Breadcrumb "Hem › Laddboxar" litet uppe till
vänster. H1 "Laddboxar **över hela** Sverige" (vitt + teal på "över hela"). En paragraf på tre rader. Sedan **~40 % av
kortets höjd är tom, död navy-yta** med bara en svag vågform. Ingen CTA, ingen bild, inget formulär, ingen laddbox.
Kortet fyller nästan hela första skärmen och bär bara en rubrik och en mening.

Tile 02 och nedåt: kortet slutar, och sidan blir en **enspaltig stapel av nära identiska produktkort** som löper ~24 tiles
djupt. Varje kort: produktfoto → kampanjpille (SUPERKAMPANJ grön / NYHET cyan / BÄSTSÄLJARE navy) → chip-rad
"1-fas & 3-fas | 22 kW" → produktnamn (Zaptec Go, Zaptec Go 2, NexBlue Edge 2, Charge Amps Luna/Halo, Amina S, Tesla
Wall Connector, go-e…) → tre rader beskrivning → avdelare → "Fr. X kr" → **full-bredds himmelsblå "Läs mer"-pill**.
Zaptec Go dyker upp igen längre ner (tile 13/24) — katalogen loopar/upprepar. Sidan **slutar på produktkort** (tile 25 =
Zaptec Go 2 + Easee). Ingen kontaktform, ingen "vilken laddbox passar mig", inget trust-block, ingen Vår process, ingen
Ampy-CTA i hela brödtexten.

### Vad ögat möter (desktop)
Tile 01: AltHero är ett brett mörkt kort. Rubrik + paragraf ligger i **vänstra ~40 %**; **högra ~55 % är helt tom** navy
med en svag mörkare vågform. Enorm outnyttjad förstaskärm. Under: **4-kolumns produktrutnät**, kort efter kort efter kort.
Samma katalog, bara bredare. Ingen konverteringsmekanism någonstans på sidan utom header-knappen "Gratis rådgivning".

### Fynd
- **H-L1 · AltHero förtjänar inte sin skärm.** Ett helskärmskort som bara bär titel+mening. Earn-rate på första skärmen ≈
  noll: inget löfte, ingen bild, ingen handling, ingen väg vidare. 40 % (mobil) / 55 % (desktop) av kortet är tomt.
- **H-L2 · Katalog utan routing-jobb gjort.** Hubbens enda jobb är att ta en förvirrad köpare ("vilken laddbox?") och
  slussa till samtal/formulär. Istället en spec-vägg av 10+ nära identiska svarta boxar + priser. Köparen får ingen hjälp
  att välja, och ingen väg till Ampy — bara "Läs mer" in i produktsidor (återvändsgränder) eller katalog-loop.
- **H-L3 · Monoton kortrytm.** Varje kort har exakt samma anatomi och samma himmelsblå "Läs mer"-pill. Efter tre kort
  slutar ögat läsa; skillnaden mellan produkterna (som är hela poängen) drunknar i upprepningen.
- **H-L4 · Inverterad konverteringsallokering (strategiskt).** Laddbox är kommersiell prioritet #2 (över batteri) — men
  hubben har **noll** formulär, medan batteri-pelaren (prioritet #3, av Google Ads) bär hela Hero_2-formuläret. Maskineriet
  sitter på fel vertikal.
- **H-L5 · "Fr. X kr" utan nästa steg.** Priset är kortets tyngsta element (störst, svartast) men leder bara till "Läs
  mer". Priset skapar sticker-frågor ("vad ingår? installation?") som ingen CTA på sidan besvarar.

### Omdesign-direktiv
1. **Ge AltHero ett jobb eller krymp den.** Antingen (a) fyll högra/nedre tomrummet med en **laddbox-produktbild** +
   lägg in **ett CTA-par** (Kostnadsfri rådgivning + Ring) så första skärmen börjar konvertera, eller (b) halvera kortets
   höjd så katalogen syns direkt. Tomma navy-ytan får inte stå kvar.
2. **Lägg in ett routing-block direkt under hero:** "Osäker på vilken laddbox?" → 2–3 frågor (villa/BRF, 1-fas/3-fas,
   fast kabel/uttag) → filtrerar katalogen ELLER leder till rådgivning. Det är hubbens riktiga jobb.
3. **Bryt kortmonotonin:** lyft 1 "Populärast"-kort till full bredd med mer copy; låt resten vara kompaktare. Låt
   kampanjpillen faktiskt betyda något (inte tre av fyra kort märkta).
4. **Stäng sidan.** Lägg **Main contact** (Block 4, sajtens starkaste tillgång) + **Vår process** (Block 11) före footern.
   Idag dör sidan på produktkort — en katalog utan avslut.
5. **Avlasta priset:** komplettera "Fr. X kr" med en liten "inkl. installation? Fråga oss" länk till rådgivning, så
   pris-ångesten fångas istället för att läcka.

---

## 2. pillar-elektriker — Hero-1 + Metrics + MainCTA

### Vad ögat möter (mobil)
Tile 01 (Hero-1, Block 2): vitt svävande kort på ljus bakgrund. **H1 "Elektriker för privatpersoner över hela Sverige!"**
— "Elektriker för privatpersoner över hela" i **solid svart**, bara "Sverige!" i teal. **Fullt läsbar** — detta är INTE
gradient-på-vitt-problemet. Paragraf: "Upptäck **marknadens billigaste priser**, trygga installationer och elektriker som
hjälper dig från start till mål." Två CTA: grön gradient **"Kostnadsfri radgivning"** (↗) + ljusblå "Ring 010-265 79 79"
(pulsande telefon-chip). Sedan "G **5.0** ★★★★★" i **teal** stjärnor. Sedan maskad hero-bild (hus i skymning) med
sinusvåg-topp.

Tile 02: Metrics (Block 22) på ljus cyan-gradient. **"1000+ Nöjda kunder"** + brödtext "Över tusen genomförda
installationer är vårt absolut starkaste kvalitetsbevis…". **"25+ Erfarenhet i branschen"**.

Tile 03–04: **"20+ Personer i teamet"** → MainCTA (Block 5): Edvin-foto (teal bg, ampy-tröja) → **"Prata med en
elektriker inom 60 sekunder!"** (navy + teal) → paragraf → **enda "Ring 010-265 79 79"-CTA** → **"G 5,0 på Google ★★★★★"
i GULD** direkt under knappen. Sedan content-block "Vårt utbud av tjänster – installerat & klart med 30 % ROT-avdrag".

### Vad ögat möter (desktop)
Tile 01: Hero-1 = brett vitt kort, hero-bild i högra ~40 % med vågmask, CTA-par sida vid sida, 5.0-rad under. Balanserat
och läsbart. Metrics blir 3-kolumn (1000+ / 25+ / 20+).

### Fynd
- **P-E1 · MainCTA: 5,0-raden stjäl fokus från Ring-knappen.** Exakt ägarens frö-fynd. Under den enda Ring-CTA:n sitter
  "5,0 på Google ★★★★★" i guld och drar blicken nedåt, bort från knappen. Ta bort raden → Ring-knappen blir hela fokuset.
  MainCTA är sajtens potentiellt starkaste samtals-tillgång; låt den vara odelad.
- **P-E2 · Två betygsrenderingar på samma sida.** Hero-1 = "5.0" med **teal** stjärnor, ingen "på Google". MainCTA = "5,0"
  med **guld** stjärnor + "på Google". Olika decimaltecken (5.0 vs 5,0), olika stjärnfärg, olika etikett. Inkonsekvent —
  och guld-stjärnorna bryter mot tokensystemet (teal är enda accent).
- **P-E3 · CTA-etikett spretar + stavfel.** Hero-knappen: **"Kostnadsfri radgivning"** (saknar å). Header: "Gratis
  rådgivning". Två namn för samma handling + felstavning på det viktigaste elementet i hjälten. Message-match-brott.
- **P-E4 · Candour: "marknadens billigaste priser".** En superlativ PRIS-påstående i hero-paragrafen. Superlativ är
  tillåtna om de inte är bevisbart falska — men "billigaste priser" är ett verifierbart, juridiskt känsligt prispåstående
  som Ampy inte kan belägga. Byt mot ett candour-tåligt löfte (t.ex. "tydliga priser, fast offert innan vi börjar").
- **P-E5 · Candour: "1000+ Nöjda kunder" + intern motsägelse.** "1000+ Nöjda kunder"/"Över tusen genomförda
  installationer" (Metrics) mot **"3 000+ genomförda installationer om året"** (magnet-testimonial, main-contact). Samma
  sajt, olika siffror. "1000+" är dessutom uttryckligen bannat om inte ägarbekräftat. Låt EN sanning gälla.

### Omdesign-direktiv
1. **Ta bort "5,0 på Google"-raden i MainCTA.** Ring-knappen blir hela fokuset (P-E1). Om social proof behövs där: en
   diskret textrad "Betyg 5,0 på Google" UTAN stjärnrad, i caption-vikt under.
2. **En betygsrendering globalt:** teal stjärnor, "5,0", med eller utan "på Google" — välj en och använd överallt. Döda
   guld-stjärnorna (token-defekt).
3. **Rätta hero-knappen till "Kostnadsfri rådgivning"** (å) och synka etiketten med header ("Gratis rådgivning" vs
   "Kostnadsfri rådgivning" — välj ett).
4. **Byt "marknadens billigaste priser"** mot candour-löfte om transparent pris/fast offert.
5. **Lås EN kundsiffra** (Metrics vs testimonial) — troligen "3 000+ installationer/år" om ägarbekräftat, annars [GAP].

### Vad INTE ska röras
- Hero-1:s svart+teal H1 (läsbar, ren) — rör inte kontrasten.
- MainCTA:s Edvin-foto + "Prata med en elektriker inom 60 sekunder" — starkt, mänskligt, behåll.
- Ring-chippets pulsande telefon — bra affordans.

---

## 3. pillar-batterilagring — Hero_2 (mörk) + produktkatalog

### Vad ögat möter (mobil)
Tile 01: **helt mörk midnattsblå hjälte** (Hero_2 på navy). Breadcrumb "Hem › Batterilagring". Grön eyebrow
"Batterilagring / Solcellsbatteri". H2 **"Batterilagring med installation – kapa elkostnaderna idag!"** (vitt + teal
gradient). Paragraf. Två CTA (grön "Kostnadsfri rådgivning" — **rätt stavat här** + blå Ring). "G 5.0 ★★★★★" teal. Sedan
börjar **ett mörkt navy formulärkort** ("Få kostnadsfri rådgivning! / Vår behöriga elektriker återkommer via telefon!").

Tile 02: formuläret (`.aof`) — **vita fält på mörk navy**: Privat/BRF/Företag-toggle → "Vad gäller arbetet?" =
Batterilagring (låst) → Namn → Telefonnummer → E-post → Adress → Postnummer → "Fler detaljer (valfritt)" → GDPR → grön
"Boka rådgivning". **5 synliga textfält + toggle + select** upp front, inkl. Adress+Postnummer.

Tile 05+: under hjälten — **produktkatalog** (batterier: "Skalbart högvoltsbatteri… LiFePO4… 8 000 laddningscykler",
Fr. 33 000 kr, BÄSTSÄLJARE, 1-fas/3-fas, 9.60–51.20 kWh, Enershare…). Samma kortmönster som laddbox-hubben.

### Vad ögat möter (desktop)
Tiles 01–04: **hjälten är TRASIG på desktop.** Header renderar, sedan en **massiv tom ljusblå tomrumsyta** — hela
hero+formuläret uteblir. Bekräftat över fyra tiles (01, 02, 03, 04 = header + blank void). En desktop-besökare möter en
vit avgrund där hjälten ska vara. (Överensstämmer med känt P0 "trasig batterilagring-hero".)

### Fynd
- **P-B1 · P0: desktop-hjälten renderar inte.** Hero+formulär saknas helt på desktop; sidan öppnar med tom yta. Detta är
  inte en finess-fråga — det är en trasig förstaskärm på sajtens dyraste vertikal-mall. Blockar allt annat här.
- **P-B2 · Dark-on-dark.** Mörk navy hjälte + mörkt navy formulärkort = tung, platt kontraststapel. Formulärkortet läser
  som en förlängning av bakgrunden istället för att lyfta som en handlingsyta. (Block 1 känd tension bekräftad visuellt.)
- **P-B3 · Full formulärfriktion på lägst prioriterad vertikal.** Batteri är prioritet #3 och AV Google Ads — ändå bär
  sidan hela Hero_2-formuläret med 5 fält + Adress+Postnummer upp front (Baymard: antal synliga fält driver upplevd
  svårighet). Maskineriet är felallokerat (jfr H-L4).
- **P-B4 · Mild urgency i H2.** "kapa elkostnaderna **idag!**" — "idag!" doftar tempo/urgency. Candour-registret för en
  ekonomisk högriskssida ska vara lugnt och sakligt, inte "idag!".
- **P-B5 · Hjälte + katalog = dubbel identitet.** Sidan är både en säljande pelare (hero+form) OCH en katalog. Besökaren
  vet inte om detta är "läs om batterilagring", "få rådgivning" eller "handla batteri". Tre jobb, ingen hierarki.

### Omdesign-direktiv
1. **Fixa desktop-renderingen (P0, P-B1)** innan någon annan ändring. Utan hjälte finns ingen sida på desktop.
2. **Lyft formulärkortet ur mörkret:** ge `.aof`-kortet en ljusare yta (ljus glas/vit) mot den mörka hjälten, ELLER gör
   hjälten ljusare. Kortet måste läsa som en separat handlingsyta (P-B2).
3. **Sänk formulärfriktionen på batteri:** min-lead = Namn + Telefon + Postnr + GDPR; flytta Adress + E-post till "Fler
   detaljer". Batteri behöver inte samma tunga formulär som en het service-sida (P-B3).
4. **Ta bort "idag!"** ur H2 → lugnt candour-register ("Batterilagring med installation – sänk dina elkostnader").
5. **Separera de två jobben:** hero+form överst = rådgivning; katalogen längre ner under en tydlig egen rubrik ("Utforska
   batterier") så besökaren förstår skiftet (P-B5).

---

## 4. magnet-energikalkylator — det nakna verktyget + ägarens wrap

### Vad ögat möter (mobil)
Tile 01: header → **direkt in i verktyget, kallt.** Vitt verktygskort "DITT HUS / Vad värmer huset idag? *Välj en eller
flera*" med 8 uppvärmnings-val + "Vet inte" + Boyta-reglage (150 m²). **Inget hero, ingen titel, ingen trust, ingen
kontext ovanför verktyget.** En annonsbesökare landar mitt i ett formulär utan att veta vad det är eller vem Ampy är.

Tile 02: DITT HUS forts. (Byggår, Boende-räknare, elområde SE1–4) → DIN EL (drar per år, Solceller). Flytande sticky-pill
"Se resultatet ↓" mitt i scrollen.

Tile 03: **mörkt resultatpanel** — "SÅ FÖRBRUKAR DITT HUS ENERGI IDAG / **38 000–48 000 kr per år**" (stor vit siffra),
staplad breakdown (Uppvärmning ~30 500 / Varmvatten ~3 500 / Hushållsel ~9 000), "Så mycket kan du spara per år" med
"★ Vår rekommendation"-kort (Behåll direktel + luft-luft, 12 500–17 500 kr/år, Ny kostnad / Besparing / Återbetalningstid
1,5–2 år) + expanderbara alternativ (Luft-vatten, Bergvärme, Smart styrning).

Tile 04: **grön "Få kostnadsfri rådgivning"-CTA** (full bredd, inuti panelen) + "Dela din kalkyl" ghost + "Så har vi
räknat"-disclosure → **testimonial-kort** (Hugo Grafström Olsson, husbild, ★★★★★ guld "5 av 5 · Betyg på Google",
"3 000+ genomförda installationer om året") → prefooter "Populära kategorier" → footer.

### Vad ögat möter (desktop)
Two-pane: **vänster vitt input-kort, höger mörkt resultatpanel** (sticky). Rent, fungerar bra. Samma **kalla öppning** —
inget hero, verktyget börjar direkt under headern. Grön CTA + "Dela" + "Så har vi räknat" i panelens botten, sedan
testimonial-kort, sedan prefooter.

### Fynd
- **M1 · Ingen topp — verktyget öppnar kallt.** Ägarens diagnos bekräftad visuellt: det finns INGET ovanför verktyget.
  Ingen AltHero, ingen rubrik ("Vad kostar ditt hus i el?"), ingen trust-framing. Besökaren får noll orientering innan
  hen ombeds fylla i 6 fält. Message-match från annons → H1 → första skärm är omöjlig utan en topp.
- **M2 · Tunn avslutning.** Closen är en **ensam grön knapp** i panelen + ett testimonial-kort. Ingen riktig **Main
  contact**-form (sajtens starkaste tillgång), ingen **Vår process** (hur rådgivningen går till). Den gröna knappen är en
  naken knapp — inget formulär i vy. Efter ett starkt resultat (38 000–48 000 kr, återbetalning 1,5–2 år) finns ingen
  lågfriktionsväg att fånga den varma besökaren.
- **M3 · Verktyget självt är bra — rör det inte.** DITT HUS/DIN EL-flödet, sticky "Se resultatet", den mörka
  resultatpanelen med breakdown + rekommendation + intervaller (38 000–48 000, 1,5–2 år) är candour-tåligt och tydligt.
  Detta är inte problemet.
- **M4 · Betyg/siffror: guld-stjärnor + 3 000+.** Testimonialen använder guld "5 av 5" (token-defekt, jfr P-E2) och
  "3 000+ installationer/år" (intern motsägelse mot pillar-metrics "1000+").

### Omdesign-direktiv (ägarens wrap: AltHero + Vår process + Main contact — men verktyget ska dominera)
1. **Lägg en AltHero (Block 3) ovanpå — låg, inte helskärm.** Kompakt navy-remsa: eyebrow "Energikalkylator" → kort H1
   ("Se vad ditt hus kostar i el – och vad du kan spara") → EN mening trust ("Räknat på svenska elpriser och ditt
   elområde"). **Får inte trycka ner verktyget under vikningen** — max ~30–40 % av första skärmen på mobil, så verktygets
   översta rad syns. Detta löser M1 utan att stjäla verktygets dominans.
2. **Lägg Vår process (Block 11) efter resultatet, före contact:** 4 steg (ring/skicka → vi ringer inom 24 h →
   kostnadsfri rådgivning → offert). Besvarar "vad händer om jag klickar?".
3. **Byt den nakna gröna knappen mot / komplettera med en riktig Main contact-form (Block 4)** längst ner — den varma
   besökaren efter kalkylen ska mötas av ett fält att fylla, inte bara en knapp. Behåll den gröna CTA:n i panelen som
   snabb-hopp till formuläret.
4. **Rätta betygsrendering till teal-stjärnor + lås kundsiffran** (M4) i linje med resten av sajten.

### Divergenta riktningar för magnet-wrappen (stort ingrepp → 3 versioner)
- **Riktning A — "Tunn hatt, tjock stjärt."** Minimal AltHero (bara eyebrow + H1, ~25 % mobil-skärm), verktyget dominerar
  omedelbart; all tyngd i avslutet (Process + Main contact + testimonial). Bäst om måldata visar att besökaren kom FÖR att
  räkna (verktyget är hjälten).
- **Riktning B — "Trust-först."** AltHero bär en kort trust-rad (behörig elektriker, 3 000+/år, teal 5,0) + H1, sedan
  verktyget. Closen = Vår process + Main contact. Bäst om annonsbesökaren är kall och behöver Ampy-legitimitet innan hen
  ger 6 svar. Risk: knuffar verktyget nedåt — håll höjden hård.
- **Riktning C — "Resultat-till-form-brygga."** Ingen tung topp; istället en **inline övergång** där den gröna CTA:n i
  resultatpanelen expanderar Main contact-formen på plats (value-then-ask, samma mönster som huvudformuläret) + Vår
  process som liten remsa bredvid. Bäst för minsta friktion mellan "aha" och lead. Rekommenderad primär om bygget tillåter.

### Vad INTE ska röras
- Själva verktyget (DITT HUS/DIN EL, sticky "Se resultatet", mörk resultatpanel, breakdown, rekommendationskort,
  intervaller, "Så har vi räknat"). Det är candour-guld och ska förbli sidans dominant.
- Two-pane desktop-layouten (input vänster / resultat höger).

---

## Genomgående (alla fyra ytor)

- **Betygsrendering är osammanhängande sajtövergripande:** teal "5.0" (Hero-1, hubbar) vs guld "5,0 på Google"
  (MainCTA, magnet-testimonial). Standardisera till EN rendering — teal stjärnor, "5,0", token-korrekt. Guld = token-defekt.
- **Kundsiffran motsäger sig själv:** "1000+" (pillar-metrics) vs "3 000+/år" (magnet/main-contact). Lås en sanning
  eller [GAP].
- **Konverteringsmaskineriet sitter på fel vertikaler:** batteri (#3, av Google) bär fullt Hero_2-formulär medan laddbox
  (#2) och magneten bär inget/naket. Omfördela: formulär dit den kommersiella prioriteten och den varma intenten finns.
- **Candour att åtgärda:** "marknadens billigaste priser" (pillar-elektriker), "1000+ nöjda kunder" (metrics),
  "kapa elkostnaderna idag!" (batteri-H2). Alla tre bryter mot grinden.
