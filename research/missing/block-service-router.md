# ServiceRouter + ProduktTeaser (homepage mid-section rebuild)

**Status: BUILD — two blocks that ship as ONE intervention; they replace MiniMenu + ProductGrid×2 + BlueCTA + ServiceGrid on the homepage.**

## Job-to-be-done
**ServiceRouter:** give the mixed-intent homepage visitor ONE decision surface, directly after the hero, ordered by the owner's commercial priority (service > laddbox > battery) — instead of today's two routers (MiniMenu at slot 3, ServiceGrid at slot 8) separated by ~8 mobile viewports of battery/laddbox webshop whose first visible prices are 33 000–36 250 kr (a 10× anchor against the ~3 500 kr service job the majority visitor needs).
**ProduktTeaser:** preserve laddbox/battery discovery + the Grön Teknik hook below the conversion layer with two compact price-anchored cards, so removing the 8-card grids doesn't amputate priority #2.

Evidence chain: HP-01 (P0, 9 — commercial-priority inversion + hostile price anchor), HP-02 (P0, 9 — 8 outbound product exits above all proof), HP-13 (6 — split routers force the "elcentral" scanner to traverse the shop), HP-12 (grid removal is also the speed fix), F5 (MiniMenu equal cards contradict priority; Laddbox card routes to the product list, not the service funnel), GSC (homepage = ~89 % of organic clicks; brand-verifier funnel role).

## Anatomy (in words)
**ServiceRouter (slot 3, after hero):**
- Eyebrow: none needed. **Headline:** keeps the ROT hook — "Vårt utbud av elinstallationer – installerat & klart med 30 % ROT-avdrag" (existing H2, SEO preserved).
- **Row 1 — services (priority #1):** 6 cards ordered by demand/urgency: Felsökning & Eljour first, then Elcentral, Belysning, Kök & Badrum, Smarta hem, + "Alla tjänster →" to /elservice/. Descriptive link labels ("Till Belysning" pattern — already the best link copy on the site, HP-11). All existing /elservice/* internal links preserved or strengthened (SEO rule: re-sequence, never delete).
- **Row 2 — two slim category cards:** Laddbox → /laddbox/ (the *service funnel*, not /laddboxar/ — F5's routing catch) and Batterilagring → /batterilagring/. Visually subordinate to row 1 (no equal-thirds billing, F5).
**ProduktTeaser (slot 7, below testimonials/process/CTA layer):**
- **Headline:** "Laddbox och batterilagring — installerat & klart med 50 % Grön Teknik-avdrag".
- Two compact cards, laddbox FIRST: "Laddbox fr. 4 190 kr efter avdrag" → /laddboxar/; "Batterilagring fr. 33 000 kr efter avdrag" → /batterilagring/ (canonical fr.-prices pending the GEO-09/PP-01 reconciliation). One "Jämför alla →" link each. No BÄSTSÄLJARE/SUPERKAMPANJ tags (candour ⚑ PP-11), no spec chips.

## Templates + position
Homepage only (1 page — but the highest-traffic URL: 295 of 333 organic clicks, and the verification step of the warm brand funnel). ServiceRouter slot 3; ProduktTeaser slot 7 per the homepage primary wireframe. The full product grids live on /laddboxar/ + /batterilagring/ where purchase intent goes — nothing is deleted, content relocates to pages that already carry it verbatim.

## Why it beats status quo
Hick's law: one decision surface beats two staggered ones; information scent: the majority intent (service) currently sits at position 8 below two product grids it outranks in owner priority. Jakob's law: the e-commerce card grammar (tags, Fr.-prices, Läs mer ×8) reframes an elfirma as a webshop for the exact audience that needs a tradesperson. Removing ~8 heavy product cards from the pre-fold-adjacent zone is simultaneously the biggest homepage speed win (HP-12, 723 kB HTML / 9–10 s lab LCP).

**Adversarial resolution — the internal redundancy in the team's own wireframe:** the proposed ServiceRouter row 2 AND the ProduktTeaser both carry Laddbox+Batterilagring — the same two categories twice on one page. Ruling: keep both at launch because the jobs differ (row 2 = routing for visitors who arrived product-minded; teaser = price-anchored discovery for service visitors who scrolled past) — but this is a named test: if scroll/click data shows the pair cannibalizing, **drop ServiceRouter row 2 first** (the teaser carries the prices and the Grön Teknik hook; the router must stay service-pure). Second trade-off: owner's floated sequence deleted ServiceGrid entirely — rejected (it is the homepage's internal-linking hub into /elservice/*; killing it trades conversion for an SEO wound).

## Candour-gate check
PASS: ROT/Grön Teknik rates are canon; fr.-prices must be the reconciled canonical figures with the "efter avdrag, standardinstallation" caveat (never bare); commercial tags (SUPERKAMPANJ) excluded pending owner substantiation. No urgency devices.

## Effort & priority
- **Effort: M** (homepage rebuild of slots 3–7; components mostly recomposed from existing card patterns). Owner-gated: homepage hero/design is approved canon — this touches blocks BELOW the locked hero only.
- **Priority arithmetic:** 1 page × 3 (hero-adjacent routing layer) × 3 (high — removes the two P0s HP-01/HP-02) = **9** nominal — but weight by traffic: this one page carries ~89 % of organic clicks and every brand-verification session; treat as **P0-by-traffic, month 1**. House rule satisfied: the "Jobb-först" divergent homepage (hero job-picker chips + form at slot 5) stays on file as the big-intervention alternative — run as a later test, not the default.

## Dependencies
1. Price reconciliation (canonical fr.-prices) before the teaser ships.
2. Hero CTA retarget to `#radgivning` (HP-03) ships in the same edit.
3. Testimonials badge anchoring (HP-04) so the proof layer the router hands visitors to is candour-clean.
