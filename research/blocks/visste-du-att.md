# Visste du att — `visste-du-att` (awareness/editorial band)

Used on: **290 of 326 pages (89%)** — the single most widely deployed content block on the site.
By category (from `data/block-map.json`): elektriker-i 56 · elinstallation-i 56 · eljour-i 56 · laddbox-i 56 (= 224 programmatic geo pages), service 22, ev-product 16, elektriker-för-x 13, battery-product 10, pillar pages 5 (/elektriker/, /elinstallation/, /laddbox/, /batterilagring/, +1). Absent only from home, kontakt, articles (post), lead magnets, and team-member pages.

Funnel position(s): **mid-to-low page, positions 8–19 of 17–23 blocks (avg ~70% scroll depth; range 40–83%)**. On the 224 geo pages it sits **immediately after BlueCTA** (the phone-first band) in every CPT. Two structurally different placements matter:

- **eljour-i (56 pages):** position 9/21 — `VarProcess → BlueCTA → VissteDuAtt → FAQ → MainContact` — i.e. it interrupts the path **before** the FAQ and the MainContact form, on the highest-urgency template on the site.
- **elektriker-i / service / product pages:** position 13–18, after MainContact/FAQ, in the tail SEO zone (`ContentBlock → BlueCTA → VissteDuAtt → CEBlock → Certificates`).

## Verified anatomy (live fetch + raw snapshot)

Fetched live: https://ampy.se/elservice/armatur/ and https://ampy.se/eljour/akersberga/; markup detail from `data/pages/elektriker.html`.

- Dark navy card: `.visste-du-att__container` **background-color: #010328** (NOT the canonical midnight #090b32 — token defect), rounded, bg wave image `Group-1591-1.webp`, white text.
- Heading: **"Visste du att.."** (literal two dots, not an ellipsis) → ACF sub-heading phrased as a question → one long ACF paragraph (~180–220 words) with internal SEO anchor links. **No CTA of any kind.** Body text is `font-weight: 300` white-on-navy at `--text-m`, max-width 70% desktop / 100% mobile.
- Lightbulb: absolutely positioned PNG (`Group-1592-1.png`, 240×382, `alt=""`), desktop `top:-15%; right:10rem; height:80%`. Bricks interaction on the `<img>`: `trigger: enterView → startAnimation, animationType: "swing", animationDuration: 4, animationDelay: 2`, with `data-interaction-hidden-on-load="1"` — the bulb is invisible until the block scrolls into view, then pops in 2s later and swings for 4 seconds. **The swing has no `prefers-reduced-motion` guard** (the site's CTA-pulse and spinner animations do have guards; this one does not).
- **Mobile (≤480px):** bulb is retained at `width:30%; top:-15%; right:0` overhanging the card's top-right corner, and the H2 is pushed down with `margin-top: var(--apspace-3xl)` (4xl at 320px) purely to clear the bulb — a spacing hack that puts dead space and a swinging PNG at the top of the card before any words.

Real copy (quoted from live fetches):
- /eljour/akersberga/: "Visste du att.. Din hemförsäkring täcker ofta akuta elfel? Många fastighetsägare är ovetande om att kostnaden för att tillkalla eljour i Åkersberga ofta kan täckas av den ordinarie hemförsäkringen. … minus din självrisk."
- /elservice/armatur/: "Visste du att.. rätt typ av armatur kan förbättra ditt välmående? … kan du faktiskt påverka både din energinivå och din sömnkvalitet."
- /elektriker/ (snapshot): "Visste du att.. Rätt belysningsstyrning kan minska din elförbrukning? … kan sänka energianvändningen för belysning med upp till hälften."

## What it does well

1. **Unique programmatic text + internal links at scale.** Each instance carries a distinct ACF paragraph with contextual anchor text ("hitta en elektriker") — real SEO substance and internal-linking value across 290 pages. This must be preserved (doctrine §3: re-sequence/repackage, never delete).
2. **The register is right.** The canon says awareness blocks should be light and inviting — and the copy actually is: välmående, energitjuvar, plånbok. No fake urgency, du-tilltal, curiosity-framed. The voice passes the candour gate.
3. **Some instances carry genuinely decision-relevant material.** The eljour version (hemförsäkring covers acute elfel, ersättning minus självrisk, documentation requirement) is anxiety-reducing information in the MECLABS sense (reduces `a`, cost-uncertainty) — the exact concern Byggahus/Reddit homeowners voice ("final price surprises").
4. **Visually distinct.** As a pattern-interrupt in a long SEO page it does re-engage a skimming eye (NN/g: users scan, contrast breaks scanning fatigue).

## Issues

**VDA-01 · P2 · desktop+mobile · Conversion dead-end after a phone ask.** On all 224 geo pages the block follows BlueCTA directly: the page asks for a call, then immediately changes the subject into a 200-word editorial with **no CTA and no next step**. MECLABS: momentum built by the CTA band decays through an un-directed digression; Jakob's law: visitors expect a "did you know" band to end in a "read more/ask us" affordance — this one just stops. On eljour-i specifically it stands **between the hero/CTA zone and FAQ+MainContact** (position 9/21) on the template Unbounce benchmarks say converts best on urgency — the worst template to pause on.

**VDA-02 · P2 · mobile-primary · Swinging lightbulb is attention theft plus an accessibility gap.** Motion is the strongest attention magnet in peripheral vision (NN/g on animation; human motion-detection bias). At 70% depth the visitor is an engaged deep-scroller (GA4: 17 of ~32 paid sessions deep-scrolled) — precisely the person we cannot afford to distract from the adjacent CTAs. On mobile the decorative PNG additionally costs the card's entire top band (margin-top hack) on a 375px screen. The swing runs unguarded by `prefers-reduced-motion` (WCAG 2.3.3 best practice; inconsistent with the site's own guarded animations). And with `data-interaction-hidden-on-load="1"`, the bulb never renders at all if the interaction JS fails.

**VDA-03 · P2 · desktop+mobile · Legibility below the audience bar.** `font-weight: 300` white text on #010328 for a ~200-word paragraph is thin light-on-dark long-form — the hardest reading condition for the 35–65 core audience (NN/g / WCAG guidance: avoid light weights for body text on dark backgrounds; presbyopia onset ~40). The block asks the most reading effort of any band on the page and styles it least readably.

**VDA-04 · P3 · desktop+mobile · "Visste du att.." punctuation defect ×290.** Two trailing dots is neither Swedish ellipsis (…) nor a sentence stop, repeated on 89% of the site. Small, but it reads as sloppiness in a brand whose entire proposition is "the tradesperson who tells you the truth" — trust is built or leaked in exactly these details (Cialdini authority = competence signals).

**VDA-05 · P3 · desktop+mobile · Off-canon surface token.** #010328 instead of midnight #090b32 (also flagged in the token-defect canon). Contributes to the documented mid-page dark-band contrast stacking (testimonials + visste-du-att + hero all navy).

**VDA-06 · P3 · content · Unanchored statistic.** "sänka energianvändningen för belysning med upp till hälften" (/elektriker/) is asserted without source. Candour gate: anchor it (Energimyndigheten or equivalent) or soften to a non-numeric claim. Provenance-check the claim set across the 290 ACF instances — a task for the copy pass, flagged here as `[GAP: source per claim]`.

**VDA-07 · P2 · placement · The best content is in the wrong block.** The eljour hemförsäkring fact is objection-handling (i.e. "what will this cost me?") demoted to trivia at position 9/21. HYPOTES: surfacing insurance/cost-certainty content nearer the hero/form on eljour-i lifts form starts (see test 2 below).

## Recommended changes (concrete)

1. **Ship the already-built redesign first.** A verified redesign exists (per block inventory note + owner memory: stacked layout, absolute bulb + 4s swing killed, #010328→#090b32 fixed, slutaudit GO) — the live site still runs the old JSON. Deploying it resolves VDA-02/VDA-05 across all 290 pages at near-zero incremental effort. Owner-gated visual-diff rule applies (approved-rendering canon).
2. **Add one soft, candour-clean next step** to the component template so all 290 instances inherit it: a single low-key text link or ghost pill after the paragraph — copy-pattern direction: "Osäker på vad som gäller hemma hos dig? Ring oss på 010-265 79 79" or a related-article link where one exists. Not a gradient CTA — the block stays editorial; it just stops being a dead-end (VDA-01).
3. **Fix readability in the same component pass:** body `font-weight` 300 → 400, keep `--text-m` or step up one, keep max-width ~65ch (VDA-03). Fix the heading string to "Visste du att …?" or "Visste du att" + question sub-heading carrying the "?" (VDA-04) — one template edit, 290 pages.
4. **Re-sequence on eljour-i only:** move VissteDuAtt below FAQ/MainContact (to the tail SEO zone where every other CPT already has it), OR promote the hemförsäkring content into the FAQ/hero support zone and let the band carry lighter trivia (VDA-07). SEO substance is preserved either way — order changes, content does not.
5. **Copy provenance sweep** of the ACF paragraph bank: anchor or soften every numeric claim (VDA-06). `[GAP: owner/copy-pass]`.

## Priority score (arithmetic shown)

- Pages affected: **290**
- Funnel position weight: **2** (mid-page; avg ~70% depth, but pos 9/21 pre-MainContact on 56 eljour pages)
- Expected effect: **1** (low — the block neither blocks nor collects conversions; harm is momentum-interruption, distraction, and trust micro-leaks; fixing it is a broad polish, not a lever like Hero_2 or MainContact)

**Priority score = 290 × 2 × 1 = 580 → P2** (meaningful, months 2–3) — **with a scheduling override**: because the redesigned component already exists and one template edit propagates to 290 pages, execute the ship-the-redesign + micro-CTA + weight/heading fixes as an early cheap win in month 1; only the eljour re-sequencing and copy provenance sweep belong in the months-2–3 window.

## Test hypotheses (top 2, A/B)

1. HYPOTES: On elektriker-i pages, adding the single phone text-link to VissteDuAtt (variant B) vs current dead-end (A) increases phone-click rate among visitors who scrolled ≥70% — measurable via tel-click attribution per scroll-depth segment.
2. HYPOTES: On eljour-i, moving VissteDuAtt below MainContact (variant B) vs current position 9/21 (A) increases form starts, because the FAQ→MainContact path shortens for urgency-driven visitors (Unbounce: urgent-repair pages are the site's best converters).
