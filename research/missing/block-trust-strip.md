# Verifieringsraden (TrustStrip) — one component, four formats

**Status: BUILD — merges THREE overlapping candidates into one component family.**
The team surfaced "Elsäkerhetsverket authority/verification strip", "compact trust strip" and "org-trust strip (B2B)" as separate blocks. Adversarial resolution: they are the **same component with different claim sets**. Building three near-identical strips would recreate the CTA-band problem this audit just diagnosed (three bands, one job — CTA-02). One component, ACF-driven claims, four formats.

## Job-to-be-done
Put the *verifiable* proof a serious Swedish customer actually checks — Elsäkerhetsverket registration, insurance, anchored Google rating — **adjacent to the ask**, instead of 6–12 blocks below it. The site's strongest trust asset already exists: the Certificates block's Elsäkerhetsverket logo links straight into the government registry **with Ampy's record pre-queried** (`?foretag=12047521`) — but it renders as a 49×49 px anonymous logo, third block from the footer, `alt=""`, on 290 pages (CERT-01). The Clarity 47 s "Kontakt → Om oss" recording is direct behavioral evidence of unmet trust-seeking at the decision point.

Evidence chain: CERT-01/-02 + recommendation A (verification-strip promotion scored **1 740**), SVC-05 (proof architecture inverted, 132), GEO-11 (authority buried at position 17), EFX-02 (B2B: no org-level proof until position 12, score 99 — highest of that template), FTR-02 (footer asserts nothing verifiable), KO-6/OM-2 (kontakt/om-oss lack the verification artifacts), MET-04 (HYPOTES: verifiable authority claim beats "25+" on form submits).

## Anatomy (in words) — four formats
**Format A — Strip (one row, hero/form-adjacent):**
- No eyebrow/headline — it IS a row. 2–4 claim chips, each icon + one line:
  1. Elsäkerhetsverket mark + "Registrerat elinstallationsföretag — kontrollera oss själv" → the existing `?foretag=12047521` registry link.
  2. Anchored rating: "5,0 av 5 · N recensioner på Google" (linked GBP). **N = owner-confirmed [GAP]; without N this chip does not ship.**
  3. "Ansvarsförsäkrade via Trygg Hansa" ([GAP: policy current]).
  4. Optional per-template slot: "30 % ROT direkt på fakturan" (service) / "Vi ringer inom 24 timmar" (if owner-confirmed SLA).
- **A-eljour claim set:** "Målsättning: på plats inom 1h" · "Dygnet runt, året om" · anchored rating · Elsäkerhetsverket (per geo-eljour wireframe slot 4 — replaces the off-JTBD Metrics trio).
- **A-B2B claim set (the org-trust strip):** ID06-anslutna · Trygg Hansa-försäkrade · Elsäkerhetsverket-registrerade · "3 000+ installationer/år" (if confirmed) — under the hero on the 11 B2B pages (EFX-02).
**Format B — Form-adjacent micro-strip:** one line under the Hero_2 GDPR row / inside MainContact's left pane: Elsäkerhetsverket line + Trygg Hansa (CERT recommendation A verbatim).
**Format C — Företagsfakta-kortet (kontakt/om-oss):** small card — besöksadress Västbergavägen 25, org.nr, öppettider [GAP], "Kontrollera vår auktorisation hos Elsäkerhetsverket" link, e-post/tel. Completes the Swedish verification ritual on-page and removes the reason for the Kontakt→Om oss detour (KO-6, OM-2).
**Format D — Footer legal-trust row:** org.nr + F-skatt + Elsäkerhetsverket check link + anchored rating, above the © bar on 325 pages (FTR-02).

## Templates + position
| Format | Where | Pages |
|---|---|---|
| A | under hero on service (slot 4), elektriker-i/elinstallation-i/laddbox-i (slot 3 "TrustStrip" in both geo wireframes), eljour (slot 4, jour claim set), B2B ×11 | ~250 |
| B | inside Hero_2 form card + MainContact pane | 260 / 295 |
| C | /kontakt/, /om-oss/ | 2 |
| D | global footer | 325 |

## Why it beats status quo
The proof already exists on 290 pages at ~90 % scroll depth as anonymous wallpaper. MECLABS: the −2a anxiety term is evaluated **at the form**, not at the footer; Cialdini authority requires the authority be *legible*. Inviting self-verification in a government register is a costly, falsifiable signal — candour-native, the exact opposite of the unanchored "5.0" epidemic (which appears 4–6×/page with no count, SVC-06/GEO-07/PIL-06). This block also becomes the delivery vehicle for the sitewide rating-anchoring fix: one canonical anchored badge, reused, replacing bare "5.0"s.

**Adversarial note — sameness risk:** a single strip on ~250 pages risks banner-blindness and deepens the geo doorway-sameness problem. Resolution: per-template claim sets (already specced above) + the strip stays SMALL (one row) so it reads as fact, not campaign. Second tension: Certificates wall stays where it is (bottom) — this is a *clone-to-decision-zone*, not a move; the wall gets its own in-place fix per the CERT audit.

## Candour-gate check
PASS by design — every chip is externally verifiable or it does not ship. Hard gates: rating count N [GAP owner]; Trygg Hansa + ID06 currency [GAP]; "3 000+ installationer/år" provenance [GAP — currently contradicts "1000+" Metrics on the same pages, MET-02: resolve the number canon FIRST]; jour SLA claims only per the owner's confirmed jour truth. No chip may assert what the register/GBP cannot back.

## Effort & priority
- **Effort: S** (component + claim sets; assets exist — Elsäkerhetsverket link, logos, GBP URL). Rollout M (per-template wiring).
- **Priority arithmetic (per CERT-A):** 290 pages × 3 (form-zone mount) × 2 (medium, honest prior, A/B-testable) = **1 740**. B2B increment: 11 × 3 × 3 = 99. → **P0-adjacent P1, weeks 2–4** (after the number-canon owner session).

## Dependencies
1. Owner number-canon session (rating + count, one installations figure, headcount) — MET-01/-02 fix is a prerequisite, or the strip inherits the contradiction.
2. `?foretag=12047521` resolves to Ampy Nordic AB's live record (verify once).
3. HYPOTES to run (from CERT-A): "Verification strip adjacent to the Hero_2 form increases form submits vs control."
