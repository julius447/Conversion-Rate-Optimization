# Två-filers kontakt (Akut? Ring / Kan det vänta? Bli uppringd) — eljour MainContact-variant

**Status: BUILD — validated; the fix for the worst internal contradiction on the highest-converting intent class.**

## Job-to-be-done
Give the eljour visitor an honest fork at the decision point: the acute majority converts on the call; the legitimate non-urgent minority (säkringen löste ut igår; BRF board documenting an issue at 23:00; the visitor who won't phone) gets a form whose promise doesn't insult the emergency framing. Today the generic MainContact runs unmodified on all 57 eljour pages and promises **"Vi ringer dig inom 24 timmar"** directly under a hero claiming "Målsättning att vara på plats inom en timme" and a MainCTA shouting "inom 60 sekunder" — three colliding response promises on one emergency page (GEO-ELJ-03, P0; PIL-03d).

Evidence chain: GEO-ELJ-03 (SLA whiplash, P0), GEO-ELJ-12 (7–8-field form unfit for the template's secondary audience), MC-05 (on all 56 eljour geo pages MainContact sits after 10 blocks), Unbounce benchmark (urgent/repair pages are the top conversion opportunity *when the page commits to the urgent job*), geo-eljour wireframe slot 9 (this block, specced).

## Anatomy (in words)
Two-pane card (MainContact shell reused — familiar surface, new logic):
- **Left lane — "Akut just nu?"** Giant single Ring CTA ("Ring eljouren 010-265 79 79"), the jour-status chip, and 2 trust bullets from the symptom block's proven set ("Prata med en behörig elektriker, inte en växel" / "Tydligt pris innan vi rycker ut"). No form. No 60-second claim unless owner-verified.
- **Right lane — "Kan det vänta till imorgon?"** Eyebrow "Bli uppringd", MiniForm (namn + telefon + valfritt meddelande — postnr prefilled from the geo page's ort), promise line with the ONE owner-confirmed callback SLA for this lane ("Vi ringer dig i morgon bitti före [GAP: tid]" or the verified equivalent). Framing makes the 24h-class promise *correct* because the visitor has self-declared non-urgency.
- **Mobile:** lanes stack, Akut lane first; sticky call-bar (separate block) covers the deep-scroll case.

## Templates + position
eljour-i (56) + /eljour/ pillar (1) = **57 pages**, replacing the generic MainContact instance (slot 9 of the eljour wireframe, after FAQ/testimonials). The generic MainContact is NOT deleted sitewide — this is a template-scoped variant.

## Why it beats status quo
MECLABS: for max-motivation urgent visitors the binding constraint is friction+anxiety, not motivation — the current page defers them into a quote form ("återkommer via telefon" = callback framing, GEO-ELJ-01). The fork resolves the SLA contradiction *structurally*: each promise attaches to the lane where it is true. It preserves the form path (two-conversion doctrine) without cannibalizing calls — and it is the honest version of urgency: severity self-selection instead of manufactured pressure.

**Adversarial note — why not just delete the form from eljour pages?** The call-first purist position (service-pages divergent wireframe) argues no form at all on urgent intents. Rejected for eljour geo pages: night-time visitors with non-acute faults are real (the symptom block's Varning tier exists precisely for them), BRF/company reporters need a written lane, and the form is the only path when calling is socially impossible (22:30 in a lägenhet). Trade-off named: the two-lane layout costs one extra decision (Hick) — accepted because the decision (akut eller inte?) is one the visitor has already made.

## Candour-gate check
PASS only with owner inputs: the right-lane callback SLA must be the real one ([GAP: verklig kvälls-/natt-callback-rutin]); "inom 60 sekunder" dies on this template unless verified; jour-status chip per the sticky-bar rules. The lane labels must not dramatize ("Akut just nu?" is descriptive, not fear-injected — fear is one tool, not the house style).

## Effort & priority
- **Effort: M** (MainContact variant + MiniForm dependency + copy via ampy-rost).
- **Priority arithmetic:** 57 pages × 3 (form/decision block) × 2 (medium-high — phone already works; this fixes the form lane + kills a P0 trust contradiction) = **342**. → **P1, month 1** (the copy-level SLA contradiction can be hotfixed in week 1 by removing "60 sekunder"/"24 timmar" collisions even before the block ships).

## Dependencies
1. Owner jour-SLA truth [GAP] — the single blocking input.
2. MiniForm component (block-mini-form.md).
3. Coordinates with: eljour hero phone-primary variant (PIL-03/GEO-ELJ-01 fix), sticky call-bar, Hemförsäkring block CTA fix (INC-01).
