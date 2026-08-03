# Spec — Proof-mönstret (TrustStrip omprövad)

**Ägarinvändningen är bindande:** en Elsäkerhetsverket-länk mitt i tratten EXPORTERAR besökaren
("det leder ju folk bort från sajten"). Den här specen löser verifieringsvärdet så att det landar
UTAN att skicka bort någon: bevisets *fakta* (registrerat, försäkrat, betygsatt) renderas som en
statisk märkesrad med **noll utlänkar i beslutszonen**; verifieringens *handling* (att slå upp
registret) flyttas till kanten (footer + en FAQ-svarsrad) där besökaren själv söker upp den.

Bygger vidare på `trust-elements-design.md` (PROOF-D1…D10 + beslutszons-råmaterialet) och
`call-cta-design.md` (MainCTA-förädlingen, 5,0-radens borttag). Repeterar inte deras fynd — bygger
komponenten de pekade mot. Tokens: teal `#00a991`, midnight `#090b32`, Outfit, ap*-skala.

---

## Vad ögat möter idag (mobil) — de fyra bevis-ytorna

Kontrollerat mot tiles, inte mot JSON:

- **Hero-trust-rad (svc-elcentral m01).** Under CTA-paret sitter en centrerad rad: färg-**G** +
  "**5.0** ★★★★★" i **teal stjärnor**. Inget recensionsantal, ingen ankring — bara ett tal och fem
  stjärnor på mörk navy hero. Länkar ut till Google Business Profile.
- **MainCTA-microrad (svc-elcentral m08).** Direkt under den ljusblå Ring-pillen: **G** + "**5,0** på
  Google" (fet) + fem **guldstjärnor**. Guldet glimmar och blir terminal blickvila — exakt ägarens
  fröfynd. Samma betyg, annan färg (guld ≠ hero-teal) på samma sida.
- **Form-panel (svc-elcentral d13).** `.aof`-formkortet: "**Få kostnadsfri rådgivning!**" +
  "Vår behöriga elektriker återkommer via telefon!" + Privat/BRF/Företag-toggle. **Noll bevis-märke
  i eller intill formkortet** — "behörig" nämns bara i prosan, aldrig som visuellt märke. Beslutszonen
  där leadet faktiskt lämnas är bevis-naken.
- **Produkt-beslutszon (prod-sigenstor m02).** Prisrader ("Totalt **Fr. 69 000 :-**", ordinarie
  138 000 struket, "Grön teknik 50%") → ljusblå "**Få skräddarsydd offert →**" → expert-kort under:
  teal-foto (blond kille, ampy-tröja) + "Rådfråga vår expert om ditt hembatteri!" + telefonnummer +
  **G** + "**5.0** ★★★★★" (teal stjärnor). Ansiktet är starkt; betyget dubbleras (igen) här.

**Modellen finns redan (geo-eljour m03).** Eljour-symptomblocket: grön pill "● Jour öppen just nu" →
fyra rader med **teal linje-glyfer** (klocka / stoppur / sköld-bock / prislapp) → sista raden
"**Tydligt pris innan vi rycker ut, inga dolda avgifter**" → grön Ring-pill. Lugnt, glyf-lett,
candour-USP:en synlig. Detta ÄR proof-mönstret — komponenten nedan lyfter dess DNA till hero, form
och produkt.

## Vad ögat möter idag (desktop)

Samma atomer, sida-vid-sida. Hero_2 (svc-elcentral d13): vänsterkolumn bär trust-raden, höger
form-panelen — men bevis-märket sitter i FEL kolumn (vänster prosa) och saknas i höger (formuläret).
Certifikatväggen (block 15, `[FRÅN SPEC — ej i mina tiles]`): sex vita logokort på navy→blå gradient
(Elsäkerhetsverket, Skatteverket, Naturvårdsverket, ID06, Trygg-Hansa, Rexel), **var och en utlänkad**
— sex utgångar strax före sista CTA, myndighet blandad med grossist (Rexel). Det är precis den yta
ägarinvändningen gäller.

---

## Fynd (design-nivå, proof-pattern-specifikt)

| ID | Element | Problem | Evidens |
|----|---------|---------|---------|
| **PP-01** | Verifiering = utlänk | Certifikatväggens 6 utlänkar + hero-radens GBP-länk exporterar besökaren i beslutszonen. Verifieringens *värde* (att Ampy ÄR registrerat) är kopplat till en *handling* (lämna sajten) som inte behöver ske här. | cert §15, svc m01 |
| **PP-02** | Betyget hävdas 3–5×/sida i olika färg | Hero (teal stjärnor) + MainCTA (guld) + testimonial-guldrad + produktexpert (teal) — samma "5,0", tre färgkodningar, inget antal. Upprepning devalverar; färgsplittringen ser oavsiktlig ut. | m01, m08, prod m02 |
| **PP-03** | Formkortet är bevis-naket | Den enda ytan där leadet faktiskt lämnas (`.aof`-panelen) bär inget synligt bevis-märke — "behörig" göms i mikrotexten. Beslutsögonblicket saknar trygghetsankare. | svc d13 |
| **PP-04** | Ingen behörighets-/försäkringsmärke som DESIGN | "Registrerat elinstallationsföretag" och "ansvarsförsäkrad" — de två bevis en orolig svensk husägare letar efter (slutpris + skadeansvar) — finns bara som utlänkad logga i cert-väggen, aldrig som statiskt märke i tratten. | cert §15 |
| **PP-05** | "5,0" utan antal = candour-flagga | Renderas som blank fakta utan recensionsantal (bannat om ej ägar-bekräftat aktuellt). Måste bära ett antal eller nedgraderas. | m01, m08 |
| **PP-06** | Produkt-expertkortets betyg dubblerar sidans betyg | Teal 5,0 i expertkortet + testimonials + main-contact på samma produktsida = 3 instanser. | prod m02 |

---

## Kärnbeslutet: var verifieringslänken bor (ärligt svar)

**Har en utgående Elsäkerhetsverket-länk NÅGON plats? Ja — men aldrig i beslutszonen.**
Verifieringen delas i två separata saker:

- **Verifieringens VÄRDE** (faktumet: "Ampy är ett registrerat elinstallationsföretag, ansvarsförsäkrat,
  5,0 på Google") → renderas som **statiskt märke, ingen länk**, i varje beslutszon (hero, form, produkt,
  metrics). Detta bär hela trygghetsvinsten utan att någon lämnar sidan.
- **Verifieringens HANDLING** (att slå upp registret själv) → flyttas till **kanten**, där besökaren är
  klar eller aktivt söker:
  1. **Footer** — en rad "Registrerat elinstallationsföretag · reg.nr `[GAP]` — kontrollera hos
     Elsäkerhetsverket" med `target="_blank" rel="noopener"`. Längst ner = ingen het lead dras bort.
  2. **En FAQ-rad** — "Är Ampy ett registrerat elinstallationsföretag?" → svar med reg.nr i klartext +
     "kontrollera själv hos Elsäkerhetsverket"-länk (ny flik). Den som läser FAQ verifierar avsiktligt;
     att ge länken där **betjänar** intentionen, exporterar inte ett varmt lead.

**Aldrig utlänk i:** Hero_2, Hero-1, MainCTA, `.aof`-formpanelen, main-contact, produkt-beslutszonen,
metrics. I dessa zoner är märket ett **icke-klickbart** grafiskt element. Det är den ärliga upplösningen
av TrustStrip-frågan: värdet skeppas överallt, handlingen bara vid kanterna.

---

## Komponenten: `ampy-trustrow` (den ena återanvändbara byggstenen)

En horisontell, **icke-länkad** rad av bevis-chips. En Bricks-komponent, chip-uppsättning styrd per
placering. Ersätter både den bara betygsraden OCH certifikatväggens jobb.

### Chip-vokabulär (atomerna)

Varje chip = **20px teal linje-glyf** (`stroke #00a991`, 1.75px, aldrig fylld svart cirkel — det var
metric-kortens fel, PROOF-D1) + **label** (`ap-caption` ~14px, Outfit 500, midnight `#090b32` @ 85%).
Chips är default **icke-interaktiva** (`pointer-events:none`, ingen `<a>`). Glyferna:

| Chip-id | Glyf | Label (svenska, ampy-röst) | Candour-not |
|---------|------|----------------------------|-------------|
| `chip-behorig` | sköld-bock | **Registrerat elinstallationsföretag** | Sann regel-fakta. Reg.nr `[GAP]` ägar-bekräftas för footer/FAQ. Märket i zonen kräver ingen siffra. |
| `chip-forsakrad` | paraply/sköld | **Ansvarsförsäkrad** | Från cert-väggen (Trygg-Hansa). "hos Trygg-Hansa" endast om aktuellt `[bekräfta]`. |
| `chip-pris` | prislapp | **Fast pris innan vi börjar** | Candour-USP, redan i eljourblocket. Svarar husägarens #1-oro (slutpris). |
| `chip-rot` | kvitto/procent | **ROT & Grön teknik direkt på fakturan** | 30% ROT / 50% grön teknik = ägar-låst kanon. |
| `chip-garanti` | märke-bock | **{X} års garanti** | Endast produktsida; X från produktdata (`10 år` sett på prod m02). |
| `chip-betyg` | Google-**G** (färg) | **5,0** ★★★★★ **({NN} omdömen)** | Antalet `[GAP]` ägar-bekräftas. Utan antal → visa stjärnor + "Omdömen på Google" UTAN "5,0"-talet. Detta är enda chip som får bära en `<a>` till GBP — men bara i form-microraden, se nedan. |

**Betygschipets stjärnor: EN färg per sajt.** Välj **teal** (matchar hero + produkt-expert idag) och
**dra tillbaka guldet** överallt (MainCTA-guldet försvinner ändå per call-cta dir 2). Aldrig teal och
guld på samma sida (PP-02).

### Layout / mekanik

- **Desktop:** `display:flex; flex-wrap:wrap; align-items:center; gap:20px 28px;` chips på EN rad,
  åtskilda av en 1px `rgba(9,11,50,.12)` vertikal hårstreck (`::before` på varje chip utom första)
  eller en `·` i midnight @ 40%. Radhöjd ~44px. Ingen bakgrund (transparent) i ljusa zoner; på navy
  hero: label byter till `#ffffff` @ 88%, glyf behåller teal.
- **Mobil (<560px):** `flex-wrap:wrap`. 2–4 chips → 2 rader; behörig+försäkrad+pris staplas som en
  **vänsterjusterad lista** (glyf-kolumn 24px + label), radavstånd 12px — läses som eljourblockets
  glyf-rader (den mall som redan fungerar). Betygschipet står ensamt först, centrerat, ovanför listan.
- **Chip-intern:** `inline-flex; align-items:center; gap:8px;` glyf 20px, label `ap-caption`.
- **States:** statisk. Ingen hover, ingen fokus-ring (icke-interaktiv). Undantag: `chip-betyg` när den
  bär GBP-länk i form-microraden → `:hover` underline på "omdömen"-ordet, `:focus-visible` 2px teal
  outline, resten av chipet inert.
- **A11y:** varje glyf `aria-hidden="true"`; chip-raden `role="list"`, chip `role="listitem"`; hela
  raden får `aria-label="Ampys behörighet och betyg"`. Betygschip utan länk = ren text (inget
  `<button>`).

---

## Anatomin per yta (bygg-färdig)

### 1. Hero trust-row (Hero_2 `.aof` + Hero-1)

**Ersätter** den bara "G 5.0 ★★★★★"-raden under CTA-paret.

- **Placering:** kvar där betygsraden sitter idag — direkt under CTA-paret, ovanför/vid formkortet.
- **Vänsterkolumn (Hero_2) / under CTA (Hero-1):** `ampy-trustrow` med **två chips**:
  `chip-behorig` + `chip-betyg`. Betyget behåller Google-G; **stjärnor teal**; antal `[GAP]`.
  På navy hero: labels vita, glyf/stjärnor teal.
- **Ingen utlänk** i hero-instansen (till skillnad mot idag). Betygschipet här är icke-klickbart —
  form-microraden (yta 3) bär den enda klickbara GBP-länken om en behövs.
- **Mobil:** de två chipsen centrerade, staplade om det inte får plats (betyg överst, behörig under),
  radavstånd 10px. Höjd ~64px totalt.
- **Storlek:** label `ap-caption` 14px; betygstalet "5,0" `ap-h5` 18px 600 inline, stjärnor 16px.

### 2. Behörighetsband (NY tunn sektion — certifikatväggens ersättare)

Det block som gör certifikatväggens jobb utan utlänkar. **En horisontell märkesrad, full bredd,
låg höjd.**

- **Placering:** EN instans per sida, i beslutszonen — rekommenderat **strax ovanför `main-contact`**
  (sista formuläret) ELLER direkt under hero på korta sidor. Ersätter `certificates` §15 i sidflödet.
- **Innehåll:** `ampy-trustrow` med **fyra chips**: `chip-behorig` · `chip-forsakrad` · `chip-pris` ·
  `chip-rot`. Icke-länkade.
- **Yta:** ljus — vit eller `#f5f9ff`; ELLER dämpad aurora-mesh (behåll varumärkesytan men sänk mesh
  ~30% så midnight-label når AA, per trust-elements dir 2). Ingen tung navy-gradient (den bar de gamla
  logokorten).
- **Höjd:** desktop ~72px (en rad, centrerad, chips gap 28px). Mobil: 2×2 rutnät eller vänsterjusterad
  4-radslista, ~180px.
- **Rubrik:** valfri liten eyebrow `ap-overline` "TRYGGT HELA VÄGEN" i teal, 12px, letter-spacing .08em
  — eller ingen rubrik alls (chipsen talar själva). Inga sex logotyper. Inga utgångar.
- **Partner-loggorna (Trygg-Hansa, ID06, Rexel)** flyttas till en **tonad, mindre logorad i footern**
  (gråskala, opacitet 60%, höjd ~40px), åtskild från myndighetsbudskapet (dir 10a). Rexel lämnar
  beslutszonen helt.

### 3. Form-panel microrow (`.aof` + main-contact)

**Löser PP-03** — beviset i själva formytan.

- **Placering:** en enda kompakt rad **under submit-knappen** ("Boka rådgivning" / "Gratis rådgivning"),
  ovanför/istället för den nakna integritetsraden — eller precis under formrubriken. Rekommenderat:
  **under submit**, som sista trygghets-touch innan avslut.
- **Innehåll:** `chip-behorig` + `chip-betyg`. Kompakt: glyf 16px, label 13px.
- **Detta är sidans betygs-instans nr 1** (top-formen). Betygschipet HÄR får bära den **enda tillåtna
  GBP-länken** om ägaren vill ha en — `<a target="_blank">` bara på "omdömen"-ordet, resten inert.
  Motivering: den som redan står vid formuläret och vill dubbelkolla betyget ska kunna, men default är
  icke-länkad för att inte exportera. Ägar-val.
- **main-contact:** dess vänsterpanel bär REDAN ett ankrat "5 av 5 · Betyg på Google" (skyddat, se
  call-cta). Lägg då INTE till betygschip i main-contacts microrow — bara `chip-behorig` +
  `chip-forsakrad`. Betyget står redan i vänsterpanelen (sidans instans nr 2, botten-formen, långt
  ifrån hero-instansen — tillåtet, se not om "en per skärm").
- **Mobil:** en rad, centrerad, wrap till två vid behov.

### 4. Produkt-beslutszon (`product` hero + expert-kort)

- **Prisrad → offert-CTA (behåll ordningen).** Under "Grön teknik 50%"-raden, **före** "Få skräddarsydd
  offert", lägg `chip-pris` ("Fast pris innan vi börjar") + `chip-garanti` ("10 års garanti" — X från
  produktdata) som en tvåchip-rad. Svarar prisoro exakt där priset visas.
- **Expert-kort (behåll — ansiktet är starkast).** Behåll teal-fotot + "Rådfråga vår expert" + telefon.
  Betygschipet HÄR = produktsidans **enda** betygs-instans (ta bort testimonial-guldraden och ev.
  main-contact-dubblett per PP-06). Stjärnor teal. Antal `[GAP]`.
- **Behörighetsband (yta 2)** placeras även på produktsidan, ovanför main-contact — bär behörig +
  försäkrad + ROT/grön-teknik. Certifikatväggen tas bort ur produktflödet (§24-flödet listar den; den
  ersätts).
- **Mobil:** tvåchip-raden staplas under prisraden (prod m02 har gott om vertikal plats där); expert-
  kortet oförändrat.

---

## Betygs-instanserna per mall (candour + "en per skärm")

"Ett betyg per sida" tolkas ärligt som **inget staplande på samma skärm**; två form-zoner 6 skärmar
isär får var sin ankrad instans.

| Mall | Behåll betyg | Ta bort betyg | Bär behörig/försäkrad |
|------|--------------|---------------|------------------------|
| Service (Hero_2 + main-contact) | Form-microrad (top) + main-contact vänsterpanel (botten) | Hero-radens bara 5.0 → blir `chip-behorig`; MainCTA-guldraden; testimonial-guldrad | Behörighetsband ovan main-contact; hero-chip; form-microrad |
| Produkt | Expert-kortet (enda) | testimonials-guldrad; ev. main-contact-dubblett | Behörighetsband + pris/garanti-rad |
| Om oss | EN strip ovanför kontaktformuläret | — (idag noll → lägg till EN) | Behörighetsband + teamansikten (PROOF-D3) |
| Geo/pillar | Form-microrad | Hero-bara-5.0; MainCTA-guld | Behörighetsband |

Antalet recensioner (`{NN}`) är **`[GAP]` — ägar-bekräftas** innan "5,0" visas som tal. Saknas
bekräftat antal: rendera stjärnor + "Omdömen på Google", utan sifferpåståendet "5,0" (candour-gate,
PP-05). "1000+ Nöjda kunder" utgår helt (bannat, MET-01) — metric-blocket byter till "3 000+
installationer/år" per trust-elements dir 3, separat block.

---

## Candour-gate (blockerande)

1. **Ingen utlänk i beslutszonen.** Hero/form/produkt/metrics = icke-klickbara märken. Registerlänk
   endast footer + FAQ, `target="_blank"`.
2. **"5,0" bara med antal** — annars stjärnor utan tal. Antal = `[GAP]` ägar-bekräftat.
3. **"Registrerat elinstallationsföretag"** = sann regel-fakta; reg.nr `[GAP]` i footer/FAQ, ej påhittat.
4. **"Ansvarsförsäkrad"** — sant (cert-vägg); försäkringsbolagets namn bara om aktuellt.
5. **Ingen falsk brådska/knapphet.** Ingen "endast X kvar", ingen nedräkning. (Ej relevant här men
   gäller.)
6. **En stjärnfärg per sida** (teal). Guld dras tillbaka.
7. **Aldrig "1000+ kunder"** som största tal. Byt till belagt tal i separat metric-block.

---

## Reasoned against existing blocks

- **vs Certificates §15 (partner-logovägg):** ersätts. De sex utlänkade logokorten → (a) icke-länkat
  **behörighetsband** (myndighet/försäkring/pris/ROT som chips) i beslutszonen + (b) tonad partnerlogo-
  rad i footern (Trygg-Hansa/ID06/Rexel, gråskala). Nettoresultat: **6 mid-funnel-utgångar borttagna**,
  Rexel-grossisten späder inte längre myndighetsauktoriteten, verifieringslänken flyttad till kant.
- **vs Metrics §22 (3 talkort):** komplement, ej dubblett. Metrics bär **tal/skala** (3 000+ inst./år),
  behörighetsbandet bär **auktoritet/trygghet** (märken). De får inte upprepa varandra; metric-blocket
  byggs om separat (trust-elements dir 1–3). På sidor med båda: metrics högre, behörighetsband i
  beslutszonen nära formen.
- **vs Hero_2/Hero-1 betygsrad §1/2:** den bara "5.0 ★★★★★" byts mot `chip-behorig` i hero + betygschip
  i form-microraden. Ingen tappad information — betyget flyttar närmare avslutet, auktoriteten blir
  synlig som märke.
- **vs MainCTA §5:** inget trustrow läggs till här. 5,0-guldraden tas bort (call-cta dir 2); ansikte +
  förädlad Ring-knapp är nog. Behörighet bärs av behörighetsbandet på sidan, inte i MainCTA.
- **vs Testimonials §9:** kortens inre (mint stjärnor, Google-G, citat) skyddas. Endast den fristående
  guldiga "5 av 5"-raden under carousellen tas bort — betyget bärs redan av form-microrad/expertkort.
- **vs main-contact §4:** dess ankrade "5 av 5 · Betyg på Google" + "3 000+" skyddas (starkaste
  konverteringsytan). Behörighetsbandet placeras OVAN den; main-contact-microraden bär bara
  behörig+försäkrad (inte ännu ett betyg).
- **vs Eljour-symptomblocket:** rörs inte — det ÄR mönstret. `ampy-trustrow` lånar dess glyf-rad-DNA
  (teal linje-glyfer, "Tydligt pris"-raden, källhänvisad ton). Bygg inte om eljourblocket.
- **vs Footer §29:** får två nya element — den tonade partnerlogo-raden OCH registerraden
  ("kontrollera hos Elsäkerhetsverket", ny flik). Det är den enda platsen utlänken lever.

---

## Divergenta riktningar (behörighetsbandet — huvudingreppet, husregel 3)

- **A — Chip-band (rekommenderad).** Fyra icke-länkade chips på en rad (behörig · försäkrad · pris ·
  ROT), teal glyfer, ljus/dämpad-aurora yta. Tätast, snabbast, noll utgångar, lånar eljour-DNA.
  Risk: mindre "institutionellt" än logotyper. Bäst för alla sidor.
- **B — Ett förtroendekort.** Ett enda kort: rubrik "Behörigt, försäkrat, tydligt" + tre belagda rader
  med teal-bock + reg.nr i klartext (ingen extern länk). Mer "dokument"-känsla, bär reg.nr synligt utan
  att länka. Risk: mer höjd. Bäst på Om oss/kontakt (trust-destinationer).
- **C — Hybrid märke + tonad logorad.** Chip-bandet (A) i beslutszonen PLUS en mycket dämpad,
  gråskale-logorad (Elsäkerhetsverket-ordmärke + Trygg-Hansa) som *ornament* under, helt utan länkar.
  Behåller en logotyps visuella auktoritet men dödar utgångarna. Risk: närmar sig gamla väggen — håll
  loggorna små och länklösa. Bäst där ägaren vill ha kvar logotyp-tyngden.

Alla tre delar tre invarianter: **(1) noll utlänk i beslutszonen, (2) en stjärnfärg (teal), (3)
belagt före volym** (märke/antal, aldrig "1000+").

---

## Vad som INTE ska röras

- **Eljour-symptomblocket** — mönstrets förlaga. Låna FRÅN det, ändra det inte.
- **Edvin/Magnus teal-foto** i MainCTA + produkt-expertkort — starkaste ansikts-beviset, behåll intill
  call-CTA:n.
- **main-contact vänsterpanel** ("5 av 5 · Betyg på Google" + "3 000+ … om året" + 3-stegen) — ankrat,
  legitimt, skyddat.
- **Testimonial-kortets inre** (mint stjärnor, Google-G, citat, namn+datum). Bara den dubblerade
  guldraden under carousellen tas bort.
- **Aurora-gradienten som varumärkesyta** — behåll, dämpa bara meshen för AA-kontrast.
- **Google-G:et** som betygsmarkör — igenkännbart, behåll. Bara stjärnfärgen enhetliggörs (teal).
