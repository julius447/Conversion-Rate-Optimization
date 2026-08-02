# Product ecosystem blocks — ProductHero · Popup form · ProductGrid · CEBlock

**Used on (verified from `data/block-map.json`, 326 pages):**

| Block | Pages | Categories | Position (1-indexed) |
|---|---|---|---|
| ProductHero | **26** | ev-product (16), battery-product (10) | Always **pos 2** (directly under Header) |
| Popup offert form | **26** | same (triggered by ProductHero CTA `Få skräddarsydd offert`, Bricks `templateId 29890`, click-interaction `action:show target:popup`; second popup 30855 also enqueued) | Modal — appended at document end |
| ProductGrid | **87** | laddbox-i (56, pos 4 of 20), ev-product (16, pos 10 of 16), battery-product (10, pos 11 of 17), page (5: `/`, `/laddbox/`, `/laddboxar/`, `/batterilagring/`, `/solcellsbatterier/`, pos 3–4) | Split: **top-of-page** on geo/pillar, **below MainContact** on product pages |
| CEBlock | **290** | ALL geo CPTs (elektriker-i/eljour-i/elinstallation-i/laddbox-i 56 each), service (22), ev-product (16), elektriker-for-x (13), battery-product (10), page (5) | **pos 13–20** of 16–23 — always in the bottom tail: VissteDuAtt → **CEBlock** → Certificates → FooterSEO |

**Union of pages carrying ≥1 of these blocks: 293 of 326.**

**Live evidence base (anti-theatre):** fetched https://ampy.se/laddboxar/zaptec-go/ and https://ampy.se/solcellsbatterier/dyness-stack100/ live 2026-08-02; markup verified in `data/pages/laddboxar-zaptec-go.html` (780 kb) + 15 sibling snapshots. Real strings quoted throughout.

**Funnel role:** these 26 product pages are the "money pages" of the laddbox/battery verticals — the destination of ProductGrid `Läs mer` links from 61 geo/pillar pages, mega-menu product cards, and (per strategy) future Meta demand-gen. Commercial priority is service > laddbox > battery, but within products, laddbox pages (16) matter most.

---

## 1. ProductHero (`product-hero`)

3-col desktop layout (verified live, Zaptec Go): [product image card + "Teknisk specifikation" 15-row accordion + "Installationsprocess" accordion] | [H1 "Zaptec Go - Laddbox", description, "Bra att veta:" grid ("Finns i lager / Installationstid: 1-3 veckor / Passar alla elbilar / 5 års garanti"), "Färger:" swatches, price stack "Totalt 4 490 :- / Ordinarie pris 8 980 :- / Inklusive installation Ja / Grön teknik 50%", CTA "Få skräddarsydd offert" → popup] | [expert card "Rådfråga vår expert om din laddbox! 010-265 79 79 … 5.0"].

### What it does well
- **Instant answer architecture.** Price incl. installation, stock status, install lead time, warranty and compatibility are all in the first viewport — exactly the JTBD questions ("vad kostar det totalt, hur snabbt, funkar den med min bil"). MECLABS value-clarity (v) is genuinely high here.
- **Dual conversion path.** Offert CTA + a visible human expert with a real phone number (010-265 79 79) matches the site's two-conversion doctrine; the expert card is a credible phone nudge for the 35–65 trust-seeking audience.
- **The spec accordion keeps 15 rows of SEO substance in the DOM without dominating the viewport** — the right repackaging instinct per MECLABS HealthSpire (sequencing, not deletion).

### Issues
- **PH-1 · P1 · desktop+mobile · Spec-accordion renders TWICE in the DOM on all 26 pages.** Verified: `Teknisk specifikation` occurs exactly 2× in the HTML — two full Bricks accordion instances with distinct IDs (`.brxe-57c33f` desktop / `.brxe-gmooup` mobile), toggled purely by CSS: `.brxe-gmooup {display: none…}` then `@media (max-width: 780px) {.brxe-gmooup {display: block…}}` and the inverse for the desktop instance. Same for the "Installationsprocess" accordion. Consequences: (a) duplicate content weight on already-heavy pages (780–813 kb HTML, vs the site's flagged ~9–10 s lab LCP — this block sits IN the LCP viewport); (b) two copies to maintain → divergence risk per product; (c) text-extraction consumers (AI-SEO/answer engines, reader mode, some crawont renderings) read the full spec table twice per page. Not an a11y bug (display:none removes from the tree) — a weight/maintenance/duplication bug. Framework: Google page-experience/LCP; DRY.
- **PH-2 · P1 · desktop+mobile · "Ordinarie pris" strike-through frames a conditional tax deduction as a retail sale.** Verified live: "Totalt 4 490 :- / Ordinarie pris 8 980 :-" (Zaptec Go); "Totalt Fr. 34 900 :- / Ordinarie pris 69 800 :-" (Dyness). The struck figure is exactly 2× — i.e. the pre-Grön-Teknik price, not an "ordinarie pris" being discounted by Ampy. The 50 % deduction is real (2026 canon) but **contingent on the buyer's personal tax space** — the site's own popup fine print admits it: "Vid avslag: Om Skatteverket nekar utbetalning faktureras det återstående beloppet". Byggahus/Reddit research says final-price surprise is THE core Swedish homeowner anxiety (MECLABS anxiety term, −2a); a buyer who lacks avdragsutrymme experiences a 100 % price surprise. Candour gate: not a fabricated claim, but discount-theatre *framing* of a state subsidy. Mobile: the price stack is the first decision element after description — the mislabel is unavoidable.
- **PH-3 · P1 · desktop+mobile · Unanchored "5.0" on the expert card.** "Rådfråga vår expert om din laddbox! 010-265 79 79 … 5.0" — no review count, no source link at this instance. Candour gate requires rating + count + source or removal (the MainContact pane lower on the same page does anchor it: "5 av 5 · Betyg på Google"). 26 pages, hero position.
- **PH-4 · P2 · SEO/mobile · Semantic + sequence oddities.** `<title>` promises "Från 4490 kr" while the visible price row omits "Fr." on laddbox pages ("Totalt 4 490 :-" reads as a fixed total, then the CTA asks for a "skräddarsydd offert" — a fixed-price signal followed by a custom-quote ask; the mixed signal feeds price-surprise anxiety). Mobile stacking (3-col → 1-col at 780px) pushes the expert/phone card below the fold entirely — the phone path, the stronger conversion for this audience, effectively disappears on the primary rendering (NN/g mobile).
- **PH-5 · P2 (cross-ref) · Battery pages only:** the adjacent Calculator-UI block (pos 3, 10 battery pages) ships a **wrong phone number in its error state**: "Något gick fel. Ring oss på **010-123 45 67** så hjälper vi dig direkt." — a placeholder, not 010-265 79 79. The failure-fallback path dials a dead number. Belongs to the Calculator-UI audit but is a **P0-class trust/conversion bug on money pages**; flagged here because it was verified during this fetch.

### Recommended changes
1. **Single accordion instance**, repositioned responsively with CSS (grid `order`) instead of duplicated DOM. Zero visual change; −~15 rows × 2 accordions of duplicate markup per page.
2. **Relabel the price anchor honestly:** struck row → "Pris före Grön Teknik-avdrag: 8 980 kr"; keep the strike visual. Add one microcopy line: "50 % dras direkt på fakturan – vi sköter ansökan. Förutsätter att du har avdragsutrymme kvar." Copy-pattern direction only; ampy-rost has final say. This *converts* the fine print from a buried liability into a MECLABS anxiety-reducer.
3. **Anchor or strip the expert-card "5.0"** → "5,0 av 5 · N omdömen på Google" (owner must confirm current rating + count) with GBP link, matching the Testimonials badge.
4. **Add "Fr." consistently** wherever installation scope can move the price (it can — the site's own standard-installation terms list exclusions: "Gräv-, schakt- och återställningsarbete… Uppsäkring, flytt eller utbyggnad av elcentral").
5. **Mobile:** keep a compact phone affordance (sticky or under the CTA) so the call path survives stacking.
6. **Fix the calculator error-state phone number now** (hand to Calculator-UI workstream).

### Priority score
26 pages × 3 (hero/form position) × 3 (high expected effect: price framing + trust anchor + LCP-viewport weight) = **234 · P1**

---

## 2. Popup offert form (Bricks popup 29890/30855)

Triggered by ProductHero's primary CTA. Verified live copy — laddbox version: "**Boka rådgivning med en laddboxexpert!** Alltid fasta priser och professionell service – fyll i formuläret för att komma igång." Battery version: "**Boka rådgivning med en batteriexpert!** Vi dimensionerar rätt batterilagring för ditt hem. Få en unik rekommendation och offert utan krav." Fields (both): Namn · E-post · Telefonnummer · Adress · Postnummer · Meddelande → "**Få ditt förslag**" → n8n → /thank-you.

### What it does well
- Vertical-matched headline (laddboxexpert/batteriexpert) and a consultative, no-pressure promise ("utan krav") — on-voice, candour-clean framing of the ask.
- Product context is implicit (popup fired from the product page, `popupContextType: post`), so the visitor never re-states which product — good message match *if* that context actually reaches the CRM payload.

### Issues
- **PU-1 · P1 · desktop+mobile · The primary conversion on all 26 money pages lives behind an interruption pattern with 6 always-visible fields.** Baymard: the number of *visible* fields drives perceived difficulty — this modal shows six at once, including **Adress + Postnummer + E-post before any value is delivered**, on a page whose CTA promised a conversation, not a data intake. NN/g on modals: they interrupt, hide the persuasive context (price, specs, expert card are now behind an overlay), and perform worst on mobile. The site tacitly admits the mobile problem: the page ships a URL-encoded JS patch forcing `.brx-popup {overflow-y:auto !important}` / `max-height: calc(100vh - 2rem)` — a hand-rolled fix for popup viewport overflow. On a 35–65 mobile audience with the iOS keyboard up, a 6-field modal is the highest-friction form on the site.
- **PU-2 · P1 · candour/consistency · "Alltid fasta priser" vs "Få skräddarsydd offert".** The CTA that opens the popup promises a tailored quote; the popup asserts *always* fixed prices; the standard-installation terms on the same page list paid additions ("Eventuella tillägg utöver standardpaketet hanteras direkt på plats … enligt gällande prislista") and exclusions. "Alltid fasta priser" is a strong claim — allowed only if demonstrably true. VERIFY with owner: if offert = fast pris once issued, say exactly that ("Du får ett fast pris i offerten – inga överraskningar på fakturan"), which is both candour-clean and a stronger anxiety-reducer (Konsumentverket written-quote norm is precisely what serious Swedish buyers check).
- **PU-3 · P1 · structural · Two competing form systems on the same page, with different promises and different field sets.** The popup (6 fields, "Få ditt förslag") and MainContact at pos 8–9 (7 fields incl. Google Places address, "Gratis rådgivning", flanked by "3 000+ genomförda installationer om året", the anchored Google badge and the 3-step process) are parallel conversion machines. MainContact is by the site's own inventory "the strongest conversion asset" — yet the hero CTA routes past it into a proof-free modal. Jakob's law + MECLABS: the popup carries none of the trust payload the page spent 3 000 words building. Also: no kundtyp (Privat/BRF/Företag) despite laddbox being a strong BRF vertical — lead-routing data lost.
- **PU-4 · P2 · measurement · HYPOTES:** popup form interactions are the least likely to emit form_start/step events (GA4 shows 0 form starts site-wide on paid traffic). If the popup form isn't instrumented distinctly from MainContact, the money pages are unmeasurable. Test instrumentation before redesign.

### Recommended changes
1. **Primary rec: retire the popup as the main path.** Make "Få skräddarsydd offert" scroll/anchor to an inline, product-prefilled offert form placed directly after ProductHero (or after Testimonials at pos 3) — product name locked, fields cut to Namn · Telefon · Postnummer (+ optional expander per Hero_2's "Fler detaljer (valfritt)" pattern; Baymard minimum-visible-fields). Keep MainContact at the bottom as the second net. (Divergent alternative, big-intervention rule: **A** keep popup but cut to 3 fields + trust row + anchored rating; **B** inline anchor form as above; **C** two-step popup — step 1 only Postnummer + Telefon, step 2 optional enrichment post-submit, mirroring the Hero_2 lead_id PATCH pattern.)
2. **Resolve the fixed-price contradiction** per PU-2 wording direction; one consistent price promise across CTA, popup and terms.
3. **Add kundtyp toggle** (or infer B2B from org-nr expander) to protect lead routing.
4. **Instrument** popup open / form_start / field_abandon / submit with distinct event names before any A/B.

### Priority score
26 pages × 3 (form) × 3 (high: this IS the money-page conversion path) = **234 · P1**

---

## 3. ProductGrid (`product__product-card` + "Ladda fler produkter")

Card grid with campaign tags (verified live: "NYHET", "SUPERKAMPANJ", "BÄSTSÄLJARE"), phase/effect chips ("1-fas & 3-fas · 22 kW"), price ("Fr. 4 390 kr"), "Läs mer" → product page. Load-more is a Bricks AJAX interaction: `action: loadMore`, `data-page="1" data-max-pages="4"` — 4 cards visible, 12 more behind "Ladda fler produkter".

### What it does well
- **Real price transparency in card form** — "Fr. X kr" with grön teknik framing ("Andra laddboxar – självklart med 50 % Grön Teknik-avdrag") answers the comparison job honestly; rare among Swedish elfirmor and a genuine differentiator.
- Sensible position on **product pages**: pos 10–11, *after* MainContact — non-converters get an alternative before exiting rather than mid-persuasion.

### Issues
- **PG-1 · P1 · geo pages (56 laddbox-i) · desktop+mobile · The grid sits at pos 4, directly under the Hero_2 form, and siphons paid/local intent into the product maze.** A "laddbox {ort}" visitor lands on a page with a full inline lead form (Hero_2 `.aof`) — the intended conversion — and is immediately offered 4–16 "Läs mer" exits into 3 000-word product pages whose only above-fold conversion is the 6-field popup (PU-1). Unbounce/message-match logic: geo intent is "install a laddbox where I live", not "compare 16 SKUs". The grid belongs *below* the geo page's proof blocks, or its cards should carry an offert CTA rather than only "Läs mer". Mobile: 4 stacked cards + load-more push Testimonials and MainCTA a full 2–3 viewports down.
- **PG-2 · P2 · product pages (26) · "Ladda fler produkter" reopens the whole assortment at the decision point.** Hick's law / choice-overload: a visitor on Zaptec Go who has scrolled past the form gets invited to browse 12 more alternatives. Some cross-shopping is healthy (keeps them on-site); unbounding it ("Ladda fler") at pos 10 competes with the just-passed MainContact. Cap at 3–4 *curated* alternatives ("Liknande laddboxar"), no load-more, on money pages.
- **PG-3 · P1 · candour · "SUPERKAMPANJ" tag.** A campaign tag implies a time-bound or price-cut offer. VERIFY with owner that Easee Charge Up is genuinely on a campaign price with a real ordinarie pris and (ideally) a stated period; otherwise this is manufactured-urgency adjacent and fails the candour gate. "BÄSTSÄLJARE" likewise needs to be true of Ampy's actual sales mix (it is checkable internally — anchor it or drop it). "NYHET" is safe.
- **PG-4 · P3 · a11y/UX · Load-more is an `<a href="#">`** styled as outline button — keyboard/AT semantics of a button, plus `#` href scroll-jump risk. Minor.

### Recommended changes
1. **Geo pages:** move ProductGrid below Testimonials/MainCTA (pos ~6–7), or convert cards on geo pages to "Se pris & få offert" CTAs that anchor into the geo page's own Hero_2 form with product preselected in "Vad gäller arbetet?" — capture the lead on the geo page, don't export it.
2. **Product pages:** rename to curated "Liknande laddboxar", cap at 4, remove "Ladda fler".
3. **Candour-verify all three tags** with owner; keep only what's demonstrably true; anchor SUPERKAMPANJ with the real ordinary price/period or delete.
4. Keep prices on cards — they are the grid's honest superpower.

### Priority score
Split arithmetic (positions differ): geo/pillar 61 pages × 3 (top-of-funnel position on page) × 2 (med) = 366; product pages 26 × 1 (low position) × 2 (med) = 52. **Total 418 · P1** (dominated by the 56 laddbox-i geo pages).

---

## 4. CEBlock (`ce-block`)

Long-form SEO + CTA block: gradient H2 → paragraph → 2 sub-headings + paragraphs → CTA pair → tall 9:16 image. Verified live instance (Zaptec Go, ~242 words): H2 "Zaptec Go för framtidens behov" → "Få 50% avdrag med Grön Teknik" → "Trygg och certifierad installation av din Zaptec Go" (6 dash-bullets) → buttons "**Kostnadsfri radgivning**" + "Ring 010-265 79 79".

### What it does well
- Keeps supplementary keyword coverage (avdrag, installation, trygghet) alive at the page bottom without touching the main content — legitimate SEO substance, and 242 words is not bloated per instance.
- The 6-bullet "vad ingår"-style list is the most concrete trust copy in the tail ("Auktoriserade elektriker… Komplett driftsättning av Zaptec-appen… Full hantering av Grön Teknik-avdraget").

### Issues
- **CE-1 · P1 · 290 pages · desktop+mobile · Typo on the primary CTA button: "Kostnadsfri radgivning" (missing å).** Verified in 20 of 37 HTML snapshots (all 16 laddbox products + batterilagring, elektriker, eljour, om-oss) — 2 occurrences per page (CEBlock + FooterSEO share the button library). HYPOTES (near-certain): the typo ships on every CEBlock/FooterSEO page ≈ 290 pages. For a risk-averse 35–65 audience scanning for professionalism signals, a misspelled main CTA is a small but sitewide trust leak — and it is a one-line library fix. Cialdini authority cuts both ways.
- **CE-2 · P2 · 290 pages · Redundant CTA tail: CEBlock and FooterSEO carry the *identical* CTA pair within ~1–2 viewports of each other**, inside a 4-block bottom stack (VissteDuAtt → CEBlock → Certificates → FooterSEO). On the Zaptec page that means the phrase-cluster repeats — "Grön Teknik" appears 19× in the page source — and the last four blocks make three near-identical asks after MainContact already made the real one. MECLABS: repetition without new value adds length (friction) not motivation. Mobile: the 9:16 CEBlock image + Certificates + FooterSEO image ≈ 3–4 extra viewports of scroll below the last new information.
- **CE-3 · P2 · geo pages · Generic superlative filler in the tail.** FooterSEO sibling copy verified: "Landets bästa Zaptec Go installatör … marknadens vassaste expertis". Strong superlatives are owner-permitted unless demonstrably false, but "landets bästa X-installatör" duplicated across 290 near-identical tails is doorway-flavored (echoes the SEO audit's doorway-devaluation diagnosis) and adds no decision information. Direction: replace one of the two tail CTA blocks per page with *differentiated* value (e.g. CEBlock keeps "vad ingår"-bullets; FooterSEO becomes a short local/anchored proof line).
- **CE-4 · P3 · SEO · CEBlock sub-headings are unstructured `<h2>/<h3>` gradient headings** repeating the page's main keyword — fine, but on 290 pages the block is a template with swapped nouns; low unique value per Google's scaled-content guidance. Not a deletion candidate (doctrine: preserve substance) — a differentiation candidate.

### Recommended changes
1. **Fix "radgivning" → "rådgivning" in the shared button library today.** One edit, ~290 pages, zero risk. (Also present in Hero-1/FooterSEO instances per inventory — same library.)
2. **De-duplicate the tail:** one CTA pair in the bottom stack, not two. Recommended: CEBlock keeps its concrete "vad ingår" bullets + single CTA; FooterSEO drops to a short brand line + phone (or is removed on product pages where CEBlock exists).
3. **Compress mobile height:** make the 9:16 image `max-height`-capped or hidden ≤480px; content stays in DOM.
4. **Differentiate per template** (product vs geo vs service) with one unique, checkable fact per instance instead of "landets bästa"-class filler.

### Priority score
290 pages × 1 (low-page position) × 2 (med: sitewide trust typo + tail redundancy/scroll cost) = **580 · P1** — the highest raw score in this set purely on spread; the typo portion alone is the cheapest high-leverage fix in the whole audit.

---

## Cross-cutting summary & ranked fixes

| Rank | Fix | Score | Effort |
|---|---|---|---|
| 1 | CE-1 typo "radgivning" in shared CTA library (≈290 pages) | 580 | XS |
| 2 | PG-1/PG-3 geo-page grid repositioning + candour-verify SUPERKAMPANJ/BÄSTSÄLJARE tags | 418 | S–M |
| 3 | PU-1/PU-3 popup → inline product-prefilled 3-field form; one form system per page | 234 | M |
| 4 | PH-2 "Ordinarie pris" → "Pris före Grön Teknik-avdrag" + avdragsutrymme microcopy; PH-3 anchor the 5.0 | 234 | S |
| 5 | PH-1 de-duplicate spec accordions (26 heavy pages, LCP viewport) | 156 (26×3×2) | S |
| — | P0 hand-off: calculator error-state phone "010-123 45 67" on 10 battery pages → Calculator-UI workstream | — | XS |

### Top 3 test hypotheses (A/B)
1. **HYPOTES:** Replacing the popup with an inline product-prefilled 3-field offert form directly under ProductHero increases form submits on the 16 laddbox product pages vs the popup control (primary metric: /thank-you pageviews from product-page sessions).
2. **HYPOTES:** Relabeling "Ordinarie pris" as "Pris före Grön Teknik-avdrag" + one avdragsutrymme reassurance line increases offert CTA clickthrough (reduced anxiety) without reducing lead quality on product pages.
3. **HYPOTES:** On laddbox-i geo pages, moving ProductGrid below Testimonials (pos 4 → ~6) increases Hero_2 form starts per session, as fewer visitors exit to product pages before seeing proof.
