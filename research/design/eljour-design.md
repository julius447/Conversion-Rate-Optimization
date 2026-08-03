# Eljour-sidorna + symptomblocket — designaudit (Round 2)

Scope: `geo-eljour-taby` (Hero_2 med formulär) · `pillar-eljour` (Hero_1 vit + bild) + det delade **symptomblocket** ("Är något fel med elen? Tryck på det du upplever.") och nedströmsblocken (stat-trio 1000+/25+/20+, MainCTA, testimonials, "Så funkar det", BlåCTA, "Visste du att", FAQ, bottenformulär). Detta är den urgent-intent-ytan. Symptomblocket missades av round-1-fingerprints — det designgranskas här första gången. Strukturkontext (ej upprepat): `research/blocks/hero2-form.md`, `main-cta.md`, `metrics-blocks.md`, `cta-bands.md`, `faq.md`.

---

## Vad ögat möter (mobil, 390px — den stressade besökaren 22:30)

**Skärm 1 (geo, tile 01, midnattsblå hero):** breadcrumb "Hem › Eljour i Täby" → grön eyebrow "Eljour i Täby" → H1 **"Eljour dygnet runt: Ring 010-265 79 79!"** (orden "runt" + numret i teal) → 4-raders paragraf → **två staplade knappar**: en dominant **grön gradient "Kostnadsfri rådgivning" ↗** och under den en **blek ljusblå "Ring 010-265 79 79"** med telefonglyf → "G 5.0 ★★★★★"-rad → och redan nu börjar formulärkortet: "Få kostnadsfri rådgivning! Vår behöriga elektriker återkommer via telefon!" + flikar **Privat / BRF / Företag**.

**Skärm 2 (geo, tile 02):** *hela skärmen är formulär* — "Vad gäller arbetet? → Elfel ▾", Namn, Telefonnummer, E-post, Adress, Postnummer, "Fler detaljer (valfritt) ▾", GDPR-checkbox, grön **"Boka rådgivning"**. Sju synliga fält innan något akut-innehåll.

**Skärm ~3 (geo, tile 03):** FÖRST här möter en panikslagen besökare triagen: H2 "Är något fel med elen? **Tryck på det du upplever.**" → vitt kort med grön pill **"● Jour öppen just nu"**, "**Akut elfel? Ring oss direkt.** Då slipper du felsöka själv…", fyra ikon-bullets (klocka/tidtagarur/sköld/prislapp: dygnet runt · på plats inom en timme · behörig elektriker, inte en växel · tydligt pris, inga dolda avgifter) → **mörkgrön solid knapp "Ring eljouren 010-265 79 79" 📞** med grön glow-prick. Detta är sidans *starkaste* call-asset — och det ligger på skärm 3, bakom hela formuläret.

**Skärm 4 (tile 04):** symptom-accordion: Säkring löser ut `Varning`, Strömavbrott `Varning`, Jordfelsbrytare löser ut `Varning`, Laddboxen blir varm `Akut`, Flimrande ljus `Varning`, Surrar/knäpper i elcentralen `Akut`, Brännlukt eller rök `Akut`, "**Se fler tecken (6) ▾**" (teal). Under kortet, grå liten text: "Varje år rycker räddningstjänsten ut till omkring **1 800 elrelaterade bränder**… Källa: Elsäkerhetsverket." Direkt därefter: det **bannade cyan-kortet "1000+ Nöjda kunder"** (badge-ikon), följt av "25+ Erfarenhet i branschen" och "20+ Personer i teamet".

**Nedåt:** MainCTA (Edvin-foto på teal, "Prata med en jour elektriker inom 60 sekunder!", **blek ljusblå Ring-knapp**, "5,0 på Google ★★★★★") → testimonials ("Vad säger dina grannar om Ampy?", mörkt kort, Jan Fernström, "5 av 5 Betyg på Google") → "Så funkar det" 4 steg → BlåCTA "Prata med en jour **elektriker!**" (cyan kort med **svart Ring-knapp**) → "Visste du att.." (mörk hemförsäkringsblock) → FAQ "Vanliga frågor".

**Pillar-varianten (tile 01):** samma hero men **vit bakgrund, INGET inline-formulär** — H1 "Eljour dygnet runt i hela **Sverige!**", samma två knappar, "5.0 ★★★★★", och en **skogsstuga-bild** där geo-sidan har formuläret. Symptomblocket kommer redan på skärm 2. Pillar avslutas med ett stort bottenformulär på navy-aurora-panel ("Få en kostnadsfri rådgivning / Bli uppringd…", Förnamn* Efternamn* E-post* Telefonnummer* +46).

## Vad ögat möter (desktop, 1440px)

**Geo hero (tile 01):** midnattsblått kort, tvåspalt — vänster: eyebrow/H1/paragraf/två knappar/5.0; höger: formulärkort "Få kostnadsfri rådgivning!" med flikar + alla fält + "Boka rådgivning". Formuläret och samtalsknappen sida vid sida — balanserat, men den bleka "Ring"-knappen försvinner mot den gröna form-knappen och det stora formulärkortet drar blicken höger.

**Symptomblock desktop (pillar tile 02, geo tile 02):** snygg **tvåpanel** — vänster: reassurance-kortet med gröna Ring-knappen; höger: symptom-accordionlistan i egen vit panel. Fungerar bättre än mobil: instruktionen "tryck på det du upplever" och den tappbara listan syns samtidigt. På mobil bryts detta — reassurance-kortet + Ring-knappen ligger *ovanpå* listan, så användaren möter en textparagraf + telefonknapp innan den tappbara listan ens syns.

**Stat-trio (geo tile 03):** "1000+ / 25+ / 20+" som tre cyan-gradientkort i rad, direkt efter symptomblocket. MainCTA under: Edvin-foto höger, copy + blek Ring-knapp vänster.

---

## Fynd

**E-01 — Formuläret begraver samtalet på den mest samtals-drivna ytan (geo).** En akut besökare möter 7 formulärfält (skärm 1–2) innan den mörkgröna "Ring eljouren"-knappen. Vid elfel 22:30 är C = 4m + 3v + 2(i−f) − 2a-friktionen (a, f) maximal och motivationen att *ringa*, inte att fylla i adress/postnummer. Evidens: tile 01 → tile 02 är rent formulär; tile 03 är först triagen. Unbounce: repair/urgent-sidor konverterar på omedelbarhet — formulärvägg motverkar det.

**E-02 — Samtalsknappen finns på skärm 1 men är visuellt underordnad.** Första tappbara telefonnumret är den **bleka ljusblå "Ring 010-265 79 79"** (mörk text, låg mättnad) *under* den gröna gradient-formknappen (tile 01, tile 12). På en emergency-yta är den svagaste visuella vikten lagd på den viktigaste handlingen. H1 innehåller numret men läses inte som en knapp (bör vara `tel:`-länk).

**E-03 — Fyra olika visuella språk för SAMMA samtalsknapp på en sida.** (1) blek ljusblå i hero, (2) **mörkgrön solid + glow** i symptomkortet, (3) blek ljusblå i MainCTA, (4) **svart solid** i BlåCTA "Prata med en jour elektriker!" (tile 09). Den gröna (2) är klart bäst — hög kontrast, telefonglyf, "Ring eljouren"-verb, glow-prick = liv. De två bleka sitter på de viktigaste platserna (hero + MainCTA). Ingen konsekvent "nödknapp".

**E-04 — Ingen sticky call-bar; den enda persistenta CTA:n leder till formulär.** Sticky headern (synlig nederst i pillar tile 11) bär pillen **"Gratis rådgivning"** = konsultation/formulär, inte ett samtal. Scrollar en stressad besökare förbi heron finns ingen ständigt närvarande ring-affordans — hen måste jaga nästa knapp. På urgent-intent är detta den enskilt största missade designen.

**E-05 — Symptom-accordionen läser som en FAQ, inte som triage.** Tap-affordansen är en tunn grå chevron (▾) längst till höger + färgprick + severity-pill. Raderna ser ut som en vanlig "frågor"-lista. Severity-pillsen (`Akut` röd / `Varning` amber) är den enda visuella hierarkin men de är små, dekorativa taggar snarare än prioritetssignal. Ordningen är inte severity-sorterad (Varning, Varning, Varning, Akut, Varning, Akut, Akut) — en panikslagen användare får ingen "börja här"-ledning.

**E-06 — Färgkodningen är sund men underutnyttjad.** Logik: röd prick+pill = Akut (Laddboxen blir varm, Surrar/knäpper, Brännlukt/rök); amber = Varning (Säkring, Strömavbrott, Jordfelsbrytare, Flimrande ljus). Rimlig kalibrering (candour: "Strömavbrott" = Varning, inte överdramatiserad Akut — bra). Men färgen driver inte layouten: Akut-rader borde visuellt lyfta (grön Ring-knapp inbäddad i den expanderade Akut-raden), inte bara byta pill-färg.

**E-07 — Det bannade "1000+ Nöjda kunder"-kortet direkt efter symptomblocket (candour-gate BLOCK).** Tile 04/05: stort cyan-kort "1000+ / Nöjda kunder / Över tusen genomförda installationer är vårt absolut starkaste kvalitetsbevis…". "1000+ kunder" är förbjudet som påstådd fakta om ej ägar-bekräftat aktuellt. Placeringen är dessutom fel: mellan akut triage och samtal ska stå *bevis på snabbhet/behörighet*, inte volymskryt.

**E-08 — "5.0 / 5,0 på Google" upprepas 3× (candour-risk + fokusstöld).** Hero-rad "5.0 ★★★★★", MainCTA-rad "5,0 på Google ★★★★★", testimonials "5 av 5 · Betyg på Google". Samma round-1-logik som MainCTA-fyndet på homepage: siffran stjäl fokus från CTA:n och upprepas tills den blir brus. Ägaren måste bekräfta 5,0 som aktuellt; annars → betyg utan siffra (som main-form-lösningen: stjärnor + "Betyg på Google" utan tal).

**E-09 — Renderingsdefekt: rå `[ort]`-placeholder i pillar MainCTA.** Pillar tile 05: paragrafen lyder ordagrant "Prata direkt med en erfaren elektriker **i [ort]** som lyssnar…". Oupplöst token syns för besökaren. Kvalitets-/candour-defekt.

**E-10 — 1800-bränder-statraden är korrekt men visuellt föräldralös.** Grå småtext som svävar mellan det vita triagekortet och det cyan 1000+-kortet (tile 04). Rätt ton (understated, källhänvisad Elsäkerhetsverket — behåll), men noll visuell inramning; den enda äkta, citerbara fear-signalen är den mest osynliga.

**E-11 — Stat-trio 25+/20+ dränker den enda relevanta akut-signalen.** "25+ Erfarenhet" och "20+ Personer i teamet" (tile 05) är generiska planned-purchase-argument på en akut-sida. Ingen av dem svarar på "kommer någon nu?". De tar tre fulla skärmar mobil.

**E-12 — Mobil bruten läsordning i symptomblocket.** Rubriken säger "tryck på det du upplever" men på mobil möter man reassurance-paragraf + Ring-knapp *före* den tappbara listan (tile 03 → 04). Löftet (tryck) och objektet (listan) är åtskilda av ett helt kort.

---

## Omdesign-direktiv (call-first)

1. **Bygg EN nödknapps-komponent och använd den överallt.** Kanon = symptomkortets mörkgröna solid + telefonglyf + glow-prick + verb "Ring eljouren · 010-265 79 79". Ersätt de bleka ljusblå Ring-knapparna i hero + MainCTA och den svarta i BlåCTA med den. Ett enda samtalsspråk på hela sidan.

2. **Geo-hero: vänd vikten (samtal = primärt, formulär = sekundärt).** Ny mobil-stack skärm 1:
   - Grön eyebrow "Eljour i Täby" (behåll)
   - H1 kortare: **"Akut elfel i Täby? Ring så rycker vi ut."** (numret som `tel:`-länk)
   - Live-pill **"● Jour öppen just nu"** flyttad UPP hit (realtidsförsäkran = starkaste motivator)
   - **Lane 1 (dominant):** nödknappen "Ring eljouren · 010-265 79 79" — full bredd, 56px hög, mörkgrön solid
   - **Lane 2 (ghost):** "Hellre bli uppringd? Fyll i formuläret ↓" — outline/text, scrollar till formuläret
   - De fyra reassurance-bullets (dygnet runt · på plats inom en timme · behörig elektriker inte växel · tydligt pris) DIREKT under — de svarar "kommer någon nu?"
   - Formuläret demoteras under symptomtriagen, inte före den.

3. **Sticky call-bar (mobil) — spec:**
   - Position: `fixed` botten, full bredd, dyker upp efter att heron scrollat ur bild
   - Höjd: **64px** + `env(safe-area-inset-bottom)`; tap-target ≥ 48px i tummens primärzon
   - Yta: **mörkgrön solid** (samma som nödknappen — vit text passerar 4.5:1; teal #00a991 gör *inte* det mot vitt, använd den mörka gröna)
   - Innehåll: telefonglyf vänster + "**Ring eljouren**" 17px semibold + numret 010-265 79 79; liten grön puls-prick = "öppen nu"
   - En handling. Ingen form-knapp i baren (skiljer den från sticky-headerns "Gratis rådgivning").

4. **Byt sticky-headerns pill-logik per intent.** På eljour-mallar bör den persistenta headerknappen vara **"Ring 010-265 79 79"** (eller dubbel: liten telefon-ikonknapp + "Gratis rådgivning"), inte enbart formulär-CTA.

5. **Symptomblocket: gör det till triage, inte FAQ.**
   - Severity-sortera: **Akut-rader först** (röd), Varning under (amber) — eller gruppera med subrubrik "🔴 Ring direkt" / "🟠 Boka snarast".
   - Höj tap-affordansen: hela raden tydligt tryckbar (hover/press-state), chevron större + i severity-färg.
   - Expanderad **Akut**-rad ska innehålla den gröna nödknappen inline ("Det här kan vara farligt — ring nu"). Expanderad Varning-rad → "Boka en elektriker" mot formuläret.
   - Behåll "Se fler tecken (6)" (bra progressiv upplysning).

6. **Ta bort "1000+ Nöjda kunder"-kortet (candour BLOCK).** Ersätt platsen mellan triage och MainCTA med *snabbhets-/behörighetsbevis*: t.ex. en rad "Auktoriserad elfirma · Behöriga jourmontörer · Tydligt pris innan utryckning" — det en akut kund faktiskt vill verifiera. Flytta 25+/20+ till om-oss, inte akut-sidan (E-11).

7. **Rama in 1800-statraden.** Ge den ett tunt vänster-border-kort (amber accent) eller lyft in den i den expanderade "Brännlukt eller rök"-raden där den är kontextuellt exakt. Behåll källhänvisningen ordagrant.

8. **De-duplicera 5.0 (E-08).** Behåll betyget på EN plats (MainCTA, närmast den konverterande knappen). Ta bort siffran ur hero-raden så den gröna knappen blir fokus (samma princip som homepage-MainCTA-fyndet). Ägar-bekräfta 5,0 innan någon siffra visas.

9. **Fixa `[ort]`-placeholdern (E-09)** i pillar MainCTA innan något annat — synlig bugg.

10. **Två-lane kontakt-layout (kanon för alla eljour-CTA-band):** Lane 1 = samtal (solid grön, större, glyf, verb); Lane 2 = formulär/återuppringning (ghost/outline, mindre). Idag är det omvänt (grön form primär, blek samtal sekundär). Gäller hero, MainCTA och bottenband.

---

## Divergenta riktningar (hero — major block, 3 versioner)

**Riktning A — "Ren nödknapp" (rekommenderad för geo/akut-intent).** Inget inline-formulär i heron. H1 + live-pill "Jour öppen just nu" + EN stor grön nödknapp + fyra reassurance-bullets, och symptomtriagen direkt under. Formulär demoteras till "Hellre bli uppringd? →". Snabbaste vägen till ett samtal; matchar 22:30-mentaliteten. Risk: förlorar de leads som hellre skriver än ringer → mildras av Lane 2.

**Riktning B — "Triagen ÄR heron".** Symptomgriden lyfts till första skärmen: "Vad har hänt? Tryck på det du märker" → tryck symptom → severity-besked (Akut → grön Ring-knapp / Varning → boka) → sticky call-bar hela vägen. Heron blir interaktiv och självsorterande; besökaren kvalificerar sitt eget ärende. Starkast för osäkra ("är det farligt?"). Risk: ett extra tap innan samtal — men det tappet ökar rätt-lead-kvalitet.

**Riktning C — "Ansikte + samtal" (split reassurance).** Behåll formuläret men flytta upp Edvin-fotot (verkligt ansikte = förtroende vid stress) bredvid H1; nödknappen dominant, formuläret kollapsat som "Boka återuppringning ▾". Varmast/mest mänskligt; bra för BRF-styrelser och äldre husägare som vill se vem de ringer. Risk: fotot tar vertikal plats på mobil — kräver disciplinerad höjd.

Intent-split (per doktrinens Hero_2-hypotes): **geo-sidan (elektriker-/eljour-i-{ort}) = kommersiellt nära → Riktning A/B (samtal + triage).** **pillar (informations-/awareness) = Riktning C eller behåll bild + lättare samtals-lane**, formuläret hör hemma i botten (som redan sker) snarare än i heron.

---

## Vad som INTE ska röras (skydda det som funkar)

- **Den mörkgröna "Ring eljouren 010-265 79 79"-knappen** med glow-prick — sidans bästa designelement. Gör den till kanon, ändra inte den.
- **Live-pillen "● Jour öppen just nu"** — äkta realtidsförsäkran, starkaste enskilda motivatorn. Flytta upp, behåll designen.
- **De fyra reassurance-bullets** (dygnet runt · på plats inom en timme · behörig elektriker inte en växel · tydligt pris, inga dolda avgifter) — candour-perfekta, exakt vad en akut kund behöver. Rör inte texten.
- **Severity-färgkodningen** (röd Akut / amber Varning) och den candour-kalibrerade nivåsättningen (Strömavbrott = Varning). Behåll konceptet, förstärk användningen (E-06).
- **Edvin-fotot** (verkligt ansikte, ampy-tröja) i MainCTA — behåll, lyft gärna upp.
- **1800-bränder-statraden med "Källa: Elsäkerhetsverket"** — äkta, citerad, understated. Behåll texten; bara rama in (E-10).
- **Desktop-tvåpanelen i symptomblocket** (reassurance-kort | accordionlista sida vid sida) — läser bra på desktop; problemet är bara mobil-stackordningen.
- **Pillars vita hero med skogsstuga-bild** — rätt lättare ton för awareness-intent; behåll som pillar-variant.
