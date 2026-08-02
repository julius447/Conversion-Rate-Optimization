# Verktygs-tilen (calculator/tool entry tile) — ONE component, three formats

**Status: BUILD — adversarial consolidation of THREE separately-proposed cross-link mechanisms.**
The category team proposed a hub "calculator entry tile" (CAT-06, hypothesis 3), the product team proposed embedding Laddboxkalkylatorn on 16 ev pages (PP-14), and the article team proposed an in-article contextual tool link (ART-04, inline CTA block A). Building three unrelated widgets would recreate the CTA-band fragmentation this audit diagnosed. Resolution: **one ACF-driven "Verktygs-tile" component with three formats**, sharing one visual grammar and one instrumentation contract. The magnets' distribution problem (they are orphans nobody routes TO) is the mirror of their wrap problem (they route nobody OUT) — this component fixes the inbound half.

## Job-to-be-done
For the not-yet-ready visitor on a money page or article: **"let me get a number for MY situation before I talk to anyone"** — the softest possible ask (zero fields to start), which converts researchers the form cannot catch yet. Baymard guided-selling: undifferentiated grids without guided selection push users to abandon rather than choose; the tile IS the guide.

## Anatomy (shared)
Light card (white/#f5f9ff — information, not campaign): small tool glyph → one-line promise ("Osäker vilken laddbox som passar? Räkna fram rätt modell och pris på 2 minuter") → arrow-link into the tool with `?src={template}-{slug}` → optional sub-line naming the honest frame ("kostnadsfritt, ingen e-post krävs" — TRUE today: the calculators show results before any ask; this line is a differentiator, keep it true). Never a dark band, never a countdown, one link only.

## Format 1 — Hub entry tile (routing pages)
- **/laddboxar/**: first tile of the ProductGrid → Laddboxkalkylatorn. Fixes the verified zero-body-links gap (CAT-06) and the "Jämför och välj"-promise the mega-menu makes but the page breaks.
- **/solcellsbatterier/**: NO tile — the full calculator is already embedded on-page (correct pattern; don't add a link that exits to a duplicate).
- **/elservice/**: Elcentral-kollen teaser tile in the grid ("Osäker på din elcentral? Testa Elcentral-kollen — Säker? Redo?") — only AFTER the grid's dead links are fixed (CAT-01) and elcentral-kollen gets its SSR layer (wrap file).

## Format 2 — Product-page embed row (16 ev-product pages)
Per PP-14: battery pages prove the pattern (Calculator-UI slot after ProductHero). For laddbox product pages, the cheaper first step is the tile (link into Laddboxkalkylatorn with the product preselected via query param) directly under the price block; full embed is the follow-up if the tile's CTR earns it. Trade-off named: an embed keeps the visitor on-page but costs page weight on a template already averaging ~780–812 KB HTML with a 9–10 s lab-LCP flag — the tile is the speed-safe v1.

## Format 3 — In-article tool tile (11 posts)
This IS the tool-variant of the article wireframe's inline CTA block A (slot 5, ~25–35 % depth) — **do not build a second inline block**. Per-cluster ACF routing:
- elcentral cluster → **Foto-bedömning micro-offer** (see magnet-foto-bedomning.md — a form ask, not a tool link, because the article has already done the tool's job of establishing price context) with Elcentral-kollen as secondary link.
- laddbox cluster (elbilsladdning-hemma-2026 etc.) → Laddboxkalkylatorn tile.
- ROT/grön-teknik posts → Energikalkylatorn tile + the "vi sköter Skatteverket-administrationen" offert line.
- LED/belysning posts (future series) → LED-kalkylatorn tile; DIY-adjacent posts → Elkollen tile.

## Deliberate exclusions (named trade-offs)
- **Geo laddbox-i pages (56): NO tile.** GEO-05's resolution is to keep visitors ON the geo page (product cards prefill the on-page form). Adding a calculator exit would re-open the funnel-hijack that finding just closed. The geo pages' price answer comes from the ProductGrid + Pris & offert block instead.
- **Service-page heroes: NO tile.** Screen 1–2 belongs to the Pris & offert block + form (SVC-02 wireframe). A tool exit above the ask would dilute the page's one job. Tiles on service pages live only in the mid-page zone, elcentral-cluster pages only.
- **Homepage: NO tile in v1.** HP-01/02 re-sequencing must land first; the mega-menu "Guider & verktyg" already routes, and the homepage's job is service routing, not tool distribution.

## Lead-capture linkage
Tile passes `?src=` + optional `?product=`/`?arbete=`; the magnet's embedded form carries the value through as hidden fields to n8n, so a lead born on an article is attributable end-to-end. Requires the wrap file's LM-02 instrumentation contract first. Elkollen's verdict-bridge (`?arbete=` into service-page Hero_2 prefill) is the same mechanism in reverse.

## Effort & priority arithmetic
- Effort: **S** (one Bricks component + ACF variants; tools already exist — this is wiring, not construction).
- Priority: hub /laddboxar/ 1 × 2 × 3 = 6; ev-product 16 × 2 × 2 = 64; articles 11 × 2 × 2 = 44 (shared with ART-04); /elservice/ teaser 1 × 2 × 2 = 4 → **≈118 total. P1–P2, month 1–2**, sequenced AFTER the wrap standard (routing traffic into unwrapped orphans wastes the clicks — wrap first, then wire).

## Candour-gate check
PASS: no urgency, no invented numbers; the "ingen e-post krävs" line is verifiably true and must be removed if any magnet ever gets an email wall (none should — value-then-ask is the family doctrine). Tile promises ("på 2 minuter") must match real tool length — verify per tool before final copy (ampy-rost pass).

## Test hypotheses
1. **HYPOTES (hub):** /laddboxar/ with the calculator entry tile as first grid tile produces more qualified leads (calc completions + offert requests) than the pure 16-card grid (= category hypothesis 3, Baymard guided-selling).
2. **HYPOTES (article):** the per-cluster tool tile at 25–35 % depth lifts article→tool→lead flow vs. the current zero-cross-link state without reducing scroll depth (shared with ART hypothesis 1).
