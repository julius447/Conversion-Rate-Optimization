# FooterSEO block (`footer-seo`)

Used on: **290 of 326 pages** — the single most-deployed content block on the site.
By category (from `data/block-map.json`): elektriker-i 56, elinstallation-i 56, eljour-i 56, laddbox-i 56 (= all 224 programmatic geo pages), service 22, ev-product 16, elektriker-för-X 13, battery-product 10, page 5 (/batterilagring/, /elektriker/, /elinstallation/, /eljour/, /laddbox/).
NOT on: homepage, /om-oss/, /kontakt/, /elservice/ pillar, lead magnets, posts, team-member pages, policy pages.

Funnel position: **always the very last content block** — on every one of the 290 pages the verified sequence ends `… Certificates → FooterSEO → Prefooter`. Absolute position index 14–21 in sequences of 16–23 blocks. This is the terminal, lowest-attention slot on the page.

## Verified structure (live fetches 2026-08-02: /elektriker/åkersberga/, /elservice/badrum/, /eljour/ + snapshot `data/pages/elektriker.html`)

White section: ACF H2 (weight 400, `--aptext-xl`, left-aligned) → one ACF paragraph (weight 300, max-width 50% desktop → 70% @1024 → 80% @780 → 100% @480) → CTA pair (`Kostnadsfri radgivning` primary → **links to https://ampy.se/kontakt/**; `Ring 010-265 79 79` → tel:) → decorative `Vector-2.svg` + a large masked landscape webp (1200×600, `footer-SEO-mask.svg`, absolutely positioned bottom-right, max-width 45% desktop / 85% mobile, lazy + fetchpriority=low). Entire container is `data-interaction-hidden-on-load="1"` with an enterView fadeIn (0.3s, runOnce).

Real copy quoted (anti-theatre):
- /elektriker/ pillar: H2 "Din trygga partner för elservice" + "När du väljer att anlita en elektriker från Ampy får du alltid garanterad kvalitet…" (~45 words)
- /elektriker/akersberga/: H2 **"Åkersberga's tryggaste elektriker nära mig"** + "…får du alltid 30% ROT-avdrag på arbetet…" (~48 words)
- /elservice/badrum/: H2 "Experter på elinstallation i badrum" + "…IP44-installationer för våtrum…" (~44 words)
- /eljour/: H2 "Certifierad expertis för din eljour" + "…snabb inställelse… akut elektriker…" (~50 words)

Mobile behavior: text goes full-width, heading stays left-aligned; the masked image grows to 85% width absolutely positioned bottom-right (decorative filler under/behind the content); CTA block keeps 20px gap. No layout breakage observed in CSS; block simply becomes a tall, mostly-empty white band above the prefooter.

## What it does well
- **Per-page unique copy** (ACF-driven) — it is not one duplicated paragraph across 290 pages, which avoids a pure boilerplate-duplication footprint.
- **A last-chance conversion touchpoint exists at the page floor** — NN/g scroll research supports catching the small cohort of thorough readers who reach the end; the phone CTA (tel:) is the correct zero-friction ask at this depth.
- Correctly performance-behaved: lazy image, low fetchpriority, one small SVG — it is not a speed offender.
- Light white surface after the dark Certificates band gives the page a calm exit — visually appropriate before the cyan prefooter.

## Issues

**FS-1 · P2 · "SEO" value is largely nominal — 40–50 words of generic trust prose at the page floor.** Desktop+mobile identical. The block's name promises SEO substance; the reality is one short paragraph of category-generic language ("garanterad kvalitet", "högsta precision") on pages that already carry 3 000+ words. Evidence: word counts above vs. page `word_count` 3 376 (Dyness product) — the block contributes ~1.5% of page text with no headings targeting distinct queries, no internal links in the text, no structured content. On the 224 geo pages the templated keyword-bolting is visible to a human reader — "Åkersberga's tryggaste elektriker nära mig" writes the search string *into* a headline addressed at a person (Jakob's law violation: nobody speaks like this; it reads as machine text to the 35–65 audience). Given the SEO-audit core diagnosis (doorway-devalvering on the geo corpus), thin templated appendices reinforce, not relieve, the doorway signature. HYPOTES: removing or rewriting this paragraph changes rankings ≈0; its retention value is the CTA band, not the text.

**FS-2 · P1 (quick win) · Primary CTA sends users OFF-page to /kontakt/ instead of anchoring to the on-page form.** Desktop+mobile. All 290 carrier pages have a full MainContact form 4–8 blocks above; the "Kostnadsfri radgivning" click at the page floor triggers a full new page load (site lab LCP ~9–10s per the paid-traffic investigation) to reach a form the visitor just scrolled past. MECLABS friction term: an extra page load is added cost with zero added value; message match also breaks (button promises rådgivning, lands on a generic contact page). An anchor scroll to `#main-contact` (or the Hero_2 form on service/geo pages) converts the same intent with zero load.

**FS-3 · P1 (quick win) · Template-wide typo: "Kostnadsfri radgivning" (missing å) on all 290 pages.** Desktop+mobile, verified live on all three fetched URLs. For a risk-averse Swedish homeowner scanning for competence signals, a misspelled CTA is a small but real trust leak (Cialdini authority works in reverse: sloppiness reads as sloppiness in the fuse box too). Same string also appears in Hero-1 per the block inventory — fix at the button-library level once.

**FS-4 · P2 · Fifth-or-sixth repetition of the identical CTA pair on the same page.** On /elektriker/akersberga/ the visitor has already passed Hero_2 (2 CTAs + form), MainCTA (ring), MainContact (form), MikroCTA (2 CTAs), MapBlock (Kontakta oss), BlueCTA (ring), CEBlock (2 CTAs) before reaching FooterSEO's pair — ≥10 CTA instances per page. Baymard/NN/g: repeated identical asks stop registering (banner blindness for internal elements); the terminal block is the one slot that could justify a *differentiated* final ask (phone-first, human, "still unsure?" framing) rather than the same two buttons a sixth time.

**FS-5 · P3 · Content hidden-on-load behind an enterView JS animation.** `data-interaction-hidden-on-load="1"` on the container: with JS disabled/failed the block never becomes visible (text stays in DOM, so crawl risk is low, but resilience is poor). Mobile note: same behavior.

**FS-6 · P3 · Exposure is minimal and unmeasured.** Position 15–21 of 16–23 blocks, below Certificates (a full-bleed logo wall) and below the page's strongest converter (MainContact). GA4 shows ~17 of 32 paid sessions "deep-scrolled", but no block-level visibility event exists, so actual reach of this block is unknown. HYPOTES: <20% of sessions ever render it; instrument an `enterView` dataLayer event (the interaction trigger already exists) before investing further in this slot.

**FS-7 · P3 · Candour note.** "Åkersberga's tryggaste elektriker" — strong superlatives are owner-allowed (2026-07-18 directive) and "tryggaste" is not demonstrably false, so no candour BLOCK; but the apostrophe-genitive is incorrect Swedish ("Åkersbergas") across the geo template — same class of trust leak as FS-3.

## Recommended changes

1. **Repoint the primary CTA** from /kontakt/ to an on-page anchor (`#main-contact`), smooth-scroll. One template edit, 290 pages. (FS-2)
2. **Fix the button-library string** "radgivning" → "rådgivning" (also fixes Hero-1) and the geo-template genitive "{Ort}'s" → "{Ort}s". (FS-3, FS-7)
3. **Reframe the block as the "last-chance close", not an SEO appendix.** Keep the ACF paragraph in DOM (SEO substance preserved — re-package, never delete) but change the copy pattern: H2 answers the exit-state JTBD ("Fortfarande osäker? Prata med en elektriker först — det kostar inget") instead of restating the page keyword; paragraph carries ONE concrete proof (Elsäkerhetsverket-registrering / written offert per Konsumentverket advice — the two things Byggahus-Swedes actually check) instead of generic "garanterad kvalitet". Phone CTA stays primary at this depth (thorough readers at page floor skew high-intent; tel: is the lowest-friction close).
4. **Merge with the prefooter — yes, structurally sound as the P2 move.** Certificates → FooterSEO → Prefooter is a three-band low-engagement stack ending every page. Fold the reframed H2 + paragraph + CTA pair into the top of the Prefooter section (above "Populära kategorier") as one compact band: one fewer full-height section, the SEO text survives in DOM, the link columns gain a reason-to-act header, and the page exit shortens by ~one viewport on mobile. Ship as one template change; the standalone FooterSEO section is then retired.
5. **Instrument first:** add the free `enterView` → dataLayer visibility event before/while testing, so the merge can be judged on real reach + click-through data. (FS-6)

Test hypothesis (A/B, template-level on geo pages): "Changing FooterSEO's primary CTA from /kontakt/ link to #main-contact anchor increases form submits per session on programmatic geo pages, because it removes a ~9s page load between final intent and the form."

## Priority score (arithmetic shown)

Pages affected = **290**. Funnel position weight = **1** (low-page/terminal slot). Expected effect = **2** (medium: quick-win CTA/typo fixes are cheap and site-wide, but the slot's low exposure caps upside).

**Priority score = 290 × 1 × 2 = 580.**

Overall **P2** (the block redesign/merge), carrying two embedded **P1 quick wins** (FS-2 CTA repoint, FS-3 typo) that are one-template-edit fixes with 290-page reach and should ship in month 1.
