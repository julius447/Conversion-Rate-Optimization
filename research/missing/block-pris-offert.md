# Pris & offert-blocket ("Vad kostar det?")

**Status: BUILD — the single highest-leverage new block in the program (THE message-match fix).**

## Job-to-be-done
Answer the visitor's #1 question — *vad kostar det, och blir jag lurad på priset?* — on screen 1–2 instead of at 70–80 % scroll depth, and re-affirm the SERP/ad promise ("fast pris", "byta elcentral pris") that today is broken on arrival. The Swedish homeowner's documented top anxiety is final-price surprise (Byggahus/Konsumentverket anchor); the paid queries are price-loaded; the answers already exist on the pages — inside collapsed FAQs at positions 8–16.

Evidence chain (all verified in phase 1–2): SVC-02 (score 198 — "byta elcentral pris" lands on a page with no visible price; the answer "6 000–12 000 kr efter ROT" sits in FAQ block 8), GEO-03 (score 504 — title tag promises "fast pris", body contains the phrase **0 times**), GEO-ELJ-07 (eljour promises "Tydligt pris innan vi rycker ut" but prints no number in 2 800 words), PIL findings (FAQ price candour "600–900 kr/tim efter ROT" buried at 70–80 % depth on every pillar), GEO-09 (laddbox grid "Fr. 4 190 kr" vs FAQ "från ca 5 000 kr" — internal contradiction).

## Anatomy (in words)
- **Eyebrow:** "Vad kostar det?"
- **Headline:** per-vertical price statement — pattern direction (final Swedish via ampy-rost): "Byta elcentral: vanligtvis 6 000–12 000 kr efter ROT-avdrag" / "Elektriker: 650–950 kr/timme efter ROT + startavgift för servicebil".
- **Element 1 — the range row:** the real, already-published range (from the page's own FAQ / ampy-foretagsdata), stated with its basis ("efter 30 % ROT på arbetskostnaden").
- **Element 2 — the promise row:** "Fast pris i offerten innan arbetet påbörjas — inga överraskningar på fakturan." (the Konsumentverket written-quote norm, made explicit).
- **Element 3 — avdrag micro-row:** one line ROT 30 %/Grön Teknik 50 % with a worked kr example where data exists (per INC-03 direction), "dras direkt på fakturan".
- **Element 4 — micro-CTA:** one text-link/button "Få ditt exakta pris →" anchor-scrolling to the on-page form (never /kontakt/ — GEO-01 class fix). No second ask.
- Light surface (white/#f5f9ff card), compact: ≤1 mobile viewport. NOT a dark band — it must read as information, not sell.

## Templates + position
| Template | Pages | Position | Content source |
|---|---|---|---|
| service (/elservice/*) | 22 | directly under Hero_2 (slot 3, per service-pages wireframe) | existing FAQ price answers; vitvaror-class pages need a new price FAQ first (SVC-02) |
| elektriker-i | 56 | under hero/trust strip | pillar FAQ "600–900 kr/tim efter ROT" |
| elinstallation-i | 56 | under hero | own FAQ "650–950 kr/tim efter ROT + startavgift" |
| laddbox-i | 56 | folded into the ProductGrid caveat line + FAQ (grid already price-anchors) | **gated on reconciling 4 190 vs "från ca 5 000" (GEO-09)** |
| eljour-i + /eljour/ | 57 | replaces the mis-wired ROT block slot (pairs with Hemförsäkring variant) | **[GAP: owner price card — fast inställelseavgift dag/kväll/helg]** |
| pillars (elektriker/elinstallation) | 2 | slot 4 "signature device" per pillar wireframe | pillar FAQs |

## Why it beats status quo
Status quo = the price answer exists but arrives after the visitor has decided to bounce (MECLABS HealthSpire: sequencing, not length, is the variable; Google message match: ad → H1 → **first screen** is mandatory). The block is 90 % repackaging of live copy — the cheapest possible way to close the #1 message-match gap. It also converts the "fast pris" SERP titles from a candour breach (GEO-03: page retracts what the snippet asserts) into a kept promise.

**Adversarial note — the sticker-shock objection:** showing 6 000–12 000 kr up front will scare off some low-intent visitors. Named trade-off: those visitors do not convert at ~2 660 kr täckningsbidrag economics anyway; price-qualified leads close at 50–75 %. Byggahus evidence says omission, not the number, is what kills trust. Run as HYPOTES (service-pages test #2) with call+form combined as primary metric and pogo-sticking as secondary.

## Candour-gate check
PASS with conditions: every number must come from already-published owner copy or ampy-foretagsdata — never invented; internal contradictions (laddbox 4 190/5 000; elcentral hero "Totalt" vs FAQ range on products) must be reconciled BEFORE rollout, or the block amplifies the contradiction it exists to kill; eljour variant ships only when the owner supplies the real inställelseavgift ([GAP]). "Fast pris i offerten" is only claimable where offerts genuinely are fixed — the /elinstallation/ legacy "Alltid fasta priser" vs "600–900 kr/timme" collision (PIL-08) shows what happens otherwise. No urgency, no discount framing.

## Effort & priority
- **Effort: S–M.** One ACF-driven Bricks component; per-page content = mostly copy relocation. Eljour variant M (needs owner data).
- **Priority arithmetic:** immediate rollout (service 22 + elektriker-i 56 + elinstallation-i 56 = 134 pages, content exists) × 3 (hero-adjacent) × 3 (high — message-match on paid landing zone) = **1 206**. Full rollout incl. laddbox-i + eljour (247 pages) = 247 × 3 × 3 = **2 223**. → **P0, weeks 1–4.**

## Dependencies
1. Price-contradiction reconciliation pass (PP-01, GEO-09) — owner locks one canonical figure per vertical.
2. Eljour price card [GAP] (also unblocks two-lane contact + eljour Hemförsäkring block).
3. Anchor-scroll targets on forms (`#main-contact` / hero form id) — ships with the GEO-01/CTA-01 retargeting fix.
4. ampy-rost final copy pass (candour register, no "!"-inflation).
