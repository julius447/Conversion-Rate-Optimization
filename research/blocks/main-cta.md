# MainCTA — `main-cta-` (ring-only mid-page CTA card, updated version)

**Used on: 268 pages** (from `data/block-map.json`): elektriker-i 56 · elinstallation-i 56 · eljour-i 56 · laddbox-i 56 · service 22 · elektriker-för-X 13 · page 9 (incl. the homepage and the pillar pages elektriker/eljour/elservice/laddboxar/batterilagring).
**Funnel position:** upper-mid page. Position index 4 on 183 pages, 5 on 57, 6 on 22, 3 on 5, 2 on 1 — i.e. it is almost always the **first CTA band after the hero + first proof block**. Preceded by Testimonials (128), Metrics (114) or VarProcess (22); followed by ContentBlock (125), Testimonials (114) or FAQ (22). Exactly one instance per page (0 pages have duplicates).
**Live pages fetched (anti-theatre):** https://ampy.se/elektriker/akersberga/ (geo template) + markup detail from snapshot `data/pages/elektriker.html` (pillar). Real copy quoted throughout.

## Verified anatomy (desktop / mobile)

DOM order (from `elektriker.html` snapshot): H2 `main-cta-__heading` with `data-highlight="last-3"` → paragraph → single `tel:+46102657979` button ("Ring 010-265 79 79", library btn-ring with phone icon) → trust row (Google-G icon linking to the GBP Maps listing → "**5.0** på Google" → 5 stars) → right column `team-image-1.webp` (498×570, `alt=""`, `loading="lazy"`, `fetchpriority="low"`) + two decorative wave SVGs (`main-cta-__overlay-wave`, `main-cta-__bg-wave`). White card, `border-radius var(--apradius-l)`, soft shadow, on-scroll fade-in interaction. Note: the block inventory describes the trust row *above* the heading; the shipped DOM places it *after* the button (proof-after-ask). The `.mcta-trust` fixes are applied by a JS panel, so rendered order should be visually verified per template.

Real copy (elektriker pillar): H2 **"Prata med en elektriker inom 60 sekunder!"** · body "Känn dig trygg med kunnig hjälp, precis när du behöver den. Prata direkt med en erfaren elektriker som lyssnar på ditt problem och guidar dig till en säker, smidig lösning."
Geo variant (Åkersberga, live): same H2, body "Slipp krångel och få fackmannamässig hjälp direkt. Prata med Ampys auktoriserad elektriker i Åkersberga som snabbt löser dina elbehov…" + "Ring 010-265 79 79" + "**5.0** på Google".

**Heading styling (measured):** base CSS clips the **entire H2** to a gradient — `background-image: linear-gradient(90deg, var(--color-25) 25%, var(--color-7) 70%); -webkit-text-fill-color: transparent`, where `--color-25` = hsl(171 95% 41%) = **#05ccae** and `--color-7` = hsl(189 43% 56%) = **#5fb1bf**. A DOMContentLoaded script then wraps the last 3 words in a gradient span and resets the rest of the heading to solid `var(--color-3)` (midnight hsl(237 69% 12%) — fine).

**Mobile (verified CSS):** at ≤767px a newer custom layer ("Ampy Main CTA — TRUST-RAD + LAYOUT") centers the whole stack (heading clamp 24→30px, body centered at ~16.1px, trust row centered, card padding 20/20/28). Waves hidden at ≤780/≤480. Team image goes full-width (`width:100% !important` at ≤780). This layer overrides an older base layer that still ships `text-align: justify` + left alignment at ≤480 — two competing `!important` layers on the same block.

## What it does well
1. **Single-ask discipline.** One tel: CTA, no competing form link — the cleanest ask on the site (Hick's law; MECLABS: fewer simultaneous objectives = clearer value exchange). On the 56 eljour-i pages a phone-first band this high is exactly right (Unbounce: urgent/repair intent converts phone-first).
2. **Correct slot.** Position 4–5, immediately after Metrics/Testimonials — the ask arrives right after proof (Cialdini social proof → commitment), before the visitor sinks into 2 000+ words of SEO content.
3. **Trust row is source-linked.** The Google-G links to the real GBP listing — verifiable, candour-compatible in structure.
4. **Human imagery, cheap.** Real team photo, lazy-loaded, `fetchpriority="low"` — trust-building faces (NN/g: real people beat stock) without an LCP cost.
5. **The mobile fix layer is genuinely good** — centered stack, prototype-measured sizes, justify-text defect corrected.

## Issues

| ID | Severity | Issue | Desktop / mobile | Evidence |
|---|---|---|---|---|
| MC-1 | **P1** | **Gradient heading fails contrast on the words that carry the claim.** The last-3 highlight ("inom 60 sekunder!") renders #05ccae→#5fb1bf on a white card: measured contrast **2.05:1 and 2.46:1 vs the WCAG AA large-text minimum 3:1**. Worse: pre-JS, the *entire* H2 is gradient-transparent — on a site with ~9–10s lab LCP, slow devices show the whole headline in failing contrast until DOMContentLoaded rewrites it. | Both; mobile sun-glare makes 2.0–2.5:1 effectively invisible | WCAG 1.4.3/1.4.11; computed from the shipped CSS variables |
| MC-2 | **P1** | **"5.0 på Google" is unanchored** — no review count, no date. Doctrine + candour gate: rating claims must be anchored (rating + count + source) or removed. Sister blocks already anchor it ("5 av 5 · Betyg på Google" in Testimonials/MainContact) — MainCTA is the odd one out, on 268 pages. | Both | Candour gate (business context §Brand); block inventory cross-cutting note |
| MC-3 | **P1** | **"inom 60 sekunder!" is an operational promise with no visible basis.** If a caller does not reach *en elektriker* (not a coordinator) within 60 seconds during opening hours, this is a false claim — candour BLOCK territory. It also collides with the adjacent MainContact promise "Vi ringer dig inom 24 timmar" two scrolls later (mixed expectation-setting). Not asserted false here — **owner must confirm or the claim must change.** | Both | Candour gate; MECLABS anxiety term (unmet promise → distrust) |
| MC-4 | **P2** | **Role redundancy vs BlueCTA.** 230 of 268 MainCTA pages also carry BlueCTA — a second phone-only band with the identical job ("Prata med en elektriker!… Ring 010-265 79 79" on the live Åkersberga page). Add MikroCTA (173 pages, dual CTA), FooterSEO (264, dual CTA), Hero_2 (260, 2 CTAs + form), MainContact (267) and the header CTA: **7–9 conversion asks per page**, with the phone ask alone repeated 4–6×. Repetition per se is fine on long pages (MECLABS HealthSpire), but *undifferentiated* repetition trains banner-blindness (NN/g) and dilutes which band is "the" phone moment. | Both; on mobile the stacked duplicates add ~3–4 extra screens of CTA | NN/g banner blindness; Jakob's law (one clear pattern per job) |
| MC-5 | **P2** | **Templated copy defects at scale.** Geo body copy ships a grammar error — "Ampys **auktoriserad** elektriker i Åkersberga" (should be *auktoriserade*) — live on the elektriker-i template (56 pages, likely mirrored in sibling geo templates). And the H2 is identical on the pillar and geo pages regardless of intent (laddbox-i visitors get the same generic "Prata med en elektriker…" line — message-match miss vs their job-to-be-done). | Both | Google message match; JTBD; audience is grammar-sensitive 35–65 homeowners |
| MC-6 | **P3** | **Fragile double CSS layer.** The old base layer (justify text, left align ≤480) is still shipped and only beaten by `!important` in the new layer; DOM trust-row position also depends on a JS panel. One specificity change regresses 268 pages. `alt=""` on the team image is acceptable-decorative but wastes an E-E-A-T hook (a named electrician). | Mobile-weighted | Maintainability; approved-rendering canon (any fix must not shift pixels without owner visual diff) |

## Recommended changes (concrete; copy-pattern direction, not final copy)

1. **Fix the heading contrast (MC-1), smallest possible visual diff:** keep the gradient *device* but darken the stops to ≥3:1 versions of the same hues (e.g. teal at ~hsl(171 95% 28%) territory), or gradient only as an underline/accent under solid midnight text. Also set the pre-JS fallback so the un-rewritten H2 renders solid `var(--color-3)` first (progressive enhancement, not gradient-first). NOTE: pixel-approved-rendering rule — ship behind an owner visual diff.
2. **Anchor the trust row (MC-2):** pattern "5,0 av 5 · {N} omdömen på Google" with owner-confirmed current rating + count (same anchor already used by MainContact/Testimonials). If count can't be confirmed, drop the number and keep "Betyg på Google ★★★★★" linked.
3. **Verify or replace the 60-second promise (MC-3):** either owner confirms average time-to-human < 60 s during öppettider (then keep and add the qualifier, e.g. "vardagar 07–17"), or shift to a verifiable pattern: "Prata direkt med en elektriker — vi svarar när du ringer" / call-answering fact Ampy can stand behind.
4. **Make MainCTA the ONE canonical phone band (MC-4):** define roles — MainCTA = early phone moment after first proof (keep); BlueCTA = retire or re-job (e.g. öppettider/eljour-specific band) — cross-reference the BlueCTA audit. Do not add a form link to MainCTA; its single-ask discipline is its value.
5. **Geo/intent copy pass (MC-5):** fix "auktoriserad→auktoriserade" across geo templates; give laddbox-i and eljour-i their own H2 pattern (eljour: urgency-true phone framing; laddbox: "prata med en laddboxinstallatör"-direction) via the existing ACF field — zero structural change.
6. **Consolidate the two CSS layers (MC-6)** into one owned stylesheet and consider naming the pictured electrician (E-E-A-T + Cialdini liking) — backlog.

## Test hypotheses
- HYPOTES: Anchoring the rating ("5,0 av 5 · N omdömen") vs bare "5.0 på Google" increases tel: click-through on the block on geo pages (measurable via per-block call-click event).
- HYPOTES: An intent-matched H2 on laddbox-i/eljour-i vs the generic electrician line increases block-level engagement + calls (message match).
- HYPOTES: Retiring BlueCTA on pages that carry MainCTA does not reduce total calls (redundancy test — validates consolidation).

## Priority score (arithmetic)
- Pages affected: **268**
- Funnel position weight: mid-page CTA = **2**
- Expected effect: medium = **2** (the block already works; fixes are legibility + trust-claim integrity + copy, not structure)
- **Priority score = 268 × 2 × 2 = 1072 → P1** (contrast + unanchored/unverified claims are trust-touching on 268 pages; fix in month 1. MC-4 consolidation is P2 pending the BlueCTA audit; MC-6 is P3.)
