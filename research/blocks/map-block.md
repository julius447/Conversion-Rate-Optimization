# MapBlock — `map` / `.map-button` ("Vi finns där du finns", geo internal-linking block, 5 variants)

**Used on: 265 of 326 pages** (from `data/block-map.json`) — the single most widely deployed content block on the site after the global header/footer.

| Category | Pages | Variant behavior (verified) |
|---|---|---|
| elektriker-i | 56 | ort buttons → `/elektriker/{ort}/` siblings |
| elinstallation-i | 56 | → `/elinstallation/{ort}/` siblings |
| eljour-i | 56 | → `/eljour/{ort}/` siblings (verified live on /eljour/akersberga/ and /eljour/solna/) |
| laddbox-i | 56 | → `/laddbox/{ort}/` siblings |
| service | 22 | global-random → `/elektriker/{ort}/` (verified live on /elservice/armatur/) |
| elektriker-for-x | 13 | global-random → `/elektriker/{ort}/` |
| page (pillars + home) | 6 | home pos 10/11; /elektriker/ pillar pos **6/21**; /eljour/ 16/20; /laddbox/ 14/21; /elinstallation/ 11/17; /batterilagring/ 16/23 |

**Funnel position(s):** low-page on 264 of 265 carriers — relative depth 0.7 (136 pages) or 0.8 (126 pages); absolute index mostly 13–17. The single high-position outlier is the /elektriker/ pillar (pos 6, depth 0.3), where it plausibly works as a genuine hub. Immediate neighbors: **directly after MainContact-card on 79 pages**, after VissteDuAtt (69), TeamSection (58), ContentBlock (57); directly before CEBlock (126), ContentBlock (56), BlueCTA (56), ROT (22).

**Verified live structure** (fetched https://ampy.se/eljour/akersberga/ + /elservice/armatur/ 2026-08-02; markup cross-checked in `data/pages/home.html`):

- H2 `map__heading`: **"Vi finns där du finns"** (identical on all three fetched pages).
- ACF intro text, per-page. Home: *"Vi är din lokala elfirma som sträcker sig över hela Sverige…"*. Armatur: *"Vi är den lokala experten med hela Sverige som arbetsfält…"*. Eljour Åkersberga: *"Akut eljour i Åkersberga med snabb hjälp i hela närområdet. … **Se alla områden där vår jour finns tillgänglig i listan nedan.**"*
- Grid of **exactly 20 ort buttons** (`map-button`, outline pill, 4-col `1fr 1fr 1fr 1fr` grid on desktop), each a bare ort-name anchor ("Sickla", "Rågsved", "Södertälje"…) linking to the CPT-matched geo page. Self-page is excluded from its own list.
- Dark navy (#090b32) sub-card: **"Osäker ifall vi finns där du bor?"** + white **"Kontakta oss"** button → `/kontakt/` (arrow SVG).
- Right column (desktop): `sweden-map-1.webp` 289×600, `loading="lazy" fetchpriority="low"`, `data-interaction-hidden-on-load="1"` + enterView fadeIn (JS-gated visibility).

**Randomization verified:** /eljour/akersberga/ and /eljour/solna/ show two different, differently-ordered 20-of-56 subsets (Alvik/Vällingby/Märsta… vs Älta/Vällingby/Lidingö…); home and /elservice/armatur/ likewise differ. The list is server-side random per cache regeneration — neither alphabetical, nor proximity-ordered, nor stable over time.

**Mobile (≤480px, verified from live CSS):** the Sweden map image column is removed entirely (`.brxe-xaarku {display:none}`, image column `visibility:collapse`) — no "dot-map" survives in production; the block collapses to heading + text + a wall of 20 links + sub-card. Ort buttons drop to `font-size: var(--aptext-xs)` and `grid-gap: 5px`. With `html{font-size:62.5%}` (1rem = 10px), `--aptext-xs` computes to **~10–12px text** and `--apspace-4xs` vertical padding to **~5px** → tap targets of roughly 22–26px height at 5px spacing.

---

## What it does well

1. **It is the site's internal-link engine for the 224 geo pages.** 265 pages × 20 links ≈ 5,300 internal links; averaged out, every one of the 56 orts per CPT receives ~80–95 contextual inlinks with clean exact-ort anchor text under a topical H2. Without this block most doorway pages would be near-orphans reachable only via sitemap.
2. **CPT-matched linking is right in principle.** Eljour pages link eljour siblings, laddbox pages link laddbox siblings — the anchor-to-target intent match is correct, and the self-page is excluded.
3. **Placement discipline.** At depth 0.7–0.8 it stays out of the conversion path's prime real estate; on the /elektriker/ pillar (pos 6) it functions as an honest hub where a visitor genuinely wants an ort list.
4. **On-brand surface.** Token-bound (#090b32 sub-card, ap* scale, outline teal buttons); the "Vi finns där du finns" framing itself is warm and on-voice.

## Issues

### MAP-01 — Random 20-of-56 subset: unstable link graph + unscannable list — **P1 (SEO), P2 (UX)**
**Desktop + mobile.** Each cache regeneration deals a new random hand of 20 orts in random order. SEO: Googlebot sees a different outlink set on successive crawls of the same URL → internal-link signals to any given ort page fluctuate instead of accumulating, and a dense, rotating cross-link mesh among 224 near-duplicate geo pages is precisely the interlinked-doorway pattern the 2026-08 SEO total-audit flagged as the site's core devaluation risk ("doorway-devalvering"). UX: NN/g — users scan lists via expected order (alphabetical/geographic); a random-order list forces worst-case linear scan, and Jakob's-law consistency breaks when the list differs on a return visit. A visitor checking "finns ni i Tyresö?" has a ~64% chance (36 of 56 orts absent) of *not* finding their ort even when Ampy has a dedicated page for it.

### MAP-02 — The sub-card manufactures doubt the brand claims not to have — **P1 (message coherence / MECLABS anxiety)**
**Desktop + mobile.** Two sentences above, the block asserts *"hela Sverige som arbetsfält"*; the sub-card then asks **"Osäker ifall vi finns där du bor?"**. If the national claim is true (owner directive 2026-07-18: it is, in copy), the question is always answerable "Ja" — instead the block re-opens a settled question and adds an anxiety term (MECLABS: −2a) exactly where the visitor was being reassured. It also contradicts the geo-list's own implicature: showing a *partial* list of orts next to a "hela Sverige" claim reads as "so you're NOT everywhere". Minor voice note: "Osäker ifall" is colloquial; ampy-rost register would prefer "om".

### MAP-03 — Sub-card CTA routes AWAY from an on-page form — **P2**
**Desktop + mobile.** "Kontakta oss" → `/kontakt/`. On **79 pages the block sits directly after MainContact-card** — the visitor is sent on a full page navigation to reach a form functionally identical to the one one viewport above (and on geo pages, to a colder generic page than the geo-primed Hero_2 form at the top). Every low-funnel navigation is a restart of the funnel; with lab LCP flagged at ~9–10s, each avoidable page load is expensive. The 20 ort buttons themselves are also 20 leak paths to sibling doorways placed right beside the site's strongest conversion asset.

### MAP-04 — Candour breach in the eljour intro copy — **P1, trivial fix**
Live quote from /eljour/akersberga/: *"**Se alla områden** där vår jour finns tillgänglig **i listan nedan**."* The list below shows a random 20 of 56 areas. The sentence is factually false as rendered — a small but real candour-gate violation (the moat is precisely never saying an untrue checkable thing). Same-pattern risk exists on any ACF text that promises completeness.

### MAP-05 — Mobile tap targets far below guideline — **P2**
**Mobile only.** ~10–12px label, ~5px vertical padding → ~22–26px-tall buttons at 5px gaps; Apple HIG 44px / Android 48dp / WCAG 2.5.8 (24px minimum, spacing) — the grid sits at or below the WCAG floor for 20 adjacent targets. Fitts's law: small, dense targets = slow, error-prone; the 35–65 audience skews toward larger-touch needs. Mis-taps land on the *wrong ort's doorway page*, the worst possible error page.

### MAP-06 — The map visual vanishes on phones; on desktop it is JS-gated — **P3**
**Mobile:** `display:none` ≤480px — the one element that dramatizes "vi finns där du finns" is absent for the majority (assume ≥65% mobile) rendering. **Desktop:** `data-interaction-hidden-on-load="1"` + enterView fadeIn means the image renders only if the interaction JS runs (reduced-motion users get near-instant animation per the global reduce rule, but a JS failure leaves it hidden). The block's emotional payload is thus mostly theoretical.

### MAP-07 — No canonical area hub to anchor the mesh — **P1 (SEO architecture)**
The block links 20 random leaves and one contact page — never a stable "Alla områden" index. There is no crawlable, user-visitable page that lists all 56 orts per CPT once, permanently. Such a hub would (a) give every geo page one stable inlink source, (b) let this block link the hub + a *short* stable list instead of a 20-link lottery, (c) give the "finns ni i X?"-visitor a complete, ctrl-F-able answer. Its absence is why the block is doing two jobs (SEO mesh + visitor reassurance) and doing both halfway.

## Recommended changes (concrete)

1. **Stabilize the list; kill the lottery.** Per CPT, render a *deterministic* list: either (a) the same page-relevant subset every time (nearest-N by geography for geo pages — "eljour nära Åkersberga" is genuinely useful when your ort's electrician is busy), or (b) alphabetical fixed 20. Deterministic output also makes the crawl graph accumulate instead of churn. HYPOTES (A/B): nearest-N ordered list vs current random list increases ort-button CTR and reduces pogo-back rate.
2. **Build the "Alla områden" hub (1 per CPT or 1 combined with tabs) and point the block at it.** Sub-card becomes the hub's front door. This is the structural fix for MAP-01/MAP-07 and converts the doorway mesh into a hub-and-spoke architecture — the shape the SEO audit's doorway diagnosis calls for. (New-block proposal filed conceptually here; belongs in `research/missing/`.)
3. **Rewrite the sub-card to answer, not ask.** Copy-pattern direction (not final copy): affirmation first — "Vi täcker hela Sverige. Hittar du inte din ort i listan? Ring oss på 010-265 79 79 — vi hjälper dig direkt." Swap the `/kontakt/` navigation for the tel: link (one of the only two conversions) or an anchor-scroll to the on-page MainContact form on the 79+ pages that have it. Kills MAP-02 + MAP-03 in one stroke.
4. **Fix the eljour ACF sentence now** (MAP-04): "Se alla områden…" → "Se ett urval av områden…" or, post-hub, "Se alla områden på områdessidan." One-line ACF edit across the eljour-i CPT; do this in week 1 regardless of everything else.
5. **Mobile repackaging:** collapse the 20 buttons behind a "Visa områden nära dig" accordion or reduce to 8 + "Alla områden →" hub link; raise tap targets to ≥44px height with ≥8px gaps (padding-s, aptext-s). Content stays in DOM (SEO preserved per doctrine — repackage, never delete). HYPOTES (A/B): accordion-collapsed ort list vs open 20-grid on mobile changes scroll-depth-past-block and MainContact form starts (expected: fewer mis-tap exits, more form starts).
6. **Decide the image's fate honestly:** either give mobile a lightweight inline-SVG dot-map (the inventory's intended design) or drop the desktop image too and reclaim the column — a half-present decorative asset earns neither the bytes nor the layout cost.

## Priority score (arithmetic)

Pages affected **265** × funnel-position weight **1** (low-page on 264/265 carriers) × expected effect **2** (medium — direct conversion effect per page is low, but the block carries a candour breach, a message-coherence contradiction, sub-guideline mobile tap targets, and the internal-link architecture of 224 geo pages):

**265 × 1 × 2 = 530 → P2 overall**, with two carve-outs promoted to **P1**: the MAP-04 candour fix (trivial ACF edit, week 1) and the MAP-01/MAP-07 link-graph stabilization + hub (SEO-architecture impact across the whole doorway estate, month 1 planning alongside the SEO audit's doorway workstream).
