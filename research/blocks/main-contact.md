# MainContact — `main-contact` (global two-pane contact form)

Used on: **295 of 326 pages** (block-map.json verified) — battery-product 10, elektriker-for-x 13, elektriker-i 56, elinstallation-i 56, eljour-i 56, ev-product 16, laddbox-i 56, page 10 (incl. homepage + /kontakt/), service 22. Absent only on lead-magnet (7), post (11), team-member (6) and 7 misc pages — the lead-magnet absence is a known separate finding (orphan pages).
Funnel position(s): **bottom-of-page primary form** on virtually every template; **sole above-fold block** only on /kontakt/ (0 blocks before it). It is the site's designated "strongest converter".

Live page fetched for this audit: `https://ampy.se/elektriker/akersberga/` (real copy quoted below). Markup detail from snapshot `data/pages/elservice.html`.

## Verified structure (live copy, 2026-08-02)

**Left photo pane** (dark-overlay photo, desktop): white Ampy logo → quote *"Från start till mål levererades en service i världsklass."* → gold ★★★★★ + *"5 av 5 · Betyg på Google"* → *"3 000+ genomförda installationer om året"* → 3 steps: *"Skicka in dina uppgifter" → "Vi ringer dig inom 24 timmar" → "Kostnadsfri rådgivning av elektriker"*.

**Right form pane**: H *"Få en kostnadsfri rådgivning"* (gradient last word) → *"Bli uppringd av vår behöriga elektriker som konsulterar dig från start till mål."* → fields (from markup, `required` attributes verified):

| Field | name | Required |
|---|---|---|
| Förnamn | `forenamn` | **yes** |
| Efternamn | `efternamn` | **yes** |
| E-post | `email` | **yes** |
| Telefonnummer | `telefon` (E.164 gate) | **yes** |
| Adress | `adress`, placeholder *"Sök efter din adress \*"* (Google Places autocomplete, SE-locked) | **yes** |
| Gatuadress / Postnummer / Postort | `adress_gata` / `adress_postnr` / `adress_ort` (manual fallback) | no |
| Meddelande | `meddelande`, *"Valfritt meddelande"* | no |

→ submit *"Gratis rådgivning"* (teal gradient pill, arrow icon) → consent line *"Genom att skicka in godkänner du att Ampy kontaktar dig enligt vår integritetspolicy."* → native Bricks POST → n8n → /thank-you.

**Position within pages** (block-map, blocks before MainContact excluding Header): 6 blocks on 143 pages, 7 on 10, 8 on 22, 9 on 58, **10 on 56 (all eljour-i geo pages)**. Only /kontakt/ (0), /elservice/ (3), /laddboxar/ (4) and 3 pillar pages (5) place it earlier. It is *not* the last block: 5–11 further blocks follow it on 288 pages (immediately after: FAQ on 131 pages, MapBlock 79, ROT-block 57, ProductGrid 26).

**Mobile behavior** (verified from the shipped CSS/JS in the page source, breakpoint 768px, quote rule to 991px):
- Card stacks; whole card takes the photo + dark overlay `rgba(6,8,26,.55)` as background.
- **Logo hidden. Volume proof ("3 000+ …") hidden** — CSS comment says *"volume proof hidden (owner call)"* — even though the JS ("Ampy global contact form — JS pane") first *moves* it below the form pane, so it is moved then display:none'd (dead weight).
- Quote scales to `clamp(2.4rem, 2rem + 2.4vw, 3rem)` and is clamped to **`max-width:15ch !important`** at ≤991px (comment: *"PARITY: prototypen ar 15ch = 288.46px"*). The 52-character quote at 24–30px wrapped inside 15ch renders as ~5 lines of display-size text.
- 3 steps are **moved below the form pane** (column ≤460px, 3-up row 461–768px).
- Fields go single-column ≤478px; Förnamn/Efternamn and E-post/Telefon are 2-col above that.
- Card has a Bricks `enterView → fadeIn` interaction with `data-interaction-hidden-on-load="1"`.

## What it does well

- **Value-then-ask microcopy is right.** "Bli uppringd av vår behöriga elektrikare som konsulterar dig" names the outcome (a callback from a qualified electrician), and the 3-step strip answers the Swedish homeowner's #1 unspoken question — *what happens after I press the button?* (Byggahus/Reddit anchor: "will they answer later"). "Vi ringer dig inom 24 timmar" is exactly the anxiety-reducer MECLABS' `−2a` term rewards.
- **Real proof elements in the right family**: a customer quote, a Google-anchored rating row, a volume claim, next to the ask — Cialdini social proof adjacent to the point of decision, which most of the site's other blocks scatter.
- **Craft quality is high**: forgiving inline validation, E.164 phone gate, honeypot, a11y live regions, SE-locked Places autocomplete with manual fallback, prefers-reduced-motion support. This is the best-engineered form on the site.
- **Consistent global placement** gives every SEO page a conversion floor; the /kontakt/ page reuses it as the hero, so the "Kontakta oss" promise in header/footer always lands on a working form.

## Issues

### MC-01 — "3 000+ genomförda installationer om året" is an unanchored volume claim — P0 (candour)
Desktop: shown on every one of 295 pages. Mobile: hidden entirely.
Evidence: candour gate (business context §Brand: volume/social-proof claims must be owner-confirmed current; "1000+ kunder" is the named precedent). No source, no year, no basis is given anywhere on the page. If it is true and current, it survives with an anchor ("3 000+ installationer 2025"); if it cannot be confirmed, it must go. Either way, today it is the exact claim-shape the candour gate exists to catch — on the site's single most trusted block. Flag: **owner confirmation required**.

### MC-02 — "5 av 5 · Betyg på Google" has no review count — P0 (candour)
Desktop + mobile (rating row survives mobile).
Evidence: method doctrine §4: *"'5.0' claims must be anchored (rating + count + source) or removed."* Source is present (Google, gold stars), count is absent. A 35–65 risk-averse homeowner reads unanchored perfection as advertising, not evidence (NN/g trust research direction; Baymard: specificity drives credibility). Same defect exists in ≥6 blocks site-wide, but this block is where the form lives, so fix here first. Pattern: *"5,0 av 5 · N omdömen på Google"* linked to GBP — count owner-confirmed.

### MC-03 — Five required fields, including full street address, for a phone callback — P1 (friction)
Desktop + mobile identical field set.
Evidence: Baymard — the number of *visible required* fields drives perceived difficulty more than actual effort; MECLABS `−2(f)` friction and `−2a` anxiety terms. The offer is "bli uppringd" — a callback. The visitor is asked for Förnamn + Efternamn (a split that exists for CRM tidiness, not for them — one "Namn" field does the same job with one fewer ask), a required E-post *and* a required Telefon (the callback needs only the phone), and a **required street address** before any conversation has happened. Swedish homeowner anxiety anchor: price-uncertainty and "why do they need this before we've even talked" — a street address pre-quote reads as commitment. Postnummer alone routes the lead geographically (the 27-kommun ops routing needs nothing finer). Note the Places widget is genuinely good — the issue is `required`, not the widget. Also: GA4 shows **0 recorded form starts** from ~32 paid sessions; with 2 phone clicks in the same cohort, the phone path out-performed the form path — consistent with (not proof of) a friction problem. HYPOTES: reducing visible required fields to Namn + Telefon + Postnummer (E-post and Adress optional/progressive) lifts form submits vs. control — A/B at n8n level, lead-quality tracked to close.

### MC-04 — Mobile inverts the proof architecture: decoration gets the viewport, reassurance gets buried — P1 (mobile)
Mobile only (≤768/991px), i.e. the primary rendering (doctrine: assume ≥65% mobile).
Evidence: verified CSS — volume proof hidden, logo hidden, quote blown up to display size and clamped to `15ch` (~5 lines filling most of the block's first mobile viewport), and the 3-step strip **including "Vi ringer dig inom 24 timmar" moved below the form**. So the mobile visitor's sequence is: giant stylised quote → stars → form fields → submit → *then* learns what happens next. MECLABS: the anxiety-reducer must appear before/at the point of decision, not after it; NN/g mobile: users decide within the first screen of a section. The element with the least decision-information (an 8-word quote) received the most space; the element that answers "what happens when I submit?" is post-CTA. The "owner call" to hide the volume proof also means mobile carries *less* proof than desktop on the majority device.

### MC-05 — On 289/295 pages the strongest converter sits after 6–10 content blocks; on all 56 eljour geo pages, after 10 — P1 (position/exposure)
Desktop + mobile.
Evidence: block-map arithmetic above. GA4 (July paid cohort): ~32 sessions, ~17 deep-scrolled → roughly half of paid visitors plausibly ever render this block. On eljour-i pages the visitor's JTBD is urgent ("elfel i huset") — phone-first is correct there, but a form 11 sections down is effectively unreachable for the segment that won't call (evenings, BRF boards documenting an issue). This is not an argument to move the block everywhere — bottom placement after content is legitimate MECLABS sequencing (HealthSpire: content that answers questions *then* the ask) — it is an argument that (a) mid-page CTAs ("Kostnadsfri rådgivning" buttons in MikroCTA/FooterSEO/Hero_2) should anchor-scroll to this block instead of competing with their own asks, and (b) eljour templates need the form (or a cut-down variant) within the first 3 blocks. Also note: FAQ *follows* the form on 131 pages — objection-handling after the ask; on those templates swap FAQ above MainContact (MECLABS sequencing; content stays in DOM, SEO preserved).

### MC-06 — Promise and label inconsistency across the conversion chain — P2 (message match)
Desktop + mobile.
Evidence: Google message-match principle extended to internal consistency (Jakob's law: users expect the same thing to be called the same thing). This block: heading *"Få en kostnadsfri rådgivning"*, button *"Gratis rådgivning"*, steps promise *"inom 24 timmar"*. Hero_2 form: *"Boka rådgivning"*. Thank-you page: *"inom kort"*. Four labels and two different callback promises for one identical action. The 24h promise is the strongest of them — if owner-confirmed as an SLA the team actually meets, standardise **"inom 24 timmar"** everywhere including /thank-you (candour: only if actually met); one verb for the button site-wide.

### MC-07 — Form emits no form_start; the block's performance is unmeasurable — P2 (instrumentation)
Evidence: business context — GA4 recorded **0 form starts** while sessions, scrolls and phone clicks tracked fine; diagnosis "custom form may not emit form_start". This is the block every CRO decision above depends on. Add form_start on first field focus + per-field abandon events (field name, not value) through the existing dataLayer, consent-gated per playbook. Without this, MC-03/MC-04 hypotheses cannot be judged.

### MC-08 — Two different lead schemas on the same page — P3 (data consistency)
All Hero_2 pages (≈259) carry the `.aof` hero form (kundtyp toggle + "Vad gäller arbetet?" select + Namn + …) *and* MainContact (Förnamn/Efternamn + Adress, no kundtyp, no arbete). Two forms, different fields, same n8n pipe → inconsistent lead records and a visitor who scrolled past form #1 meets a form that asks different questions. Long-term: converge on one field contract (the Hero-2 redesign's "min lead = namn+telefon+postnr" doctrine) with per-block presentation.

### MC-09 — Card is hidden-on-load pending a JS fadeIn — P3 (robustness)
Markup: `data-interactions='[{"trigger":"enterView","action":"startAnimation","animationType":"fadeIn"}]'` + `data-interaction-hidden-on-load="1"`. If the interactions script fails or is delayed (the site already has a ~9–10s lab LCP flag), the primary conversion block renders invisible. HYPOTES (needs a throttled/JS-off render to confirm severity): remove hidden-on-load from this block specifically — a form should never depend on an animation to exist.

## Recommended changes (concrete)

1. **Candour pass (week 1, no design work):** anchor or remove "3 000+ genomförda installationer om året"; anchor the rating as "5,0 av 5 · N omdömen på Google" (GBP-linked). Both need one owner confirmation each. (MC-01, MC-02)
2. **Field diet:** Namn (single field) + Telefonnummer + Postnummer required; E-post optional ("om du hellre vill bli kontaktad via mejl"); Adress optional with the Places widget kept as the postnummer-filler; Meddelande stays optional. Run as A/B against the current set with lead-quality tracked to Closed Won, not just submits. (MC-03)
3. **Mobile re-stack:** compress the quote (body size, no 15ch display treatment), restore ONE line of hard proof above the form (the anchored rating or the anchored volume claim), and move the 3-step strip — or at minimum the line *"Vi ringer dig inom 24 timmar"* — **above the submit button** (e.g. as microcopy directly under the CTA). Copy-pattern direction, not final copy: "Skicka in — vi ringer dig inom 24 timmar." (MC-04)
4. **Exposure without duplication:** make mid-page CTA buttons on the same page anchor-scroll to `#main-contact` instead of pushing to /kontakt or competing; on eljour templates add a cut-down 3-field variant within the first 3 blocks (phone stays primary). Swap FAQ above MainContact where it currently follows (131 pages). (MC-05)
5. **One vocabulary:** pick one action label ("Få kostnadsfri rådgivning" as heading, one button verb) and one callback promise (24h if owner-confirms the SLA) across Hero_2, MainContact, popup and /thank-you. (MC-06)
6. **Instrument before iterating:** form_start on first focus, per-field abandonment, submit-error events → dataLayer, consent-gated. Ship this before or with change 2 so the A/B is readable. (MC-07)
7. Backlog: unify the Hero_2/MainContact field contract; drop hidden-on-load on this block. (MC-08, MC-09)

## Priority score (arithmetic)

Formula: (pages affected) × (funnel position weight) × (expected effect).

- Pages affected: **295**
- Funnel position weight: **3** (form block — the conversion point itself)
- Expected effect: **2** (medium — the block is already the site's best converter; these are candour, friction and mobile-sequencing refinements plus measurement, not a rebuild. The upside is real given 0 recorded form leads from paid, but the block is not the *cause* of arrival-leaks upstream)

**Priority score = 295 × 3 × 2 = 1770.**

Overall block priority: **P1** (fix in month 1) — with two embedded **P0 candour items** (MC-01, MC-02: trust-damaging claims, fix in weeks 1–2, copy-only) and the P2 instrumentation fix (MC-07) as a prerequisite for testing everything else.
