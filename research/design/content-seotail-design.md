# SEO-svansen som visuell upplevelse — ContentBlock · VissteDuAtt · CEBlock · FooterSEO

Design-lager (Round 2) ovanpå round-1-strukturen (`blocks/content-block.md`, `visste-du-att.md`, `footer-seo.md`). Round-1-fynd-ID:n (CB-, VDA-, FS-) refereras, upprepas inte.

**Vad jag faktiskt SÅG (anti-teater, golden rule 0):**
- **ContentBlock** — observerad i pixlar på tre sidor: `svc-elcentral` (mobil 14–17), `svc-vitvaror` (mobil 4–6 + **desktop 3–4**), `geo-elinstallation-vaxholm` (mobil 22, en textrad). Desktop-alternering och mobil-stackning verifierade i skärmdump.
- **Services-grid** (`Vårt utbud av eltjänster i Tyresö`) på `geo-elektriker-tyreso` (mobil 18–19, 27–28) — geo-elektriker-mallen bär en **bildkorts-grid** i SEO-svansen istället för de alternerande essä-raderna. Viktigt jämförelseobjekt (se Riktning C).
- **VissteDuAtt / CEBlock / FooterSEO** — **syns INTE i mina fyra tilset.** Alla fyra captures loopar (sidan börjar om) efter Vår process / MainContact innan de når den djupa SEO-svansen (idx ~15–21 där VDA/CE/FooterSEO bor på elektriker-i/produkt). Jag ljuger inte om pixlar jag inte sett: designdirektiven för de tre nedan bygger på round-1:s **verifierade CSS** (exakta tokens/animationer citerade där) + blockinventariet, och är märkta `[från verifierad CSS, ej observerad i mina tiles]`. CEBlock finns dessutom bara på produktsidor (inventarie §25), inte på någon av mina fyra sidor.

---

## Vad ögat möter (mobil, 390px)

**ContentBlock — `svc-elcentral` (14–17) & `svc-vitvaror` (4–6):**
Ögat möter en **enformig vertikal remsa** av tre identiskt formade rader. Varje rad = en **helbred bild ~340px hög** → **H2 på två rader** (mörk marin, ~28px, halvfet) → **två stycken löptext**, vart och ett 4–6 rader mellangrå. Rad 1 och 3 **öppnar med bilden före rubriken** (CB verifierat: mobil stackar i DOM-ordning) — du skrollar alltså ett halvt skärmhögt foto *innan* du får veta vad avsnittet handlar om. Tre rader i följd ≈ **3 foton + 3 rubriker + 6 textstycken ≈ 4–5 skärmhöjder** utan en enda skann-ankare: noll punktlistor, noll fetad nyckelfakta, noll bildtext. Elcentral-texten på tile 17 ("Tecken på att det är dags att byta proppskåp") möter direkt "Så funkar det" — raden **dör in i nästa band utan CTA** (CB-05-släkting).

Rytmen är *värre* på mobil än desktop: desktop alternerar vänster/höger (viss variation), mobil kollapsar allt till **samma form om och om** → "same-same"-trötthet. En 35–65-årig husägare som skrollar möter grå textblock och lämnar (jfr Clarity "23s no-click på Belysning").

**Bildernas motiv (citat av vad jag ser):**
- `svc-elcentral`: öppet proppskåp/elcentral med automatsäkringar och färgad kabeldragning; komponenter utlagda på vägg (gul kabelrulle, uttag, dvärgbrytare); ett stort industriskåp med brokig kabelmatta; ännu ett öppet elskåp. **Ämnesrelevant (elcentral) men generiska AI/stock-renders** — ingen är daterad, platsangiven eller bildtextad.
- `svc-vitvaror`: iscensatt modernt kök med öppen diskmaskin full av vita tallrikar; grått kök med rostfri diskmaskin; ljusblått kök med diskmaskin + **torkade blommor i vas**; marmorbänk. Ämnesrelevant (vitvaror) men uppenbart **AI-iscensatt inrednings-stock** (torkade blommor, stylad rekvisita) — läser som möbelkatalog, inte som "riktigt jobb hos en kund".

**Services-grid — `geo-elektriker-tyreso` (18–19, 27–28):** Här möter ögat istället **vita kort**: foto (~4:3) → kort rubrik (Elcentral / Köksrenovering / Luftvärmepump / Smarta hem / Spotlights / Belysning) → **en rad bildtext** ("Ny elcentral i Tyresö? Vi byter och säkrar enligt dagens krav.") → himmelsblå pill "Till {tjänst}". Detta är **markant mer skannbart** än ContentBlocks essä-rader — kort motiv, en mening, tydlig affordans. Motiven är dock samma AI-stock-klass (LG-värmepump mot träpanel i snö, pendellampa, takspottar).

**VissteDuAtt** `[från verifierad CSS, ej observerad]`: mörkt marinblått kort (**#010328**, inte kanon-midnight #090b32), vit tunn text (**font-weight 300**), och en **absolut­positionerad glödlamps-PNG som gungar 4s** (swing, ingen `prefers-reduced-motion`-spärr) och överlappar kortets övre högra hörn; H2 knuffas ner med `margin-top` bara för att rensa lampan → dödyta + rörelse högst upp i kortet före ett enda ord.

**FooterSEO** `[från verifierad CSS, ej observerad]`: vitt band, vänsterställd H2, ~45 ords stycke, CTA-paret ("Kostnadsfri **radgivning**" [sic, saknar å] → /kontakt/ + "Ring…" → tel:), stor **maskad landskaps-webp (1200×600) absolut nere till höger** som dekorativ fyllnad; blir "ett högt, mestadels tomt vitt band" ovanför prefooter.

## Vad ögat möter (desktop, 1440px)

**ContentBlock — `svc-vitvaror` desktop 3–4:** Klassisk alternerande zig-zag: **bild ~600px rundad** i ena kolumnen, textkolumn (~40%) i den andra — I/T, T/I, I/T. På desktop **fungerar** rytmen bättre: rubrik läsbar (mörk, halvfet, ~30px, 2 rader), två textstycken i behaglig radlängd, läsbar mellangrå. **Men två defekter syns tydligt:**
1. **Höjd-obalans** — textkolumnen är kortare än bilden. Rad 1: texten slutar ~y490 medan bilden går till ~y560 → **dödyta under texten**; raderna är inte vertikalt centrerade mot varandra, vilket ger ett hoppigt högervänster-hål.
2. Fortfarande **vägg av löptext** — noll punkter, noll fetad fakta, ingen bildtext. Bilden bär 600px bredd × ~550px höjd **ren dekoration** bredvid texten (CB-02).

Desktop-svansens övergång ContentBlock → Vår process (svc-vitvaror desktop 5) är ren och luftig — processblocket är det *enda* i svansen med skann-ankare (ikon + numrerad kort rubrik + 3-rads text i 4-kolumn).

**FaQ + MainContact** avslutar desktop-svansen på service-sidorna (svc-vitvaror desktop 6): FAQ-ackordeon 55% + köksbild 45% — bilden här är återigen dekorativ AI-stock, inte informationsbärande.

---

## Fynd

| ID | Block · yta | Vad ögat träffar / problem | Evidens |
|---|---|---|---|
| **D-CT-01** | ContentBlock · mobil | Tre identiskt formade rader → uniform "same-same"-remsa, noll skann-ankare (0 punktlistor, 0 fetad fakta, 0 bildtext). Rad 1 & 3 öppnar med ~340px bild *före* rubriken. | svc-elcentral 14–17, svc-vitvaror 4–6; jfr CB-01 |
| **D-CT-02** | ContentBlock · desktop | Höjd-obalans: textkolumn kortare än 600px-bilden → dödyta, overtikalt ojusterade rader; ändå textvägg utan bullets. | svc-vitvaror desktop 3–4 |
| **D-CT-03** | ContentBlock · båda | Bilderna är AI-iscensatt stock (torkade blommor, katalog-kök; generiska elskåp) — ämnesrelevanta men **noll informationsvärde, noll trovärdighetsbevis**, kostar 340px mobil / 550px desktop styck. Ingen bildtext (den mest lästa copyn på en sida, Ogilvy — outnyttjad). | svc-vitvaror 4–6, svc-elcentral 14–17; jfr CB-02 |
| **D-CT-04** | ContentBlock · båda | H2-vikten för låg (round-1: `--aptext-xl` **weight 400** ≈ knappt tyngre än brödtext) → de enda skann-ankarna är svaga. Brödtext ≤780px faller till `--aptext-sm` weight 300 (tunt grått smått för den äldsta målgruppen). | CB-01/CB-05 verifierad CSS; svc-vitvaror mobil 4–6 |
| **D-CT-05** | ContentBlock · geo | På geo-elinstallation-vaxholm är raden **ett enda 8-radigt stycke** ("Många hushåll väljer idag att investera i smart belysning…") — ännu tätare än service-sidornas 2-styckes-rad. | geo-elinstallation-vaxholm mobil 22 |
| **D-CT-06** | Services-grid vs ContentBlock · geo | geo-elektriker-mallen har ett **mer skannbart** SEO-mass-mönster (kort + 1-rads bildtext + pill) än service-sidornas essä-rader — bevis på att kort-mönstret redan finns i systemet och kan lånas. | geo-elektriker-tyreso 18–19, 27–28 |
| **D-VDA-01** | VissteDuAtt | `[verifierad CSS]` Gungande glödlamps-PNG (4s swing, ingen reduced-motion-spärr) + off-kanon #010328 + weight-300 vit text = rörelsestöld + tunn läsbarhet högst upp i kortet, dödyta från margin-top-hacket på mobil. | VDA-02/03/05 verifierad CSS |
| **D-FS-01** | FooterSEO | `[verifierad CSS]` Primär-CTA "Kostnadsfri **radgivning**" (stavfel, saknar å) länkar **bort till /kontakt/** (~9s ny sidladdning) förbi formuläret man just skrollade. Maskad 1200×600-bild = dekorativ fyllnad i ett mestadels tomt band. | FS-2/FS-3 verifierad live |

---

## Omdesign-direktiv

> Princip (doktrin §3): SEO-substansen **behålls i DOM** — vi packar om, raderar aldrig. Allt nedan är **mallnivå → 1 redigering propagerar till 291 sidor** (ContentBlock) resp. 290 (VDA/FooterSEO). Det är den största hävstången på sajten.

### A. Typografisk pattern-spec — gör samma DOM-text skannbar (ContentBlock, gäller alla rader)

Ersätt "H2 + ett/två odelade löptextstycken" med en **fast läshierarki**. Behåll varje befintlig mening; omfördela bara vikt och form.

1. **Rubrik (H2):** vikt **400 → 600**, `--aptext-xl` desktop / `--aptext-l` mobil, färg midnight #090b32. Det ska vara det tydligaste ankaret i raden.
2. **Ledmening (lead):** de 1–2 första meningarna som en egen `<p>`, `--aptext-m`, **weight 400**, **full färg** (inte `--color-20`-grått). Den bär radens svar.
3. **Tre fakta-punkter (bullets):** resten av stycket omvandlas till **3 punkter, var och en med fetad ledfras** (weight 600) + resten weight 400. Bär den hårda faktan: `**ROT 30 %** dras direkt på fakturan`, `**Behörig elektriker** — krävs för att försäkringen ska gälla`, `**2026-krav:** typ A jordfelsbrytare`. Punkter = det som scannas i F-mönstret (NN/g).
4. **Brödtextvikt ≤780px:** **300 → 400**; behåll `--aptext-m` (kliv inte ner till `sm`). Ingen weight-300-brödtext på dark eller på smått för 45+.
5. **Avslutande inline-länk per rad** (dödar dead-end, CB-05): en lågmäld textlänk, inte gradient-knapp — `Vill du ha fast pris? Ring 010-265 79 79 eller boka kostnadsfri rådgivning`.

### B. Bildtext-mönster (ny, obligatorisk copy-slot per bild)

Under varje bild: **en rad bildtext**, `--aptext-sm`, **weight 500**, färg #333 (eller teal #00a991 för platsordet), vänsterställd, max 1 rad. Format: **`{vad} — {ort}, {månad år}`**, t.ex. `Elcentralbyte, radhus i Tyresö — mars 2026` / `Diskmaskin installerad, kök i Vaxholm — 2026`. Bildtext är den mest lästa copyn på sidan (Ogilvy) och en daterad+platsad rad gör ett dekorativt foto till **candour-kompatibelt bevis** (motverkar Byggahus "är det ett riktigt företag?"-oron). Bildtext är candour-gatead: bara verkliga jobb får datum/ort; saknas det → generisk ämnesbildtext utan påhittad plats.

### C. Riktig-jobb-foto-riktning (ersätt AI-stock, CB-02/D-CT-03)

- **Byt de iscensatta AI-renderna** (torkade-blomster-kök, generiska industriskåp) mot **verkliga Ampy-jobb**: elektriker vid en riktig elcentral, en installerad diskmaskin i ett riktigt kundkök, ett bytt fasadmätarskåp. Konsekvent färggradering, 4:3, ett foto per rad.
- **Motivmatchning per sidtyp** (round-1: geo-flottan återanvänder t.o.m. batteri/växelriktar-foton på fel sidor). Elcentral-sida → elcentral-foto. Vitvaror → vitvaru-foto (redan rätt ämne här, men gör dem *riktiga*).
- **Där inget verkligt topikfoto finns:** krymp bildkolumnen (desktop) / cap:a höjden (mobil) hellre än att skeppa iscensatt stock — eller använd ett **märkt detalj-/diagramfoto** (t.ex. "typ A jordfelsbrytare") som bär information.
- Fixa de felaktiga alt-texterna (round-1: logo-beskrivning klistrad på elektrikerfoto) — ren a11y/SEO-defekt på sajtens största mall.

### D. Mobil-layout (ContentBlock, D-CT-01)

- **Cap:a bilder till ~240–260px** höjd på ≤480px (round-1 CB-rek 4). En 340px-bild före varje rubrik äter halva vyn utan att svara på något.
- **Text-först-stackning:** ordna om så mobil visar **rubrik → lead → punkter → bild** (rad 1 & 3 öppnar idag med bild). `flex-direction: column-reverse` på bild-först-rader eller DOM-omordning i mallen.
- Behåll den subtila enterView-animationen **bara på bilder** — strippa `hidden-on-load` från textkolumnerna (CB-05) så text aldrig kan bli blank på långsam JS.

### E. Desktop-obalans (D-CT-02)

- Vertikalt **centrera textkolumnen mot bilden** (`align-items: center` på raden) så den korta texten inte lämnar dödyta i botten.
- Efter B/C blir raderna jämnhöga av sig själva (bildtext + punkter fyller ut) — men centrering är en 1-raders säkerhet.

### F. VissteDuAtt `[verifierad CSS-bas]`

- **Skeppa den redan byggda redesignen** (round-1 VDA-rek 1 + ägar-memo: stackad layout, gungande lampa + 4s swing dödad, #010328→#090b32 fixad, slutaudit GO) — live kör fortfarande gamla JSON:en. Löser rörelsestöld + off-kanon-token på 290 sidor till ~noll extra jobb. Ägar-gatead visuell diff (approved-rendering-canon).
- Brödtext **weight 300 → 400**; behåll editorial-registret (ljust, inbjudande — kanon: awareness ska vara lätt).
- Lägg **en mjuk nästa-steg-länk** efter stycket (inte gradient-CTA) så bandet slutar vara dead-end (VDA-01): `Osäker på vad som gäller hemma hos dig? Ring 010-265 79 79`.
- Fixa "Visste du att.." (två punkter) → "Visste du att …?".

### G. FooterSEO `[verifierad CSS-bas]`

- **Ompeka primär-CTA** /kontakt/ → on-page-ankare `#main-contact` (smooth-scroll). 1 mallredigering, 290 sidor, tar bort ~9s sidladdning mellan slutintention och formulär (FS-2).
- Fixa knapp-biblioteks-strängen **"radgivning" → "rådgivning"** (fixar även Hero-1) + geo-genitiven "{Ort}'s" → "{Ort}s" (FS-3/FS-7).
- Rama om som **"sista chansen att fråga", inte SEO-bihang**: H2 svarar på exit-JTBD (`Fortfarande osäker? Prata med en elektriker först — det kostar inget`), stycket bär **ett konkret bevis** (Elsäkerhetsverket-registrering / skriftlig offert enligt Konsumentverket) istället för generisk "garanterad kvalitet". Telefon-CTA primär på detta djup (grundliga läsare = hög intention).

---

## Divergenta riktningar — ContentBlock (huvudblock, 3 versioner, husregel)

**Riktning A — "Lead + 3 fakta-punkter" (minsta ingrepp, säkrast).**
Behåll den alternerande layouten exakt. Applicera bara pattern-spec A + bildtext B + foto-riktning C. Varje rad blir: tung rubrik → ledmening → 3 fetad-lead-punkter → bildtextad riktig-jobb-bild → inline-länk. **En mallredigering → 291 sidor.** Noll SEO-risk (all text kvar i DOM). Detta är MECLABS-HealthSpire-flytten: samma längd, mer värdeklarhet. **Rekommenderad default.**

**Riktning B — "Beslutskort".**
Konvertera varje rad till ett **beslutskort** riktat mot en av de tre Byggahus-frågorna: Rad 1 = prislogik, Rad 2 = process/ansvar, Rad 3 = verifiering. Kortet = rubrik som fråga + svar-lead + en **kompakt fakta-remsa av chips** (`ROT 30%` · `Behörig` · `2026-krav`) + bildtextat foto + inline-länk. Mer designarbete (ny chip-komponent), men förvandlar SEO-svansen från "essä man skrollar förbi" till "invändningshantering man läser". Starkast på service-sidor (elcentral/vitvaror) där besluts­ångesten är hög.

**Riktning C — "Låna services-grid-mönstret" (djärvast, geo).**
På geo-sidor där ContentBlock är ren keyword-fyllning: ersätt de tre essä-raderna med den **skannbara bildkorts-griden som geo-elektriker-tyreso redan använder** (kort + 1-rads bildtext + pill), och behåll **en** essä-rad för SEO-body längst ner. Återvinner ~1000px mobil-skroll, ger interna länkar (varje kort länkar vidare), och matchar det mönster användaren redan möter högre upp på samma mall. Kräver att man bekräftar att body-texten som tas bort inte tankar ranking (round-1 FS-1-hypotes: tunn geo-appendix ≈ 0 ranking-värde) — A/B-gate:a.

---

## Vad som INTE ska röras

- **Den alternerande desktop-zig-zaggen** (I/T, T/I, I/T) — den fungerar på desktop och bryter monotoni; problemet är textväggen och bildvalet, inte layoutväxlingen. Riktning A/B behåller den.
- **Att SEO-texten finns och är unik per sida** (ACF-driven, 291 sidor, candour-ren, ingen urgency-teater) — round-1 CB "what it does well". Packa om, radera aldrig.
- **Services-griden på geo-elektriker** — den är redan det mest skannbara mönstret i svansen; använd den som förebild, degradera den inte.
- **VissteDuAtt:s lätta, inbjudande register** (välmående/plånbok/energitjuvar, du-tilltal) — kanon säger awareness ska vara lätt; rör vikten och lampan, inte tonen.
- **FooterSEO:s vita, lugna yta efter det mörka Certifikat-bandet** — visuellt rätt utandning före cyan-prefootern; behåll ytan, byt bara copy-jobbet och CTA-målet.
- **Vår process-blocket** (det enda i svansen med riktiga skann-ankare: ikon + numrerad kort rubrik + 3-rads text) — det är förebilden för hur tät SEO-text borde se ut, inte ett mål för ingrepp.
