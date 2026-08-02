# FAQ block (`faq-` / FAQ + FAQ-accordion)

Used on: **309 of 326 pages** — the second-most-deployed content block on the site.
Category spread (from `data/block-map.json`): elektriker-i 56 · elinstallation-i 56 · eljour-i 56 · laddbox-i 56 · service 22 · ev-product 16 · elektriker-for-x 13 · battery-product 10 · page 8 · post 8 (accordion-only, no image) · team-member 6 · lead-magnet 2. Pages WITHOUT it: 9 static pages, 5 lead magnets, 3 posts.

Funnel position(s): **mid-page objection handling** — verified index ranges per template: ev-product idx 5/16, battery-product 6/17, service 7/18, laddbox-i 8/20, elektriker-i & eljour-i & elinstallation-i 9/19–22, elektriker-for-x 9/17, post 3/7, team-member 2/5. As a fraction of page length it sits at 30–50% depth on 306 of 309 pages.

**The single most important placement fact:** on **161 pages** (eljour-i, laddbox-i, service, battery/ev-product…) FAQ sits **directly BEFORE MainContact** — objections answered, then the ask. On **131 pages** (elektriker-i 56, elinstallation-i 56, elektriker-for-x 13, page 6) FAQ sits **AFTER MainContact** — the form asks before the anxieties are handled. Same block, two opposite funnel logics, split roughly down the middle of the site.

Live pages fetched and verified 2026-08-02: `https://ampy.se/elektriker/taby/`, `https://ampy.se/elservice/byta-elcentral/` (snapshot re-parse), plus geo comparisons (Tyresö, Åkersberga, Huddinge eljour, Nacka laddbox) and the `/eljour/` snapshot.

## Verified structure (live markup, byta-elcentral)

- `<section class="brxe-section faq-">` → container → column (H2 `faq-__top-heading` "Vanliga frågor" + `faq-__accordion-nested`, ~55% width) + column (`faq-__image`, ~45%).
- Each item: `<div class="faq-__title accordion-title-wrapper" role="button" aria-expanded="false" tabindex="0" aria-controls="">` wrapping an `<h3 class="faq-__question" id="">` + chevron icon; content: `<div class="faq-__content" id="" role="region" aria-labelledby="">` → `faq-__answer` paragraph.
- All items collapsed by default (`aria-expanded="false"` on every item, none `"true"`). Answers are in the DOM (accordion ≠ hidden from Google — SEO substance preserved).
- **Exactly 4 questions per page** on every instance inspected (elcentral, eljour, Täby, Tyresö, Åkersberga, Huddinge, Nacka) — schema and on-page match 1:1.
- Article variant (8 posts): accordion only, no image column.
- Mobile (≤780px): columns stack, accordion first, image below (`.faq-__image { max-width: 100% }`, forced `aspect-ratio: 1` crop at ≤1024px); question width 95%; container padding tightens at 480px. Image is `loading="lazy"`, so it costs little on load — but it still appends a full-width decorative square at the end of the block on mobile.

## What it does well

1. **Real answers with real numbers — rare and valuable.** Live copy, byta-elcentral: *"Att installera en ny elcentral kostar vanligtvis mellan 6 000 och 12 000 kronor efter ROT-avdrag"* — this is the price-anchor content Swedish homeowners search for (business context: "byta elcentral pris" is a top paid query). MECLABS: concrete value clarity (v) up, anxiety (a) down.
2. **Behörighet anxiety is genuinely addressed.** *"Endast ett auktoriserat elinstallationsföretag registrerat hos Elsäkerhetsverket får byta elcentral"* (elcentral); Åkersberga even has *"Hur kontrollerar jag att en elfirma i Åkersberga är behörig?"* — exactly the Elsäkerhetsverket-check proof the research says a serious Swedish customer looks for (Cialdini authority, candour-compliant).
3. **Fixed-vs-löpande is covered on some geo pages.** Täby: *"Erbjuder ni fast pris på elarbeten i Täby eller faktureras arbetet löpande per timme?"* with a straight both-answer. This directly hits the Konsumentverket written-quote anxiety.
4. **Programmatic quality is above par.** Geo questions are genuinely localized and varied per ort (Täby ≠ Tyresö ≠ Åkersberga question sets), not copy-paste templating — reduces doorway-page thinness risk.
5. **Candour holds.** Eljour response-time is framed as *"Vår målsättning är att en jourmontör … inom en timme"* + *"får du alltid en realistisk tidsuppskattning"* — a promise with an honest hedge, no fake urgency.
6. **FAQPage schema is present and consistent.** JSON-LD `@graph` carries a `FAQPage` node with all 4 Q&As, matching on-page text exactly (verified eljour + Täby + elcentral). No schema/page divergence, no laundered claims.
7. **Whole title row is the tap target** (role=button on the wrapper, not just the text) — good Fitts's-law behavior on mobile.

## Issues

**FAQ-01 · P1 · desktop+mobile — 131 pages put the FAQ AFTER the main form.**
On elektriker-i (56), elinstallation-i (56), elektriker-for-x (13) + 6 static pages the sequence is `… MainContact → FAQ → ROT-block …`: the strongest conversion asset asks for name/phone/address *before* "Vad kostar det?", "Erbjuder ni fast pris?" and "Är ni behöriga?" are answered. MECLABS heuristic: anxiety-reducing content must precede or adjoin the ask (HealthSpire: the +638% page won because added content answered decision questions *before* the conversion point). The other 161 pages already do it right — this is an inconsistency, not a redesign. Mobile: worse, because the visitor scroll-passes the form with unresolved objections and rarely scrolls back up.

**FAQ-02 · P1 · desktop+mobile — 4 questions per page is too thin, and two of the four documented Swedish-homeowner anxieties are missing.**
Verified coverage across all fetched instances: price ✓, behörighet ✓, fixed-vs-estimate ✓ (some pages), insurance ✓ (eljour). **Missing everywhere inspected: (a) damage responsibility** ("vem ansvarar om något går sönder / blir fel efter installationen?" — ansvarsförsäkring, garanti på arbetet) and **(b) "will they answer later"** (aftercare, vad händer efter jobbet, reklamation). These are two of the five Byggahus/Reddit anxieties named in the business context. Baymard/NN/g: an accordion scales cheaply — 6–8 questions costs no above-fold space. HYPOTES: adding garanti/ansvar + efterservice questions to the FAQ on service + geo templates increases form-submit rate; A/B on the elektriker-i template.

**FAQ-03 · P2 · a11y (both) — ARIA wiring is present but EMPTY.**
Live markup: `aria-controls=""`, `<h3 … id="">`, `aria-labelledby=""` on every item. A screen reader announces an unlabeled button state and an unlabeled region with no programmatic Q↔A association (WCAG 1.3.1 / 4.1.2). The pattern is also a `div role="button"` rather than a native `<button>`, so keyboard operability depends entirely on Bricks JS honoring Enter/Space on tabindex=0. For a 35–65 audience with rising assistive-tech usage this is a real defect, and it is one template fix propagated to 309 pages.

**FAQ-04 · P2 · desktop+mobile — the 45% image column carries near-zero and sometimes negative value.**
Verified: Täby, Tyresö, Åkersberga all reuse `Ampy-elektriker-logotyp.webp`; the Huddinge **eljour** page shows `elektriker-for-brf.webp` (*"En elektriker som inspekterar elsystemet i en bostadsrättsförening inför en renovering"* — a planned-renovation image on an emergency page); the main `/eljour/` page shows a **Tibber Pulse lastbalansering** close-up next to "När ska jag ringa en eljour?". Only elcentral's `elcentral-med-jordfelsbrytare.webp` is on-topic. NN/g: decorative/mismatched imagery is ignored or, worse, dilutes message match. On mobile it stacks below the accordion as a full-width forced-square crop — pure scroll cost. The column real estate could hold a compact anxiety-reducer instead (Elsäkerhetsverket registration proof, "Så lämnar vi pris" mini-card, or the Ring-CTA).

**FAQ-05 · P3 · SEO/AEO — schema is fine but expectation should be calibrated; posts lack the image-column block only, not schema.**
FAQPage rich results have been restricted by Google since 2023 to well-known authoritative government/health sites, so the structured data will not produce SERP accordions for ampy.se; its value today is machine-readability (AI Overviews/AEO parity with on-page text). Keep it — it is correctly implemented and matches visible content (no policy risk) — but do not count on it for CTR. No `Speakable`/aggregation games needed; candour-clean as is.

**FAQ-06 · P3 · mobile — all items collapsed by default.**
NN/g accepts collapsed accordions, but with only 4 questions and the #1 question being the price question, opening the first item by default (aria-expanded="true") exposes the price anchor to scanners without a tap. HYPOTES: first-item-open increases FAQ engagement and downstream form starts; cheap A/B via template toggle.

## Recommended changes (concrete)

1. **Re-sequence (template-level, no content change):** move FAQ to directly above MainContact on elektriker-i, elinstallation-i, elektriker-for-x and the 6 static pages → all 292 form-bearing FAQ pages share the proven `objections → ask` order. This is re-sequencing, not deletion — SEO substance untouched.
2. **Expand question set 4 → 6–7 per template** (copy-pattern direction, not final copy): add (a) *"Vad händer om något skadas eller blir fel — vem ansvarar?"* → answer names ansvarsförsäkring + garanti on the work; (b) *"Vad händer efter installationen?"* → aftercare/reklamation/who to call; keep per-ort localization discipline. Update the JSON-LD mainEntity in the same edit so schema stays 1:1 with the page.
3. **Fix the accordion component once:** generate unique `id` per question/content pair, populate `aria-controls`/`aria-labelledby`, prefer native `<button>` in the title wrapper. One Bricks component edit → 309 pages.
4. **Replace or repurpose the image column:** minimum fix = per-template on-topic image (eljour gets an eljour image); better fix = swap the 45% column for a compact proof card (Elsäkerhetsverket-registrerad + "Skriftlig offert innan arbete" + Ring-knapp), which converts dead decoration into an anxiety-reducer at the exact objection-handling moment. On mobile, if image is kept, hide it below 780px — it adds scroll with no message.
5. **Test first-item-open default** (FAQ-06 hypothesis) on one high-traffic template before rollout.

## Priority score (arithmetic)

Pages affected **309** × funnel position weight **2** (mid-page objection handling; adjoins the form on 161 pages) × expected effect **2** (medium — supportive block, improves the form's conversion rather than converting itself) = **309 × 2 × 2 = 1236**.

Sub-score for the placement fix alone (FAQ-01): 131 pages × 3 (it directly gates the form's context) × 2 = 786 — the single highest-leverage change in this block.

Overall priority: **P1** — the block is content-healthy but structurally mis-sequenced on 42% of its pages, thin on two documented anxieties, and carries a one-fix a11y defect replicated 309 times.
