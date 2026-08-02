# Category / Landing Hub Template (AlternativHero pages)

URLs analyzed (all fetched live 2026-08-02): https://ampy.se/elservice/ · https://ampy.se/laddboxar/ · https://ampy.se/solcellsbatterier/ · https://ampy.se/nyheter/
Pages using this template: **4** (block-map category "page"; the other AlternativHero users — 2 lead magnets, 6 team pages — are separate templates). Downstream dependency: the 22 service pages under /elservice/*, 16 laddbox products, 10 battery products, 8 articles — these hubs are their internal-linking parents.

**Template job (JTBD):** these are ROUTING pages. The visitor's job is "help me find the right specific page (service/product/article), or let me talk to a human if I can't decide." Verdict up front: **/laddboxar/ and /solcellsbatterier/ route; /elservice/ visually pretends to route but factually cannot (dead grid); /nyheter/ is a naked archive that dead-ends.**

---

## Current block sequence (verified against live HTML + block-map.json)

### /elservice/ (title "Se utbudet över alla våra eltjänster!", word_count 1 042, **h1: none**)
1. **Header** — mega-menu, "Gratis rådgivning" CTA, mobile: offcanvas + "Ring en expert" + "5.0".
2. **AlternativHero** (`laddbox-hero`) — breadcrumb "Hem **Services**" (English label in a Swedish trail), heading **H3** "Elinstallationer över hela Sverige" (white→green gradient on dark navy card), paragraph "Vi utför allt från akuta felsökningar och byte av elcentral till modern belysningsdesign." No CTA, no image, no proof. Mobile: same card, heading max-width 100% under 480px.
3. **services-loop** (NOT in block-map — undetected block) — 22 photo cards (Belysning, Elcentral, Köksrenovering, Luftvärmepump, Smarta hem, Spotlights, … Strömbrytare), each: image + H3 + one-line description + a "Till {tjänst}" button. **Verified in live DOM: the section contains 0 `<a href>` — every "Till Belysning"-style button is a `<span class="brxe-button">`; no onclick, no data-href, no click interaction.** The whole grid is `data-interaction-hidden-on-load="1"` with an enterView fadeIn (invisible until JS runs). Mobile: cards stack into a long single/two-column scroll (~22 screens of cards), still unclickable.
4. **MainCTA** — "Prata med en elektriker inom 60 sekunder!" + Ring-only CTA (tel:) + "5.0 på Google" (no count, no link anchor visible in text).
5. **VarProcess** — "Så funkar det" 4 steps ("1. Samtal med elektriker … 4. Installation utförd. Du får ett protokoll … inklusive avdraget.").
6. **MainContact** — full two-pane form section ("Från start till mål levererades en service i världsklass." / "5 av 5 · Betyg på Google" / "3 000+ genomförda installationer om året").
7. **FAQ** — 4 good questions (ROT 30%, DIY-byte av uttag, vad ingår i elcentralsbyte, eljour-utryckningstid "inom 60 minuter").
8. **Prefooter/Footer.**

### /laddboxar/ (title "Se alla våra laddboxar", word_count 1 226, **h1: none**)
1. Header → 2. **AlternativHero**: H3 "Laddboxar över hela Sverige" + paragraph. No CTA/proof/image.
3. **ProductGrid** (`product`) — 16 laddbox cards **with real anchors** ("Läs mer" → /laddboxar/zaptec-go/ etc.), tags SUPERKAMPANJ/NYHET/BÄSTSÄLJARE, chips "1-fas & 3-fas 22 kW", prices "Fr. 4 490 kr" (one card "Fr. 4 990 **Kr**" — inconsistent). Almost every card says "upp till 22 kW" / "smart" — near-zero differentiation. **No filter, no sort, no comparison, no "hjälp mig välja", and zero body links to Laddboxkalkylatorn** (it exists only in the header mega-menu). Mobile: 16 stacked cards.
4. **MainCTA** — "Prata med en laddboxinstallatör inom 60 sekunder!" + Ring + "5.0 på Google".
5. **VarProcess** — with duplicated-word typos: "Vi går **vi** igenom dina behov…", "Vi skickar **vi** ut en bekräftelse samt ett formulär för Grön teknik ansökan…".
6. **MainContact** → 7. **FAQ** (Grön Teknik 50%, lastbalansering, standardinstallation, laddhastighet) → 8. Prefooter/Footer. **No GrönTeknik block** — the 50%-halved-price message lives only inside a collapsed FAQ answer.

### /solcellsbatterier/ (title "Våra hemmabatterier – Jämför marknadens bästa batterilagring", word_count 1 291, **h1: none**)
1. Header → 2. **AlternativHero**: H3 "Batterilagring med installation över hela Sverige".
3. **ProductGrid** — 10 battery cards with real anchors, prices Fr. 33 000–70 500 kr, kWh-range chips; also links to thin tag archives (/product_tag/bastsaljare/, /product_tag/superkampanj/).
4. **MainCTA** — "Prata med en batteriexpert inom 60 sekunder!".
5. **Calculator-UI** (`ampy-calc`) — "Vad tjänar du på ett solcellsbatteri?" full two-pane calculator: model/capacity, elprisområde, stödtjänster, effekttariff, payback-kurva, "Så har vi räknat" methodology, and its own embedded lead form "Få en exakt offert … inom 24 timmar" (Namn/E-post/Telefon/Postnummer). **Its error state reads "Något gick fel. Ring oss på 010-123 45 67" — a placeholder phone number; the real number is 010-265 79 79.**
6. **VarProcess** (same typos) → 7. **MainContact** (second full form on the page) → 8. **FAQ** (payback "3–6 år", befintliga solceller, ö-drift, Grön Teknik 50%; note grammar "…framförallt då staten slopad 60-öringen") → 9. Prefooter/Footer.

### /nyheter/ (title "Nyheter & Inspiration", word_count 579, **h1: none**)
1. Header → 2. **AlternativHero**: breadcrumb "Hem Nyheter" + the single word **"Nyheter"** as an H3. No paragraph, nothing else in the hero.
3. **Article loop** (undetected by block-map, which lists only Header→AlternativHero→Prefooter) — 8 cards (date, title, ~20-word excerpt, "Läs artikel" → real anchors, e.g. /byta-elcentral-2026/). Five of eight are dated "juni 14, 2026" (batch-publish look). **No pagination, no category filter, no search, no intro text.**
4. **Prefooter/Footer.** No MainContact, no CTA of any kind between header and footer.

---

## Customer-flow walkthrough (35–65 Swedish homeowner, mobile)

**First 5 seconds:** every hub opens with a dark navy card whose only content is a gradient headline and (except /nyheter/) one sentence. No photo, no face, no phone number, no proof. For a trust-seeking 55-year-old this first screen answers neither "är det här ett riktigt företag?" nor "vad gör jag nu?". The header's "Gratis rådgivning" pill is the only visible action.

**Scroll (elservice):** a wall of 22 attractive photo cards appears (after the JS fadeIn). She finds "Vitvaror", taps the card, taps "Till Vitvaror" — **nothing happens**. Cards look interactive (Jakob's law: category cards on every Swedish e-commerce/service site are links) but are inert spans. Best case she scrolls on, worst case she concludes the site is broken. Note the July Clarity recording: *23 seconds on Belysning, no click* — this dead grid is a plausible mechanical explanation for click-less sessions arriving at service categories, not just a motivation problem.

**Scroll (laddboxar/solcellsbatterier):** 10–16 nearly identical product cards ("smart", "upp till 22 kW", 5 års garanti) with prices that differ by a few hundred kronor. She has no way to answer "vilken passar mitt hus?" — no filter (fast kabel? utomhus? två bilar?), no comparison, no guide link. Choice overload (Hick's law; Baymard category-page research: undifferentiated grids without guided selection push users to abandon rather than choose). The FAQ, five screens down, is where she'd learn the price effectively halves via Grön Teknik — if she ever opens it.

**Decision:** the pages DO end well — MainCTA (call) → VarProcess (how it works) → MainContact (the site's strongest form). A patient scroller converts. But the middle of the funnel leaks: on /elservice/ the routing layer is broken; on the product hubs the "compare" promise ("Jämför och välj laddbox…" in the mega-menu, "Jämför marknadens bästa batterilagring" in the meta title) is not kept by any comparison capability — a message-match failure inside the site's own navigation.

**/nyheter/:** she reads 8 titles and either clicks an article or leaves. The hub itself offers no reason to trust Ampy, no path to a service page, no CTA. Pure dead-end (the only "conversion path" is the header).

---

## What works (keep)

- **The closing trio** MainCTA → VarProcess → MainContact is coherent and on every commercial hub: call option, expectation-setting process, then the site's best form with proof stack ("5 av 5 · Betyg på Google", "3 000+ genomförda installationer om året" — pending owner anchoring, see CAT-08).
- **FAQ quality is genuinely high** — real questions with candour-register answers ("Enligt svensk lag får du byta ut befintliga strömbrytare och uttag för högst 16 ampere om du har tillräcklig kännedom…"). This is exactly the content a Konsumentverket-minded homeowner wants. Keep verbatim; only re-position.
- **Product cards on laddboxar/solcellsbatterier have honest, concrete specs** (kW, kWh-range, fas, garanti, from-price) and real links. The SUPERKAMPANJ/NYHET/BÄSTSÄLJARE tags are useful scent — if the claims are true (candour check with owner).
- **The battery calculator embed** is best-in-class structure: value-then-ask, its own low-friction 4-field offert form, honest methodology box ("Den här kalkylatorn ger en uppskattning — inte ett erbjudande och inte en garanti."). This is the pattern the *other* hubs should copy.
- **Breadcrumbs everywhere** (orientation, Jakob's law) and clean information scent from hero paragraphs (except /nyheter/).

---

## Findings

**CAT-01 — /elservice/ service grid is non-functional: 22 cards, zero links. Severity P0.**
Verified live: the `services-loop` section contains 0 `<a href>`; every "Till {tjänst}" button is a `<span>`; no click handler exists in markup. The template's entire reason to exist — routing — is broken. Secondary damage: (a) SEO — the hub passes zero internal links to its 22 children; (b) **orphan risk** — Luftvärmepump, Armatur, Badrumsrenovering and Köksrenovering appear in neither the header mega-menu nor the prefooter, so this dead grid may be their only intended internal link source; (c) the grid is `hidden-on-load` behind a JS fadeIn — with the site's known ~9–10 s lab LCP, slow devices show a hub with *no visible services at all* for seconds. Frameworks: Jakob's law (cards must click), NN/g affordance, internal-linking basics. Mobile: identical failure, plus ~22 screens of unclickable scroll. Fix: convert each card wrapper (or button) to a real link in Bricks, remove hidden-on-load. **Priority score: 1 page × 3 (routing = funnel-entry weight) × 3 (high effect) = 9, plus unblocks 22 downstream money pages.**

**CAT-02 — Placeholder phone number in the battery calculator error state. Severity P0 (trust-damaging, trivial fix).**
Live copy on /solcellsbatterier/: "Något gick fel. Ring oss på **010-123 45 67** så hjälper vi dig direkt." The real number is 010-265 79 79. It renders exactly when a lead tried to convert and the webhook failed — the worst possible moment to display a fake number. Candour gate + basic QA. Mobile: same. **Score: 1 × 3 (form-adjacent) × 3 = 9** (one-line fix).

**CAT-03 — No H1 on any of the four hubs. Severity P1.**
Verified: `h1 count: 0` on all four (block-map "h1": [] concurs); the hero heading is an `<h3 class="laddbox-hero__heading">`. These pages target head terms ("laddbox", "batterilagring", "eltjänster") with the weakest possible heading semantics, and card/product names are also H3s so the document outline is flat. Fix inside AlternativHero once → fixes all four (plus the lead-magnet/team pages sharing the block). Frameworks: SEO fundamentals; NN/g page-title clarity. **Score: 4 pages × 3 (hero) × 2 (med-high effect) = 24.**

**CAT-04 — /nyheter/ is a naked archive: one-word hero, no intro, no taxonomy, no pagination, no CTA, no contact block. Severity P1.**
Hero text in full: "Hem Nyheter **Nyheter**". 8 articles, 5 dated the same day (looks machine-published to a wary reader), no category filter, no路 path to services, nothing between the last card and the footer. Content marketing that cannot hand a warmed-up reader to a conversion path. Frameworks: MECLABS (motivation exists — the articles are decision-support — but no value channel), content-hub best practice (hub = topical authority page, not a bare loop). Mobile: same. **Score: 1 × 1 (low-funnel weight) × 3 = 3** — but strategic for SEO/E-E-A-T.

**CAT-05 — AlternativHero carries no CTA, no proof, no image on commercial hubs. Severity P1.**
First screen = dark card + gradient H3 + one sentence. For a routing page the hero need not sell hard, but it currently doesn't even offer the phone number or the "5.0" row that Hero_2 pages get, and provides no visual reassurance (no human, no work photo). MECLABS heuristic: value clarity ok, incentive/proof = 0 at the moment of arrival. Mobile: the dark card fills most of the first viewport — the routing content is below the fold. Fix: add a compact trust row (anchored Google rating + Ring-link) inside the hero; keep it light. **Score: 3 commercial pages × 3 × 2 = 18.**

**CAT-06 — Product hubs promise comparison but provide none; no guided selection; calculator cross-links missing. Severity P1.**
The mega-menu sells /laddboxar/ as "Jämför och välj laddbox för villa, BRF och företag"; the battery meta title says "Jämför marknadens bästa batterilagring". On-page: flat card grids, no filters (fas/effekt/fast kabel/utomhus/BRF), no compare view, and — verified — **zero body links from /laddboxar/ to Laddboxkalkylatorn** even though the tool exists. Message-match failure (Google message-match doctrine applies to internal scent too) + Hick's law/choice overload + Baymard guided-selling findings. Mobile: 16 undifferentiated cards in sequence make comparison memory-bound. **Score: 2 pages × 2 (mid) × 3 = 12.**

**CAT-07 — The strongest purchase motivator (Grön Teknik 50% / halved price) is buried in a collapsed FAQ; from-prices carry no avdrag context. Severity P1.**
On /laddboxar/ and /solcellsbatterier/ the cards say "Fr. 4 490 kr" etc. with no line clarifying whether Grön Teknik is included, and the 50%-reduction explanation appears only inside FAQ answers five screens down ("Du får 50 % skattereduktion på både material och arbetskostnad direkt på fakturan."). Swedish homeowners' #1 documented anxiety is final-price surprise (Byggahus/Reddit anchor in business context); ambiguity about what "Fr."-pris means feeds it. The site owns a GrönTeknik block — it simply isn't placed on these hubs. MECLABS: incentive term underexploited; anxiety term inflated. **Score: 2 × 2 × 3 = 12.**

**CAT-08 — Unanchored/unverified claims: "5.0 på Google" (MainCTA), "3 000+ genomförda installationer om året" (MainContact), and three "inom 60 sekunder" promises. Severity P1 (candour gate).**
"Prata med en elektriker/laddboxinstallatör/batteriexpert inom 60 sekunder!" is a concrete operational promise (call answered <60 s) that must be owner-confirmed or softened; "5.0 på Google" appears without count or date anchor (candour rule: anchored or flagged); "3 000+" needs owner confirmation. None of these should be deleted if true — they should be **anchored** (e.g. rating + antal omdömen + länk till GBP). Cialdini social proof only works when verifiable. **Score: 3 pages (+ every other page using MainCTA/MainContact) × 2 × 2 = 12 within this template.**

**CAT-09 — /elservice/ grid: 22 flat cards, arbitrary order, missing the highest-intent routes. Severity P2.**
Card order (Belysning, Elcentral, Köksrenovering, Luftvärmepump, …) matches neither demand (July search terms: "installera taklampa", "installera diskmaskin", "byta elcentral pris", "elfel i huset") nor the nav's own 4-group taxonomy. And the grid omits **Eljour** and **Elektriker** entirely — the two "Populära" nav items, and (Unbounce home-services benchmark) the urgent/repair intents that convert best. HYPOTES: grouping the grid (Akut & felsökning / Elcentral & säkerhet / Belysning / Kök & badrum / Laddning & energi) with Eljour first will lift routing CTR. **Score: 1 × 2 × 2 = 4.**

**CAT-10 — VarProcess copy defects on laddboxar + solcellsbatterier. Severity P2.**
Live: "Vi går **vi** igenom dina behov och skickar en transparent offert…", "Vi skickar **vi** ut en bekräftelse samt ett formulär för Grön teknik ansökan och föranmälan!". Also FAQ grammar "…framförallt då staten slopad 60-öringen" and "berättigar dig grön teknik avdraget". Duplicated words in the trust-building block read as carelessness — fatal register for a "noggrannhet" trade. **Score: 2 × 2 × 1 = 4** (minutes to fix).

**CAT-11 — Breadcrumb label "Services" (English) on /elservice/. Severity P3.**
Live trail: "Hem **Services** …". Swedish-first rule; also inconsistent with "Hem Laddboxar" / "Hem Batterier" / "Hem Nyheter" on siblings. **Score: 1 × 1 × 1 = 1.**

**CAT-12 — Hubs are SEO-thin: ~1 000 words that are mostly chrome; no ContentBlock/CE substance despite head-term targeting. Severity P2.**
elservice 1 042 / laddboxar 1 226 / solcellsbatterier 1 291 / nyheter 579 words, most of it nav + card labels. MECLABS HealthSpire: longer pages win when added content answers real decision questions — a compressed "Så väljer du rätt laddbox" / "Vad kostar elektriker?" section (accordion or CE block; content stays in DOM) adds relevance without hurting routing. Never delete the grids — add beneath them. **Score: 3 × 1 × 2 = 6.**

**CAT-13 — Conversion firepower is inverted vs. commercial priority. Severity P2.**
Owner priority is service > laddbox > battery, yet /solcellsbatterier/ (lowest priority) is the only hub with an embedded calculator + dedicated 4-field offert form, while /laddboxar/ (priority 2) doesn't even link its existing calculator and /elservice/ (priority 1) has a broken grid. Rebalance: port the Calculator-UI embed pattern to /laddboxar/ (Laddboxkalkylatorn exists, v-mature), fix /elservice/ first. **Score: 3 × 2 × 2 = 12.**

**CAT-14 — Minor product-grid hygiene. Severity P3.**
"Fr. 4 990 **Kr**" capitalization outlier (go-e Gemini); battery grid links to thin tag archives (/product_tag/bastsaljare/ etc.) that dilute crawl; "Zaptec Pro — Begär offert" is the only card without a price (fine for B2B, but consider a "för BRF/företag" label to explain why). **Score: 2 × 1 × 1 = 2.**

---

## Recommended sequence (wireframe)

### Commercial hubs (/elservice/, /laddboxar/, /solcellsbatterier/)

| # | Block | Why here | New/existing/modified |
|---|-------|----------|----------------------|
| 1 | Header | unchanged | existing |
| 2 | **AlternativHero v2** — real `<h1>`, Swedish breadcrumb, + compact trust row (anchored Google rating + tel-link) | orientation + immediate proof + escape hatch to the call without selling pressure | modified (fixes CAT-03/05/11 for all 4 pages at once) |
| 3 | **Routing grid** — elservice: linked, grouped (Akut/Eljour first → Elcentral & säkerhet → Belysning → Kök & badrum → Energi), max ~6 per group with "visa alla"; laddboxar/solcellsbatterier: ProductGrid + filter chips (fas, effekt, fast kabel, BRF/företag) + "Osäker? Räkna fram rätt modell →" link-card into the relevant kalkylator | the page's core job; guided selection kills choice overload (CAT-01/06/09) | modified + new filter row |
| 4 | **GrönTeknik / ROT block** (gron-teknik on product hubs; rot on elservice) — 3-item explainer + "priser visas före avdrag"-klargörande vid korten | surfaces the halved-price incentive at decision moment (CAT-07); block already exists in library | existing, re-placed |
| 5 | **Calculator-UI embed** (solcellsbatterier: keep; laddboxar: port Laddboxkalkylatorn; elservice: skip or Elcentral-kollen teaser card) | value-then-ask lead capture mid-page; proven pattern on battery hub (CAT-13) | existing/ported |
| 6 | **MainCTA** — claims anchored ("60 sekunder" owner-verified or reworded to "Prata direkt med en elektriker"), rating anchored with count | phone path for decided visitors | modified (CAT-08) |
| 7 | **VarProcess** — typos fixed | expectation-setting before the form | modified (CAT-10) |
| 8 | **Compressed SEO section** (accordion/CE block: "Så väljer du…", pris-FAQ, regelverk) | HealthSpire: decision-answering depth without pushing form down; feeds head-term relevance (CAT-12) | new (reuses ContentBlock/CE patterns) |
| 9 | **MainContact** | the closer; strongest asset stays last-but-one | existing |
| 10 | **FAQ** | objection cleanup adjacent to the form | existing |
| 11 | Prefooter/Footer | unchanged | existing |

### /nyheter/

| # | Block | Why here | New/existing/modified |
|---|-------|----------|----------------------|
| 1 | Header | | existing |
| 2 | AlternativHero v2 — H1 "Nyheter & guider" + one candour-register intro sentence + trust row | a hub, not a label (CAT-04) | modified |
| 3 | **Featured/pillar row** — 1–2 pinned cornerstone guides (e.g. "Byta elcentral 2026") | topical authority + best content first, not newest | new (curation only) |
| 4 | Article loop + **category filter chips** (Elcentral, Laddning, Solel/batteri) + pagination when >12 | findability, scent | modified |
| 5 | **MikroCTA or BlueCTA band** — "Frågor om din el? Ring oss" | gives a warmed reader an exit to conversion; today there is none | existing block, newly placed |
| 6 | Prefooter/Footer | | existing |

---

## Test hypotheses (top 3, A/B-phrased)

1. **HYPOTES (grid repair + grouping, /elservice/):** Fixing the dead links and grouping the 22 cards with Eljour/felsökning first will raise hub→service-page click-through from its current (mechanically capped) level and increase downstream form/call conversions per hub session. A: fixed flat grid; B: fixed grouped grid. Primary metric: card CTR + downstream conversion. (The link fix itself ships un-tested — broken ≠ baseline.)
2. **HYPOTES (incentive placement, /laddboxar/):** Moving Grön Teknik 50% from the FAQ into a block directly under the product grid, with a per-card "pris före grönt avdrag"-klargörande, will increase "Läs mer" CTR and offert-form submits vs. the current FAQ-only placement. A: current; B: GrönTeknik block + price clarifier.
3. **HYPOTES (guided selection):** Adding "Osäker vilken som passar? → Laddboxkalkylatorn" as the first tile of the product grid will produce more qualified leads (calculator completions + offert requests) than the pure 16-card grid, per Baymard guided-selling findings. A: grid only; B: grid + calculator entry tile.

---

*Fetch record (anti-theatre): all four URLs curl-fetched live 2026-08-02; raw-HTML verification on data/pages/elservice.html + laddboxar.html snapshots and fresh live pulls of /elservice/, /solcellsbatterier/, /nyheter/ (scratchpad copies). Quoted strings are verbatim from fetched content. block-map.json omissions found: `services-loop` block on /elservice/ and the article loop on /nyheter/ are real but undetected.*
