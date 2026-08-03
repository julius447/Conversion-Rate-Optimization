# Artikelmallen — visuell designaudit (round 2)

Scope: den fullständiga artikelmallen, sedd på `byta-elcentral-2026` (49 884 px hög på mobil, 34 mobiltiles / 20 desktoptiles). Round-1-strukturen (ART-01…ART-08 i `research/templates/articles.md` + `research/blocks/article-blocks.md`) är KONTEXT — den här filen lägger designlagret ovanpå: vad ögat faktiskt möter, pixel för pixel, och de två saknade konverteringskorten (inline-CTA + Nästa-steg) fullt utritade — det som round 1 specade utan utseende.

Observerad designvokabulär (det mallen redan äger — nya block ska tala samma språk):
- **Snabbt svar-kortet:** vitt kort, tjock grön vänsterstripe (teal→ljusgrön gradient ~6 px), grön bock-cirkel, `SNABBT SVAR`-eyebrow i grön spärrad versal, bold "Sammanfattning:" + brödtext + "Nyckelpunkter:" punktlista. Rundade ~20 px hörn, mjuk skugga. **Mallens starkaste element.**
- **Pro Tip-kortet:** vitt kort, tunn grå ram (~1 px), ingen stripe, centrerad `💡 PRO TIP`-eyebrow (navy spärrad), **centrerad** brödtext, hårfin avdelare, grön "Verifierad av [namn]"-pill centrerad.
- **Story-/citatkortet:** vitt kort, tunn grå ram, stora lavendelfärgade citattecken uppe-vänster + nere-höger, **centrerad** citattext (~22 px), avdelare, attributionsrad = rund avatar + bold navy namn + dämpad lavendel roll-undertitel.
- **Numrerad process:** mintgrön cirkel (~28 px) med grön siffra + bold navy inledning + regular brödtext.
- **TOC-kortet:** vitt rundat kort, `≡ Innehållsförteckning` navy bold + chevron; aktiv rad = fylld **lavendel/indigo** pill med indigo vänsterstapel; inaktiva = navy länkar med luftig radhöjd.
- **Inline-länkar:** teal `#00a991` understruket. **Brödtext:** navy `#090b32`, Outfit, radhöjd ~1.7, ~19 px mobil. **H2:** bold navy, stor, **ingen accentbar**.

---

## Vad ögat möter (mobil)

**Tile 01 — topp.** Sticky header (ampy-logo vänster, grön `Gratis rådgivning`-pill i mitten med en lysande grön pulsprick under, hamburgare höger). Under: breadcrumb `Hem > Nyheter > Byta elcentral 2026: pris, ROT-avdrag 30% och vad som in…` (avklippt). Sedan mörk hero: öppen elcentral-/proppskåpsbild med mörk overlay, **H1 vit, mycket stor, 3 rader** ("Byta elcentral 2026: pris, ROT-avdrag 30% och vad som ingår") + **6 rader vit ingress**. Första blicken landar på H1 → korrekt för en artikel. Enda konverteringsaffordansen i vy = den gröna header-pillen, som lämnar viewporten direkt vid scroll.

**Under hero (tile 01 forts.):** bylinetrio — **3 överlappande runda avatarer** till vänster + tre rader text ("Skriven av **Julius Callahan**", "Redigerad av **Magnus Harald Metsniin**", "Faktagranskad av **Edvin Gustavsson**"). Under: grön `✓ Verifierad av expert`-pill + kalender `Uppdaterad juni 8, 2026`, sedan klocka `17 min läsning`. Mycket trust-chrome, staplat. **Avatarerna är överlappade → man kan inte mappa vilket ansikte = vilken roll.**

**Tile 01→02 — TOC.** Rundat vitt kort `≡ Innehållsförteckning` med chevron, **uppfällt**, aktiv rad ("Vad kostar det att byta elcentral 2026") i lavendel pill; sedan 8 navy länkrader med luft (ROT avdrag, Vad ingår i standardpaketet, … Summering). Ett helt block läsaren måste scrolla förbi innan innehållet. Inte sticky på mobil.

**Tile 02→03 — Snabbt svar.** Grön vänsterstripe, grön bock, `SNABBT SVAR`, "**Sammanfattning:** …", lång brödtext, "**Nyckelpunkter:**" + 5 punkter (snittpris, ROT bara arbetsdelen, 8 av 10 villor dolda fel, tidsåtgång, komplettering räcker). Fyller 2+ mobilskärmar. Bäst utformade elementet.

**Tile 04→06 — brödtext + tabell + Pro Tip.** H2 "**Vad kostar det att byta elcentral 2026**" (bold navy, ingen accentbar) → luftig brödtext, teal inline-länkar (byta elcentral, ny laddbox). **Prismatrisen reflowar till STAPLADE kort** på mobil — ett kort per fastighetstyp (Lägenhet / Radhus / Villa), och i varje kort tre **versala spärrade etiketter** `PRIS FÖRE ROT (KR)` / `ARBETSKOSTNAD (KR)` / `PRIS EFTER ROT 30 % (KR)` med värdet under. Etiketterna är höga, versala och **upprepas 3×** → tungt visuellt brus, och jämförelsen villa-vs-radhus (tabellens hela poäng) försvinner. Pro Tip-kortet: **centrerad** brödtext (svårare att läsa än vänsterställd) + grön "Verifierad av Magnus Harald Metsniin"-pill.

**Tile 18→20 — citat + räkneexempel.** Story-kort: stora lavendelcitattecken, **centrerad** citattext från Edvin, attributionsrad med avatar + "**Edvin Gustavsson**" + **avklippt roll** "Senior Elektriker, Arbetsledare & Kvalitetsa…". Sedan räkneexempel som bold-lead punktlista (Arbetskostnad 16 000 kr … Slutpris att betala 22 200 kr).

**Tile 30→33 — numrerad process.** Mintgröna sifferbadges 1–6 (Demontering … Säkerhetstester). Efter tile 33 loopar tilesen tillbaka till header/hero (capture-artefakt) — **end-zonen (FAQ → review-CTA → dela/skriv ut → Populära artiklar) fångades aldrig i tiles**; verifierad via round 1: det enda stylade CTA-kortet i hela artikeln är Google-review-asken, och den sitter i den bästa slot:en (ART-02/03).

**Sammanfattning mobil:** genom hela 49 884 px finns **noll** ring-/formaffordans i brödtexten (ART-01/ART-05). Motivationen toppar vid räkneexempel och process — kanalen är tom.

## Vad ögat möter (desktop)

**Tile 01.** Header med `Tjänster ▾ Produkter ▾ Lösningar ▾` + grön `Gratis rådgivning`-pill. Mörk hero, **H1 ~60 % bredd**, 3 rader ingress. Bylinerad = horisontellt band: **vänsterkluster** (3 avatarer + 3-rollstext) och **långt till höger** grön `Verifierad av expert`-pill + `Uppdaterad juni 8, 2026` + `17 min läsning`. **Stort tomt gap i mitten** av bandet.

**Tile 01→02 — 2-kolumn.** Artikel 65 % vänster, **TOC 30 % höger** (vitt rundat kort, aktiv rad lavendel pill med **indigo** vänsterstapel — indigo, inte teal-brand). Snabbt svar-kortet i vänsterspalten.

**Tile 03 — tabell.** På desktop en ren 4-kolumns tabell (FASTIGHETSTYP / PRIS FÖRE ROT / ARBETSKOSTNAD / PRIS EFTER ROT 30 %), radavdelare, rundad ram. **Läsbar och bra — problemet är bara mobilreflowen.**

**Tile 15→20 — den tomma högerspalten.** Efter att TOC-kortet tar slut (sista raden "Så jämför du offerter — 12-punkts-checklista") är **hela högra ~30 %-spalten TOM vit yta genom resten av artikeln** — tiotusentals pixlar. TOC:en är `position: sticky` men kortet är kort; den försvinner och lämnar en gigantisk tom ränna. Desktoptilesen (20 st) når bara ~1/3 ner — end-zonen fångades inte heller här.

---

## Fynd

**AD-01 · P0 · Ingen konverteringsaffordans i brödtexten, och den tomma högerspalten är oanvänd.** (bygger på ART-01/ART-05)
Element: hela artikelkroppen + desktop högerspalt. Problem: 49 884 px läsning, 0 ring/form i kroppen; på desktop dessutom ~70 % av högerspalten tom efter TOC. Evidens: MECLABS — m och v toppar vid pris/räkneexempel, i = 0. Den tomma högerrännan är premium-yta som skriker efter ett persistent kort.

**AD-02 · P0 · Det enda stylade CTA-kortet pekar till Google.com i den bästa slot:en.** (ART-02/ART-03)
Element: review-CTA efter FAQ. Problem: prospektets beslutsögonblick får en Google-review-ask (fel publik — en läsare kan inte recensera; en kund läser sällan "byta elcentral pris") istället för en offert/ring. Detta är den seedade "5.0-tar-fokus"-logiken i sin grövsta form: en hel CTA-slot exporterar den varmaste trafiken bort från sajten.

**AD-03 · P1 · Prismatrisens mobilreflow är visuellt bullrig och tappar jämförelsen.**
Element: prismatris, mobil. Problem: 3 staplade kort × 3 versala spärrade etiketter = 9 tunga etikettrader; siffrorna (det man faktiskt vill scanna) drunknar, och sida-vid-sida-jämförelsen försvinner. Desktop-tabellen är däremot bra.

**AD-04 · P2 · Centrerad brödtext i Pro Tip- och citatkort sänker läsbarheten.**
Element: Pro Tip, story-/citatkort. Problem: långa centrerade stycken (ragged båda kanter) är mätbart trögare för 35–65-publik än vänsterställt. Story-kortets **roll-undertitel klipps** ("…Kvalitetsa…") — E-E-A-T-raden, vars hela poäng är trovärdighet, kapas.

**AD-05 · P2 · Bylinetrion mappar inte ansikte→roll; på desktop glest band.**
Element: byline. Problem: 3 överlappande avatarer läser som "ett team", men texten namnger 3 distinkta roller — kopplingen tappas. Desktop: stort tomt mittgap mellan vänster- och högerkluster.

**AD-06 · P3 · H2/H3 saknar rytmmarkör; TOC-accent är indigo, inte teal-brand.**
Element: rubriker + TOC aktiv pill. Problem: H2 lutar sig enbart på vikt/storlek — sektionsstarter kunde scannas snabbare med en lätt teal-markör. TOC:ens aktiva pill använder indigo/lavendel medan brandaccenten är teal `#00a991` — en inkonsekvens (accentfärgen borde vara teal, eller lavendeln medvetet motiverad).

**AD-07 · P3 · TOC uppfälld by default på mobil är ett hinder.**
Element: mobil-TOC. Problem: helt uppfälld accordion mellan byline och Snabbt svar tvingar läsaren scrolla förbi 9 rader innan innehållet; bör vara kollapsad by default på mobil.

---

## Omdesign-direktiv

1. **Bygg INLINE-CTA-kortet "Skicka en bild" (fixar AD-01, ART-06).** Placeras efter första pristabellen (~25–35 % djup, där prisnyfikenheten toppar). Native till Snabbt svar men *invers signal* — handling, inte info:
   - **Yta/bredd:** samma kolumnbredd som Snabbt svar/Pro Tip (~680 px desktop; full kolumnbredd mobil, 24 px inre padding). Mjuk **teal-tint bakgrund `#ECFBF7`** + **4 px teal `#00a991` vänsterstripe** (medvetet ljust, INTE mörkt Mikro-band — läsflödet ska överleva).
   - **Anatomi (vänsterställt, aldrig centrerat):** eyebrow `KOSTNADSFRI BEDÖMNING` (teal spärrad versal, samma stil som `SNABBT SVAR`) → **en bold navy rad** (H3-vikt) "Osäker på just ditt proppskåp?" → **en brödrad** "Skicka ett par skarpa bilder på din central — du får en kostnadsfri bedömning och ett prisförslag inom två arbetsdagar." → **EN lugn knapp** teal-fylld `Skicka en bild` → `/offert` (formulär förifyllt "Byta elcentral", bild-upload i fokus). Inget telefonnummer här — ett enda lågfriktionssteg (Baymard).
   - **Höjd:** medvetet KORTARE än Snabbt svar (3–4 rader) så det läser som en paus, inte en vägg. 48–56 px vertikal marginal isolerar det. Mobil: full-bredds tapknapp ≥44 px.

2. **Bygg NÄSTA-STEG-slutkortet och ta review-CTA:ns slot (fixar AD-02, ART-03).** Efter FAQ. Detta kort FÅR bära mer visuell vikt — det är beslutspunktens primära ask:
   - **Yta:** **midnight-platta `#090b32`** (brandmörk), full kolumnbredd, rundade ~20 px, generös padding (40 px desktop / 28 px mobil). Den mörka plattan gör kortet till end-zonens visuella ankare och skiljer det från alla vita brödkort.
   - **Anatomi:** eyebrow `NÄSTA STEG` (teal versal) → **H3 vit** "Vill du ha ett fast pris på ditt elcentralbyte?" → en vit brödrad "Berätta om ditt skåp så återkommer vi med en kostnadsfri offert — du ligger aldrig ute med pengarna." → **TVÅ knappar:** primär teal-fylld `Få en kostnadsfri offert` (→ /offert) + sekundär vit-outline `Ring 010-265 79 79` (tel:) → tertiär tyst länk "Räkna själv i Elcentral-kollen".
   - **Trust-fot inuti kortet (candour-sann, svarar Byggahus-oron):** liten rad `Registrerad hos Elsäkerhetsverket · ROT förräknat på fakturan · Fast pris i offerten`. **Ingen 5.0-siffra här** — per doktrinens seed: ta bort ratingraden så knapparna blir hela fokuset.

3. **Demota + reframe review-CTA (fixar AD-02, ART-02).** Flytta under Nästa-steg. Kund-gate:a asken: "Har vi hjälpt dig tidigare? Lämna gärna ett omdöme." Rätta svenskan ("**Hjälp oss**…", "tack **för att du tar dig tid**"). Behåll det förankrade "5.0 · 25 omdömen på Google"-mönstret men bara i den demoterade review-kontexten, aldrig i tävlan med konverterings-asken.

4. **Persistent högerrälskort på desktop (fixar AD-01 desktop + ART-05).** Från ~20 % scroll och nedåt, i den tomma högerspalten: kondenserad vertikal Nästa-steg-variant — litet midnight-kort `sticky; top: 8rem`, "Prata med en elektriker", teal `Få offert`-knapp + `Ring 010-265 79 79` tel-länk + Edvin-avatar-miniatyr. Löser tom-ränna + ingen-persistent-CTA i ett drag. (Mobil-motsvarighet: valfri tunn sticky bottenbar som experiment, ej default.)

5. **Prismatris mobil (fixar AD-03).** Byt de 3 versala spärrade etiketterna mot **en kompakt tvåkolumns nyckel-värde-rad** per fastighetstyp (etikett i normal sentence-case navy-medium vänster, värde höger), eller en horisontellt scrollbar riktig tabell. Lyft "PRIS EFTER ROT 30 %"-värdet som den enda feta/tealade siffran per kort (det läsaren vill ha), dämpa de andra två.

6. **Vänsterställ Pro Tip- och citatbrödtext; fixa roll-truncation (fixar AD-04).** Låt citattexten vara vänsterställd med citattecknet som hängande initial; låt roll-undertiteln radbryta i stället för att klippas (max 2 rader).

7. **Byline (fixar AD-05).** Sära avatarerna (ej överlappade) och para varje avatar visuellt med sin roll-rad, eller reducera till EN avatar (Faktagranskad-personen Edvin) + text. Desktop: dra ihop mittgapet — vänster- och högerkluster närmare, eller centrera meta-raden.

8. **Rytm + accentkonsekvens (fixar AD-06/AD-07).** Lägg en subtil **3 px teal vänster-tick** på H2 (inte full bar) för snabbare sektionsscanning. Byt TOC:ens aktiva pill från indigo till teal-tint `#ECFBF7` + teal vänsterstapel så accenten är konsekvent. Kollapsa mobil-TOC by default.

---

## Divergenta riktningar — Nästa-steg-slutkortet (det stora nya blocket)

**Riktning A — Midnight-platta (rekommenderas som default för slutkortet).** `#090b32`-kort, teal eyebrow, vit H3, två knappar (teal fill + vit outline tel), teal-fot. Ankare/premium, tillhör MainCTA-familjen, maximal visuell separation från de vita brödkorten. Risk: ett mörkt band mitt i en ljus artikel kan kännas "annons" — motverkas av candour-copy utan brådska.

**Riktning B — Mjuk teal-tint-panel (rekommenderas som default för INLINE-kortet, alternativ för slutet).** Ljus `#ECFBF7`-bakgrund, teal vänsteraccent, navy text, EN primär knapp + tel-länk inline. Stannar i artikelns vita/ljusa register, minst "annons-ig", passar den anti-sälj-candoura hjärtat i varumärket. Risk: lägre visuell vikt vid beslutspunkten än A.

**Riktning C — Split-kort med riktig elektriker (hög insats, testkandidat).** Vänster: Edvins ansikte (Faktagranskad-av-personen) + en mänsklig utfästelse "Jag läser din bild samma dag — Edvin, kvalitetsansvarig". Höger: mini-lead-teaser (namn / telefon / postnr) som postar en lead inline. Sätter en namngiven elektriker vid beslutspunkten → maximal trust, svarar "kan jag lita på dem?"-beteendet (Clarity: kontakt→Om-oss). Risk: tyngst att bygga; formfriktion vid beslutspunkten — testa mot A/B.

Default-mix: **B för inline-CTA (~30 % djup, tyst), A för Nästa-steg-slutkortet (ankare), C som high-effort A/B-test** mot A i slutslot:en.

---

## Vad som INTE ska röras (skydda det som funkar)

- **Snabbt svar-kortet** — mallens bästa element (grön stripe, bock, `SNABBT SVAR`-eyebrow, Sammanfattning/Nyckelpunkter). Exportera dess DNA, ändra inte det.
- **Bylinens innehåll + `Verifierad av expert`-pill + `17 min läsning`** — E-E-A-T är starkt; rör bara avatar-mappningen och mobilluften (AD-05), inte substansen.
- **Brödtextens rytm** — Outfit, navy `#090b32`, radhöjd ~1.7, teal inline-länkar. Läsbart för 35–65. Krymp inte, ändra inte färg.
- **Desktop-prismatrisen** — ren, läsbar 4-kolumn. Endast mobilreflowen ska röras.
- **Citatet från den namngivna experten (Edvin)** — behåll; fixa bara vänsterställning + roll-truncation.
- **Anti-sälj-sektionen "När vi avråder från byte — komplettering räcker"** — varumärkets moat i artikelform. Alla CTA-insättningar ska bevara det konsultativa registret utan brådska.
- **Den förankrade "5.0 · 25 omdömen på Google"-notationen** — behåll mönstret (rating+antal+källa), men bara i den demoterade review-kontexten, aldrig konkurrerande med konverterings-asken.
