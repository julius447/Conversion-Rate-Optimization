# Ampy CRO-masterstrategi 2026 — konverteringsmotorn

*Baserad på: strukturell crawl av samtliga 326 URL:er, 41 specialistanalyser (14 templates + 20 block + 7 tvärlinser), GSC-data, betaltrafik-utredningen (Clarity/GA4), och live-verifiering i browser. All underliggande research: `research/`. Datalager: `data/`. Inget påstående i detta dokument saknar källa i dessa filer.*

---

## 0. Executive summary — fem systemdiagnoser

Sajtens problem är inte att den saknar innehåll, design eller CTA:er. Den har för många av fel sak, i fel ordning, med motstridiga siffror — och det enda mätinstrumentet är trasigt. De fem diagnoserna:

1. **Konverteringen är mekaniskt undertryckt, inte motivationsmässigt.** Hero-formuläret finns inte i server-HTML (tom `#ampy-form-root` som JS-injiceras sist på en sida med ~9–10 s LCP i labbet). Verifierat live: hela sektioner ligger på `opacity: 0` tills en enterView-animation triggar — snabbscrollande besökare möter blanka skärmar. Inga formulär skickar `form_start`. GA4:s "0 form starts" är alltså *oobserverbart*, inte diagnostiserat. → Detta förklarar betalutredningens läcka bättre än någon copy-hypotes.
2. **~900 CTA-instanser konvergerar på en trasig sida.** Nästan varje "Kostnadsfri rådgivning"-knapp navigerar till `/kontakt/` — en sida utan H1, utan synligt telefonnummer i brödytan, 386 ord — i stället för att ankra till formuläret som redan finns på sidan besökaren står på. Samtidigt saknar headern telefonlänk på alla brytpunkter, trots att telefonklick är de enda registrerade betalkonverteringarna.
3. **Trust-systemet motsäger sig självt.** Tre olika volymsiffror lever samtidigt ("1000+ Nöjda kunder" [bannad claim], "Över tusen genomförda installationer", "3 000+ installationer om året"). "5.0" förekommer 4–6 gånger per sida utan antal — medan sidans egen JSON-LD bär `reviewCount: 25`. Tre olika svarslöften på samma sida (60 sekunder / 24 timmar / "inom kort"). Sajtens starkaste verifierbara bevis — Elsäkerhetsverkets registerslagning förifylld med Ampys post (`?foretag=12047521`) — renderas som en 49px anonym logga tre block från footern.
4. **Message match brister på pris — den #1 svenska husägar-oron.** SERP-titlar lovar "fast pris"; frasen förekommer 0 gånger i brödtext. Prissvaren finns ("6 000–12 000 kr efter ROT") men ligger begravda i FAQ-block 8. Produktsidor visar "Totalt 5 890:-" medan sidans egen FAQ säger 7 000–10 000 kr. Betalsökningar som "byta elcentral pris" landar på sidor som inte besvarar frågan i skärm 1–2.
5. **Ordningen är inverterad mot beslutspsykologin.** Proof efter ask (Certificates medianslot 18, TeamSection 14, FAQ *efter* formuläret på 131 sidor), incitament (ROT/Grön teknik) efter formuläret, och eljour — det mest brådskande intentet — möts av samma lugna installations-template med 7-fälts formulär först.

**Det positiva:** 100 % template-konsekvens (en fix skalar till 56+ sidor), ett genuint starkt MainContact-formulär, godkänd homepage-hero med rätt disciplin, utmärkt E-E-A-T-maskineri i artikelmallen, verklig myndighetsproof som bara behöver flyttas, och `.aof`-formulärets per-sida-resolver som är tekniskt utmärkt. Grunden är byggbar — den behöver omsekvenseras, saneras och mätas.

---

## 1. Sprint 0 (vecka 1–2): Mät + sanera — inga tester, inga beroenden

**Regel: inget av detta A/B-testas. Det är trasigt, osant eller omätbart. (Tier 0 i mätplanen.)**

| # | Åtgärd | Omfattning | Källa |
|---|---|---|---|
| 0.1 | **Instrumentering:** `form_view/start/error/submit` + `tel_click` + blockexponering för alla sex formulärsystem; Clarity-taggning | Sitewide | measurement-plan.md |
| 0.2 | **Pixel-integritet:** `/thank-you/` noindex + konvertering på submit-event, inte på pageview (idag myntar varje direktbesök en fejkkonvertering) | 1 sida, hela programmets beroende variabel | seo-guard, header-footer-thankyou |
| 0.3 | **enterView-buggen:** ta bort hidden-on-load/opacity-gates från innehålls- och konverteringsblock | Sitewide (verifierad live) | mobile-doctrine, live-observations |
| 0.4 | **Stavfelet "Kostnadsfri radgivning"** (saknat å) i CTA-biblioteket | ~290 sidor, en edit | pillar-pages, product-blocks |
| 0.5 | **Dött nummer 010-123 45 67** i kalkylatorernas felmeddelande (rätt: 010-265 79 79) | Alla batterisidor + hubbar | product-pages, category-landing |
| 0.6 | **Publicerade platshållare:** literal "[ort]" i /eljour/ MainCTA; "(ADD FAQ SECTION)" som H2 i rot-avdrag-2026 + gron-teknik-2026 | 3 sidor | pillar-pages, articles |
| 0.7 | **/elservice/ routing-grid är död:** 22 "Till {tjänst}"-kort är `<span>` utan `<a href>` | Hubb #1, 22 länkmål | category-landing |
| 0.8 | **Staging-404:** pillar-hero förladdar `staging.ampy.se/hero-bg-1.webp` (404) i LCP-fönstret | 5 pelarsidor | hero1-minimenu |
| 0.9 | **Telefon i headern:** synlig `tel:`-knapp på alla brytpunkter, utanför hamburgaren | 325 sidor (score 2925 = högst i hela auditen) | header-footer-thankyou, mobile-doctrine |
| 0.10 | **"Ordinarie pris"-genomstrykningen** (exakt 2× netto = rea-inramning av ett villkorat skatteavdrag) → "Pris före Grön Teknik-avdrag" | 26 produktsidor | product-pages, trust-architecture |
| 0.11 | **Eljour-falsheten** "Se alla områden … i listan nedan" (visar 20 av 56) + hemförsäkringsblockets felknapp "Läs mer om ROT-avdrag" | 56–57 sidor | map-block, incentive-blocks |
| 0.12 | **Ägarsession — sifferkanon (17 [GAP]):** betyg+antal (25?), EN volymsiffra (1000+ totalt vs 3000+/år), 60-sek-löftet, 24h helger?, fast-pris-i-offerten, jourens inställelseavgift, Trygg Hansa/ID06-status, SUPERKAMPANJ-beläggen, öppettider, foto-bedömningens 2-dagars-SLA m.fl. | Låser upp hela trust-systemet | trust-architecture.md §GAP |
| 0.13 | **Lead-rör-test:** testa alla 5 magnetformulär + verifiera n8n-webhooks (stubbar droppar leads idag) | 7 magneter | lead-magnets, magnet-wrap |

---

## 2. Den kanoniska sidryggraden (gäller alla mallar)

**CTA-kanon:** "Kostnadsfri rådgivning" (knapp) / "Boka rådgivning" (submit) / "Ring 010-265 79 79" (nummer alltid synligt). *Gratis rådgivning, offert, förslag, konsultation* pensioneras som knappetiketter. **Ankar-regeln:** alla body-CTA:er scrollar till sidans eget formulär (`#main-contact`); endast chrome + formulärlösa sidor navigerar till /kontakt/. **Ask-budget:** max 5 body-asks per sida (idag 13–17), var och en med eget jobb. **Telefondominans per intent-temperatur:** URGENT (eljour) = ring-först + sticky call-bar, HIGH (service/geo/produkt) = SSR-kortformulär först, MID (varumärkesverifiering) = ankrat formulär-close, LOW (artiklar/magneter) = värde → "Nästa steg".

**Spinen:** Hero → **TrustStrip** (Elsäkerhetsverket-länk + "5,0 av 5 · N omdömen" + EN volymsiffra) → Testimonials (vertikal-pinnade, före första telefon-asket) → router/pris → SEO-innehåll → incitament (ROT/GT) FÖRE formuläret → VarProcess → FAQ ALLTID före MainContact → Map → sammanslagen SEO-svans → Certificates → terminal. Fullständig tabell per mall (16 rader, med explicita överprövningar av enskilda template-filer): `research/synthesis/funnel-architecture.md §2`.

**Block som dödas/slås ihop:** MikroCTA pensioneras (173 sidor; skalet återanvänds som B2B-serviceavtal/team/artikel-close). BlueCTA+MainCTA → ETT PhoneBand. FooterSEO viks in i prefootern (men per-sida-unika ACF-texten BEHÅLLS — SEO-vaktens veto mot boilerplate). Produkt-popupen ersätts av inline 3-fälts formulär. VisualCTA, legacy-formuläret på /elinstallation/, homepage-ProductGrid (ersätts av ServiceRouter + 2-korts ProductTeaser) — bort.

---

## 3. Mallarna i korthet (djupdykningar i `research/templates/`)

- **Homepage** (89 % av organiska klick; 73 % varumärkes-verifierare): Hero-1 behålls (godkänd), CTA → ankare. ServiceRouter (MiniMenu+ServiceGrid sammanslagen, tjänster först) ersätter batteri-först-ProductGrid. Certificates NY på homepage. Ägarens instinkt om ProductGrid bekräftades; hans skiss justerades (routern raderas inte — den flyttas upp).
- **Service (22):** Hero_2 v2 (H1 = riktiga rubriken, SSR-formulär) → **Prisblock** (spann efter ROT, redan skrivet i FAQ — 90 % copy-flytt) → TrustStrip. ROT-blocket eligibility-gatas (felsökning får INTE ROT — sidan motsäger sig själv idag).
- **Geo elektriker/elinstallation/laddbox (168):** samma spine; laddbox-i behåller ProductGrid men med dubbel-CTA till sidans formulär; ContentBlock upp från slot 15.
- **Eljour (56 + pelare):** egen arkitektur — telefon-i-H1, INGET hero-formulär, symptomblocket med återställd sticky panel + fast mobil ring-bar (verifierat: shipped CSS saknar sticky helt), tvåfilig kontakt ("Akut? Ring" / "Kan vänta? namn+telefon"), Hemförsäkring ersätter ROT.
- **Elektriker-för-X (13):** org-skin — OrgTrustStrip (ID06/Trygg Hansa/ESV), Referenser i stället för "grannar", VarProcess-B2B (offert→avtal→utförande→dokumentation), org-fält i MainContact.
- **Produkt (26):** omramas från e-handel till installationspaket — inline-form ersätter popup, "Vad ingår i priset?" (popup-innehållet upp på sidan), ärlig prisrad, namngiven expert, kalkylator-embed.
- **Artiklar (11):** E-E-A-T-skalet behålls; inline-CTA vid ~30 % djup, "Nästa steg"-kort ersätter den inverterade Google-recensionsbönen, `tel:` på varje "ring eljour"-sträng.
- **Team (6) + om-oss:** profilerna är länk-föräldralösa och saknar CTA — stäng återvändsgränden först, länka sedan TeamSection-korten, bygg om /om-oss/ till trust-hubben (Clarity-besökaren gick dit och fann: inga ansikten, inga omdömen, inga certifikat, tomma sifferkort).
- **Magneter (7):** wrap-standard = AlternativHero + verktyg (orört — approved rendering) + VarProcess + FAQ + MainContact. Ordning: energi → laddbox → elcentral.
- **Kontakt + Thank-you:** /kontakt får H1, telefon, öppettider, "Vad händer sen". /thank-you får kalibrerat löfte ("inom 24 timmar", "samtalet kommer från 010-265 79 79 — spara numret"), förberedelse-checklista per form_type, teamansikten.

---

## 4. Blockprioriteringar (fullständiga audits i `research/blocks/`)

| Prio | Block | Score | Kärnproblem → åtgärd |
|---|---|---|---|
| P0 | Header/Footer/ThankYou | 2925 | Ingen telefon i header; pixel på pageview; TY utan förväntanssättning |
| P0 | Hero_2 + aof-form | 2340 | Trippel-ask, JS-only-form, dubbla H1, adress-före-värde → SSR + ankare + fältbantning |
| P1 | MainContact | 1770 | Oankrade claims, 5 obligatoriska fält, mobilstack inverterad, exponeras sent |
| P1 | Certificates | 1740 | ESV-beviset osynligt på slot 18 → klonas till TrustStrip i beslutszonen |
| P1 | FAQ | 1236 | Efter formuläret på 131 sidor; 4 frågor; tom ARIA; saknar ansvar/garanti-frågorna |
| P1 | Testimonials | 1164 | Slumpad ordning krossar message match → vertikal-pinning; badge oankrad |
| P1 | ContentBlock | 1164 | Textvägg utan punkter; generiska bilder; svarar inte på Byggahus-frågorna |
| P1 | Incitament (ROT/GT/Hemförs.) | 1108 | Fel CTA på eljour-tvillingen (P0-del); inget kr-exempel; efter formuläret |
| P1 | MainCTA | 1072 | Gradient under WCAG-kontrast; "60 sekunder" overifierat |
| P1 | MikroCTA+BlueCTA | 920 | 13 asks/sida → döda/slå ihop till ETT PhoneBand |
| P1 | VarProcess | 848 | "Vi går vi igenom"-fel; saknar pris-transparenssteg; jourvariant fel |
| P0 | Metrics-familjen | 684 | "1000+ Nöjda kunder" = bannad claim live på 114 sidor |
| P1/P2 | VissteDuAtt (580), FooterSEO (580), Produkt-ekosystemet (580), MapBlock (530), TeamSection (364), Artikel-block (99), AlternativHero (72), Hero-1 (36 men 2×P0-delar) | | Se respektive fil |

---

## 5. Nya block (11 st, `research/missing/00-blocks-index.md`) och magneter

**Bygg först:** 1) **Pris & offert-blocket** (score 2223 — message-match-fixen; 90 % copy-flytt från FAQ), 2) **TrustStrip** (1740; fyra format, ESV-länken är kärnan), 3) **Sticky call-bar** (eljour alltid-på; test på artiklar), 4) **Inline mini-form SSR** (3 fält), 5) **Efter-submit-paketet** (/thank-you), 6) **Two-lane contact** (eljour), 7) **ServiceRouter** (homepage), 8) **Nästa steg-artikelkort**, 9) **Vad ingår i priset?** (produkt), 10) **B2B-referenser**, 11) **Alla områden-hub + deterministisk ort-rad** (ersätter 20-av-56-lotteriet som churnar länkgrafen).

**Magneter:** portföljens problem är rör/wrap/distribution — inte inventarie. Vecka 1: testa alla lead-rör + döda platshållarnumret. Månad 1: wrap-standard på energi/laddbox/elcentral + **Foto-bedömningen** (enda nya magneten — service-lane, "skicka bilder → bedömning inom två arbetsdagar" [GAP: SLA], 3 fält + foton). Verktygs-tiles (EN komponent) för korslänkning — medvetet INTE på geo-sidor (återöppnar inte funnel-hijacken). Dödade med motivering: elpriskoll, e-post-gated PDF:er, kalkylator #8-förslag.

---

## 6. Mätning & test-ärlighet (`research/synthesis/measurement-plan.md`)

- **KPI-träd:** primär = kvalificerade leads/vecka (samtal >90 s + CRM-relevant, formulär som når CRM). Vakter: CRM-disposition, telefon/formulär-mix, bounce, LCP-fältdata. CPL-tak 1 300–2 000 kr.
- **Power-ärlighet:** vid ~450–900 sessioner/månad tar ett sitewide bottom-line-test 5–10 månader. Därför: Tier 0 = fixa-utan-test (trasigt/candour), Tier 1 = ship-and-monitor (best practice med diagnostik), Tier 2 = riktiga tester först när betalvolymen skalar: hero-ask form-först vs ring-först, sticky-bar på icke-eljour, minimala fältsetet (med CRM-kontaktbarhets-vakt), laddbox-i ProductGrid-dragningen.
- **Veckoritual 45 min:** leads-scorecard mot CPL-taket, funnel-diagnostik med noll-event-tripwire, 100 % genomgång av betalda Clarity-inspelningar (låg trafik gör det möjligt), ändringsannoteringar.

---

## 7. Roadmap 3–6 månader

| Fas | Innehåll |
|---|---|
| **V 1–2 (Sprint 0)** | Hela §1-listan: instrumentering, pixel, sanering, ägarens sifferkanon, header-telefon, lead-rör-test |
| **Månad 1** | Hero_2 v2 (SSR-form, H1, ankar-CTA) på 260 sidor · Prisblock + TrustStrip på service/geo · FAQ-flytt + utökning · MainContact-bantning + mobilstack · /kontakt-ombyggnad · CTA-retarget (~600 länkar) · magnetwrap energi/laddbox/elcentral |
| **Månad 2** | Eljour-arkitekturen (sticky bar, two-lane, jourvariant, hemförsäkringsfix) · Homepage ServiceRouter + Certificates · Produkt: inline-form + Vad ingår + ärlig prisrad · Artikel-close + tel-länkar · Team-mesh + om-oss-ombyggnad · Foto-bedömningen |
| **Månad 3** | B2B org-skin (13 sidor) · Alla områden-hub + deterministisk MapBlock · SEO-svans-merge + Terminal · resterande magneter + verktygs-tiles · PhoneBand-konsolidering |
| **Månad 4–6** | Tier 2-testprogram i takt med betalskala (förregistrerade, fixed-horizon) · BRF-laddguide (candour-gated) · iterera på Clarity/CRM-data · kvartalsvis claims-revision |

**Beroendekedjan som inte får brytas:** instrumentering → enterView-fix → SSR-form → *därefter* CTA-ankring (att ankra till ett osynligt formulär är värre än att navigera) → *därefter* omsekvensering → *därefter* tester.
