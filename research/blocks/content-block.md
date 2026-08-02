# ContentBlock — `content-block` (SEO alternating rows)

**Used on: 291 of 326 pages** (verified via `data/block-map.json`) — the single most-deployed content unit on the site.
By category: elektriker-i 56 · elinstallation-i 56 · eljour-i 56 · laddbox-i 56 · service 22 · ev-product 16 · elektriker-för-x 13 · battery-product 10 · page 6. Never appears twice on the same page (0 duplicates).

**Funnel position(s): TWO distinct regimes** (median block index, verified):
- **Mid-page regime (~idx 4–6 of 16–19 blocks, fraction ~0.25–0.32):** service (idx 4), ev-product (4), battery-product (5), elinstallation-i (5), elektriker-för-x (5), laddbox-i (6). Sits right after Testimonials/MainCTA, right before VarProcess/MikroCTA. Example verified sequence (ampy.se/elservice/armatur/): Hero_2 → Testimonials → **ContentBlock** → VarProcess → MainCTA → FAQ → MainContact …
- **Deep regime (~idx 15 of 21–22, fraction ~0.68–0.75):** elektriker-i (idx 15) and eljour-i (idx 15) — placed AFTER MainContact, FAQ, ROT, MikroCTA, and (on elektriker-i) after MapBlock. Example (ampy.se/elektriker/akersberga/): … TeamSection → MapBlock → **ContentBlock** → BlueCTA → VissteDuAtt → CEBlock …

**Anatomy (verified in raw HTML, `laddboxar-zaptec-go.html` + `eljour.html`):** 3 alternating rows, each = one image column + one text column (H2 `content-block__heading` + a single `<p>`-run in `content-block__text-basic`). DOM order alternates image-first / text-first / image-first. Each row's container carries an `enterView` startAnimation (0.3s, runOnce) and images carry `data-interaction-hidden-on-load="1"`. Zero `<ul>` bullets in any inspected instance. Paragraphs measured: 84/89/72 words (Zaptec Go), 69/69/70 words (eljour) — one unbroken ~5-sentence paragraph per row.

**Responsive behavior (verified CSS):** Desktop image 600–620px wide, min-height 550px, radius `--apradius-l`, `object-fit: cover`. Heading `--aptext-xl` weight **400**; body `--aptext-mm` weight **300**, #333. ≤1024px: text `--aptext-m`; ≤780px: image min 300px/max-width 100%, text `--aptext-sm`; ≤480px: image full-width max-height 350px, text `--text-m` color `var(--color-20)`. Mobile = stacked in DOM order → rows 1 and 3 show a ~300–350px image BEFORE their heading.

---

## What it does well

- **It carries the SEO payload without faking anything.** Real long-form Swedish copy, real H2s, unique per page via ACF — e.g. armatur: "Energieffektiv belysning med LED-armaturer" / "Säker montering av din nya taklampa i hemmet"; eljour: "Vanliga tecken på att du behöver en eljour". No urgency theatre, no invented numbers — candour-clean.
- **Some rows already answer real decision questions.** Armatur row 3: "Att byta armatur själv kan verka enkelt, men vid fasta installationer krävs ofta en auktoriserad elektriker för att försäkringar ska gälla." That is exactly the Byggahus responsibility/insurance question — proof the block CAN do MECLABS-HealthSpire work (longer converted +638% when content answered real questions).
- **Technically disciplined images:** lazy-loaded, full srcset, webp, explicit width/height (no CLS from the img itself).
- **Alternating layout breaks monotony on desktop** and the single-template architecture means one fix propagates to 291 pages — enormous leverage.

## Issues

**CB-01 · P1 · Wall-of-paragraph, zero scan anchors (desktop + mobile).**
Every row is one H2 + one unbroken 70–90-word paragraph. No bullets, no bold key facts, no sub-heads, no captions (0 `<ul>` found in inspected instances). NN/g: users scan in an F-pattern and read a fraction of body text; a 35–65 homeowner scrolling past sees three grey slabs. Mobile compounds it: at ≤780px body drops to `--aptext-sm` at weight 300 — light-weight small grey text for the oldest-skewing audience on the site (check `--color-20` contrast at 480px against WCAG AA; weight 300 at small sizes is a known legibility risk for 45+ readers — HYPOTES, verify with Clarity reading heatmaps). The Clarity "23s no-click on Belysning" bounce is consistent with a visitor meeting unscannable mid-page slabs and leaving.

**CB-02 · P1 · Images are generic filler with broken information scent — on 224 geo pages they don't even match the topic.**
Verified on eljour.html: the three images are `Installation-av-amy.webp` (electrician mounting a **växelriktare/inverter**), `Ampy-elektriker-utfor-installation.webp` — whose alt text reads "En ren och tydlig version av Ampys logotyp som symboliserar professionella eltjänster" (a logo description pasted onto an electrician photo), and `ampy-elektriker-felsoker.webp` ("står framför ett nyinstallerat **hemmabatteri**"). Battery/inverter imagery on an EMERGENCY-ELECTRICIAN page, with mismatched alt text, recycled across the geo fleet. These images cost 550px of desktop viewport / 300–350px of mobile viewport apiece (~1 000px+ of mobile scroll across the block) while carrying zero decision information. NN/g image research: users ignore decorative stock-like images but engage with photos that carry information (real jobs, real people). Cialdini authority + the Byggahus "is this a real firm?" anxiety: a captioned real-job photo is trust evidence; a recycled render is noise. Product pages (Zaptec Go) do this better — actual product-in-situ photos. Alt-text mismatches are also an SEO/a11y defect on the site's biggest template.

**CB-03 · P1 · Content keyword-fills instead of answering the three Byggahus decision questions (price logic, process/responsibility, verification).**
Verified geo copy (elektriker/akersberga): headings "Noggranna installationer för ditt hem" / "Certifierat elföretag i Åkersberga" / "Modernisering och smart elservice" — the phrase "elektriker i Åkersberga" is worked into nearly every heading and paragraph, but **no row anywhere inspected addresses: what does it cost / fast vs. estimerad offert, material markups, who is liable if something breaks, "will they answer later"** — the exact concerns the specialist flagged from Byggahus/Reddit. No kr figure, no offert-logic sentence, no Elsäkerhetsverket self-check pointer ("så kontrollerar du oss i Elsäkerhetsverkets register" — the single highest-trust move available, currently absent). MECLABS heuristic: this content adds length (a) without adding value clarity (v). The block is the natural home for this material — it exists on 291 pages and is already indexed.

**CB-04 · P2 · Placement regimes are inconsistent and the mid-page regime interrupts the proof→process→ask chain.**
On service/product pages the block's three slabs sit at idx 4–6, inserting ~1 600–1 800px desktop (more mobile) between Testimonials and VarProcess/MainCTA — a motivated visitor must scroll through the SEO essay to reach "Så funkar det" and the form. On elektriker-i/eljour-i it sits at idx 15, AFTER the form and FAQ — defensible for eljour (Unbounce: urgent-repair visitors convert on immediacy, not essays; keep decision content out of their way) but on elektriker-i the block holds the page's best E-E-A-T copy ("Typ A jordfelsbrytare obligatoriska... 2026", "egenkontrollprogram", Elsäkerhetsverket) 15 blocks deep where almost no one arrives. Neither regime is wrong per se — the defect is that neither was chosen deliberately per intent type.

**CB-05 · P3 · JS-gated reveal + weak heading weight.**
Rows are `data-interaction-hidden-on-load="1"` with an enterView animation — on a page with ~9–10s lab LCP, fast scrollers can meet momentarily blank slots, and content visibility depends on JS. Headings render at weight 400 (`--aptext-xl`) — visually barely heavier than body, weakening the only scan anchors the block has. Also: eljour instance has 0 internal links in its paragraphs (geo instance had 1) — missed internal-linking equity on the site's most-deployed block.

## Recommended changes (SEO substance preserved — repackage, never delete)

1. **Repackage every row (template-level, one edit → 291 pages):** keep H2 + all existing sentences, but split into a 1–2 sentence lead + **3 bolded-lead bullets** carrying the hard facts (ROT 30%, behörighetskrav, IP-klass, 2026 jordfelsbrytarkrav). Content stays in DOM = zero SEO loss; scannability transforms. Raise heading weight to 600+, body weight 300→400 on ≤780px.
2. **Re-aim the three rows at the three decision questions** (copy-pattern direction, per service type): Row 1 = price logic ("Så sätter vi priset — fast offert efter rådgivning, ROT 30% dras direkt på fakturan"), Row 2 = process & responsibility ("Vad händer om något går fel — försäkring, dokumentation, egenkontrollprogram"), Row 3 = verification ("Så kontrollerar du oss själv — Elsäkerhetsverkets register + skriftlig offert enligt Konsumentverkets råd"). Keyword phrases survive inside answer-shaped copy. This is the MECLABS-HealthSpire move.
3. **Replace recycled renders with captioned real-job photos** matched to page topic ("Elcentralbyte, radhus i Täby — 2026"). Captions are the highest-read copy on a page (Ogilvy craft doctrine); a dated, located job photo is candour-compatible proof. Fix the mismatched alt texts (logo-description alt on eljour is a straight defect). Where no topical photo exists, shrink image column rather than ship a battery photo on an eljour page.
4. **Mobile:** cap images at ~240–260px, and reorder stacking text-first (heading → bullets → image) so the answer leads — rows 1/3 currently open with a 300–350px image. Consider `flex-direction: column-reverse` on image-first rows or DOM reorder in template.
5. **Placement, decided per intent:** eljour-i keeps deep placement (compress to 2 rows); elektriker-i moves the block to ~idx 5 (its E-E-A-T copy is wasted at idx 15); service/product pages keep position but the repackaged block must end with **one low-pressure inline text link** ("Vill du ha ett fast pris för ditt projekt? Ring 010-265 79 79 eller boka rådgivning") to harvest researcher-mode readers — currently the block dead-ends into the next band.
6. **Strip `hidden-on-load` from text columns** (keep subtle animation on images only) and add 1–2 relevant internal links per block instance.

## Test hypotheses (top 3, A/B)

1. **HYPOTES:** Repackaged rows (lead + bullets + bold facts) vs. current paragraph slabs → ≥15% more visitors scroll past the block and form-submit rate on service pages rises. (NN/g scannability; measure scroll-depth + submits.)
2. **HYPOTES:** Decision-question copy (price logic / responsibility / Elsäkerhetsverket check) vs. current keyword-fill on 20 geo pages → higher engaged time + more phone clicks. (MECLABS HealthSpire; Byggahus JTBD.)
3. **HYPOTES:** Captioned real-job photos vs. current recycled renders → phone-click rate up on service pages. (Cialdini authority; Clarity trust-seeking behavior — the 47s visitor who went Contact → About Us.)

## Priority score (arithmetic)

Pages affected **291** × funnel position **mid = 2** × expected effect **medium = 2** = **1 164** — the highest pages-affected multiplier of any block on the site, and a single-template fix. Per-page effect is medium (mid-page content, not hero/form), but leverage makes this **P1** (fix in month 1, bundled as one template edit: repackaging + image/alt fix + inline link).
