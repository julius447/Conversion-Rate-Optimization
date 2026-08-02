# Homepage (ampy.se/)

URLs analyzed: https://ampy.se/ (live fetch 2026-08-02) + raw snapshot `data/pages/home.html` (723 kB, word_count 1 416). | Pages using this template: **1** (unique template; but it is the highest-traffic single URL and the brand's front door — priority weight treats it as hero-position on the whole funnel).

**Block-map correction (verified against snapshot byte-positions):** the block-map entry omits three blocks that exist on the live page. The true sequence is Header > **Hero-1** > MiniMenu-Elfirma > ProductGrid(batteries) > BlueCTA > ProductGrid(laddboxar) > Testimonials > **ServiceGrid ("Vårt utbud av elinstallationer")** > MainCTA > VarProcess > MainContact > MapBlock > **News** > Prefooter. Positions confirmed in `home.html`: `hero-1` @6018, `ampy-elfirma` @443971, "Våra hembatterier" @458339, "Prata med en elektriker!" @470823, "Zaptec Go" @474211, "Vad säger dina grannar" @484991, "Vårt utbud av elinstallationer" @533367, "inom 60 sekunder" @544535, "Så funkar det" @558314, "Vi finns där du finns" @664727, "Nyheter och artiklar" @670705.

---

## Current block sequence (verified)

1. **Header** — mega-menus Tjänster/Produkter/Lösningar + "Gratis rådgivning" teal CTA (→ `/kontakt/`) + mobile offcanvas with "Ring en expert" (tel:) + "5.0". *Mobile: offcanvas accordion; CTA + rating persistent.*
2. **Hero-1** — H1 "Elinstallationer i hemmet, gjort ordentligt." → sub "Våra egna behöriga elektriker hjälper dig i hela Sverige, med allt från elfel och elcentraler till laddbox och batterilagring." → CTA "Kostnadsfri rådgivning" (**href = `/kontakt/`**, verified) → trust row "5.0 på Google · Över 3 000 installationer per år". *Mobile: stacked, masked image absolute bottom.*
3. **MiniMenu-Elfirma** — H2 "Din elektriker för hela hemmet" + "Med över 3000 installationer per år…" → 3 photo cards: Elservice → `/elservice/`, Laddbox → `/laddboxar/`, Batterilagring → `/batterilagring/`, each with generic "Läs mer" pill. *Mobile: cards stack vertically.*
4. **ProductGrid, part 1 (BATTERIES)** — H2 "Våra hembatterier och laddboxar – installerat & klart med 50 % Grön Teknik-avdrag" → 4 battery cards with commerce tags (BÄSTSÄLJARE / SUPERKAMPANJ), phase/kWh chips, prices **"Fr. 34 900 kr" / "Fr. 33 000 kr" / "Fr. 36 250 kr" / "Fr. 34 900 kr"**, each "Läs mer" → `/solcellsbatterier/{dyness-stack100|eway|enershare|saj-hs3}/`. *Mobile: 4 full-width cards ≈ 4 viewport-heights.*
5. **BlueCTA** — H2 "Prata med en elektriker!" + "Vi finns här för dig och ditt hem…" → single black "Ring 010-265 79 79" button. Sits BETWEEN battery and laddbox halves of the grid. *Mobile: full-width band.*
6. **ProductGrid, part 2 (LADDBOXAR)** — 4 laddbox cards (Zaptec Go "Fr. 4 490 kr", Zaptec Go 2 "Fr. 5 890 kr", Easee Charge Up "Fr. 4 390 kr", NexBlue Edge 2 "Fr. 4 190 kr") → `/laddboxar/{slug}/`. *Mobile: 4 more viewport-heights.*
7. **Testimonials** — "Vad säger dina grannar om Ampy?" / "Riktiga omdömen från riktiga jobb." → Splide slider, 12 real Google reviews with names + months (e.g. Jan Fernström juni 2026: "…både kunnigare och billigare…") → badge "5 av 5 · Betyg på Google" (no review count). *Mobile: 1-up slider.*
8. **ServiceGrid** — H2 "Vårt utbud av elinstallationer – installerat & klart med 30 % ROT-avdrag" → 6 service cards (Belysning, Elcentral, Köksrenovering, Luftvärmepump, Smarta hem, Spotlights) with descriptive links "Till Belysning" → `/elservice/belysning/` etc. → "Ladda fler tjänster" (`href="#"`, JS load-more). *Mobile: stacked cards.*
9. **MainCTA** — trust row + H2 "Prata med en elektriker inom 60 sekunder!" + "Känn dig trygg med kunnig hjälp…" → Ring-only CTA + "5.0 på Google". *Mobile: centered stack.*
10. **VarProcess** — "Så funkar det" + "Ampy's steg-för-steg-lista…" → 4 steps (Samtal med elektriker → Offert & tidsförslag → Bokning bekräftad → Installation utförd). Contains live typos (see HP-06). *Mobile: steps stack.*
11. **MainContact** — left proof pane (quote, "5 av 5 · Betyg på Google", "3 000+ genomförda installationer om året", 3-step promise incl. "Vi ringer dig inom 24 timmar") + right form: Förnamn / Efternamn / E-post / Telefonnummer / Adress (gatuadress) / Postnummer / Postort / Meddelande → "Gratis rådgivning" submit → n8n → /thank-you. **8 visible fields.** *Mobile: proof pane above form → form starts ~1 viewport down.*
12. **MapBlock** — "Vi finns där du finns" + "…lokala elfirma som sträcker sig över hela Sverige" → 20 ort buttons, all Stockholm-region (Sickla, Sköndal, Sundbyberg, … Södertälje, Sigtuna) → "Osäker ifall vi finns där du bor?" + Kontakta oss → `/kontakt/`. *Mobile: dot-map variant.*
13. **News** — "Nyheter och artiklar!" → 3 article cards (all elcentral/laddbox-technical, juni 2026) → "Läs artikel". *Mobile: stacked.*
14. **Prefooter + Footer** — Populära kategorier link columns; footer with "5.0", address, tel. 4 `tel:` links on the page total.

---

## Customer-flow walkthrough (35–65 y/o Swedish homeowner, mobile-first)

**0–5 seconds:** Strong. H1 "Elinstallationer i hemmet, gjort ordentligt." is service-first, plain-spoken, exactly the candour register — a taklampa/elcentral/elfel visitor feels addressed. Trust row (5.0 + 3 000 installationer) supports it. One clear CTA. This above-the-fold is the best-matched screen on the page for the actual query mix ("installera taklampa", "byta elcentral pris", "elfel i huset").

**First scroll (screens 2–3):** MiniMenu offers a 3-way fork — but only one of the three (Elservice) matches the majority intent, and its card is visually co-equal with two product categories. Acceptable.

**Screens 3–8 — the leak:** The visitor now enters ~8 viewport-heights (mobile) of **webshop**: four batteries at 33 000–36 250 kr, a phone band, four laddboxar. Jakob's law: the card grammar (BÄSTSÄLJARE tag, spec chips, "Fr."-price, Läs mer) is e-commerce grammar; it silently reframes Ampy from "elektriker som hjälper dig" to "butik som säljer dyra energiprodukter". The **first prices the visitor ever sees are 33 000–36 250 kr** — a brutal price anchor for someone whose job is a ~3 500 kr service call (MECLABS *a*, anxiety: "this firm is for solar people, not for my proppskåp"). Eight "Läs mer" exits leave the homepage before any proof has been shown.

**Screens 8–10:** Testimonials finally deliver trust — 12 real, named, dated reviews; genuinely strong. Then, at last, the ServiceGrid: the content the majority visitor came for (Belysning, Elcentral, Kök…) sits at position 8, below two product grids it should out-rank per the owner's own priority (service > laddbox > battery — **currently rendered in exactly inverted order**).

**Decision point:** MainCTA (phone) → VarProcess (very good anxiety-reducer: transparent offert, ROT handled for you) → MainContact form (strongest asset, but 8 visible fields, and on mobile the proof pane pushes the first field a full viewport down). The Clarity "Contact → About Us" recording suggests this visitor wanted more proof than the page gave before the ask — and Certificates/Team, the site's institutional-proof blocks (Elsäkerhetsverket!), are **absent from the homepage entirely**.

---

## What works (keep)

- **H1 + hero copy** — "Elinstallationer i hemmet, gjort ordentligt." is the right promise in the right voice; single H1, clean heading tree.
- **Testimonials block** — 12 real, named, dated Google reviews; the strongest social proof on the site (Cialdini, candour-clean at the review level).
- **VarProcess** — directly answers the top Byggahus/Reddit anxieties (fixed vs estimated offert, "what happens after I call", ROT paperwork handled). Keep, fix typos.
- **MainContact** — best conversion asset; proof-pane + form pattern is right, only friction tuning needed.
- **BlueCTA / MainCTA phone-first bands** — right conversion type for this audience; placement and earned-ness are the issue, not the blocks.
- **ServiceGrid links are descriptive** ("Till Belysning") — better link copy than the products' generic "Läs mer" (NN/g).
- **Header mega-menu IA** — comprehensive routing incl. kalkylator links.

---

## Findings

**HP-01 · P0 · Commercial-priority inversion + hostile price anchor.** The first commercial content after the hero is 4 batteries (priority #3, OFF Google Ads) at "Fr. 33 000–36 250 kr"; laddbox (#2) second; services (#1) at position 8 below testimonials. The majority visitor's job costs ~3 500 kr, and the page's first price signal is 10× that. Evidence: MECLABS heuristic (anxiety *a* + incentive mismatch), anchoring bias, JTBD (search-term reality: "installera taklampa", "byta elcentral pris", "elfel i huset"), owner-confirmed priority service > laddbox > battery. *Mobile: ~8 viewport-heights of product cards between hero and the first service link.* Priority: 1 page × 3 (hero-adjacent) × 3 (high effect) = **9**.

**HP-02 · P0 · ProductGrid leaks visitors pre-proof.** 8 outbound "Läs mer" product links sit ABOVE the testimonials and above every trust block, so the highest-attention scroll zone exports traffic before trust is established. The owner's suspicion is **confirmed**. Evidence: 0 confirmed form leads despite ~17 deep-scrolled paid sessions site-wide; NN/g — every link is a decision point and an exit. *Mobile: exits occupy the prime thumb zone.* Priority: 1 × 3 × 3 = **9**.

**HP-03 · P1 · Hero CTA navigates away instead of anchoring.** "Kostnadsfri rådgivning" → `/kontakt/` (verified href) although MainContact — the same form — exists on-page. That is a full extra page-load at ~9–10 s lab LCP for the single highest-intent click on the page. Evidence: NN/g interaction cost; site speed flag from the specialist investigation. *Mobile: worst-case — slow reload where a 0-cost scroll-to-anchor existed.* Priority: 1 × 3 × 3 = **9**.

**HP-04 · P1 · Unanchored ratings & scale claims (candour gate).** "5.0 på Google" appears bare in hero, MainCTA, header, footer; testimonials badge says "5 av 5 · Betyg på Google" with **no review count**; "Över 3 000 installationer per år" / "3 000+ genomförda…" appears 3× unanchored. Candour gate: rating must carry count + source link, and 3 000+ must be owner-verified current, or these lines come out. Evidence: Cialdini — social proof persuades only when verifiable; Konsumentverket-minded Swedes check. *Mobile: identical.* Priority: 1 × 3 × 2 = **6** (site-wide fix scores far higher in the block audit).

**HP-05 · P1 · MainContact shows 8 fields for a callback ask.** Förnamn/Efternamn/E-post/Telefon/Adress/Postnummer/Postort/Meddelande all visible. Minimum viable for "vi ringer dig inom 24 timmar" is namn + telefon (+ postnr for routing); everything else can be progressive disclosure or collected on the call. Evidence: Baymard — *visible/required field count drives perceived difficulty more than steps*; GA4 shows 0 form starts recorded (instrumentation AND friction both suspect). *Mobile: proof pane pushes field 1 a viewport down; 8 fields ≈ 2+ screens of typing.* Priority: 1 × 3 × 3 = **9** (block-level fix affects every page using MainContact).

**HP-06 · P2 · Live typos in the trust-critical process block.** VarProcess step 2: "Vi går **vi** igenom dina behov…"; step 3: "Vi skickar **vi** ut en bekräftelse…"; plus anglicism "Ampy's" (Swedish: "Ampys"). For a 35–65 audience, sloppy text is a workmanship proxy — precisely in the block whose job is to signal precision. Evidence: credibility heuristics (Stanford web credibility / NN/g trust research tradition). *Mobile: identical.* Priority: 1 × 2 × 2 = **4** (VarProcess is multi-page: score rises in block audit).

**HP-07 · P2 · Meta description mismatches page & audience.** "Smart batterilagring och rikstäckande elservice. Vi förenar **AI-lösningar** med fackmannamässig precision…" — battery-first ordering (inverts priority again) and "AI-lösningar" is founder-taste jargon that repels the 35–65 homeowner. H1 is service-first; the SERP snippet is battery/AI-first → message-match break before the visit even starts (Google message-match doctrine). Priority: 1 × 2 × 2 = **4**.

**HP-08 · P2 · Three conflicting response-time promises on one page.** MainCTA: "Prata med en elektriker inom 60 sekunder!"; MainContact pane: "Vi ringer dig inom 24 timmar"; VarProcess: "vår seniora elektriker ringer upp dig". If the 60-second claim is not operationally guaranteed it is a candour-gate violation; even if true, the 60 s/24 h collision reads as inconsistency. Evidence: candour gate; message consistency (MECLABS *v* clarity). Priority: 1 × 2 × 2 = **4**. **[OWNER-VERIFY: is 60 seconds real call-answer SLA?]**

**HP-09 · P2 · "Hela Sverige" copy vs all-Stockholm ort grid.** MapBlock text says "…sträcker sig över hela Sverige", yet all 20 buttons are Stockholm-region orter. Copy is owner-permitted; the *presentation* undermines it — a Göteborg visitor concludes "not my area" and the sub-card even invites doubt ("Osäker ifall vi finns där du bor?"). Fix presentation (regional grouping or explicit "+ fler orter i hela Sverige"), not the claim. Evidence: message consistency; NN/g scanning — users read the grid, not the paragraph. Priority: 1 × 1 × 2 = **2**.

**HP-10 · P2 · Institutional proof absent from the homepage.** Certificates (Elsäkerhetsverket, Skatteverket, Trygg Hansa…), Team, and Metrics blocks exist in the library but none render on the homepage — the one page every trust-seeking visitor touches. The Clarity "Contact → About Us" path is direct behavioral evidence of unmet proof demand. Elsäkerhetsverket registration is *the* check Konsumentverket-literate Swedes perform. Evidence: Cialdini authority; Swedish homeowner research anchors in business context. Priority: 1 × 2 × 3 = **6**.

**HP-11 · P3 · Generic "Läs mer" ×11 + `href="#"` load-more.** Products and mini-menu use non-descriptive "Läs mer" (NN/g descriptive-link doctrine); "Ladda fler tjänster" is `href="#"` JS — verify hidden services remain in DOM for SEO (doctrine: accordion/load-more OK only if content stays in DOM). Priority: 1 × 1 × 1 = **1**.

**HP-12 · P3 · Weight/speed.** 723 kB HTML, ~9–10 s lab LCP flag; the 8-card ProductGrid (images, tags, chips) is a major contributor in the pre-fold-adjacent zone. Re-sequencing (HP-01/02 fix) is also a speed fix. Priority: 1 × 1 × 2 = **2** (compounds with every other finding — slow LCP suppresses everything).

**HP-13 · P2 · Split intent-routers.** Two service routers (MiniMenu, 3 cards; ServiceGrid, 6 cards) are separated by ~5 viewport-heights of products, forcing the "elcentral" scanner to traverse the entire shop to find their route. One consolidated router directly after the hero removes the traverse. Evidence: information scent (NN/g), Hick's law (one decision surface beats two staggered ones). Priority: 1 × 3 × 2 = **6**.

---

## Verdict on the owner's instinct

**Directionally right, and the core call — ProductGrid out of the mid-funnel — is confirmed** (HP-01/HP-02 are the page's two P0s). Two pushbacks on his floated sequence (Hero-1 > MiniMenu > Testimonials > MainCTA > VarProcess > MainContact > Map > News):

1. **It deletes the ServiceGrid, which is the wrong casualty.** The service router is the homepage's #1-priority content and its main internal-linking hub into /elservice/* (SEO doctrine: re-sequence, never delete). It should move UP (merged with MiniMenu into one router), not disappear.
2. **It removes all product presence, over-rotating.** Laddbox is commercial priority #2 and homepage is the shop window; a compact 2-card category teaser (Laddbox first, Batterilagring second, "fr."-pris + 50 % grön teknik line) below the conversion layer preserves discovery and the Grön Teknik hook without the e-commerce takeover — the full grids already live on /laddboxar/ and /batterilagring/ where purchase-intent visitors go.
3. Minor: MainCTA (hard phone ask) lands better AFTER VarProcess has answered "vad händer när jag ringer?" — swap them.

---

## Recommended sequence (primary wireframe)

| # | Block | Why here | New/existing/modified |
|---|-------|----------|----------------------|
| 1 | Header | unchanged | existing |
| 2 | **Hero-1** | keep H1/copy; CTA → anchor `#radgivning` (on-page form) not `/kontakt/`; anchor the rating ("5,0 · N recensioner på Google", linked) | modified (HP-03, HP-04) |
| 3 | **ServiceRouter** (MiniMenu + ServiceGrid merged) | one decision surface right after hero: row 1 = services (Felsökning/Eljour, Elcentral, Belysning, Kök & Badrum, Smarta hem, +fler → /elservice/); row 2 = 2 slim category cards Laddbox · Batterilagring; keeps "30 % ROT" headline value and all /elservice/* internal links | modified/merged (HP-01, HP-13) |
| 4 | **Testimonials** | trust immediately after routing, before any hard ask (Clarity trust-seeking evidence); add review count to badge | existing, badge modified (HP-04) |
| 5 | **VarProcess** | answers "vad händer om jag hör av mig?" BEFORE the phone ask; fix typos | existing, copy-fixed (HP-06) |
| 6 | **MainCTA** | phone ask now earned by proof + process; reconcile response-time promise (HP-08) | existing, copy-verified |
| 7 | **ProductTeaser** | compact 2 cards — Laddbox ("fr. 4 190 kr, 50 % Grön Teknik") before Batterilagring ("fr. 33 000 kr") → pillar pages; preserves priority order and Grön Teknik hook without webshop takeover | **new** (replaces 8-card ProductGrid + BlueCTA) |
| 8 | **Certificates** | institutional proof (Elsäkerhetsverket, Trygg Hansa…) directly above the form = last-anxiety kill before the ask | existing block, new to homepage (HP-10) |
| 9 | **MainContact** (`#radgivning`) | the close; trim visible fields to Namn/Telefon/Postnr + "Fler detaljer (valfritt)" disclosure | modified (HP-05) |
| 10 | **MapBlock** | local reassurance post-form; regroup orter or add "+ fler orter i hela Sverige" | modified (HP-09) |
| 11 | **News** | freshness + internal links, correct low position | existing |
| 12 | Prefooter/Footer | unchanged | existing |

Net effect: nothing deleted — ProductGrid content relocates to its pillar pages (where it already exists verbatim), ServiceGrid content merges upward, all internal links preserved or strengthened. Page sheds ~8 heavy product cards from the mid-funnel (HP-12 speed win).

## Divergent alternative (house rule)

**"Jobb-först" homepage** — for the thesis that the homepage's main job is conversion, not routing. Hero-1 gains a **job-picker** (chips: "Elfel / felsökning", "Byta elcentral", "Belysning", "Laddbox", "Batterilagring", "Annat") that either deep-links to the matching service page or pre-fills an inline 3-field mini-form (namn/telefon/valt jobb) directly in the hero — the eljour-symptom-block pattern generalized. Sequence: 1 Header · 2 Hero-1+JobPicker · 3 VarProcess · 4 Testimonials · 5 **MainContact (position 5 — form in the first half of the page)** · 6 ServiceRouter (SEO/routing layer now BELOW the conversion layer) · 7 ProductTeaser · 8 Certificates · 9 MainCTA (phone, for scroll-past-form visitors) · 10 Map · 11 News · 12 Footer. Trade-off: maximizes lead capture from decided visitors, risks under-serving researchers; higher build effort (job-picker is a new component). Test candidate rather than default.

---

## Test hypotheses (top 3, A/B)

1. **HYPOTES (sequence):** Replacing ProductGrid+BlueCTA (positions 4–6) with the merged ServiceRouter + compact ProductTeaser increases homepage → (tel-click + form_start) rate, without reducing sessions into /laddboxar/* by more than 20 %. Metric: GA4 tel clicks + form_start (must first be instrumented), pillar-page entrances. Basis: MECLABS anxiety/anchor removal + information scent.
2. **HYPOTES (CTA cost):** Hero CTA as scroll-to-anchor `#radgivning` beats navigation to `/kontakt/` on completed form submissions per hero-CTA click. Basis: NN/g interaction cost + ~9–10 s LCP penalty on the extra load.
3. **HYPOTES (proof anchoring):** "5,0 av 5 · N recensioner på Google" (linked, owner-confirmed N) in hero + MainCTA beats bare "5.0 på Google" on form starts. Basis: Cialdini — verifiable proof outperforms asserted proof; candour gate requires the fix regardless of test outcome.

*(Secondary bench: 3-field vs 8-field MainContact per Baymard — belongs to the MainContact block audit since it affects every page carrying the form.)*
