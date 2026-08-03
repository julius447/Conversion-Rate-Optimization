# Call-CTA-banden på designnivå — MainCTA · BlueCTA · MikroCTA

Scope: de tre "ring / prata-med-oss"-banden ägaren pekade ut. Auditerade som **designer**, mobil först, på
`home`, `svc-elcentral`, `pillar-elektriker`, `geo-elektriker-tyreso`, `geo-elinstallation-vaxholm`.
Ägarens frö: *"MainCTA mår skitbra … men vi borde ta bort '5.0 på Google' för att den tar så mycket fokus.
Tar vi bort den blir CTA-knappen hela fokuset."* Nedan utvecklas det fullt — och ett större fokustjuv-problem
än 5.0-raden avtäcks.

**Ärlighet om scope (anti-teater):** Jag hittade **MainCTA** (svc-elcentral m08, pillar m14), **BlueCTA**
(home m19, pillar desktop d10) och de närliggande call-banden (Hero_2, footer-seo, main-contact) på tilesen.
**MikroCTA (mörk foto-bg + CTA-par) finns INTE på någon av mina fem sidor** — de call-band som faktiskt
renderas här är Hero_2, MainCTA, BlueCTA, footer-seo och main-contact. MikroCTA auditeras därför mot
block-inventariet §6 + resoneras om dess öde relativt de andra, inte mot en observerad pixel. Sägs rakt ut
istället för att låtsas.

---

## Vad ögat möter (mobil)

### MainCTA (svc-elcentral m08, pillar m14) — huvudobjektet
Vit rundad kort, generös padding. Uppifrån och ned:
1. **En stor teal-bakgrundad porträttbild** av en leende blond kille i svart Ampy-tröja (blob/våg-grafik
   nere till höger, urtvättad "ampy"-logga på bröstet). Bilden fyller **~50–55 % av kortets höjd** och är
   det första och absolut dominerande ögat möter — ett mänskligt ansikte är den starkaste blickmagneten som
   finns.
2. **H2 centrerad, två rader:** "Prata med en elektriker" (marinblå) **"inom 60 sekunder!"** (teal). Bra
   rubrik, tealen poppar lagom.
3. **Paragraf, 4 rader, mellangrå, centrerad:** "Känn dig trygg med kunnig hjälp, precis när du behöver den.
   Prata direkt med en erfaren elektriker …"
4. **CTA:** helbredds **cyan/ljusblå gradient-pill "Ring 010-265 79 79"** med mörk marinblå text + vit rund
   telefon-chip höger. Mjuk glow-skugga.
5. **Under knappen:** "G **5,0** på Google ★★★★★" (guldstjärnor), centrerad.

Observerad blickordning: **ansikte → "inom 60 sekunder!" → paragraf → (ned till) Ring-knapp → guldstjärne-raden
avslutar.** Knappen är alltså *inklämd mellan två fokustjuvar* och är dessutom det minst salienta av de fem
elementen (cyan gradient med mörk text = samma visuella vikt som "Läs mer"- och "Till X"-navigeringsknapparna
som ligger överallt på sidan). Tummen måste scrolla förbi hela ansiktet + rubrik + 4 rader innan knappen når
tumzonen — knappen ligger ~1,3 skärmhöjder ned i bandet.

### BlueCTA (home m19)
Cyan→himmelsblå gradient-kort, svag bolt/"a"-vattenstämpel i bg. Centrerad stack: **H2 "Prata med en
elektriker!"** (mörk marinblå, "elektriker!" **understruket**) → paragraf 3 rader (mörk) → **en enda SVART pill
"Ring 010-265 79 79"** med vit telefon-chip. Ingen bild. Ingen 5.0-rad. Den svarta knappen mot cyan =
**den högsta knapp-kontrasten på hela sajten** — här läser ringknappen faktiskt som primär.

### MikroCTA (ej på dessa sidor; per inventarium §6)
Mörkt foto-bg (soft-light blend) rundat kort: vit H2 → paragraf → **CTA-par** (Kostnadsfri rådgivning +
Ring). Dvs samma dubbel-ask som Hero_2 fast på bild-bakgrund.

### Grannbanden (kontext, ej scope men styr ödesbeslut)
- **Hero_2** (m01): mörk marinblå hero, grön eyebrow + stor vit/grön H2 + paragraf + **Kostnadsfri rådgivning
  (grön) + Ring (cyan)** + teal "5.0 ★★★★★"-rad + formulärkort. Tre samtidiga asks.
- **footer-seo** (pillar m12, geo m16-svans): vitt kort, H2 + paragraf + **CTA-par (grön + cyan)** + teal
  "5.0 ★★★★★"-rad + maskad husbild med våg.
- **main-contact** (svc m10): den starkaste konverteringsytan — teal-navy vänsterpanel med citat "Från start
  till mål …", guld ★★★★★ "5 av 5 · Betyg på Google", "3 000+ … om året", 3 steg; vit formulärpanel höger,
  grön "Gratis rådgivning"-submit.

**Proof-motivet "5,0 / 5 av 5 · Betyg på Google" räknas i ≥5 block per servicesida** (Hero_2, MainCTA,
footer-seo, main-contact, testimonials). Cf. block-inventory X-cutting: "5.0-claims i ≥6 block".

## Vad ögat möter (desktop)
- **MainCTA (desktop):** text-stack vänster, teamfoto med våg-overlay höger (~40–45 % bredd). Sida-vid-sida
  gör bilden mindre kväljande än mobilens topp-placering — textkolumnen håller emot. Men de två kärnfelen
  kvarstår: (a) cyan-gradient-knappen med mörk text har låg salience och är färgtvilling med
  navigeringsknapparna, (b) 5,0-raden hänger kvar som avslutande blickvila.
- **BlueCTA (desktop, pillar d10):** horisontellt band — rubrik "Prata med en **elektriker!**" + paragraf
  vänster, **svart Ring-knapp höger**. Ren, kontraststark, en enda ask. Fungerar som den är.
- **Hero_2 / footer-seo (desktop):** grön + cyan CTA-par sida vid sida — de två knapparna delar bredd och
  ingen vinner; den gröna "Kostnadsfri rådgivning" tar visuellt över den cyanblå "Ring".

---

## Fynd

| ID | Element | Problem | Evidens |
|----|---------|---------|---------|
| **CTA-01** | MainCTA teamfoto | Foto ~55 % av kortet = **primär fokustjuv**; ett ansikte slår varje knapp om blick. Knappen kan aldrig bli "hela fokuset" så länge fotot är detta stort. Detta är ett *större* problem än 5.0-raden. | svc m08, pillar m14 |
| **CTA-02** | MainCTA "5,0 på Google ★★★★★"-rad | Guldstjärnor under knappen = **terminal blickvila** (ögat stannar sist på nedersta elementet, och guld/stjärnor glimmar). Stjäl exakt det fokus ägaren beskriver. Dessutom **candour-risk**: "5,0" utan recensionsantal/ankare (bannad om ej ägarbekräftad aktuell). | svc m08, pillar m14 |
| **CTA-03** | MainCTA Ring-knapp (cyan gradient, mörk text) | **Låg salience + färgtvilling** med "Läs mer"/"Till X"-navknapparna. Sajtens *viktigaste* ring-knapp ser ut som en låg-intents-navlänk. BlueCTA:s svarta knapp bevisar att hög kontrast finns i systemet. | svc m08 vs home m19; jfr Zaptec "Läs mer" m10 |
| **CTA-04** | MainCTA knapp-position (mobil) | Knappen ligger ~1,3 skärmhöjder ned, bakom fullhöjdsfoto + rubrik + 4 radig paragraf. Utanför första tumzon. | svc m08 |
| **CTA-05** | BlueCTA vs MainCTA redundans | Båda är **phone-only-asks**. På `pillar-elektriker` renderas BÅDA (MainCTA m14 + BlueCTA d10) → två ringband på samma sida. Rå upprepning av samma ask. | pillar m14 + pillar d10 |
| **CTA-06** | MikroCTA (där den finns) CTA-par | Dubbel-ask (Kostnadsfri rådgivning + Ring) på fotobakgrund = **dupliceringen av Hero_2:s dubbel-ask** en gång till, utan nytt visuellt jobb. Två knappar som delar vikt → ingen vinner. | inventarium §6; jfr Hero_2 m01 |
| **CTA-07** | System: "Ring 010-265 79 79" × N | Telefonnumret som knappetikett upprepas i Hero_2, MainCTA, BlueCTA, footer-seo + main-contact — 4–5 ggr/sida. Upprepning ≠ styrka; det gör varje enskild knapp billigare. | alla sidor |
| **CTA-08** | Grön vs cyan CTA-par (Hero_2/footer-seo/MikroCTA) | När "Kostnadsfri rådgivning" (grön, formväg) och "Ring" (cyan) står sida vid sida delar de fokus. Grönt vinner alltid → **ringasket underordnas** genomgående, tvärtemot att MainCTA ska vara ring-flaggskeppet. | m01, pillar m12 |

---

## Omdesign-direktiv

1. **Krymp MainCTA-fotot (CTA-01).** Mobil: från ~55 % fullbredds-topp till en **liten inset-porträtt**
   (t.ex. rund/rundad 96–120 px ovanför rubriken, ELLER helt struket och ersatt av en enkel telefon-glyf i
   Ampy-teal). Bilden ska *stödja* värmen, inte äga kortet. Desktop: kapa fotokolumnen till max ~35 % så
   textstacken + knappen dominerar.
2. **Ta bort "5,0 på Google"-raden i MainCTA (CTA-02, ägarens frö).** Dubbelvinst: (a) knappen blir sista
   blickvila, (b) en oankrad candour-liability försvinner. Det ankrade proofet ("5 av 5 · Betyg på Google" +
   riktiga recensioner) bor redan i testimonials + main-contact — MainCTA behöver det inte.
3. **Byt Ring-knappens färg i MainCTA till högsta kontrast (CTA-03).** Använd BlueCTA:s svarta pill *eller*
   en mättad teal (#00a991) med vit text — men **inte** cyan-gradienten som delas med navknapparna. Efter
   direktiv 1+2+3 blir knappen sajtens hetaste enskilda element i bandet.
4. **Lyft knappen i tumzon (CTA-04).** När fotot krympt och 5.0-raden är borta åker Ring-knappen upp ~1
   skärm; på mobil ska den nås utan att scrolla förbi ett ansikte.
5. **Avgör bandens öde med designskäl (CTA-05/06):**
   - **MainCTA = det starkaste call-assetet** — enda bandet med *värme (ansikte) + nyttolöfte ("inom 60
     sekunder") + lugnande copy + en enda ren ring-ask*. Behåll och förädla den (spec nedan). För en publik
     35–65 med trygghetsbehov är den mänskliga, icke-formulär-mässiga ring-inbjudan ett **distinkt visuellt
     jobb** som formblocken (Hero_2, main-contact) inte gör.
   - **BlueCTA = behåll ENDAST på sidor utan MainCTA** (t.ex. som lätt phone-strip på home). På sidor som bär
     den förädlade MainCTA (svc, geo, pillar) → **droppa BlueCTA** (CTA-05): den är då en tunnare dublett av
     samma ask. Dess enda överlägsenhet — svarta knappen — flyttas in i MainCTA (direktiv 3), så inget värde
     går förlorat.
   - **MikroCTA → retirera eller reducera till en enda Ring-ask (CTA-06).** Dess dubbel-ask duplicerar
     Hero_2. Behövs ett bild-backat ringband någonstans, gör om det till MainCTA-mönstret (ett ansikte/en
     knapp), inte ett CTA-par.
6. **Bryt grön+cyan-tvillingen (CTA-08) i kvarvarande dubbel-ask-band.** Där ett CTA-par måste stå (Hero_2,
   footer-seo): gör den ena visuellt underordnad (ghost/outline) så en väg är primär — annars konkurrerar de
   och den gröna formvägen slår alltid ihjäl ring-vägen.
7. **Ranta ned "Ring 010-…" som etikett (CTA-07).** Överväg "Ring en elektriker" som knapptext och låt
   numret stå en gång tydligt — upprepat nummer × 5 sänker varje instans värde.

### Förädlad MainCTA — spec (mobil)

Elementlista uppifrån och ned, efter ingrepp:
1. *(valfri)* liten teal telefon-glyf **eller** 96 px rund inset-porträtt — stödelement, ej dominant.
2. **H2** "Prata med en elektriker **inom 60 sekunder**" (marin + teal), centrerad. (Behåll — den mår bra.)
3. **Paragraf** 2–3 rader, mellangrå: "Känn dig trygg med kunnig hjälp, precis när du behöver den. Prata
   direkt med en erfaren elektriker som guidar dig rätt." (Kort ned från 4 → 3 rader.)
4. **Ring-knapp** — full bredd, **svart eller teal #00a991**, vit text, vit telefon-chip. **Enda knappen.**
   Sajtens hetaste element i bandet.

**Borttaget:** 5,0-guldstjärneraden (CTA-02). **Nedtonat:** fotot från dominant → stöd (CTA-01). **Omfärgat:**
knappen cyan → svart/teal (CTA-03). **Fokusflöde efter:** rubrik → (kort) paragraf → **KNAPP (terminal
blickvila, hetast)**. Precis "CTA-knappen blir hela fokuset."

Desktop-variant: textstack (rubrik/paragraf/knapp) vänster ~65 %, litet stödfoto höger ~35 %; samma
knappfärg; ingen 5.0-rad.

---

## Divergenta riktningar (MainCTA — det stora ingreppet, husregel 3 versioner)

**Riktning A — "Ansiktet krymper, knappen vinner" (minsta ingrepp, rekommenderas).**
Behåll teamfotot men som liten rund inset (96–120 px) ovanför rubriken. Ta bort 5.0-raden, gör knappen svart.
Värmen finns kvar via ansiktet i litet format; knappen blir terminal. Lägst risk — pixel-nära dagens block.

**Riktning B — "Ren typografisk ring-inbjudan" (inget foto).**
Stryk fotot helt. Kortet blir: teal telefon-glyf → H2 → 2 rader → stor svart/teal Ring-knapp. Renast möjliga
fokus, snabbast till tumzon, lättast (ingen bildladdning → snabbare LCP, relevant givet ~9–10 s lab-LCP-flagg).
Tappar den mänskliga värmen — testa mot A.

**Riktning C — "Split: ansikte-vänster, ask-höger" (desktop-först, mobil staplar).**
Halvt kort: foto vänster (kontrollerad ~40 %), höger = rubrik + paragraf + svart Ring-knapp, INGEN 5.0. Nära
main-contact-mönstret men utan formulär → en trygg mellanform mellan "kallt formblock" och "varmt ringband".
Bäst där MainCTA ersätter både sig själv OCH en droppad BlueCTA.

Bygg alla tre för Julius pixel-QA innan Bricks. Alla tre delar tre invarianter: **(1) ingen 5.0-rad, (2)
hög-kontrast (svart/teal) ringknapp ≠ navfärg, (3) en enda ask.**

---

## Vad som INTE ska röras
- **Rubriken "Prata med en elektriker inom 60 sekunder!"** — nyttolöfte + tidsangivelse + teal-pop, mår bra.
  Rör inte copy eller tealen (ampy-röst-godkänd, konkret, ej superlativ-fluff).
- **Paragrafens ton** — lugn, du-tilltal, trygghetsförankrad. Korta bara längden, byt inte rösten.
- **BlueCTA:s svarta knapp mot cyan** — behåll den kontrasten; det är precis den som ska koloniseras in i
  MainCTA. Rör inte BlueCTA där den står ensam (home).
- **main-contact-blocket** — starkaste konverteringsytan; dess ankrade "5 av 5 · Betyg på Google" + "3 000+"
  + 3-stegen är legitimt proof. Denna audit rör *ring-banden*, inte formblocket.
- **Att MainCTA är phone-only (ingen formulär-CTA)** — det ÄR dess distinkta jobb. Lägg aldrig till en
  grön "Kostnadsfri rådgivning"-knapp här; det skulle återinföra grön/cyan-tvillingen (CTA-08) och döda
  ring-fokuset.
