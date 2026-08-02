# Global journey: Header, Footer, Prefooter & cross-page flow

URLs analyzed (live-fetched 2026-08-02): https://ampy.se/ · https://ampy.se/elservice/elcentral/ · https://ampy.se/kontakt/ — plus raw snapshots (`data/pages/home.html`, `elcentral-*.html`, 36 files) and `data/block-map.json`.
**Pages using this template: 325 of 326** (Header + Prefooter/Footer on every crawled page except /thank-you/, which is a deliberately chrome-free full-viewport card — the only page without global nav).

---

## Current verified sequence (desktop / mobile)

### Header (sticky, `#brx-header.brx-sticky`, bg #f5f9ff)
1. **Skip links** — "Hoppa till huvudinnehåll / Hoppa till sidfot" (good a11y, both platforms).
2. **Logo** → https://ampy.se.
3. **Mega-menu "Tjänster"** — 4 columns:
   - *Elinstallationer* (WP menu, 6 links: Byte av elcentral → /elservice/elcentral/, Elbesiktning, Felsökning av el, Jordfelsbrytare, Lastbalansering, Smarta hem)
   - *Belysning* (5 links: Inomhus-/Utomhusbelysning, Installation av spotlights, Installera Strömbrytare, Byte av ljuskällor)
   - *Kök & Badrum* (6 links: kök, badrum, Golvvärme, Vitvaror, Ugn & Spis, Elrenovering)
   - *Populära* — 4 description cards: **Eljour** "Akut hjälp när det inte kan vänta" → /eljour/ · **Elektriker** "Boka en auktoriserad elektriker" → /elektriker/ · **Laddbox** "Installation av hemmaladdning" → /laddbox/ · **Batterilagring** "Installation av solcellsbatteri" → /batterilagring/.
   - Column headings (Elinstallationer/Belysning/Kök & Badrum) are **unlinked** `<span class="gradientdarkblue-text">` — no route to the /elservice/ pillar itself from the panel.
4. **Mega-menu "Produkter"** — Laddboxar card "Jämför och välj laddbox för villa, BRF och företag" → /laddboxar/ · Solcellsbatterier "Lagra din solel, använd den när elen är dyr" → /solcellsbatterier/ · **"Guider & verktyg"**: Laddboxkalkylatorn → /laddboxkalkylator (no trailing slash), Batterikalkylatorn → /batterikalkylator, Energikalkylator → /energikalkylator/, **"Elcentralkalkylator" → /elcentral-kollen/** (label ≠ product name).
5. **Mega-menu "Lösningar"** — 4 photo cards: **Privatperson → /elektriker/** (same URL as Populära>Elektriker), Bostadsrättsförening → /bostadsrattsforening/, Företag → /foretag/, Kommun → /kommuner/.
6. **CTA "Gratis rådgivning"** (`.ampy-cta`, teal, pulsing green dot, box-shadow) → **https://ampy.se/kontakt/** (postId 17138). CSS verified: stays visible at ≤780px (font-size drops to `--aptext-s`); it is the only conversion element in the desktop header — **no phone number anywhere in the desktop header**.
7. **Mobile** (≤1024px): hamburger `#brxe-fsrjct` appears; offcanvas accordion duplicates the ENTIRE menu tree (all ~30 links), then: **"Ring en expert" → tel:+46102657979** (teal button, phone icon) + a bare **"5.0"** Google rating chip. Live render 375px (2026-08-02): the accordion groups are **collapsed by default**, so the panel shows only "MENY / Tjänster ▾ / Produkter ▾ / Lösningar ▾" + the full-width "Ring en expert" button **visible without scrolling** — phone is 2 interactions away (burger → tap), not buried under a scroll. Eljour, however, is burger → Tjänster → Populära → Eljour = **4 taps**. Interaction caveats observed in the rendered session: taps on the accordion row label and on the chevron coordinates did **not** toggle the group; only activating the underlying toggle `button` via the accessibility tree worked — and those toggle buttons expose **no accessible name** (unnamed `button` elements in the a11y tree).

### Footer stack (bottom of all 325 pages)
1. **Prefooter "Populära kategorier"** (cyan gradient, 5 `<h3 class="prefooter__heading">` columns, headings unlinked):
   - *Elinstallation*: Eljour → /eljour/, Elektriker → /elektriker/, Belysning → /elservice/belysning/
   - *Laddboxar*: Zaptec Go, Zaptec Go 2, Easee Charge up (product pages)
   - *Batterilagring*: SAJ HS3, SigenStor, Dyness Stack100
   - *Områden*: **Stockholm, Sollentuna, Haninge only** (all /elektriker/{ort}/) — 3 links for a 224-page geo set
   - *Lösningar*: Elektriker för företag / restaurang / bostadsrättsförening
2. **Main footer** (navy): logo + "Framtidens elfirma för privatpersoner som värderar kvalitet, transparens och en elektriker som går extra milen för ditt hem!" + socials (incl. tiktok.com/@ampy.se) + Google-G icon + bare **"5.0"** → *Mer om Ampy* (Om oss, Jobba hos oss → ampy.teamtailor.com, Nyheter & Artiklar) · *Kundtjänst* (Support → /kontakt/, ROT avdrag 2026, Grön Teknik 2026) · **H3 "Få en kostnadsfri konsultation!"** (heading, not a link) over Västbergavägen 25 Hägersten, e-mail (Cloudflare-obfuscated → renders "[email protected]" without JS), tel 010-265 79 79.
3. **Footer bar**: © 2026 Ampy Nordic AB + Tillgänglighetsredogörelse / Cookie policy / Integritetspolicy.
Mobile: columns stack vertically; identical content.

### Cross-page conversion topology (verified hrefs)
Nearly every non-phone CTA on the site converges on **/kontakt/**: header CTA (325×), Hero_2 hero button "Kostnadsfri rådgivning" (→ /kontakt/, verified on elcentral — *while an identical lead form sits 500px to its right in the same hero*), CE-block button (~290×), FooterSEO button (~290×), Hero-1 buttons. /kontakt/ itself is the thinnest page on the site: block sequence `Header → MainContact → Prefooter` — **386 words, `h1: []` (no H1 at all)**, and no visible phone number above the footer (the MainContact left pane carries the quote "Från start till mål levererades en service i världsklass.", "5 av 5 · Betyg på Google", "3 000+ genomförda installationer om året" and the 3 steps — but no tel link). The Hero_2 lead form is a JS-mounted stub: `<div id="ampy-form-root" class="aof" data-endpoint="https://…supabase.co/functions/v1/hero-lead" … data-thankyou="/thank-you">` — zero form fields in server HTML.

---

## Customer-flow walkthrough (35–65 yo homeowner, mobile)

**0–5 s:** Lands from Google on a service page. Header: logo, "Gratis rådgivning" pill, hamburger. To *call* — the faster, higher-intent path for "elfel i huset" searchers — she must know to open the hamburger, where "Ring en expert" waits (visible once open, but nothing in the bar signals a phone option exists). The visible one-tap conversion is the form path only; her learned pattern from every other Swedish trade site — a number in the top bar — fails.
**Scroll:** If she taps "Gratis rådgivning" expecting advice, she lands on /kontakt/: no heading hierarchy (no H1), a form asking Förnamn/Efternamn/E-post/Telefonnummer/Adress/Postnummer/Postort, and still no phone number. The Clarity-recorded paid visitor who went Contact → **About Us** (47 s, no conversion) is exactly this trust-seeking loop: the conversion hub gives her nothing new to trust.
**Decision:** On the elcentral page she instead scrolls; the last two CTAs she sees before the footer read "**Kostnadsfri radgivning**" — missing the å, twice, live today. For an audience that is hiring someone for *precision work in their home*, a misspelled primary CTA is a small but real competence signal (MECLABS anxiety term). Footer offers address + org + policies (good), but the rating is a bare "5.0" with no count.

---

## What works (keep)

- **One header everywhere** (325/326): Jakob's law satisfied on placement — logo left, nav center, CTA right, sticky. Skip links present.
- **Mega-menu card descriptions are the best copy in the nav** — "Akut hjälp när det inte kan vänta" (Eljour), "Lagra din solel, använd den när elen är dyr" — task-language, JTBD-true. The pattern is right; the hierarchy above it is wrong.
- **Kalkylatorer surfaced in the nav at all** ("Guider & verktyg") — near-unique among Swedish elfirmor; keep, relocate.
- **Header CTA survives on mobile** (CSS-verified, only font-size changes ≤780px) with pulsing-dot affordance.
- **Footer NAP + policy hygiene**: real address, org name, © , tillgänglighetsredogörelse — the formal proof layer a risk-averse Swedish homeowner scans for (Konsumentverket-style seriousness).
- **Prefooter as internal-link engine** exists and points at money pages (Eljour/Elektriker/products) — right idea, under-scaled.

---

## Findings

**GLOB-01 · P0 · Sitewide CTA typo "Kostnadsfri radgivning" (missing å).**
Live-verified on /elservice/elcentral/ (2 instances). Snapshot sweep: 20 of 36 pages, always in `ce-block__button` and `footer-seo__button` (both → /kontakt/) — blocks present on **~290 pages** per block-map — plus `hero-1__button` on /elektriker/, /eljour/, /om-oss/ (on /elektriker/ it is the **primary hero CTA** under H1 "Elektriker för privatpersoner över hela Sverige!"). Evidence: MECLABS anxiety (a); NN/g credibility heuristic — surface errors transfer to perceived service quality for a precision trade. Mobile: identical, full-width buttons, more prominent. Fix = two template strings + three hero instances. Priority: 290 pages × weight 1 (low-page CTA) × effect 2 = **580**; hero instances 3 × 3 × 2 = 18 → do first regardless, it is a 10-minute fix.

**GLOB-02 · P0 · /kontakt/ — the convergence point of ~900 CTA instances — is the weakest page on the site.**
No H1 (verified `h1: []`), 386 words, block chain `Header → MainContact → Prefooter`, **no visible phone number above the footer**. Every header CTA (325 pages), every CE-block and FooterSEO button (~290 pages each) and the Hero_2 hero button all dump motivation here, where it evaporates: no restatement of value, no FAQ, no anxiety reducers, no tel link for the half of visitors whose preferred conversion is a call (business context: phone is conversion path #1). Message match breaks twice: button promises "Gratis rådgivning" → page `<title>` "Kontakta oss" → form heading "Få en kostnadsfri rådgivning". Evidence: MECLABS heuristic (motivation not carried, friction f and anxiety a unaddressed); Google message-match doctrine; Clarity paid session Contact→About Us = observed trust-seeking bailout. Mobile: form fills first viewport, trust pane stacks below (order inverted vs need). Priority: 325 referring pages × 3 (form) × 3 (high) = **2925 — the single highest-leverage template fix in the global journey**.

**GLOB-03 · P1 · CTA label fragmentation: ≥8 labels for the same action.**
Census across 36 snapshots (occurrences): "Gratis rådgivning" 59 (header CTA + MainContact submit) · "Kostnadsfri radgivning" 41 (typo variant) · "Kostnadsfri rådgivning" 29 (Hero_2/Hero-1/MikroCTA) · "Få en kostnadsfri rådgivning" 24 (MainContact H2) · "Boka rådgivning" 16 (aof form submit) · "Få skräddarsydd offert" 16 (product CTA) · "Få ditt förslag" 16 (popup submit) · "Få en kostnadsfri konsultation!" (footer H3) · plus phone-path variants "Ring 010-265 79 79" 55, "Ring en expert" 35, "Prata med en elektriker inom 60 sekunder!". Gratis vs Kostnadsfri vs Konsultation vs Offert vs Förslag are five different mental objects for one identical outcome (an electrician calls you back). Evidence: NN/g consistency heuristic; Jakob's law (users spend most time on other sites — one action, one name); message match chain ad→button→page→submit currently mutates at every hop. Mobile: worse — labels are seen sequentially in isolation, so the visitor cannot infer they are the same funnel. Priority: 326 × 2 × 2 = **1304**.

**GLOB-04 · P1 · Phone path is hidden from the header bar despite phone being conversion path #1.**
Desktop header: no phone at all (verified live render — logo, 3 nav triggers, "Gratis rådgivning" only). Mobile: tel CTA "Ring en expert" exists only *inside* the offcanvas — live render shows it IS immediately visible once the panel opens (collapsed accordions, no scroll needed), so the true cost is 2 interactions, but the bar itself offers zero call affordance and nothing signals that a phone option exists behind the burger. The sticky header spends its one CTA slot on the *form* path. GA4 shows 2 phone clicks vs 0 form leads from paid — the phone is the path that actually produces. Evidence: Jakob's law (Swedish trade-site convention = number visible in the top bar); Fitts's law / thumb-zone reachability; Unbounce home-services benchmark (urgent/repair intent converts by phone); two-conversion doctrine. Mobile note: this IS the mobile finding; desktop should also carry a visible number for the 55–65 cohort who dial from memory. Priority: 325 × 3 (header=first-viewport) × 2 = **1950**.

**GLOB-05 · P1 · Hero_2 hero CTA navigates away from its own form; the form itself is JS-only.**
On /elservice/elcentral/ the green "Kostnadsfri rådgivning" hero button links to /kontakt/ — a full page-load detour (lab LCP ~9–10 s) to a *worse* form, while the `.aof` form with per-page prefill sits in the same hero. And that form is an empty `<div id="ampy-form-root">` in server HTML, mounted client-side against a Supabase endpoint: slow/failed JS = a hero with a hole in it, and no server-rendered fields also degrades analytics (consistent with "0 form starts recorded"). Evidence: MECLABS friction; Baymard (unexpected navigation during a form decision resets commitment); speed budget from business context. Mobile: hero CTAs render ABOVE the form card (stacked), so the detour link is what the thumb meets first. Priority: ~150 Hero_2 pages × 3 × 2 = **900**.

**GLOB-06 · P1 · Nav taxonomy is company-logic, not visitor-logic; the two money intents are demoted.**
Top level "Tjänster / Produkter / Lösningar" is SaaS-speak. The visitor's mental model (verified search terms: "installera taklampa", "byta elcentral pris", "elfel i huset") is task/urgency-based. **Eljour and Elektriker — the two highest-commercial-priority intents (service > laddbox > battery) — are hidden as the 4th column "Populära" inside the Tjänster hover panel**, invisible until a mega-menu opens. Meanwhile "Lösningar > Privatperson" and "Tjänster > Populära > Elektriker" both resolve to /elektriker/ under different labels — the same door twice, labelled differently (Jakob's law violation; NN/g match between system and real world). Mobile: Eljour is one accordion + one scroll deep — for the one visitor segment (acute fault) who is least willing to browse. Priority: 326 × 2 × 2 = **1304**.

**GLOB-07 · P2 · Mega-menu choice overload + full DOM duplication.**
Tjänster panel ≈ 21 tap targets (17 service links + 4 cards); the entire nav tree is rendered twice per page (desktop + offcanvas), inflating already-heavy pages (500–800 kB HTML) and doubling strings like "Boka en auktoriserad" (70 occurrences / 36 pages = ~2 per page). Evidence: Hick's law; page-weight vs the 9–10 s LCP flag. Mobile: 30+ item accordion between hamburger and the tel CTA. Priority: 326 × 1 × 2 = 652.

**GLOB-08 · P2 · Guider & verktyg: naming mismatch + wrong shelf.**
Nav "Elcentralkalkylator" → /elcentral-kollen/ ("Elcentral-kollen" is a diagnostic, not a calculator — label promises numbers, page delivers a verdict); "Energikalkylator" vs product name "Energikalkylatorn"; trailing-slash inconsistency (/laddboxkalkylator, /batterikalkylator no slash vs /energikalkylator/) risks redirect hops. The tools live only under **Produkter**, so a service-intent visitor (elcentral) never meets Elcentral-kollen in her menu path. Evidence: message match; information scent (NN/g). Mobile: same. Priority: 326 × 1 × 1 = 326.

**GLOB-09 · P2 · Unanchored "5.0" in global chrome (candour gate).**
Bare "5.0" appears in the mobile-menu chip and the footer (Google-G icon + "5.0", no count, no date); prefooter/hero variants elsewhere say "5.0 på Google". Candour rule: rating must be anchored — *rating + count + source* — or removed. "5 av 5 · Betyg på Google" (MainContact) is the closest compliant pattern; still lacks count. Evidence: candour gate (non-negotiable); Cialdini social proof only works when verifiable. Mobile: the mobile-menu "5.0" chip has no label at all. Priority: 325 × 1 × 2 = 650 (trust-integrity weighting).

**GLOB-10 · P2 · Prefooter "Områden" starves the 224-page geo set.**
3 links (Stockholm, Sollentuna, Haninge — elektriker-i only) vs 224 programmatic pages across 4 CPTs (elektriker-i/eljour-i/elinstallation-i/laddbox-i × 56). No hub page linked. The in-page MapBlock (20 ort buttons) exists only on some templates and randomizes; the *global* chrome — the only element on all 325 pages — passes almost no equity to the geo layer. Evidence: internal-linking/site-architecture practice (crawl depth for programmatic sets); NN/g footer-as-directory. Mobile: same 3 links. Priority: 224 × 1 × 2 = 448.

**GLOB-11 · P3 · Footer polish items.**
(a) E-mail is Cloudflare-obfuscated — with JS off it literally renders "[email protected]" (verified in fetched text). (b) "Få en kostnadsfri konsultation!" is an H3 *heading*, styled like the CTA language used in buttons elsewhere — looks tappable, is not — **and its markup is malformed**: `<span class="gradientwhitegreen-text">konsultation!<span>` (unclosed span, verified in home.html), shipped sitewide. (c) Prefooter column headings (Elinstallation, Laddboxar, Batterilagring, Områden, Lösningar) are unlinked H3s — each should link its pillar (/elservice/, /laddboxar/, /solcellsbatterier/, områden-hub, /foretag/). (d) Footer "Support" → /kontakt/ — yet another label for the same destination the header calls "Gratis rådgivning". Mobile: (b) is a thumb-trap. Priority: 325 × 1 × 1 = 325.

**GLOB-13 · P2 · Mobile accordion a11y + tap-target integrity (verify on device).**
Observed in the rendered 375px session: the offcanvas accordion toggle `button`s have **no accessible name** (WCAG 2.1 4.1.2 name/role/value failure — screen-reader users hear "button" three times); coordinate taps on the row label and the chevron did not toggle the group, while activating the button via the accessibility tree did. HYPOTES: on some real devices the effective toggle target is smaller than the visual row (Fitts violation for 45–65 y/o thumbs) — verify on-device; if reproduced, make the entire row the toggle and give each button its group name. Priority: 325 × 2 × 1 = **650** pending device verification.

**GLOB-14 · P3 · Self-referential header CTA on /kontakt/.**
On /kontakt/ the header "Gratis rådgivning" still links to /kontakt/ — a dead click at the exact moment of conversion (verified in kontakt.html). Swap it for the phone CTA on that page (the one conversion path the page currently lacks). Priority: 1 × 3 × 1 = 3, trivial fix bundled with GLOB-02.

**GLOB-12 · P3 · Unlinked Tjänster column headings.**
"Elinstallationer / Belysning / Kök & Badrum" panel headings are decorative spans; no path from the mega-menu to the /elservice/ pillar page itself (only to leaf pages). Evidence: information scent; polyhierarchy convention. Mobile: accordion parents likewise toggle-only. Priority: 326 × 1 × 1 = 326.

---

## Recommended sequence (wireframe)

### Header (all pages)
| # | Element | Why here | New/existing/modified |
|---|---------|----------|----------------------|
| 1 | Logo → / | convention (Jakob) | existing |
| 2 | **Tjänster** mega-menu — add linked column headings; move **Eljour out** | reduce panel to ~17 items; pillar reachable | modified |
| 3 | **Eljour** as top-level nav item (subtle red/amber accent, no fake urgency) | urgent intent = 0-click visibility; Unbounce: repair intent converts best | new (promotion) |
| 4 | **Produkter** (Laddboxar / Solcellsbatterier) | keep | existing |
| 5 | **Guider & verktyg** promoted out of Produkter (or duplicated into Tjänster); rename "Elcentralkalkylator" → "Elcentral-kollen" | message match; service-intent discovery of magnets | modified |
| 6 | **Lösningar** — rename "Privatperson" card destination or drop card (points at /elektriker/ duplicate) | kill duplicate-door confusion | modified |
| 7 | **Visible phone number "010-265 79 79"** (tel:) beside CTA — desktop text link; mobile: phone icon-button in the bar itself | phone = conversion #1; Fitts; GA4 evidence | **new** |
| 8 | CTA **"Kostnadsfri rådgivning"** (ONE canonical label sitewide) → /kontakt | consistency (NN/g); ends Gratis/Kostnadsfri split | modified |
| 9 | Mobile offcanvas: keep the collapsed-accordion shape (verified good); make the **entire row the toggle**, name the toggle buttons, anchor the rating chip | reachability + WCAG 4.1.2 (GLOB-13) | modified |

### /kontakt (the CTA destination — companion fix, same sprint)
H1 "Kostnadsfri rådgivning av elektriker" → phone-first row (tel button + "Vi svarar vardagar HH–HH" [GAP: owner hours]) → MainContact form → anchored rating (5,0 · N recensioner · Google [GAP: count]) → 3-4 FAQ (pris/offert/ROT/vem kommer) → Prefooter. (Full spec belongs to the kontakt-page deep-dive; listed here because GLOB-02's fix is inseparable from the header CTA.)

### Prefooter / Footer (all pages)
| # | Element | Why here | New/existing/modified |
|---|---------|----------|----------------------|
| 1 | Populära kategorier — link the 5 column headings to their pillars | information scent; equity | modified |
| 2 | **Områden column → 6–10 orter + "Alla områden →" hub link** (rotate or curate by volume) | feed the 224-page geo set from 325 pages | modified |
| 3 | Main footer: anchored rating ("5,0 av 5 · N recensioner på Google", linked GBP) replaces bare "5.0" | candour gate | modified |
| 4 | "Få en kostnadsfri konsultation!" → make it a real link/CTA to /kontakt or render as plain heading without CTA styling | affordance honesty | modified |
| 5 | NAP + policies + socials | keep — compliance proof layer | existing |

---

## Test hypotheses (top 3, A/B)

1. **HYPOTES (phone visibility):** Adding a persistent tel-CTA in the mobile header bar (vs today's menu-buried "Ring en expert") increases phone-click conversions per session by a measurable margin on paid landings within 4 weeks. Metric: `tel:` click rate / paid session (GA4). B-variant: sticky bottom call-bar instead of header icon.
2. **HYPOTES (CTA convergence):** On Hero_2 pages, pointing the hero "Kostnadsfri rådgivning" button at the adjacent `.aof` form (smooth-scroll + focus first field) instead of navigating to /kontakt/ increases form starts (once form_start instrumentation exists) without reducing phone clicks. Metric: form_start rate on Hero_2 pages.
3. **HYPOTES (label unification):** Normalizing all form-path CTAs to the single label "Kostnadsfri rådgivning" (incl. typo fix, header, submits) lifts click-through on mid/low-page CTAs (CE-block, FooterSEO) vs the current 8-label mix. Metric: CTA CTR per block, bucketed by experiment_id.

*Not testable, just fix:* GLOB-01 typo, GLOB-09 rating anchoring (candour), GLOB-11 dead-looking heading.
