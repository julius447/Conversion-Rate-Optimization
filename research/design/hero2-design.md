# Hero_2 + `.aof`-formulär — DESIGN-audit (round 2)

Scope: den mest använda hjälten på sajten (260 sidor, block-index 1 på alla). Round-1-strukturfynden (H2-01…H2-10 i `research/blocks/hero2-form.md`) är KONTEXT — den här filen tittar på pixlarna: vikt, kontrast, trängsel, vad ögat landar på, och om det matchar sidans jobb. Auditerade tiles: `svc-elcentral`, `svc-vitvaror`, `geo-elektriker-tyreso`, `geo-laddbox-nacka`, `b2b-brf` (mobil 01–02, desktop 01–02).

Fem sidor, ETT block. Enda variablerna: eyebrow, H2, paragraf, och om formuläret har låst "Vad gäller arbetet?"-select (service-sidor har den; `geo-elektriker-tyreso` saknar den → ett fält kortare). Allt annat — mörk navy-hjälte, två CTA, 5.0-rad, formkort — är identiskt pixel för pixel. Det betyder: en design-fix träffar 260 sidor samtidigt.

---

## Vad ögat möter (mobil, 390px)

Jag läser tre skärmar innan formuläret ens är ifyllbart. Det är sjukdomen i ett nötskal.

**Skärm 1 (tile 01, alla fem sidor):** Ljus header (`#f5f9ff`) med svart ampy-logga + grön "Gratis rådgivning"-pill (med lysande grön prick) + hamburgare. Sedan slår ett **stort mörkt navyfält** in och tar resten av vyn. I ordning uppifrån: liten grå breadcrumb ("Hem › Elcentral") → **grön gradient-eyebrow** ("Byta elcentral", ~22px) → **stor vit/grön H2** ("Ny elcentral installerad med 30% ROT-avdrag", ~44px, tar 2 rader) → 4–6 rader vit brödtext → **grön gradient-CTA** "Kostnadsfri rådgivning" (full bredd, med ↗-pil) → **ljusblå CTA** "Ring 010-265 79 79" (full bredd, vit telefon-chip höger) → **teal "5.0 ★★★★★"-rad** med Google-G. Längst ner skymtar formkortets rubrik "Få kostnadsfri rådgivning!".

Vad DOMINERAR första glimten: den stora vita H2:n vinner klart — bra. Men näst starkast är den **gröna CTA-knappen**, inte formuläret (formuläret är inte ens i vyn). Den gröna knappen är visuellt tyngst av alla interaktiva element, och den leder BORT till `/kontakt/` (H2-01). Ögats andra fixpunkt är alltså den enda tumnära handlingen som lämnar sidan — och den utlovar exakt vad formuläret 1,5 vy längre ner levererar.

**Skärm 2 (tile 02, alla fem sidor): tomfälts-väggen.** Hela vyn är formkortet: Privat/BRF/Företag-toggle överst (Privat ljusblå-markerad) → på service-sidor "Vad gäller arbetet? [Elcentral ▾]" (förifyllt/låst) → **fem stora tomma vita fält på rad**: Namn, Telefonnummer, E-post, Adress, Postnummer → streckad "Fler detaljer (valfritt) ▾" → GDPR-checkbox → **mint-grön gradient-submit "Boka rådgivning"**. På `geo-elektriker-tyreso` saknas selecten, så väggen börjar direkt på Namn — fyra tomma fält istället för fem, men fortfarande en hel vy av vita rektanglar.

Detta är precis det brief:en varnar för: **en full mobil-vy av blanka inputs innan ett enda värdeargument eller en enda bild.** De vita fälten lyser hårdast på hela sidan (maximal ljus-mot-mörk-kontrast) — så det första ögat "läser" om formuläret är dess ARBETE, inte dess belöning. Fält-räkningen (Baymard, H2-04) drabbar dubbelt: den upplevda svårigheten sätts av hur många tomma fält som syns samtidigt, och här syns alla fem på en gång utan progressiv avslöjning.

**Skärm 3 (tile 03):** Först här kommer innehåll — testimonials ("Vad säger dina grannar om Ampy?") och, på elcentral, en riktig bild av en elcentral längst ner. Servicebesökaren som var nyfiken på *tjänsten* får se tjänsten först på tredje skärmen.

**b2b-brf-avvikelse (tile 01):** paragrafen är 6 rader (längst av alla), vilket trycker CTA:erna och 5.0-raden ännu längre ner — formrubriken hamnar först vid vyns absoluta botten. Paragraflängden styr direkt hur djupt formuläret begravs; den är oreglerad.

## Vad ögat möter (desktop, 1440px)

**Split (svc-elcentral/vitvaror desktop 01):** Klassisk 2-kolumn inuti ett stort mörkt navy-rundat kort. **Vänster ~55%:** breadcrumb → grön eyebrow → stor H2 (nu 2 rader, ~48px) → paragraf (2–3 rader) → **två CTA sida vid sida** (grön "Kostnadsfri rådgivning ↗" + ljusblå "Ring 010-265 79 79") → liten "G 5.0 ★★★★★"-rad. **Höger ~40%:** formkortet, något ljusare navy-blå-glas mot den mörkare hjältebakgrunden, med rubrik + toggle + select + Namn + Telefon/E-post (2-kol) + Adress/Postnummer (2-kol) + Fler detaljer + GDPR + mint submit.

Vad dominerar: blicken landar på H2 vänster, hoppar sedan till **formkortets ljusare massa höger** — bra, formuläret vinner på desktop eftersom det är en avgränsad ljusare yta. Men två defekter syns direkt:

1. **Stor död yta nere till vänster.** Under CTA/5.0-raden är hela nedre vänstra kvadranten tom mörk navy — inget innehåll, ingen bild, inget. Formkortet höger är högre än textkolumnen vänster, så vänsterspalten "tar slut" på mitten och lämnar ~35% av hjälten som svart tomrum. Ingen bild av tjänsten fyller den (elcentral, tvättmaskin, laddbox) — den mest övertygande visuella tillgången saknas helt.
2. **Mörkt-på-mörkt (H2-06).** Formkortet (blåtonad navy) sitter på hjälten (mörkare navy-aurora). Kontrasten kort↔bakgrund är svag; kortet "flyter" utan tydlig kant. Den grå underrubriken "Vår behöriga elektriker återkommer via telefon!" och fältlabels är låg-kontrast grå mot navy.

**geo desktop 01/02: hjälten renderade BLANKT** (bara header, resten ljusblå tom yta). Det är en lazy-load/LCP-artefakt men den bekräftar H2-07 skarpt: formuläret (och hela hjälten) är JS-injicerat och sist att måla. På ett verkligt lab-LCP ~9–10s betyder det att en betald besökare stirrar på en tom ljusblå ruta under exakt de sekunder hen bestämmer sig för att stanna (Clarity: 1s-studs på Vitvaror). **Money-blocket är osynligt vid first paint.**

---

## Fynd (design-lagret; kompletterar H2-01…H2-10)

| ID | Element | Problem (design) | Evidens |
|---|---|---|---|
| **D-01** | Grön CTA vs formkort | Grön gradient-knapp är sidans tyngsta interaktiva element och vinner ögats andra fixpunkt — men leder till `/kontakt/`, bort från det identiska formuläret intill. Färgvikt kämpar mot konverteringsjobbet. | tile 01 alla 5 sidor; H2-01 |
| **D-02** | Tomfälts-väggen (mobil tile 02) | Hela vyn = 4–5 tomma vita fält, maximal kontrast mot navy → ögat läser formulärets ARBETE, inte belöning. Ingen progressiv avslöjning; all fält-massa exponeras på en gång. | tile 02 alla 5; Baymard fält-antal; H2-04 |
| **D-03** | Hjältens döda nedre-vänstra kvadrant (desktop) | ~35% av hjälten är tom svart navy under vänsterspalten. Ingen tjänstebild fyller den. Premiumkänsla tappas; ingen visuell bekräftelse på tjänsten. | desktop 01 elcentral/vitvaror |
| **D-04** | Ingen tjänstebild någonstans i hjälten | 260 sidor visar en tjänst (elcentral/vitvara/laddbox/BRF) men hjälten har noll bild av den. Servicebesökaren ser tjänsten först på skärm 3. | alla tiles; owner-hypotes |
| **D-05** | Mörkt-på-mörkt kortkant + grå microtext | Formkort (blå-navy) på hjälte (navy-aurora) — svag kant, kortet flyter. Underrubrik + labels låg-kontrast grå. | desktop 01; mobil 02; H2-06 |
| **D-06** | Tre gradient-knappar tävlar i färg | Grön gradient (CTA) + blå gradient (Ring) + mint gradient (submit "Boka rådgivning") — tre olika lysande gradienter i samma block. Ingen färg äger "handlingen"; ögat vet inte vad som är primärt. | tile 01+02 alla 5 |
| **D-07** | 5.0-raden som fokustjuv (mobilens MainCTA-lärdom applicerad) | Teal "5.0 ★★★★★" sitter mellan CTA-paret och formkortet och bryter det visuella flödet CTA→form; den är dessutom oankrad (ingen räknare) = candour-risk på 260 sidor. | tile 01 alla 5; H2-05 |
| **D-08** | H1/H2-inversion syns i vikt | Den gröna eyebrow:n ("Byta elcentral") ÄR sidans H1 men renderas som liten label; den stora rubriken är H2. Visuell hierarki och dokumenthierarki pekar åt olika håll. | alla tiles; H2-03 |
| **D-09** | Paragraflängd oreglerad → varierande begravningsdjup | b2b-brf 6 rader vs vitvaror 3 → CTA/form sjunker olika djupt per sida. Ingen max-höjd på hjältetexten. | b2b-brf tile 01 vs vitvaror tile 01 |
| **D-10** | Kundtyp-toggle är första interaktiva elementet i formuläret | Privat/BRF/Företag möter besökaren före Namn; 90%+ är Privat (redan default) → ett onödigt beslut överst. På service-sidan följs den direkt av en LÅST select (Elcentral) — två "kontroller" innan första riktiga inmatningen. | tile 02; H2-08 |
| **D-11** | Money-blocket målas sist / blankt | Geo desktop-tiles renderade tom hjälte (JS-injicerad form). Vid LCP ~9–10s är formuläret osynligt när besökaren bestämmer sig. | geo desktop 01/02; H2-07 |

---

## Omdesign-direktiv (konkret, i prioritetsordning)

1. **Dela hjälten efter INTENT, inte en mall för alla 260.** Två klasser:
   - **Service-sidor (`/elservice/*`, elcentral, vitvaror, belysning…):** besökaren är NYFIKEN PÅ EN TJÄNST. Ge tjänste-bild-hjälte, EN CTA, INGET formulär i hjälten (se Riktning A). Formuläret flyttar ner till det befintliga MainContact-blocket.
   - **Geo/kommersiella sidor (`elektriker-i-{ort}`, `laddbox-i-{ort}`, `eljour-i`, `elinstallation-i`, `elektriker-för-X`):** besökaren är KÖPREDO. Behåll form-i-hjälte men komprimerad (se Riktning B).
2. **Döda färgkonkurrensen (D-06).** Endast EN gradient får äga "handlingen" per hjälte. På form-hjälten: submit-knappen ("Boka rådgivning") är den enda mint-gröna gradienten; "Ring" blir en lugn sekundär (ghost/outline, inte lysande blå gradient); den gröna "Kostnadsfri rådgivning ↗"-knappen tas BORT från form-hjältar (den dumpar besökaren på /kontakt/ = samma sak, D-01/H2-01).
3. **Bryt tomfälts-väggen (D-02).** Rendera bara 3 fält synligt först (Namn, Telefon, Postnummer — minsta kvalificerande lead), resten (E-post, Adress) i ett "Fler uppgifter"-steg eller under first fold. Ta bort den låsta "Vad gäller arbetet?"-selecten från synligt läge på service-sidor (den är förutbestämd av URL:en — visa den som en liten låst chip "Gäller: Elcentral", inte en full dropdown). Flytta Privat/BRF/Företag-toggeln till efter Namn eller göm den bakom default Privat (D-10).
4. **Fyll den döda kvadranten + ge tjänstebild (D-03/D-04).** Varje hjälte får en riktig installationsbild av den faktiska tjänsten (elcentral öppen med moderna automatsäkringar; tvättmaskin inkopplad; laddbox på fasad; BRF-trapphusbelysning). På form-hjältar: bilden fyller nedre vänstra kvadranten som bakgrund bakom texten (mörk overlay bevarar läsbarhet). På service-hjältar: bilden ÄR höger kolumn.
5. **Höj formkortets kant och microtext-kontrast (D-05).** Ge kortet en ljusare glas-yta + 1px teal-kant + tydligare skugga så det lyfter från hjälten. Höj underrubrik och labels från grå till minst `#c9d4e0` (WCAG AA mot navy).
6. **5.0-raden: flytta eller demotera (D-07).** Ta bort den mellan CTA och form (den bryter flödet). Antingen (a) flytta den in i formkortets sidfot som liten trust-rad precis ovanför submit ("★★★★★ · Betyg på Google" MED räknare — candour kräver ankare), eller (b) ersätt med "behörig elektriker · F-skatt · ROT direkt på faktura"-mikrotrust som är mer relevant vid formuläret. Aldrig oankrad "5.0".
7. **Fixa vikt-inversionen visuellt (D-08).** Behåll den gröna eyebrow:n liten men gör den till en riktig kicker (versal-spärrad, mindre) så det är tydligt att den är kategori-label; den stora rubriken bär budskapet. (SEO-H1/H2-taggning löses separat i seo-guard — här handlar det om att ögat inte ska förvirras.)
8. **Klipp hjältetextens höjd (D-09).** Max 3 rader paragraf i hjälten; överskott flyttar till content-blocket. Standardiserar begravningsdjupet över 260 sidor.
9. **SSR formskalet (D-11/H2-07).** Server-rendera kort-chrome + rubrik + de 3 första fälten i Bricks; låt JS hydrera URL-resolvern. Minst en statisk skelett så slotten SYNS som "ett formulär" vid first paint.

---

## Divergenta riktningar (3 hjälte-redesigns)

Alla tre delar: bevarad ampy-token-palett (teal `#00a991`, midnight `#090b32`, Outfit), candour-grind (ingen oankrad 5.0, ingen fejk-brådska), två konverteringsvägar (ring/formulär), du-tilltal.

### Riktning A — Service-bild-hjälte, EN CTA, inget formulär (ägarens hypotes)
**För:** service-sidor (`/elservice/*`: elcentral, vitvaror, belysning) där intent = nyfiken på en tjänst.

**Element-lista:**
- Behåll mörk navy-hjälte men **split 50/50 med riktig bild** höger (desktop) / överst (mobil).
- Vänster: breadcrumb → grön kicker-eyebrow (liten) → stor H2 ("Ny elcentral installerad med 30% ROT-avdrag") → 2-raders paragraf → **EN primär CTA** "Få kostnadsfri rådgivning ↗" (mint gradient, leder till MainContact-ankaret längre ner på SAMMA sida, inte /kontakt/) → under den en lugn sekundär textlänk "eller ring 010-265 79 79" (ghost, telefonikon). → liten trust-rad: "Behörig elektriker · ROT 30% direkt på fakturan".
- Höger: **fotografi av den faktiska tjänsten** — öppen elcentral med moderna automatsäkringar (elcentral-sidan) / inkopplad tvättmaskin i badrum (vitvaror). Rundade hörn, teal-kant, mjuk skugga. Ingen text ovanpå.
- Formuläret: BORT från hjälten → besökaren möter formuläret först i det befintliga MainContact-blocket längre ner, EFTER content-block + testimonials som svarar på frågorna (MECLABS HealthSpire: längre sekvens, mer värde före ask).

**Mobil stack-ordning:** header → tjänstebild (16:9, ~40vh) → grön kicker → H2 → paragraf → EN mint CTA (full bredd) → "eller ring …" textlänk → mikrotrust-rad → (scroll) content-block → testimonials → MainContact-form.

**Desktop split:** vänster 50% text+1 CTA, höger 50% tjänstebild. Ingen död kvadrant (bilden fyller höger, texten centreras vertikalt vänster).

**Vad dominerar första glimten & varför:** Bilden av tjänsten + H2. Det matchar intent: en besökare på "vitvaror" vill VETA att Ampy gör detta tryggt — visa jobbet, inte en tom blankett. Den enda CTA:n har inga rivaler, så all uppmärksamhet kanaliseras till ett ask. Detta är exakt ägarens 5.0-rad-logik uppskalad: ta bort det som stjäl fokus (formulär + 2 extra CTA + 5.0-rad) → tjänsten + en handling blir hela fokuset.

### Riktning B — Kompakt-form-hjälte (3 fält SSR, ring sekundär) — visuellt förfinad
**För:** geo/kommersiella sidor (`elektriker-i-{ort}`, `laddbox-i`, `elinstallation-i`, `elektriker-för-X`) där intent = köpredo.

**Element-lista:**
- Behåll 2-kolumn navy-hjälte men **fyll nedre vänstra kvadranten med en dämpad tjänstebild-bakgrund** (mörk overlay 70%) så den döda ytan försvinner.
- Vänster: breadcrumb → grön kicker → H2 ("Boka en pålitlig elektriker i Tyresö!") → **max 2 raders** paragraf → EN sekundär "Ring 010-265 79 79" (ghost/outline med telefon-chip — INTE lysande blå gradient). Ingen grön /kontakt/-knapp.
- Höger: **förfinat formkort** — ljusare glas-yta, 1px teal-kant, tydlig skugga (lyfter från hjälten, löser D-05). Innehåll SSR:at:
  - Rubrik "Få kostnadsfri rådgivning" + underrubrik i AA-kontrast.
  - Låst service som liten chip "Gäller: Laddbox" (inte dropdown) på sidor där URL bestämmer tjänsten; på ren elektriker-i visas ingen chip.
  - **Endast 3 synliga fält:** Namn, Telefonnummer, Postnummer. Under dem: "Fler uppgifter (e-post, adress) →" som avslöjar E-post/Adress vid behov.
  - Privat/BRF/Företag: default Privat, flyttad under fälten som liten segment-kontroll (bara den som är B2B klickar).
  - Mint submit "Boka rådgivning" — enda gradienten i hela blocket.
  - Formkortets sidfot: "★★★★★ · X omdömen på Google" (ankrad räknare) ELLER "Behörig · F-skatt · ROT på faktura".

**Mobil stack-ordning:** header → grön kicker → H2 → 2-raders paragraf → "Ring …" ghost-länk → formkort (3 fält, mint submit) → mikrotrust. Formuläret når tummen inom ~1,3 vy istället för 2+, och ingen tomfälts-vägg (3 fält, inte 5).

**Desktop split:** vänster 45% text + ghost-ring, höger 55% formkort. Bakgrundsbild fyller vänster botten.

**Vad dominerar & varför:** Formkortet (ljusare massa, teal-kant) på desktop; på mobil H2 → kompakt formkort direkt. Matchar köpredo intent: geo-besökaren sökte "elektriker i Tyresö" och vill boka — ge dem det minsta möjliga formuläret omedelbart, med ring som lugn backup. Tre fält sänker upplevd svårighet (Baymard) och submit-gradienten är oomtvistad.

### Riktning C — "Prata med en elektriker på 60 sekunder": samtals-först hjälte (min egen)
**För:** en argumenterad tredje väg, primärt för `eljour-i` (akut) men testbar på alla geo-sidor. Rationale: Ampys starkaste och snabbaste konvertering är samtalet (MainCTA-blocket "Prata med en elektriker inom 60 sekunder" är enligt ägaren potentiellt mycket starkt), och för akut/köpredo intent är ett telefonsamtal lägre friktion än ett formulär. Unbounce: repair/urgent-sidor konverterar långt bättre — så led med samtalet där brådskan är äkta.

**Element-lista:**
- Navy-hjälte, **centrerad enkolumn** (ingen split, ingen död kvadrant).
- Breadcrumb → grön kicker → stor H2 ("Elektriker i Tyresö — vi svarar nu") → 1-raders paragraf.
- **Dominant primär: en stor ring-knapp** — mint gradient, telefon-chip, "Ring 010-265 79 79", med undertext "Vi svarar oftast inom 60 sekunder" (candour: "oftast", inte garanti). Detta är hjältens tyngdpunkt.
- Under den, en lugn sekundär: **"Föredrar du att vi ringer dig? →"** som avslöjar det kompakta 3-fälts-formuläret inline (progressive disclosure) — formuläret finns men är opt-in, inte en vägg.
- Mikrotrust-rad under: "Behörig elektriker · Jour dygnet runt · ROT på faktura" (byts per sidtyp).
- Bakgrund: dämpad bild (elektriker vid elcentral / servicebil) med mörk overlay — fyller hela hjälten, ingen tom yta.

**Mobil stack-ordning:** header → grön kicker → H2 (kort) → 1-raders paragraf → STOR mint ring-knapp (full bredd, sticky-kandidat) → "Vi svarar oftast inom 60 sek" → "Föredrar du att vi ringer dig? →" (fäller ut 3 fält) → mikrotrust. Tumnära handling = RING, som stannar i konverteringen (till skillnad från dagens gröna /kontakt/-detour).

**Desktop:** centrerad ~720px kolumn på fullbredds bakgrundsbild; ring-knapp centralt dominant; formulär utfällbart under.

**Vad dominerar & varför:** Ring-knappen, entydigt. Matchar akut/köpredo intent där samtalet är den snabbaste, lägsta-friktions-konverteringen och där Ampy redan har ett starkt samtals-erbjudande. Formuläret degraderas till opt-in men försvinner inte — vi tvingar inte fram en tomfälts-vägg, vi erbjuder den som val. Detta är den enda riktningen som gör Ampys starkaste tillgång (det snabba samtalet) till hjältens tyngdpunkt.

**Argument för C över status quo:** dagens hjälte har tre asks och den tumnära handlingen lämnar sidan; C har ett dominant ask (ring, stannar i konverteringen) + ett frivilligt (form). För eljour är detta message-match rakt av; för övriga geo är det ett A/B-värdigt alternativ till B.

---

## Vad som INTE ska röras (skydda det som funkar)

- **H2:ns storlek och vit/grön gradient-behandling** — den vinner första glimten korrekt på alla fem sidor; den är läsbar, självsäker, on-brand. Rör inte skalan.
- **Den mörka navy-hjälten som yta** — den är premium och särskiljande; problemet är tomrummet OCH bristen på bild i den, inte färgen. Behåll navy; fyll den.
- **Mint-gradient-submitknappen "Boka rådgivning"** — den är sidans starkaste färgsignal och SKA förbli den enda handlings-gradienten. Rör inte dess färg; ta bort rivalerna runt den istället.
- **Per-sida förifylld/låst service** (Elcentral/Vitvaror i selecten) — smart message-match-mekanik; behåll logiken, ändra bara presentationen (chip istället för dropdown).
- **Kicker→H2→paragraf-copyn i ampy-röst** — copyn är candour-ren och du-tilltalande ("Dags att byta ditt gamla proppskåp?"); den är bland det bättre på sajten. Endast paragraflängden ska kapas, inte tonen.
- **Att geo-formuläret saknar service-selecten** — det är rätt (tjänsten är obestämd på en ren elektriker-i-sida); behåll den skillnaden.
- **Ring-numret 010-265 79 79 som permanent synlig konverteringsväg** — ska aldrig försvinna; den ändras bara från lysande blå gradient till en lugnare sekundär vikt så submit/ring inte tävlar.
