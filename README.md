# Ampy — Conversion Rate Optimization Master Program (2026)

Fullständig CRO-audit och 3–6-månadersstrategi för ampy.se. Producerad 2026-08-02 av ett 41-agenters analysprogram (14 template-djupdykningar + 20 block-audits + 7 adversariella tvärlinser), grundat i en strukturell crawl av samtliga 326 URL:er, GSC-data, betaltrafik-utredningen och live-browserverifiering.

## Börja här
1. **`report/index.html`** — den designade rapporten (öppna i webbläsare). Exec summary → Sprint 0 → wireframes per sidtyp → blockprioriteringar → nya block → mätning → roadmap.
2. **`strategy/master-strategy.md`** — samma innehåll som beslutsdokument i markdown.

## Struktur
| Katalog | Innehåll |
|---|---|
| `context/` | Affärskontext, distillerat blockinventarie (30 block), metoddoktrin som styrde alla agenter |
| `data/` | `block-map.json` (verifierad blockordning för alla 326 sidor), blockstatistik, GSC-sammanfattning, live-browserobservationer, sitemaps, HTML-snapshots |
| `research/templates/` | 14 template-djupdykningar (homepage, service, 4× geo, B2B, produkt, pelare, hubbar, artiklar, team, om-oss/kontakt/thank-you, magneter, global nav) |
| `research/blocks/` | 20 block-audits med prioritetsaritmetik (sidor × funnelposition × effekt) |
| `research/synthesis/` | 5 tvärlinser: funnel-arkitektur (kanoniska spinen + överprövningar), trust-arkitektur (claims-kanon + 17 [GAP]), SEO-vakt (adversariell riskgranskning), mobildoktrin, mätplan |
| `research/missing/` | 11 nya block + magnetstrategi, rankade, med dödade förslag |
| `scripts/` | Crawlern som byggde block-kartan |

## De fem systemdiagnoserna (kortversion)
1. Konverteringen är **mekaniskt undertryckt**: JS-only hero-formulär, verifierad opacity:0-bugg, noll form-instrumentering.
2. **~900 CTA:er konvergerar på trasiga /kontakt/**; headern saknar telefon trots att samtal är enda registrerade konverteringen.
3. **Trust-systemet motsäger sig självt** (tre volymsiffror, oankrade 5.0, tre svarslöften); starkaste beviset (Elsäkerhetsverket-slagningen) är osynligt.
4. **Pris-message-match brister** — svaren finns men ligger i FAQ-block 8.
5. **Ordningen inverterad**: proof/FAQ/incitament efter asket; eljour saknar akutarkitektur.

## Regler för implementation
- Beroendekedjan: instrumentering → enterView-fix → SSR-form → CTA-ankring → omsekvensering → tester.
- Candour-gate: inga oankrade claims; [GAP]-märkta punkter kräver ägarbeslut (17 st, listade i trust-architecture.md).
- SEO: inget innehåll raderas — omsekvensering/ompaketering; FooterSEO:s per-sida-unika text behålls (SEO-vaktens veto).
