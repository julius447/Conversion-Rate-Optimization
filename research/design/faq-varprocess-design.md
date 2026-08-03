# FAQ (`faq-`, block 10) + Vår process / "Så funkar det" (`our-process`, block 11) — designaudit

Scope: de två blocken som de renderas på `svc-elcentral`, `geo-elektriker-tyreso`, `geo-laddbox-nacka`. `kontakt` bär varken FAQ eller process (bara Hero_2-formulär + footer) — utgår. Kanonisk rendering av båda blocken sedd tydligast på `svc-elcentral` desktop (tiles 05–07) + mobil (tiles 07–10). Grannblock som blocken jämförs mot: metrics (block 22) och grön-teknik-stegen (block 13) som ligger på samma geo-sidor.

---

## Vad ögat möter (mobil)

**Vår process (svc-elcentral mobil 06–07):** Centrerad rubrik "Så funkar **det**" (sista ordet i grön gradient), centrerad underrubrik "Ampy's steg-för-steg-lista som beskriver hela installationsprocessen för byte av elcentral!". Sedan EN kolumn, allt centrerat: en naken tunn-linje-ikon (telefon) → fet navy "1. Samtal med elektriker" → centrerad brödtext. Skrolla → pennikon → "2. Offert & tidsförslag"; fil-bock → "3. Bokning bekräftad"; blixt → "4. Installation utförd". Fyra höga, luftiga, centrerade block staplade — ingen visuell tråd mellan dem. Ögat får fyra löst svävande kort, inte en sekvens.

**FAQ (svc-elcentral mobil 09–10):** Mint→ljusblå gradient-container. Vänsterställd rubrik "Vanliga frågor". Fyra kort staplade: "Vad kostar det att byta elcentral?", "Vem får byta elcentral?", "Vilka regler gäller för elinstallationer?", "Ingår ROT-avdrag vid byte av elcentral?". Varje kort är näst-intill-vitt på den ljusa mint-ytan med EN tunn chevron längst till höger. Alla stängda. Under fjärde frågan: en stor, suddig AI-renderad bild på en halvöppen elcentral som tar ~en och en halv skärmhöjd. Ögat landar på rubriken, ser fyra passiva etiketter, och sedan en stor dekorbild — noll svar levereras utan tapp.

## Vad ögat möter (desktop)

**Vår process (svc-elcentral desktop 05–06):** Centrerad rubrik + underrubrik. Fyra jämnbreda kolumner sida vid sida. I varje: vänsterställd naken ikon → "1. …/2. …" fet navy → vänsterställd brödtext. Kolumnerna sitter långt isär utan pil, linje eller nummer-cirkel emellan — läsordningen vänster→höger bärs enbart av de små "1./2./3./4."-prefixen. Steg 4:s brödtext är **ordagrant identisk** med steg 2:s.

**FAQ (svc-elcentral desktop 06–07):** Bred mint-gradient-container. Vänster ~55 %: rubrik "Vanliga frågor" + fyra staplade accordion-kort (låg-kontrast vita på mint, chevron till höger, alla stängda). Höger ~45 %: samma suddiga AI-elcentralbild, nu som en hög kolumn som äter halva blockets bredd. Accordion trängs ihop till vänster medan halva ytan går till en dekorbild som inte besvarar någon fråga.

---

## Fynd

| ID | Element | Problem | Evidens |
|---|---|---|---|
| **FAQ-1** | Accordion-affordans | Korten är near-vita på ljus mint-gradient — ingen ram, minimal skugga, enda interaktions-signal är en tunn chevron. Läser som passiva rubriker, inte tappbara kontroller. Målgrupp 35–65 måste gissa att de går att öppna. | Mobil 09, desktop 07: kort smälter in i containern; kontrasten kort↔bakgrund är minimal. |
| **FAQ-2** | Default-state = allt stängt | Alla fyra frågor kollapsade från start → besökaren möter noll svar. FAQ:ns hela jobb (avväpna sista invändningen) levereras aldrig utan aktivt tapp. NN/g: öppna första posten som default. | Mobil 09 + desktop 07: inget svar syns i något läge. |
| **FAQ-3** | Bildkolumnens earn-rate | Desktop: suddig AI-render av elcentral äter ~45 % av blockets bredd och illustrerar ingen specifik fråga, bygger ingen tillit (uppenbart AI, inget riktigt Ampy-jobb). Mobil: samma bild staplas UNDER accordion och lägger ~1,5 skärmhöjd ren dekor + LCP-kostnad, noll informationsvärde. | Desktop 07 höger kolumn; mobil 09→10 bild under korten. |
| **FAQ-4** | Frågetypografi / radbrytning | 2-rads-frågor ("Vilka regler gäller för elinstallationer?", "Ingår ROT-avdrag vid byte av elcentral?") får varierande korthöjd och chevron som flyter mitt i höger kant → ojämn rytm i stacken. Trängseln kommer delvis av att accordion bara får 55 % bredd (FAQ-3). | Desktop 07: kort 3 & 4 tvåradiga, kort 1 & 2 enradiga. |
| **FAQ-5** | Ingen close i FAQ | Efter sista frågan tar blocket slut (bild) → nästa block. FAQ är peak-consideration-läget men bär ingen mjuk ring-/kontakt-nudge. Konverterings-tillfälle bränt. | Desktop 07 → nästa block utan CTA. |
| **PROC-1** | Duplicerad brödtext steg 4 | Steg 4 "Installation utförd" har ordagrant steg 2:s text: "Vi går vi igenom dina behov och skickar en transparent offert och tidsförslag." Ren copy-paste-bugg live. Steg 4 ska beskriva installationen. | Desktop 06 + mobil 07: steg 2 = steg 4 identiskt. |
| **PROC-2** | Grammatikfel i 3 av 4 steg | "Vi går **vi** igenom" (steg 2 & 4) och "Vi skickar **vi** ut" (steg 3) — dubbla pronomen. Tre live-typos i ett förtroende-block. Underminerar candour ("hantverkaren som säger sanningen"). | Desktop 06: alla tre synliga. |
| **PROC-3** | "Ampy's" + meta-filler i underrubrik | Engelsk possessiv-apostrof "Ampy's" (ska vara "Ampys" på svenska). "steg-för-steg-lista som beskriver..." beskriver sig själv = filler. | Mobil 06, desktop 05. |
| **PROC-4** | Nakna ikoner + inkonsekvent accent | Ikonerna svävar utan behållare medan metrics-blocket på SAMMA sidor lägger sina ikoner i fyllda navy-cirklar → två ikon-språk på en sida. Telefon-ikonen (steg 1) är tyngre/större än övriga; penn-ikonen har en grön squiggle som inga andra matchar. Accent-logiken spretar. | Desktop 06 process vs geo-tyreso mobil 14/25 metrics-cirklar. |
| **PROC-5** | Nummer utan egen vikt → ingen sekvens | "1./2./3./4." är samma storlek/färg som rubriken, kolumnerna sitter isär utan linje/pil. Progressionen läses inte vid en blick. grön-teknik-blocket (block 13) på geo-laddbox gör tvärtom rätt: stora numrerade cirklar 1–2–3 på streckad linje = läses direkt som sekvens. Inkonsekvens inom samma sajt. | Desktop 06 process vs geo-laddbox desktop 11 grön-teknik. |
| **PROC-6** | Mobil centrering | På mobil är allt centrerat (ikon, rubrik, flerradig brödtext). Centrerad flerradig brödtext = trasiga båda kanter, tyngre läsning för 35–65, och den centrerade stapeln gör varje steg högt → 4 steg äter mycket skroll och tappar "steg"-känslan. Desktop är vänsterställt (bättre). | Mobil 06–07 centrerat vs desktop 06 vänsterställt. |
| **PROC-7** | Dubblerad ring-utfästelse | Steg 1 "Samtal med elektriker / …ringer vår seniora elektriker upp dig" upprepar exakt MainCTA-blocket ("Prata med en elektriker inom 60 sekunder") som ligger direkt under. Två grannblock lovar samma sak. | svc-elcentral mobil 07 (process) → 08 (MainCTA). |

---

## Omdesign-direktiv

**FAQ:**
1. **Öppna första frågan som default.** Låt "Vad kostar det att byta elcentral?" stå expanderad vid inladdning → besökaren möter direkt ett riktigt svar. Övriga stängda. (FAQ-2)
2. **Bygg affordans i kortet.** Ge varje kort: vit yta med 1px teal-tonad kant ELLER tydligare skugga, och flytta chevron in i en liten teal cirkel (teal #00a991) höger. Aktiv/öppen: kortet får vit fyllning + tunn teal vänsterribba, chevron roterar. Press-state på mobil. Så blir "tappbar" oförhandlingsbart. (FAQ-1)
3. **Släpp AI-bilden.** Mobil: ta bort bilden helt — ren skroll-/LCP-skatt. Desktop: låt accordion gå **full bredd** → inga 2-radsbrytningar (FAQ-4), svar får plats. (FAQ-3)
4. **Konvertera den frigjorda desktop-högerkolumnen till en close** i stället för dekor: litet "Har du en fråga vi inte svarat på?"-kort med Edvin-bild + "Ring 010-265 79 79" (samma ljusblå ring-knapp som MainCTA). Då tjänar ytan konvertering i stället för att äta bredd. (FAQ-3, FAQ-5)
5. **Håll containern** men höj kort-kontrasten (FAQ-1). Mint-gradienten som mjuk sektionsbrytning är ok.

**Vår process:**
6. **Fixa live-buggarna omgående (candour-gate):** skriv om steg 4 så det beskriver installationen (t.ex. "Vår behöriga elektriker byter din elcentral — fackmässigt, städat och driftklart samma dag."), rätta "Vi går vi igenom"→"Vi går igenom", "Vi skickar vi ut"→"Vi skickar ut", "Ampy's"→"Ampys". (PROC-1, PROC-2, PROC-3)
7. **Ge numret vikt och koppla stegen.** Lägg numret i en cirkel (navy fylld, vit siffra — samma språk som metrics/grön-teknik) ovanför/vänster om ikonen, och dra en tunn connector mellan stegen: streckad horisontell linje på desktop (som grön-teknik), vertikal linje i vänster ränna på mobil. Sekvensen ska läsas vid en blick. (PROC-4, PROC-5)
8. **En ikon-logik.** Behåll tunn-linje-stilen ELLER byt till fyllda cirklar — men matcha metrics-blockets behållare så sidan har ETT ikon-språk. Normalisera alla fyra till samma stroke-vikt och samma accent-regel (t.ex. teal enbart på det aktiva/rörelse-elementet). (PROC-4)
9. **Vänsterställ på mobil.** Ikon + nummer + rubrik + brödtext vänsterställda i en kolumn, connector-linje i vänster ränna, stramare vertikal rytm → färre skärmhöjder, tydlig sekvens. (PROC-6)
10. **Avdramatisera underrubriken:** ersätt meta-fillern med ett konkret löfte, t.ex. "Från första samtal till färdig installation — så här går det till." (PROC-3)
11. **Differentiera steg 1 från MainCTA.** Rama steg 1 kring vad SOM HÄNDER när du fyllt i ("Vi ringer upp, oftast samma dag"), inte kring samma "prata med elektriker"-erbjudande som blocket under. (PROC-7)

---

## Divergenta riktningar

### FAQ — 3 riktningar
- **A — Full-bredd accordion + close-kort (rekommenderas).** Bild bort, accordion full bredd, första frågan öppen, förstärkta kort (dir 1–3). Desktop får ett smalt ring-close-kort till höger (dir 4). Renast, snabbast, högst konverterings-earn per pixel.
- **B — Två-kolumns fråge-grid.** Desktop: 2×2 grid av accordion-kort (ingen bild alls), full bredd, luftigare. Passar om FAQ växer till 6+ frågor. Mobil: enkel stack. Ger fler frågor "above image-less fold" men tappar close-kortet.
- **C — FAQ + inline-svar (ingen accordion).** De 3–4 viktigaste frågorna med svaren SYNLIGA (kort svar, "Så räknar vi"-stil), resten som "Fler frågor →" länk. Maximerar levererat värde för 35–65 som ogärna tappar, men blir högre; motiverat främst på elcentral-pris-sidor där pris-frågan är avgörande.

### Vår process — 3 riktningar
- **A — Numrerad timeline (rekommenderas).** Behållna 4 steg, nummer-cirklar på connector-linje (dir 7), en ikon-logik (dir 8), vänsterställt på mobil (dir 9). Låg risk, fixar alla fynd, harmoniserar med grön-teknik/metrics.
- **B — Horisontell stepper med progress.** Desktop: en tunn teal progress-rail som binder de fyra cirklarna; aktivt steg lyfts. Mer "modernt" men mer rörelse — håll subtilt för målgruppen (candour ≠ gimmick).
- **C — Kollapsa till 3 steg.** Slå ihop "Bokning bekräftad" i "Offert & tidsförslag" → 3 steg (Samtal → Offert & bokning → Installation), matchar grön-teknik-blockets 1–2–3 exakt och skär en redundant ruta. Enklaste sekvensen att ta in; kräver copy-omskrivning.

---

## Vad som INTE ska röras
- **Rubrik-mönstret "Vanliga frågor" / "Så funkar det"** — korta, tydliga, on-voice. Behåll (grön gradient på "det" är harmlös).
- **Frågeuppsättningen i FAQ** (pris / vem får / regler / ROT) — rätt fyra invändningar för elcentral-intent. Rör innehållet, inte urvalet.
- **Ikon-VALEN i processen** (telefon → penna → fil-bock → blixt) mappar logiskt mot samtal→offert→bekräftelse→jobb. Normalisera stilen, byt inte motiven.
- **Fyra-stegs-berättelsen som koncept** (om inte riktning C väljs) — sekvensen är begriplig; det är den visuella bäraren, inte storyn, som är trasig.
- **Mint-gradient-containern som sektionsbrytning** — mjuk kontrast mot de vita sektionerna; behåll, höj bara kort-kontrasten inuti.
