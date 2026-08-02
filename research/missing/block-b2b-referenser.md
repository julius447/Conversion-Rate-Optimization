# Org-referenser & serviceavtal-blocket (B2B proof + long-cycle ask)

**Status: BUILD-GATED — the block design is validated; the proof it needs does not exist yet. Ships in two states: interim (now) and full (after owner collection). The separately-floated "org-trust strip" is NOT here — it merged into block-trust-strip.md (B2B claim set).**

## Job-to-be-done
Give the 11 B2B/BRF/public-sector pages (bostadsrattsforening, foretag, kontor, butik, restauranger, hotell, idrottshallar, kommuner, byggforetag, entreprenad, tredjepartsinstallationer) proof that resembles the buyer — and an ask that matches procurement pace. Today these pages open with "Vad säger dina **grannar** om Ampy?" + 12 private-villa reviews (zero from any BRF/förvaltare/company), the footer asserts "Framtidens elfirma **för privatpersoner**", and no referenser/ramavtal/serviceavtal block exists anywhere (EFX-01 P0, EFX-02 P0 — the template's highest score). /bostadsrattsforening/ already pulls 546 impressions (GSC) — pre-positioning matters.

## Anatomy (in words)
**Element 1 — Referenser/case-rader (the proof):**
- **Eyebrow:** "Referenser". **Headline:** "Uppdrag för föreningar och företag".
- 2–3 case rows: kundtyp + uppdragstyp + omfattning + one factual outcome line ("BRF, 90 lägenheter — laddboxar på 24 p-platser med lastbalansering, klart på 3 veckor") + kontaktbar referens where permitted. NO invented quotes.
- **INTERIM STATE (until real B2B proof exists):** re-headed testimonials — "Vad säger våra kunder" (drop "grannar"), org-plausible quotes sorted first, PLUS the TrustStrip B2B claim set carrying the verifiable org proof (ID06, Trygg Hansa, Elsäkerhetsverket). The interim state invents nothing and claims nothing org-specific.
**Element 2 — Serviceavtal/ramavtal-kortet (the ask):**
- **Headline:** "Vill ni ha en långsiktig elpartner?" — one card naming the offer (serviceavtal, ramavtal, LOU-vana for kommuner via ACF), 2–3 bullet what-you-get lines (dokumentation, fasta kontaktvägar, årlig elbesiktning), and ONE lower-commitment CTA: "Boka ett avtalsmöte" → the org-adapted form (kundtyp prefilled via the existing EFX resolver — the resolver already does orgLabel "Föreningens namn"/"Förvaltning eller enhet", the template's best asset).

## Templates + position
The 11 B2B pages (org variant of elektriker-för-X): Element 1 at the decision point (EFX wireframe slot 6, replacing the consumer testimonial slot); Element 2 before MainContact (slot 8). Consumer pages (villor, radhus) keep the "grannar" testimonials — there it is *right*.

## Why it beats status quo
Cialdini similarity: proof persuades when the prover resembles the prospect — a kommun upphandlare reading villa reviews reads "wrong supplier". JTBD: the board's job is *defend this choice to members/colleagues* — that requires org-shaped, documentable proof, not stars. The serviceavtal ask fixes the pace mismatch: "Prata med en elektriker inom 60 sekunder!" is consumer-urgency framing aimed at a buyer running a shortlist process; a named long-cycle offer is the ask that matches how these 11 audiences buy (EFX-11).

**Adversarial note — the empty-proof trap:** the strongest temptation here is to fake it (generic "våra företagskunder älskar oss" copy, stock logos). That fails the candour gate and the procurement reader's sniff test simultaneously — this segment runs due diligence for a living. Ruling: the block ships in the interim state with zero org claims until the owner delivers ≥2 real references; the FULL state is explicitly blocked on collection. Named trade-off: the interim state is materially weaker — accepted, because invented B2B proof is the one candour breach that could cost a ramavtal shortlist spot permanently.

## Candour-gate check
INTERIM: PASS (re-heading + sorting invents nothing; TrustStrip claims are externally verifiable). FULL: PASS only with owner-collected, permission-cleared references [GAP: no B2B/BRF reviews or named references exist in the current proof pool — start collection now: BRF chair quotes, company serviceavtal references, GBP review drive at B2B job completion]. Footer tagline "för privatpersoner" must get the org variant in the same sprint (EFX-01) or the block contradicts its own page.

## Effort & priority
- **Effort: M** (interim S: re-head + sort + TrustStrip wiring; full M: case-row component + collected content; serviceavtal card S).
- **Priority arithmetic:** 11 pages × 2 (mid-funnel decision zone) × 3 (high — the template's two P0s, EFX-01/-02, both resolve here) = **66**. Modest reach but B2B deal sizes are multiples of the ~3 500 kr service job, and /bostadsrattsforening/ has real search demand building. → **P1 interim (month 1), P2 full (months 2–3, gated on collection).**

## Dependencies
1. Owner reference-collection program (the blocking [GAP] — start week 1, ships whenever ready).
2. TrustStrip B2B claim set (block-trust-strip.md).
3. MainContact org-variant (EFX-04 — orgnamn + kontaktperson via the existing resolver) so the avtalsmöte CTA lands on a fit-to-task form.
4. Footer org-tagline variant (EFX-01).
