# Missing blocks — index & ranked verdicts (conversion infrastructure, ideator A)

Adversarial integration pass over 14 template deep-dives + 20 block audits. The team's 12 candidates were validated, merged, killed or extended; 2 blocks the candidate list missed were added. Scoring per doctrine: (pages affected) × (funnel weight: hero/form 3 / mid 2 / low 1) × (effect: high 3 / med 2 / low 1). All proposals are additive or repackaging — no SEO substance is deleted anywhere.

## Ranked build list

| # | Block (file) | Reach | Score (arithmetic) | Priority | Effort | Blocking [GAP]s |
|---|---|---|---|---|---|---|
| 1 | **Pris & offert-blocket** (`block-pris-offert.md`) — THE message-match fix; price ranges + fast-offert promise on screen 1–2, sourced from the site's own buried FAQ copy | 134 now → 247 full | 134×3×3=**1 206** (full: 247×3×3=2 223) | **P0** | S–M | price reconciliation; eljour price card |
| 2 | **Verifieringsraden / TrustStrip** (`block-trust-strip.md`) — merges 3 candidates (Elsäkerhetsverket strip + compact trust strip + B2B org-strip) into one component, 4 formats; clones the pre-queried registry link to the form zone | ~290 (+B2B 11, kontakt/om-oss, footer 325) | 290×3×2=**1 740** (+11×3×3=99) | **P0/P1** | S | rating count N; number canon (1000+/3000+); försäkring/ID06 currency |
| 3 | **MiniForm (SSR 3-fält)** (`block-mini-form.md`) — namn/telefon/postnr + GDPR, server-rendered, fully instrumented; replaces the product popup, arms pillars/articles/eljour-lane; enabler for the Hero_2 SSR fix | 30 committed placements + enabler for 260 | committed ≈**678** combined; enables 2 340-score Hero_2 fix | **P1** (instrumentation = week-1 P0) | M | backend decision; SLA label |
| 4 | **Sticky mobil ring-rad** (`block-sticky-call-bar.md`) — eljour committed (owned v3 spec restored), geo/articles as gated A/B; jour-status chip folded in | 57 committed (+190+11 gated) | 57×3×3=**513** (+1 140 gated) | **P1** | S | owner visual diff; 24/7 staffing truth |
| 5 | **Efter-submit-paketet** (`block-tack-forberedelse.md`) — thank-you: calibrated 24h promise + spara-numret + prep checklist + team faces + relocated review ask; pixel-sanctity rider | 1 page = 100 % of form leads | 1×3×3=9 → **sanctity/lead-value override** | **P0 rider + P1 content** | S | SLA + hours; caller roles; GTM sign-off |
| 6 | **ServiceRouter + ProduktTeaser** (`block-service-router.md`) — homepage mid-section rebuild; one service-first router after the hero, compact price-anchored product teaser below the conversion layer; kills HP-01/HP-02 | 1 page (~89 % of organic clicks) | 1×3×3=9 → **P0 by traffic weight** | **P0/P1** | M | canonical fr.-prices |
| 7 | **Två-filers kontakt (eljour)** (`block-two-lane-contact.md`) — Akut? Ring / Kan det vänta? MiniForm; structurally resolves the 60s/1h/24h SLA whiplash | 57 | 57×3×2=**342** | **P1** | M | jour-SLA truth |
| 8 | **"Vad ingår i priset?"** (`block-vad-ingar.md`) — popup-30855 candour content surfaced beside the price; products first, laddbox-i compact variant phase 2 | 26 → 82 | 26×3×2=156 (+56×2×2=224) = **380** | **P1–P2** | S | price-frame fix ships first |
| 9 | **Artikelns konverteringskit** (`block-nasta-steg-artikel.md`) — inline photo-bedömning micro-CTA + "Nästa steg"-slutkort; review ask demoted/relocated | 11 posts (the money-query pages) | 11×2×3=**66** | **P1** | S–M | 2-dagars SLA; field-stat provenance |
| 10 | **Org-referenser & serviceavtal** (`block-b2b-referenser.md`) — B2B proof + long-cycle ask; ships interim (invents nothing) → full when references are collected | 11 B2B pages | 11×2×3=**66** | **P1 interim / P2 full** | M | **B2B reference collection (start week 1)** |
| 11 | **"Alla områden"-hubben + deterministisk ort-rad** (`block-omraden-hub.md`) — hub page(s) + stable nearest-N MapBlock v2 + footer feed; ends the 20-of-56 link lottery | 224 geo fed / 265 carriers | 265×1×2=**~530** | **P2** (MAP-04 candour hotfix = week 1) | M | routing truth; SEO-workstream URL canon |

## Merged (candidates that were the same block)
- **"Elsäkerhetsverket authority strip" + "compact trust strip" + "org-trust strip (B2B)"** → one component: TrustStrip with per-template claim sets (#2). Building three near-identical strips would recreate the diagnosed CTA-band disease (three bands, one job).
- **"Jour-status/öppet-indicator"** → chip inside the sticky ring-rad + eljour hero variant (#4). As a standalone block it duplicates the persistence job and adds candour surface area for zero extra reach.
- ProduktTeaser folded into the ServiceRouter intervention (#6) — they only make sense shipped together; the internal redundancy in the team's own homepage wireframe (products appearing in BOTH router row 2 and teaser) is named and given a kill order (router row 2 dies first if cannibalizing).

## Killed (with reasoning)
- **Related-services grid** — NOT missing. It exists as `services-loop`/ServiceGrid on geo + service pages (and as the post-form exit grid on service pages), correctly placed below the conversion zone. The real work is repair, not creation: the /elservice/ instance has 22 cards with **zero `<a href>`** (CAT-01, dead spans) and needs grouping by demand (CAT-09) — both belong to the block-fix backlog, not the missing-blocks list. Building a "new" grid would duplicate a broken one instead of fixing it.
- **Calculator-embed "blocks"** (Laddboxkalkylatorn on /laddbox/ + EV product pages, per PIL-13/CAT-13/PP-14) — real gaps, but they are *new placements of existing assets* (the Calculator-UI embed pattern is proven on /batterilagring/). Routed to the template wireframes' rollout, not scoped as new block builds.
- **Homepage job-picker hero chips** — the "Jobb-först" divergent homepage stays a deferred test, not a committed block: it modifies an owner-locked, pixel-approved hero (approved-rendering-is-canon) and its thesis (conversion-first homepage) is unproven against the router thesis. Revisit after #6 ships and instruments.
- **Magnet wrap as a "new block"** — the lead-magnet orphan fix (LM-03) is a *sequence* of existing blocks (AlternativHero + VarProcess + FAQ + MainContact); owned by the lead-magnets template rollout. No new component needed.

## Cross-cutting dependencies (the four gates most blocks share)
1. **Owner number-canon session** — one sitting resolves: Google rating + review count N, ONE installations figure (1000+ total vs 3 000+/år contradiction, MET-02/OM-1), headcount, "60 sekunder" and "24 timmar" SLA truth, jour inställelseavgift. Blocks #1, #2, #3, #5, #7 all wait on parts of this.
2. **Instrumentation contract live** (form_start/form_submit + thank-you pixel sanctity) — without it, none of these blocks is measurable; ship week 1 (H2-02, MC-07, TY-03).
3. **Price reconciliation pass** (laddbox 4 190 vs "från ca 5 000"; product hero vs FAQ) — #1, #6, #8 amplify contradictions if shipped first.
4. **CTA-retarget fix** (all "Kostnadsfri rådgivning" → on-page anchors, GEO-01/CTA-01/HP-03) — every micro-CTA in these blocks assumes anchor targets exist.
