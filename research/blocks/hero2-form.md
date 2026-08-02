# Hero_2 + `.aof` form (service-page hero + quote form)

**Used on: 260 pages** (verified in `data/block-map.json`; note: assignment brief said 238 — the verified count is 260 of 326 mapped pages, 79.8% of the site). Categories: elektriker-i 56 · elinstallation-i 56 · eljour-i 56 · laddbox-i 56 · service 22 · elektriker-för-x 13 · page (batterilagring) 1.
**Funnel position: block index 1 (immediately after Header) on all 260 pages** — every page that has Hero_2 also has `Hero_2-aof-form` (260/260), and no page has the form without the hero. This is the first thing every paid-search and organic service visitor sees. All 260 pages also carry MainCTA + MainContact + FooterSEO further down (225 also BlueCTA, 169 also MikroCTA), so Hero_2 is ask #1 of typically 5–7 asks per page.

**Live evidence base (fetched 2026-08-02):**
- `https://ampy.se/elservice/elcentral/` — H1 `<h1 class="…hero_2__section-subheading">Byta elcentral</h1>`, H2 `<h2 class="…hero_2__section-heading">Ny elcentral installerad med 30% ROT-avdrag</h2>`, paragraph "Dags att byta ditt gamla proppskåp? …", CTAs `Kostnadsfri rådgivning` → **`https://ampy.se/kontakt/`** and `Ring 010-265 79 79` → `tel:+46102657979`, then a GBP-linked row containing only "5.0" + 5 stars.
- `https://ampy.se/eljour/taby/` — same structure: H1 "Eljour i Täby", H2 "Eljour dygnet runt: Ring 010-265 79 79!", same two CTA hrefs (primary again → `/kontakt/`).
- The `.aof` form is **rendered entirely client-side** from a 56 kB URL-encoded `<script defer src="data:text/javascript,…">` blob into `<div id="ampy-form-root" class="aof" data-endpoint="https://…supabase.co/functions/v1/hero-lead" … data-thankyou="/thank-you">`. Decoded script (saved during audit) confirms: card title `<h1 class="title">Få kostnadsfri rådgivning!</h1>` + "Vår behöriga elektriker återkommer via telefon!" → kundtyp radiogroup (Privat/BRF/Företag) → "Vad gäller arbetet?" select → required fields (privat: Namn → Telefonnummer+E-post → **Adress+Postnummer**) → "Fler detaljer (valfritt)" disclosure (beskriv, tidsram, bilder, org-fält) → GDPR checkbox → "Boka rådgivning" → POST → redirect `/thank-you`.

---

## What it does well (keep — this is real craft)

1. **The per-page prefill resolver is genuinely good.** `resolve(location.pathname)` maps every URL family to a config: 22 `/elservice/{slug}` slugs → a locked-but-editable "Vad gäller arbetet?" preselect (elcentral→"Elcentral", vitvaror→"Vitvaror" …); `/eljour/*` preselects "Elfel"; `/laddbox/*` locks "Laddbox"; `/batterilagring` locks "Batterilagring"; every elektriker-för-X vertical gets its own kundtyp + bespoke option list (restauranger → "Storkök / fläkt / trefas…", kommuner → orgLabel "Förvaltning eller enhet"). The preselect is **visible and editable** — the code comment says it best: "the exploring visitor is not trapped by the page they happen to be on." This removes one decision on ~240 of 260 pages and stamps `vertical`/`tjanst_intresse`/`kallsida` onto the lead. Keep and extend; never flatten this into a generic form.
2. **Page preselects kundtyp but the visitor's choice wins** (`segTouched` guard) — correct precedence.
3. **Failure recovery routes to the other conversion**: on fetch error the card becomes "Något gick fel — Försök igen, eller ring oss på 010-265 79 79" with a tel: link and a retry button. Textbook.
4. **Solid form hygiene**: honeypot (`aof-company_url`), `novalidate` + per-field Swedish error copy ("Postnummer ska vara fem siffror."), E.164 phone normalisation, correct `autocomplete` attrs, `aria-live` status region, roving-tabindex radiogroup, duplicate-mount guard, "Skickar…" disabled state, GDPR consent with `policy_version` stamped into the payload.
5. **Redirect to `/thank-you` is preserved** (`data-thankyou="/thank-you"` → `location.href=THANKYOU` after `dataLayer.push({event:'ampy_lead_submit', kundtyp, vertical, tjanst, kallsida, source_form})`), so the GA4/Ads conversion pageview can fire, with useful lead dimensions attached.
6. **The "Fler detaljer (valfritt)" disclosure is the right pattern** (Baymard: perceived difficulty tracks *visible/required* fields) — optional enrichment (beskrivning, tidsram, bilder, orgnr) stays out of the required path, and enrichment fields can never block a lead.

---

## Issues

### H2-01 · P0 · Triple simultaneous ask — and the primary CTA navigates AWAY from its own form
**Desktop:** the first screen presents three competing conversion mechanisms: green "Kostnadsfri rådgivning" button, blue "Ring 010-265 79 79" button, and the aof form card 400 px to the right whose title is *also* "Få kostnadsfri rådgivning!". Worse, the green button's href is `https://ampy.se/kontakt/` — it promises exactly what the adjacent form delivers, and answers the click with a page load to a *different* form. Evidence: MECLABS attention-ratio / Unbounce 1:1 principle (one page, one goal); Hick's law (three equal-weight choices delay all of them); the live GA4 picture (33 paid clicks, 2 phone clicks, 0 recorded form interactions) is consistent with attention never settling on the form. On `eljour/taby` this is also a message-match break: H2 shouts "Eljour dygnet runt: Ring 010-265 79 79!" yet the visually-primary green button offers a calm detour to /kontakt/.
**Mobile (390 px):** worst case. Container stacks text-column first (source order), primary button becomes `width:100%` at ≤767 px — so the first screen is breadcrumb → eyebrow → big H2 → paragraph → full-width green button. The best-converting element on the page (the form) sits ~2 viewports down, and the first thumb-reachable action **leaves the page**.

### H2-02 · P0 · Measurement void: the form emits exactly one analytics event
The decoded script contains **one** `dataLayer.push` — `ampy_lead_submit`, fired only at submit. No `form_start`, no field-focus, no kundtyp/disclosure interaction, no validation-error, no fetch-error event. This is why GA4 shows "0 form starts" on ~32 paid sessions: the funnel between render and submit is unobservable, so "nobody touched it" and "everyone abandoned at Adress" are indistinguishable. Cheapest-possible P0: add `form_start` (first focusin), per-field abandon, error events. (ampy-webb-playbook instrumentation contract already specifies this.)

### H2-03 · P1 · H1/H2 inversion + a second H1 injected by the form
On all 260 pages the H1 is the *small* green eyebrow ("Byta elcentral", "Eljour i Täby") and the big value headline is an H2 ("Ny elcentral installerad med 30% ROT-avdrag"). Visually acceptable; semantically the page's largest promise is demoted. Compounding it: the JS form injects `<h1 class="title">Få kostnadsfri rådgivning!</h1>`, so the **rendered DOM has two H1s on every one of the 260 pages**, the second being identical boilerplate site-wide. Fix is CSS-free: keep the visual design, swap heading tags (H1 = the big headline, keep the keyword eyebrow as a `<p>`/`<span>` or fold the keyword into the H1), and demote the form title to `<h2>`/`<p>`. SEO substance preserved — this is re-tagging, not rewriting. Google message match: the ad-clicked query ("byta elcentral pris") should meet its strongest echo in the H1.

### H2-04 · P1 · Field order: Adress + Postnummer required before any value is delivered
Privat required set = Namn, Telefonnummer, E-post, **Adress, Postnummer** (5 required + kundtyp + tjänst-select + GDPR ≈ 8 visible interactions). The card's own promise is "Vår behöriga elektriker återkommer via telefon!" — a phone callback needs name + phone (+ postnr at most, for routing/ops geo). Full street address before the visitor has received anything is a commitment/anxiety spike exactly at the Swedish homeowner's sore point (Byggahus/Reddit: "final price surprises", "will they answer later"). Baymard: visible+required field count drives perceived difficulty more than actual effort; MECLABS friction term `−2(i−f)`. Move Adress into "Fler detaljer"; keep Postnummer (ops needs it). HYPOTES: "Removing required Adress from the aof form increases form submits per session with no measurable drop in lead contactability (address is captured in the 24h callback anyway)."

### H2-05 · P1 · Unanchored 5.0 — candour-gate violation on 260 pages
The hero trust row is literally `<div class="…">5.0</div>` + five stars inside a GBP link — no count, no "på Google" label, no date. The candour gate requires rating + count + source or removal; an unanchored "5.0" reads as decoration to the trust-seeking 35–65 visitor (the Clarity recording that went Contact → About Us was hunting for exactly this proof). The MainContact block lower on the same pages already does it nearly right ("5 av 5 · Betyg på Google"). Fix: "5,0 av 5 · N recensioner på Google" with owner-confirmed current N, or drop the number and keep the labelled GBP link. (Owner confirmation of current rating/count is an open gap — flagged, not invented.)

### H2-06 · P2 · Dark-on-dark: navy card on navy aurora + low-contrast microcopy
The section container's background is a dark navy aurora image (`Group-13582-1.webp`) and the `.aof` card's base token is `--mid:#090b32` — near-identical values, so the form card barely separates from its background (the block inventory's known tension, confirmed in CSS). Small text compounds it: consent text 12.5 px at `opacity:.82`, subtitle 15 px at `.9`, help text 13 px `#bff3e6` — thin weights on navy, judged by 45–65-year-old eyes on a phone in daylight. WCAG 1.4.3 risk on the consent line; NN/g: forms on dark, low-separation surfaces read as "advanced/technical", the opposite of the reassurance this audience needs. HYPOTES: "A light (white/#f5f9ff) form card on the dark hero increases form starts vs the navy card" — the site's own MainContact form pane (its strongest converter) is already light.

### H2-07 · P1 · The money block is JS-only and last to paint
The entire form exists only after a 56 kB `data:` URI `defer` script executes and injects DOM. With the documented ~9–10 s lab LCP, the right column is an empty navy box during the exact seconds a paid visitor decides to stay (Clarity: 1 s and 23 s abandons). No-JS/failed-JS visitors get nothing at all (mitigated by the phone CTA, but on mobile that's a different problem — see H2-01). Recommendation: server-render the shell (title, subtitle, first fields) in Bricks and let JS hydrate the resolver behavior; at minimum render a static skeleton with the card chrome + title so the slot is visibly "a form" at first paint.

### H2-08 · P2 · Kundtyp toggle is the first interactive element
Privat/BRF/Företag segmented control sits above everything, forcing a self-classification before any value question — yet on 224 of 260 pages (the four geo CPTs) the visitor is near-certainly privat, and the resolver already knows the page's default. Hick's law: a decision that 90%+ of visitors answer with the default is friction, not routing. Recommendation: default privat silently; demote the toggle to a quiet text link under the fields ("Företag eller BRF? →" swaps the field set). Keep the full toggle only on elektriker-för-X pages where kundtyp is genuinely ambiguous (the resolver's EFX map already flags exactly these).

### H2-09 · P3 · "Fler detaljer (valfritt)" disclosure — right pattern, vague label
The dashed-border toggle labelled "Fler detaljer (valfritt)" undersells its contents (photo upload is the single highest-lead-quality enrichment for an electrician — a picture of the proppskåp). A benefit-labelled disclosure ("Beskriv jobbet eller ladda upp en bild — då kan vi ge ett snabbare besked") should lift enrichment usage without adding required friction. Mobile: the collapsed disclosure is fine; no change to the pattern itself.

### H2-10 · P2 · Eljour message mismatch (56 pages)
On eljour geo pages the H2 is call-imperative ("Eljour dygnet runt: Ring 010-265 79 79!") and the resolver correctly preselects "Elfel" — but the card still opens "Få kostnadsfri rådgivning!" / "Boka rådgivning", planned-purchase language on an emergency page (Unbounce: urgent/repair intent converts on immediacy). The form itself is right to exist here (owner decision, and some visitors prefer writing at 02:00); the copy register should shift per-vertical — the resolver already carries `vertical:'service'`+`tjanst:'Elfel'` and could just as easily carry a card-copy variant ("Akut elfel? Ring direkt — eller skriv, så ringer vi dig.").

---

## Recommended changes (concrete)

1. **Collapse the triple ask to a 1+1 hierarchy** (P0): on all 260 pages, primary green CTA stops navigating to /kontakt/ and instead scrolls/focuses the adjacent aof form (desktop: focus first field; mobile: smooth-scroll to card). "Ring …" stays as the co-equal second path. Eljour pages invert: Ring primary, form secondary. Attention ratio drops from 3 competing mechanisms to 2 intentional ones.
2. **Mobile order swap** (P0, ships with #1): at ≤767 px render H1 → one-line paragraph → form card → Ring button → rating → rest. The form — not a detour button — becomes the first-screen action. HYPOTES: "Form-above-CTAs on mobile increases form starts on paid landings vs current stack."
3. **Instrument the form** (P0, ~hours of work): `form_start` on first focusin, `form_field_abandon` (last focused field on unload), `form_error` (field id), `form_submit_error`, disclosure-open, kundtyp-switch — all pushed with the existing kundtyp/vertical/kallsida dimensions, consent-gated per the playbook contract. Do this FIRST so every other change becomes measurable.
4. **Re-tag headings** (P1): big headline becomes the H1 (keyword folded in: "Byta elcentral — installerad med 30% ROT-avdrag" pattern); eyebrow becomes non-heading; form title `<h1>`→`<p class="title">`. Zero visual change, zero copy deletion.
5. **Demote Adress to "Fler detaljer"** (P1): required set becomes Namn, Telefon, E-post, Postnummer. Payload/webhook fields unchanged (adress already nullable in `buildPayload`).
6. **Anchor the 5.0** (P1): "5,0 av 5 · N recensioner på Google" (owner to confirm current N) or remove the numeral. Apply the same fix wherever the hero pattern is cloned.
7. **Lighten the card or its backdrop** (P2): test a light form card (site-standard white/#f5f9ff, dark text) on the navy hero; simultaneously raise consent/help text to ≥14 px and kill sub-.9 opacities on navy.
8. **Silent kundtyp default + text-link switcher** on geo/service pages; keep the visible toggle only where EFX marks kundtyp ambiguous (P2).
9. **Server-render the card shell** with JS hydration for the resolver (P2, pairs with the site-wide speed workstream).
10. **Per-vertical card copy via the resolver** (eljour register first) (P2). Copy direction only — final Swedish through ampy-rost.

## Priority score (doctrine arithmetic)

- Pages affected: **260**
- Funnel position weight: hero/form = **3**
- Expected effect: **high = 3** (first screen of 80% of the site; both conversion paths originate here; paid traffic lands here with 0 recorded form leads)

**Priority score = 260 × 3 × 3 = 2340** → **P0**. Highest-leverage block on the site; nothing else in the inventory can match this product of reach × position × effect. Sequencing inside the block: instrument (#3) → CTA/mobile restructure (#1–2) → friction & trust (#4–6) → surface & register (#7–10).
