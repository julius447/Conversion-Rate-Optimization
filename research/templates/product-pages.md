# Product pages — ev-product (laddbox) + battery-product (solcellsbatteri)

URLs analyzed (live-fetched 2026-08-02): https://ampy.se/laddboxar/zaptec-go-2/ (781 KB, ~3 020 words) and https://ampy.se/solcellsbatterier/sigenstor/ (813 KB, ~3 285 words).
**Fetch note:** the assigned URL `https://ampy.se/laddbox/zaptec-go-2/` returns **404**; the live canonical path is `/laddboxar/…`. If `/laddbox/<product>/` URLs exist in any ad, sitemap or internal link, they leak traffic to a 404 (see PP-15).

Pages using this template: **26** (16 ev-product + 10 battery-product, from block-map.json). The two categories share an identical block sequence except battery pages insert **Calculator-UI** (the embedded Batterikalkylatorn, `ampy-calc-outer`) directly after ProductHero. Word counts: ev 2 934–3 080 (avg 3 025); battery 3 233–3 425 (avg 3 326). HTML weight avg 780–812 KB **before** images/JS — speed flag consistent with the ~9–10 s lab LCP finding.

---

## Current block sequence (verified against live HTML + block-map)

1. **Header** (global) — mega-menus + "Gratis rådgivning" CTA → links to **/kontakt/** (not an on-page form). Mobile: offcanvas + "Ring en expert" (`tel:+46102657979`) + "5.0".
2. **ProductHero** (`product-hero`, 3-col) —
   - *Left col:* breadcrumbs ("Hem > Zaptec Go 2") → product image → **Teknisk specifikation** accordion (15 rows: Varumärke, Antal faser, IP-klass, Maxladdningseffekt 22 kW, Produktgaranti 5 år …) → **Installationsprocess** accordion ("…din personliga offert baseras på bilder och data du skickar in via vårt formulär… Snabbt, tryggt och utan dolda kostnader.") with **"Läs mer här"** → opens popup 30855.
   - *Middle col:* **H1 "Zaptec Go 2 - Laddbox"** / "Sigenergy - SigenStor" → description paragraph → "Bra att veta:" 2×2 (Finns i lager / Installationstid: 1-3 veckor / Passar alla elbilar / 5 års garanti) → "Färger:" swatches → price block: **"Totalt 5 890 :-" + struck "Ordinarie pris 11 780 :-"** + "Inklusive installation Ja" + "Grön teknik 50%" (battery: "Fr. 69 000 :-" / struck 138 000) → cyan CTA **"Få skräddarsydd offert"** — `href="#"`, opens popup 29890 (battery: 29891).
   - *Right col:* expert card — anonymous team photo (`team-image-1.webp`, **empty alt**) + "Rådfråga vår expert om din laddbox!" / "…om ditt hembatteri!" + `tel:010-265 79 79` (space-formatted tel URI) + unanchored "5.0".
   - *Mobile (verified from DOM order + Bricks stacking):* image → H1/price/CTA block → expert card → a **duplicated** spec+process accordion pair (two full copies in DOM, toggled `display:none`/`block` by breakpoint).
3. **Calculator-UI** (battery pages only) — "Vad tjänar du på ett solcellsbatteri?" two-pane calculator: model/capacity + situation inputs → "Tjänar in på 15 år / Att betala / Årlig avkastning / Payback-tid" → candour states ("Utan solpaneler — Grön Teknik gäller inte…") → inline lead form "Få en exakt offert" (Namn/E-post/Telefon/Postnummer → REST `ampy-calc/v1/lead/<postId>`, verified wired) → "Så har vi räknat" methodology. **Error state contains the wrong phone number** (PP-02). Mobile: single column stack.
4. **Testimonials** — "Vad säger dina grannar om Ampy?" Splide slider, 12 real Google reviews with names + months, close: "5 av 5 Betyg på Google" (no review count on page; JSON-LD says reviewCount 25).
5. **GronTeknik** — "Sänk din {Produkt} kostnad genom 50% Grön Teknik-avdrag" → 3 steps (Projektledning med expert / Installation av elektriker / Vi hanterar ansökan) → "Läs mer om Grön Teknik-avdrag". Contains grammar slip "Vår experter går igenom" (all 26 pages).
6. **ContentBlock** — 3 alternating SEO rows ("Varför välja en Zaptec Go 2 laddare" / "Investering i framtiden" / "En prisbelönt laddbox"; battery: "Maximera din vinst…" / "Sigenergy teknik för smarta stödtjänster" / "SigenStor för en lönsam investering").
7. **FAQ + FAQ-accordion** — 4 H3 questions. On zaptec the price FAQ **contradicts the hero price** (PP-01).
8. **MainContact** — the strongest converter: proof pane ("Från start till mål levererades en service i världsklass." / "5 av 5 · Betyg på Google" / "3 000+ genomförda installationer om året" / 3 steps incl. "Vi ringer dig inom 24 timmar") + form (Förnamn/Efternamn/E-post/Telefonnummer/Adress/Postnummer/Meddelande → "Gratis rådgivning"). Mobile: JS moves proof below form pane (verified in source comment).
9. **ProductGrid** — "Andra laddboxar / Andra solcellsbatterier – självklart med 50 % Grön Teknik-avdrag": cards with badges **SUPERKAMPANJ / NYHET / BÄSTSÄLJARE**, phase/effect chips, "Fr. X kr", "Läs mer".
10. **TeamSection** — "Träffa Ampys Zaptec Go 2 installatörer" → 5 bios (Mio/Magnus/Felix/Edvin/Yousef). Bios are generic site-wide copy — Mio's bio under the *laddbox* headline is about batteries, "SAJ HS3 och Dyness Stack 100" (PP-08). Typo "ocg företag" in Yousef's bio.
11. **VissteDuAtt** — dark band: "Visste du att.. Zaptec Go 2 har vunnit det prestigefyllda priset Red Dot Design Award?" + long SEO body.
12. **CEBlock** — long-form SEO ("Maximera elbilsladdningen med Zaptec Go 2") → CTA pair: "Kostnadsfri radgivning" (typo, missing å) → **/kontakt/** + "Ring 010-265 79 79".
13. **Certificates** — logo wall (Elsäkerhetsverket, Skatteverket, Naturvårdsverket, ID06, Trygg Hansa, Rexel).
14. **FooterSEO** — "Landets bästa Zaptec Go 2 installatör" + same CTA pair ("Kostnadsfri radgivning" typo again → /kontakt/).
15. **Prefooter/Footer** (global).
16. **Popups (2 per page, hidden):** #29890/29891 = offert form ("Boka rådgivning med en laddboxexpert/batteriexpert! Alltid fasta priser och professionell service…" — Namn/E-post/Telefonnummer/Adress/Postnummer **all `required`**, Meddelande optional, hidden `form_type`, no GDPR checkbox — consent implied by submit line). #30855/30795 = **installation-scope popup**: "Så går det till – steg för steg", "Det här ingår i vår standardinstallation" (10 m kabel, max 3 hål, jordfelsbrytare, drifttagning), exclusions (gräv/schakt, uppsäkring, lift, rör), 11/22 kW fuse table, Grön Teknik terms incl. "Vid avslag … faktureras det återstående beloppet med 30 dagars betalningsvillkor", lastbalansering. Opens body-scroll-locked modal on mobile.

---

## Customer-flow walkthrough (35–65 y/o homeowner, mobile-first)

**0–5 s (mobile):** Breadcrumb + product photo fill the first screen. The H1, price and CTA arrive on scroll ~1 screen down. First impression = webshop product card. The visitor searching "zaptec go 2 pris" gets the answer ("Totalt 5 890 :-") quickly — good message match for price queries — but the *installation company* identity is nearly invisible above the fold: no "vi installerar", no proof, an anonymous expert photo further down.

**Scroll / consideration:** The struck "Ordinarie pris 11 780 :-" is exactly 2× the net price on every page checked (5 890→11 780; 69 000→138 000) — a sale-style presentation of a *tax deduction*. A price-savvy 50-year-old recognizes the pattern and it costs trust (MECLABS anxiety `a`). Then the FAQ tells them "Ett vanligt Zaptec Go 2 pris inklusive installation ligger ofta mellan 7 000 och 10 000 kronor efter att Grön Teknik-avdraget… har applicerats" — directly contradicting "Totalt 5 890 :-" three screens earlier. This is *the* Swedish-homeowner fear (final-price surprise, Byggahus/Konsumentverket anchor) triggered by the page itself.

**Decision:** The only primary CTA, "Få skräddarsydd offert", opens a modal demanding 5 required fields including full address before any reciprocity — while the page's honesty asset (what the standard installation includes/excludes, the fuse/effect table, Grön Teknik villkor) is hidden inside a *different* popup behind a low-salience "Läs mer här". On battery pages the calculator does the persuasion work beautifully (value-then-ask, payback math, candour states) — but its error state tells a failed submitter to call **010-123 45 67**, a number that is not Ampy's.

**Late page:** After FAQ the visitor meets MainContact (the best form) — but then ProductGrid invites them to leave to sibling products, TeamSection shows a battery specialist under a laddbox headline, and the last two CTA bands send them off-page to /kontakt/ with a typo ("Kostnadsfri radgivning") even though a form exists on this very page.

---

## What works (keep)

- **Real price transparency, inkl. installation** — rare in Swedish elinstallation, matches candour positioning, wins the "pris" query. JSON-LD Product+Offer (price 5890 SEK) is correctly emitted.
- **Calculator-UI on battery pages** — archetype-correct signature device: value before ask, honest methodology ("Den här kalkylatorn ger en uppskattning — inte ett erbjudande…"), candour edge-cases ("Utan solpaneler — Grön Teknik gäller inte"), wired inline lead form with a concrete promise ("En batteriexpert återkommer inom 24 timmar med en exakt offert").
- **Testimonials early** (right after hero/calc) — 12 real, named, dated Google reviews; correct placement for the trust-seeking visitor (Cialdini social proof; matches the Clarity "About Us" trust-seeking pattern).
- **The installation-scope content itself** (popup 30855) — steg-för-steg, inklusioner/exklusioner, fuse table, Grön Teknik risk disclosure. This is best-in-class candour copy; only its *placement* is wrong.
- **MainContact** near the decision point with anchored-ish proof ("3 000+ genomförda installationer om året") and a 24-h promise.
- **Spec accordions** keep 15-row tables out of the visual flow while staying in DOM for SEO (correct repackaging pattern).
- Uniform template across all 26 pages → every fix below multiplies ×16 or ×26.

---

## Findings

**PP-01 · P0 · Internal price contradiction + "Totalt" overclaim (ev-product; pattern risk on all 26).**
Hero: "Totalt 5 890 :-" + title tag "Från 5890 kr inkl. installation". FAQ on the same page: "ofta mellan 7 000 och 10 000 kronor efter att Grön Teknik-avdraget på 50 % har applicerats." Two prices for the same thing, 3 screens apart. "Totalt" also overpromises: the standard-install exclusions (gräv, uppsäkring, lift, kapsling) live in a popup. Evidence: MECLABS anxiety term; business-context research anchor "final price surprises" = the #1 Swedish homeowner concern; 2026-canon rule "flag INTERNAL contradictions". Mobile: FAQ contradiction is *more* visible on mobile (linear read). Fix: one price truth per page — "Paketpris standardinstallation: 5 890 kr efter Grön Teknik (50 %)" + visible "Vad ingår?" (see PP-06); align or delete the FAQ price range. Priority: 16 pages × 3 (hero) × 3 (high) = **144**.

**PP-02 · P0 · Wrong phone number in calculator error state (all 10 battery pages).**
Live sigenstor markup contains the failure fallback: "Något gick fel. Ring oss på **010-123 45 67** så hjälper vi dig direkt." — a placeholder, not Ampy's 010-265 79 79. A visitor whose offert request fails is told to call a dead number at the exact moment of highest intent. Trust-damaging + lead-losing. Mobile identical. Fix: replace with `tel:+46102657979` and display 010-265 79 79. Priority: 10 × 3 (form) × 3 = **90**.

**PP-03 · P0 · Fake-sale anchoring: struck "Ordinarie pris" = exactly 2× net.**
5 890/11 780 and 69 000/138 000 — the "ordinarie pris" is simply the pre-deduction sum, styled as a sale strike-through. Candour gate ⚑: the reference price never existed as a selling price; a strike-through reads as merchant discount, not skattereduktion (and grön teknik is conditional — the buyer must have tax room, disclosed only in popup 30855: "Vid avslag … faktureras det återstående beloppet"). Framework: candour gate (no manufactured urgency/discount framing); Cialdini contrast used deceptively erodes the authority position. Fix: relabel rows "Pris före Grön Teknik: 11 780 kr / **Efter 50 % Grön Teknik: 5 890 kr**" — same math, honest frame, no strike. Same fix ×26. Priority: 26 × 3 × 2 = **156**.

**PP-04 · P1 · Popup form vs inline — the primary CTA hides the conversion behind a 5-required-field modal.**
"Få skräddarsydd offert" (`href="#"` → popup 29890/29891) requires Namn, E-post, Telefonnummer, Adress, Postnummer before submit ("Få ditt förslag"); no GDPR checkbox (implied-consent line only — inconsistent with Hero_2/MainContact checkbox pattern). Baymard: visible required-field count drives perceived difficulty; the modal severs the visitor from on-page trust context; on mobile it locks body scroll (`body.brx-popup-open{overflow:hidden}`) — mis-taps trap users. Also plausibly invisible to GA4 form_start (matches "0 form starts recorded"). Hero_2's proven minimum is namn+telefon+postnr, contact-first. Fix: primary = inline 3-field mini-form (or the calc form on battery pages); if popup is kept, cut required to 3, add the standard consent checkbox, fire form_start/form_submit events. Priority: 26 × 3 × 3 = **234** (highest of this template).

**PP-05 · P1 · Trust is unanchored and anonymous in the decision zone.**
Buy-column trust = anonymous expert photo (`team-image-1.webp`, empty alt, no name) + bare "5.0" (three unanchored 5.0s per page: header, expert card, footer). JSON-LD asserts `ratingValue 5.0, reviewCount 25` — so the anchor exists but is never shown to humans; candour gate requires "5.0" anchored (rating + count + source) or removed. The real proof (Google-named reviews, 3 000+ installationer, Elsäkerhetsverket logo) all sits below the ask. Cialdini authority/social proof; Clarity trust-seeking evidence. Fix: expert card → real named electrician with role ("Yousef — senior laddboxinstallatör"); rating → "5,0 · 25 recensioner på Google" linked to GBP (owner-confirm the current count first); pull one Elsäkerhetsverket/certifiering line into the hero. Mobile: expert card is the 3rd stacked element — currently wasted prime space. Priority: 26 × 3 × 2 = **156**.

**PP-06 · P1 · The honesty asset is buried in popup 30855.**
"Det här ingår i vår standardinstallation", exclusions, the 11/22 kW huvudsäkring table, and Grön Teknik terms are exactly the content that defuses price anxiety and qualifies leads — hidden behind "Läs mer här" inside the Installationsprocess accordion (a popup inside an accordion). MECLABS HealthSpire: longer pages win when added content answers real decision questions; NN/g: critical purchase information must not require discovery. Fix: promote to an on-page "Vad ingår i priset?" block directly under the price (accordion is fine — content stays in DOM), keep the popup as secondary. Mobile: popup is scroll-locked and long — worst on small screens. Priority: 26 × 3 × 2 = **156**.

**PP-07 · P2 · Duplicated hero accordions + page weight.**
Both spec and process accordions are rendered twice in DOM (desktop copy `display:none;visibility:collapse` vs mobile copy) — ~15 rows of duplicated text ×2 per page; HTML alone averages 780–812 KB with 589 media-query blocks and multi-KB data-URI scripts; consistent with the 9–10 s lab-LCP flag. Fix: single accordion instance repositioned with CSS order; audit inline CSS/JS payload. Priority: 26 × 1 × 2 = **52**.

**PP-08 · P2 · TeamSection headline/bio mismatch.**
"Träffa Ampys Zaptec Go 2 installatörer" introduces Mio, whose bio is entirely battery-focused ("…rådgivning kring SAJ HS3 och Dyness Stack 100…"). Same 5 generic bios on all 26 pages under a product-specific promise; typo "ocg företag". NN/g credibility research: small mismatches disproportionately damage trust; E-E-A-T dilution. Fix: per-category bio ordering (laddbox pages lead with Yousef/Edvin; battery with Mio/Felix) — data exists, only sequencing is wrong. Priority: 26 × 1 × 2 = **52**.

**PP-09 · P2 · CTA proliferation + off-page detours + typo.**
One zaptec page carries ≥7 conversion asks across 4 different mechanisms (header→/kontakt, popup form, expert tel, MainContact form, calc form on battery, CE-block pair→/kontakt, FooterSEO pair→/kontakt). CE-block and FooterSEO both send "Kostnadsfri radgivning" (missing å — visible typo, twice per page ×26) to /kontakt/ although MainContact sits on-page. Hick's law + friction: every extra route dilutes; the off-page hop adds a page load (~9 s risk) before any form. Fix: late-page CTAs anchor-scroll to on-page MainContact (`#kontakt`); fix "rådgivning"; make phone the consistent secondary. Priority: 26 × 1 × 2 = **52**.

**PP-10 · P2 · Three competing lead promises with different SLAs.**
Popup: "Alltid fasta priser… Få ditt förslag" (no time promise). Calc: "En batteriexpert återkommer inom 24 timmar med en exakt offert." MainContact: "Vi ringer dig inom 24 timmar." Thank-you page: "inom kort". Message-match discipline applies to internal promises too — pick one ("Vi ringer inom 24 timmar") everywhere. Also "Alltid fasta priser" must survive the candour gate vs the popup-30855 caveat "Eventuella tillägg … hanteras direkt på plats … enligt gällande prislista" — "fasta priser" + open-ended tillägg is the exact combination Konsumentverket-minded buyers distrust. Priority: 26 × 2 × 1 = **52**.

**PP-11 · P2 · "SUPERKAMPANJ" badges (ProductGrid + hero on some products).**
Candour ⚑: a kampanj implies a time-bound offer; if no actual campaign with defined terms exists, this is manufactured urgency (banned class). Owner confirm or rename ("Populär", "Bästsäljare" where true by sales data). Also casing inconsistency "Fr. 4 990 Kr". Priority: 26 × 2 × 1 = **52**.

**PP-12 · P3 · tel: URI inconsistency.** Expert card uses `tel:010-265 79 79` (spaces, no country code) while header/footer use `tel:+46102657979`. Standardize on E.164. 26 × 3 × 1 = 78 arithmetic but trivial effort — bundle with PP-02.

**PP-13 · P3 · Grammar/typo sweep.** "Vår experter går igenom" (GronTeknik, ×26), "Kostnadsfri radgivning" (×2 per page), "ocg företag" (TeamSection). Bundle into one copy pass.

**PP-14 · P2 · EV pages have no calculator while battery pages do.**
Laddboxkalkylatorn exists as an orphan page but is absent from the 16 ev-product pages — the one place a "vad kostar laddning hemma"-minded visitor is already standing. Battery pages prove the pattern (Calculator-UI slot after ProductHero). Effort M (embed exists). Priority: 16 × 2 × 2 = **64**.

**PP-15 · P1 (verify scope) · /laddbox/ vs /laddboxar/ 404.**
`https://ampy.se/laddbox/zaptec-go-2/` = 404 with no redirect. HYPOTES: legacy or externally-shared /laddbox/ product URLs exist (this audit's own brief contained one). Add 301 rules `/laddbox/(.*) → /laddboxar/$1` — zero-risk insurance for paid/organic equity.

---

## Strategic verdict: is a price-anchored product page the right frame?

**Keep the price anchor; drop the e-commerce costume.** The price ("inkl. installation, efter Grön Teknik") is Ampy's differentiator and wins the "pris"-shaped queries these pages rank for — removing it would be a mistake. But Ampy sells **installation + rådgivning**, not boxes: there is no checkout, so every webshop signal (struck ordinarie pris, SUPERKAMPANJ badges, color swatches above the ask, "Finns i lager") builds a mental model the CTA then breaks — the visitor primed to *buy* is instead asked for their address in a modal. The correct frame is an **installation-package page**: price = "paketpris standardinstallation efter Grön Teknik", flanked by *vad ingår/ingår inte* (the popup-30855 content, surfaced), a named expert, anchored rating, and ONE ask — "vi ringer dig inom 24 timmar". Product specs remain as supporting evidence in accordions. This resolves PP-01/03/04/05/06 with one reframe and is fully consistent with the candour moat.

---

## Recommended sequence (wireframe — both categories; Δ = change)

| # | Block | Why here | New/existing/modified |
|---|-------|----------|------------------------|
| 1 | Header | unchanged; CTA → anchor to on-page form on product pages | modified (link target) |
| 2 | **ProductHero — installation-package version** | H1 + image + honest price stack ("Pris före Grön Teknik / Efter 50 %: X kr, standardinstallation") + **inline 3-field mini-form** (namn/telefon/postnr, "Vi ringer inom 24 h") as primary CTA + named expert w/ phone + anchored "5,0 · N recensioner på Google" | modified (PP-01/03/04/05) |
| 3 | **"Vad ingår i priset?"** | popup-30855 content on-page as accordion: ingår/ingår inte, 11/22 kW-tabell, Grön Teknik-villkor. Defuses price anxiety at the moment it arises (MECLABS HealthSpire) | new placement of existing content (PP-06) |
| 4 | Calculator-UI | battery: keep exactly here; **ev: embed Laddboxkalkylatorn** (PP-14). Fix error-state number (PP-02) | modified / new-on-ev |
| 5 | Testimonials | social proof immediately after the value/price zone — current position is correct | existing |
| 6 | GronTeknik 3-step | process clarity + "vi hanterar ansökan" reassurance; fix "Vår→Våra" | existing (copy fix) |
| 7 | ContentBlock (SEO rows) | SEO substance preserved, mid-page | existing |
| 8 | VissteDuAtt (award/fact band) | light-register brand moment breaks the SEO stretch; move UP from #11 so it supports consideration | moved |
| 9 | FAQ | align price answer with hero (PP-01); keep in DOM as accordion | modified |
| 10 | **MainContact** | the close, right after objections are answered; all late CTAs anchor here | existing (anchor target) |
| 11 | TeamSection | category-matched bios (PP-08) — E-E-A-T after the ask supports "who comes to my house" | modified |
| 12 | ProductGrid ("Andra …") | AFTER the close — sideways exit offered only once the primary ask has been made; honest badges (PP-11) | moved/modified |
| 13 | CEBlock + Certificates | long-form SEO + authority wall for scrollers/crawlers | existing |
| 14 | FooterSEO | CTA pair → anchor to #10 + tel; fix typo | modified (PP-09) |
| 15 | Prefooter/Footer | unchanged | existing |
| — | Popup offert form | demoted to secondary (kept for ProductGrid quick-offert if desired): 3 required fields + consent checkbox + form events | modified (PP-04) |

Net: nothing deleted; two blocks moved; the modal's job is taken over by an inline form; hidden candour content surfaced.

---

## Test hypotheses (top 3, A/B)

1. **HYPOTES — inline vs popup ask:** Replacing the "Få skräddarsydd offert" popup (5 required fields) with an inline 3-field mini-form (namn/telefon/postnr + "Vi ringer inom 24 timmar") in the ProductHero increases form starts and completed product-page leads. Measure: form_start, form_submit, /thank-you pageviews per session, on all 26 pages (popup arm = control). Rationale: Baymard field-count, modal context loss, mobile scroll-lock.
2. **HYPOTES — honest price frame:** "Pris före Grön Teknik / Efter 50 %" two-row presentation + visible "Vad ingår i priset?" accordion outperforms the struck "Ordinarie pris" + hidden popup on qualified leads (form submits + phone clicks) without hurting engagement, because it removes the sale-pattern distrust and answers the final-price-surprise objection in place. Guardrail metric: scroll-depth past price block.
3. **HYPOTES — anchored, named trust in the decision zone:** Expert card with a real named installer + "5,0 · 25 recensioner på Google" (owner-confirmed count, linked) lifts combined conversions vs the anonymous photo + bare "5.0". Measure: tel: clicks from the card + hero-form submits. Rationale: Cialdini authority; candour gate anchoring; Clarity trust-seeking evidence.

*(Sequencing pre-req for all three: instrument form_start/form_submit on popup, calc and MainContact forms first — current GA4 shows 0 form starts, so today no arm can be measured.)*
