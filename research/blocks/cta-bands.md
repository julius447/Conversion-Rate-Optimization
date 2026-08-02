# CTA-band family: Mikro_CTA (`mikro_cta`) + Blue CTA (`blue-cta-`)

**Used on:**
- **Mikro_CTA: 173 pages** — elektriker-i 56, eljour-i 56, laddbox-i 56, pillar pages 5 (/elektriker/, /eljour/, /laddbox/, /elinstallation/, /batterilagring/). *(verified from `data/block-map.json`, 326 pages)*
- **Blue CTA: 230 pages** — the same 173 **plus** elinstallation-i 56 and the homepage. Blue CTA is the only CTA band on the homepage body (position 4 of 11 blocks — before Testimonials).
- **Co-occurrence: all 173 Mikro_CTA pages also carry Blue CTA, MainCTA AND FooterSEO** (block-map combo query: `(Mikro ∧ Blue ∧ MainCTA ∧ FooterSEO) = 173 pages`). This family never appears alone; it always stacks on top of the other ask-blocks.

**Funnel position(s):** mid-to-low page. Verified relative positions (block index ÷ page length): Mikro_CTA clusters at 0.3 / 0.5 / 0.7 (56 pages each — one position per geo template); Blue CTA at 0.3 (59), 0.6 (57), 0.7 (112). **The order of the two bands is inconsistent across templates** — on laddbox-i Mikro (#8) comes before Blue (#14); on elektriker-i Mikro (#13) before Blue (#17); on eljour-i Blue (#8) before Mikro (#15). There is no deliberate sequencing doctrine, just template drift.

---

## The total-ask ledger (the real subject of this audit)

Counted on the live, fetched https://ampy.se/elektriker/akersberga/ (elektriker-i template, 22 blocks). Every conversion control in the body, in order:

| # | Block (pos) | Ask(s) | Target |
|---|---|---|---|
| 1 | Hero_2 (2) | "Kostnadsfri rådgivning" + "Ring 010-265 79 79" | **→ /kontakt/** + tel: |
| 2 | Hero_2 .aof form (3) | full lead form "Boka rådgivning" | n8n → /thank-you |
| 3 | MainCTA (5) | "Prata med en elektriker inom 60 sekunder!" → Ring | tel: |
| 4 | MainContact (8–9) | full lead form "Gratis rådgivning" | n8n → /thank-you |
| 5 | **Mikro_CTA (13)** | "Vill du veta mer?" → Kostnadsfri rådgivning + Ring | **→ /kontakt/** + tel: |
| 6 | MapBlock (15) | "Osäker ifall vi finns där du bor?" → Kontakta oss | → /kontakt/ |
| 7 | **Blue CTA (17)** | "Prata med en elektriker!" → Ring (single black button) | tel: |
| 8 | CEBlock (19) | CTA pair ("Kostnadsfri radgivning" + Ring) | → /kontakt/ + tel: |
| 9 | FooterSEO (21) | CTA pair ("Kostnadsfri radgivning" + Ring) | → /kontakt/ + tel: |

**= 11 conversion buttons + 2 embedded lead forms = 13 body asks** (15 counting the header "Gratis rådgivning" CTA and mobile "Ring en expert"). Anchor-verified in the fetched HTML: 5× `href="https://ampy.se/kontakt/"` and 6× `href="tel:+46102657979"` in the body. eljour-i and laddbox-i carry the same 13; elinstallation-i (no Mikro) carries 11.

Six of those asks are *interchangeable generic bands* (MainCTA, Mikro, Blue, CE-pair, FooterSEO-pair, Map-button). Three separate bands say virtually the same sentence: MainCTA **"Prata med en elektriker inom 60 sekunder!"**, Blue CTA **"Prata med en elektriker!"**, Mikro **"Prata med en av våra seniora elektriker i Åkersberga…"**. That is not a repetition *strategy*; it is one idea pasted three times.

**MECLABS heuristic reading (C = 4m + 3v + 2(i−f) − 2a):** repeated asks add no motivation (m) and no new value clarity (v) after the first exposure of each *type*; each redundant band adds a small amount of friction/anxiety (page length between the visitor and the form, one more "they really want me to call" pressure signal). Repetition on a long page is legitimate — the CXL/Unbounce long-page practice and the serial-position effect both support an ask after each major value block — **but only when each repeat carries a distinct job** (new proof, new angle, new funnel stage). Here the distinct jobs collapse: three phone-first bands, four "Kostnadsfri rådgivning" exports, zero bands that point at the two forms already on the page.

---

## What the family does well

- **Blue CTA has the clearest single job on the site:** one message, one black phone button, no competing choice (Hick's law: one option beats two). Its light cyan gradient also visually relieves the dark-navy stacking (Hero_2 card, Testimonials, Visste-du-att are all navy) — it reads as a deliberate "breathing" band. Homepage copy is genuinely good and specific: *"Vi finns här för dig och ditt hem. Oavsett om du planerar att installera batterilagring, sätta upp en laddbox eller en komplett elinstallation i hemmet."* with internal links inside the paragraph (SEO + navigation value).
- **Mikro_CTA is compact and mobile-disciplined:** ACF-driven copy is localized per ort ("…seniora elektriker i Åkersberga…"), the reused `hero_2__primary-button` library button goes full-width below 767px (`width:100% !important`, icon right — good Fitts's-law tap target), container gets `min-height:400px`, centered stack at 480px. It costs little vertically.
- **Both bands respect the candour gate on tactics:** no countdowns, no fake scarcity, no invented reviews inside the bands themselves.
- **Phone-first emphasis matches reality:** GA4 July data shows 2 phone clicks vs 0 recorded form starts from paid traffic — for this audience the phone IS the conversion, so keeping a dedicated phone band is right.

## Issues

**CTA-01 · P1 · desktop+mobile — "Kostnadsfri rådgivning" buttons export the visitor to /kontakt/ while TWO forms sit on the same page.**
Verified in fetched HTML: on /elektriker/akersberga/ the Hero_2 primary button, the Mikro_CTA primary button, the CEBlock and FooterSEO primary buttons all carry `href="https://ampy.se/kontakt/"` — even though the Hero_2 `.aof` form is *directly beside the hero button* and MainContact sits mid-page. Evidence: Baymard — every added step/page-load sheds completers; with ~9–10 s lab LCP the extra pageview is doubly expensive; Jakob's law/message match — a button promising "Kostnadsfri rådgivning" should land on the rådgivning form *now*, not restart the journey on a new URL. Mobile note: on mobile the full-width Mikro button is the most tappable element in view, so the leak is worst exactly where traffic is. HYPOTES (A/B): changing all mid-page "Kostnadsfri rådgivning" buttons from `/kontakt/` to a smooth-scroll anchor on the on-page MainContact form increases form starts on geo pages.

**CTA-02 · P1 · desktop+mobile — three bands, one job: phone-ask redundancy.**
MainCTA (pos 5, ring-only), Blue CTA (pos 8–17, ring-only) and Mikro's secondary ring button all sell the identical action with near-identical copy (quoted above). MECLABS: no added m/v, added a. The GA4 picture (17 deep-scrollers, 2 phone clicks, 0 form starts) is consistent with fatigue-by-repetition rather than lack of opportunity — the page never lacked a phone button; it lacked a *reason at the moment of the ask*. HYPOTES: one consolidated phone band placed immediately after Testimonials (proof-adjacent, Cialdini social proof → ask) outperforms three scattered phone bands on calls per session.

**CTA-03 · P2 · desktop+mobile — Mikro_CTA copy is the weakest ask on the page and carries an unanchored superlative.**
"Vill du veta mer?" is a curiosity ask with no value increment, and "Sveriges snabbast växande elfirma" (live-quoted) is a strong superlative — permitted per owner directive unless demonstrably false, but currently anchored to nothing (no metric, no year, no source). Candour gate: either anchor it (e.g. growth basis + year) or drop it. The band sits *after* the ROT block on elektriker-i/eljour-i, so it also interrupts ROT → Team flow with a generic ask.

**CTA-04 · P2 · desktop+mobile — Blue CTA's underlined H2 fakes a link.**
CSS verified: `.blue-cta-__heading {color:#1e1e1e; … text-decoration: underline}`. NN/g: underlined text on the web signals a hyperlink; a non-clickable underlined heading trains distrust of the page's real links. The single button is also off-token pure black (`background-color:#212121; background-image: repeating-linear-gradient(225deg,#000000,#252525)`) — the only black element in a teal/midnight token system (`ampy-design-system`: teal #00a991 / midnight #090b32). Mobile: button goes `width:100%; height:50px` — fine.

**CTA-05 · P2 — band order and presence are template-inconsistent.**
Mikro before Blue on laddbox-i, after Blue on eljour-i; elinstallation-i has no Mikro at all; homepage's only band (Blue, pos 4 of 11) asks for a phone call *before* any proof block (Testimonials is pos 5). Serial-position logic says the early homepage slot should carry proof or value, not a naked ask.

**CTA-06 · P3 — adjacent-band findings surfaced while counting asks (owned by other audits, logged here):** MainCTA's "**Prata med en elektriker inom 60 sekunder!**" is a service-level promise with no stated basis (candour: anchor or soften to "…svarar snabbt"); MainCTA's "5.0 på Google" has no review count (candour gate: anchored rating required); CEBlock + FooterSEO buttons read "Kostnadsfri **radgivning**" — missing å, live-quoted twice on /elektriker/akersberga/.

## Recommended changes

1. **Retarget, then thin.** First fix CTA-01 everywhere (mid-page "Kostnadsfri rådgivning" → anchor-scroll to on-page MainContact; keep /kontakt/ only in header + pages without a form). This is a pure config change across ~290 pages and de-risks step 2.
2. **Kill Mikro_CTA on the three geo templates that carry both bands** (173 pages). Its two jobs are already done better elsewhere: form-ask → MainContact/anchored buttons; phone-ask → the consolidated phone band. If a mid-page ask is still wanted after ROT, replace it with a *contextual* one-liner tied to the preceding block ("Räkna ut ditt ROT-avdrag med en elektriker — ring …") rather than "Vill du veta mer?". Copy-pattern direction only; final words via ampy-rost.
3. **Merge MainCTA + Blue CTA into ONE phone band** and place it proof-adjacent (immediately after Testimonials on every template). Keep Blue's single-button clarity and light surface; keep MainCTA's trust row *only once anchored* (rating + count + source). Kill the H2 underline; re-token the button (midnight #090b32, not #212121).
4. **Keep FooterSEO's CTA pair as the last-chance close** (bottom-of-page ask is standard and cheap) — but retargeted per (1) and with the "radgivning" typo fixed.
5. **Homepage:** move Blue CTA below Testimonials (swap positions 4↔5) so the first body ask follows the first proof. HYPOTES: proof-then-ask ordering raises homepage call clicks.
6. **Net effect per geo page:** 13 body asks → ~8 (hero pair + hero form + 1 phone band + MainContact + Map + FooterSEO pair), every remaining ask either proof-adjacent or form-adjacent. SEO substance untouched — bands carry no ranking content; ContentBlock/CEBlock text stays where it is.

## Priority score (arithmetic shown)

- **Pages affected:** 230 (Blue CTA reach; the full family incl. MainCTA/FooterSEO interplay touches 290, Mikro subset 173 — scored on the 230 pages where the band-family redundancy exists).
- **Funnel position weight:** mid-page = **2** (these are never the hero/form, but they gate the path to it).
- **Expected effect:** medium = **2** (redundancy removal + /kontakt/ retargeting is a real leak-fix, but the bands are not the primary conversion surface; the forms/hero are).
- **Priority score = 230 × 2 × 2 = 920.**
- **Priority: P1** — not conversion-blocking on its own (→ not P0), but the /kontakt/ export defect (CTA-01) plus three-band phone redundancy (CTA-02) plausibly contribute directly to the observed "0 form starts / 2 phone clicks" paid-traffic leak, and both fixes are low-effort config/copy changes executable in month 1.
