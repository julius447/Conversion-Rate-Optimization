# 00 — Ampy design-doktrin (round 2, det enade design-lagret)

Detta är takytan över de 21 design-auditerna. Round 1 gav STRUKTUR (block-ordning per mall — det ägaren
godkände). Round 2 gav DESIGN-finess på ägarens altitud: *"ta bort '5.0 på Google' så CTA-knappen blir hela
fokuset — DET är CRO."* Den här filen destillerar de återkommande reglerna som föll ut när 21 agenter tittade
på samma pixlar, löser motsägelserna dem emellan, och listar besluten bara Julius kan fatta. Struktur/tratt-
lagret ligger kvar i `synthesis/funnel-architecture.md` (round 1) — där design-analysen ändrade den domen
säger jag det rakt ut i §4.

Tokens genomgående: teal `#00a991`, midnight `#090b32`, Outfit, ap*-skala. Candour-grinden oförändrad.
Publik: svenska husägare/BRF 35–65 — läsbarhet, lugn självsäkerhet, verifierbart bevis. Två konverteringar:
ring eller formulär.

---

## 1. Visuell-hierarki-reglerna som föll ut (fokusekonomin)

Fem lagar återkom i nästan varje audit. De ÄR doktrinen; allt annat är tillämpning.

### 1.1 ETT dominant element per block, matchat mot blockets konverteringsjobb
Ägarens 5.0-frö är ett specialfall av en generell lag: **det som är störst/ljusast/mest kontrastrikt i ett
block ska vara det element som gör blockets jobb — inget annat får tävla.** Auditerna hittade samma defekt om
och om, alltid som "fel element vinner ögat":
- **MainCTA:** ansiktet (~55 % av kortet) + 5,0-guldraden inramar Ring-knappen mellan två fokustjuvar →
  krymp ansiktet till inset, ta bort 5,0-raden, knappen blir terminal blickvila (`call-cta-design`,
  `spec-main-cta-evolution`).
- **Metric-kortet:** den svarta ikoncirkeln vinner, siffran — kortets hela existensberättigande — kommer tvåa
  → tal-först stat-trio, ikon till liten inline-glyf (`trust-elements-design` PROOF-D1).
- **Testimonials:** fast korthöjd → dött navy-tomrum + dekor-glyfen väger tyngre än Google-G:t (beviset) →
  content-hug + förstora G:t (`testimonials-design` TD-01/03).
- **MainContact (mobil):** 15ch display-citat äter hela första skärmen, formuläret osynligt → demota citatet
  (`maincontact-design` MCD-01).
- **Produkt:** det tomma vita bildkortet är sidans största, ljusaste element och bär minst information →
  krymp, lyft värde+pris över vikning (`product-design` PD-1/12).
- **Incitament:** rubriken lovar pengar, de tre process-cirklarna levererar logistik → gör kronorna till
  hjälten med number-isolation (`incentive-design` D-INC-2).
- **Prisblock:** prisintervallet måste vara "det ohotat största, mest kontrastrika elementet" (`spec-pris-offert`).
- **AltHero (hubbar):** helskärmskort som bara bär titel+mening, 40–55 % tom navy → ge den ett jobb eller
  krymp (`hub-pillar-magnet-design` H-L1).

### 1.2 När trust-rader HJÄLPER vs STJÄL fokus
Regeln: **ett bevis-element hjälper när det bär blockets jobb eller sitter i beslutszonen som ett lugnt
ankare; det stjäl när det sitter terminalt/adjacent till den enda handlingen och glimmar.**
- **STJÄL (ta bort):** oankrad "5,0 ★★★★★" direkt under/bredvid en CTA-knapp — bekräftat på MainCTA, Hero_2-
  raden, produkt-expertkortet, eljour-heron, artikel-slutkortet. Guldstjärnorna glimmar och blir sista
  blickvila. Betyget hävdas 3–5×/sida i blandade färger → upprepning devalverar (`spec-proof-pattern` PP-02,
  `trust-elements-design` PROOF-D5).
- **HJÄLPER (behåll/lyft):** icke-länkade bevis-chips i beslutszonen (behörig · försäkrad · fast pris · ROT),
  teal linjeglyfer, `ampy-trustrow` (`spec-proof-pattern`). Reassurance-bullets på eljour (dygnet runt · inom
  en timme · behörig, inte en växel · tydligt pris) — candour-perfekta (`eljour-design` behåll-listan).
  Ankrat "3 000+ installationer/år" i MainContacts vänsterpanel. Källbelagd "1 800 elbränder · Elsäkerhetsverket".
- **Netto-regeln:** EN ankrad betygs-instans per sida (med recensionsantal), placerad vid formuläret eller inne
  i testimonials — aldrig i hero-raden mellan CTA och form, aldrig staplad på samma skärm.

### 1.3 Färg- och CTA-konkurrens
- **Teal är tapet, inte accent** (`homepage-design` HD-10): teal/cyan ligger på hero-CTA, MiniMenu, produkt-
  "Läs mer", BlueCTA, ServiceGrid, MainCTA-panel, contact-knapp, MapBlock, prefooter — tre nyanser i stora
  ytor. **Reservera teal för EN sak: den primära handlingen (+ dess signatur-glyfer).**
- **EN handlings-gradient per block.** Idag tävlar tre lysande gradienter i Hero_2 (grön /kontakt/ + blå Ring +
  mint submit). Kanon: mint-submit äger handlingen; allt annat interaktivt är ghost/text/solid-emergency
  (`spec-hero-system` §1, `spec-form-system` §0.2).
- **EN kanonisk Ring-knapp = hög kontrast, ≠ navfärg.** Dagens ljust-cyana Ring-pill är färgtvilling med
  "Läs mer"/"Till X"-navknapparna. Kanon = midnight `#090b32` solid (BlueCTA:s bevisade look), teal chip
  vänster (`spec-main-cta-evolution`). **Undantag: eljour** använder mörkgrön `--eljour-emergency-green`
  (vit text klarar 4.5:1; teal gör det inte) (`spec-eljour-kit`).
- **EN stjärnfärg per sajt = teal.** Guld är token-defekt (`hub-pillar-magnet-design` genomgående, `testimonials`
  TD-02, `spec-proof-pattern` PP-02). Aldrig teal och guld på samma sida.
- **Badges:** SUPERKAMPANJ (skrikgrön) / BÄSTSÄLJARE (navy) / NYHET (teal) — tre färger, ingen semantik, den
  grönaste sitter på lägst-prio-produkten → EN dämpad form eller inga badges (candour ⚑) (HD-05, PD-10).

### 1.4 Mörk-band-rytm
- **Cyan-band dyker upp utan logik** (HD-11) — "här är ett färgat band". Reservera cyan/färgband för EN
  betydelse ("prata med oss"-moment), inte slumpvisa avdelare.
- **Mörkt-på-mörkt flyter:** navy formkort på navy hero (Hero_2, batteri-pelaren) → formkortet läser som
  bakgrunds-förlängning → ljusare glas-yta + 1px teal-kant + skugga så det lyfter (`spec-hero-system` D-05,
  `hub-pillar-magnet` P-B2).
- **Mörka band ska vara AVSIKTLIGA ankare, inte slump.** Rätt användning: artikelns Nästa-steg midnight-platta
  (end-zonens ankare, maximal separation från vita brödkort); Prisblocket medvetet LJUST efter mörk hero =
  välkommen visuell lättnad "nu talar vi rakt" (`spec-router-article` B.3, `spec-pris-offert`). Fel: navy-på-
  navy-stapling hero→testimonials, slumpvisa cyan-band.
- **Palett-reset som sektionssignal:** offwhite `#f5f9ff` under den låsta heron signalerar "nu går vi från
  känsla till funktion" — löser att MiniMenu läser som ett tredje dusk-foto/hero-förlängning (HD-14,
  `spec-router-article` A.2).

---

## 2. Konsoliderad per-block design-direktivtabell

Topp-3-ingreppen per block. Fullständig spec i den citerade filen.

| Block | Topp-3 design-direktiv | Källfil |
|---|---|---|
| **Hero_2 / .aof** | (1) Dela efter INTENT: HERO-S (tjänste-bild, ingen form) / HERO-G (3-fälts SSR-form) / HERO-E (call-first). (2) EN handlings-gradient — döda grön /kontakt/ + blå Ring-gradient. (3) Fyll döda navy-kvadranten med tjänstebild; höj formkortet med teal-kant. | `hero2-design`, `spec-hero-system` |
| **MainCTA** | (1) Ta bort 5,0-raden → knappen blir fokus. (2) Krymp ansiktet 55 %→inset 104px. (3) Ring-knapp cyan→midnight solid, teal-chip. | `call-cta-design`, `spec-main-cta-evolution` |
| **BlueCTA** | (1) Droppa på sidor som bär MainCTA v2 (samma phone-ask). (2) Behåll bara på ansiktslösa sidor; svart→midnight `#090b32` token. (3) Ärver ut sin pill-look till MainCTA. | `spec-main-cta-evolution` |
| **MikroCTA** | (1) Retirera (dubbel-ask duplicerar Hero_2). (2) Skalet överlever bara som B2B serviceavtal-CTA / team-close / artikel-Nästa-steg-bas. | `call-cta-design`, `spec-main-cta-evolution` |
| **Testimonials (V1 låst)** | (1) Content-hug (döda navy-tomrummet). (2) EN stjärnfärg = teal, ta bort dubblerad guldrad. (3) Förstora Google-G > dekor-glyf; ärlig navigation. [inom lås: pinning + ankrad badge + mobil-peek/underrubrik] | `testimonials-design` |
| **MainContact** | (1) Mobil: demota jätte-citatet, lyft mekanismen. (2) Reassurance (24h) OVANFÖR submit. (3) Fält-kant + fält-diet (namn+tel min) + synligt telefon-nr; submit "Bli uppringd". | `maincontact-design`, `spec-form-system` |
| **Proof/trust-yta** | (1) `ampy-trustrow` = icke-länkade bevis-chips i beslutszonen. (2) Behörighetsband ersätter certifikatväggen. (3) Verifieringslänk bara i footer + FAQ, aldrig i beslutszonen. | `trust-elements-design`, `spec-proof-pattern` |
| **Metrics** | (1) Tal-först stat-trio (~56px), ikon → liten inline-glyf. (2) EN rad 3-across även mobil (~160px, ej 400px). (3) Byt "1000+ Nöjda kunder" (bannat) → "3 000+ installationer/år". | `trust-elements-design` |
| **Certifikatvägg** | (1) Splittra myndighet från kommersiellt (Rexel späder). (2) Ta bort 6 utlänkar före sista CTA. (3) Reg.nr i klartext, ej anonym logga. | `trust-elements-design`, `spec-proof-pattern` |
| **FAQ** | (1) Öppna första frågan default. (2) Bygg kort-affordans (teal-kant/chevron-cirkel). (3) Släpp AI-bilden → full bredd + close-kort i frigjord yta. | `faq-varprocess-design` |
| **Vår process** | (1) Fixa live-buggar (dubblerad steg-4-text, "Vi går vi", "Ampy's"). (2) Nummer-cirklar på connector-linje. (3) Vänsterställ på mobil. | `faq-varprocess-design` |
| **Header/nav/footer** | (1) Lägg tel-affordans i headern (desktop text-länk, mobil teal ikon-knapp utanför hamburgaren). (2) Höger-ankra mobilens handlingszon. (3) Elevera telefonen i footern; bryt prefooter-väggen. | `nav-design` |
| **Incitament (ROT/GT/försäkring)** | (1) Kronor = hjälten (number-isolation-remsa före stegen). (2) Lyft värdefrasen ur gradienten (solid teal på siffran). (3) Döda utgångsknappen → inline-accordion; fixa hemförsäkrings-P0-etiketten. | `incentive-design` |
| **Produkt (hero+pris+grid)** | (1) Ärlig avdragsstege (ingen fejk-rea/struket "ordinarie", ingen `.=`-glyf). (2) En offert-CTA, grön, starkast på sidan. (3) Krymp bildkortet; ta bort 5,0 ur expertkortet. [P0: fixa zaptec-404] | `product-design` |
| **Eljour-hero** | (1) Samtal primärt: dominant grön nödknapp, form → opt-in. (2) Live-pill "Jour öppen just nu" upp. (3) Sticky mobil call-bar + two-lane kanon. | `eljour-design`, `spec-eljour-kit` |
| **Symptomblock** | (1) Severity-sortera (Akut röd först). (2) Hela raden tryckbar, chevron i severity-färg. (3) Ta bort "1000+"-kortet → snabbhets/behörighetsrad. [SKYDDA — sajtens bästa bevisdesign] | `eljour-design`, `spec-eljour-kit` |
| **ServiceRouter (startsida)** | (1) Döda dekorativa dusk-MiniMenu:n. (2) Promota ServiceGrids funktionsfoto+scent-grammatik till plats 3. (3) Prio-viktad 6+2 (tjänst>laddbox>batteri); offwhite palett-reset. | `homepage-design`, `spec-router-article` |
| **ContentBlock (SEO-svans)** | (1) Läshierarki: rubrik(600) → lead → 3 fetad-lead-punkter. (2) Riktiga-jobb-foton + obligatorisk platsad/daterad bildtext. (3) Cap mobil-bild ~240px, text-först-stack. | `content-seotail-design` |
| **VissteDuAtt** | (1) Skeppa redan-byggda redesignen (döda gungande lampa, #010328→#090b32). (2) Vikt 300→400. (3) Mjuk nästa-steg-länk (ej dead-end). | `content-seotail-design` |
| **FooterSEO** | (1) Ompeka CTA /kontakt/ → `#main-contact`. (2) Fixa "radgivning"→"rådgivning". (3) Rama om som "sista chansen att fråga", telefon primär. | `content-seotail-design` |
| **Artikel** | (1) Inline-CTA "Skicka en bild" (~30 % djup, teal-tint-paus). (2) Nästa-steg midnight-slutkort tar review-slotten. (3) Persistent högerräls-kort (fyller tom desktop-ränna). | `article-design`, `spec-router-article` |
| **Prisblock (NYTT)** | (1) Prisintervallet = ohotat största elementet (teal solid, ej gradient). (2) Fast-pris-i-offerten-löfte (Konsumentverket-normen synlig). (3) Inline räkneexempel-accordion, micro-CTA ankrar på sidan. | `spec-pris-offert` |
| **Thank-you** | (1) Animerad ✓ (fixa tom-cirkel-bugg) + konkret 24h-SLA. (2) Förberedelse-checklista + team-ansikten. (3) Spara-numret vCard; döda browse-detour-pillen. | `spec-form-system` |
| **Hubbar/pelare/magneter** | (1) AltHero: ge jobb eller krymp (ej helskärm tomrum). (2) Stäng med MainContact + Vår process (ej dö på produktkort). (3) Omfördela formmaskineriet till rätt vertikal (batteri #3 bär full form, laddbox #2 bär inget). | `hub-pillar-magnet-design` |
| **MapBlock** | (1) 20 identiska piller → 6–8 orter + "fler orter →". (2) Byt hex-blob mot äkta silhuett eller släpp. (3) Sub-kort bekräftar ("hela Sverige"), tvivlar inte; ankra på sidan. | `homepage-design`, `trust-elements-design` |

**Delade primitiver (definieras EN gång, propageras):** `btn-primary-mint` (enda handlings-gradienten) ·
`btn-ring-dark`/midnight (kanonisk Ring) · `btn-emergency-green` (eljour) · `link-quiet` (ersätter cyan-pill-
havet) · `ampy-field` (ETT input-språk, 1px kant + teal focus) · `ampy-trustrow` (icke-länkade bevis-chips).

---

## 3. Motsägelser jag löste mellan audit-filerna (namngivna)

1. **PhoneBand-frågan (`funnel-architecture` §3 vs `spec-main-cta-evolution`).** Round-1-tratten sa
   "MERGE MainCTA×BlueCTA → PhoneBand". Ägaren underkände uttryckligen den framingen ("ersätt inte tre CTA-
   block med en tunn telefonrad"). **Löst:** MainCTA v2 är ring-flaggskeppet (varmt ansikte + nyttolöfte + EN
   ren ring-ask); BlueCTA DROPPAS på MainCTA-sidor och överlever bara ansiktslöst med sin pill donerad till
   MainCTA; MikroCTA killas. Namnet "PhoneBand" pensioneras. (Design-domen övertrumfar round-1.)

2. **Stjärnfärg (teal vs guld) — `hub-pillar-magnet` / `testimonials` / `spec-proof-pattern` / `homepage`.**
   Fyra filer, samma splittring: hero/hub renderar teal, MainCTA/magnet renderar guld. **Löst enhetligt:** EN
   färg = teal (token-disciplin); guld = defekt, dras tillbaka sajtövergripande.

3. **Certifikatväggens öde (`funnel-architecture` §3 "Certificates wall stays at the tail" vs
   `trust-elements` / `spec-proof-pattern`).** Round-1 behöll väggen; round-2 mötte ägarens "det leder ju folk
   bort"-invändning. **Löst:** de 6 utlänkade logokorten retireras; verifieringens VÄRDE (registrerad,
   försäkrad, betygsatt) renderas som icke-länkat behörighetsband i beslutszonen; verifieringens HANDLING
   (slå upp ESV-registret) flyttas till footer + FAQ; partner-loggor (Trygg-Hansa/ID06/Rexel) → tonad footer-
   rad, Rexel-grossisten lämnar auktoritetsytan. (Round-2 supersederar round-1:s "keep wall".)

4. **Testimonials-slot + låst-status (`service-pages` slot 7 vs `funnel` slot 4 vs `testimonials-design`
   V1-lås).** **Löst:** slot 4 (bevis-före-ask; vertikal-pinning löser generisk-invändningen). Design-lagret
   lägger till: content-hug som dödar tomrummet (TD-01) går INTE inom pixel-låset → dokumenterat som owner-
   gated diff (Riktning B), medan inom-lås = pinning + ankrad badge + mobil-peek/underrubrik.

5. **Hero_2 som en mall vs intent-varianter (`funnel` behandlar 260 sidor som en Hero_2 vs `spec-hero-system`).**
   **Löst:** ägarens hypotes operationaliserad — HERO-S (service, ingen form) / HERO-G (geo, 3-fälts form) /
   HERO-E (eljour, call-first), routad av CPT. `spec-hero-system` är kanonisk; Hero-1 (homepage/pelare) rörs
   inte (ägar-referens).

6. **MainContacts 3-stegs-remsa (`funnel` §3 "KILL where VarProcess precedes" vs `maincontact-design` "flytta
   reassurance ovanför submit").** **Löst:** 24h-löftet flyttar till mikrocopy direkt under submit (mobil-
   kritiskt); den fulla 3-stegs-remsan de-dupas mot VarProcess bara där de ligger adjacent.

7. **Fält-antal (`spec-form-system` mini=3 · `maincontact` callback-min=namn+tel · `hub-pillar` batteri-diet ·
   `spec-hero-system` HERO-G=3).** Fyra filer, samma riktning men olika tal. **Löst:** ETT `ampy-field`-språk i
   tre densiteter — mini (3: namn/tel/postnr), full (MainContact: 2 default + disclosure), confirmation
   (thank-you: 0). Minsta kvalificerande lead = namn+telefon(+postnr för geo-routing); allt annat bakom
   "Fler uppgifter".

8. **Ring-knappens kanoniska färg (`spec-main-cta-evolution` midnight vs `spec-eljour-kit` emergency-green).**
   Inte en konflikt utan en **intent-split:** midnight `#090b32` är sajt-kanon; mörkgrön reserveras för eljour
   där vit text mot teal fallerar 4.5:1 och akut-registret motiverar en egen "nödknapp". Teal-fylld pill =
   dokumenterat alternativ.

9. **Header CTA anchor vs navigate (`funnel` §1.2 övertrumfar header-auditens per-sida-anchor).** `nav-design`
   lägger till en tel-affordans utan att röra det: headern navigerar uniformt till (fixat) /kontakt/, telefon
   blir ett andra lågfriktions-alternativ. Konsistent, ingen konflikt kvar.

---

## 4. Reviderade domar mot round 1 (där design-analysen ändrade beslutet)

| Round-1-dom | Round-2-design-dom | Varför |
|---|---|---|
| **TrustStrip** = nytt block med ESV-utlänk mid-funnel | **`ampy-trustrow`** = icke-länkade bevis-chips + behörighetsband; verifieringslänk bara footer+FAQ | Ägar-pushback: utlänk exporterar det varma leadet. Värdet skeppas överallt, handlingen bara vid kanterna (`spec-proof-pattern`) |
| **PhoneBand** = merga MainCTA×BlueCTA till en tunn telefonrad | **MainCTA v2** = ring-flaggskepp; BlueCTA droppas/degraderas; MikroCTA killas | Ägar-pushback: MainCTA "mår skitbra", förädla den — inte ersätt med tunn rad (`spec-main-cta-evolution`) |
| **Hero_2** = en mall på 260 sidor | **Tre intent-heroes** (S/G/E) | Ägarens hypotes: service = nyfiken (visa tjänsten, ingen form), geo = köpredo (form), eljour = akut (samtal). Fel design på fel intent kostar leads (`spec-hero-system`) |
| **Certifikatväggen** stannar i svansen | Väggen retireras; kärnan klonas UPP som icke-länkade chips; partners → tonad footer | "Leder folk bort"; Rexel späder myndighet; 6 utgångar före sista CTA (`trust-elements`, `spec-proof-pattern`) |
| **Metrics** "1000+ Nöjda kunder" (P0-fynd men behållet block) | Number-först stat-trio med **belagda** tal ("3 000+/år", "Reg. ESV", ankrat betyg) | "1000+" bannat + dess svart-ikon-cirkel stjäl blicken från siffran (PROOF-D1/D6) |
| **Thank-you** = destination, pixel fires | **Post-submit workspace** (bekräfta→förbered→ansikten→spara-nummer) | Sajtens högsta-trust-ögonblick spenderat på tom check + browse-detour; svarar inget den oroliga konverteraren frågar (`spec-form-system` C) |
| Betyg/CTA-rad som proof överallt | **5,0-raden bort under VARJE CTA** (hero, MainCTA, produkt-expertkort, eljour, artikel) | Ägar-fröet generaliserat: oankrad glimmande betygsrad = terminal fokustjuv, candour-liability |
| **Guld-stjärnor** som Google-konvention | **Teal-stjärnor** token-brett | Guld = token-defekt; teal ensam accent |
| VissteDuAtt / FooterSEO copy-fixar | **Skeppa redan-byggda VDA-redesignen** + ompeka FooterSEO till `#main-contact` | Live kör gammal JSON (gungande lampa, off-kanon token); mallnivå → 290 sidor på ~noll jobb (`content-seotail`) |

Oförändrat från round 1 (design bekräftade tratten): 5-slot ask-budget, /kontakt/-paradoxen (destination
först, retarget sedan, prereq: instrumentera formulär + döda `hidden-on-load`), label-kanon ("Kostnadsfri
rådgivning"/"Boka rådgivning"/"Ring 010-265 79 79"), FAQ ovanför MainContact, incitament över formuläret.

---

## 5. Ägar-beslut (design-val bara Julius kan fatta — med rekommendation)

1. **Google-recensionsantal `{N}` + aktuellt 5,0.** Låser upp varje ankrad betygs-instans (trustrow, form-
   microrad, testimonials-badge). *Rek:* bekräfta antalet; tills dess rendera stjärnor + "Betyg på Google"
   UTAN siffran "5,0" (candour).
2. **Testimonials — öppna designen eller ej.** Inom V1-lås = config (pinning/badge/peek). Öppnad = content-
   hug + teal-stjärnor + ärlig navigation. *Rek:* godkänn **Riktning B** (minsta avvikelse, dödar tomrummet
   som är blockets största defekt) som owner-gated visuell diff.
3. **Kanonisk Ring-knappsfärg.** Midnight `#090b32` (sajt) vs emergency-green (eljour) vs teal-fylld. *Rek:*
   midnight globalt, emergency-green ENBART på eljour, teal-fyll som dokumenterat alt.
4. **Stjärnfärg teal vs guld sajtövergripande.** *Rek:* teal (token-disciplin) — dra tillbaka guldet.
5. **MainCTA "inom 60 sekunder"-rubriken.** Behåll (om verklig time-to-human-SLA) eller byt till "Prata
   direkt med en elektriker". *Rek:* bekräfta SLA:t eller använd fallback — hitta aldrig på svarstid.
6. **Kanonisk kundsiffra.** "1000+ kunder" (bannat) vs "3 000+ installationer/år". *Rek:* lås "3 000+/år" om
   ägar-bekräftat; annars `[GAP]`. Löser intern motsägelse på 114+ sidor.
7. **MainContact fält-diet.** Namn+telefon (callback-min) vs dagens 6 fält. *Rek:* A/B spårat till Closed Won,
   default = callback-minimum + "Lägg till detaljer (valfritt)".
8. **24h-återuppringnings-SLA som skriftligt löfte** (thank-you + form-mikrocopy). *Rek:* bekräfta ops-SLA
   eller mjuka till "hör av oss så snart vi kan" — aldrig ett snävare tal än ops kan hålla.
9. **Certifikat — partner-loggor i footern.** Vilka överlever? Rexel (grossist) späder myndighet. *Rek:* släpp
   Rexel; behåll Trygg-Hansa/ID06 tonade; lägg ESV-registerlänk (`?foretag=…`) bara i footer + FAQ.
10. **Reg.nr/org.nr i klartext** för behörighets-chip (footer/FAQ). *Rek:* leverera numret — det är sajtens
    starkaste trust-tillgång, idag en 49px anonym logga.
11. **Sticky mobil-barer (appighets-risk för 35–65).** Eljour call-bar + artikel mini-bar. *Rek:* skeppa
    eljour-baren (akut JTBD motiverar den), A/B artikel-baren, ej default.
12. **Prisblock — kanonisk siffra per vertikal + interna motsägelser** (laddbox 4 190 grid vs "~5 000" FAQ;
    produkt 69 000 vs FAQ). *Rek:* lås EN siffra per vertikal FÖRE rollout — blocket förstärker annars just
    den motsägelse det finns för att döda.
