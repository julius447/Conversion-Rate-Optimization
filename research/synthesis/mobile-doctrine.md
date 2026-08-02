# Mobile Experience Doctrine (BINDING)

Synthesis lens: mobile. Consolidates every mobile finding from the 14 template deep-dives + 20 block audits into one binding doctrine. Sources cited by finding-ID (e.g. H2-01 = `blocks/hero2-form.md`; GEO-ELJ-05 = `templates/geo-eljour.md`). Where template agents disagreed, this file resolves the conflict and names the trade-off (§6).

## 0. Why mobile is the primary rendering (evidence, not assumption)

- **53% of organic clicks are mobile** (GSC 2026-05→08: 176 mobile / 152 desktop / 5 tablet), and paid/local intent skews higher — method doctrine assumes **≥65% mobile for paid/local**.
- The only recorded paid conversions were **2 phone clicks; 0 form starts** across ~32 paid sessions — the phone is the conversion that works on mobile, and the form funnel is both unmeasured (no `form_start` emitted — H2-02, MC-07) and mechanically suppressed (JS-injected hero form, ~9–10 s lab LCP — SVC-01, GEO-02).
- **Verified live (2026-08-02):** the enterView fadeIn interaction left a full homepage viewport **blank** (`.brxe-cgamzx` inner container at `opacity:0` at y≈1000, reproduced twice) — on a slow mobile main thread this class of failure is sitewide (§4).
- The audience is 35–65, risk-averse, presbyopia-onset: every mobile rule below is calibrated to older eyes and thumbs (WCAG 2.5.8 / Apple 44 px / Android 48 dp; ≥4.5:1 body contrast; weight ≥400 on dark surfaces).

**Doctrine rule 0: every template/block change in this program is specified mobile-first at 390×844 and verified there before desktop.** SEO substance is never deleted — repackaged and re-sequenced only (MECLABS HealthSpire: order, not length, is the variable).

---

## 1. The first-viewport budget @ 390×844 (what MUST be visible before any scroll)

Arithmetic: 844 px minus sticky header (~64 px) leaves **~780 px**. Budget allocation (hard caps): headline ≤2 lines (~120 px) · sub-line ≤2 lines (~90 px) · ONE ask ≥48 px tap target · trust anchor 1 line (~28 px). The cookie banner may not overlay the trust anchor (verified defect on homepage first load — live-browser-observations #4): consent UI must render as a bottom sheet *below* the hero trust row or the trust row is repositioned above the banner's top edge.

**Four mandatory elements per first viewport: (1) value headline, (2) price/cost-certainty signal, (3) exactly ONE primary ask, (4) one anchored trust element.** Two equal-weight CTAs in the first viewport are banned everywhere (Hick's law; H2-01, SVC-04). All `[GAP]` items = owner-confirm before ship (candour gate).

| Template (pages) | Headline | Price signal | The ONE ask | Trust anchor | Banned from viewport 1 |
|---|---|---|---|---|---|
| **Service /elservice/* (22)** | H1 = value headline w/ query keyword ("Byta elcentral — fast offert med 30 % ROT") — re-tagged per H2-03 | "fr. X–Y kr efter ROT" or "fast offert innan arbetet påbörjas" (SVC-02; content already exists in FAQ) | Server-rendered short form (namn/telefon/postnr) top of stack; compact Ring line beneath (not an equal button) | "5,0 av 5 · N recensioner på Google" `[GAP: N]` | Second gradient CTA; Adress field; JS-only form |
| **Geo elektriker-i / elinstallation-i (112)** | "Elektriker i {ort} — fast pris i offerten" (GEO-03/GEO-04: substantiate the SERP's "fast pris" or rewrite the title) | Fixed-price promise + hourly range efter ROT (650–950 kr/h exists in FAQ) | Same form-first stack as service | Anchored rating + "Registrerad hos Elsäkerhetsverket" strip | CTA that navigates to /kontakt/ (GEO-01) |
| **Geo laddbox-i (56)** | "Laddbox installerad i {ort} — fr. X kr efter 50 % Grön Teknik" (X = ONE reconciled figure; GEO-09 contradiction 4 190 vs "från ca 5 000") | The from-price IS the signal | Form-first stack (product preselect kept) | Anchored rating | 4-card ProductGrid before proof (GEO-05/PG-1) |
| **Geo eljour-i (56) + /eljour/ pillar** | H1 with phone number in the headline ("Eljour i {ort} — Ring 010-265 79 79", Täby pattern rolled to all 56; GEO-ELJ-09) | "Tydligt pris innan vi rycker ut" + real inställelseavgift `[GAP: belopp dag/kväll/helg]` (GEO-ELJ-07) | **ONE giant Ring button + "Jour öppen just nu" status. NO form in viewport 1** (GEO-ELJ-01, PIL-03) | "Målsättning: på plats inom en timme" + Elsäkerhetsverket fire stat | The aof form card; "Kostnadsfri rådgivning" framing; calm cabin imagery |
| **Homepage (1)** | Keep "Elinstallationer i hemmet, gjort ordentligt." (approved, locked) | Not required — 73 % of organic clicks are branded trust-verifiers (GSC); the homepage's viewport-1 job is verification, not pricing | Single CTA → anchor `#radgivning` (on-page MainContact), not /kontakt/ (HP-03; owner-gated — locked design) | Anchored "5,0 · N på Google · 3 000+ installationer" `[GAP]`, NOT hidden behind cookie banner | 33 000-kr battery cards anywhere near the fold (HP-01) |
| **Pillars Hero-1 (4: elektriker/elinstallation/laddbox/eljour)** | H1 paints with HTML — remove `hidden-on-load` + fix gradient contrast 1.85:1 (F3) | Verifiable price promise replaces "marknadens billigaste" (F7 ⚑) | Compact 3-field capture or anchor-CTA to MainContact (PIL-04: first form currently 8–12 mobile screens down) | Anchored rating (F6) | Typo-button "radgivning" (F1); staging 404 preload (F2) |
| **Product pages (26)** | H1 + product; price+ask must land within screens 1–2 (mobile currently: breadcrumb+photo fill screen 1) | "Efter 50 % Grön Teknik: X kr, standardinstallation" — no fake strike-through (PP-03), FAQ price aligned (PP-01) | Inline 3-field mini-form (popup demoted; PU-1/PP-04) | Named expert + "5,0 · 25 omdömen" (PP-05); phone affordance survives stacking (PH-4) | 5-required-field scroll-locked modal as the only ask |
| **Category hubs (4: elservice/laddboxar/solcellsbatterier/nyheter)** | Real `<h1>` (currently `<h3>`, no H1 — CAT-03/AH-01) | Grid from-prices + "pris efter avdrag"-klargörande (CAT-07) | Tel-link in a compact hero trust row (AH-03) | Anchored rating row | 4xl mobile padding that spends viewport 1 on waves (AH-04: cap hero so first routing/product row is visible within ~700 px); dead unclickable service grid (CAT-01) |
| **Elektriker-för-X B2B (11 of 13)** | H1 vertical headline (message match already good) | "Fast offert / ramavtal" framing | Hero form (org-aware resolver kept) with SSR fallback (EFX-05) | **Org-trust strip: ID06 · Trygg Hansa · Elsäkerhetsverket** within screen 2 (EFX-02 — currently position 12) | Consumer "grannar" review slider as screen 2 (EFX-01) |
| **Articles (11)** | H1 + excerpt answering the query (already the site's best; keep) | The price answer already in excerpt/Snabbt svar | No hero ask — the ask arrives as inline CTA at 25–35 % depth + Nästa-steg card (ART-01); sticky mini-bar per §2 | Byline trio + "5.0 · 25 omdömen" (already anchored — the site's model) | Review-beg card at the decision point (ART-02) |
| **Lead magnets (7)** | Benefit H1 ("Vad sparar du…?") ≤1 compact AlternativHero screen | The calculator IS the price signal | First calculator input visible in viewport 1; embedded 4-field lead form stays value-then-ask | "Så har vi räknat" + Elsäkerhetsverket sourcing (elkollen pattern) | Any second fixed bar (see §2 — energikalkylatorn's sticky result bar owns the bottom edge) |
| **Kontakt (1)** | New H1 "Kontakta Ampy — kostnadsfri rådgivning" (KO-2: page has no H1) | "Kostnadsfri" + öppettider `[GAP]` | **Phone row (tel + hours) + first form field within viewport 1** — mobile order form-first, condensed trust strip above it (KO-1/KO-4: today mobile viewport 1 is a photo panel with a quote, zero tel links in body) | Anchored rating + "Vi ringer dig inom 24 timmar" | Required Adress for a phone callback (KO-3) |
| **Thank-you (1)** | Confirmation H1 (keep) | n/a | "Spara numret: 010-265 79 79" as a tap-to-save `tel:`/vCard target (TY-01 — mobile-native one-tap; page currently has zero tel links) | Exact promise restated: "inom 24 timmar" — never "inom kort" (TY-2) | Indexable conversion pageview (TY-03/TY-1 — noindex + event-gated conversion first) |
| **Team pages (6)** | H1 = full name + role (currently h3, no H1 — TEAM-03) | n/a | Expert phone-card within screen 2 (TEAM-02: today 0 tel, 0 CTA, 0 form in body) | Credential chips in hero: Auktoriserad · ECY · X års erfarenhet (TEAM-08) | — |

---

## 2. Sticky / persistent mobile CTA spec

### 2a. Where a fixed bottom call-bar IS warranted

**Fitts reasoning:** a fixed bar puts the conversion permanently one thumb-reach away — worth its ~7 % viewport tax only where (a) the call is the primary conversion for the intent, (b) the page is long enough that in-flow CTAs scroll away, and (c) no other fixed element owns the bottom edge.

| Surface | Verdict | Basis |
|---|---|---|
| **eljour-i (56) + /eljour/ pillar + /ampy-eljour/** | **SHIP — always-on, not a test.** | Urgent intent converts on the call (Unbounce); shipped CSS has **zero** sticky/fixed rules — the "Jour öppen just nu" panel scrolls away mid-triage (GEO-ELJ-05); the owned Eljour-block v3 spec already includes the fixed bar (/ampy-eljour/ ships 26 sticky/fixed rules — port it). Owner-gated visual diff (approved-rendering canon). |
| **Urgent-intent service pages** (felsokning-av-el, jordfelsbrytare, elbesiktning class) | **SHIP with the call-first hero variant** (service-pages divergent alternative). | Same Unbounce urgent-repair logic; these pages drop the hero form entirely, so the bar is the persistent ask. |
| **Articles (11)** | **TEST** (ART-05 / articles-H3): dismissible mini-bar "Ring · Få prisförslag", appears at 40–60 % scroll. | 17-minute reads with zero in-body conversion affordance; guardrail: dismiss rate <40 %, read-completion neutral. |
| **Geo elektriker-i / elinstallation-i / laddbox-i (168)** | **TEST, sequenced AFTER the anchor-retarget + SSR-form tests** (GEO-10: "run after 1–3 to avoid interaction effects"). | Long pages (19–22 blocks) with the form 10+ screens down; but the primary fixes (CTA anchors, SSR form) may absorb the need — do not confound the experiments. |

### 2b. Where it is NOT warranted (and why)

- **Homepage:** brand-verification traffic; header phone affordance (§5) suffices; a permanent bar trains banner blindness on the page every organic visitor sees, and the locked hero design is owner-gated.
- **Lead magnets:** the energikalkylatorn **sticky result bar already owns the bottom edge** — two stacked fixed bars are banned (rule: max ONE fixed bottom element per page, ever). The magnets' conversion is the embedded value-then-ask form, not a cold call.
- **Kontakt / Thank-you:** the page IS the conversion surface; a bar would compete with itself (attention ratio). Kontakt gets the in-flow phone row instead.
- **Product pages:** the scroll-locked popup + iOS keyboard already fight for the bottom edge (PU-1); fix the modal first, keep a compact in-flow phone affordance under the price CTA (PH-4).
- **Reachability reasoning:** the bottom ~120 px of modern phones is contested by OS gesture zones — the bar must sit above `env(safe-area-inset-bottom)`; anything we place there must be deliberate, singular, and high-value, or it generates mis-taps for 55–65-year-old thumbs.

### 2c. Exact behavior spec (binding for every instance)

1. **Structure:** full-width bottom bar, height 56–64 px + `padding-bottom: env(safe-area-inset-bottom)`; primary `tel:+46102657979` button ≥48 px ("Ring 010-265 79 79"; eljour: "Ring eljouren"); optional secondary "Få offert" = smooth-scroll anchor to the on-page form (never a /kontakt/ navigation).
2. **Appearance threshold:** eljour = visible from load (urgency has no threshold). All others = appear only when the hero's own ask leaves the viewport (IntersectionObserver on the hero form/CTA; articles 40–60 % scroll) — a bar competing with the hero's ask violates the one-ask rule.
3. **Dismissibility:** eljour = not dismissible. Articles/geo = dismissible (≥44 px close target), dismissal persisted per session.
4. **No-CLS:** `position:fixed` (out of document flow — zero layout shift by construction); enter/exit animate `transform: translateY` + opacity only, never height; no reserved spacer. Honors `prefers-reduced-motion`.
5. **Coexistence rules:** hides while any form field is focused (keyboard up); z-index below the cookie consent sheet; **never rendered on a page with another fixed bottom element** (energikalkylatorn rule); on eljour the bar *replaces* the header's form-CTA as the page's persistent ask — never two persistent asks at once (§5 + HDR-01 resolution, §6-c2).
6. **Instrumentation:** emits `tel_click` / `cta_anchor_click` with `source_block: 'sticky_bar'` + template dimension — the GEO-ELJ hypothesis (tel-clicks conditioned on `eb_panel_open`) requires it.

---

## 3. Mobile form doctrine

**The locked minimum lead = namn + telefon + postnummer (+ GDPR).** Everything else is progressive disclosure or collected on the 24 h call. (Baymard: visible/required field count drives perceived difficulty; MC-03, H2-04, SVC-08, KO-3.)

### 3a. Field order (all forms, mobile)
1. Kundtyp: **silent default privat** on the 224 geo + 22 service pages; visible toggle only on elektriker-för-X where kundtyp is genuinely ambiguous (H2-08 — the resolver's EFX map already flags exactly these).
2. Ärende/"Vad gäller arbetet?": prefilled + locked-but-editable per page (keep the resolver — it is the form's best asset).
3. **Namn** (single field — the Förnamn/Efternamn split is CRM tidiness, not user value; MC-03).
4. **Telefonnummer**.
5. **Postnummer** (routes the lead; the 27-kommun ops set needs nothing finer).
6. E-post → optional. **Adress → demoted to "Fler detaljer (valfritt)"** (H2-04; KO-3: required street address before any value is the documented Swedish-homeowner anxiety spike). Relabel the disclosure benefit-first: "Beskriv jobbet eller ladda upp en bild — då kan vi ge ett snabbare besked" (H2-09; photo of the proppskåp is the highest-quality enrichment).
7. GDPR consent → submit.

### 3b. Keyboard & input types (binding)
- Telefon: `type="tel"` (keep the E.164 normalization).
- Postnummer: `inputmode="numeric" pattern="\d{5}" autocomplete="postal-code"`.
- E-post: `type="email" autocomplete="email"`; Namn: `autocomplete="name" autocapitalize="words"`.
- **All inputs ≥16 px font-size** (prevents iOS auto-zoom), fields single-column at ≤478 px, tap targets ≥48 px.
- Google Places autocomplete stays but never `required` (KO-3: iOS keyboard + Places is an extra friction step).
- Error copy inline in Swedish (already good — keep), `aria-live` regions kept.

### 3c. The aof hero form's mobile position relative to the CTAs
Current (verified): text column → two full-width gradient CTAs (the first navigating to /kontakt/) → rating → form card 1.5–2 screens down, **and the form does not exist until a 56 kB deferred `data:`-URI script runs** (H2-01, H2-07, GEO-02, SVC-01). Doctrine:
- **≤767 px stack order: H1 → one-line sub → FORM CARD → compact Ring line → rating.** The form — not a detour button — is the first thumb-reachable action (H2 rec #2). Eljour templates invert: Ring primary, no form card in the hero (§1).
- **Server-render the form shell** (title + first fields + submit) so the slot is visibly a form at first paint; JS hydrates the resolver (H2-07, GEO-02 — the plausible mechanical cause of "0 form starts" on paid traffic).
- Kill the runtime-injected second `<h1>` in the card (GEO-05/EFX-08).
- Surface: test a light card (#f5f9ff) on the navy hero (H2-06 — navy-on-navy with 12.5 px consent text at opacity .82 fails older eyes); consent/help text ≥14 px, no sub-.9 opacities on navy.

### 3d. MainContact mobile stack order (295 pages)
Current mobile (verified CSS, MC-04): logo hidden, **volume proof hidden**, quote blown to display size clamped at `15ch` (~5 lines), **3-step strip incl. "Vi ringer dig inom 24 timmar" moved BELOW the form** — the visitor learns what happens next only after submitting. Doctrine:
1. Condensed trust strip ABOVE the form: anchored rating + ONE hard proof line (restore "3 000+ installationer" only once owner-anchored `[GAP]`).
2. Quote compressed to body size (kill the 15ch display treatment).
3. Form fields (3a diet).
4. **The 24 h promise rendered as microcopy directly under/above the submit button: "Skicka in — vi ringer dig inom 24 timmar."** The anxiety-reducer must sit at the decision point, not after it (MECLABS −2a).
5. Full 3-step strip below for readers.
6. Remove `data-interaction-hidden-on-load` from this block — **a form must never depend on an animation to exist** (MC-09; see §4).

### 3e. Instrumentation prerequisite (blocking)
No mobile form change is testable until both form systems emit `form_start` (first focusin), per-field abandon, `form_error`, `form_submit_error` — consent-gated per the playbook contract (H2-02, MC-07, SVC-10, PU-4). Ship instrumentation first, in week 1, with the thank-you pixel fix (TY-03: noindex + submit-event-gated conversion).

---

## 4. The animation / performance kill-list

Context multiplier: ~9–10 s lab LCP, 723–877 kB HTML per page. On mobile every item below compounds into blank screens, late-painting asks, and attention theft. **Rule: content and conversion surfaces are never JS-gated; animation is decorative-only, CSS-driven, `prefers-reduced-motion`-guarded.**

| # | Defect | Where (verified) | Expected mobile impact | Fix |
|---|---|---|---|---|
| 1 | **enterView fadeIn `opacity:0` bug — VERIFIED LIVE.** `data-interaction-hidden-on-load="1"` leaves sections invisible when the interaction JS hasn't fired; reproduced twice on the homepage (blank viewport, DOM at opacity:0) | Nearly every section: MainContact (MC-09), Metrics (MET-08), Certificates (CERT-05), ContentBlock (CB-05), FooterSEO (FS-5), VarProcess (VP-7), AlternativHero **first screen** (AH-02), pillar Hero-1 **H1** (F3), MapBlock image, /elservice/ services grid (CAT-01) | Fast-scrolling or JS-delayed mobile visitors meet empty screens where the trust content, the process block, or **the form** should be; on a 9–10 s-LCP stack this is a sitewide conversion-surface lottery | Strip `hidden-on-load` from ALL content/conversion blocks sitewide (one Bricks interaction sweep); keep entrance effects only as CSS that never hides pre-JS content. Also fix the Metrics `animationDelay:"1,5"` comma-locale bug |
| 2 | **Swinging lightbulb** — 4 s swing, 2 s delay, no reduced-motion guard, absolute PNG whose mobile clearance hack (`margin-top: 3xl/4xl`) spends the card's top band on dead space | VissteDuAtt, 290 pages (VDA-02) | Motion is the strongest peripheral attention magnet — deployed at ~70 % depth against the deep-scrollers (17/32 paid sessions) we can least afford to distract; WCAG 2.3.3 gap | **Ship the already-built redesign** (stacked, bulb/swing killed, #010328→#090b32) — slutaudit GO exists; owner-gated visual diff |
| 3 | **Autoplay carousels** | Testimonials Splide 4000 ms (T-03/T-04: mobile 1-up, `arrows:false`, 4 dots for 12 slides, sub-line `display:none` on mobile); TeamSection 3000 ms (TB-03) | Testimonials: 1-in-12 chance the single visible mobile card matches the page's vertical; 11 proofs invisible. Team: ~90-word bios yanked every 3 s — unreadable for the 35–65 reader; `pauseOnHover` does not exist on touch (WCAG 2.2.2) | Kill autoplay on mobile; add next-card peek (`padding-right`) + arrows; pin vertical-matched review as slide 1; restore the mobile sub-line. Testimonials V1 is LOCKED → all visual diffs owner-gated |
| 4 | **Double-rendered DOM** | ProductHero spec+process accordions ×2 (PH-1, 26 pages, in the LCP viewport); incentive-block dual icon `<img>`s per item (INC); pillar hero photo downloaded twice, both `eager fetchpriority=high` (F4, ~200 kB); entire nav tree rendered twice — 68 anchors / 148 kB header on every page (GLOB-07/HDR-03) | Pure transfer+parse tax on 780–877 kB pages feeding the 9–10 s LCP; the duplicate eager hero fetch competes inside the LCP window on 4G | One accordion instance repositioned with CSS `order`; one nav source; media-split preloads (the homepage hero already does this correctly — 31 kB mobile AVIF; copy the in-house pattern) |
| 5 | **404 staging preload** — `<link rel=preload fetchpriority=high href="https://staging.ampy.se/…/hero-bg-1.webp">` + same URL as the banner background; HTTP-verified **404** | Pillar Hero-1, 5 pages (F2) | A high-priority request + DNS/TLS to a dead staging host inside the LCP critical window; the design's background silently never renders; staging hostname leaking into production | Delete the preload; repoint or remove the background (removal is the pixel-identical option — approved-rendering safe). Week 1 |
| 6 | **56 kB data:-URI deferred form script** builds the entire hero form client-side | All 260 Hero_2 pages (H2-07) | The money element paints last on the slowest devices; empty navy box during the seconds a paid visitor decides to stay (Clarity 1 s / 23 s abandons) | SSR the shell (§3c); move the script off the data: URI so it caches |
| 7 | **Cookie banner overlays the hero trust row** on first load | Homepage, verified live (obs #4) | The anchored "5,0 på Google" row is hidden at the exact moment a first-time visitor evaluates the hero | Bottom-sheet consent that never covers the trust anchor (§1) |
| 8 | Gradient headings JS-rewritten post-DOMContentLoaded; pre-JS state fails contrast (MainCTA whole-H2 at 2.05:1; pillar H1 1.85:1 on white) | MainCTA 268 pages (MC-1), pillar Hero-1 (F3) | Slow mobiles show near-invisible headlines until JS runs — in sun glare, effectively blank | Solid-color pre-JS fallback; darken gradient stops to ≥3:1; server-side last-word wrap. Owner-gated visual diff |

---

## 5. Mobile nav: phone reachability + offcanvas restructure

**The single highest-scoring finding in the whole program is mobile-first: HDR-01 (325 × 3 × 3 = 2 925).** The desktop header has **no phone at all**; on mobile the only tel affordance sits inside the offcanvas — 2 interactions away, with nothing in the bar signaling it exists. GA4: phone clicks are the only conversions that fire. Jakob's law: every Swedish trade site puts the number in the top bar.

Binding spec:
1. **Phone in the bar itself, all breakpoints.** Mobile: a `tel:` icon-button (≥48 px) between logo and hamburger — outside the menu. Desktop: visible "Ring 010-265 79 79" text link beside the CTA. On the 57 eljour pages the phone becomes the header's primary CTA (conditional per CPT).
2. **One CTA label sitewide** ("Kostnadsfri rådgivning" — ends the Gratis/Kostnadsfri/Boka/Support 8-label split, GLOB-03/HDR-02); header CTA anchor-scrolls to the on-page form where one exists, /kontakt/ only where none does. On /kontakt/ itself, swap the self-referential CTA for the phone (GLOB-14).
3. **Offcanvas restructure** (keep the verified-good collapsed-accordion shape): (a) **the entire row is the toggle**, not the unnamed inner button — observed taps on label/chevron did nothing (GLOB-13, Fitts for 45–65 thumbs); (b) name every toggle button (WCAG 4.1.2 — screen readers currently hear "button" three times) and fix `aria-label="Öppna"`/"close" (HDR-05); (c) **Eljour promoted to top level** — an acute-fault visitor currently needs burger → Tjänster → Populära → Eljour = 4 taps (GLOB-06); (d) anchor the offcanvas "5.0" chip ("5,0 · N omdömen på Google" `[GAP]`); (e) "Ring en expert" stays visible-on-open (verified good — keep).
4. **Menu hygiene feeding mobile:** rename "Elcentralkalkylator"→"Elcentral-kollen" (label = landing H1); kill the Privatperson/Elektriker duplicate door; single nav DOM source (kill the 68-anchor duplication, §4-4); prefooter "Områden" 3 links → 6–10 + "Alla områden →" hub (GLOB-10, feeds 224 geo pages).
5. **Tap-target floor sitewide:** MapBlock ort buttons measured ~22–26 px tall at 5 px gaps (MAP-05 — at/below the WCAG 2.5.8 floor, mis-taps land on the wrong ort's doorway page). Rule: **≥44 px height, ≥8 px gaps for all mobile link grids**; collapse the 20-ort wall behind "Visa områden nära dig" (content stays in DOM).

---

## 6. Adversarial resolutions (where agents disagreed — decision + trade-off)

**c1 · Form-first vs call-first mobile hero.** The Hero_2 audit prescribes form-above-CTAs on mobile (H2 rec #2); the GA4 reality and Unbounce say the phone is what converts. **Resolution: split by intent.** Planned-improvement templates (service, geo elektriker/elinstallation/laddbox, elektriker-för-X, products) = form-first with a compact Ring line always in viewport 1. Urgent templates (eljour ×57, felsökning-class) = call-first, no hero form. *Trade-off named:* form-first risks suppressing the one path that demonstrably works — mitigated by keeping the phone visible in viewport 1 everywhere and by the instrumentation gate (§3e) so the split is measurable within 28 days.

**c2 · Header phone button AND sticky bottom bar = double persistent chrome.** HDR-01 wants the phone in the bar; GEO-ELJ-05/ART-05 want bottom bars. Both persistent asks at once = banner blindness + ~15 % combined viewport tax. **Resolution: header phone ships sitewide (it is the 2 925-score fix); the bottom bar ships only per §2a, and where it renders it is the page's ONE persistent ask** (on eljour the header shows logo + burger only; the bar owns the call). *Trade-off:* eljour loses the header ask — acceptable because the bar is strictly more thumb-reachable (Fitts).

**c3 · Sticky call bar vs energikalkylatorn's sticky result bar.** Two fixed bottom elements would stack. **Resolution: max one fixed bottom element per page; magnets keep the result bar (it carries the tool's value), get no call bar.** *Trade-off:* magnet visitors keep a 2-interaction call path (header icon) — acceptable since magnet conversion is the embedded form.

**c4 · MainContact mobile "owner call" hid the volume proof; this doctrine restores a proof line.** Not a contradiction of the owner: the candour gate blocked the *unanchored* claim; **the doctrine restores exactly ONE proof line only after owner anchors it** (`[GAP: 3 000+/år basis]`; the 1 000+ vs 3 000+/år contradiction — OM-1/GEO-04/PIL-07 — must resolve to one canonical figure first).

**c5 · Viewport budget vs SEO length.** Compressing viewport 1 and collapsing the ort wall/ContentBlock slabs never deletes text — accordion/"visa alla" repackaging keeps everything in DOM (method doctrine §3; HealthSpire). Mobile-first ≠ shorter pages; it means the first 780 px are spent on the four mandatory elements.

**c6 · Locked designs (homepage hero, Testimonials V1) vs mobile fixes.** Every pixel-visible change on a locked block (hero CTA target, mobile peek, sub-line restore, gradient stops) is **owner-gated with a before/after visual diff** (approved-rendering canon). Zero-visual-diff fixes (h3→h1 retags, preload deletion, instrumentation, `hidden-on-load` removal on invisible-until-JS content) ship in week 1 without the gate.

**c7 · Sticky-bar rollout order on geo templates.** The elinstallation/laddbox agent explicitly sequences the bar AFTER the anchor-retarget + SSR-form tests (interaction effects); the eljour agent wants it now. **Resolution: eljour ships (its evidence is mechanical — the panel scrolls away mid-triage and the built v3 spec exists); geo waits its test slot.**

---

## 7. Week-1 mobile punch list (all zero/near-zero visual diff)

1. Instrument both form systems + sticky-bar events; thank-you `noindex` + submit-event conversion (§3e, TY-03).
2. Strip `hidden-on-load` from all content/conversion blocks; fix the `"1,5"` delay bug (§4-1).
3. Delete the staging.ampy.se 404 preload; fix "radgivning" in the shared button library (~290 pages); fix the batterikalkylator/battery-calc error-state phone 010-123 45 67 → 010-265 79 79 (LM-01/PP-02/CAT-02).
4. Header phone icon-button on mobile + desktop tel link (HDR-01); name the offcanvas toggle buttons, whole-row tap targets (GLOB-13).
5. h3→h1 retags (hubs, magnets, team — AH-01/CAT-03/TEAM-03); Hero_2 H1/H2 re-tag + de-H1 the injected form title (H2-03).
6. Kill TeamSection autoplay on mobile (TB-03).
7. Owner `[GAP]` sheet: rating + review count; ONE installations figure; 60-sekunder SLA; jour-SLA + inställelseavgift; laddbox canonical from-price.
