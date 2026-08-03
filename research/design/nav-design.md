# Nav-design — Header + mobilnav + prefooter/footer (visuell round-2-audit)

Scope: den globala headern (båda viewporterna, 4 sidor), mobilnavens tel-affordans, samt
prefooter (`Populära kategorier`) + footer + footer-bar. Grundat i tiles för `home`,
`svc-elcentral`, `artikel-elcentral`, `kontakt`.

**Anti-teater — vad jag INTE kunde se (sägs rakt ut):** ingen tile visar (a) den öppna
hamburger-offcanvasen, (b) de öppna mega-menypanelerna (Tjänster/Produkter/Lösningar),
(c) home-mobilens footer (home-mobile slutar på produktkorten, tile 27, före footern).
Mobilfootern jag granskar kommer från `kontakt--mobile--03/04/05`. Allt om mega-menyns
densitet och offcanvasens innehåll är därför **oobserverat** och flaggas som hypotes, inte
fynd. Block-inventariet (§28) säger att offcanvasen innehåller "Ring en expert" + Google-betyg
— jag tar det som uppgift, inte som sett.

---

## Vad ögat möter (mobil)

**Header** (`home/svc/artikel--mobile--01`, identisk på alla tre): tre element på en ljus rad
`#f5f9ff` — svart **ampy**-logga vänster, en grön gradient-pill **"Gratis rådgivning"**
**centrerad** (med en lysande grön puls-prick under-höger), och en svart hamburger längst till
höger. Ögat landar på den gröna pillen först (mättad grön mot ljus bakgrund + puls), loggan
andra, hamburgern sist. **Inget telefonnummer syns någonstans i headern.** Den centrerade pillen
sitter obalanserat mellan logga och hamburger — den är varken vänster-ankrad till varumärket
eller höger-ankrad till handlingszonen, den "flyter".

**Prefooter** (`kontakt--mobile--03/04`): "Populära kategorier" på en ljus cyan-gradient, där de
fem kolumnerna (Elinstallation → Laddboxar → Batterilagring → Områden → Lösningar) **staplas
vertikalt till en enda lång vägg**: 5 feta rubriker + ~15 identiska gråa textlänkar under
varandra, alla samma vikt, ingen ikon, ingen gruppering utom luft. Det är ~20 tap-mål i en rak
remsa som ögat inte kan skanna — det bara sveper förbi.

**Footer** (`kontakt--mobile--04/05`): hård övergång cyan → midnattsblå `#090b32`. Vit **ampy**-
logga, brödtext-tagline i dämpat blågrått, 5 sociala ikoner (LinkedIn/IG/FB/Reddit/TikTok),
sedan staplade rubrik-kolumner **Mer om Ampy** och **Kundtjänst**, och först **allra sist**:
"Få en kostnadsfri konsultation!" + adress (Västbergavägen 25, 126 30 Hägersten) + `bokning@ampy.se`
+ **010-265 79 79** + Google "5.0 ★★★★★". Footer-bar: "© 2026 Ampy Nordic AB – All Rights
Reserved" + Tillgänglighetsredogörelse / Cookie policy / Integritetspolicy (centrerade).
Nettoeffekten: telefonnumrets enda pålitliga hemvist ligger efter hela länkväggen — det är det
sista man når.

## Vad ögat möter (desktop)

**Header** (`home/svc/artikel/kontakt--desktop--01`, identisk): logga vänster | mega-nav
centrerad (**Tjänster ▾ · Produkter ▾ · Lösningar ▾**, tre poster, rena) | **"Gratis rådgivning"**
grön pill längst till höger med puls-prick. Mellan "Lösningar" (~920 px) och pillen (~1140 px)
finns **~500 px tom yta** på 1440-canvasen. Headern är luftig och balanserad — men även här
**noll telefon-affordans**. Den enda persistenta konverteringsvägen i global-nav är formuläret;
telefonen (Ampys lägst-friktion, högst-intent money-path, hela MainCTA-tillgången bygger på
"prata med en elektriker inom 60 sekunder") finns inte i navigationen alls.

**Prefooter** (`home--desktop--11`): "Populära kategorier" i 5 prydliga kolumner på cyan — här
fungerar rastret (skannbart, jämna kolumner). Rubrikerna är feta svarta, länkarna mörkgrå. Ren.

**Footer** (`home--desktop--12`): midnattsblå, tre logiska block — tagline+socialt+Google-betyg
vänster | länkkolumner (Om oss/Jobba hos oss/Nyheter & Artiklar · Support/ROT avdrag 2026/Grön
Teknik 2026) mitten | "…konsultation!" + adress/mail/**010-265 79 79** höger. Footer-baren
högerställd med policy-länkar. Prydlig, men telefonen är plain text i en hörnkolumn — ingen
visuell tyngd trots att det är en av bara två konverteringsvägar.

---

## Fynd

**NAV-01 — Telefonen saknas i den globala headern (båda viewporter).** Sajten har exakt två
konverteringar (ring / formulär, per business-context). Headern surfar bara den ena. För en
elfirma där samtalet är den snabbaste, mest kvalificerande och för akut-intent (elfel, eljour)
den *enda* rimliga vägen, är det ett strukturellt tapp att inte ha en tel-affordans i det enda
element som följer med på varje sida och varje scroll-position. Evidens: GA4 visar 2 phone-clicks
mot 0 form-starts (business-context) — det lilla telefonintresse som finns lyckas *trots* att
numret inte finns i navet.

**NAV-02 — Mobilens "Gratis rådgivning"-pill är obalanserat centrerad.** Den ankrar varken till
varumärke eller handlingszon; den konkurrerar optiskt med loggan om mitten och skjuter hamburgern
till kanten. En centrerad primär-CTA i en 3-elements mobilheader är en ovanlig, rörig lösning.

**NAV-03 — Hamburgern sitter i den svåraste tumzonen, och samtalsvägen är inlåst bakom den.**
Övre höger hörn är den klassiska döda zonen för höger tumme på stora telefoner (35–65-publiken
använder ofta större enheter). Enligt inventariet ligger "Ring en expert" *inuti* offcanvasen —
alltså kräver ett samtal på mobil: nå övre-höger hörn → öppna meny → hitta ring-raden. Money-path
med tre steg och ett tumsträck. (Offcanvasen själv oobserverad — men placeringen av triggern är
sedd.)

**NAV-04 — Prefooter-väggen på mobil (~20 staplade länkar) sänker skannbarheten och skjuter
footern/kontakten nedåt.** SEO-intern-länkning är legitim, men den nuvarande vertikala stapeln
har noll visuell hierarki (allt samma vikt/färg) och lägger en lång skroll mellan innehåll och
kontaktuppgifter. Desktop-rastret löser detta; mobilen ärver bara staplingen.

**NAV-05 — Telefon (money-path) begravd sist i footern och utan visuell tyngd.** Numret finns
(bra — NAP komplett med adress + mail), men det är plain text i sista kolumnen/sist i stapeln,
efter hela länkväggen. Det behandlas som en detalj, inte som 1 av 2 konverteringar.

**NAV-06 — Candour-risk: footerns "5.0 ★★★★★" utan antal.** Samma sak som site-wide (block-
inventariet §108, ≥6 block). "5.0" som påstått faktum utan antal recensioner passerar inte
candour-grinden om det inte är ägar-bekräftat aktuellt. Footern upprepar påståendet en gång till.

**NAV-07 — Artikel-mobilens breadcrumb spiller under headern.** `artikel-elcentral--mobile--01`:
"Byta elcentral 2026: pris, ROT-avdrag 30% och vad som in…" trunkeras hårt mot högerkanten precis
under headern. Inte header-komponenten i sig, men det första under den ser trasigt ut. (Noteras;
tillhör artikel-hero-audit att lösa — trunkera på sista segmentet, inte mitt i en titel.)

**NAV-08 — "Få en kostnadsfri konsultation!" i footern är en rubrik utan knapp.** Den ser ut som
en CTA men bär ingen kontroll; adress/mail/telefon under är de enda tap-målen. Antingen gör
telefonen till den uppenbara handlingen, eller ge rubriken en riktig knapp.

---

## Omdesign-direktiv

1. **Lägg en tel-affordans i headern — desktop.** Utnyttja de ~500 px döda ytan till vänster om
   den gröna pillen: sätt **"010-265 79 79"** som en *text-länk med liten telefon-glyf* i
   midnatt `#090b32`, INTE en fylld knapp. Mönstret blir sekundär telefon-textlänk + primär grön
   form-pill — servicesajtens standard. Den grönaste pixeln (formuläret) förblir dominant; ögat
   får ett andra, lägre-friktions-alternativ utan att något trängs. Ingen crowding: navet slutar
   vid ~920 px, telefonen kan sitta ~980–1120 px, pillen från ~1140 px.

2. **Lös mobilheadern: höger-ankra handlingszonen.** Ta bort den centrerade pillen. Höger kluster
   = **[teal telefon-ikonknapp, tap-to-call `tel:+46102657979`] + [hamburger]**. Loggan
   vänster får luft. Telefonen blir ett ett-tums-tryck utan att öppna menyn (löser NAV-03:s
   money-path). "Gratis rådgivning" flyttas till hero-CTA:n (redan stark) + som första rad överst
   i offcanvasen. Ikonknappen ärver samma teal `#00a991` som varumärket; puls-pricken kan flytta
   dit metrerat.

3. **Behåll den gröna form-pillen som primär på desktop, oförändrad.** Den mår bra (mättad,
   balanserad, puls-prick är en affordans-cue, inte fejkad brådska). Rör den inte.

4. **Prefooter mobil: bryt väggen.** Antingen (a) lägg de 5 kategorierna i **kollapsbara
   accordions** (rubrik synlig, länkar under på tryck) så footern/kontakten når man snabbt, eller
   (b) gör ett **2-kolumners raster** som halverar höjden. Behåll desktop-rastret som det är.

5. **Elevera telefonen i footern.** Gör **010-265 79 79** till det visuellt tyngsta i kontakt-
   blocket: större vikt, teal glyf, ev. en tunn teal-outline-knapp "Ring oss · 010-265 79 79".
   Flytta hela "Få en kostnadsfri konsultation!"-blocket **först** i footerns kolumnordning på
   mobil (före Mer om Ampy / Kundtjänst) — kontakt är footern's jobb, inte länk-SEO.

6. **Candour: footerns betyg.** Antingen "5,0 · X omdömen på Google" (om ägar-bekräftat aktuellt)
   eller ta bort siffran och behåll bara Google-märket + länk. Ingen naken "5.0".

7. **NAP som trust, inte som fotnot.** Adress + org (Ampy Nordic AB) + telefon är riktig lokal
   trovärdighet för en svensk husägare (Clarity visar trust-sökande beteende → About Us). Håll
   dem samlade och läsbara; öka radavstånd så de tre raderna andas.

---

## Divergenta riktningar (headerns tel-fråga — big intervention, 3 versioner)

**Riktning A — "Telefon som co-primär" (rekommenderad).** Desktop: text-länk-telefon till
vänster om grön pill (direktiv 1). Mobil: teal telefon-ikonknapp + hamburger, form-pill flyttad
till hero/offcanvas (direktiv 2). Minsta ingrepp, störst reach, respekterar att formuläret ska
förbli primär enligt commercial priority. Risk: telefon-textlänk kan underutnyttjas av ovana
ögon på desktop (mildras av glyf + tydlig färg).

**Riktning B — "Persistent dubbel mobil-bar".** Låt mobilheadern bli minimal (logga +
hamburger), men lägg en **sticky bottom-bar** i två halvor: vänster **"Ring"** (telefon-glyf,
tel:) | höger **"Få rådgivning"** (form). Alltid synlig, alltid ett tryck bort, löser
tumzon-problemet (NAV-03) helt eftersom baren sitter i den lättaste zonen längst ner. Detta är
den starkaste rena-CRO-patternen för mobila servicesajter. Risk: en persistent bar äter ~64 px
vertikal yta och kan kännas "appig" för 35–65-publiken; testa mot A. Kräver z-index/skymmer-
disciplin så den inte döljer form-submit-knappar.

**Riktning C — "Telefon-först header".** Vänd hierarkin: eftersom samtalet är lägst friktion och
"60 sekunder"-löftet är money-path, gör **telefonen till den fyllda knappen** (teal) och
"Gratis rådgivning" till ghost/text-länk. Desktop och mobil. Passar om eljour/akut-intent-trafik
prioriteras (Unbounce: repair/urgent konverterar bäst). Risk: krockar med commercial priority
(service-formulär → kvalificerad lead → offert) och kan sänka form-fill som redan är 0; **endast
för akut-tunga geo/eljour-mallar, inte homepage**. Behåll A globalt, C på eljour-i-{ort}.

**Prefooter (mindre intervention, 2 varianter):** (1) mobil-accordions, (2) 2-kol-raster.
Rekommendation: accordions — de gör kontakt-footern nåbar snabbast, vilket är hela poängen.

---

## Vad som INTE ska röras

- **Desktop-headerns grön form-pill + puls-prick.** Balanserad, rätt kontrast, affordans-cue är
  inte en banned-tactic. Lämna.
- **Trepostiga mega-navet (Tjänster/Produkter/Lösningar).** Rent, luftigt, rätt informations-
  bredd. Lägg inte till fler poster. (Panelernas densitet oobserverad — auditeras separat.)
- **Loggan.** Distinkt, läsbar i både svart (ljus header) och vit (mörk footer). Rör inte.
- **Footerns tagline-copy** ("…en elektriker som går extra milen för ditt hem!"). On-brand
  candour, du-nära värme. Behåll ordagrant.
- **NAP-fakta i footern** (adress, mail, telefon, org). Behåll allt innehåll — direktiven ovan
  *elevera* och *omordnar*, tar aldrig bort någon uppgift.
- **Desktop-prefooterns 5-kol-raster.** Fungerar; endast mobil-staplingen ska brytas.
- **Footer-barens policy-länkar** (Tillgänglighet/Cookie/Integritet). Korrekt, lågmält, rätt.
