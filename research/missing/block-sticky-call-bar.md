# Sticky mobil ring-rad (fixed bottom call-bar)

**Status: BUILD (eljour committed; geo + articles as gated A/B). The "jour-status/öppet-indicator" candidate is KILLED as a standalone block and folded in here as a chip.**

## Job-to-be-done
Keep the call — the only conversion that demonstrably works today (GA4: 2 phone clicks, 0 form starts from paid) — one thumb-reach away through long mobile scrolls, on the templates where the visitor's JTBD is call-shaped. Mobile is the primary rendering (53 % of organic clicks, higher on paid/local); pages run 14–22 blocks with no persistent affordance.

Evidence chain: GEO-ELJ-05 (P1 — "the single highest-leverage mechanical fix on the template": the shipped eljour symptom-block CSS contains **zero** sticky/fixed rules; the owned v3 block spec at julius447/Eljour-block already includes the fixed mobile call-bar, and the standalone /ampy-eljour/ magnet ships one with 26 sticky/fixed rules — the pattern is proven in-house), ART-05 (44 — 17-minute mobile reads with literally no visible conversion affordance after the header scrolls away), GEO-10 (672 if the test wins), HDR-01 B-variant (sticky bottom bar as alternative to header phone icon).

## Anatomy (in words)
- **Bar:** fixed bottom, safe-area-inset aware, ≤56 px tall, light surface with teal accent (token-bound; not a dark slab).
- **Left element — status chip (eljour variant only):** small pulse dot + "Jour öppen just nu" — folded in from the killed standalone candidate. Candour basis: consistent with the published "Jour dygnet runt, året om" (LM-12 recorded PASS on this exact copy) — it states standing coverage, not fake live-status.
- **Primary:** "Ring 010-265 79 79" (tel:, full E.164, min 44 px tap target — Fitts).
- **Secondary (non-eljour variants):** "Få prisförslag" → anchor-scroll to the on-page form (never /kontakt/).
- **Behavior:** eljour = always visible on mobile; geo/service = visible after first scroll; articles = appears at ≥40 % scroll depth, **dismissible** (ART-05 guardrail: dismiss rate <40 %, no drop in read completion).
- Emits `sticky_bar_view` / `sticky_bar_call` / `sticky_bar_form` / `sticky_bar_dismiss` events.

## Templates + position
| Variant | Templates | Pages | Mode |
|---|---|---|---|
| Eljour (committed) | eljour-i + /eljour/ pillar + /ampy-eljour/ parity | 57 | always-on mobile; port of the owned v3 spec |
| Geo/service (A/B) | elektriker-i, elinstallation-i, laddbox-i, service | 190 | test after the CTA-retarget + SSR-form tests (geo template's own backlog note: run 4th to avoid interaction effects) |
| Articles (A/B) | post | 11 | ≥40 % scroll, dismissible, "Ring · Få prisförslag" |

## Why it beats status quo
Fitts's law: during symptom-triage or a 3 900-word read, the conversion action should be permanently one thumb-reach away; today the per-panel tel links partially compensate on eljour (22 scattered tel links) and articles have **zero**. Unbounce: urgent/repair intent converts on the call. The eljour case needs no test — it restores an owner-approved spec that was dropped in shipping.

**Adversarial resolution — collision with the header phone fix (HDR-01, score 2 925):** if the header gets a persistent phone icon AND the bottom bar ships, mobile carries two chrome-level call affordances. Ruling: they serve different scroll states — header icon covers arrival/top, bottom bar covers deep-scroll — but ship **header first sitewide** (cheaper, zero content risk), then bottom-bar variants per template where depth is the problem. On eljour both are justified (emergency intent tolerates redundancy in the call path; it tolerates none in the form path). Do not ship the bar on pages where it would cover the MainContact submit button — suppress while a form is in viewport.

## Candour-gate check
PASS with one rule: the status chip may claim only standing coverage ("Jour öppen just nu" backed by dygnet-runt service). If jour coverage has any gap, the chip is a candour breach and must reflect the truth [GAP: owner confirms 24/7/365 staffing]. No countdowns, no "3 personer tittar just nu"-class inventions.

## Effort & priority
- **Effort: S** (eljour: CSS port of the owned v3 spec — but **owner-gated visual diff per the approved-rendering rule**); geo/articles variants S–M each.
- **Priority arithmetic:** eljour 57 × 3 (persistent conversion affordance) × 3 = **513** (committed). Geo upside 190 × 3 × 2 = 1 140 (gated on test). Articles 11 × 2 × 2 = 44. → **P1, month 1 (eljour); tests months 2–3.**

## Dependencies
1. Owner visual-diff sign-off (approved-rendering-is-canon; activating previously-inert sticky CSS = owner-gated).
2. tel-click instrumentation already works (the 2 recorded clicks prove it) — add the bar-specific events.
3. Header phone fix (HDR-01) sequenced first; then measure incrementality of the bar, not the pair.
