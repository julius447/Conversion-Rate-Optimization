# Pillar pages — /elektriker/, /eljour/, /elinstallation/, /laddbox/, /batterilagring/

URLs analyzed (all five fetched live 2026-08-02; batterilagring + elektriker + eljour additionally rendered in browser, desktop 1280px and mobile 375px):
https://ampy.se/elektriker/ · https://ampy.se/eljour/ · https://ampy.se/elinstallation/ · https://ampy.se/laddbox/ · https://ampy.se/batterilagring/
Comparison children fetched: /elektriker/akersberga/, /eljour/akersberga/ (+ block-map sequences for /elinstallation/akersberga/, /laddbox/akersberga/).

**Pages using this template: 5** (the SEO/Lösningar powerhouses). Template-level decisions here also cascade by example into **224 geo children** (4 × 56 per block-map) that sit directly beneath these pillars, and the shared blocks audited here (CTA library button, Metrics, MainCTA, VarProcess) render on most of the site's ~326 pages.

**Anti-theatre note / verified state:** the block-map is stale in two places, verified against live HTML:
1. `/eljour/` now carries the **Eljour symptom block** ("Är något fel med elen? Tryck på det du upplever." — 15 symptom cards, Akut/Varning tiers, Elsäkerhetsverket ~1 800-bränder stat) immediately after the hero. It is NOT in block-map.json.
2. `/elinstallation/` carries a **legacy contact-form block** ("Få en kostnadsfri konsultation! Alltid fasta priser och professionell service" → "Få ditt förslag") plus a ServiceGrid ("Vårt utbud av elinstallationer") — neither in its block-map entry, which also lacks MainContact.
3. The **batterilagring Hero_2 is FIXED**: the site-audit-2026-07 P0 ("trasig batterilagring-hero") no longer reproduces. The `.aof` form is JS-rendered into `#ampy-form-root` (posts to a Supabase edge function `hero-lead`) and renders correctly on desktop AND mobile — verified by screenshot: "Få kostnadsfri rådgivning!", Privat/BRF/Företag toggle, "Vad gäller arbetet?" prefilled **Batterilagring**, Namn, Telefonnummer/E-post, Adress/Postnummer, "Fler detaljer (valfritt)", GDPR. Because the form is client-rendered, it is invisible to no-JS crawls — worth a render-state check in the SEO lane, but conversion-wise it works.

---

## Current block sequence (verified live, per pillar)

### /elektriker/ (H1: "Elektriker för privatpersoner över hela Sverige!", 2 525 words)
1. **Hero-1** — white floating card, H1 + "Upptäck marknadens billigaste priser, trygga installationer…" + CTA pair ("Kostnadsfri **radgivning**" [sic, missing å] green / "Ring 010-265 79 79" blue) + Google 5.0 ★ row + house photo. *Mobile: stacked, both CTAs full-width, image below trust row; clean.*
2. **Metrics** — "1000+ Nöjda kunder / 25+ Erfarenhet i branschen / 20+ Personer i teamet". *Mobile: stacked cards.*
3. **MainCTA** — "Prata med en elektriker inom 60 sekunder!" + Ring-only CTA + "5.0 på Google". 
4. **ServiceGrid** — "Vårt utbud av tjänster – installerat & klart med 30 % ROT-avdrag" (Belysning/Elcentral/Köksrenovering/Luftvärmepump/Smarta hem/Spotlights + "Ladda fler tjänster"). Internal-linking asset.
5. **Testimonials** — 12 real Google reviews, "5 av 5 Betyg på Google" badge.
6. **MapBlock** — "Vi finns där du finns" + 20 ort buttons (all Stockholm-region) + "Osäker ifall vi finns där du bor? Kontakta oss".
7. **VarProcess** — "Så funkar det" 4 steps ("Fyll i vårt intresseformulär så ringer vår seniora elektriker upp dig" …).
8. **MainContact** — first FORM on the page (~65–70 % scroll depth): trust pane ("3 000+ genomförda installationer om året", 3 steps) + form "Få en kostnadsfri rådgivning".
9. FAQ (5 Q, incl. "600 och 900 kronor i timmen efter ROT") → 10. ContentBlock (3 SEO rows) → 11. BlueCTA ("Prata med en elektriker!") → 12. TeamSection (5 electricians, E-E-A-T) → 13. VissteDuAtt → 14. ROT-block → 15. MikroCTA ("Vill du veta mer? … Sveriges snabbast växande elfirma") → 16. CEBlock (+ CTA pair) → 17. Certificates → 18. FooterSEO (+ CTA pair) → Prefooter/Footer.

### /eljour/ (H1: "Eljour dygnet runt i hela Sverige!", ~2 900+ words live)
1. **Hero-1** — symptom-led paragraph ("Strömlöst, luktar det bränt eller har en säkring gått…") but **primary CTA = form ("Kostnadsfri radgivning"), phone secondary**; hero image = serene forest cabin. *Mobile: same order, form-CTA on top.*
2. **Eljour symptom block** (NEW, not in block-map) — "Jour öppen just nu", 4 promise bullets ("Målsättning att vara på plats inom en timme", "Tydligt pris innan vi rycker ut, inga dolda avgifter"), 15 symptom cards each ending "Ring eljouren 010-265 79 79", Elsäkerhetsverket-sourced fire stat, 112-first escalation. *Mobile: accordion + "Se fler tecken (6)".* Excellent.
3. **Metrics** — same installation-framed trio ("1000+ Nöjda kunder … Över tusen genomförda **installationer**"). Off-JTBD here.
4. **MainCTA** — "Prata direkt med en erfaren elektriker **i [ort]** som lyssnar…" — **literal unfilled `[ort]` placeholder live on the pillar**.
5. Testimonials → 6. VarProcess ("steg-för-steg-lista som beskriver hela **installationsprocessen**"; step 1 "Fyll i vårt intresseformulär") → 7. BlueCTA ("Prata med en jour elektriker!") → 8. VissteDuAtt → 9. FAQ (good candour: inställelseavgift + timtaxa, hemförsäkring) → 10. **MainContact** — "**Vi ringer dig inom 24 timmar**" on an emergency page → 11. Hemförsäkring block (ROT twin) whose button reads "**Läs mer om ROT-avdrag**" (mismatch) → 12. MikroCTA ("…hur Sveriges snabbast växande elfirma kan dig när du behöver akut eljour" — missing word "hjälpa") → 13. ContentBlock → 14. MapBlock → 15. CEBlock ("säkerhetskrifter" typo) → 16. Certificates → 17. FooterSEO → Footer.

### /elinstallation/ (H1: "Elinstallationer över hela Sverige!", 2 027 words)
1. **Hero-1** — sub mentions "moderna AI lösningar" to a 35–65 homeowner audience. 2. **Testimonials** (proof before any claim of what they do). 3. MainCTA ("inom 60 sekunder"). 4. ServiceGrid. 5. VarProcess. 6. **LEGACY form block** — "Få en kostnadsfri konsultation! **Alltid fasta priser** och professionell service" → Förnamn/Efternamn/E-post/Telefon/Adress/Postnummer/Tjänst/Meddelande → "Få ditt förslag" (different field set, different submit label, different system than MainContact). 7. FAQ ("mellan 600 och 900 kronor per timme" — contradicts "Alltid fasta priser"). 8. ContentBlock → 9. BlueCTA → 10. ROT-block → 11. MapBlock → 12. VissteDuAtt → 13. MikroCTA → 14. CEBlock → 15. Certificates → 16. FooterSEO → Footer. **No MainContact two-pane block on this pillar.**

### /laddbox/ (H1: "Laddbox med installation i hela Sverige!", 2 531 words)
1. **Hero-1** — "marknadens bästa priser … branschens lägsta priser". 2. **ProductGrid** — 4 laddboxar with real Fr.-prices (Zaptec Go 4 490 kr, Zaptec Go 2 5 890 kr, Easee Charge Up 4 390 kr, NexBlue Edge 2 4 190 kr) + kampanj tags. 3. Testimonials. 4. MainCTA ("Prata med en rådgivare inom 60 sekunder!"). 5. VarProcess. 6. **MainContact** (first form, ~55 % depth). 7. FAQ (price anchor: "5 000–10 000 kr efter skatteavdrag"). 8. ContentBlock → 9. BlueCTA → 10. TeamSection → 11. MapBlock → 12. VissteDuAtt → 13. MikroCTA → 14. GronTeknik → 15. CEBlock → 16. Certificates → 17. FooterSEO → Footer. **No Laddboxkalkylatorn embed or link anywhere on the pillar** (it exists as an orphan page and in the header mega-menu only).

### /batterilagring/ (2 752 words) — the ONLY pillar on Hero_2
1. **Hero_2 + aof form** — breadcrumbs (Hem › Batterilagring); **H1 = the small eyebrow "Batterilagring / Solcellsbatteri"; H2 = the real headline "Batterilagring med installation – kapa elkostnaderna idag!"** (H1/H2 inversion). CTA pair + 5.0 row left, full lead form right. *Mobile: text → 2 CTAs → 5.0 → form card stacked below (~1.5 screens to reach form).* 
2. **ProductGrid** — 4 batteries with Fr.-prices (Dyness Stack100 Pro 34 900 kr, Eway 33 000 kr, Enershare 36 250 kr, SAJ HS3 34 900 kr).
3. MainCTA ("Prata med en batteriexpert inom 60 sekunder!").
4. **Calculator-UI** — embedded Batterikalkylatorn ("Vad tjänar du på ett solcellsbatteri?") incl. its own offert mini-form (Namn/E-post/Telefon/Postnummer → "Skicka offertförfrågan") and candour-clean "Så har vi räknat" methodology. **Its error state reads "Något gick fel. Ring oss på 010-123 45 67" — a placeholder phone number, not Ampy's real 010-265 79 79.**
5. Testimonials → 6. ContentBlock (stödtjänster/Tibber, Grön Teknik 50 %) → 7. BlueCTA → 8. VarProcess → 9. **MainContact** (form #3 on the page) → 10. FAQ (candour-clean: "Besparingen … normalt mellan 10 000 och 30 000 kronor per år, beroende på…") → 11. TeamSection → 12. MapBlock → 13. MikroCTA → 14. GronTeknik → 15. VissteDuAtt → 16. CEBlock ("Landets bästa hembatteri installatörer" in FooterSEO) → 17. Certificates → 18. FooterSEO → Footer.

---

## Customer-flow walkthrough (35–65 Swedish homeowner, mobile-first)

**First 5 seconds (Hero-1 pillars):** A clean white card, a large clear H1 naming the service, two big buttons, a Google 5.0 row. Good scent for organic "elektriker"/"laddbox" queries — message match to broad intent is fine. But the first thing the eye can read on the primary button is a spelling error ("Kostnadsfri radgivning"), and the promise underneath is a price superlative ("marknadens billigaste priser") that this risk-averse audience has learned to distrust from Byggahus/Reddit horror stories about final-price surprises. Nothing above the fold answers their actual anxieties: *what does it cost, who comes, will they answer later*.

**Scroll (elektriker/laddbox):** Metrics/ProductGrid → a Ring-band → services → 12 reviews → orter → process. The narrative is decent but the **first form appears at block 6–8 (~55–70 % depth)**. On mobile that is 8–12 screens of thumb-scrolling before the site asks for anything. The MECLABS heuristic says motivation is being built (v: reviews, process, ROT) but the *call to action arrives after attention has decayed*; the Clarity paid-session data (deep scrolls, 0 form starts) is consistent with exactly this shape.

**Eljour flow:** A panicked visitor gets a superb symptom triage block within one scroll — severity-calibrated advice, 112-first, "Ring eljouren" on every card. But the page frame fights it: hero primary CTA is a *form*, the hero photo is a tranquil forest cabin, the Metrics/VarProcess talk about *installations*, and the only form block promises a call-back "inom 24 timmar" — a promise that reads as an insult at 23:30 with a burning smell. Unbounce's professional-services benchmark says urgent/repair pages are the highest-converting page type *when the page commits to the urgent job*; this one half-commits.

**Batterilagring flow:** The strongest composition of the five — form in hero, priced products, an interactive calculator as the signature device, candour-clean methodology, FAQ with honest ranges. A motivated researcher can self-qualify and convert in three different places. The cost of that richness: three separate form systems on one page and an H1 that is a two-word eyebrow.

**Decision point:** On every pillar the visitor who wants to act early has only the phone or the header "Gratis rådgivning" CTA (which opens the form journey). The visitor who reads to the end passes 6–9 CTA bands with near-identical "Kostnadsfri rådgivning / Ring" asks — repetition without progression (each band re-asks; none answers a new objection at that scroll depth).

---

## What works (keep)

- **Eljour symptom block** — best conversion asset on any pillar: JTBD-perfect, severity-calibrated, phone-first, real Elsäkerhetsverket stat, 112-first candour. Keep, and let the rest of /eljour/ inherit its register.
- **Embedded Batterikalkylatorn on /batterilagring/** — the "signature device" pattern working: instant value, self-qualification, its own low-friction offert form (4 fields — Baymard-compliant), honest "Så har vi räknat". This is the template for /laddbox/.
- **Testimonials block** — 12 verifiably real Google reviews with names + months; "5 av 5 · Betyg på Google" is the *only* anchored rating instance on the site.
- **ProductGrid with real prices** (laddbox, batterilagring) — genuine price anchoring; rare among Swedish elfirmor, strong differentiator.
- **FAQ price candour** — "600–900 kr/timme efter ROT", "5 000–10 000 kr efter skatteavdrag", "10 000–30 000 kr per år beroende på…" — exactly the transparent-price proof Konsumentverket-minded customers seek. It is just buried at 70–80 % depth.
- **Hero-1 visual clarity** on mobile — stacked, legible, fast to parse; big tap targets (Fitts).
- **MainContact two-pane** — proof + 3-step expectation ("Vi ringer dig inom 24 timmar") + form is the right *pattern* for planned services.
- **Breadcrumbs on Hero_2** (batterilagring + all geo children) — correct hierarchy signal.

---

## Findings

**PIL-01 · P0 · Literal `[ort]` placeholder live on /eljour/ pillar.** MainCTA copy: "Prata direkt med en erfaren elektriker i [ort] som lyssnar på ditt problem…". Verified in the live fetch and in `data/pages/eljour.html` (pillar only; the Åkersberga child fills correctly). A raw template token on a trust-critical CTA destroys credibility (NN/g: visible system internals = perceived sloppiness → anxiety per MECLABS `a`). *Mobile: identical.* Fix = 5-minute content edit. Priority: 1 page × 2 (mid) × 3 (high, trust) = **6, but P0 on trust-damage grounds**.

**PIL-02 · P0 · "Kostnadsfri radgivning" (missing å) on the primary CTA button, site-wide.** Verified live on /elektriker/, /eljour/, /elinstallation/, /laddbox/ heroes and in CE/FooterSEO CTA pairs; present in 20 of 36 HTML snapshots incl. all laddbox product pages and om-oss; also live on geo children (2 hits on /eljour/akersberga/). The Hero_2 variant spells it correctly, proving it's the shared Hero-1/CTA-library string. A spelling error **on the primary conversion button** is the single highest-visibility trust defect on the site (MECLABS anxiety; Cialdini authority undermined). Priority: ≥250 pages × 3 (hero) × 2 = **1500+ — highest score in this audit**. One string fix in the button library.

**PIL-03 · P0 · /eljour/ page architecture contradicts the emergency JTBD.** Four verified mismatches: (a) hero primary CTA is the form, phone is secondary; (b) hero image is a calm forest cabin; (c) Metrics + VarProcess use installation copy ("beskriver hela installationsprocessen", "Fyll i vårt intresseformulär"); (d) MainContact promises "Vi ringer dig inom 24 timmar" directly under a hero claiming "Målsättning att vara på plats inom en timme" — an internal contradiction the candour canon itself flags. Unbounce benchmark: urgent/repair pages are the top conversion opportunity in home services *when phone-first*; business context confirms Eljour is the strongest future campaign candidate. *Mobile: the symptom block's fixed call bar partially rescues this — but the hero above it still leads with the form.*  Priority: 1 page (+56 eljour-i children sharing the copy pattern) × 3 × 3 = **~513**.

**PIL-04 · P1 · First form arrives at 55–70 % depth on all four Hero-1 pillars.** /elektriker/ block 8 of 18; /laddbox/ block 6 of 17; /elinstallation/ block 6 (and it's the legacy form); /eljour/ block 10. Meanwhile every geo CHILD gets Hero_2 with the form in the hero. The template hierarchy is inverted: the pages with the most authority and traffic have the least conversion machinery up front (MECLABS: the funnel sequence must present the ask while motivation is peaking; GA4 shows deep scrolls but 0 form starts). *Mobile: 8–12 screens to the first field.* Priority: 4 pages × 3 (hero-level structural) × 3 = **36** (template-level; ×leverage as the pattern for future pillars).

**PIL-05 · P1 · H1/H2 inversion on /batterilagring/ (Hero_2).** Verified markup: `<h1 class="hero_2__section-subheading">Batterilagring / Solcellsbatteri</h1>` (the small eyebrow) vs `<h2 class="hero_2__section-heading">Batterilagring med installation – kapa elkostnaderna idag!</h2>`. The document's H1 is a 2-word category label — weak for SEO (H1 should carry the primary intent phrase) and it's visually subordinate (message-match: the biggest text should be the H1 promise). Affects this pillar + all 224 Hero_2 geo children + ~22 service pages. Priority: ~250 pages × 3 × 2 = **1500 (shared with the Hero_2 block audit — fix once in the template)**.

**PIL-06 · P1 · Unanchored "5.0" appears 4–6× per pillar.** Hero row, MainCTA "5.0 på Google", MapBlock (batterilagring shows a bare "Vi finns där du finns 5.0"), header, footer — all rating-without-count. Only the Testimonials badge anchors ("5 av 5 · Betyg på Google" + 12 named reviews). Candour gate: anchored = keep; bare "5.0" = must gain "(X recensioner)" + link or be dropped. Baymard/Cialdini: social proof without verifiable substance reads as decoration to skeptical buyers. **[GAP: owner-confirmed current rating + review count needed.]** Priority: ~326 pages × 2 × 2 = **~1300 (shared, fix in trust-row component)**.

**PIL-07 · P1 · Metrics block claims vs candour canon + internal contradiction.** "1000+ Nöjda kunder … Över tusen genomförda installationer" (business context lists "1000+ kunder" as banned unless owner-confirmed current) sits on the same pages as MainContact's "3 000+ genomförda installationer om året". Both cannot be the headline scale-fact; a visitor who notices does the arithmetic and trusts neither. "25+ Erfarenhet i branschen" (unit missing — years? combined?) is ambiguous. **[GAP: owner to lock one canonical scale metric + unit.]** Priority: ~10 pages (metrics) but the 3 000+/1000+ pairing recurs wherever MainContact renders → 2 × 2 × ~60 = **~240**.

**PIL-08 · P1 · /elinstallation/ runs a legacy form system with a contradicted claim.** "Få en kostnadsfri konsultation! **Alltid fasta priser**…" → "Få ditt förslag" — while the FAQ two blocks later says "mellan 600 och 900 kronor per timme". Fixed-price claim vs hourly-rate reality is precisely the Byggahus-forum trust killer (final-price surprise). The block also fragments the form estate (third distinct field set/submit label → third analytics signature; plausibly contributes to the "0 form_start" measurement hole). Replace with MainContact. Priority: 1 page × 3 × 3 = **9** + measurement benefit.

**PIL-09 · P1 · Placeholder phone number in the embedded calculator's error state (/batterilagring/).** "Något gick fel. Ring oss på **010-123 45 67**" — not Ampy's number. The one moment the tool fails is the one moment it hands the user a dead phone line. Same string likely in the standalone /batterikalkylator/. *Mobile: identical.* Priority: 2 pages × 3 (form) × 3 = **18; P1 because it only shows on error**.

**PIL-10 · P2 · Superlative price story is inconsistent across pillars.** /elektriker/: "marknadens billigaste priser"; /laddbox/: "marknadens bästa priser … branschens lägsta priser"; /elinstallation/: "Alltid fasta priser"; MikroCTA everywhere: "Sveriges snabbast växande elfirma". Owner directive allows strong superlatives unless demonstrably false — but "billigaste/lägsta" are the *falsifiable* kind (⚑ owner-confirm or soften to the verifiable transparent-price story the FAQs already carry: real kr-ranges beat "billigast" for this audience per the Konsumentverket written-quote norm). Priority: 5 pages × 3 × 1 = **15 ⚑**.

**PIL-11 · P2 · "Hela Sverige!" headline vs all-Stockholm ort grid.** Every pillar H1 claims national coverage (allowed, owner directive 2026-07-18) but MapBlock then lists 20 Stockholm-region orter (Solna, Sollentuna, Vaxholm, Tumba…). A Göteborg visitor experiences a bait-and-switch inside one page (message-match violation *within* the page; Jakob's law — users expect a coverage map to reflect the promise). Fix in the MapBlock: keep national claim, reframe grid heading ("Här har vi installerat senast" or add region tabs), keep the "Osäker ifall vi finns där du bor?" fallback which is good. Priority: 5 pillars + all pages carrying MapBlock (~250) × 2 × 1 = **~500 (fix once in MapBlock)**.

**PIL-12 · P2 · CTA proliferation without progression.** /elektriker/ carries ~9 ask-bands (hero pair, MainCTA, MainContact, BlueCTA, MikroCTA, CEBlock pair, FooterSEO pair, header, footer) all saying variants of "Kostnadsfri rådgivning / Ring". NN/g: repeated identical asks train banner-blindness; each band spends attention that a differentiated ask (price question → calculator; risk question → symptom check; proof question → reviews) would convert. Consolidate to ~4 asks, each answering the objection live at that scroll depth. Priority: 5 × 2 × 2 = **20 template-level**.

**PIL-13 · P2 · /laddbox/ lacks its calculator; template asymmetry with /batterilagring/.** Batterilagring embeds its kalkylator as the signature device; laddbox — the #2 commercial priority — has no Laddboxkalkylatorn embed, no link in body, no price-comparison device beyond the 4-card grid. The proven pattern is one paste away. Priority: 1 page × 2 × 3 = **6 (+ lead-magnet de-orphaning strategy)**.

**PIL-14 · P2 · /elinstallation/ sequence puts proof before claim, and "AI lösningar" in the hero.** Testimonials as block 2 (before the page has said what elinstallation covers) inverts claim→proof order (MECLABS: value proposition first, corroboration second). Hero sub "Vi kombinerar traditionell yrkesstolthet med moderna AI lösningar" — unexplained "AI" to a 35–65 homeowner adds confusion, not value clarity. Priority: 1 × 3 × 2 = **6**.

**PIL-15 · P3 · Systematic copy-grammar defects in shared blocks.** "Vi går **vi** igenom dina behov", "Vi skickar **vi** ut en bekräftelse" (VarProcess steps 2–3, live on ALL five pillars); "ocg företag" (TeamSection Yousef bio, 2 pillars); "säkerhetskrifter", "kan dig när du behöver" (eljour); eljour hemförsäkring block's button linking "Läs mer om ROT-avdrag". Individually trivial; together they read as carelessness to the exact audience that equates carelessness in text with carelessness in el. One proofread sweep of the shared-block copy fixes ~300 pages at once. Priority: ~300 × 1 × 1 = **~300 (cheap)**.

**PIL-16 · P3 · Duplicate TeamSection/testimonials content across pillars dilutes local relevance.** The identical 12 reviews + 5 identical bios render on all pillars; none is filtered to the pillar's vertical (laddbox pillar could lead with the elbox/laddbox reviews — Alexandra Kamona's "installerade vår elbox", Daniel Hellström's "uppfarten"). CPT already stores them; ordering by vertical is a query change. Priority: 5 × 1 × 1 = **5**.

---

## Pillar vs geo children — is the hierarchy clear to a visitor?

**Structurally yes, experientially half.** Children carry breadcrumbs (Hem › Eljour › Åkersberga) and correct localized H1s ("Eljour i Åkersberga"); the pillar links down via MapBlock's 20-ort grid. But three things blur it for a human:
1. **The conversion hierarchy is upside down.** Children (Hero_2) open with a lead form; pillars (Hero-1) open with none. A visitor arriving on the pillar — the highest-traffic entry — gets the *weaker* conversion page, then must either find a tiny ort button at 40–60 % depth or convert via a form that is 8+ mobile screens down. The child pages are better landing pages than their parents.
2. **The MapBlock shows 20 of 56 orter with no "see all" index** — a visitor from an unlisted kommun can't tell whether their ort page exists; the only fallback is "Kontakta oss". No pillar links to a full ort index (SEO: crawl path to 56 children currently depends on the partial grid + sitemap).
3. **Content is near-identical between parent and child** (Åkersberga eljour = same Metrics, same reviews, same VarProcess, ~2 850 words vs pillar's ~2 880). The only differentiation is the H1/intro ort token — which the pillar itself leaks (`[ort]`, PIL-01). For visitors the pages are indistinguishable; nothing on a child says "this is your local page" beyond the headline (no local proof, no ort-specific review filtering, no inställelsetid for that ort).

**Recommendation:** keep the parent→child architecture, but (a) give pillars the same hero-form capability as children (PIL-04), (b) add a full ort A–Z index behind the MapBlock grid, (c) differentiate children with one genuinely local element (nearest reviews, "senaste jobb i {ort}") rather than more boilerplate.

---

## Recommended sequence (wireframe) — canonical Hero-1 pillar (elektriker / elinstallation / laddbox)

| # | Block | Why here | New/existing/modified |
|---|-------|----------|----------------------|
| 1 | Hero-1 **with compact lead-capture** (name+tel+postnr, "Fler detaljer" later) or persistent "Boka rådgivning" that jumps to MainContact | Ask while motivation peaks (MECLABS); match the geo-child pattern; Baymard: 3 visible fields | **Modified** (typo fixed; superlative → verifiable price promise, e.g. "Fasta priser i offerten – 600–900 kr/tim efter ROT") |
| 2 | Metrics (one canonical, owner-confirmed scale fact + Elsäkerhetsverket-registered badge) | Instant credibility before the first scroll decision; Cialdini authority | **Modified** (candour fix PIL-07; add "Kolla elföretaget"-verifiable claim) |
| 3 | ServiceGrid / ProductGrid (with prices where they exist) | Self-segmentation + price anchoring; laddbox keeps grid, elektriker keeps tjänster | Existing |
| 4 | **Signature device**: Laddboxkalkylatorn embed (laddbox) / price-range table from FAQ content (elektriker, elinstallation) | Answers the #1 JTBD question (vad kostar det?) at 30 % depth instead of 75 %; HealthSpire: content that answers real questions converts | **New placement** (content exists) |
| 5 | Testimonials (vertical-filtered order) + Certificates **merged proof band** | Proof directly after price claim (claim→proof order); moves authority up from the basement | Modified |
| 6 | VarProcess (grammar-fixed) → **MainContact** | Process removes uncertainty, form catches the decision it creates | Existing, re-paired |
| 7 | FAQ (keep price candour; add "Vad händer efter att jag skickat?" ) | Objection handling for the still-unsure | Modified |
| 8 | ContentBlock + CEBlock (SEO meat, intact, accordion-packaged on mobile) | SEO preserved — re-sequenced, never deleted | Existing |
| 9 | TeamSection → VissteDuAtt → ROT/GronTeknik | E-E-A-T + incentive close | Existing |
| 10 | MapBlock (reframed heading + full ort index link) → ONE closing CTA band (FooterSEO) → Footer | Hierarchy clarity (PIL-11) + single final ask instead of 4 stacked bands | Modified (drop BlueCTA + MikroCTA + CEBlock CTAs → PIL-12) |

### /eljour/ variant (emergency-first)
1. Hero-1 **phone-primary** (swap CTA order; ring button green; image = electrician at a dark elcentral, not a cabin) → 2. Symptom block (unchanged — it IS the page) → 3. Jour-specific trust strip (inställelsetid promise + "Tydligt pris innan vi rycker ut" + anchored rating) → 4. Jour-FAQ (cost/insurance — already good) → 5. Hemförsäkring block (CTA fixed) → 6. MainContact **re-copied for non-acute** ("Inte akut? Beskriv felet så ringer vi upp dig" — kills the 24h contradiction) → 7. SEO content intact → 8. MapBlock → footer. Mobile: sticky "Ring eljouren" call bar page-wide, not just inside the symptom block.

### /batterilagring/ variant
Keep current spine (it's the best); fix H1/H2 (PIL-05), fix the error-state phone (PIL-09), and reduce to two form systems (hero aof + calculator offert; MainContact becomes phone-CTA band) — three identical-purpose forms on one page is redundancy without coverage.

---

## Test hypotheses (top 3, A/B)

1. **HYPOTES — hero form on pillars:** Adding a 3-field lead capture (namn/telefon/postnr) to Hero-1 on /elektriker/ and /laddbox/ (A = current no-form hero, B = hero with compact form) will increase form submissions per session by ≥30 % without lowering lead quality, because geo children already run the form-in-hero pattern and the MECLABS sequence currently delays the ask past peak motivation. Guardrail metric: phone-click rate.
2. **HYPOTES — phone-primary eljour hero:** Swapping CTA order on /eljour/ (A = form-first, B = "Ring eljouren 010-265 79 79" as the single primary hero CTA with form demoted to "Inte akut?") will increase tel-clicks per session by ≥50 % on mobile, per the Unbounce urgent-page benchmark and the JTBD mismatch documented in PIL-03.
3. **HYPOTES — anchored rating:** Replacing bare "5.0 ★★★★★" trust rows with "5,0 av 5 · {N} recensioner på Google" (linked) will lift hero→scroll continuation and form-start rate measurably, because unanchored perfection reads as fabricated to skeptical Swedish homeowners (Cialdini social proof requires verifiability). Requires owner-confirmed count [GAP]; run A/B only after the count is real.

---

*File is the permanent record for the pillar template. Companion block-level records: research/blocks/ (Hero-1, Hero_2, MainContact, MapBlock, Metrics). All quotes above are verbatim from live fetches 2026-08-02.*
