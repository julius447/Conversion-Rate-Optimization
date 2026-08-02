# TeamSection (`team`) + Team-member page (E-E-A-T profile)

**Used on:** TeamSection appears on **85 of 326 pages** (verified in `data/block-map.json`): 56 × elektriker-i geo pages, 16 × ev-product, 10 × battery-product, 3 × pillar pages (/elektriker/, /laddbox/, /batterilagring/). The 6 team-member profile pages (/om-oss/edvin-gustavsson/ etc.) are a separate template — **91 pages total** in this audit's scope.
**Funnel position(s):** Low-page trust proof. TeamSection sits at block index 10–14 on every carrier (16 pages @10, 10 @11, 1 @12, 57 @13, 1 @14), i.e. **60–69% down the page (avg 64%)** — always after MikroCTA or ProductGrid, always before MapBlock or VissteDuAtt, and **always AFTER the MainContact form** (MainContact sits at index 7–8 on elektriker-i pages, TeamSection at 13). Team-member pages are standalone (Header → AlternativHero → stacked cards → FAQ → Prefooter): no funnel position at all — they are orphans.

## Verified live structure (fetched 2026-08-02)

**TeamSection on https://ampy.se/elektriker/** — H2 `"Möt våra auktoriserade elektriker"` on the white floating card, then a Splide slider of 5 cards (Mio, Magnus, Felix, Edvin, Yousef). Each card = portrait photo (`team__image`, e.g. `Mio-1.webp` with alt "Porträtt av Mio, ECY-certifierad elektriker…") → `<h3 class="team__acf_member_name">Mio</h3>` (first name only) → one dense bio paragraph (~90–100 words), e.g.: *"Mio är en ECY-certifierad elektriker med 4 års erfarenhet av komplexa batterilösningar och smart laddinfrastruktur. Som specialist på hemmabatterier och funktioner som stödtjänster och ö-drift…"*. Verified Splide config: `"perPage":3, "autoplay":true, "interval":3000, "arrows":false, "pagination":true`, breakpoints `1024 → perPage 2`, `480 → perPage 1`.

**Team-member page https://ampy.se/om-oss/edvin-gustavsson/** — dark AlternativHero (name + "Senior Elektriker, Arbetsledare & Kvalitetsansvarig" + preloaded portrait) → Nyckelfakta (mint card) → About → Expertis & systemkompetens (incl. "KNX-system", "Plejd, Shelly") → Erfarenhet → **Certifieringar** ("Auktoriserad elektriker (full behörighet)", "ECY-certifierad elektriker (Elbranschens Centrala Yrkesnämnd)") → Arbetssätt → quote *"En bra installation handlar inte bara om att det fungerar idag, utan att det är byggt rätt för framtiden."* → FAQ "Vanliga frågor om Edvin". Page carries `@type: Person` schema and the org AggregateRating (5.0, reviewCount 25). **Zero `<form>` elements, zero body phone CTAs** (the only 2 `tel:` links are header + footer chrome).

## What it does well
- **The right asset for this demographic exists.** Real portraits, real Swedish names, real certifications (ECY, Bas P/U, full auktorisation), specific years of experience — exactly the authority proof (Cialdini) a risk-averse 35–65 homeowner and the Byggahus-style "is this firm serious?" checker responds to. The Clarity paid-session recording (47s visitor navigating Contact → **About Us**) is direct behavioral evidence this audience seeks people-proof before converting.
- Photo alt-texts are descriptive and E-E-A-T-loaded ("Porträtt av Mio, ECY-certifierad elektriker specialiserad på SAJ HS3…").
- The member pages are genuinely deep, candour-consistent E-E-A-T documents (Person schema, named certification bodies, real work descriptions, honest scoping like "Även om hans primära fokus ligger på ledning…") — rare in the elfirma category and a real differentiator vs. competitor sites with stock photos.
- The H2 "Möt våra auktoriserade elektriker" is a strong, verifiable authority claim ("auktoriserade" is checkable at Elsäkerhetsverket).

## Issues

**TB-01 — P1 — The E-E-A-T pipes are disconnected: cards never link to the profile pages, and the profile pages have ZERO inbound links.**
Desktop + mobile: the only `<a>` elements inside the TeamSection are mid-bio links to *product/service* pages (batterilagring, SAJ HS3, Dyness Stack100, elcentral…) — verified by extracting every href in the section; **none point to /om-oss/{name}/**. A grep across all 37 HTML snapshots (home, om-oss, elektriker, all product pages, kontakt…) found the member URLs referenced **only by their own self-canonical tags**. Six built, expensive E-E-A-T pages are complete orphans: no crawl equity, no user path, no link-through value. Evidence: NN/g — users don't perceive non-clickable content as "more exists"; internal-linking basics; the site's own article byline pattern (block 19) implies these pages were built to be linked.

**TB-02 — P1 — Trust proof placed after the ask (inverted proof architecture).**
On all 56 elektriker-i pages the order is MainContact form @7–8 → ROT @11 → MikroCTA @12 → **TeamSection @13**. The faces that reduce anxiety about "who shows up at my door" render ~5 blocks *below* the primary form. MECLABS heuristic: anxiety (a) must be corrected at or before the point of ask; here the a-reducer arrives after it. This block-level finding matches the site-audit P0 "inverterad proof-arkitektur". Mobile note: at avg 64% page depth on pages that are 16–23 blocks long, GA4 shows ~17 of 32 paid sessions deep-scrolled — roughly half of paid visitors plausibly never see the team at all (HYPOTES — needs scroll-map confirmation per template).

**TB-03 — P1 — Auto-rotating carousel fights the reader; on mobile it hides 4 of 5 electricians.**
Verified config: autoplay every **3000ms**, `arrows:false`, mobile breakpoint 480 → `perPage:1`. Each bio is ~90–100 words (~25–30s reading time at normal Swedish reading speed) but the card is yanked away after 3s. NN/g carousel research: auto-forwarding carousels are routinely ignored or cause "banner blindness"; accessibility guidance (WCAG 2.2.2) expects moving content >5s to be pausable — pauseOnHover exists but there is no hover on touch devices, so **on mobile (the primary rendering) the block is an unreadable 1-up slideshow**. Pagination dots without arrows give poor affordance for 35–65-year-olds (Fitts/affordance).

**TB-04 — P2 — Card information hierarchy is name-only; the credentials are buried in paragraph prose.**
The card's only structured data is `<h3>Mio</h3>` (first name, 26px). No surname, no job-title line, no years-of-experience marker, no certification badge — everything a scanning homeowner needs is trapped inside a 100-word paragraph, partly in installer jargon ("stödtjänster och ö-drift", "Bas P/U", "ledandemontör") that means nothing to the target customer. NN/g F-pattern/scanability: users read headings + first lines; Baymard: scannable fact fragments beat prose for evaluation tasks. The member page *has* the structured version (title line + Nyckelfakta + Certifieringar) — the card just doesn't surface it.

**TB-05 — P2 — No certification badges on cards; the site's strongest checkable proof stays textual.**
"ECY-certifierad", "Bas P/U", "full auktorisation" appear only as words inside bios. No visual chip/badge, no link to what ECY means, and no card-level tie to the Elsäkerhetsverket registry — the exact verification a serious Swedish customer performs (Konsumentverket/Byggahus research anchor in business context). Cialdini authority works through *symbols* as well as claims. The Certificates logo-wall block exists elsewhere on the same pages but is never connected to the people.

**TB-06 — P1 — /om-oss/ — the page trust-seekers actually visit — has NO TeamSection.**
Verified from block-map + snapshot: /om-oss/ = Hero-1 → ContentBlock → AboutMetrics → Metrics → VisualCTA → MainContact → Prefooter. `team__` classes: absent. The Clarity recording shows a paid visitor going Contact → About Us; the About page answers with metrics and a photo CTA but **zero faces, zero names**. Jakob's law: users expect an About page to show the people. This is the single cheapest placement win in the whole team system.

**TB-07 — P2 — Team-member pages are conversion dead ends.**
No MainContact, no body `tel:` CTA, no "Boka rådgivning" — a visitor convinced by Edvin's profile has only header/footer chrome to act on. Both conversions (call/form) are effectively absent from the template. Must be fixed *before* TB-01 sends traffic here, otherwise we link into a cul-de-sac. Mobile note: the long stacked cards make the distance from bio to any CTA several full viewports.

**TB-08 — P3 — Bio links leak attention out of the trust moment.**
Mid-bio hrefs route to product pages (SAJ HS3, Dyness Stack100) — the block moonlights as an internal-linking vehicle. Fine for SEO, but the only clickable affordances in a *people* block lead to *products*, not people (message mismatch within the block).

**TB-09 — P3 — Roster inconsistency.** Slider shows 5 electricians; 6 profile pages exist (Julius Callahan has a page but no card). Harmless today, confusing once TB-01 wiring lands.

**TB-C (candour note)** — bios use "garanterar" twice on safety outcomes ("garanterar han trygga elmiljöer"). Strong superlatives are owner-allowed, but a safety *guarantee* is a legal-adjacent promise — flag for owner/ampy-rost review, not a unilateral rewrite. Positive: nothing in the block asserts unanchored "1000+ kunder"; the schema's 5.0 is anchored with reviewCount 25.

## Recommended changes (concrete)

1. **Re-sequence (TB-02):** on elektriker-i and service templates, move TeamSection to sit immediately **before** MainContact (proof → ask), e.g. …Testimonials → VarProcess → **TeamSection** → MainContact → FAQ…. SEO substance untouched — pure re-ordering.
2. **Rebuild the card (TB-04/TB-05):** photo → **Full name** → title line ("Senior serviceelektriker") → fact chips (⚡ 17 års erfarenhet · ECY-certifierad · Auktoriserad) → 2-sentence plain-Swedish bio (compress current prose; keep full text on profile page) → **"Läs mer om Magnus →"** link. Copy-pattern direction: chips carry the checkable nouns, the bio carries warmth ("Magnus har bytt fler elcentraler än han kan räkna" register — final words via ampy-rost).
3. **Wire the link-through (TB-01):** card CTA → /om-oss/{name}/; add a "Vårt team" card grid or link block on /om-oss/; link article bylines (block 19 avatars) to profiles. This alone converts 6 orphan pages into an E-E-A-T mesh feeding Person schema authority back to service pages.
4. **Kill autoplay (TB-03):** desktop = static 3-up grid (5 members fit in 2 rows or a manual slider with arrows); mobile = swipeable 1-up with visible arrows + ~15% next-card peek, `autoplay:false`. No content should move while a 60-year-old reads it.
5. **Add TeamSection to /om-oss/ (TB-06)** between AboutMetrics and MainContact — the highest-intent trust page finally gets faces.
6. **Close the member-page loop (TB-07):** append MainCTA (ring-only) + MainContact to the team-member template, with prefilled context ("Vill du att Edvin kvalitetssäkrar ditt jobb?" — copy direction only), plus "Fler i teamet" cross-links.
7. **Owner review (TB-C, TB-09):** "garanterar" phrasing; add or intentionally exclude Julius from the slider.

## Test hypotheses (A/B)
- HYPOTES: Moving TeamSection above MainContact on elektriker-i pages increases form submits vs. current order (MECLABS a-reduction before ask).
- HYPOTES: Cards with title + cert chips + "Läs mer" outperform name-only autoplay cards on engagement (card clicks, downstream form rate).
- HYPOTES: Adding TeamSection to /om-oss/ lifts About-page → kontakt/form continuation rate for trust-seeking sessions (Clarity pattern).

## Priority score (arithmetic)
- Pages affected: **91** (85 TeamSection carriers + 6 team-member pages; the /om-oss/ addition is a new placement, not counted).
- Funnel position weight: **2** (mid — the block's job is trust proof feeding the form decision; it is currently low-page, which is itself the defect).
- Expected effect: **2** (medium — trust-mechanism hypothesis with direct behavioral signal from Clarity, but no direct conversion data yet).
- **Priority score = 91 × 2 × 2 = 364 → P1** (fix in month 1; TB-06 om-oss placement and autoplay kill are week-1-cheap).
