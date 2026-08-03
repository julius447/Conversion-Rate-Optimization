# Incitamentsblocken — visuell omdesign (ROT 30 % · Grön Teknik 50 % · Hemförsäkring)

Blocken `rot` / `gron-teknik` + hemförsäkrings-tvillingen (inventory §12–13; round-1 `incentive-blocks.md`, INC-01…08). Round 1 verifierade struktur, copy och funnel-position live. Detta lager är rent visuellt: vad ögat gör med blocket, element för element.

**Anti-teater / vad jag faktiskt SÅG (inte narrativ):**
- **Direkt sett, renderat:** hemförsäkringsvarianten på **desktop** (`geo-eljour-taby--desktop--08`) — den enda av mina fyra sidor där själva incitamentsblocket dök upp i mina tile-intervall. Där ser jag hela mönstret: centrerad H2 med teal-gradient-fragment, **tre numrerade cirklar (1·2·3) med skissig/handritad teal-ring + streckade teal-kopplingar**, tre processrubriker, och en liten skiss-ring-pill "Läs mer om ROT-avdrag".
- **Direkt sett, incitamentet uttryckt via ANDRA bärare** på geo-sidorna: hero-paragraf ("alltid med 30 % ROT-avdrag direkt på fakturan", `elektriker-tyreso--mobile--12`), processteg ("formulär för ditt ROT avdrag", steg 3), och **produkt/tjänst-gridens rubrik** i grön gradient ("installerat & klart med 30 % ROT-avdrag", `--mobile--16`; "50 % Grön Teknik-avdrag", `laddbox-nacka--mobile--14`).
- **Inte sett i mina tiles:** ROT-varianten (elektriker) och Grön Teknik-varianten (laddbox) som *eget stegblock*, och stegblockets **mobil**-rendering. Round-1 hämtade dem live (identisk `rot__`-mall); mobil-beteendet nedan är därför märkt som **härlett ur INC-07-CSS**, inte observerat. `prod-zaptec-go2` är en **404-sida** ("Sidan kunde inte hittas") — inget produktblock att granska där.
- **Bonus, direkt sett:** eljour-symptomblocket (`geo-eljour-taby--mobile--14`) är den lugnaste, mest läsbara ikonlistan på sidan ("Tydligt pris innan vi rycker ut, inga dolda avgifter" + EN grön Ring-knapp). Det är den interna nordstjärnan incitamentsblocket bör sträva mot — se Rikt C.

---

## Vad ögat möter (mobil)

Stegblockets mobil-rendering låg inte i mina eljour-tiles (05–11 bar hemförsäkrings-argumentet via *Visste du att*-kortet + FAQ i stället). Härlett ur INC-07-CSS (1-kolumn ≤780 px, `--apspace-3xl`-gap vid 480 px, `.rot__process-item{margin-top:-15px}`, gradient `-webkit-text-fill-color:transparent` på hela H2):

- Ögat möter en **centrerad rubrik i teal-gradient** där hela raden är gradientfylld — dvs. de viktigaste orden ("30 % rot-avdrag") renderas i den svagaste kontrasten på hela sidan. På vit botten ligger teal (#00a991) runt ~2.8:1 mot vitt; en gradient drar ena änden ännu ljusare. **Värdefrasen är minst läsbar av allt i blocket** — raka motsatsen till vad den ska vara för 35–65-publiken.
- Under rubriken: **tre staplade cirklar (1·2·3)** med processtext under vardera. Ingen siffra i kronor. ~2–3 skärmhöjder icke-klickbar scroll (INC-07) inklämt mitt i tratten.
- Längst ner en **liten skiss-ring-pill** ("Läs mer om …") — blockets enda interaktiva element, och det leder **ut** till en formulärslös artikelsida (INC-02).
- Det som FAKTISKT bar hemförsäkrings-argumentet på mobilen jag såg: *Visste du att*-kortet i mörk marin ("Din hemförsäkring kan täcka kostnaden för eljour?", `--mobile--10`) — två långa vita textstycken, ingen kr, ingen CTA. Plus FAQ-raden "Täcker försäkringen kostnaden för eljour i Täby?" (`--mobile--11`). **Samma budskap tre gånger, aldrig en enda siffra.**

## Vad ögat möter (desktop)

Från `geo-eljour-taby--desktop--08` (hemförsäkringsvarianten, direkt sett):

1. **Först:** den centrerade rubriken "Sänk kostnaden för din eljour i Täby **genom din hemförsäkring**" — svart-marin bas, teal-gradient på slutfrasen. Kontrasten på den svarta delen är utmärkt; teal-fragmentet (det som säljer) är den svagaste texten i raden.
2. **Andra:** tre stora **numrerade cirklar (1·2·3)** i handritad/skissig teal-ring, sammanbundna av **streckade teal-linjer** — ett stigblock, inte ikoner. Ögat läser "en process i tre steg", inte "så mycket sparar du".
3. **Tredje:** rubrik + brödtext under varje cirkel — "Samtal med expert / Installation av elektriker / Underlag till ansökan". Rena **papperslogistik-etiketter**. Copyn bär synliga fel: "**Vår** experter", "försäkring**b**olaget" (INC-05).
4. **Sist:** den lilla skiss-ring-pillen "**Läs mer om ROT-avdrag**" — fel etikett på ett hemförsäkringsblock (INC-01, P0), lågt visuellt djup men blockets enda klick, och den skickar besökaren ut ur sidan.

Nettot desktop: blocket **lovar pengar i rubriken och levererar en byråkrati-tidslinje**. Siffran som spelar roll (30 %/50 %, och framför allt kronorna) finns ingenstans med visuell tyngd.

---

## Fynd

| ID | Element | Problem (visuellt) | Evidens |
|---|---|---|---|
| **D-INC-1** | H2 teal-gradient-fragment | Värdefrasen ("30 % rot-avdrag"/"genom din hemförsäkring") renderas i lägst kontrast i hela blocket; ~2.8:1 mot vitt, under AA-large 3:1, sämre i gradientens ljusa ände. Mobilen gradientfyller HELA raden (`text-fill:transparent`) → render-risk på äldre Android-WebView som målgruppen använder. | `eljour-taby--desktop--08`; INC-07 |
| **D-INC-2** | De tre cirklarna (1·2·3) | Kommunicerar **process/logistik**, inte matematik. Rubriken frågar "hur mycket sparar jag?", cirklarna svarar "vi ringer, installerar, ansöker". Läses som dekoration. Numren är inte incitamentet — de stjäl blockets fokusyta från kronorna som borde stå där. | `desktop--08`; INC-06 |
| **D-INC-3** | Kronor / talbehandling | **Noll kr någonstans.** Procenttalet lever bara som gradienttext i rubriken — ingen isolering, ingen vikt, ingen "du betalar Y kr". Ingen 50 000-tak. ROT = 30 % av *arbetskostnaden*, men rubrikens "Sänk din elektriker kostnad genom 30 %" antyder 30 % av hela notan (precisions-/candour-risk). | INC-03 |
| **D-INC-4** | "Läs mer"-pillen | Blockets enda interaktiva element är en **utgång** till `/rot-avdrag-2026/` resp. `/gron-teknik-2026/` — sidor **utan formulär** (verifierat round-1). Mitt i utvärderingsfasen (djup 61 %) skickas besökaren från en 2-formulärssida till en 0-formulärssida. | INC-02 |
| **D-INC-5** | Hemförsäkrings-pillen | Etiketten säger "**Läs mer om ROT-avdrag**" på ett block där rubrik + alla tre steg säger *försäkring*. NN/g: länketiketter måste förutsäga målet. På sajtens mest akuta intent (eljour) kostar en felmärkt avfart mest. | `desktop--08`; INC-01, P0 |
| **D-INC-6** | Grammatik i mall | "Vår experter", "försäkringbolaget", särskrivning i varje rubrik ("Sänk din elektriker kostnad", "din laddbox kostnad"). I ett pengar/skatte-sammanhang läser 35–65-publiken det som slarv — exakt där Konsumentverket-diligens signalerar trovärdighet. | `desktop--08`; INC-05 |
| **D-INC-7** | Mobil scroll-vägg | Tre staplade cirkel+rubrik+stycke ≈ 2–3 skärmhöjder icke-klickbar scroll, negativa marginal-hack, dubbla ikon-`<img>` (desktop/mobil) på en sajt redan flaggad ~9–10 s LCP. | INC-06/07 |
| **D-INC-8** | Redundans på eljour | Hemförsäkring förklaras **3 ggr** (stegblock + *Visste du att*-mörkkort + FAQ-rad), aldrig en gång med siffror. Tre block konkurrerar om samma budskap i stället för ett som svarar. | `desktop--08` + `mobile--10` + `mobile--11` |

---

## Omdesign-direktiv (element för element, i fokusordning)

1. **Gör kronorna till blockets hjälte — number-isolation direkt under H2.** Sätt in en **räkne-remsa** som blockets visuella centrum, FÖRE de tre stegen. Talbehandling (återanvänd produktsidornas pris-vokabulär — ordinarie struket → avdrag → slutpris, som redan finns i inventory §24):
   - Rad 1, litet & grått (ap-body, ~16 px, `#5b6472`): "Arbetskostnad, byte av elcentral · **[GAP: X kr ur ampy-foretagsdata]**" — struken eller dämpad.
   - Rad 2, HJÄLTEN: "Du betalar **[GAP: Y] kr** efter ROT" — Outfit, desktop ~clamp(40→60 px), mobil ~34–40 px, midnight #090b32, siffran i teal #00a991 (solid, **inte** gradient). Detta är den enda platsen teal-solid får dominera.
   - Rad 3, finstilt (ap-caption ~13 px): "30 % av arbetskostnaden, upp till 50 000 kr per person och år, dras direkt på fakturan." Fixar precisions-risken i D-INC-3.
   - Alla tal `[GAP]` ur `ampy-foretagsdata` eller flaggade — **aldrig påhittade** (Golden Rule 3).
2. **Lyft värdefrasen ur gradienten.** H2 basfärg midnight #090b32; incitamentsordet i **teal solid #00a991, inte gradientfyll** (AA-large klaras, render-risken på gammal WebView försvinner). Behåll gradienten som accent på max ETT dekor-element, inte på läsbar text (Golden Rule 6: candour ≠ dekor som sänker läsbarhet).
3. **Demotera de tre cirklarna till en tunn trygghets-remsa.** Behåll innehållet (dödar "krånglig ansökan"-invändningen — värdefullt), men krymp: en rad med tre korta chips "① Samtal ② Installation ③ Vi sköter ansökan" i ap-caption, EN delad skiss-ring som signatur i stället för tre tunga cirklar + dubbla ikon-assets. Kronorna får fokusytan; logistiken blir fotnot. Fixar D-INC-2 + D-INC-7.
4. **Döda utgångsknappen — ersätt med inline-mekanik.** Byt "Läs mer om …"-pillen mot en **`Vad gäller avdraget?`-accordion** (innehållet stannar i DOM → SEO bevaras) med samma finstilta mekanik + en textlänk för de få som vill ha djupet. Blocket ska SVARA besökarens fråga *på plats* (HealthSpire), inte navigera bort mitt i tratten. Fixar D-INC-4.
5. **P0 — fixa hemförsäkrings-etiketten (57 eljour-sidor, en mall-edit).** Ta bort "Läs mer om ROT-avdrag"; hemförsäkringsvarianten ska INTE ha en spar-procent (det finns ingen fast %) — den ska ha en **telefon-CTA** ("Ring oss — vi förbereder underlaget till ditt försäkringsbolag"), per blockets egen spec. Fixa "Vår experter→Våra experter", "försäkringbolaget→försäkringsbolaget". Fixar D-INC-5 + D-INC-6.
6. **Mobil: räkne-remsan som ett centrerat kort, stegen som en rad.** Stort tal överst, struket litet ovanför, finstilt under; de tre stegen kollapsar till EN horisontell mini-stepper eller kompakt numrerad lista — kapar ~2 skärmhöjder scroll (D-INC-7). Mobilen är den viktigaste ytan; kronorna ska rymmas ovanför nästa scroll.
7. **Eljour: slå ihop de tre försäkrings-touchpunkterna till ETT svar.** Stegblocket (fixat per Rikt C) blir det enda försäkrings-blocket; *Visste du att*-mörkkortets kärnpoäng flyttas in som en rad, FAQ-raden får peka på blocket. Fixar D-INC-8.

---

## Divergenta riktningar (huvudblock → 3 versioner, husregel)

**Rikt A — "Räknesnurra-först" (service/elektriker, ROT).**
Blocket leds av räkne-remsan som ett litet resultatkort (speglar Ampys egna kalkylatorer → visuell familjekänsla). H2 solid, kronorna som hjälte, tre steg som tunn chips-rad under, ingen utgångsknapp — bara `Vad gäller avdraget?`-accordion. Ett anfört exempel (byte av elcentral) förankrar i sidans faktiska tjänst. Bäst där arbetskostnaden är det stora ankaret. Kräver `[GAP]`-tal.

**Rikt B — "Prisankare bredvid CTA" (laddbox/produkt, Grön Teknik 50 %).**
Komprimera till 2-kolumn: vänster = kr-matematiken (ordinarie struket → efter 50 % Grön Teknik), höger = telefon/formulär-CTA i samma kort. Grön Teknik = 50 % på **arbete och material** (annan mekanik än ROT — copyn måste säga det). Förvandlar incitamentet från dekorativ remsa till en **konverteringsenhet** placerad där priset redan syns (produktsidan gör redan detta rätt, index 3–4). Behåll den ENA skiss-ringen som signatur.

**Rikt C — "Försäkrings-spår" (eljour, hemförsäkring — egen gaffel).**
Sluta tvinga in försäkring i en spar-%-mall. Bygg om till en **"Så får du ersättning"-checklista** i symptomblockets lugna stil (`--mobile--14` som referens): 3–4 teal-outline-ikonrader ("Vi dokumenterar skadan", "Du får underlaget", "Auktoriserad montör = försäkringskrav uppfyllt") + EN grön Ring-CTA ("Ring — vi förbereder underlaget"). Ingen påhittad procent, ingen kr (candour: ersättning är villkorad — säg "kan täcka", `kan`-registret). Slår ihop med *Visste du att*-kortet (D-INC-8) och löser P0-etiketten i samma drag. Den mest akuta, högst konverterande intent-sidan förtjänar det seriösa registret (Golden Rule 6).

---

## Vad som INTE ska röras

- **Trygghets-innehållet i de tre stegen** (samtal → installation → ansökan) — det dödar "krånglig ansökan"-invändningen. Demotera, radera inte.
- **De candour-rena påståendena:** fakturamodellen ("skickar in ansökan till Skatteverket åt dig"), hemförsäkringens ärliga tredje steg ("skickar över underlaget till dig för din försäkringsansökan"). PASS round-1 — behåll ordagrant.
- **Ränte-/procent-kanon:** 30 % ROT / 50 % Grön Teknik är korrekt på varje sampel. Rör inte talen; lägg bara till kronor och tak runt dem.
- **Den handritade skiss-ringen som EN signatur-enhet** — den är särpräglad och on-brand. Multiplicera den inte (tre tunga cirklar), destillera till en.
- **Teal + Outfit + midnight-tokens.** Byt bara *var* teal används (solid på siffran, inte gradient på läsbar rubriktext) — inte paletten.
- **Ingen urgency/scarcity** införs (candour-grinden). Kronorna och taket är övertygande nog; de behöver ingen nedräkning.
