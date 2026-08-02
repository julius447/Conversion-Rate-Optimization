# Hero-1 + MiniMenu-Elfirma (block audit)

**Used on: 6 pages.** MiniMenu-Elfirma: homepage only (position 2, directly under the hero). Hero-1 exists in **two generations** that must be audited separately:

- **New "home-hero"** (the owner-approved "PERFEKTION" hero, prototype-parity build): **homepage only** (`https://ampy.se/`, position 1). Full-bleed photo card, single H1, one CTA, trust row bottom. *Note: `data/block-map.json` does not fingerprint the homepage hero as Hero-1 because it uses `home-hero__*` classes; verified directly in `data/pages/home.html` + live fetch 2026-08-02.*
- **Old pillar Hero-1** (`hero-1__floating-banner` white banner card): **5 pages** (verified in block-map, all at position 1 of the page): `/elektriker/` (21 blocks), `/elinstallation/` (17), `/eljour/` (20), `/laddbox/` (21), `/om-oss/` (9).

**Funnel position:** hero — the first screen of the homepage and all five pillars. Funnel weight 3 in every score below.

**Grounding (anti-theatre):** live fetches of `https://ampy.se/` and `https://ampy.se/elektriker/` on 2026-08-02, raw snapshots `data/pages/home.html`, `elektriker.html`, `eljour.html`, `om-oss.html`, plus HTTP HEAD checks on every hero/mini-menu image. All copy quoted below is real fetched copy.

**Verified live copy:**
- Homepage H1: *"Elinstallationer i hemmet, gjort ordentligt."* → *"Våra egna behöriga elektriker hjälper dig i hela Sverige, med allt från elfel och elcentraler till laddbox och batterilagring."* → single CTA *"Kostnadsfri rådgivning"* (→ `/kontakt/`) → trust row *"**5.0** på Google"* (linked to GBP) + *"Över **3 000** installationer per år"*.
- MiniMenu: H2 *"Din elektriker för hela hemmet"* → lead *"Med över 3000 installationer per år hjälper vi dig med elinstallationer, laddbox och batterilagring, allt under ett och samma tak."* → three equal 1:1 photo cards: **Elservice** (`/elservice/`), **Laddbox** (`/laddboxar/`), **Batterilagring** (`/batterilagring/`), each with a sky-blue "Läs mer" pill.
- Pillar H1s: *"Elektriker för privatpersoner över hela Sverige!"* / *"Elinstallationer över hela Sverige!"* / *"Eljour dygnet runt i hela Sverige!"* / *"Laddbox med installation i hela Sverige!"* / *"Sveriges snabbast växande elfirma, byggd för kvalitet."* Pillar CTAs: **"Kostnadsfri radgivning"** [sic] + "Ring 010-265 79 79", then a "5.0" + 5-star row (GBP link, no review count).

---

## What it does well (keep)

1. **The homepage hero earns its approval.** Verified craft: media-attribute-split preloads (`ampy-home-hero-new.avif` 68.7 KB desktop / `ampy-home-hero-new-mobile.avif` 31.1 KB mobile, `fetchpriority=high`, only the matching one downloads), `100svh`-based height (no mobile URL-bar jump), font preloads, a single unambiguous primary CTA, and a trust row that is *anchored in behavior* ("5.0 på Google" **links to the actual GBP listing** — Cialdini social proof made verifiable) plus a volume proof ("Över 3 000 installationer per år"). A deferred script even renders the rating with Swedish decimal ("5,0"). Mobile: H1 36px, CTA min-height 52px (comfortably above thumb-target minimums — Fitts), proof stacked bottom-left. This is the reference standard the rest of the site should be held to.
2. **The H1 is a genuine value proposition, not a category label.** "Elinstallationer i hemmet, gjort ordentligt." states what + for whom + the differentiating promise in seven words — strong on the MECLABS value-clarity term (v), and in the candour register.
3. **MiniMenu craft is high.** Scoped CSS (zero theme leakage), container queries with `@supports` fallback, `prefers-reduced-motion` and `forced-colors` handling, aurora-gradient fallback if a photo fails, real `aria-label`s ("Elservice – Läs mer"), print styles. Card photos are reasonable (90–101 KB webp, lazy via `flying-press-lazy-bg`).
4. **The three-card mini-menu is the right pattern for the homepage job.** A homepage serves mixed intent; a visual router into the three business lines directly under the hero matches Jakob's law (users expect category tiles) and gives the "I know what I need" visitor a one-click path.
5. **Pillar Hero-1 mobile stacking order is sane:** H1 → text → two full-width stacked CTA buttons → centered trust row → image last (image demoted below the ask, not blocking it).

---

## Issues

### F1 — P0 — Primary CTA is misspelled on all five pillar heroes: "Kostnadsfri radgivning"
- **Desktop + mobile, 5 pages.** Verified live on `/elektriker/` and in `eljour.html`, `om-oss.html` snapshots: the green primary button reads *"Kostnadsfri radgivning"* — missing the "å" in rådgivning. The homepage hero and the header CTA spell it correctly ("Kostnadsfri rådgivning" / "Gratis rådgivning"), so the defect is isolated to the shared pillar Hero-1 component.
- **Evidence:** the audience is a risk-averse 35–65yo homeowner scanning for competence signals (business context; Byggahus/Reddit trust concerns). A spelling error **in the primary conversion button** is a credibility micro-cue at the exact moment of decision — MECLABS anxiety term (a), Cialdini authority undermined. NN/g: users judge professionalism from surface errors.
- Fix time: minutes (one shared Bricks component).

### F2 — P0 — Pillar hero preloads and references a staging asset that 404s
- **Desktop + mobile, 5 pages.** Live `/elektriker/` HTML contains `<link rel=preload ... fetchpriority='high' href='https://staging.ampy.se/wp-content/uploads/hero-bg-1.webp'>` AND `.hero-1__floating-banner` sets the same URL as its background-image. Verified via HEAD: **HTTP 404**. Consequences: (a) the banner card's decorative background silently never renders — the design ships broken; (b) every pillar pageview spends a high-priority request + a DNS/TLS connection to `staging.ampy.se` on a dead asset, competing with the real LCP image during the critical window; (c) a staging hostname is leaking into production markup.
- **Evidence:** direct HTTP verification; web-vitals preload guidance (a high-priority preload of an unused/404 resource delays actual LCP-path fetches). Relevant to the known ~9–10s lab LCP flag.

### F3 — P1 — Pillar H1 is JS-gated (hidden on load) and gradient-clipped from a near-invisible green
- **Desktop + mobile, 5 pages.** The H1 carries `data-interaction-hidden-on-load="1"` + fadeIn (verified on elektriker, eljour, om-oss) — the page's most important element is **invisible until Bricks' interaction JS runs**, worsening perceived speed on slow mobile connections and pushing LCP-candidate text later. The base CSS paints the whole heading as gradient text: `linear-gradient(90deg, #3ED886 9%, hsl(144 50% 40%) 100%)` with `-webkit-text-fill-color: transparent` on a **white** card; a second JS pass (`data-highlight="last-1"` → `.has-gradient-highlight`) then re-scopes the gradient to the last word. Contrast arithmetic: #3ED886 on #ffffff ≈ **1.85:1** (fails WCAG 1.4.3 large-text 3:1); even the dark end hsl(144 50% 40%) is ≈ 3.6:1. So the pre-JS render is a heading that starts near-invisible, and the final render depends on two JS passes.
- **Evidence:** WCAG 2.1 AA; NN/g on ageing vision (contrast sensitivity declines from ~50; the stated 55–65 segment needs *more* contrast than AA minimums, not less). MECLABS clarity: the H1 carries the value prop — it should be the most robust element on the page, not the most fragile.
- **Mobile note:** same behavior; on 4G the fadeIn delay is most visible there.

### F4 — P1 — Pillar hero downloads the hero photo twice, both eager + high priority
- **Mobile primarily, 5 pages.** Verified in live `/elektriker/` markup: `Ampy-framtidssakrat-hus.webp` (1200×992, ~100 KB) appears **twice** — once as `hero-1__hero-image` (desktop mask) and once as `hero-1__hero-mobile-image` (mobile mask) — **both** `loading="eager" fetchpriority="high"`, with the off-breakpoint copy hidden only by CSS `display:none`. Browsers download `display:none` images: every visitor fetches ~200 KB where ~100 KB (or a properly sized ~40 KB mobile rendition) would do, and two high-priority image fetches + the 404 staging preload (F2) compete in the LCP window. `sizes="(max-width:1200px) 100vw"` also means no smaller srcset candidate is honored meaningfully on mobile.
- **Evidence:** web.dev LCP guidance; contrast with the homepage hero's correct `media`-split preload pattern (31 KB on mobile) — the fix pattern already exists in-house.

### F5 — P1 — MiniMenu card equality contradicts the commercial priority (service > laddbox > battery)
- **Desktop + mobile, homepage (the highest-traffic page).** The three cards are visually identical equal-thirds (`grid-template-columns:repeat(3,1fr)`, same size, same "Läs mer" pill), giving **Batterilagring equal billing with Elservice** — and the *very next block* (ProductGrid) opens *"Våra hembatterier och laddboxar – installerat & klart med 50 % Grön Teknik-avdrag"* with **four battery products before any laddbox**. Net effect: a homepage that the owner wants weighted service-first reads battery-first from block 2 onward. Additionally the **Laddbox card routes to `/laddboxar/` (product listing)**, not the `/laddbox/` service funnel that carries the full conversion stack (21 blocks incl. MainContact) — a routing decision worth a deliberate re-check, since "laddbox med installation" intent is a service purchase, not a spec-comparison task.
- **Evidence:** business context "Commercial priority: service > laddbox > battery (owner-confirmed). Batteries are OFF Google Ads." Visual hierarchy = priority communication (NN/g); equal cards signal equal importance. HYPOTES: A = equal cards (control) vs B = Elservice card 2× width / listed first with laddbox + batteri half-cards, measuring click share into /elservice/ and downstream form submits — B increases service-path CTR.

### F6 — P1 — "5.0" is unanchored (no review count) in every hero trust row
- **Desktop + mobile, 6 pages.** Homepage: *"5.0 på Google"* + stars; pillars: bare "5.0" + stars. All link to GBP (good — verifiable), but none states the review count, and the number is asserted as current. Candour gate: a rating without volume ("5.0 **av X omdömen**") is a soft claim — a 5.0 from 8 reviews and from 300 reviews are different promises, and Baymard shows users discount ratings without counts. The testimonials block ("X av 5 · Betyg på Google") already has the anchored pattern.
- **Action needed from owner:** confirm current rating + count; then render "5,0 av X · Google" in the hero rows. (Never assert "5.0" as fact unless owner-confirmed current — CLAUDE.md rule.)

### F7 — P2 — Claim-register risks in pillar hero copy (flag to owner, not a unilateral rewrite)
- `/elektriker/` paragraph: *"Upptäck marknadens billigaste priser, trygga installationer…"* — "marknadens billigaste priser" is a market-superlative **price** claim. Owner directive allows strong superlatives *unless demonstrably false*; a cheapest-in-market claim is the most falsifiable claim type there is (marknadsföringslagen vilseledande-risk if unsubstantiated) AND it positions on price while the whole trust architecture positions on quality ("gjort ordentligt", behöriga elektriker). MECLABS: it also attracts price-shoppers, degrading lead quality against the ~1 300–2 000 kr max-CPL economics. ⚑ owner decision.
- `/eljour/`: *"garanterar vi snabb inställelsetid, dygnet runt, året om"* — "garanterar" is a guarantee without stated terms; either state the term (a real inställelsetid) or soften.
- `/om-oss/`: *"Sveriges snabbast växande elfirma"* — allowed under the loosened superlative rule if substantiable; ⚑ confirm the basis (e.g., Allabolag growth figures) so it survives challenge.
- Internal-consistency flag (adjacent block, same first screen on /elektriker/): hero row claims sit directly above a Metrics card saying *"1000+ Nöjda kunder — Över tusen genomförda installationer"* while the homepage hero says *"Över 3 000 installationer per år"* — 1 000 total vs 3 000/year read as a contradiction to a careful visitor. Reconcile to one canonical volume proof.
- **Mobile note:** same copy both viewports.

### F8 — P2 — Homepage hero: single CTA routes to /kontakt/ — the phone path is absent from the hero
- **Desktop + mobile, homepage.** The approved hero has ONE CTA ("Kostnadsfri rådgivning" → `/kontakt/`). Single-CTA focus is defensible (NN/g one-primary-action; the pillar pair splits attention three ways once the form is present). But with **only two conversion paths in the business**, the hero of the highest-traffic page offers neither directly: no tel: link, and the form is a page-navigation away (added step vs an anchor to the on-page MainContact lower down). The 2-phone-clicks-out-of-32-paid-sessions reality says the call path needs more surface, not less. HYPOTES: A = current single CTA→/kontakt/ vs B = primary "Kostnadsfri rådgivning" (anchor to on-page MainContact) + secondary "Ring 010-265 79 79" tel: ghost button — B increases combined call-clicks + form starts on mobile. Keep the pixel-approved rendering constraint in mind: this is an owner-gated change to a locked design (approved-rendering-is-canon).
- Pillar pages keep the pair — correct for service intent (Unbounce home-services: urgent/repair visitors skew phone) — so the site currently has the pair where it belongs and the single where it's debatable, which at minimum deserves the test.

### F9 — P2 — MiniMenu mobile cost: three full-width 1:1 cards ≈ three screens of scroll
- **Mobile.** `@container (max-width:767px)`: grid → 1 column, max-width 440px, cards keep `aspect-ratio:1/1` → on a 390px phone each card is ~370px tall; header + lead + 3 cards ≈ 1 300+ px of scroll before the visitor reaches anything else. The router becomes a corridor. Also "Läs mer" is a generic label (NN/g information scent — descriptive labels outperform; the card title carries the scent, the pill does not).
- HYPOTES: A = stacked 1:1 cards vs B = compact 3:1 horizontal cards (photo left, title + arrow right, ~110px tall each) on ≤767px — B improves scroll-depth past the block and click-through into the three funnels.

### F10 — P3 — Minor hygiene
- `data-sheets-root="1"` span residue in `/elektriker/` hero paragraph (Google Sheets paste artifact).
- Two conflicting definitions of `--aptext-3xl` present on pillar pages (`clamp(3rem…4.8rem)` vs `clamp(2.6rem…6rem)`) — the known one-token-truth problem surfacing inside this block's sizing.
- "Över 3 000" (hero) vs "över 3000" (MiniMenu lead) — inconsistent thousands formatting one viewport apart.
- Four of five pillar H1s end in "!" — allowed (metered), but four heroes in a row using the same exclamation pattern reads as a tic, not emphasis; the homepage's period ("gjort ordentligt.") is the stronger register.

---

## Recommended changes (concrete)

1. **Week-1 fixes (no design change, no owner gate):** correct "radgivning" → "rådgivning" in the shared pillar Hero-1 button; delete the `staging.ampy.se/hero-bg-1.webp` preload and repoint the banner background to a production asset (or remove the background — it currently never renders anyway, so removing it is the pixel-identical option per approved-rendering-is-canon); strip the Sheets span.
2. **Perf pass on pillar Hero-1 (format-only):** adopt the homepage's own pattern — one `<picture>`/media-split preload, mobile rendition ~≤40 KB, only the active breakpoint's image eager; drop the duplicate eager fetch. Remove `hidden-on-load` from the H1 (let the H1 paint with HTML; keep fadeIn for decorative elements only).
3. **Gradient H1 policy:** keep the signature gradient but (a) scope it in CSS to the last word from the start (no JS dependency, e.g. wrap the last word server-side), and (b) raise the gradient's light stop so the *whole* range clears 4.5:1 on white — or run the gradient only over words sitting on the darker photo areas. Test target: 55–65yo legibility, not brand-guide fidelity.
4. **MiniMenu hierarchy:** re-order/re-weight to Elservice-first prominence (larger card or first + labeled row), keep Batterilagring present but not co-equal; decide deliberately whether the Laddbox card should feed `/laddbox/` (service funnel) instead of `/laddboxar/` (product list). Copy-pattern direction for pills: "Se elservice" / "Välj laddbox" / "Om batterilagring" instead of 3× "Läs mer".
5. **Anchor the rating everywhere it appears in this block:** "5,0 av X · Google" (owner supplies current X), or drop the number and keep stars + "Betyg på Google" link.
6. **Owner flags (⚑):** "marknadens billigaste priser", "garanterar … inställelsetid", "Sveriges snabbast växande", and the 1 000+/3 000-per-år volume-proof contradiction — pick one canonical proof set.
7. **Tests to queue (top 3):** F5 hypothesis (service-weighted mini-menu), F8 hypothesis (hero CTA single vs pair+anchor on homepage), F9 hypothesis (compact mobile cards). All phrased above as A/B statements.

---

## Priority score (arithmetic)

Formula: pages affected × funnel-position weight (hero = 3) × expected effect (high 3 / med 2 / low 1).

| Finding | Pages | Weight | Effect | Score | Priority |
|---|---|---|---|---|---|
| F1 CTA typo | 5 | 3 | 2 | **30** | P0 (trust, trivial fix) |
| F2 staging 404 preload/bg | 5 | 3 | 2 | **30** | P0 (broken render + LCP, trivial fix) |
| F3 JS-gated gradient H1 | 5 | 3 | 2 | **30** | P1 |
| F4 double eager hero image | 5 | 3 | 2 | **30** | P1 |
| F5 MiniMenu priority mismatch | 1 | 3 | 3 | **9** | P1 (homepage = highest traffic) |
| F6 unanchored 5.0 | 6 | 3 | 1 | **18** | P1 (candour) |
| F7 claim-register flags | 3 | 3 | 2 | **18** | P2 (owner-gated) |
| F8 homepage CTA single vs pair | 1 | 3 | 2 | **6** | P2 (test) |
| F9 MiniMenu mobile height | 1 | 3 | 2 | **6** | P2 (test) |
| F10 hygiene | 6 | 3 | 1 | **18** | P3 |

**Block overall: 6 pages × 3 (hero) × 2 (medium-high expected effect) = 36 → P1**, carrying two P0 line-items (F1, F2) that should ship in week 1. The homepage half of the block is strong and should be treated as the internal reference implementation; the five pillar Hero-1 instances are a previous generation that needs to be brought up to the homepage's own standard.
