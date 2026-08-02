# Artikelns konverteringskit: inline micro-CTA + "Nästa steg"-slutkort

**Status: BUILD — two elements, one template edit, 11 posts. Fixes the only template family with a 0-affordance conversion path.**

## Job-to-be-done
Give the article reader — who the template spends 17 minutes convincing (motivation maxed, anxiety answered, MECLABS m/v/a all worked) — an offer to accept. Verified today: **0 in-body tel links, 0 styled CTA blocks**, one plain text link at word ~3 700, and the only styled card at the decision point asks the READER to do Ampy a favor (Google review) — the ask inversion (ART-03). On elbilsladdning-hemma-2026 (commercial vertical): 0 tel, 0 /kontakt/, 0 calculator links. These pages capture the exact paid queries ("byta elcentral pris") that produced 0 form leads.

Evidence chain: ART-01 (P0, 66), ART-03 (44), ART-04 (44 — calculator cross-sell absent), ART-06 (the photo-bedömning micro-offer buried as plain text), ART-02 (the two bare posts need the shell + a linked CTA at all).

## Anatomy (in words)
**Element A — inline micro-CTA (one per article, at ~25–35 % depth, after the first price table):**
- Article-width, visually quiet (light card, thin teal left stripe — NOT a dark Mikro_CTA band; reading flow must survive).
- Category-contextual via ACF:
  - elcentral cluster: the site's best buried offer, packaged — "Osäker på just ditt proppskåp? Skicka ett par bilder — kostnadsfri bedömning och prisförslag inom två arbetsdagar." + one light button (→ service-page form with bilder-disclosure open, or MiniForm inline).
  - laddbox cluster: "Räkna ut vad hemmaladdning sparar dig →" → Laddboxkalkylatorn.
  - rot/grön-teknik: "Vi sköter Skatteverket-administrationen — få offerten med avdraget förräknat" → form anchor; alt. Energikalkylatorn.
**Element B — "Nästa steg"-slutkort (replaces the review card's slot, after Summering, before FAQ):**
- **Headline:** "Nästa steg" / per-category variant. Three tiers: primary "Kostnadsfri rådgivning" (MiniForm inline or anchor to the article's MainContact if that test arm runs — never both), secondary "Ring 010-265 79 79" (tel:), tertiary contextual calculator/tool link.
- The Google-review card is NOT deleted — demoted below, reframed to actual customers ("Har vi hjälpt dig tidigare?"); the primary review ask lives on /thank-you/ + post-job email where customers are.
**Mobile companion:** the article sticky-bar variant (see block-sticky-call-bar) covers the mid-read state; Element A/B cover the decision points.

## Templates + position
All 11 posts (one template edit), + the 2 bare posts (rot-avdrag-2026, gron-teknik-2026) get it as part of their shell retrofit — those two are footer-linked from every page on the site and currently end in an UNLINKED "Kontakta oss…" sentence + a published "(ADD FAQ SECTION)" editor note (ART-02, week-1 fix regardless).

## Why it beats status quo
The template's own content argues Ampy's value prop ("den ärliga elektrikern är värd mer än den billigaste") and then offers no channel — the purest MECLABS motivation-without-channel case in the audit. The photo-bedömning offer is the lowest-friction, most candour-true ask on the site (zero fields perceived; directly answers the fixed-quote anxiety) and it matches an existing capability (Hero_2's bilder upload). Consultative register throughout — articles are mid-funnel; no urgency, no hard sell (the anti-sell candour content is the moat and must not be contaminated).

**Adversarial note — triple-ask risk:** Element A + Element B + (test arm) MainContact could recreate the CTA-proliferation disease on the one template that's currently clean of it. Ruling: hard cap of ONE inline CTA per article; if MainContact is added (article wireframe slot 9 test), Element B's primary button anchors down to it instead of carrying its own form. Reading-experience guardrails: scroll depth + time-on-page must not drop (ART hypothesis 1).

## Candour-gate check
PASS: the två-arbetsdagar promise must be operationally true [owner confirm]; ART-07's in-article field statistics ("8 av 10 villor…", "över 600 centralbyten") need provenance confirmation in the same editorial pass — the CTA kit must not sit on top of unverifiable numbers; review-ask demotion is itself a candour improvement (asking non-customers for reviews borders invented social proof).

## Effort & priority
- **Effort: S–M** (two ACF-driven components, one template; the 2 bare-post retrofits ride the existing ART-02 work).
- **Priority arithmetic:** 11 pages × 2 (mid-funnel) × 3 (high — from zero affordance to full path) = **66**. Low reach, but these are the pages that rank/land for the money queries, and the fix is one template edit. → **P1, month 1** (bare-post fixes week 1).

## Dependencies
1. MiniForm component (or anchor targets) — block-mini-form.md.
2. Owner confirm: 2-arbetsdagar photo-assessment SLA; field-stat provenance (ART-07).
3. Review-ask relocation to /thank-you/ (coordinates with block-tack-forberedelse.md).
