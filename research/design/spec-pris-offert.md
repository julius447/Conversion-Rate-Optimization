# Pris & offert-blocket — fullständig designspec

Round-1 döpte detta till programmets **#1 nya block** (`missing/block-pris-offert.md`, status BUILD, P0, prioritetstal 1 206–2 223). Round 1 bevisade JOBBET och POSITIONEN; det här lagret ger blocket dess **utseende** — zon för zon, token för token, tills en Bricks-byggare kan resa det utan en enda fråga.

**Anti-teater — vad jag faktiskt SÅG (inte narrativ):**
- **Direkt sett, renderat:** Hero_2 på `svc-elcentral--mobile--01/02` + `--desktop--01` — den mörka marinblå hjälten som blocket ska ligga **direkt under** (slot 3). H2 "Ny elcentral installerad med 30% ROT-avdrag", två CTA:er, teal "5.0 ★★★★★"-rad, och en `.aof`-formulärskort. **Ingenstans i hela hero:n står en enda krona.** En besökare från "byta elcentral pris" möter ett löfte om ROT men inget pris.
- **Direkt sett:** produktmallens prisblock (`prod-sigenstor--mobile--13`): "Totalt / **Fr. 69 000 :-**" med "Ordinarie pris **138 000 .=**" (genomstrykningen korsar `:-` → glyfdefekt), "Inklusive installation | Ja", "Grön teknik | 50%", ljust cyan "Få skräddarsydd offert →". Detta är den prismodul jag resonerar EMOT nedan.
- **Direkt sett:** att där priset FAKTISKT bor idag på tjänstesidan är begravt i FAQ:n långt ner (round-1 verifierade live: *"Att installera en ny elcentral kostar vanligtvis mellan 6 000 och 12 000 kronor efter ROT-avdrag"*, `blocks/faq.md` rad 23, kollapsad accordion vid 30–50 % scrolldjup). `svc-elcentral--desktop--08` visar området strax innan FAQ/kartan — ren SEO-text, inget pris med tyngd.
- **Inte direkt sett:** blockets egen rendering (det existerar inte ännu). Allt nedan är en byggspec, inte en observation — men förankrad i det jag såg och i round-1:s live-hämtade siffror.

---

## Vad ögat möter idag (mobil) — problemet blocket löser

På `svc-elcentral--mobile--01` möter ögat, uppifrån: grön "Gratis rådgivning"-pill i headern → mörk marin hero → teal eyebrow "Byta elcentral" → stor vit H2 "Ny elcentral installerad **med 30% ROT-avdrag**" (sista frasen i teal-gradient) → paragraf → grön "Kostnadsfri rådgivning"-knapp → ljusblå "Ring"-knapp → teal "5.0 ★★★★★" → formulärkortet börjar (`--mobile--02`: kundtyp-toggle → "Vad gäller arbetet? Elcentral" → Namn → Telefon → E-post → Adress → Postnummer → GDPR → "Boka rådgivning"). **Sex vertikala skärmhöjder passerar innan besökaren ser ett pris — och den kommer aldrig, förrän FAQ:n långt nere.** Ordet "pris" som lockade in klicket besvaras aldrig ovanför formuläret. Det är precis den läckan (MECLABS message-match: ad → H1 → **first screen**) blocket täpper.

## Vad ögat möter idag (desktop) — samma tomrum

`svc-elcentral--desktop--01`: 2-kolumns hero, vänster textkolonn (eyebrow → H2 → paragraf → CTA-par → 5.0-rad), höger `.aof`-formulärkort. Marinblått kort på ljus botten. Ögat landar på formuläret (ljusast, tätast) och på H2. **Priset finns inte i synfältet** — det bor i FAQ:n vid ~35 % djup (`--desktop--08`-området och nedåt). Byggahus/Konsumentverket-ankaret säger att slutpris-överraskning är husägarens #1-oro; sidan svarar på den oron sist, efter att beslutet att studsa redan fattats.

---

## Designprincip (blockets ENDA jobb)

Blocket ska, på ≤1 mobilskärm direkt under Hero_2, säga tre saker i sjunkande storlek:
1. **VAD det kostar** (det redan publicerade intervallet — hjälten).
2. **ATT priset är fast i offerten** (Konsumentverket-normen, gjord explicit — dödar slutpris-oron).
3. **HUR avdraget räknas** (ett verkligt kr-exempel — gör intervallet trovärdigt), + **en** micro-CTA till formuläret på sidan.

Det ska läsa som **information, inte försäljning**: ljus yta (vit/`#f5f9ff`), inget mörkt band, ingen gradient på läsbar text, ingen urgency. Kontrast-rytm: den mörka Hero_2 → detta ljusa lugna kort ger välkommen visuell lättnad och signalerar "nu talar vi rakt".

---

## Anatomi — desktop (1440)

Ett **enda ljust kort**, full innehållsbredd (matchar Hero_2:s container-bredd, ~1180 px inuti sidmarginalen), `--apradius-l` (16→20px), `0 2px 6px #bebebe` skugga, bakgrund vit på `#f5f9ff`-sektion. Inre padding `--apspace-xl` (~25→56px). Kortet är **lågt** — en horisontell remsa, inte en sektion; höjd ~ 260–300 px.

Layout: **12-kolumns, delad 7 / 5** (två zoner sida vid sida, tunn vertikal avdelare `--apgray-white` 1px mellan):

**Zon A (vänster, ~7 kol) — Prisintervallet (hjälten):**
```
[eyebrow]   VAD KOSTAR DET?            ← --aptext-s (12→14), Outfit 600, letter-spacing .04em,
                                          --apteal-core, versal-tracking (eyebrow-manér)
[H2]        Byte av elcentral kostar   ← --aptext-l (18→28), Outfit 500, --apmidnight-blue,
            vanligtvis                    lh 1.2 — sätter kontexten, INTE hjälten
[PRISRAD]   6 000–12 000 kr            ← SE "Prisintervallets typografi" nedan — det STÖRSTA
                                          elementet i hela blocket
[qualifier] efter 30 % ROT-avdrag       ← --aptext-m (17→18), Outfit 400, --apcharcoal-gray,
            på arbetskostnaden            direkt under prisraden, vänsterställd
```

**Zon B (höger, ~5 kol) — Löfte + exempel + CTA, staplade:**
```
[löfteskort]  ✓ Fast pris i offerten    ← se "Fast-pris-löftet" nedan
              innan arbetet påbörjas.
              Inga överraskningar på
              fakturan.
[exempel]     ▸ Se ett räkneexempel      ← inline-accordion (öppnar NEDÅT, stannar i DOM)
                                            → avdragsstege (se "Worked ROT-exempel")
[micro-CTA]   Få ditt exakta pris →      ← EN länkknapp, ankarscroll till #hero-form
```

Ögonordning desktop, avsiktlig: **prisintervallet (störst, teal-siffror) → fast-pris-löftet (grön bock) → micro-CTA (teal)**. Ingen andra ask, inget telefonnummer här (det bor i hero + main-cta), ingen 5.0-rad (den stjäl fokus — samma lärdom som ägarens MainCTA-frö och `product-design.md` PD-9).

## Anatomi — mobil (390 / 780px tile)

Zonerna **staplas** (A ovanför B), hela blocket ska rymmas inom ~1,2 skärmhöjd så prisintervallet ligger i eller precis under första skärmen efter hero:

```
┌──────────────────────────────────────┐
│  VAD KOSTAR DET?          (eyebrow)   │  --apspace-m padding runt
│                                        │
│  Byte av elcentral kostar vanligtvis   │  H2, --aptext-l, midnight, centrerad-vänster
│                                        │
│      6 000–12 000 kr                   │  PRISRAD — --aptext-2xl (22→48), centrerad
│      efter 30 % ROT-avdrag             │  qualifier --aptext-s, --apcharcoal-gray
│  ──────────────────────────────────    │  1px --apgray-white avdelare
│  ✓  Fast pris i offerten innan vi      │  löfteskort, --aptext-m, midnight,
│     börjar. Inga överraskningar.        │  grön bock --apteal-core, vänster
│                                        │
│  ▸  Se ett räkneexempel                │  accordion, kollapsad default
│                                        │
│  [   Få ditt exakta pris  →   ]        │  micro-CTA, full bredd, teal outline-knapp
└──────────────────────────────────────┘
```

Mobilkortet: `--apradius-l`, vit på `#f5f9ff`, padding `--apspace-m` (16→28), zonavstånd `--apspace-s`. Prisraden **centrerad** på mobil (ensammast, störst tyngd); allt annat vänsterställt. Kortet får aldrig kräva en horisontell scroll — prisintervallet sätts med `white-space: nowrap` men i `--aptext-2xl` som ryms på 390px (48px max endast desktop; på 390 landar clampen ~30–34px, mätt).

---

## Prisintervallets typografi (ägarens altitud — det bärande elementet)

Detta är blockets "5.0-rad borttagen så CTA-knappen blir hela fokuset"-moment: **intervallet måste vara det ohotat största, mest kontrastrika elementet i blocket**, och de två talen måste läsas som två ändpunkter, inte en enda sifferklump.

```
6 000 – 12 000 kr
└─siffror─┘   └─┘
   HJÄLTE     suffix
```

| Del | Token / värde | Detalj |
|---|---|---|
| Siffrorna `6 000` / `12 000` | Outfit **600**, `--aptext-2xl` desktop (22→**48**), mobil landar ~30–34px | `--apmidnight-blue` bas; **kr-beloppens siffror i `--apteal-core` SOLID** — aldrig gradient (lärdom `incentive-design.md` D-INC-1: gradient sänker värdefrasen till lägst kontrast + WebView-render-risk på 35–65-publikens gamla Android). Teal solid #00a991 klarar AA-large mot vitt först vid ~28px+ — därför är **stor storlek en tillgänglighetsgrind, inte bara stil**. Sätt `font-variant-numeric: tabular-nums` så tusentalen linjerar. |
| Tankstreck `–` | en-dash (U+2013), **inte** bindestreck | `--apmidnight-blue` vid **40 % opacitet** (`--apdarkest-black-40`-manér), `--aptext-xl`, med hårspaces (` `) runt → separerar ändpunkterna visuellt så "6 000" och "12 000" läses som spann |
| `kr`-suffix | Outfit 500, `0.55em` av siffrornas storlek, `--apmidnight-blue` (ej teal) | står som `kr`, aldrig `:-` (undviker produktsidans `.=`-glyfdefekt, PD-3); baseline-alignad mot siffrornas underkant |
| Prefix `vanligtvis` | flyttas upp i H2-raden ("kostar vanligtvis"), INTE inne i prisraden | håller prisraden ren; hedge-ordet bär candour-kravet (round-1: "vanligtvis mellan …") |
| Qualifier-rad `efter 30 % ROT-avdrag på arbetskostnaden` | `--aptext-m` (17→18) desktop / `--aptext-s` mobil, Outfit 400, `--apcharcoal-gray` | fixar precisions-/candour-risken (INC/PD): ROT är 30 % av **arbetskostnaden**, inte hela notan. Denna rad får ALDRIG utelämnas. |

**Regeln som bites:** teal-solid får dominera på siffrorna och **ingen annanstans i blocket**. Eyebrow är teal men liten; micro-CTA är teal outline. Om två teal-element tävlar om first-glance har blocket misslyckats — intervallet ska vinna varje gång.

**Timme-varianten** (elektriker-geo): `650–950 kr/timme` med `/timme` i suffix-storlek (`0.55em`, midnight), qualifier-rad "efter ROT + startavgift för servicebil". Samma typografi-regel.

---

## Fast-pris-löftet (treatment)

Konsumentverket-normen gjord synlig — den enskilt starkaste ångest-dämparen (Byggahus: slutpris-överraskning = #1-oro). Behandling som ett **litet lugnt löfteskort**, inte en säljruta:

- Layout: en rad med **grön bock-ikon** (`--apteal-core`, 20px, tunn outline-stil — samma vikt som eljour-symptomblockets ikoner, den lugnaste ikonlistan på sajten enligt `incentive-design.md`) + text till höger.
- Text: **"Fast pris i offerten innan arbetet påbörjas — inga överraskningar på fakturan."** `--aptext-m`, Outfit 400, `--apmidnight-blue`. Nyckelorden "Fast pris i offerten" i Outfit 600 (vikt-lyft, inte färg-lyft — undviker en andra teal).
- Ingen ram, ingen fyllnad, ingen skugga — bara ikon + text på kortets vita yta, avgränsad från prisintervallet med en 1px `--apgray-white`-linje.
- **Candour-grind:** frasen "fast pris i offerten" får ENDAST renderas på verticals där offerten genuint är fast. På timdebiterade sidor (elektriker löpande) byts den mot **"Tydlig prisbild innan vi börjar — du godkänner alltid innan arbetet startar."** (PIL-08-kollisionen "Alltid fasta priser" vs "600–900 kr/tim" får inte återuppstå.) ACF-fält `pris_loftestyp: fast | löpande` styr vilken sträng som renderas.

---

## Worked ROT-exempel (integration)

Gör intervallet trovärdigt genom att visa **ett** verkligt genomräknat exempel — och gör det utan att skicka besökaren någonstans. Renderas som en **inline-accordion** ("▸ Se ett räkneexempel"), kollapsad default, som öppnar nedåt och **stannar i DOM** (SEO-substans bevaras; ingen utgång — lärdom `incentive-design.md` D-INC-4: blocket ska SVARA på plats, inte navigera bort mitt i tratten).

Öppnat innehåll = **avdragsstege** (återanvänder den ärliga stegen från `product-design.md` direktiv 1, som ägaren redan efterfrågat):

```
Exempel: byte av elcentral i villa
Arbetskostnad                    [GAP: X] kr      ← --aptext-m, --apcharcoal-gray
– ROT-avdrag (30 %)             –[GAP: Y] kr      ← grön --apteal-core, minus-tecken
────────────────────────────────────────────
Du betalar                       [GAP: Z] kr      ← --aptext-l, Outfit 600, midnight —
                                                     radens tyngdpunkt
Materialkostnad tillkommer och specificeras i offerten.
```

- Talen: **alla `[GAP]` ur `ampy-foretagsdata`** eller ägar-låsta — aldrig påhittade (Golden Rule 3). Exemplet måste ligga INOM det publicerade intervallet (Z ∈ 6 000–12 000) annars motsäger blocket sig självt.
- Genomstrykning: **ingen** — stegen använder ett rent minus-tecken, aldrig `line-through` över `:-` (dödar PD-3-defekten och produktmallens "fejk-rea"-läsning PD-2).
- Mikrocopy under stegen: **"Vi drar av ROT direkt på fakturan och sköter ansökan till Skatteverket åt dig."** — gör avdraget till bevis på ärlighet, inte en rabatt-lockelse.
- Accordion-mekanik: samma finstilta chevron som FAQ-blocket, men med **korrekt ARIA** (unikt `id`, ifyllt `aria-controls`/`aria-labelledby`, native `<button>` — fixa direkt, upprepa inte FAQ-03-defekten).

**Grön Teknik-variant** (laddbox/batteri, 50 % på arbete + material): stegen byter etikett till "– Grön Teknik-avdrag (50 %)" och qualifiern säger "50 % på både arbete och material" (annan mekanik än ROT — copyn måste säga det).

---

## Micro-CTA

**Exakt en** interaktiv utgång framåt, aldrig en andra ask:

- Etikett: **"Få ditt exakta pris →"** (service/geo). Kopplar prislöftet till nästa steg: intervallet är vägledande, offerten är exakt.
- Stil: **teal outline-knapp** (`--apteal-core` 1.5px ram, teal text, transparent fyllning, `--apradius-full`, padding `--apspace-xs` block / `--apspace-m` inline). Medvetet **sekundär vikt** — den ska inte tävla med Hero_2:s gröna gradient-CTA eller main-contacts formulär; den är en mjuk bro, inte sidans huvud-ask.
- Mål: **ankarscroll till formuläret på SAMMA sida** (`#hero-form` på service/geo, `#main-contact` som fallback) — **aldrig `/kontakt/`** (GEO-01-klassens fix). `scroll-behavior: smooth`, sätter fokus på formulärets första fält efter scroll (a11y).
- Mobil: full bredd. Desktop: auto-bredd, vänsterställd under exemplet i Zon B.
- Ingen telefon-CTA i detta block (ring-vägen ägs av hero + main-cta); ingen dubbelknapp.

---

## States

| Element | State | Behandling |
|---|---|---|
| Micro-CTA | hover/focus | fyllning → `--apteal-core` solid, text → vit; `--focus-ring` teal 2px outline (tangentbord) |
| Räkneexempel-accordion | collapsed (default) | chevron ▸, `aria-expanded="false"`; endast rubrikraden syns |
| Räkneexempel-accordion | expanded | chevron ▾, stegen animerar in (max-height, 200ms ease); ingen layout-shift på prisraden ovanför |
| Löftesbock | statisk | ingen hover; rent informativt |
| Prisrad | `[GAP]`-data saknas | blocket renderas **inte** på den sidan (hellre inget än påhittat pris) — ACF-villkor `pris_min && pris_max` |
| Hela blocket | print | accordionen tvingas öppen, CTA döljs (`@media print`) |

---

## Copy-mönster (svenska, ampy-röst — riktningar, ej slutcopy)

| Vertical | Eyebrow | H2-kontext | Prisrad | Qualifier | Löfte |
|---|---|---|---|---|---|
| **Service / elcentral** (22 sidor) | Vad kostar det? | Byte av elcentral kostar vanligtvis | **6 000–12 000 kr** | efter 30 % ROT-avdrag på arbetskostnaden | Fast pris i offerten |
| **elektriker-i** (56) | Vad kostar en elektriker? | En elektriker kostar | **650–950 kr/timme** | efter ROT + startavgift för servicebil | Tydlig prisbild innan vi börjar |
| **elinstallation-i** (56) | Vad kostar det? | Elinstallation kostar | **[GAP: intervall]** | efter ROT | Fast pris i offerten |
| **laddbox-i** (56) | Vad kostar en laddbox? | Installerad laddbox från | **Fr. [GAP] kr** | efter 50 % Grön Teknik-avdrag | Fast pris i offerten |
| **eljour** (57) | Vad kostar eljour? | Utryckning kostar | **[GAP: fast inställelseavgift]** | dag/kväll/helg — beloppet innan vi åker | Fast utryckningsavgift, sagd innan vi åker |

Röst-regler (ampy-rost har sista ordet): du-tilltal, "vanligtvis/kan variera" som ärlig hedge, inga utropstecken i detta lugna block (dämpat register — pris/skatt är high-stakes, `Golden Rule 6`), inga superlativ på priset.

---

## Candour-grindar (blocket får inte skeppas om något fallerar)

1. **Varje siffra är publicerad eller `[GAP]`** — ur `ampy-foretagsdata` eller sidans egen live-FAQ. Aldrig uppfunnen (Golden Rule 3).
2. **Intern motsägelse måste lösas FÖRE rollout** — laddbox 4 190 (grid) vs "från ca 5 000" (FAQ) (GEO-09); produktmallens "Totalt 69 000" vs FAQ-intervall. Blocket förstärker annars just den motsägelse det finns för att döda. Ägaren låser **en kanonisk siffra per vertical**.
3. **Räkneexemplets slutpris måste ligga inom det visade intervallet** (Z ∈ min–max).
4. **"Fast pris i offerten" bara där offerten är fast** — timdebiterade sidor får löpande-strängen (ACF `pris_loftestyp`).
5. **Eljour skeppar först när ägaren gett fast inställelseavgift** (`[GAP]`) — annars renderas eljour-varianten inte.
6. **Ingen 5.0-rad, inget påhittat recensionsantal, ingen urgency/scarcity/nedräkning** — intervallet + taket + fast-pris-löftet är övertygande nog.
7. **ROT-precision:** alltid "30 % av arbetskostnaden, upp till 50 000 kr per person och år" tillgängligt (i qualifier eller exempel) — aldrig antydan om 30 % av hela notan.

---

## Reasoned against existing blocks (varför ett NYTT block, inte en variant)

**Mot FAQ-svaret (där priset bor idag, `blocks/faq.md`):** FAQ:n HAR rätt siffra ("6 000–12 000 kr efter ROT") men fel på tre designaxlar. (a) **Position:** kollapsad accordion vid 30–50 % scrolldjup — svaret på ad-löftet kommer efter beslutet att studsa (MECLABS message-match kräver first screen). (b) **Vikt:** som `--aptext-l` H3-fråga i en radlista har priset noll visuell tyngd; det syns inte ens öppet. (c) **Interaktionskostnad:** kräver en tap för att ens exponeras (FAQ-06). Blocket **flyttar inte** FAQ:n — det **repackar** samma copy till ett hero-adjacent, öppet, tungt viktat element. FAQ:n behålls för de andra frågorna (behörighet, garanti, ansvar). Detta block = 90 % omplacering av live copy → billigaste möjliga message-match-fix.

**Mot ProductHero-priskolumnen (`prod-sigenstor--mobile--13`, `product-design.md`):** produktmallens prisblock är rätt IDÉ, fel UTFÖRANDE, och fel KONTEXT för tjänstesidor. (a) Det visar ett **exakt pris** (69 000 kr) för en **fysisk produkt** — tjänstesidor har inget exakt pris, de har ett **intervall**; att låna produktens "Totalt"-manér skulle tvinga fram en falsk precision. (b) Det bär tre defekter blocket uttryckligen undviker: `.=`-glyfen (PD-3), "fejk-rea"-läsningen av struket ordinariepris (PD-2), och den ljust cyan svaga CTA:n (PD-5). (c) Det sitter i en 3-kolumns produkt-hero; tjänste-blocket är en **horisontell remsa under en 2-kol hero**. Blocket **ärver** produktmodulens ENDA goda drag — den ärliga avdragsstegen (direktiv 1 där) — som sitt kollapsade räkneexempel, och slänger resten.

**Mot incitamentsblocken (ROT/Grön Teknik/hemförsäkring, `incentive-blocks.md`, `incentive-design.md`):** incitamentsblocken svarar på fel fråga med fel form. Rubriken lovar pengar men de tre penseldragna cirklarna levererar en **byråkrati-tidslinje** ("samtal → installation → ansökan"), värdefrasen sitter i lågkontrast-gradient, och blockets enda klick är en **utgång** till en formulärslös artikel (D-INC-2/3/4). Pris & offert-blocket är dess motsats: **kronorna är hjälten**, inte processen; teal är **solid på siffran**, inte gradient på rubriken; klicket går **till formuläret på sidan**, inte bort. De två blocken **överlappar inte** — incitamentsblocket (fixat) förklarar *hur avdraget fungerar* längre ner; pris-blocket *svarar på vad det kostar* högst upp. Blockets räkneexempel lånar incitamentsdesignens ENDA behållna signatur — den destillerade skiss-ringen — men bara som en liten dekor-accent, aldrig som tre tunga cirklar.

---

## Divergenta riktningar (huvudingrepp → 3 versioner, husregel)

**Riktning A — "Öppen räkneremsa" (rekommenderas för service + elektriker-geo).**
Precis specen ovan: prisintervallet öppet och störst, fast-pris-löftet som bock-rad, räkneexemplet i en kollapsad accordion. Lugnt, informativt, ljust. Passar tjänste-/timverticals där intervallet ÄR svaret. Kräver `[GAP]`-tal + kontradiktions-lås. Lägst risk, billigast, störst räckvidd (134 sidor content finns).

**Riktning B — "Prisankare bredvid formuläret" (produkt/laddbox).**
Komprimera blocket till en **2-kol enhet där vänster = kr-matematiken (avdragsstegen öppen, inte kollapsad) och höger = micro-CTA/kort formulär-teaser**, placerad där priset redan syns (produktmönstret gör detta rätt). Förvandlar blocket från informationsremsa till **konverteringsenhet**. Risk: mer "e-handel" i känslan än en tjänstesida vill ha — reserveras för produkt/laddbox där ett exakt "Fr."-pris finns. Gated på 4 190/5 000-låsningen.

**Riktning C — "Prisförsäkran utan siffra" (eljour, tills [GAP] löst).**
Där ägaren ännu inte gett fast inställelseavgift får blocket INTE fejka en siffra. Bygg i stället en **process-försäkran i eljour-symptomblockets lugna stil** (`geo-eljour-taby--mobile--14` som referens): 2–3 teal-outline-ikonrader ("Du får utryckningsavgiften **innan** vi åker", "Fast timpris — inga påslag kväll/helg utan att du vet", "Tydlig faktura, inga dolda avgifter") + samma micro-CTA. Ingen påhittad krona, `kan`-registret. Byts mot Riktning A i samma sekund ägaren levererar prislistan. Löser även den felmärkta hemförsäkrings-pillen (INC-01 P0) i samma drag.

Alla tre: teal solid endast på siffran, ROT/Grön Teknik-precision i qualifiern, micro-CTA ankrar till formuläret på sidan, noll urgency.

---

## Vad som INTE ska röras

- **De publicerade intervallen** (6 000–12 000 kr, 650–950 kr/tim) — de är candour-korrekta och redan indexerade. Blocket **lyfter** dem, ändrar dem inte.
- **FAQ-blocket** — behålls för behörighet/garanti/ansvar/efterservice. Pris-blocket kompletterar, ersätter inte (FAQ:ns prisrad kan på sikt öppnas default, men det är en FAQ-fix, inte detta blocks jobb).
- **Hero_2:s struktur** — blocket ligger under den, konkurrerar inte med den. Ingen andra CTA-färg, inget telefonnummer, ingen 5.0-rad som skulle addera brus till en redan CTA-tät hero.
- **Teal + Outfit + midnight-tokens** — byt bara VAR teal används (solid på siffran, aldrig gradient på läsbar text). Inte paletten.
- **Den ärliga fakturamodellen** ("drar av direkt på fakturan, sköter ansökan till Skatteverket åt dig") — behåll ordagrant, den är blockets trovärdighets-ankare.
- **Ljus yta** — blocket får aldrig bli ett mörkt band. Dess jobb är att läsa som rak, lugn information efter den tunga hero:n.
