# Template deep-dive: Om oss + Kontakt + Thank-you (the trust-verification & conversion-terminus templates)

URLs analyzed (live-fetched 2026-08-02 + raw snapshots in `data/pages/`):
- https://ampy.se/om-oss/ (725 words)
- https://ampy.se/kontakt/ (386 words)
- https://ampy.se/thank-you/ (32 words)

Pages using these templates: **3 direct** — but their funnel reach is site-wide: the header CTA **"Gratis rådgivning" on all 326 pages links to `/kontakt/`** (verified `href="https://ampy.se/kontakt/"` on the `ampy-cta` header button), and `/thank-you/` is the redirect terminus of **every** form on the site (Hero_2, MainContact on 295 pages, product popups). These three pages are the narrowest part of the funnel: every improvement here compounds across the whole site.

Why this trio matters (evidence): the only identifiable engaged paid visitor in Clarity (47s session) went **Kontakt → Om oss** before leaving — a classic trust-verification journey. The visitor reached the conversion page, hesitated, went looking for proof the company is real, and did not come back. These pages currently fail that journey, as documented below.

---

## 1. OM OSS — https://ampy.se/om-oss/

### Current block sequence (verified from live HTML `<section>` classes)

| # | Block | Desktop behavior | Mobile behavior |
|---|---|---|---|
| 1 | Header (mega-menu) | Tjänster/Produkter/Lösningar mega-menus + "Gratis rådgivning" teal CTA → `/kontakt/` | Offcanvas accordion + "Ring en expert" + 5.0 |
| 2 | **Hero-1** | Floating white card: H1 "Sveriges snabbast växande elfirma, byggd för kvalitet." → paragraph → CTA pair ("Kostnadsfri radgivning" → `/kontakt/`; "Ring 010-265 79 79" → tel:) → "5.0" Google row (links to Maps, no review count) → image `seniora-ampy-elektriker.webp` | Stacked; image absolute bottom |
| 3 | **ContentBlock** | 3 alternating image/text rows: H2 "Nya generationens elfirma" / "Trygg el, utan krångel" / "Kvalitet du ser direkt". Images: `Pixii-Home-hemmabatteri.webp` (a battery product), two "Modernt hus" exterior shots | Rows stack image-over-text; long scroll of abstract copy |
| 4 | **AboutMetrics** (`metrics about-us-metrics` — one section carrying both fingerprints) | 3 cards on `numbers-bg.webp`, min-height 380px: icon → H4 → text. Headings: "Nöjda kunder", "Erfarenhet i branschen", "Personer i teamet". **No number element exists** (`metrics__number` absent from page) | 780px: 1-col; 480px: flex column, 16px gap |
| 5 | **VisualCTA** | Full-bleed image bg: "Ditt hem, vår spetskompetens" + black "Kontakta oss" → `/kontakt/` | Centered, `--aptext-2-5xl` heading |
| 6 | **MainContact** | Two-pane card: photo pane (quote "Från start till mål levererades en service i världsklass.", "5 av 5 · Betyg på Google", "3 000+ genomförda installationer om året", 3 steps) + form pane (Förnamn/Efternamn/E-post/Telefon/Adress + Meddelande → "Gratis rådgivning") | Photo pane precedes form pane in DOM → stacks above form |
| 7 | Prefooter + Footer | Populära kategorier links; footer with address/email/phone | Stacked link columns |

Notably **absent** from this page: Testimonials, Team section, Certificates, FAQ, Vår process — and the page links to **zero** of the six team-member profile pages that live directly under `/om-oss/*` (verified: no `href="https://ampy.se/om-oss/…"` anywhere in the page).

### Customer-flow walkthrough (35–65 Swedish homeowner, arriving mid-decision to verify the company)

**First 5 seconds:** H1 makes a big claim — "Sveriges snabbast växande elfirma, byggd för kvalitet." — with no anchor. The sub-line pitches "AI och IT som minskar friktion", founder language, not homeowner language. The visitor came asking *"vilka är ni egentligen — vågar jag släppa in er i mitt hem?"* and gets a growth pitch. **Scroll:** three long brand-essay rows illustrated with a battery product and two house exteriors — no faces, no names, no credentials. **Decision zone:** a "numbers" block with headings that promise numbers ("Personer i teamet") and deliver none, then a CTA that sends them to another page, then the same form they will find there. The verification visitor leaves with rhetoric, not proof. This is exactly the journey the Clarity recording shows ending in a bounce.

### What works (keep)

- Hero-1 photo is real electricians (`seniora-ampy-elektriker.webp`) — the only human proof on the page; right instinct.
- The three ContentBlock stories are genuinely on-voice candour copy ("Vi guidar dig genom vad som behöver göras, varför det behövs och vad det kostar – utan överraskningar") — the *substance* is good; it is the sequencing and lack of proof around it that fails. SEO substance must be preserved.
- MainContact at the bottom = correct terminal block; a verification visitor who is convinced can convert without leaving.
- AboutMetrics card *texts* contain the germ of real proof ("egna, auktoriserade elektriker istället för osäkra mellanhänder").

### Findings

**OM-1 — P0 (candour/trust). Internal number contradiction on the same page.**
AboutMetrics card 1: "**Över tusen** genomförda installationer är vårt absolut starkaste kvalitetsbevis." MainContact pane, three viewports later: "**3 000+ genomförda installationer om året**." Over-a-thousand-total vs three-thousand-plus-per-year cannot both be the honest framing. The one visitor persona this page exists for — the verifier — is exactly the one who notices. Candour gate: pick ONE owner-confirmed figure with a unit (total vs per år) and use it everywhere. Note the "1000+ kunder"-family claims are on the banned list unless owner-confirmed current. Mobile: both claims are seen in the same continuous scroll. *Framework: candour gate; Cialdini consistency (inconsistency destroys the authority signal it was meant to build).*

**OM-2 — P1 (trust architecture). The trust-verification page contains no verification artifacts.**
No Team block, no Testimonials, no Certificates (Elsäkerhetsverket/ID06/Trygg Hansa logo wall exists as a site block but is not used here), no org.nr, no address in body, and zero links to the six E-E-A-T team-member pages at `/om-oss/edvin-gustavsson/` etc. (verified). The specialist's research anchor: a serious Swedish customer's proof-of-choice is the **Elsäkerhetsverket registration check + Konsumentverket written-quote advice** — neither is facilitated. *Frameworks: NN/g About-Us research (users seek people, facts, credentials — not mission statements); Cialdini authority; E-E-A-T.* Mobile: the absence hurts more — 4+ viewports of text with no scannable proof.

**OM-3 — P1 (unfinished block). AboutMetrics is a numbers block with the numbers missing.**
The section reuses the `metrics` component (bg image literally named `numbers-bg.webp`) but renders icon+H4+text only; `metrics__number` does not exist in the DOM. "Personer i teamet" as a heading with no count reads as a template left half-filled — on the page claiming "genomtänkt in i minsta detalj". Fill with owner-confirmed numbers (antal elektriker, år samlad erfarenhet, installationer med unit) or retitle the cards as value statements. *Framework: MECLABS value clarity (specificity carries credibility); Ogilvy-style specificity.*

**OM-4 — P2 (candour/claims). Unanchored superlatives at the load-bearing point.**
H1 "Sveriges snabbast växande elfirma" — allowed per owner directive (strong superlatives permitted unless demonstrably false) but on *this* page skeptics arrive to test claims; an anchor ("enligt Allabolag-tillväxt 20XX" or similar owner-supplied source) converts puffery into proof. Same for the "5.0" hero rating row: links to Google Maps but shows no review count (candour rule: rating + count + source or remove). *Framework: candour gate; MECLABS anxiety reduction via evidentials.*

**OM-5 — P2 (copy/audience mismatch). Founder-voice over customer-JTBD.**
"Lägg till AI och IT som minskar friktion, så får du en kundresa som känns modern på riktigt" — the 35–65 homeowner's job-to-be-done is *safe home, fair price, someone who answers*; "AI och IT" is the 24-year-old founder's pride, and the known taste-mismatch risk in the business context. Keep modernity as a *benefit* ("du får offert samma dag, dokumentation digitalt") not a technology list. *Framework: JTBD; MECLABS motivation-matching.* Mobile: this is the second sentence read on the page.

**OM-6 — P2 (imagery). Product/house photos where people belong.**
ContentBlock images are a **Pixii Home battery** and two house exteriors. A battery photo on the About page also cuts against commercial priority (service > laddbox > battery). Replace with real team-at-work photos (the six team pages have portraits already shot). *Framework: NN/g imagery research — real people photos outperform decorative/product shots for trust.*

**OM-7 — P3 (wasted click). VisualCTA sends visitors off-page past the on-page form.**
"Kontakta oss" → `/kontakt/`, whose entire content is the same MainContact form sitting one scroll below the button. Change to anchor `#main-contact` (or keep `/kontakt/` only if kontakt is upgraded per §2). Mobile: an off-page navigation costs a full page load at the moment of highest intent (~9–10s lab LCP flagged site-wide). *Framework: Tesler's law / NN/g — do not add steps that add no information.*

**OM-8 — P2 (typo). "Kostnadsfri radgivning" — missing å in the Hero-1 CTA button** (verified in live HTML, likely the shared Hero-1 library button, so also on other Hero-1 pages). A spelling error inside the primary CTA on the page whose copy promises precision "in i minsta detalj" is a micro-trust leak. *Framework: credibility heuristics (Fogg) — surface errors are read as competence signals.*

**Priority arithmetic (om oss):** OM-1: 1 page × 2 (mid) × 3 (high — trust kill for the decisive persona) = **6**, elevated to P0 by candour-gate rule. OM-2: 1 × 2 × 3 = **6**. OM-3: 1 × 2 × 2 = **4**. OM-7/OM-8 are shared-block fixes whose true reach is larger (Hero-1 button ships on multiple pages).

### Recommended sequence (wireframe) — om oss

| # | Block | Why here | New/existing/modified |
|---|---|---|---|
| 1 | Hero-1, anchored | Keep H1 ambition but anchor it (source or reframe "byggd för kvalitet" as lead); fix å-typo; anchor 5.0 with count; keep electrician photo | Modified |
| 2 | **Team section** (existing site block) + links to all 6 profile pages | The verifier's first question is "vilka är ni?" — answer with faces, names, Auktoriserad elinstallatör credentials. Unlocks the orphaned E-E-A-T pages | Existing, added here |
| 3 | **Metrics with real numbers** (one confirmed installations figure, år erfarenhet, antal elektriker) | Specific numbers directly under faces = proof stack; resolves OM-1/OM-3 | Modified |
| 4 | **Testimonials** (existing block, 12 real Google reviews) | Third-party voice after first-party claims (Cialdini social proof ordering) | Existing, added here |
| 5 | ContentBlock (3 story rows, compressed intros, people photos) | Full SEO substance preserved, now *below* proof — MECLABS HealthSpire: length converts when sequenced to answer live questions | Modified (images + order) |
| 6 | **Certificates** + company-facts line (org.nr, "kontrollera oss hos Elsäkerhetsverket" link) | The named Swedish-buyer verification behavior, made one-click | Existing block + new facts line |
| 7 | VisualCTA → anchor `#main-contact` | Emotional close, now lands on the form instantly | Modified |
| 8 | MainContact | Terminal conversion block, unchanged position | Existing |

### Test hypotheses (om oss)

1. **HYPOTES:** Proof-first re-sequence (team + numbers + testimonials above ContentBlock) vs current order increases form submits + phone clicks from om-oss sessions, because the Clarity-observed verification journey currently ends unanswered. A/B at template level, metric: conversion per om-oss session.
2. **HYPOTES:** Replacing product/house images with named team-at-work photos increases scroll depth past ContentBlock row 1 and reduces exit rate (NN/g imagery effect). Measure via Clarity scroll maps.

---

## 2. KONTAKT — https://ampy.se/kontakt/

### Current block sequence (verified)

| # | Block | Desktop behavior | Mobile behavior |
|---|---|---|---|
| 1 | Header | Mega-menu + "Gratis rådgivning" CTA which links… to this very page | Offcanvas + "Ring en expert" (tel:) |
| 2 | **MainContact** (the entire page body) | Left photo pane: white logo, quote "Från start till mål levererades en service i världsklass.", gold stars "5 av 5 · Betyg på Google", "3 000+ genomförda installationer om året", 3 steps (Skicka in dina uppgifter → Vi ringer dig inom 24 timmar → Kostnadsfri rådgivning av elektriker). Right form pane: H3 "Få en kostnadsfri rådgivning" → Förnamn/Efternamn (2-col), E-post, Telefonnummer, Adress (Google Places, `placeholder="Sök efter din adress *"`, **required**) + gata/postnr/ort fallback, Meddelande (valfritt) → "Gratis rådgivning" pill → integritetspolicy line | Photo pane is before form pane in DOM (idx 355277 vs 360142) → trust panel stacks above; form starts ~1 viewport down |
| 3 | Prefooter + Footer | Populära kategorier; footer address/email/phone | Stacked |

Page facts (all verified): **no H1 exists** (only H3s); 386 words; **no tel: link in the page body** — the only two tel: links are the mobile-offcanvas "Ring en expert" button and the footer; no org.nr, no öppettider, no map, no FAQ. Meta description promises "kostnadsfri **offert**"; page delivers "kostnadsfri **rådgivning**"; submit button says "**Gratis** rådgivning".

### Customer-flow walkthrough

This is where the header CTA from all 326 pages, the om-oss hero CTA, and the VisualCTA all land. The click that brought the visitor here said "Gratis rådgivning" — an implicit promise of *talking to someone*. **First 5 seconds, desktop:** a form. Good form, strongest block on the site — but the visitor who wanted to *call* (half the conversion model, and the older half of the 35–65 demographic skews phone) finds **no phone number on the page body at all**. **First 5 seconds, mobile:** not even the form — a photo panel with a quote and steps; the form begins below the fold. **Hesitation moment:** "Adress — Sök efter din adress *" required, for a phone consultation; no hours ("if I submit Friday 17:00, when do they actually call?"); no org.nr or address in body for the verifier — which is plausibly why the Clarity visitor left this page for Om oss, where the loop of rhetoric closed with no proof and the session died.

### What works (keep)

- **Single-purpose page**: no competing CTAs, no mid-page bands — correct for the bottom of the funnel (Unbounce attention-ratio principle). Do not "enrich" it into a brochure.
- MainContact itself is the site's best conversion asset: 3-step expectation setting ("Vi ringer dig inom 24 timmar" is exactly the anxiety-reducer Swedish homeowners cite — "will they answer later"), real quote, light implicit-consent GDPR line instead of a checkbox.
- Optional Meddelande, address autocomplete with manual fallback, E.164 phone validation — professional form engineering.

### Findings

**KO-1 — P0 (conversion path). The primary CTA destination hides one of the two conversions.**
Two conversion paths exist (call, form). On the page every other page pushes traffic to, the phone number appears **only** in the mobile offcanvas menu and the footer — desktop body: zero tel: links, no number in visible text above the footer. GA4 already shows phone clicks are the only conversions actually firing (2 phone clicks, 0 form starts) — the demand skews call, and the contact page suppresses it. Fix: phone CTA + number in a compact page-top row and/or inside the photo pane ("Ring oss direkt: 010-265 79 79, vardagar HH–HH"). Mobile: the offcanvas button exists but requires opening the menu — Fitts-law-hostile at peak intent. *Frameworks: MECLABS friction; NN/g contact-page conventions (phone + hours are the #1 sought elements); Jakob's law.* Priority: 1 page × 3 (form/hero weight) × 3 (high) = **9**, with site-wide reach as the destination of 326 pages' header CTA.

**KO-2 — P1 (message match + SEO). No H1; "offert" promised, "rådgivning" delivered.**
The page has no H1 element at all (verified — h1 array empty, headings start at H3 "Få en kostnadsfri rådgivning"). The inbound scent chain is inconsistent: header CTA "Gratis rådgivning" → meta "kostnadsfri offert" → H3 "kostnadsfri rådgivning" → button "Gratis rådgivning". Pick one noun ladder (rekommendation: "Kostnadsfri rådgivning" everywhere, "offert" as the step-2 outcome in the steps copy) and add H1 "Kontakta Ampy — kostnadsfri rådgivning". *Frameworks: Google message match (ad→H1→first screen mandatory); MECLABS value-proposition congruence.* Mobile: the missing H1 also removes the orientation cue after the offcanvas closes.

**KO-3 — P1 (form friction/anxiety). Required address for a phone call.**
5 required fields; the 5th is full address via Google Places (`required` on `adress`, asterisked placeholder). Baymard: perceived difficulty tracks required-field count; and the field triggers the exact Swedish-homeowner anxiety documented in research ("why does a phone consultation need my street address?"). The Hero_2 pattern already solved this elsewhere on the site (post-submit enrichment / "Fler detaljer (valfritt)"). Make address optional or deferred; keep it for booked jobs. **HYPOTES phrased under Test hypotheses below.** Mobile: Places autocomplete on iOS keyboards is a further friction step.

**KO-4 — P2 (mobile sequencing). Trust panel before form on mobile.**
DOM order photo-pane → form-pane means the mobile visitor who clicked "Gratis rådgivning" scrolls through logo, quote, stars, volume claim and 3 steps before the first input. Reorder for mobile (form first, condensed trust strip above it: stars + "Vi ringer dig inom 24 timmar"), keep the full panel below. *Framework: NN/g mobile — lead with the task; MECLABS friction.* (Exact fold position not measured — flagged as layout-verified DOM order, fold = HYPOTES.)

**KO-5 — P2 (candour). "5 av 5 · Betyg på Google" and "3 000+ genomförda installationer om året" need owner-confirmed anchors** (count of reviews; source/period for 3 000+ — and consistency with om-oss "över tusen", see OM-1). Shared-block fix with every MainContact instance (295 pages).

**KO-6 — P2 (missing reassurance layer). 386 words leaves real questions unanswered.**
The candidate is *not* more marketing — it is decision-support: (a) "Vad händer efter att du skickat in?" expanded steps incl. who calls and from which number; (b) 3–4 FAQ (Kostar rådgivningen något? Är offerten bindande? Hur snabbt kan ni komma? Fast pris eller löpande?) — the fixed-vs-estimated-offert anxiety is the top documented Swedish-homeowner concern; (c) company-facts card: besöksadress Västbergavägen 25, org.nr, "kontrollera vår auktorisation hos Elsäkerhetsverket". MECLABS HealthSpire: added content that answers live decision questions lifts conversion (+638% in the cited case); this is the template where that logic applies most directly. *Frameworks: MECLABS; Konsumentverket-buyer-behavior anchor; Cialdini authority.*

### Recommended sequence (wireframe) — kontakt

| # | Block | Why here | New/existing/modified |
|---|---|---|---|
| 1 | Compact contact header: H1 "Kontakta Ampy" + tel-CTA "Ring 010-265 79 79" + öppettider + e-post | Both conversion paths visible in viewport 1, desktop AND mobile; fixes KO-1/KO-2 | New (small band, not a hero) |
| 2 | MainContact | The engine, unchanged role; mobile order form-first with condensed trust strip | Existing, mobile-modified |
| 3 | "Vad händer sen?" — expanded 3 steps + "samtalet kommer från 010-265 79 79" | Anxiety reduction at the decision point; feeds answer-rate | New (copy block, reuses Vår process styling) |
| 4 | Mini-FAQ (4 questions: pris/bindande/tid/fast pris) | Documented top objections; SEO adds body to a 386-word page | Existing FAQ block, new content |
| 5 | Company-facts card: adress, org.nr, Elsäkerhetsverket-check link, karta | The Swedish verification ritual, completed on-page — removes the reason to detour to Om oss | New |
| 6 | Prefooter/Footer | Escape routes for the not-ready | Existing |

Attention-ratio guard: blocks 3–5 contain **no** new CTAs — the page keeps exactly two actions (call, submit).

### Test hypotheses (kontakt)

1. **HYPOTES (KO-1):** Adding a visible phone row (number + hours) above the form vs current increases *combined* conversions (tel clicks + submits) without cannibalizing form submits below the level of total lift. Measure both events per session.
2. **HYPOTES (KO-3):** Making Adress optional (label "Adress (valfritt — hjälper oss förbereda samtalet)") vs required increases form completion rate ≥ relative 15% with no measurable drop in lead quality (sales-confirmed contactability). Baymard field-count principle.
3. **HYPOTES (KO-6):** Appending "Vad händer sen" + mini-FAQ below the form vs bare form increases conversion for paid traffic (the segment shown by Clarity to be trust-verifying), per MECLABS HealthSpire sequencing logic.

---

## 3. THANK-YOU — https://ampy.se/thank-you/

### Current block sequence (verified)

| # | Block | Desktop behavior | Mobile behavior |
|---|---|---|---|
| 1 | **ThankYou** (`ampy-tack`) — the entire page; **no header, no footer** (verified: no header section, no mega-anchor) | Full-viewport aurora bg, glass card: animated mint check → H1 "Din förfrågan har blivit mottagen!" → "En av våra rådgivare kommer att kontakta dig inom kort." → gold stars "5 av 5 · Betyg på Google" → divider → "Utforska våra eltjänster" teal pill → `https://ampy.se/elservice` → "Till startsidan" ghost link → `/` | Same single card, centered |

Page facts (all verified): 32 words total; `<title>Thank you</title>` (English); `<meta name="robots" content="index, follow, …">` with a self-canonical; GTM-568WF66G loads (GA4/Ads conversion fires on this pageview per business context); exactly two navigable links (plus one empty `href="#"` anchor); no tel: link; no phone number.

### Customer-flow walkthrough

The visitor has just done the highest-commitment act the site allows. Their state: mild anxiety ("did it work? who calls? when? what do I say?") and peak engagement (Cialdini consistency: post-commitment is when people are most receptive to the brand). The page answers with a celebration and "inom kort" — **contradicting the promise they were just given** in the form pane ("Vi ringer dig inom 24 timmar"). Then two links, no phone number (if their need escalates to urgent, they must navigate away to find how to call), no preparation guidance, no faces. The single most expensive moment in the funnel — the moment that decides whether an unknown 010-number gets answered on Monday — is spent on a dead end.

### What works (keep)

- The confirmation is unambiguous and instant (H1 + animated check) — NN/g confirmation-page requirement #1 met.
- Visually the calmest, most premium surface on the site; no distracting nav is a defensible post-conversion choice *if* the page itself carries the next step.
- "Utforska våra eltjänster" is at least a non-dead-end gesture.

### Findings

**TY-1 — P0 (measurement integrity). The conversion-counting page is indexable and directly reachable.**
`robots: index, follow` + self-canonical on the page whose *pageview* fires the GA4/Ads conversion. Anyone — organic searcher, bot, bookmark, prefetch — who loads `/thank-you/` mints a fake conversion. In an account currently debugging "0 confirmed form leads" vs ad-click discrepancies, signal integrity is the P0 of P0s. Fix: `noindex,nofollow`; better, fire the conversion on a `form_submit`/`generate_lead` event (or gate the pageview conversion on a session flag set at submit) so direct loads count nothing. Also emit `form_start` (GA4 currently records none — the custom form likely never sends it). *Framework: measurement hygiene / Google Ads conversion-quality guidance.* Priority: 1 × 3 × 3 = **9**, reach = every form on 295+ pages.

**TY-2 — P1 (expectation calibration). "Inom kort" breaks the 24-timmar promise and does nothing for answer rate.**
The form promised "Vi ringer dig inom 24 timmar"; the thank-you page downgrades to "inom kort". Close rate is 50–75% *of contacted leads* — the cheapest lever in the whole economics is getting the call answered. Replace with concrete calibration: "Vi ringer dig **inom 24 timmar** (vardagar 07–16). Samtalet kommer från **010-265 79 79** — spara gärna numret så du vet att det är vi." Optionally show the promised window dynamically (submitted Friday evening → "senast måndag förmiddag"). *Frameworks: MECLABS anxiety; NN/g confirmation-page guidance (state what happens next, when, by whom); peak-end rule.* Mobile: add tap-to-save/tel link so the number lands in recents/contacts.

**TY-3 — P1 (dead-end celebration — the post-conversion opportunity).**
32 words at peak engagement. The page should carry, in order of value: **(a) Förbered dig-checklist** — "Ta gärna en bild på din elcentral / mät avståndet till parkeringen / lista vad som krånglar" (primes a better first call, signals professionalism, echoes the documented buyer wish for fixed offerts based on real info); **(b) Vilka ringer** — 2–3 team faces with names/titles reused from the team pages (the caller becomes a known person; answer-rate lever again); **(c) Läs medan du väntar** — ROT 30%/Grön teknik 2026 explainer links + relevant kalkylator, matched to `form_type` where available (service > laddbox > battery ordering per commercial priority); **(d) real review snippet** with anchored rating. All additive; nothing competes with the already-completed conversion. *Frameworks: Cialdini consistency/commitment; NN/g; peak-end.*

**TY-4 — P2 (polish/candour).** `<title>Thank you</title>` in English on a Swedish site (also what shows in the browser tab and analytics reports — rename "Tack – vi hör av oss inom 24 timmar"); "5 av 5 · Betyg på Google" unanchored (no count, not linked here); one empty `href="#"` link in the card; "Utforska våra eltjänster" points to `https://ampy.se/elservice` without trailing slash (extra 301 hop).

### Recommended sequence (wireframe) — thank-you

| # | Block | Why here | New/existing/modified |
|---|---|---|---|
| 1 | Confirmation card (keep check + H1) with calibrated promise: 24 h / vardagar / "samtalet kommer från 010-265 79 79 — spara numret" | Kills TY-2; protects answer rate | Modified |
| 2 | "Så förbereder du dig" checklist (3 items, per-ärende where form_type exists) | Better first call, lower offert friction | New |
| 3 | "Du kommer att prata med" — 2–3 team portraits + names | Unknown number → known person | New (reuses team assets) |
| 4 | "Medan du väntar": ROT/Grön teknik 2026 + relevant kalkylator (service-first ordering) | Peak-engagement education; feeds cross-sell honestly | New (links to existing assets) |
| 5 | Anchored review snippet + Google badge | Post-decision reassurance (buyer's-remorse damping) | Modified |
| — | Technical: noindex; conversion on submit-event not pageview; emit form_start on first field focus; Swedish title | TY-1 | Modified |

### Test hypotheses (thank-you)

1. **HYPOTES (TY-2/TY-3):** Calibrated-expectation thank-you (24 h + number-to-save + team faces) vs current celebration card increases **call answer rate** on first outbound attempt (measure in CRM/Nimbata), the highest-leverage metric given 50–75% close of contacted leads.
2. **HYPOTES (TY-1, quasi-experiment):** Moving the Ads conversion from thank-you pageview to submit-event changes reported conversions; the delta quantifies current pollution and recalibrates true CPL before any bidding-strategy decision.

---

## Cross-template summary (what to do first)

1. **Week 1 (P0):** thank-you noindex + event-based conversion + form_start (TY-1); resolve the installations-number contradiction with one owner-confirmed figure (OM-1); phone row on kontakt (KO-1).
2. **Month 1 (P1):** kontakt H1 + message-match noun ladder (KO-2); address optional test (KO-3); thank-you calibration + prep/team content (TY-2/TY-3); om-oss proof-first re-sequence with Team/Testimonials/Certificates + team-page links (OM-2/OM-3).
3. **Months 2–3 (P2):** kontakt reassurance layer (KO-6) + mobile form-first order (KO-4); om-oss imagery/copy pass (OM-5/OM-6); candour anchors on every 5.0/5 av 5 instance (shared-block fix, 295+ pages).

Owner inputs required before shipping: confirmed current Google rating + review count; ONE canonical installations figure with unit; org.nr for the facts cards; öppettider; anchor/source for "Sveriges snabbast växande elfirma" (or reframe).
