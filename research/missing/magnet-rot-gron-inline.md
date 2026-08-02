# ROT/Grön Teknik-miniräknaren (inline avdrag-widget) — verdict: MERGE, do not build standalone

**Status: MERGED into the Pris & offert block (research/missing/block-pris-offert.md). No standalone magnet.**

## The candidate
An inline mini-calculator ("skriv in arbetskostnad → se ditt ROT 30 % / Grön Teknik 50 % avdrag i kronor") embeddable on service pages, incentive blocks and articles.

## Adversarial evaluation — why standalone loses
1. **The slot is already taken by a cheaper fix.** The Pris & offert block (the program's #1 new block, score 1 206–2 223, P0) already specifies Element 3: an avdrag micro-row "with a worked kr example where data exists… dras direkt på fakturan". A static worked example ("Arbetskostnad 10 000 kr → du betalar 7 000 kr efter ROT") delivers ~all of the comprehension value at zero interaction cost, zero JS, zero LCP risk — on a site whose 9–10 s lab LCP is a standing P0-class problem. Adding an interactive widget to the hero-adjacent zone works *against* the speed program.
2. **Interaction adds friction where none is needed.** MECLABS: the incentive term needs to be SEEN before the ask; it does not need to be computed by the visitor. The deduction math is one multiplication — an input field asks the visitor to do work to learn what one sentence can tell them. (Contrast the real calculators, which compute things the visitor genuinely cannot: consumption, payback, lastbalansering.)
3. **Candour risk of false precision.** A widget outputting "ditt avdrag: 3 000 kr" invites treating it as an offer; ROT/grön-teknik eligibility has per-person caps (50 000 kr grön teknik cap, ROT rules) and eligibility conditions (fastighetsägare, tax room — "Vid avslag … faktureras det återstående beloppet" per the product popup). A one-line worked example with the "exakt i offerten" caveat is more honest than an interactive number generator.
4. **It would be the program's third avdrag surface** (ROT block, GrönTeknik block, Pris & offert Element 3) — the same fragmentation anti-pattern the TrustStrip and Verktygs-tile consolidations exist to prevent.

## What survives (folded into existing workstreams)
- **Pris & offert block Element 3** carries the worked kr example per vertical (already specced; this file adds nothing to build).
- **Energikalkylatorn/Laddboxkalkylatorn already show efter-avdrag results** — the interactive avdrag experience exists inside the real calculators where it belongs.
- **IF a future A/B shows the static worked example underperforms** (HYPOTES below), the upgrade path is a slider inside the Pris & offert block — an enhancement ticket on that block, never a separate magnet.

## Priority arithmetic
Standalone incremental value over the merged solution: ~0 at effort M. → **MERGE. No build.**

## Test hypothesis (the reopening condition)
**HYPOTES:** In the Pris & offert block, a static worked avdrag example vs. an interactive avdrag slider produce equal lift in combined conversions; if the slider wins by a meaningful margin AND does not degrade LCP, promote the slider into the block spec. Until that test exists, the static row ships.
