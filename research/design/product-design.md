# Produktsidans designsystem (ProductHero + prisblock + produktgrid)

Scope: hela produktmallen (`product-hero` + `product`, inventory §24). Underlag: `prod-sigenstor`
(riktig produktsida, 16 desktop- + 26 mobiltiles) och `prod-zaptec-go2`.

**Först, en blocker som ligger under hela auditen:** `prod-zaptec-go2` renderar **404**
("Sidan kunde inte hittas. Sidan du försöker nå finns inte. Alternativt upplever den sidan ett
strömavbrott..") på både mobil och desktop. En produkt som ligger i headerns Produkter-megameny och
i prefooterns "Populära kategorier" (mobiltile 02: *Laddboxar → Zaptec Go 2*) leder till en död URL.
Det är en läckande väg in i produktmallen som ingen designfinish räddar — **fixa datat/redirekten före
allt annat.** Resten av auditen gäller `prod-sigenstor`.

---

## Vad ögat möter (mobil)

**Fold 1 (tile 01):** Header (svart ampy-logo + grön "Gratis rådgivning"-pill med pulserande grön
prick + hamburgare) → brödsmula "Hem > SigenStor" → och sen **ett enormt vitt bildkort** som äter hela
resten av skärmen. Produkten (den vita SigenStor-batterimodulen) svävar pytteliten i mitten med ~30 %
bildyta och ~70 % tom vit padding runt om. Första skärmen är alltså i praktiken **ett nästan tomt vitt
kort.** Produktnamnet, värdeerbjudandet, priset och CTA:n ligger ALLA under fold.

**Fold 2 (tile 01 botten → 02):** Nytt vitt kort med H1 "Sigenergy - SigenStor" (stor svart) →
brödtext-paragraf (5-6 rader, "5-i-ett-system med inbyggd AI-optimering…"). Sen "Bra att veta:" med
4 ikonrader staplade (Finns i lager / Installationstid 2-4 veckor / Oberoende av solcellsfabrikat /
10 års garanti) → "Färger:" med **en enda tom grå konturcirkel** utan fyllning → prisblock.

**Prisblock (tile 02 / 13):** "Totalt" (stor svart) + "Fr. 69 000 :-" (stor svart, höger). Under:
"Ordinarie pris" (liten grå) + "138 000 :-" överstruket. Strecket korsar ":-"-suffixet och gör att det
läser **"138 000 .="** — en ren glyfdefekt. Sen två rader "Inklusive installation | Ja" och
"Grön teknik | 50%". Sen en **ljust cyan** knapp "Få skräddarsydd offert →".

**Expertkort (tile 02 botten):** Separat vitt kort — blond kille i ampy-tröja på teal bakgrund +
"Rådfråga vår expert om ditt hembatteri!" + telefon 010-265 79 79 + Google-G + "5.0 ★★★★★" (teal stjärnor).

**Sen (tile 03):** Först NU kommer accordions "Teknisk specifikation" och "Installationsprocess"
(kollapsade) — de har hamnat mellan expertkortet och kalkylatorn. Sen kalkylatorn
"Vad tjänar du på ett solcellsbatteri?" (VAD DU KÖPER / Kapacitet 18 kWh slider / DIN SITUATION).

## Vad ögat möter (desktop, 1440)

**2 kolumner, inte 3.** Vänster: stort vitt bildkort (~640px högt) med produkten liten i mitten,
enorm vit tomrymd. Under bildkortet: accordion "Teknisk specifikation", sen "Installationsprocess"
(tile 01 botten + 02 topp). Höger: H1 → paragraf → "Bra att veta" som **2×2-ikongrid** → "Färger:"
(en tom cirkel) → prisblock ("Totalt Fr. 69 000 :-" / "Ordinarie pris 138 000 :-" struck /
Inklusive installation Ja / Grön teknik 50%) → cyan "Få skräddarsydd offert".

Den så kallade "tredje kolumnen" (expertkortet, inventory §24) är i verkligheten **staplad UNDER**
prisblocket i högerkolumnen (tile 02) — den existerar inte som egen kolumn. Ögat landar först på det
tomma vita bildkortet (störst, ljusast), sen på H1, sist på priset längst ned till höger.

Under: kalkylatorn i full bredd med grön payback-panel ("TJÄNAR IN PÅ 15 ÅR / 133 625 kr", payback-kurva,
grön "Få en exakt offert →", "din@email.se / Maila kalkylen"). Sen grön-teknik-processblock
(3 penseldragna ringar 1-2-3, tile 05), content-block (hus-bilder + text, tile 05-06), FAQ + montörsbild
(tile 08), main-contact (mörk foto-panel + formulär, tile 08-09), produktgrid (tile 09-10), team (tile 11).

---

## Fynd

**PD-1 — Fold 1 på mobil är ett tomt vitt bildkort.** Produkten fyller ~30 % av ett ~800px högt kort;
resten är vit padding. Namn, värde, pris och CTA ligger under fold. Första skärmen bär noll
konverteringsjobb och noll budskapsmatchning (en besökare från en batteriannons ser inte ordet "batteri",
"Grön Teknik" eller ett pris — bara en svävande vit låda). *Bevis: mobiltile 01.*

**PD-2 — Prisblocket är designat som en fejk-rea, inte som en ärlig Grön Teknik-uträkning.**
"Totalt Fr. 69 000 :-" med "Ordinarie pris 138 000 :-" överstruket LÄSER som en 50 %-butiksrabatt. Men
raden under säger separat "Grön teknik 50 %". En svensk husägare kan omöjligt avgöra: är 69 000 priset
*efter* Grön Teknik, eller får jag 50 % Grön Teknik *till på* 69 000? Om 138 000 → 69 000 ÄR grön-teknik-
avdraget så är etiketten "Ordinarie pris" (butiksrabatt-språk) **direkt vilseledande** och strukna priset
dubbelräknar avdraget. Detta är en candour-gate-träff, inte bara en layoutfråga. *Bevis: tile 02/13, desktop 01-02.*

**PD-3 — Strukna priset renderar som "138 000 .=".** Genomstrykningslinjen korsar ":-"-glyferna och
producerar en tvetydig sträng. Ett pris får aldrig vara oläsligt. *Bevis: tile 02, 13.*

**PD-4 — Fyra offert-CTA:er, tre etiketter, två färger, på samma sida.** "Få skräddarsydd offert" (cyan,
popup) · expertkortets "010-265 79 79" (telefon) · kalkylatorns "Få en exakt offert" (grön) ·
main-contactens "Gratis rådgivning" (grön) — plus headerns "Gratis rådgivning" (grön, alltid synlig).
Samma handling (få en offert) heter tre olika saker och har två olika färger. Beslutsförlamning för
35-65-målgruppen. *Bevis: tile 02-03, desktop 02-03, 09.*

**PD-5 — Sidans primära produkt-CTA är svagare än headerns.** "Få skräddarsydd offert" är ljust cyan
med mörk text — låg kontrast, läser som sekundär/ghost. Headerns "Gratis rådgivning" är mättad grön
gradient. Produktsidans egen huvudknapp konkurreras alltså ut av den ständigt synliga header-knappen.
Kalkylatorns "Få en exakt offert" (grön) är dessutom starkare än produktens egen köp-CTA. *Bevis: desktop 01-03.*

**PD-6 — "Färger:" visar en tom konturcirkel.** En enda ofylld grå ring under en pluraletikett läser som
ett trasigt/laddande element, inte som ett färgval. Antingen har produkten en färg (då är ringen brus)
eller flera (då är den ofylld = buggig). *Bevis: tile 02/13, desktop 01.*

**PD-7 — Accordion-ordningen kollapsar på mobil.** "Teknisk specifikation" + "Installationsprocess" bor
i vänsterkolumnen på desktop (under bilden), men på mobil hamnar de **efter expertkortet och före
kalkylatorn** (tile 03) — föräldralösa, långt från produktinfon de beskriver. (Jag ser INTE en bokstavlig
dubbel-render på sigenstor; två DISTINKTA accordions, inte en duplikat. Om dubbel-render finns är den
per-produkt och obekräftad här.) *Bevis: mobiltile 01 vs 03; desktop 01-02.*

**PD-8 — "Bra att veta"-ikonerna är generiska och en är semantiskt fel.** Tunna enkla konturikoner
(paket-check, skiftnyckel, lastbil, badge-check). "Oberoende av solcellsfabrikat" paras med en
**leverans-lastbil** — lastbil ≠ oberoende/kompatibilitet. Skiftnyckeln för "Installationstid" är okej.
Ikonerna bär mening men en av fyra ljuger. *Bevis: tile 02, desktop 01.*

**PD-9 — 5.0-raden stjäl expertkortet (samma fynd som MainCTA-fröet).** I expertkortet finns "5.0 ★★★★★"
i teal precis under telefonnumret. Precis som ägarens MainCTA-observation ("ta bort 5.0 så blir CTA:n
hela fokuset") drar den teal-stjärnraden blicken från det som är kortets jobb — telefonnumret. Plus
candour: "5.0" utan antal recensioner, upprepat i ≥6 block. *Bevis: tile 02, desktop 02.*

**PD-10 — Produktgridens taggpiller saknar system.** "BÄSTSÄLJARE" = mörk navy pill; "SUPERKAMPANJ" =
grön pill (≈ varumärkets teal). Två färger, ingen semantisk logik, och den gröna "SUPERKAMPANJ" späder
ut brand-accenten OCH luktar rea/urgency (candour-risk: är det en verklig kampanj?). *Bevis: desktop 09.*

**PD-11 — Prislogik krockar mellan hero och grid.** Hero-produkten visar struket "ordinarie" (138 000 →
69 000). Grid-korten under ("Andra solcellsbatterier") visar rena priser utan strykning ("Fr. 34 900 kr").
Samma sida, två prisspråk. Dessutom: SigenStor 69 000 kr står direkt ovanför billigare alternativ
(33-36k) under rubriken "Andra solcellsbatterier" — merchandising som undergräver den dyra hjälteprodukten.
*Bevis: desktop 09-10.*

**PD-12 — Bildkortets tomrymd upprepas på desktop.** ~640px kort, produkt liten i mitten, resten vit.
Största, ljusaste elementet på sidan bär minst information och drar first-glance-blicken bort från H1/pris.
*Bevis: desktop 01.*

---

## Omdesign-direktiv

1. **Bygg det ärliga prismodulen (PD-2, PD-3).** Ersätt "Totalt / Ordinarie pris struck" med en läsbar
   avdragsstege — det ÄR designen ägaren efterfrågar:
   ```
   Pris inkl. installation           138 000 kr
   – Grön Teknik-avdrag (50 %)       –69 000 kr   (grön, +ikon)
   ─────────────────────────────────────────────
   Du betalar                    Fr. 69 000 kr    (stort, fetast elementet i kolumnen)
   ```
   Slopa ordet "Ordinarie pris" (butiksrabatt-språk). Ingen genomstrykning över ":-". Mikrocopy under:
   "Vi drar av Grön Teknik direkt på fakturan och sköter ansökan till Skatteverket åt dig." Det gör
   avdraget till bevis på ärlighet i stället för en tvetydig rea. Behåll "Fr." (från-pris) — det är candour-korrekt.

2. **Gör "Få skräddarsydd offert" till sidans starkaste knapp (PD-5).** Byt cyan → samma gröna gradient
   som "Gratis rådgivning"/"Få en exakt offert". En färg för "få en offert" över hela sidan. Full bredd i
   högerkolumnen, direkt under prismodulen, som kolumnens visuella slutpunkt.

3. **Slå ihop CTA-språket (PD-4).** Välj EN etikett för formulär-vägen ("Få kostnadsfri rådgivning") och
   låt telefon vara den tydligt sekundära. Kalkylatorns knapp får heta samma sak. Två vägar (ring/formulär),
   ett ordval, en färg — inte fyra.

4. **Krymp bildkortet och lyft värdet över fold på mobil (PD-1, PD-12).** Beskär den vita tomrymden så
   produkten fyller ~70 % av ett lägre kort (~360-400px på mobil). Direkt under bilden, i fold 1-2: H1 +
   EN värderad rad ("5-i-ett-batteri med AI-styrning — 50 % Grön Teknik") + "Fr. 69 000 kr efter Grön
   Teknik" + primär CTA. Batteribesökaren ska se ordet batteri, ett pris och en knapp på första/andra skärmen.

5. **Flytta accordions tillbaka till produkten på mobil (PD-7).** Rendera "Teknisk specifikation" +
   "Installationsprocess" direkt efter prismodulen/CTA:n, FÖRE expertkortet och kalkylatorn — inte
   föräldralösa mellan dem. (Verifiera samtidigt om någon produkt faktiskt dubbel-renderar spec-accordion;
   obekräftat här.)

6. **Fixa "Färger" (PD-6).** Om en färg: fyll cirkeln med produktens faktiska vita + tunn kant +
   markerad/vald-state (bock), eller ta bort hela "Färger"-raden för enfärgade produkter. En tom ring är
   alltid ett fel.

7. **Byt lastbilsikonen (PD-8).** "Oberoende av solcellsfabrikat" → en pussel-/kompatibilitetsikon eller
   plug-ikon, inte en leveranslastbil. Behåll ikongriden 2×2 desktop / 1-kol mobil.

8. **Ta bort 5.0-raden ur expertkortet (PD-9).** Låt telefonnumret bli kortets fokus (samma logik som
   MainCTA-fröet). Om betyg behövs: flytta det till ETT ställe på sidan (main-contact eller testimonials)
   och ankra det med antal recensioner, annars candour-brott.

9. **Systematisera taggpillren (PD-10).** En pill-stil (t.ex. mörk navy med vit text) för alla taggar,
   semantiskt använd. Släpp "SUPERKAMPANJ" (urgency-doft) → om det är en riktig kampanj: "Kampanjpris".
   Grön reserveras för Grön Teknik, inte för rea.

10. **Ett prisspråk hero↔grid (PD-11).** Om hero visar avdragsstege ska grid-korten visa samma logik
    ("Fr. X kr efter Grön Teknik") — eller båda rena. Överväg att döpa om "Andra solcellsbatterier" så den
    inte skickar besökaren till billigare konkurrenter mitt i köpövervägandet ("Jämför modeller" / "Fler
    batterier vi installerar").

---

## Divergenta riktningar — prismodulen + högerkolumnens CTA-zon (huvudingreppet)

**Riktning A — "Ärlig avdragsstege" (rekommenderas).** Prismodulen = uträkningsstegen (direktiv 1) med
grön avdragsrad, stort "Du betalar", grön primär-CTA direkt under. Expertkortet demoteras till en tunn
telefonrad ("Hellre prata? Ring 010-265 79 79", ingen bild, ingen 5.0). Lugnt, transparent, säljer på
ärlighet — matchar candour-gaten och 35-65-målgruppens pris-oro (final-price-surprise).

**Riktning B — "Sticky köp-panel".** Högerkolumnens prismodul + CTA blir en sticky panel som följer med
när man scrollar genom accordions/kalkylator på desktop; på mobil en sticky bottenbar ("Fr. 69 000 kr ·
Få offert") som dyker upp efter fold 2. Maximerar CTA-närvaro utan att duplicera fyra knappar. Risk:
mer "e-handel" i känslan än en elfirma vill ha — testas mot A.

**Riktning C — "Kalkylator-först".** Eftersom kalkylatorn redan räknar payback (133 625 kr / 5,4 år) —
gör den till hjälten högst upp i högerkolumnen och låt prismodulen bli dess sammanfattning ("Din uträkning:
Fr. 69 000 kr, payback 5,4 år → Få en exakt offert"). Ett enda offert-flöde. Mest övertygande för den
rationella batteriköparen, men tyngst (kräver att kalkylatorn flyttas upp) — reservera för batteri-
produkter, inte laddbox.

Alla tre delar: en färg för offert, ärlig Grön Teknik-uträkning, telefon som sekundär.

---

## Vad som INTE ska röras

- **Kalkylatorn "Vad tjänar du på ett solcellsbatteri?"** — payback-panel, kurva, fyra intäktskällor,
  "Så har vi räknat"-öppning: stark, ärlig, välbyggd. Rör inte designen; koppla bara ihop dess CTA-språk
  med resten (direktiv 3).
- **Grön-teknik-processblocket** (3 penseldragna ringar 1-2-3, "Läs mer om Grön Teknik-avdrag", tile 05) —
  varmt, tydligt, on-brand. Behåll.
- **Content-blockets hus-bilder** (tile 05-06) — hög bildkvalitet, lugn premiumkänsla för målgruppen. Behåll.
- **Main-contact** (mörk fotopanel + formulär, tile 08-09) — sidans starkaste konverteringstillgång
  (inventory §4). Rör inte strukturen; endast 5.0/antal-recensioner-candour gäller globalt.
- **Team-slidern** (Magnus/Felix/Edvin, tile 11) — riktiga ansikten, E-E-A-T, byggd på riktiga elektriker. Behåll.
- **H1 "Sigenergy - SigenStor" som riktig H1** — till skillnad från Hero_2:s inverterade eyebrow-H1 är
  produktmallens rubrikhierarki korrekt. Rör den inte.
