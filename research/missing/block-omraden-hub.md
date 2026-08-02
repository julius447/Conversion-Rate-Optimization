# "Alla områden"-hubben + deterministisk ort-rad (MapBlock v2 backbone)

**Status: BUILD — my addition (not on the team's candidate list, but explicitly deferred to research/missing/ by the MapBlock audit: "New-block proposal filed conceptually here; belongs in `research/missing/`"). Routing/conversion infrastructure for the 224-page geo estate.**

## Job-to-be-done
Give the "finns ni i X?"-visitor a complete, scannable answer — and give the 224 programmatic geo pages a stable internal-link architecture instead of a lottery. Today the MapBlock deals a **random 20-of-56** ort subset per cache regeneration (verified: different lists on sibling pages and over time), so a visitor checking their ort has a ~64 % chance of not finding it *even when the page exists* (MAP-01); the global footer links 3 of 224 geo pages (GLOB-10/FTR-01); no "alla områden" index exists anywhere (MAP-07); and the sub-card manufactures doubt ("Osäker ifall vi finns där du bor?") two sentences under a "hela Sverige" claim (MAP-02).

## Anatomy (in words)
**Element 1 — the hub page(s):** 1 per CPT (or one combined page with tabs: Elektriker / Eljour / Elinstallation / Laddbox):
- AlternativHero v2 (real H1: "Här finns Ampy — alla områden", one candour intro line, compact trust row per the CAT-05 fix).
- A–Z / region-grouped complete ort list (all 56 per CPT), ctrl-F-able, real links.
- One MainCTA-class close: "Hittar du inte din ort? Ring oss — vi täcker hela Sverige" (tel: — answer, don't ask).
**Element 2 — the deterministic ort-rad (MapBlock v2):** replaces the random 20-grid on 265 pages:
- Nearest-N by geography for geo pages ("eljour nära Åkersberga" is genuinely useful), alphabetical fixed set elsewhere; **stable across crawls**.
- 8–12 links + "Alla områden →" hub link (mobile: accordion-collapsed, ≥44 px tap targets — fixes MAP-05's sub-WCAG 22–26 px buttons).
- Sub-card rewritten to affirm: "Vi täcker hela Sverige. Hittar du inte din ort? Ring 010-265 79 79." (tel: or anchor to the on-page form — kills the /kontakt/ export, MAP-03).
**Element 3 — footer feed:** "Områden" prefooter column → 6–10 curated orter + "Alla områden →" (GLOB-10).

## Templates + position
Hub: 1–4 new pages under a stable URL (e.g. /omraden/). Ort-rad: all 265 MapBlock carrier pages, same slot (low-page, depth 0.7–0.8 — placement discipline is already right). Footer: 325 pages.

## Why it beats status quo
UX: NN/g — users scan lists via expected order; a stable, complete, grouped list answers the coverage question instead of gambling on it. SEO: converts the rotating doorway cross-link mesh (the exact "doorway-devalvering" pattern the 2026-08 SEO total-audit named as the site's core risk) into hub-and-spoke; every geo page gets one permanent inlink source and the crawl graph accumulates instead of churning. Conversion: the reframed sub-card turns a manufactured-doubt moment (MECLABS −2a) into a phone CTA.

**Adversarial note — is this CRO or SEO scope?** Both, and that is the point: the block's conversion job (coverage reassurance + call CTA at the "do they serve me?" moment) and its SEO job (stable link equity) are currently entangled in one broken block doing both halfway (MAP audit's own verdict). Trade-off named: nearest-N lists are more build effort than alphabetical; alphabetical is an acceptable v1. Coordinate with the SEO workstream's doorway program so hub URLs are set once.

## Candour-gate check
PASS with one week-1 hotfix independent of the build: the live eljour ACF sentence "**Se alla områden** där vår jour finns tillgänglig i listan nedan" above a random 20-of-56 list is factually false as rendered (MAP-04) — fix the sentence now ("Se ett urval…"), then point it at the hub when live. The hub itself must reflect routing truth: national copy claim is owner-permitted, but the ort list shows where dedicated pages/coverage exist [GAP: routing truth for the reframed intro — "rikstäckande nätverk" vs 27-kommun ops].

## Effort & priority
- **Effort: M** (hub template = AlternativHero v2 + list loop, mostly existing components; deterministic list = query change in the CPT loop; footer = config).
- **Priority arithmetic:** 224 geo pages (fed) + 265 carriers × 1 (low-page funnel weight) × 2 (medium — architecture + reassurance, not a direct form fix) = **~530** (per the MapBlock audit's own arithmetic), with the MAP-04 candour hotfix carved out as week-1. → **P2 overall, month 2 — but the deterministic-list switch and the sub-card rewrite are cheap month-1 riders.**

## Dependencies
1. SEO-workstream alignment (doorway program, hub URL canon).
2. Owner routing-truth confirmation for coverage copy [GAP].
3. Sub-card CTA anchor targets (ships with the sitewide CTA-retarget fix).
