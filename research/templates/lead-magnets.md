# Lead magnet pages (7) — template deep-dive

URLs analyzed (all fetched live 2026-08-02, cross-checked against `data/pages/*.html` snapshots and `data/block-map.json`):
`/energikalkylator/` · `/laddboxkalkylator/` · `/elcentral-kollen/` · `/batterikalkylator/` · `/led-kalkylator/` · `/elkollen/` · `/ampy-eljour/`
Pages using this template family: **7** (block-map category `lead-magnet`). These are not one template — they are 7 hand-built pages in three maturity states. That inconsistency is itself the core finding.

---

## Current block sequence (verified from block-map + live fetch)

### State A — "wrapped" (the owner's target pattern, partially achieved): batterikalkylator, led-kalkylator
1. **Header** (global mega-menu, "Gratis rådgivning" CTA, "Ring en expert 5.0"). Desktop: sticky bar. Mobile: offcanvas accordion.
2. **AlternativHero** (dark navy compact hero): breadcrumbs ("Hem / Ampy batterikalkylator") → heading ("Batterikalkylator: räkna ut vad du tjänar på ett solcellsbatteri") → sub-paragraph. No CTA, no image. Mobile: stacks, breadcrumb row on top.
   - **Defect found: on batterikalkylator this heading renders as `<h3>` — the page has NO `<h1>` at all** (block-map `h1: []` confirms; led-kalkylator renders a proper H1 "Vad sparar du på att byta till LED?").
3. **Calculator-UI** (two-pane: inputs left, live results right; "Så har vi räknat" methodology; embedded lead form "Få en exakt offert" / "Få en skräddarsydd offert" with Namn/E-post/Telefon/Postnummer + GDPR consent + honeypot). Mobile: panes stack, results below inputs.
4. **FAQ accordion** ("Vanliga frågor", 5 real questions with substantive answers — e.g. "Är ett solcellsbatteri lönsamt 2026?", lysrörsförbud explainer on LED). Content in DOM (SEO-safe).
5. **Prefooter + Footer** (global).
   - Missing vs owner's target: no **VarProcess**, no **MainContact** — the page ends at FAQ with no human close.

### State B — "half-wrapped": laddboxkalkylator, energikalkylator
- **laddboxkalkylator**: Header → Calculator-UI (H1 "Hur mycket sparar du på att ladda hemma?", eyebrow "Laddbox-kalkylator", full two-pane calc, "Så har vi räknat", lead form `ampyEvLeadForm`, "Läs mer om laddboxen" links to `/laddboxar/…` product pages) → Prefooter. **No AlternativHero (no breadcrumbs), no FAQ, no VarProcess, no MainContact.** Good `<title>` + meta description ("Sluta överbetala på offentliga laddstationer…").
- **energikalkylator**: Header → Calculator-UI (H1 "Energikalkylatorn" — label only; inputs: uppvärmning/boyta/byggår/boende/elområde/förbrukning/solceller; result "Så förbrukar ditt hus energi idag" + "Så mycket kan du spara per år"; sticky summary bar markup `ampy-ek__sb-*` + `position:sticky` present for mobile; share row "Kopiera länk / Dela via mejl / Dela på Facebook"; embedded lead form "En elektriker räknar på ditt hus" with Namn*/Telefon*/Postnummer*/E-post* + trust strip quote "Från start till mål levererades en service i världsklass." + "3 000+ genomförda installationer om året"; "Så har vi räknat") → Prefooter. **No AlternativHero, no FAQ, no VarProcess, no MainContact. No meta description. Title "Energikalkylatorn – Ampy".**

### State C — "naked shells": elcentral-kollen, elkollen, ampy-eljour (block-map: Header + Prefooter only)
- **elcentral-kollen**: title **"Ampy – Elcentral-kollen – Ampy"** (brand duplicated), **no H1, no H2, no meta description, 418 words**. The crawlable fallback is ASCII-broken Swedish: "Elcentral-kollen staller nagra snabba fragor … besked pa tva axlar: Saker? och Redo?" — missing å/ä/ö, visible to Google and no-JS users. The diagnostic (7 questions: "Hur gammalt är huset…", "Är elcentralen utbytt eller original?" …), the verdict routing (links to /elbesiktning/, byta-elcentral, jordfelsbrytare, lastbalansering found in JS), and the lead form ("Boka rådgivning" + consent + submit states, confirmed in JS strings) are **entirely client-rendered — invisible to crawlers**. Static fallback does list service links ("Vill du ga vidare direkt? … Elbesiktning / Byta elcentral / Installera jordfelsbrytare / Lastbalansering / Uppsäkring").
- **elkollen**: H1 "Får du göra eljobbet själv? Kolla innan du kopplar." + 25 job chips (Byta glödlampa … Skarva eller förlänga fast installation) → verdict per selection → trust strip ("Källa: Elsäkerhetsverket & Elsäkerhetslagen (2016:732)", "Registrerat elinstallationsföretag") → close "Hellre prata med en elektriker direkt? Kontakta oss / Ring 010-265 79 79". **No lead form, no wrap blocks.** Title "Ampy Elkollen – Ampy". 434 words crawlable.
- **ampy-eljour**: **no H1** (main heading is `<h2>` "Är något fel med elen? Tryck på det du upplever."), title "Ampy Eljour – Ampy", no meta description. Two-pane: sticky call panel ("Jour öppen just nu" / "Akut elfel? Ring oss direkt." / 4 promises incl. "Tydligt pris innan vi rycker ut, inga dolda avgifter" / "Ring eljouren 010-265 79 79") + 14+6 symptom accordion cards, each severity-tagged (Akut/Varning) with 112-first safety instructions and its own tel CTA (24 `tel:` links). Grounding stat "omkring 1 800 elrelaterade bränder … Källa: Elsäkerhetsverket." Mobile: fixed call-bar (26 sticky/fixed rules). Call-only by design — no form.

---

## Customer-flow walkthrough (35–65 Swedish homeowner, mobile)

**First 5 seconds (energikalkylator, the owner's example case):** Arrives from header "Guider & verktyg → Energikalkylator" or a shared link. Sees H1 "Energikalkylatorn" — a label, not a promise. No breadcrumb, no sub-line saying what she gets or why Ampy built it. She's dropped straight into an input form ("Vad värmer huset idag?") with zero framing of who Ampy is on this page. MECLABS 3v: value clarity is carried entirely by the tool's own labels.

**Scroll/use:** The calculator itself is genuinely good — plain-Swedish helper text ("Ett normalstort elvärmt hus drar 15 000-25 000 kWh om året. Siffran står på elnätsfakturan."), live result, sticky summary bar on mobile, share row. The lead ask is minimal (4 fields — Baymard-compliant) and value-then-ask ("En elektriker räknar på ditt hus. Vi hör av oss inom en arbetsdag").

**Decision point — where the leak is:** After the result, a hesitant visitor (the majority) who is not ready to submit has **nowhere to go**. No "how does an Ampy job actually work" (VarProcess), no testimonials, no FAQ answering the anxiety questions (fixed vs estimated offert, damage responsibility — the Byggahus/Reddit concerns in business context), no second form at the bottom. The page ends at "Så har vi räknat" → footer. The Clarity trust-seeking pattern (paid visitor who went Contact → About Us) predicts exactly this: **the magnets deliver value then abandon the trust-building job.** On elcentral-kollen/elkollen the shell is even barer; on batteri/LED the FAQ helps but the page still ends without a human close.

---

## What works (keep)

- **The calculators themselves.** Real interactive value, honest helper text, methodology disclosure ("Så har vi räknat … en uppskattning — inte ett erbjudande och inte bindande för Ampy"), no juiced defaults visible in fallback. This is the candour register done right and a genuine differentiator.
- **Embedded value-then-ask lead forms** (energi/laddbox/batteri/LED): 4 fields, honeypot, GDPR consent, success copy that sets an expectation ("En expert återkommer inom 24 timmar med en exakt offert. Du får kalkylen mailad till dig."). Baymard field-count principle satisfied.
- **Energikalkylator share row** (Kopiera länk / mejl / Facebook) — the only viral loop on the site.
- **ampy-eljour severity triage** — 112-first safety, "Tydligt pris innan vi rycker ut", Elsäkerhetsverket-sourced 1 800-bränder stat: Cialdini authority + Unbounce urgent-repair pattern, correctly call-only.
- **elkollen trust strip** — "Källa: Elsäkerhetsverket & Elsäkerhetslagen (2016:732)" + "Registrerat elinstallationsföretag" is exactly the proof a serious Swedish customer checks (Konsumentverket/Elsäkerhetsverket anchor from business context).
- **batteri/LED FAQ blocks** — real questions, real answers, in-DOM (SEO preserved), with internal links (LED FAQ → Elkollen: "Kolla in vårt verktyg Koppla Elen").
- **LED-kalkylator title/meta/H1** — the benchmark the others should copy ("LED-kalkylator: räkna ut vad du sparar på LED varje år" / benefit-framed H1).

---

## Findings

**LM-01 · P0 · Placeholder phone number in batterikalkylator error state.** The form-failure fallback reads "Något gick fel. Ring oss på **010-123 45 67** så hjälper vi dig direkt." (confirmed in live fetch and snapshot, 1 occurrence) — a dead dummy number shown at the exact moment a hot lead's submission fails. Laddbox/energi versions correctly use 010-265 79 79. Evidence: error-recovery is a conversion-critical path (NN/g error-state guidance); this converts a recoverable failure into a lost lead and a trust hit. Mobile: same string; tap-to-call would dial a wrong number if linked. One-line fix, ship this week.

**LM-02 · P0 (verify week 1) · Lead-webhook integrity unproven on the naked magnets.** No webhook endpoint is resolvable from the page HTML (posted from JS), and project state (Energycalc handover notes) records the energikalkylator lead webhook as a **stub — leads dropped**; elcentral-kollen launch was likewise gated on a webhook URL. If true in production, every submit on these pages 404s into nothing while showing "Tack." **HYPOTES to verify, not asserted:** submit a test lead on each of the 5 form-bearing magnets and confirm arrival in n8n/CRM + /thank-you or in-place success. Until proven, treat all magnet lead counts as untrustworthy. This also explains part of "0 confirmed form leads" in GA4: custom forms here do not emit `form_start`/`generate_lead` (business context) — instrument all 5 forms with the standard dataLayer contract.

**LM-03 · P1 · The orphan-wrap gap (the owner's own diagnosis, confirmed).** 5 of 7 magnets end without any trust/process/close architecture: energikalkylator + laddboxkalkylator end at the calculator, elcentral-kollen/elkollen/ampy-eljour are Header+tool+Prefooter shells. Even the two "wrapped" pages (batteri, LED) stop at FAQ — **no VarProcess, no MainContact anywhere in the family**, so the site's strongest conversion asset (MainContact, per block inventory) is absent from exactly the pages that pre-qualify visitors hardest. Framework: MECLABS HealthSpire — added content that answers real decision questions lifts conversion; the missing content here is the how-it-works + human-close sequence. JTBD: the visitor's job after "how much can I save?" is "can I trust these people to do it?" — currently unanswered on-page. Mobile: the deficit is worse because the naked pages are short — the visitor hits the footer within 1–2 result screens.
Priority arithmetic: 5 pages (fully naked/half) × 3 (adds form-stage block) × 2 (medium-high expected effect) = **30** — highest structural score in this family.

**LM-04 · P1 · Batterikalkylator has no H1.** The AlternativHero heading renders as `<h3>`; block-map records `h1: []`. The page ranks-relevant head term ("batterikalkylator") has no H1 carrier. Also breadcrumb markup exists here but on no other magnet. Fix: promote hero heading to H1 (led-kalkylator already does this correctly — copy its markup). 1 page × 3 × 2 = 6, but trivial effort.

**LM-05 · P1 · elcentral-kollen is invisible to Google and broken without JS.** Title "Ampy – Elcentral-kollen – Ampy" (duplicated brand), no H1/H2, no meta description, 418 crawlable words, tool + verdict + lead form all client-rendered, and the crawlable fallback text has stripped diacritics ("staller nagra snabba fragor … Saker? och Redo?") — malformed Swedish shown to Google and screen-reader/no-JS users. This kills both discoverability and the E-E-A-T impression for the flagship "byta elcentral" commercial lane (search terms in the paid data: "byta elcentral pris", "byta proppskåp"). Fix: server-render a static summary (H1 + what the tool checks + the two axes Säker?/Redo? + service links) with correct Swedish; keep the app on top of it.

**LM-06 · P1 · Candour gate: "5.0" unanchored on every magnet page.** Header ("Ring en expert 5.0"), footer ("5.0"), and `AggregateRating` JSON-LD ship on all 7 pages with no review count or owner-confirmed current rating anchor. Energikalkylator's in-form trust strip does it right ("5 av 5 · Betyg på Google" + named reviewer) — the global chrome doesn't. Cross-template issue (owned by global-nav audit) but recorded here because these pages otherwise preach candour ("inte ett erbjudande, inte bindande"). Anchor as "{rating} av 5 · {N} omdömen på Google" or drop.

**LM-07 · P2 · Label-H1 and missing metas on the naked magnets.** energikalkylator H1 "Energikalkylatorn" + no meta description; elkollen title "Ampy Elkollen – Ampy"; ampy-eljour has **no H1 at all** and title "Ampy Eljour – Ampy"; none of the three has a meta description. Google message match + MECLABS value clarity: the SERP snippet and first screen should state the benefit ("Se vad ditt hus drar — och vad du kan spara"), as LED/laddbox already do. 4 pages × 3 (hero) × 1 = 12.

**LM-08 · P2 · Discovery orphaning + nav label mismatch.** Header "Guider & verktyg" lists only 4 tools and with mismatched names: "Energikalkylator" (page says Energikalkylatorn), "**Elcentralkalkylator**" (page is Elcentral-kollen — a diagnostic, not a calculator). LED-kalkylatorn, Elkollen and ampy-eljour are in NO navigation surface (orphan in the crawl sense too). Jakob's law/message match: the link label must match the destination H1. Also decide /ampy-eljour/'s relationship to /eljour/ — same intent served by two URLs risks cannibalising the service page; either canonicalise, merge, or make /ampy-eljour/ the campaign-only landing page (noindex is defensible if it's a paid-only asset — owner call).

**LM-09 · P2 · elkollen has no lead-capture bridge on "electrician-required" verdicts.** When the verdict is "this requires an authorized electrician" the close is a generic "Kontakta oss / Ring …" — no form, no deep link into the matching service page's prefilled Hero_2 form (the URL-resolver prefill mechanism already exists per block inventory). The tool pre-qualifies intent ("Ansluta spis eller ugn", "Arbete i elcentralen" = exactly the paid search terms) and then drops it. Fix: verdict CTA → service page with `?arbete=` prefill, plus MainContact at page bottom. 1 × 3 × 2 = 6.

**LM-10 · P2 · laddboxkalkylator missing FAQ + hero wrap despite being the priority-2 commercial lane.** Commercial priority is service > laddbox > battery, yet batterikalkylator (priority 3) got the fuller wrap first. Add the batteri/LED-pattern FAQ (laddbox questions exist in the vertical's content) and AlternativHero with breadcrumbs. SEO substance is added, nothing removed. 1 × 2 × 2 = 4.

**LM-11 · P3 · Consent-microcopy inconsistency across the 5 forms.** energikalkylator: implicit consent sentence under the button; laddbox: explicit checkbox with revocation rights text; LED: short "Jag godkänner…" checkbox. One GDPR pattern should govern (the laddbox version is the most defensible). Low conversion impact, compliance hygiene.

**LM-12 · PASS (candour check, recorded).** ampy-eljour "Jour öppen just nu" is consistent with the stated "Jour dygnet runt, året om" — not fake urgency. The 1 800-bränder stat is sourced (Elsäkerhetsverket). batteri/LED methodology disclaimers are exemplary candour. No banned tactics found on any of the 7 pages.

---

## Recommended sequence (wireframe) — the standard "magnet wrap"

Owner's example fix for energikalkylator, extended into the family standard. SEO substance is only added, never removed.

| # | Block | Why here | New/existing/modified |
|---|---|---|---|
| 1 | **AlternativHero** (breadcrumbs + benefit-framed **H1** + 1-line sub naming the tool and the promise) | Orients arrivals from nav/ads/shares; message match (Google); fixes H1/meta layer | Existing block, new instances (5 pages) + H1-tag fix on batterikalkylator |
| 2 | **Calculator-UI** (the magnet, unchanged, incl. its embedded value-then-ask lead form + "Så har vi räknat") | The value engine; do not disturb approved rendering | Existing |
| 3 | **VarProcess** (4 steps, copy tuned per magnet: "Skicka kalkylen → vi ringer inom 24h → kostnadsfri rådgivning → fast offert") | Answers "what happens if I submit?" — the anxiety (MECLABS 2a) the Byggahus research says Swedish homeowners carry | Existing block, per-magnet copy |
| 4 | **FAQ accordion** (magnet-specific; already live on batteri/LED — build for energi/laddbox/elcentral) | HealthSpire: content that answers decision questions lifts, not shortens; in-DOM = SEO gain | Existing pattern, 3 new content sets |
| 5 | **MainContact** (global two-pane form, anchored trust: "5 av 5 · Betyg på Google", "3 000+ genomförda installationer om året") | The site's strongest converter as the human close for visitors the in-tool form didn't catch | Existing |
| 6 | Prefooter/Footer | — | Existing |

**Per-magnet variants (divergences, per house rule):**
- **ampy-eljour (call-only):** AlternativHero-variant with H1 → symptom block → keep call-only: substitute step 5 with **MainCTA (ring-only)** or the existing sticky call panel — a form here would fight the urgent JTBD (Unbounce: urgent-repair pages convert on the call). Add H1 + meta only.
- **elkollen (DIY audience):** wrap steps 1–4, and route "electrician-required" verdicts to prefilled service pages (LM-09) **before** MainContact — capture at intent peak.
- **elcentral-kollen:** the wrap PLUS the server-rendered Swedish summary layer (LM-05) so the page exists for Google.
- **Mobile ordering note (all):** hero compact (≤1 screen), calculator immediately second; sticky result bar (energi pattern) should generalise to laddbox/batteri so the value stays visible while scrolling to VarProcess/MainContact.

---

## Test hypotheses (top 3, A/B)

1. **HYPOTES — wrap lift:** On /energikalkylator/, adding AlternativHero + VarProcess + FAQ + MainContact below the unchanged calculator increases (form submits + phone clicks)/session vs the current naked page, without reducing calculator completion rate. (MECLABS HealthSpire; primary metric: qualified leads per 1 000 sessions.)
2. **HYPOTES — benefit H1:** Replacing label H1s ("Energikalkylatorn") with benefit-framed H1s ("Vad drar ditt hus — och vad kan du spara per år?") increases scroll-past-hero rate and calc-start rate on energi/elcentral/eljour vs label versions. (Google message match + MECLABS value clarity.)
3. **HYPOTES — verdict bridge:** On /elkollen/, an "electrician-required" verdict CTA that deep-links to the matching service page with prefilled "Vad gäller arbetet?" produces a higher lead rate than the generic "Kontakta oss" close. (JTBD intent-peak capture; guardrail: no drop in call clicks.)

**Sequencing recommendation:** Week 1 = LM-01 (phone string) + LM-02 (webhook + form-event verification on all 5 forms) — nothing else matters if leads evaporate. Month 1 = LM-03 wrap rollout starting with energikalkylator (owner's example) then laddboxkalkylator (commercial priority 2), + LM-04/LM-05 markup fixes. Months 2–3 = LM-07/08/09/10 (metas, nav labels + orphan links, elkollen bridge, laddbox FAQ), then LM-11.
