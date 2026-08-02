# Incentive blocks — ROT-block (`rot`) + Grön Teknik (`gron-teknik`) + Hemförsäkring-variant

**Used on: 277 of 326 pages (85%)** — verified from `data/block-map.json`:

| Variant | Pages | Categories | Position (verified) |
|---|---|---|---|
| ROT-block (30 %) | 193 | elektriker-i 56 · elinstallation-i 56 · eljour-i 56 · service 22 · pillars 3 (/elektriker/, /elinstallation/, /eljour/) | index 9–15 of ~18–22 blocks; mean depth **61 %** |
| Grön Teknik (50 %) | 84 | laddbox-i 56 · ev-product 16 · battery-product 10 · pillars 2 (/laddbox/, /batterilagring/) | product pages index 3–4 (~20 % depth); laddbox-i index 15 (~79 % depth) |
| Hemförsäkring twin | subsumed in ROT-block count | eljour pillar + all sampled eljour-i geo pages carry it (rendered with the same `rot__` classes) | eljour-i index 13, **after MainContact** |

**Funnel position:** mid-to-low page (weight 2). Zero pages carry both ROT and Grön Teknik simultaneously (verified: 0 co-occurrences).

**Structure (identical 4-part pattern in all three):** white card w/ blue overlay bg → gradient H2 ("Sänk din X kostnad genom 30 %/50 % …-avdrag") → 3 icon items (Samtal/Projektledning → Installation → Vi hanterar ansökan) → one "Läs mer om …" button exit. Live copy verified (anti-theatre):

- **elektriker/taby (live fetch):** "Sänk din elektriker kostnad genom 30% rot-avdrag" → "Projektledning med elektriker — Vår elektriker … räknar ut hur mycket du kan spara i ROT." → "Vi hanterar ansökan — … skickar in ROT ansökan till Skatteverket åt dig." → `[Läs mer om ROT-avdrag → /rot-avdrag-2026/]`
- **laddbox/nacka (live fetch):** "Sänk din laddbox kostnad genom 50% Grön Teknik-avdrag" → "Projektledning med expert — Vår experter går igenom ditt projekt …" → `[Läs mer om Grön Teknik-avdrag → /gron-teknik-2026/]`
- **eljour/akersberga (live fetch):** "Sänk kostnaden för din eljour i Åkersberga genom din hemförsäkring" → "Samtal med expert — Vår experter … förbereder allt underlag för försäkringbolaget" → "Underlag till ansökan — … skickar över underlaget till dig för din försäkringsansökan" → **`[Läs mer om ROT-avdrag → /rot-avdrag-2026/]`** ← wrong CTA on an insurance block.

## What it does well
- **The right argument exists at scale.** Reducing perceived price is the strongest lever for a price-uncertainty-averse Swedish homeowner (MECLABS `i` term: incentive offsets friction). 277 pages already have a dedicated cost-reduction block — this is an asset, not a liability.
- **Rates are canon-correct.** 30 % ROT and 50 % grön teknik match the owner-confirmed 2026 canon on every page sampled. No rate errors found.
- **The hemförsäkring third step is honest** ("skickar över underlaget till dig för din försäkringsansökan" — Ampy doesn't overclaim it files insurance claims). The ROT variant's "vi skickar in ansökan till Skatteverket åt dig" is factually how fakturamodellen works. Candour gate: PASS on claims.
- **Product-page placement of Grön Teknik is right:** index 3–4, adjacent to the price/testimonials zone where the 50 %-avdrag directly de-anchors the visible price.

## Issues

### INC-01 · **P0 · Mismatched CTA on the Hemförsäkring variant (57 eljour pages)**
Desktop + mobile identical. The block argues hemförsäkring, all three steps mention försäkringsbolaget/försäkringsansökan — and the button reads **"Läs mer om ROT-avdrag"** linking to `/rot-avdrag-2026/` (verified live on eljour/akersberga and the eljour pillar). The block inventory specs this twin **"with phone CTA instead"** — the live build deviates from its own spec. Message-match break (Google message-match principle applied intra-page) plus expectation violation (NN/g: link labels must predict destinations) on the site's highest-urgency intent (Unbounce: urgent/repair pages are the best converters — this is where a wrong off-ramp costs most). A distressed visitor with a sparking outlet who taps this lands in a ROT tax-rules article.

### INC-02 · **P1 · The "Läs mer" exit lands on a page with no form — a mid-funnel off-ramp on 277 pages**
Verified live: `/rot-avdrag-2026/` and `/gron-teknik-2026/` contain **no MainContact and no Hero_2 form** (checked fetched HTML: `main-contact` absent, `aof` absent); their only closes are a BlueCTA phone band + header. The visitor leaves a page with two forms (Hero_2 + MainContact) for a page with zero. At mean depth 61 % this button interrupts exactly the evaluation phase MECLABS says the incentive should be resolving in place. HealthSpire logic applies: the visitor's question ("vad betyder 30 % för mig?") should be answered **on** the money page, not via navigation. Desktop and mobile behave identically (same anchor).

### INC-03 · **P1 · 30 %/50 % comprehension failure — no kronor anywhere**
All three variants promise savings ("räknar ut hur mycket du kan spara") but never show a single kr figure, never state **what** the percentage applies to, and never mention the 50 000 kr cap. Two concrete comprehension defects:
- ROT is **30 % of arbetskostnaden only** — the heading "Sänk din elektriker kostnad genom 30% rot-avdrag" implies 30 % off the whole bill. For material-heavy jobs that overstates; precision risk that borders the candour gate (not a false claim, but an imprecise one Ampy's register should tighten).
- No worked example. Baymard/NN/g: users don't compute percentages; concrete numbers beat abstractions. A 55-year-old homeowner comparing quotes wants "byta elcentral: arbetskostnad ~X kr → du betalar ~Y kr efter ROT" — numbers must come from `ampy-foretagsdata` or be flagged `[GAP]`, never invented.

### INC-04 · **P1 · Placement after the main form on most templates — incentive arrives after the ask**
Verified sequences: elektriker/taby and elinstallation/taby put ROT-block at index 11 — after MainContact (7–8) and FAQ; eljour-i puts it at 13, directly after MainContact-card; laddbox-i puts Grön Teknik at 15 of 20, after MainContact **and** after BlueCTA. /elservice/elcentral/: ROT at index 12, after MainContact (9). MECLABS: the `i` term must offset friction **at or before** the point of decision — a cost-reduction argument below the form can't lift the form. Only the 26 product pages sequence it correctly (before the content/contact zone).

### INC-05 · **P1 · Template-level Swedish errors replicated across ~140+ pages — trust damage with the exact target audience**
Quoted verbatim from live/snapshot HTML: "**Vår experter**" (Grön Teknik on 84 pages + eljour variant), "**försäkringbolaget**" (missing s, eljour), särskrivningar in every heading: "**Sänk din elektriker kostnad**", "**Sänk din laddbox kostnad**", "**Sänk din jour kostnad**" (should be elektrikerkostnad/laddboxkostnad/jourkostnad), and the adjacent eljour MikroCTA "…hur Sveriges snabbast växande elfirma **kan dig** när du behöver akut eljour" (missing "hjälpa"). For a 35–65 Swedish homeowner, särskrivning and grammar slips in a money/tax context read as carelessness — precisely where Konsumentverket-style diligence signals matter (NN/g credibility heuristics). One template fix propagates everywhere.

### INC-06 · **P2 · Three-icon abstraction answers the wrong question**
The heading promises money; the three steps describe **paperwork logistics** (samtal → installation → ansökan). Process reassurance is valuable (it kills the "krånglig ansökan" objection — keep it), but the block never delivers the promised math, so it reads as decoration. Desktop and mobile ship **two icon `<img>`s per item** (`icon-desktop`/`icon-mobile` swapped at 767 px — verified CSS), doubling asset weight on a site already flagged for ~9–10 s lab LCP.

### INC-07 · **P2 · Mobile: a tall dead-scroll wall between the form and the next CTA**
Verified CSS: grid collapses to 1 column at ≤780 px (`grid-template-columns: 1fr`, `max-width: 80%`), gap inflates to `--apspace-3xl` at 480 px, with negative-margin hacks (`.rot__process-item { margin-top:-15px }`). Three stacked icon+heading+paragraph cells plus button ≈ 2–3 viewport heights of non-actionable scroll inserted mid-funnel on the primary rendering (mobile-first doctrine). Heading uses gradient text-fill (`-webkit-text-fill-color: transparent`) — rendering-risk on older Android WebViews used by this demographic.

### INC-08 · **P3 · Coverage inconsistency**
/elservice/ — the pillar for the **#1 commercial priority (service)** — carries neither variant, while its 22 subpages all carry ROT. The service money page is the one place the ROT argument is missing.

## Recommended changes (concrete)

1. **(P0, ~1 h) Fix the eljour twin per its own spec:** replace "Läs mer om ROT-avdrag"→/rot-avdrag-2026/ with the specced **phone CTA** ("Ring oss — vi förbereder underlaget till ditt försäkringsbolag" direction), and fix "försäkringbolaget"→"försäkringsbolaget", "Vår experter"→"Våra experter", "kan dig"→"kan hjälpa dig". 57 pages fixed in one template edit.
2. **(P1) Add one worked-example line** under the H2, per variant. Copy-pattern direction (not final copy): "Exempel: byte av elcentral — arbetskostnad `[GAP: kr från ampy-foretagsdata]` kr, du betalar `[GAP]` kr efter ROT. Avdraget gäller 30 % av arbetskostnaden, upp till 50 000 kr per person och år, och dras direkt på fakturan." Same pattern for Grön Teknik (50 % på arbete **och** material för laddbox/batteri, tak 50 000 kr). This converts the block from decoration to a decision tool and fixes the precision risk in the heading (change to "…genom 30 % ROT-avdrag på arbetskostnaden").
3. **(P1) Re-sequence: move the block above MainContact** on geo/service templates — ideally directly after ContentBlock (where price is discussed) and before the FAQ/MainContact close, mirroring the product-page family that already does this right. Pure re-ordering: zero SEO substance removed.
4. **(P1) Demote the exit:** replace the button with an inline disclosure ("Vad gäller avdraget?" accordion — content stays in DOM, SEO preserved) containing the mechanics + a text link to the article for the minority who want depth. If the button stays anywhere, cross-team note: `/rot-avdrag-2026/` and `/gron-teknik-2026/` need a MainContact close so the off-ramp can convert (currently form-less; separate article-template workstream).
5. **(P2) Mobile compression:** collapse the 3 steps to a single compact numbered row-list on ≤780 px (no icons or one shared icon), killing ~2 viewports of scroll and the duplicate icon assets.
6. **(P3) Add the ROT variant to /elservice/** with an elcentral-anchored example (service = priority #1).
7. **Candour footnote:** "Sveriges snabbast växande elfirma" in the adjacent MikroCTA is allowed under the 2026-07-18 superlative directive **unless demonstrably false** — flag to owner for verification, do not remove unilaterally.

## Test hypotheses (top 3, A/B)
1. **HYPOTES:** Adding a worked kr example (variant B) vs the current abstract 3-icon block (A) increases MainContact form submits on elektriker-i geo pages — MECLABS `v`+`i`: concretized incentive.
2. **HYPOTES:** Moving the incentive block above MainContact (B) vs current post-form placement (A) increases form-submit rate on service subpages without changing bounce.
3. **HYPOTES:** Replacing the "Läs mer" button with an inline accordion (B) vs the exit link (A) reduces mid-page exits to article pages and increases phone-click + form-submit combined conversions on laddbox-i pages.

## Priority score (arithmetic)
- Pages affected: **277** (193 ROT incl. 57-page hemförsäkring twin + 84 Grön Teknik)
- Funnel position weight: **2** (mid-page block)
- Expected effect: **2** (medium — supporting-cast block, but currently leaking traffic to form-less pages, mis-linked on urgent pages, and mute on the math it exists to explain)
- **Priority score = 277 × 2 × 2 = 1108 → P1 overall**, with the INC-01 eljour CTA-mismatch + grammar strings carved out as **P0** (trust-damaging, 57 urgent-intent pages, ~1 hour template fix).
