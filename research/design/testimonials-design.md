# Testimonials-slidern — designaudit (`ampy-testimonials`, V1 LÅST)

Scope: den visuella designen av testimonials-blocket så som det RENDERAS, mobil + desktop, sett på `svc-elcentral` (mobil 03/04/14, desktop 14), `geo-elektriker-tyreso` (mobil 15-runt, desktop) och homepage-kontext. Samma återanvända block på 291/326 sidor. Runt-1 tog struktur/innehåll/mekanik (T-01…T-07 i `research/blocks/testimonials.md`, rung 3 i `synthesis/trust-architecture.md`) — de upprepas INTE här; jag refererar ID och lägger designlagret ovanpå. Uppdelning enligt uppdrag: **(a)** fixar som ryms inom pixel-låset (innehåll/ordning/config) och **(b)** dokumenterat case OM ägaren någonsin öppnar designen igen.

---

## Vad ögat möter (mobil) — den primära ytan

Sekvens för första blicken, uppmätt på svc-elcentral mobil 03/04 (kortet med Alexandra Kamona):

1. **Den stora mintgröna citat-glyfen (66)** uppe till vänster. Den är det första — och grafiskt tyngsta — ögat landar på. Den är dekor. Den bär noll bevisvärde.
2. **En stor tom navyblå yta.** Citatet ("Vi är supernöjda med de som installerade vår elbox! … Rekommenderas varmt!") slutar högt i kortet; sedan följer ~140 px tomt mörkt fält innan namnet. Kortet ser **halvtomt/trasigt** ut. Ögat vilar på tomrum, inte på bevis.
3. Först därefter: **namnet "Alexandra Kamona"** (vit fet), en tunn avdelare, och en rad med **5 mintgröna stjärnor** + "maj 2026".
4. Under kortet: **4 avlånga prickar**, varav en grön "växande" pill och tre bleka grå. Läses som en *progress-/laddningsstapel*, inte som "svep för fler".
5. Under det: **5 GULA stjärnor + "5 av 5" + "Betyg på Google"**.

Rubriken "Vad säger dina grannar om Ampy?" står i midnattsblått, centrerad, tvåradig, över kortet. **Underrubriken "Riktiga omdömen från riktiga jobb." saknas på mobil** (döljs `≤759px`, T-03) — den ena rad som förramar korten som äkta är borttagen just på huvudytan.

Endast **ETT kort** syns, i full bredd med symmetriska sidomarginaler. **Ingen peek** av nästa kort. Inga pilar. Mobilanvändaren ser alltså: en dekorativ glyf, ett tomrum, ett omdöme, och en grön stapel utan förklaring.

## Vad ögat möter (desktop)

Sett på svc-elcentral desktop 14. Rubrik + **underrubrik syns** ("Riktiga omdömen från riktiga jobb.", grå, centrerad). Under den: en **rad med 3 hela kort + en avklippt peek-remsa på VARDERA kanten**. Peek-remsorna visar bara glyf + Google-G som svävar utan text — det ser ut som en **renderingsglitch, inte som en avsiktlig "det finns fler"-signal**. Korten har samma navy-gradient. Eftersom raden tvingar **enhetlig korthöjd** blir tomrums-defekten synlig sida-vid-sida: ett kort med långt citat är fyllt, grannen med kort citat står halvtomt bredvid. Autoplay flyttar texten var 4:e sekund (rörelse intill läsning, T-04).

Notera inkonsekvensen: **desktop HAR en peek/kontinuitetssignal, mobil har den inte** — tvärtemot vilket som borde prioriteras (mobil = primär yta).

---

## Fynd (design)

**TD-01 — Fast korthöjd → stort dött navy-tomrum; ögat landar på tomhet, inte på bevis.** Mobil (akut) + desktop. Kortet dimensioneras efter det längsta citatet i setet; korta omdömen (majoriteten är 1–3 meningar) lämnar ~120–140 px tom mörk yta mellan citat och namn. Detta är blockets **enskilt största visuella defekt**: den mest värdefulla ytan (ett kort, full bredd, på primärytan) spenderas på tomrum. Konsekvens i ägarens altitud: precis som "5.0-raden stjäl fokus från CTA-knappen" stjäl tomrummet + glyfen fokus från namnet/stjärnorna/Google — själva beviset. Evidens: visuell hierarki (den dominerande ytan ska bära det viktigaste elementet); kortet gör tvärtom.

**TD-02 — Två olika stjärnfärger för samma "5 av 5", ~80 px isär.** Mobil + desktop. Inne i kortet: **mintgröna** stjärnor. I badgen strax under: **gula** stjärnor. Två betygsvisualiseringar staplade läses som *två system* och skaver — särskilt för en 35–65-publik som avkodar "är det här samma betyg?". Mint = varumärkes-teal (on-brand men okonventionellt för Google-betyg); guld = Google-konvention men bryter tokens. Måste enas till EN. Evidens: Jakobs lag (en sak = en representation); token-disciplin (teal ensam accent, designsystem-djupanalys).

**TD-03 — Dekor-glyfen väger tyngre än bevis-märket.** Mobil + desktop. Den mintgröna citat-glyfen (~40 px) dominerar uppe till vänster; **Google-G:t (~32 px) är mindre**, uppe till höger. Men G:t är trovärdighetssignalen ("det här är ett RIKTIGT Google-omdöme") — det starkaste beviset i kortet — och det är det mindre märket. Ögonvikt spenderas på dekoration framför proof. Evidens: Cialdini (social proof övertygar bara när verifierbar → gör verifieringsmärket dominant); visuell hierarki.

**TD-04 — 4 prickar för 12 omdömen, i en "växande stapel"-metafor som läses som laddning.** Mobil + desktop. Navigationen är fyra bleka pills med en grön växande pill; `dot = index % 4` (T-03). Designproblemet ovanpå comprehension-problemet: **pill-formen + den fyllande gröna signalerar "progress bar", inte "sida 1 av flera".** Kontrasten mot `#f5f9ff`-bakgrunden är dessutom svag (blekgrå pills), så signalen är nästan osynlig. Evidens: NN/g (prickar är svaga signaler på touch; item-antal ska vara ärligt); Baymard (carousel-antal ska stämma).

**TD-05 — Ingen peek på mobil = ingen visuell signal att fler kort finns.** Mobil (akut). Full bredd + symmetriska marginaler + `arrows:false` + pausar-på-touch (`pauseOnFocus`) → en användare som rör kortet stoppar autoplay och har då **noll synlig ledtråd** att 11 omdömen till finns. Desktop peekar (om än fult), mobil inte alls. Evidens: NN/g (avklippt/peek är den sanktionerade "innehållet fortsätter"-signalen).

**TD-06 — Gradientens ljusnande hörn sänker textkontrasten inom samma stycke.** Mobil + desktop. Kortet är `linear-gradient(-27deg, #0b0f30 → #2d516d)` med **vit vikt-300** brödtext. De nedre/högra raderna sitter mot det ljusare stål-blå (#2d516d) → **lägre kontrast och mer halation på just de sista raderna** av ett citat, för äldre ögon (T-06 tog vikt-300 generellt; det NYA här är att kontrasten *varierar inom stycket* p.g.a. gradientriktningen). Evidens: tunn ljus-på-mörk typ + fallande kontrast = känd läsbarhetsrisk för kärnpubliken.

**TD-07 — Google-betygsmotivet dyker upp 4–5 ggr per servicesida; testimonials-badgen är den ENDA som förtjänar sina pixlar.** Cross-block, men loggas här eftersom blocket äger bevisen. På svc-elcentral inom ~2 skärmar: Hero_2 "5.0 ★★★★★" (teal stjärnor) → MainCTA "5,0 på Google" (gula) → main-contact "5 av 5 · Betyg på Google" (gula) → **testimonials-badge "5 av 5 Betyg på Google" (gul) + mintstjärnor i korten**. Fem stjärnrader, blandade färger. Designargumentet i ägarens altitud: badgen **inne i testimonials är den enda instansen som är förankrad i synliga, namngivna omdömen precis ovanför** — den förtjänar numret. De dekorativa upprepningarna på andra block gör inte det (trust-architecture R3: max 2 numeriska betyg/sida). Slutsatsen: skala inte upp badgen — **skala NER numret överallt utom här**.

**TD-08 — Underrubriken (förramningen) raderas på mobil.** Primärytan tappar "Riktiga omdömen från riktiga jobb." — den enda raden som säger *att omdömena är äkta* — samtidigt som mobilkortet redan är glest på bevis (T-03; upprepas som designfynd eftersom det förvärrar TD-01/TD-03: mobil får minst förramning där den behövs mest).

---

## Omdesign-direktiv

### (a) Inom V1-låset — innehåll/ordning/config, inga nya pixel-mönster
Dessa ändrar VILKET innehåll/vilken ordning, inte kortets utseende. Prioriterade; de flesta härledda i runt 1 — här som designmotiverad exekveringslista:

1. **Förankra badge-texten** (T-01): "5 av 5 · Betyg på Google" → **"5,0 av 5 · 25 omdömen på Google"** (ägarbekräfta antal; synka schema `reviewCount:25`). Ren textswap. Detta gör badgen till den förtjänade betygsinstansen (TD-07) — och legitimerar att numret tas bort på Hero_2-trust-raden/MainCTA/main-contact.
2. **Vertikal-styrd pinning istället för blind shuffle** (T-02): tagga varje omdöme i CPT (belysning/elcentral/laddbox/batteri/eljour/allmänt); pinna matchande omdöme till **slide 1 = det enda mobilkortet**; slide 2 = ångest-dödaren (Fernström/Mohammed/Daniel). Noll visuell diff, 291-sidors relevanslyft. Löser även TD-01 delvis: ett *längre*, mer specifikt citat på slide 1 fyller kortet och krymper tomrummet.
3. **Normalisera slotten på geo** (T-05): flytta blocket från position 5 → 3 på elektriker-i/eljour-i (112 sidor), så bevis kommer före telefon-asket (MainCTA).
4. **Review-refresh-kontrakt** (T-07): kvartalsvis byt de 3 äldsta korten + uppdatera antal. Process, ej kod.

### (b) Owner-gated visuella diffar på det låsta blocket — låg risk, hög avkastning
Kräver före/efter-godkännande per approved-rendering-kanon, men rör inte kort-arketypen:

5. **Återställ underrubriken på mobil** (TD-08/T-03): ta bort `.att-sub{display:none}` `≤759px` (ev. korta ner). Ett CSS-regel, återför förramningen på primärytan.
6. **Mobil-peek** (TD-05/T-03): lägg `padding:{right:'2.5–3rem'}` på 759-brytpunkten så nästa korts vänsterkant syns ~28–32 px. Config-värde, inget kort-redesign. Se till att peek visar **textkant, inte bara glyf/G** (justera så remsan klipps in i brödtexten, annars upprepas desktop-glitchen).

### (c) Finess-fixar som kräver att en enda token/regel rörs (gränsfall — föreslå som före/efter)
Dessa är minimala men ÄR visuella diffar; lägg fram för ägaren som riktade en-radiga byten, inte som redesign:

7. **Ena stjärnfärgen** (TD-02): välj EN. Rekommendation: **teal/mint i BÅDE kort och badge** (token-disciplin, teal ensam accent) — eller, om Google-igenkänning väger tyngst, guld i båda. Aldrig en av varje i samma block.
8. **Väg om glyf vs Google-G** (TD-03): krymp citat-glyfen ~25–30 % och/eller förstora G:t så **proof-märket ≥ dekor-märket**. Gör G:t till det som drar blicken uppe i kortet.
9. **Byt pill-navigationens metafor** (TD-04): antingen (i) runda punkter i faktiskt antal-läge med en diskret "1/12"-räknare, eller (ii) behåll pills men höj kontrasten mot `#f5f9ff` (mörkare inaktiv, teal aktiv istället för grön-som-läser-progress). Målet: läses som "bläddra", inte "laddar".

Notera: **TD-01 (fast korthöjd/tomrum)** går inte att lösa utan att röra kort-layouten → den hör hemma i case (b) reopen nedan, inte i det låsta lagret. Delvis-lindring via direktiv 2 (längre pinnade citat).

---

## Divergenta riktningar (OM designen öppnas — case (b))

Tre strukturellt skilda omtag på blocket. Alla behåller de äkta namngivna/daterade omdömena och den utlänkade Google-badgen; de skiljer sig i bäraren.

**Riktning A — "Kurerat rutnät, ingen slider" (lugnast, bäst för 35–65).**
Döda karusellen. Visa de **6 starkaste** omdömena (pinnade efter specificitet: pris-vs-konkurrent, "svarar de sen?", kompetens-där-annan-firma-föll) i ett rutnät: **3×2 desktop, staplat 1-kolumn mobil**. Korten **hugger innehållshöjd** (min-height, inte fast) → TD-01 försvinner helt. Ingen rörelse (T-04), ingen dold-bakom-svep-proof, deterministiskt starkaste bevis. Google-G överst-höger, EN stjärnfärg, glyf nedtonad till liten accent. Under rutnätet: den förankrade badgen + "Se alla 25 omdömen på Google →". Detta är den mest läsbara, mest bevis-täta versionen och matchar publikens tålamod.

**Riktning B — "Content-hug slider med ärlig peek" (minsta avvikelse från V1).**
Behåll slider-arketypen men fixa mekaniken visuellt: **min-height-kort (inget tomrum, TD-01)**, asymmetrisk peek på mobil (TD-05), **ärlig navigation** — antingen faktiskt prickantal eller pilar + "1/12"-räknare (TD-04), **enad stjärnfärg** (TD-02), **förstorat Google-G** (TD-03), autoplay av eller ≥7 s med tydlig paus-signal (T-04/äldre läsare). Samma navy-kort, samma känsla — bara ärligt och fyllt. Lägst risk om ägaren vill känna igen V1.

**Riktning C — "Redaktionellt, ljust, ett hjälte-omdöme" (bryter mörk-stapling).**
Vänd kortet från navy till **ljust** (löser dark-stacking Hero_2→Testimonials och halation TD-06) och gör ETT stort, pinnat, vertikal-matchat hjälte-omdöme läsbart och centralt (stor citat-typ, namn, roll om finns, Google-G, datum). Under det: en kompakt **horisontell filmremsa av små omdöme-chips** (namn + 1 rad + stjärna) att bläddra bland — peek är inbyggd i remsan. Proof-tätt, lugnt, ljust, och citat-glyfen får bli det brand-motiv den vill vara utan att slåss med brödtexten. Bäst om ägaren vill bryta det navy-på-navy-staplet som flera block delar.

Rekommendation att lägga för ägaren: **A som default** för 35–65-läsbarhet + determinism, **B** om V1-igenkänning måste bevaras, **C** om mörk-staplingen ska lösas i samma tag.

---

## Vad som INTE ska röras (skydda det som funkar)

- **De äkta, namngivna, daterade Google-omdömena.** Kategorins bästa proof, candour-rent. Rör bara ordning/pinning, aldrig substansen.
- **Rubriken "Vad säger dina grannar om Ampy?"** på konsumentsidor — varm, lokal, on-voice; Filip Erikssons "Blev rekommenderad av en granne" gestaltar den bokstavligen. (B2B-sidor byter till "Vad säger våra kunder?" per trust-architecture #22 — men det är copy, inte design.)
- **Badgen som LÄNKAR ut till GBP** (verifierbar social proof, ny flik) — behåll länken; förankra bara texten.
- **Positionen intill hero/formulär** på service/elinstallation/produkt (rätt altitud — bevis vid asket).
- **Teal citat-glyfen som brand-motiv** — väg om storleken, radera inte konceptet.
- **Ingenjörskonsten:** server-renderad statisk fallback, `prefers-reduced-motion` som dödar autoplay, pause-on-hover/focus, aria-labels. Rör inte a11y-lagret.
