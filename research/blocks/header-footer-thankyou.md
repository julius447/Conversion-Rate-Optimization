# Header (global) + Footer/Prefooter (global) + Thank-you page (`ampy-tack`)

**Used on (verified against `data/block-map.json`, 326 pages):**

| Block | Pages | Position | Categories |
|---|---|---|---|
| Header | **325 / 326** | Always index 0 (first block on every page) | All: elektriker-i 56, elinstallation-i 56, eljour-i 56, laddbox-i 56, service 22, ev-product 16, page 16, elektriker-for-x 13, post 11, battery-product 10, lead-magnet 7, team-member 6 |
| Prefooter + Footer | **325 / 326** | Always the last block (from-end distance 0 on all 325) | Same spread |
| ThankYou | **1 page** (`/thank-you/`) | Standalone — the ONLY page on the site with **no Header and no Prefooter** (word_count 32) | page |

**Funnel position(s):** Header = permanent above-the-fold chrome on every page (weight 3). Footer/Prefooter = page-bottom (weight 1). Thank-you = **post-conversion endpoint — 100 % of form conversions pass through it and the GA4/Ads conversion fires on its pageview** (weight 3 by sanctity, despite N=1 page).

**Live evidence fetched 2026-08-02:** `https://ampy.se/` (full header + footer text and markup, snapshot `data/pages/home.html`, header markup alone = 148 KB / 68 anchor tags) and `https://ampy.se/thank-you/` (full visible text: *"Din förfrågan har blivit mottagen! En av våra rådgivare kommer att kontakta dig inom kort. 5 av 5 · Betyg på Google — Utforska våra eltjänster — Till startsidan"* — that is the entire page).

---

## What these blocks do well

**Header**
- Clean IA taxonomy: three mega-menus (**Tjänster / Produkter / Lösningar**) with real user-language groupings (Elinstallationer, Belysning, Kök & Badrum, Populära) — grouped mega-menus are the NN/g-endorsed pattern for large service catalogs; the grouping itself is not the problem.
- The "Populära" column surfaces the four money verticals with benefit microcopy: *"Eljour — Akut hjälp när det inte kan vänta"*, *"Laddbox — Installation av hemmaladdning"*. Good scent.
- Persistent teal CTA with pulsing dot ("Gratis rådgivning") gives every page a standing next step.
- Skip-links (*"Hoppa till huvudinnehåll"*, *"Hoppa till sidfot"*) and `aria-expanded` on submenu toggles: baseline a11y is present.

**Footer/Prefooter**
- Full Swedish NAP in the footer: *"Västbergavägen 25, 126 30 Hägersten · [email protected] · 010-265 79 79"* + `tel:` link — the footer is currently the ONLY place on a desktop page (outside hero blocks) with a tappable phone number.
- Prefooter "Populära kategorier" (5 columns, 15 links) is a sane crawl/discovery layer; policies (Tillgänglighetsredogörelse, Cookie policy, Integritetspolicy) all present.
- Kundtjänst column links ROT avdrag 2026 + Grön Teknik 2026 — the two questions Swedish homeowners actually have.

**Thank-you**
- Correctly isolated: no header/footer means no navigation chrome competing at the measurement moment, and Consent Mode (default denied → update) is properly implemented around GTM-568WF66G.
- Copy confirms receipt instantly in du-tilltal; the mint check animation gives closure feedback (NN/g: visibility of system status).

---

## Issues

### HEADER

**HDR-01 — The phone conversion is invisible on desktop and buried behind the hamburger on mobile. Severity P0.**
Verified in markup: the desktop header bar contains logo + 3 mega-menus + one CTA (`class="ampy-cta" href="https://ampy.se/kontakt/"` — "Gratis rådgivning"). There is **no `tel:` link and no visible phone number anywhere in the desktop header**. The only header `tel:` link ("Ring en expert", `tel:+46102657979`) sits inside `brxe-offcanvas` — i.e., mobile users must tap the hamburger, then find it below the full accordion nav. Business context: only two conversion paths exist, and in the July paid-traffic investigation the **only recorded conversions were 2 phone clicks** (0 form starts). Evidence: Fitts's law (target availability/steps), Unbounce home-services benchmark (urgent/repair intent converts via call), Jakob's law (Swedish trade-service sites show the number top-right; visitors expect it there). *Mobile note:* on the Eljour template (56 geo pages + pillar — emergency intent by definition) an emergency visitor currently has zero one-tap call affordance until they either open the menu or scroll to a CTA block.

**HDR-02 — Header CTA destination forces a page reload away from a live form; label is inconsistent across the journey. Severity P1.**
"Gratis rådgivning" → `/kontakt/` as a full navigation — including on the 260 pages that already carry the Hero_2 `.aof` form one scroll away, and on pages with Main contact at the bottom (295 pages). The user is transported off a page that could convert them to a generic contact page (extra step = MECLABS friction term). Label drift across one journey: header **"Gratis rådgivning"** → hero CTA **"Kostnadsfri rådgivning"** → Hero_2 submit **"Boka rådgivning"** → Main-contact submit **"Gratis rådgivning"**. Four labels for the same act (NN/g consistency heuristic; message match). *Mobile note:* same destination in offcanvas; plus the offcanvas CTA competes with "Ring en expert" inside the same panel.

**HDR-03 — Mega-menu overload + duplicate/mismatched targets. Severity P2.**
34 unique destinations in the header, rendered twice (desktop nav + offcanvas duplicate) = 68 anchors and 148 KB of header markup on every page (relevant given the 9–10 s lab LCP flag). Tjänster alone exposes 22 choices (18 sub-services + 4 Populära) — Hick's law. Concrete defects verified in markup: **"Privatperson" links to `/elektriker/` — the identical target as the "Elektriker" Populära card** (two labels, one page: scent confusion); **"Elcentralkalkylator" links to `/elcentral-kollen/`** — the tool's actual name/H1 is "Elcentral-kollen" (link label ≠ landing page, message-match break); the four "Guider & verktyg" calculator links route sitewide authority and clicks into lead-magnet **orphan pages** (known problem: no hero/process/contact wrap, Energikalkylatorn lead-webhook still a stub) — the nav funnels visitors into the leakiest pages on the site. *Mobile note:* the offcanvas accordion repeats all 34, so the mobile first-interaction is a wall of 30+ rows.

**HDR-04 — Candour: offcanvas "5.0" rating chip links to Google Maps but shows no review count. Severity P2.**
Partially anchored (it does link to the GBP source) but "5.0" with no count fails the house rule "rating + count + source". *Mobile note:* this chip is mobile-only (offcanvas), so the weakest form of the claim is the one mobile users see.

**HDR-05 — Mobile toggle labelled only "Öppna". Severity P3.**
`aria-label="Öppna"` on the hamburger (open what?); close button `aria-label="close"` (English). Minor a11y/localization polish. *Mobile note:* screen-reader users on the primary device get the vaguest labels.

### FOOTER / PREFOOTER

**FTR-01 — Prefooter column headings are dead text; pillar pages missing from their own columns. Severity P2.**
Verified: `<h3 class="prefooter__heading">Elinstallation</h3>` etc. are plain headings, not links. The "Elinstallation" column lists Eljour/Elektriker/Belysning but never links `/elservice/`; "Laddboxar" lists 3 products but not `/laddboxar/`; "Batterilagring" 3 products but not `/batterilagring/` or `/solcellsbatterier/`. Users (and crawlers) get leaf pages without the category hubs — inverted internal-linking hierarchy at the site-wide layer. "Områden" exposes 3 of the 224 geo pages (Stockholm, Sollentuna, Haninge) with no route to the rest (the Maps block partially covers this mid-page, but the footer layer is where Jakob's law says users look for it). *Mobile note:* five stacked columns = long scroll, all before the actual footer.

**FTR-02 — Footer trust layer is thinner than Swedish convention demands. Severity P2.**
Footer bar reads *"© 2026 Ampy Nordic AB - All Rights Reserved"* — **no org.nr, no F-skatt mention, no Elsäkerhetsverket self-service check link**. Business context names the Elsäkerhetsverket registration check + written-quote advice as "the proof a serious Swedish customer looks for" (Byggahus/Reddit evidence; Cialdini authority). The Certificates block carries the logo mid-page on 290 pages, but the footer — the place a due-diligence visitor scrolls to (the Clarity recording that went Contact → About Us is exactly this trust-seeking persona) — asserts nothing verifiable. The standalone "5.0" next to the footer logo is unanchored (no count, no link — worse than the header chip). *Mobile note:* footer is the last thing a scroll-through mobile reader sees; it currently ends on policies, not proof.

**FTR-03 — Social row includes `reddit.com/r/Hantverkare` — an external community Ampy does not own. Severity P3.**
Verified href in footer socials (alongside LinkedIn/Instagram/Facebook/TikTok). Sends bottom-of-page visitors to an unmoderated third-party forum where price-surprise horror stories are the genre. Low traffic, but pure downside. Also "Support" as the label for `/kontakt/` (label ≠ destination page name "Kontakt").

**FTR-04 — Footer/prefooter mass sits directly under Footer-SEO + Main-contact on most templates. Severity P3 (coordination note).**
On the 290 pages ending …MainContact → (blocks) → FooterSEO → Prefooter, the bottom of the page stacks a CTA block, an SEO block, 15 prefooter links and ~30 footer links. The conversion-relevant asset (Main contact) is fenced off from page-end by two link fields. Not a footer defect per se, but any footer slimming increases Main-contact's end-of-page capture (serial-position effect).

### THANK-YOU PAGE

**TY-01 — Zero expectation-setting at the moment of maximum anxiety. Severity P0.**
Full live copy: *"Din förfrågan har blivit mottagen! En av våra rådgivare kommer att kontakta dig inom kort."* No **WHO** (a named electrician/team photo — the page markup contains **zero `<img>` elements**), no **WHEN** (the Main-contact form the user just submitted promised *"Vi ringer dig inom 24 timmar"* — the thank-you page immediately downgrades that commitment to "inom kort": a message-match break at the exact moment reassurance is cheapest), no **WHICH number** will call. Swedish homeowners screen unknown numbers; the #1 documented worry is "will they answer later". A missed callback is a lost lead that was already paid for. There is **no "spara numret 010-265 79 79" instruction and no `tel:` link anywhere on the page** (verified: only 3 anchors exist — skip-link, `/elservice`, `/`). Evidence: MECLABS anxiety term (−2a) applies post-submit too; NN/g confirmation-page guidance (state what happens next, when, by whom); Baymard post-order UX. *Mobile note:* on mobile the save-the-number action is a native one-tap (contact card / long-press) — the page currently offers nothing to tap.

**TY-02 — Dead end: the site's highest-motivation pageview is discarded. Severity P1.**
Two generic links ("Utforska våra eltjänster" → `/elservice`, "Till startsidan"). A just-converted lead is the best audience for: preparing the call (foto på elcentralen, questions to ask), the relevant calculator, team page ("vem ringer dig"), or a second-vertical teaser. Nothing exploits it. (Positive: at least the primary link follows the service>laddbox>battery priority.) *Mobile note:* the full-viewport aurora card means even those two links are all there is — no scroll content at all (word_count 32).

**TY-03 — Conversion-pixel sanctity: the page is indexable and openly reachable. Severity P0 (measurement).**
Verified in `thank-you.html`: `<meta name="robots" content="index, follow, max-snippet:-1, …">` and `<title>Thank you</title>`, with GTM-568WF66G firing on pageview (gtag consent-mode wrapper confirmed; 11 gtag refs, 7 fbq refs). Consequences: (a) Google can index and serve `/thank-you/` — any organic/direct/refreshed visit fires a GA4/Ads conversion with no form behind it; (b) bookmark/back-button revisits double-count; (c) the entire CRO program's dependent variable is corruptible. With current volumes (0 recorded form leads) even single phantom conversions distort CPL math. This is the block whose integrity every other audit file depends on.

**TY-04 — Candour + language details. Severity P2.**
*"5 av 5 · Betyg på Google"* — no review count, and on this page not even a link to the GBP source (the homepage badge at least links out). Unanchored rating on the conversion page = candour-gate fail. `<title>Thank you</title>` and the `/thank-you/` slug are English on an otherwise all-Swedish site (voice/system-image inconsistency; also the title is what shows in the browser tab while the user waits).

---

## Recommended changes (concrete; copy-pattern direction, not final copy)

**Header (one intervention, sitewide):**
1. Put the phone number in the header bar on all breakpoints: desktop = visible `tel:` link with number ("Ring 010-265 79 79"); mobile = persistent phone icon button OUTSIDE the hamburger (right of logo, left of toggle). On the 57 eljour pages, consider the phone as the primary header CTA.
2. Unify the CTA verb sitewide (pick ONE of Gratis/Kostnadsfri rådgivning and use it in header, heroes, submits). Retarget the header CTA: on pages with an on-page form (Hero_2/Main contact), smooth-scroll to the form (`#`-anchor) instead of navigating to `/kontakt/`; keep `/kontakt/` only where no form exists.
3. Mega-menu hygiene: give "Privatperson" its own destination or remove it; rename "Elcentralkalkylator" ↔ "Elcentral-kollen" so label = landing H1; gate the "Guider & verktyg" links until the lead-magnet pages get their hero/process/contact wrap (or route them last, not as a promoted column). Anchor the offcanvas 5.0 chip: "5,0 · N omdömen på Google".
4. Trim the duplicated offcanvas DOM if Bricks allows (one nav source, two renderings) — supports the LCP workstream.

**Footer/Prefooter:**
5. Link the prefooter column headings to their pillar pages (`/elservice/`, `/laddboxar/`, `/solcellsbatterier/` or `/batterilagring/`); add "Alla områden →" to Områden.
6. Add a one-line legal-trust row above the © bar: org.nr, F-skatt, "Registrerad hos Elsäkerhetsverket — kontrollera oss" linking to Elsäkerhetsverket's self-service check. Anchor or remove the footer "5.0". (Candour: every element verifiable.)
7. Drop the Reddit social link; rename "Support" → "Kontakt".

**Thank-you (protect the pixel, then use the moment):**
8. Expectation block, in order: WHO (photo + first name of a real rådgivare/electrician — team assets exist in `om-oss-*` pages), WHEN (repeat the exact promise made in the form: "inom 24 timmar" — never vaguer than the form), WHICH number ("Vi ringer från 010-265 79 79 — spara numret så du känner igen oss" with `tel:`/vCard tap target on mobile).
9. Measurement sanctity: set `noindex` on `/thank-you/`; prefer firing the Ads/GA4 conversion on a submit-confirmed signal (form-success event or a one-time token/param checked by GTM) rather than a bare pageview, so direct hits/refreshes don't convert. Retitle to Swedish ("Tack — vi hör av oss") once retagging is verified (approved-rendering rule: pixel logic changes are owner-gated and must be regression-tested against the live GTM container before any redirect/URL change).
10. Post-conversion content (below the fold, never displacing the confirmation): "Så förbereder du samtalet" micro-list + one relevant calculator + link to the team page. Anchor the rating ("5,0 av 5 · N omdömen · länk till Google") or remove it.

**HYPOTES (top test statements):**
- HYPOTES: Adding a persistent header `tel:` button outside the mobile hamburger increases phone-click conversions per session vs. the current offcanvas-only placement (A/B by template group; primary metric tel-click rate, guardrail form-submit rate).
- HYPOTES: Retargeting the header CTA to the on-page form anchor (vs. `/kontakt/` navigation) increases form starts on Hero_2 pages (MECLABS friction reduction).
- HYPOTES: A thank-you page stating who calls, when, and from which number ("spara numret") increases callback answer rate / booked consultations per lead vs. the current generic confirmation (measured in CRM outcome, not on-page).

---

## Priority score (arithmetic shown, doctrine formula: pages × funnel-weight × effect)

| Item | Pages affected | Funnel weight | Expected effect | Score | Priority |
|---|---|---|---|---|---|
| HDR-01 phone in header (desktop + un-buried mobile) | 325 | 3 (above-fold chrome, primary conversion path) | 3 (high — the only recorded conversions were phone clicks) | **325 × 3 × 3 = 2 925** | **P0** |
| HDR-02 CTA label/destination unification | 325 | 3 | 2 (med) | 325 × 3 × 2 = 1 950 | P1 |
| TY-03 pixel sanctity (noindex + gated firing) | 1 (but gates 100 % of form-conversion measurement for all 326 pages' optimization) | 3 (conversion endpoint) | 3 (high — protects the program's dependent variable) | 1 × 3 × 3 = 9 nominal; **treated as P0 by sanctity override** | **P0** |
| TY-01/TY-02 expectation-setting + next steps | 1 (100 % of form leads) | 3 | 3 (lead-to-contact rate) | 1 × 3 × 3 = 9 nominal → P1 by lead-value | P1 |
| HDR-03 mega-menu hygiene | 325 | 3 | 1 (low-med) | 325 × 3 × 1 = 975 | P2 |
| FTR-01 prefooter pillar links | 325 | 1 | 2 | 325 × 1 × 2 = 650 | P2 |
| FTR-02 footer legal-trust row + rating anchor | 325 | 1 | 2 | 325 × 1 × 2 = 650 | P2 |
| HDR-04/05, FTR-03/04, TY-04 polish | 325 / 1 | 1–3 | 1 | ≤ 325 | P3 |

**Block-group verdict: P0.** Dominant score 2 925 (HDR-01). The thank-you fixes ride along in the same sprint because TY-03 protects the measurement that every other finding in this program will be judged by.
