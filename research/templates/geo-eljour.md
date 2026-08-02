# Programmatic geo template: eljour-i ("Eljour i {ort}")

URLs analyzed (live-fetched 2026-08-02): https://ampy.se/eljour/taby/ , https://ampy.se/eljour/huddinge/ ; symptom-block presence spot-verified on /eljour/akersberga/, /alvik/, /nynashamn/, /sollentuna/, /vallentuna/.
Pages using this template: **56** (block-map lists 57 `/eljour/*` URLs; the 57th is the pillar https://ampy.se/eljour/ which uses Hero-1 without the aof form and is out of scope here).
Intent class: **URGENT / repair** — the highest-converting intent class in the Unbounce professional-services benchmark (repair/urgent >> planned-improvement). This is Ampy's single best conversion-rate opportunity per page-visit.

> **Snapshot delta (important):** `data/block-map.json` shows the old sequence `Hero_2 → Metrics → MainCTA → …`. The LIVE pages now carry the **eljour symptom block** ("Är något fel med elen? Tryck på det du upplever.") inserted as a shortcode section directly after Hero_2 — verified in rendered HTML on all 7 pages checked (`<section class="eb" aria-labelledby="ebTitle">`). The block-map is stale for this template; everything below is from the live DOM.

---

## Current block sequence (verified in live DOM order, taby.html body)

| # | Block | Desktop behavior | Mobile behavior |
|---|---|---|---|
| 1 | Header | Mega-menus + "Gratis rådgivning" teal CTA (pulsing dot) + "5.0" | Offcanvas accordion + "Ring en expert" + 5.0 |
| 2 | **Hero_2 + aof form** | Left: breadcrumbs → **H1 = small eyebrow "Eljour i Täby"** (`h1.hero_2__section-subheading`) → H2 big headline (Täby: "Eljour dygnet runt: Ring 010-265 79 79!"; Huddinge: "Eljour dygnet runt i hela Huddinge!") → paragraph → CTA pair (**"Kostnadsfri rådgivning" first**, "Ring 010-265 79 79" second) → unanchored "5.0" star row (links GBP). Right: `.aof` form card — **JS-rendered** into `<div id="ampy-form-root" class="aof" data-endpoint="…supabase.co/functions/v1/hero-lead">` (kundtyp toggle, ärende-select, namn, telefon, e-post, adress+postnr, GDPR). | Stacked: hero text → full form card → then everything else. The form occupies ~1.5 viewports before the symptom block. Form is invisible to no-JS/first-paint (client-rendered). |
| 3 | **Eljour symptom block** (`.eb`, new) | Two-pane grid (`grid-template-columns:var(--col-l) var(--col-r)`): left aside = call panel ("Jour öppen just nu" pulse, "Akut elfel? Ring oss direkt.", 4 trust bullets — "Jour dygnet runt, året om" / "Målsättning att vara på plats inom en timme" / "Prata med en av våra behöriga elektriker, inte en växel" / "Tydligt pris innan vi rycker ut, inga dolda avgifter" — "Ring eljouren 010-265 79 79" CTA, Elsäkerhetsverket grounding stat "~1 800 elrelaterade bränder… Källa: Elsäkerhetsverket"). Right: 14-symptom accordion (Akut/Varning tags, 112/1177-first safety copy, per-panel "Ring eljouren" tel CTA), "Se fler tecken (6)" progressive disclosure. **CSS verified: NO `position:sticky`/`fixed` anywhere in `50-eljour-lead-magnet.css`** — the call panel scrolls away. | `@media (max-width:992px){.eb__grid{display:block}}` — call panel stacks ABOVE the accordion, then scrolls out of view; **no fixed mobile call-bar shipped** (the v3 concept had one). Grounding stat renders twice (`.eb__ground--d`/`--m` duplication visible in text extraction). |
| 4 | Metrics | 3 number cards: "1000+ Nöjda kunder … Över tusen genomförda installationer är vårt absolut starkaste kvalitetsbevis" / "25+ Erfarenhet i branschen" / "20+ Personer i teamet". Installation-framed copy. | Cards stack vertically. |
| 5 | MainCTA | "Prata med en jour elektriker inom 60 sekunder!" + Ring-only CTA + "5.0 på Google" + team image. | Centered stack. |
| 6 | Testimonials | "Vad säger dina grannar om Ampy?" Splide slider, 12 real Google reviews (mostly installation jobs; only Moa Olaussen's "Snabb hjälp när elcentralen strulade. Ampy dök upp direkt" is urgency-relevant), badge "5 av 5 · Betyg på Google". | 1-up swipe slider. |
| 7 | VarProcess | "Så funkar det … 1. Samtal med elektriker — **Fyll i formuläret** så ringer vår jourhavande elektriker i Täby upp dig direkt. 2. Offert & tidsförslag … 3. Bokning bekräftad … 4. **Installation utförd**". | 4 icon-boxes stack. |
| 8 | BlueCTA | "Prata med en jour elektriker! … när det som inte får hända, plötsligt händer." Single black Ring button. | Full-width card. |
| 9 | VissteDuAtt | "Visste du att.. Din hemförsäkring kan täcka kostnaden för eljour?" + ~180-word insurance explainer (localized: "Många villaägare och bostadsrättshavare i Täby…"). | Dark card stacks; long text block. |
| 10 | FAQ + accordion | 4 localized Q&As (pris, "inom en timme… Täby centrum och närliggande villaområden", försäkring — **"Då ROT-avdrag inte är tillämpligt på jourutryckningar blir försäkringsskyddet extra viktigt"**, när ska jag ringa). | Accordion, works. |
| 11 | MainContact | Left proof pane ("Från start till mål…", "5 av 5 · Betyg på Google", "**3 000+ genomförda installationer om året**", 3 steps incl. "**Vi ringer dig inom 24 timmar**") + right form: Förnamn/Efternamn/E-post/Telefon/Adress(gatuadress+postnr+postort)/Meddelande → "Gratis rådgivning". | Panes stack; 7+ visible fields. |
| 12 | ROT block (reworded) | "Sänk kostnaden för din eljour i Täby genom din **hemförsäkring**" + 3 steps ("Samtal med expert… förbereder allt underlag för försäkringbolaget" [sic], "**Installation av elektriker** … utför installationen", "Underlag till ansökan") → button **"Läs mer om ROT-avdrag"**. | Stacks. |
| 13 | MikroCTA | "Vill du veta mer? Prata med en av våra seniora jour elektriker och få reda på hur **Sveriges snabbast växande elfirma** kan dig när du behöver akut eljour" [sic — missing "hjälpa"] + CTA pair. | Photo band stacks. |
| 14 | ContentBlock | 3 alternating SEO rows: "Akut hjälp vid oväntade elfel dygnet runt" / "Professionell jourmontör för trygg felsökning" / "Säkra hemmet vid kortslutning och avbrott". | Image-over-text stacks; long scroll. |
| 15 | MapBlock | "Vi finns där du finns" + 20 random ort-buttons (Täby page lists Huddinge, Nynäshamn, Norrtälje…) + "Som ett rikstäckande nätverk…" + Kontakta oss sub-card. | Dot-map variant. |
| 16 | CEBlock | "Certifierad expertis när du behöver eljour i Täby" — genuinely local copy ("från de äldre villorna i **Näsby Park** till modernare fastigheter i **Täby Park**"; Huddinge: "**Stuvsta, Segeltorp och Flemingsberg**") + "Täcker hemförsäkringen din eljour?" + "Utöver vår eljour… kan vi hjälpa dig med" 6-item cross-sell list (incl. batterilagring) + CTA pair + 9:16 image. | Tall image + long text. |
| 17 | Certificates | Logo wall (Elsäkerhetsverket, Skatteverket, ID06, Trygg Hansa…). | Wraps. |
| 18 | FooterSEO | "Eljour Täby – på plats dygnet runt" + text + CTA pair. | Stacks. |
| 19 | Prefooter + Footer | Populära kategorier + navy footer + "5.0". | Accordion columns. |

Page-wide: **22 `tel:+46102657979` links** (Täby and Huddinge identical count). HTML alone ≈ **838–839 kB** (block-map size_kb) — consistent with the known ~9–10 s lab-LCP flag. Word count ≈ 2 800.

---

## Customer-flow walkthrough (35–65 y/o homeowner, 22:30, breaker keeps tripping, mobile)

**0–5 s:** Ad/SERP promise matches — title "Eljour Täby - akut elfel? Vi är på plats snabbt" → H2 with the phone number in it (Täby). Good message match (Google message-match doctrine). But the first CTA button is "Kostnadsfri rådgivning" (a *consultation* frame), and directly beneath the headline sits a **7-field quote form** whose sub-line promises "återkommer via telefon" — a callback, not help now. On a ~9–10 s LCP mobile connection the visitor may be staring at a blank hero for several seconds first.

**Scroll 1–2:** Past the form card, the visitor hits the symptom block — **the best thing on the page**: "Säkring löser ut … löser samma säkring ut gång på gång … är det en kortslutning eller ett glapp som kan värma en kabel du inte ser. Tvinga inte tillbaka den om och om igen. Ring oss så hittar vi felet." This is exactly severity-calibrated triage with a per-symptom Ring CTA. But by now the "Jour öppen just nu" call panel has scrolled away and there is no fixed call bar, so after reading their symptom the CTA is the in-panel text link only.

**Scroll 3+ (the calm-template tail):** The page then reverts to the planned-installation register: Metrics brag about "1000+ Nöjda kunder … installationer", VarProcess step 1 tells the emergency visitor to **fill in a form**, step 4 promises "Installation utförd"; MainCTA promises contact "inom 60 sekunder" while MainContact's own proof pane promises "Vi ringer dig inom 24 timmar"; a hemförsäkring block ends in a "Läs mer om ROT-avdrag" button two scrolls after the FAQ said ROT doesn't apply to jour. A stressed visitor who reads any of this either calls despite the page (best case) or feels the "will they actually come NOW?" doubt the Byggahus research says Swedish homeowners already carry.

**Decision:** The call happens IF the visitor meets the symptom block early enough and trusts "Målsättning att vara på plats inom en timme." Everything after block 3 is at best neutral, at worst actively contradicting the emergency promise.

---

## What works (keep)

1. **The symptom block itself** — severity-calibrated (Akut/Varning), 112/1177-first safety copy, candour-clean promises ("Målsättning att vara på plats inom en timme" — an ambition, not a fake guarantee; "Tydligt pris innan vi rycker ut, inga dolda avgifter"), the Elsäkerhetsverket grounding stat with named source, progressive disclosure ("Se fler tecken (6)"), per-symptom Ring CTA, a11y (aria-expanded, labelled region). This is the correct JTBD artifact for urgent intent and the template's signature device.
2. **Message-matched titles/meta** — "akut elfel? Vi är på plats snabbt" / "snabbt på plats inom 1h"; Täby's H2 puts the phone number in the headline (do this on all 56).
3. **Genuinely local copy** in FAQ + CEBlock (Näsby Park/Täby Park; Stuvsta/Segeltorp/Flemingsberg) — real local signal, not doorway-page filler. Preserve; it's also the E-E-A-T defense for 56 near-duplicate pages.
4. **FAQ answers the real decision questions** (price basis, response time, insurance vs ROT, when to call) — MECLABS HealthSpire logic says keep this content, just earlier-relevant framing is fine where it is.
5. **Honest insurance angle** (hemförsäkring often covers acute work + "vi hjälper dig med dokumentation") — a true differentiator and anxiety-reducer (MECLABS `a` term).
6. **12 real, named, dated Google reviews** — candour-compatible social proof (Cialdini), even if mis-sorted for this intent.

---

## Findings

**GEO-ELJ-01 — Hero is form-first on the one template where the form is the wrong first ask. Severity P0.**
Evidence: aof card renders beside/under the headline with kundtyp toggle + ärende + namn + telefon + e-post + adress + postnr (7+ visible asks; Baymard: visible/required field count drives perceived difficulty) and the sub-promise "återkommer via telefon" (callback framing). First hero CTA is "Kostnadsfri rådgivning" (form), phone second. MECLABS heuristic: for max-motivation urgent visitors the constraint is friction+anxiety, not motivation — every second of form is friction; Unbounce says urgent intent converts on the *call*. Mobile: the form pushes the symptom block ~1.5 viewports down; a 22:30 visitor must scroll past a quote form to reach triage. Fix: eljour hero variant — phone-dominant (single giant Ring CTA + "Jour öppen just nu" status), demote/remove the aof card (see wireframe).

**GEO-ELJ-02 — ROT/hemförsäkring block self-contradiction. Severity P0 (trust-damaging).**
Evidence: FAQ states "Då ROT-avdrag inte är tillämpligt på jourutryckningar blir försäkringsskyddet extra viktigt", yet block 12's button reads "Läs mer om ROT-avdrag", its step 2 says "Installation av elektriker … utför installationen" (installation language on a repair job), and it contains typos ("Vår experter", "försäkringbolaget"); MikroCTA has "…kan dig när du behöver" (missing "hjälpa"). Candour gate + NN/g credibility: visible internal contradiction and sloppy copy on a trust-critical page. Mobile: same. Fix: dedicated Hemförsäkring block (link → hemförsäkring/kundtjänst page), kill the ROT button on all 56 pages, proofread pass.

**GEO-ELJ-03 — Callback-SLA whiplash: "inom 60 sekunder" vs "inom 24 timmar". Severity P0.**
Evidence: MainCTA: "Prata med en jour elektriker inom 60 sekunder!"; MainContact proof pane on the same page: "Vi ringer dig inom 24 timmar"; VarProcess step 1: "Fyll i formuläret så ringer vår jourhavande elektriker i Täby upp dig direkt." Three different response promises for one emergency. Message match + candour: an unmet 60-second expectation is worse than none; a 24-hour promise on an eljour page kills the form path for genuinely urgent visitors. Mobile: MainContact's "24 timmar" sits directly above the form fields. Fix: one owner-confirmed jour-SLA `[GAP: verklig svarstid på jourlinjen + kvällscallback-SLA]`; the generic MainContact must not run unmodified on this template.

**GEO-ELJ-04 — Proof numbers contradict each other and trip the candour gate. Severity P1.**
Evidence: Metrics: "1000+ Nöjda kunder — Över tusen genomförda installationer är vårt absolut starkaste kvalitetsbevis"; MainContact: "3 000+ genomförda installationer om året". Both can't be the headline truth; "1000+ kunder" is on the banned-unless-owner-confirmed list, and "25+ Erfarenhet i branschen" doesn't say 25+ *what*. Additionally all Metrics copy is installation-framed ("dimensionerar och installerar din anläggning") — wrong JTBD here. "Sveriges snabbast växande elfirma" (MikroCTA) is an unanchored superlative (allowed per owner directive 2026-07-18 unless demonstrably false, but should carry an anchor). "5.0" appears in header/hero/footer without count. Mobile: Metrics is the first thing after the symptom block — the first proof the visitor sees is off-intent and self-contradictory. Fix: one canonical proof set `[GAP: owner-confirmed counts + Google rating w/ review count]`, eljour-relevant metrics (response ambition, jour coverage, antal jourärenden).

**GEO-ELJ-05 — Symptom block's call panel is not persistent: no sticky desktop panel, no fixed mobile call bar. Severity P1.**
Evidence: shipped CSS `50-eljour-lead-magnet.css` (7.7 kB) contains **zero** `sticky`/`fixed` declarations; `@media (max-width:992px){.eb__grid{display:block}}` stacks the call panel above the 14-symptom accordion, after which it scrolls away. The v3 owned concept (repo julius447/Eljour-block) specifies a sticky two-pane call panel + fixed mobile call-bar. Fitts's law: the conversion action should be permanently one thumb-reach away during triage. Per-panel "Ring eljouren" links partially compensate (22 tel links page-wide) but the collapsed-state list rows have no call affordance. Mobile: this is the single highest-leverage mechanical fix on the template. Fix: port the sticky/fixed behavior from the owned v3 block; approved-rendering rule applies — owner-gated visual diff before activating.

**GEO-ELJ-06 — Mid-page reverts to the calm installation template (sequencing, not content, is wrong). Severity P1.**
Evidence: blocks 4–7 and 12–14 are the generic service-page set: VarProcess step 4 "Installation utförd", testimonials ordered with installation reviews first (the one emergency review, "Snabb hjälp när elcentralen strulade… dök upp direkt" — Moa Olaussen — is buried mid-slider), ~1 500 words of ContentBlock/CEBlock before Certificates. MECLABS HealthSpire: length is fine when it answers decision questions — but here the decision questions for urgent intent are (kommer ni NU? vad kostar det? täcker försäkringen?) and they're answered at positions 3, 10 and 12 with installation content interleaved. Mobile: ~10+ viewports between symptom block and FAQ. Fix: re-sequence per wireframe below; rewrite VarProcess/Metrics/testimonial-sort for jour register; delete nothing (SEO preserved).

**GEO-ELJ-07 — No price anchor despite claiming price transparency. Severity P1.**
Evidence: symptom block promises "Tydligt pris innan vi rycker ut, inga dolda avgifter"; FAQ says "vi tillämpar alltid fasta inställelseavgifter" — but no number appears anywhere on 2 800 words. Byggahus/Reddit research anchor: final-price surprise is THE Swedish homeowner fear; competitors who print "fast inställelseavgift från X kr" win the comparison shop that happens even at 22:30. Candour gate: claiming transparency without a number is a soft contradiction. Mobile: same. Fix: price block or FAQ upgrade with real fixed call-out fee + vardag/kväll/helg matrix `[GAP: owner price card]`.

**GEO-ELJ-08 — H1 is the tiny eyebrow; heading hierarchy inverted. Severity P2.**
Evidence: `<h1 class="…hero_2__section-subheading">Eljour i Täby</h1>` — the visually dominant "Eljour dygnet runt: Ring 010-265 79 79!" is an H2; page has 16 H2s. Template-wide Hero_2 defect, but on 56 programmatic pages the H1 = exact-match geo phrase is at least SEO-consistent; the visual/semantic mismatch remains (NN/g hierarchy; screen-reader users hear the eyebrow as the page topic and the phone-bearing promise demoted). Mobile: same. Fix in the shared Hero_2 component (cross-template fix, counted once there too).

**GEO-ELJ-09 — Headline and hero copy quality varies randomly across the 56 pages. Severity P2.**
Evidence: Täby H2 embeds the phone number ("Eljour dygnet runt: Ring 010-265 79 79!"); Huddinge's does not ("Eljour dygnet runt i hela Huddinge!"). Titles also differ in promise ("på plats snabbt" vs "inom 1h" — the 1h title outpromises the body's "målsättning" phrasing). Message match should be uniform: strongest verified pattern on all 56. Mobile: headline is the LCP element. Fix: roll the phone-in-headline + "målsättning inom en timme" pattern programmatically.

**GEO-ELJ-10 — MapBlock claims collide with local positioning. Severity P2.**
Evidence: on the Täby page, "Vi finns där du finns … Som ett **rikstäckande nätverk**…" plus 20 random orter (incl. Nynäshamn, Södertälje). National claims are owner-allowed in copy, but placed directly under "lokalt verksamma i Täby" copy it dilutes the local trust story (Jakob's law: visitors read geo pages as "the local firm's page"). It's an internal-linking block, not a customer block. Mobile: 20 buttons of low-relevance tap targets. Fix: keep for SEO, move below CEBlock/Certificates, reframe intro to "Vi har jourelektriker i hela Stockholmsområdet" `[GAP: routing truth]`.

**GEO-ELJ-11 — Weight/speed: ~839 kB HTML, client-rendered hero form, known 9–10 s lab LCP. Severity P1 (mechanical).**
Evidence: block-map size_kb 838–839 for these URLs; aof form is injected by JS (empty `#ampy-form-root` at parse time); symptom block ships ~27 kB inline shortcode markup + duplicated grounding-stat DOM (`--d`/`--m` variants). HYPOTES (no field data cited): for urgent mobile visitors on cellular, each second of hero delay costs calls — treat LCP as a P1 workstream (defer non-hero Splide/map assets, server-render or placeholder the hero form). Mobile: the whole finding is mobile.

**GEO-ELJ-12 — MainContact form friction is unfit for the template's secondary (non-urgent) audience. Severity P2.**
Evidence: 7+ visible fields (Förnamn/Efternamn/E-post/Telefon/Gatuadress/Postnummer/Postort/Meddelande) against Baymard's visible-field principle, under a proof pane promising a 24 h callback. The legitimate users of this form on an eljour page are the *non-urgent* minority ("säkringen löste ut igår, kan vänta till imorgon"). Fix: explicit two-lane framing — "Akut? Ring." / "Kan det vänta? Bli uppringd i morgon bitti" — with a reduced field set (namn + telefon + valfritt meddelande). This preserves the form conversion path without cannibalizing calls.

---

## Recommended sequence (wireframe — eljour-i template, all 56 pages)

| # | Block | Why here | New/existing/modified |
|---|---|---|---|
| 1 | Header (eljour-aware: swap "Gratis rådgivning" CTA → "Ring eljouren" on this CPT) | The global CTA must not compete with the call on urgent pages | Modified (conditional) |
| 2 | **Hero_2 Eljour-variant**: H1 = real headline "Eljour i {ort} – akut elektriker dygnet runt", phone number in headline, ONE dominant Ring CTA + "Jour öppen just nu" status chip; right column = compact call panel (the eb aside promoted) — **no aof form** | Phone must dominate; kills GEO-ELJ-01/-08/-09 in one component | Modified (major) |
| 3 | **Symptom block** with restored sticky desktop panel + fixed mobile call-bar (owned v3 spec) | The signature device, now the hero's direct continuation; persistent call affordance during triage (Fitts) | Modified (CSS port, owner-gated visual diff) |
| 4 | **Jour-proof strip** (replaces Metrics): "Målsättning: på plats inom 1h" · "Dygnet runt, året om" · anchored Google badge (rating + count) `[GAP]` · Elsäkerhetsverket-auktoriserad | First proof after triage must be emergency-relevant and candour-anchored (GEO-ELJ-04) | Modified |
| 5 | **Vår process Eljour-variant**: 1. Ring — prata direkt med elektriker 2. Tydligt pris innan utryckning 3. Felet åtgärdat + hemmet säkrat 4. Dokumentation till din försäkring | Call-first steps; removes "Fyll i formuläret"/"Installation utförd" (GEO-ELJ-06) | Modified |
| 6 | **Pris & hemförsäkring block** (replaces ROT block): fast inställelseavgift `[GAP: belopp + dag/kväll/helg]` + försäkring täcker ofta + dokumentationslöfte; button → hemförsäkring/kundtjänst, **not ROT** | Answers the #2 decision question with a number; kills GEO-ELJ-02/-07 | New (from ROT-block shell) |
| 7 | FAQ (existing localized Q&As, price answer upgraded with the number) | Already the right content; earlier = decision support (HealthSpire) | Existing (copy patch) |
| 8 | Testimonials, emergency/service reviews sorted first | Right proof, right order (Cialdini; GEO-ELJ-06) | Modified (sort) |
| 9 | **Two-lane contact**: MainContact Eljour-variant — left pane: "Akut? Ring 010-265 79 79" (giant) / right: "Kan det vänta? Bli uppringd `[GAP: SLA]`" with namn+telefon(+meddelande) only; one truthful callback promise | Preserves form path for non-urgent lane without SLA whiplash (GEO-ELJ-03/-12) | Modified (major) |
| 10 | VissteDuAtt (hemförsäkring editorial) + ContentBlock (3 SEO rows) + CEBlock (local expertise + cross-sell) | ALL SEO substance preserved, consolidated into one calm long-form tail after both conversion moments | Existing (re-sequenced) |
| 11 | Certificates | Authority close for the long-form readers | Existing |
| 12 | MapBlock (reframed intro, below the fold-tail) | Internal linking retained; local story no longer diluted mid-page (GEO-ELJ-10) | Modified (copy + position) |
| 13 | FooterSEO ("Eljour {ort} – på plats dygnet runt") → Prefooter → Footer | Existing close | Existing |

Removed from template: standalone MainCTA, BlueCTA, MikroCTA (their job — "ring" — is now done by hero, sticky bar, and blocks 4/9; cutting them reduces the 22-tel-link/CTA proliferation and ~2 viewports of scroll). Their H2 copy that carries SEO value ("Prata med en jour elektriker") folds into blocks 5/9.

**Template priority score:** 56 pages × 3 (hero/form position) × 3 (high expected effect, urgent-intent benchmark) = **504** — the highest-leverage template in the audit after the homepage.

---

## Test hypotheses (top 3, A/B)

1. **HYPOTES (hero):** Replacing the aof form card with a phone-dominant call panel ("Jour öppen just nu" + single Ring CTA) on eljour-i pages will increase tel-click rate per session by ≥30% without reducing total leads (calls + forms), because urgent visitors convert on the call and the form only defers them. Measure: `tel_click` + form submits per session, 28 days, 56 pages bucketed A/B by ort.
2. **HYPOTES (sticky call bar):** Adding the fixed mobile call-bar during symptom-block interaction will lift mobile tel-clicks among visitors who open ≥1 symptom panel by ≥20% vs. the scrolling panel, per Fitts's-law persistent affordance. Measure: tel_click conditioned on `eb_panel_open` event (instrument the accordion).
3. **HYPOTES (price anchor):** Publishing the fixed inställelseavgift (amount + kväll/helg matrix) in block 6 + FAQ will increase call rate and reduce pogo-sticking (return-to-SERP) vs. "tydligt pris" without a number, per Byggahus price-uncertainty findings — anxiety reduction outweighs sticker-shock loss. Requires owner price card first `[GAP]`.

---

## Open [GAP]s for the owner
1. Real jour phone-answer SLA + evening/night callback truth (blocks 2/9; kills the 60 s-vs-24 h contradiction).
2. Fixed inställelseavgift amounts (dag/kväll/helg) for the price block.
3. Canonical proof set: installations count (1000+ total vs 3 000+/year?), Google rating + review count, "25+" definition.
4. Confirm sticky/fixed call-bar port from the owned Eljour-block v3 (visual diff sign-off — approved-rendering rule).
5. MapBlock routing truth ("rikstäckande nätverk" vs 27-kommun ops routing) for the reframed intro.
