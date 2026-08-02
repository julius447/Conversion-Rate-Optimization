# Template deep-dive: Service pages (/elservice/*)

URLs analyzed (fetched live 2026-08-02): https://ampy.se/elservice/elcentral/ · https://ampy.se/elservice/vitvaror/ · https://ampy.se/elservice/felsokning-av-el/ — plus raw-HTML inspection of elcentral (822 KB download) and block-map cross-check of all 22.
**Pages using this template: 22** (block-map.json: every /elservice/* child page — armatur, badrum, badrumsrenovering, belysning, elbesiktning, elcentral, elrenovering, felsokning-av-el, glodlampa, golvvarme, inomhusbelysning, jordfelsbrytare, kok, koksrenovering, lastbalansering, luftvarmepump, smarta-hem, spotlights, strombrytare, ugn-spis, utomhusbelysning, vitvaror — carries the **identical** block sequence). The /elservice/ pillar itself uses a different thin sequence (AlternativHero > MainCTA > VarProcess > MainContact > FAQ) and is out of scope here but flagged for the pillar audit.
**Why this template matters most:** it receives the Google Ads service traffic ("byta elcentral pris", "installera diskmaskin", "elfel i huset") — the commercial-priority #1 vertical — and it is where the July diagnosis localized the leak: 33 clicks, ~32 arrived sessions, 17 deep scrolls, 2 phone clicks, **0 recorded form starts**, and the 1-second paid bounce recorded on Vitvaror.

---

## Current block sequence (verified, identical on all 22)

| # | Block | Desktop behavior | Mobile behavior |
|---|---|---|---|
| 1 | Header | Mega-menus + "Gratis rådgivning" teal CTA (pulsing dot) + tel link | Offcanvas accordion + "Ring en expert" + 5.0 row |
| 2 | **Hero_2** | Left: breadcrumbs → **H1 = small eyebrow** ("Byta elcentral") → **H2 = big gradient headline** ("Ny elcentral installerad med 30% ROT-avdrag") → paragraph → TWO gradient CTAs ("Kostnadsfri rådgivning" + "Ring 010-265 79 79") → unanchored "5.0" ★★★★★ GBP link. Right: `.aof` form card | Columns stack: full text column + CTAs first, form card a viewport below; ~9–10 s lab LCP means late paint |
| 3 | **Hero_2-aof-form** | **NOT in server HTML.** `#ampy-form-root.aof` is an empty div; the entire card ("Få kostnadsfri rådgivning!", kundtyp toggle, ärende-select, fields, GDPR, submit → Supabase `hero-lead` → /thank-you) is injected by a **deferred `data:` URI script** | Same — form invisible until JS executes; on slow mobile the navy card area renders empty |
| 4 | Testimonials | "Vad säger dina grannar om Ampy?" Splide slider, **same 12 reviews on every page**, "5 av 5 Betyg på Google" badge (no review count) | Swipe slider, tall cards; pushes content ~2 viewports down |
| 5 | ContentBlock | 3 alternating image/text SEO rows (e.g. "Varför du bör uppgradera till en ny elcentral") | Stacked image-then-text, long scroll |
| 6 | VarProcess | "Så funkar det" 4 numbered steps | 4 stacked icon boxes |
| 7 | MainCTA | "Prata med en elektriker inom 60 sekunder!" + **Ring-only** CTA + "5.0 på Google" | Centered stack, phone button |
| 8–9 | FAQ + accordion | "Vanliga frågor" — 4 H3 questions incl. the **price answer** on elcentral | Accordion 100% width |
| 10–11 | MainContact + card | Left proof pane (quote, "5 av 5 · Betyg på Google", "3 000+ genomförda installationer om året", 3 steps) + right 8-field form → n8n → /thank-you | Proof pane stacks above form; form ~1 viewport tall |
| 12 | MapBlock | "Vi finns där du finns" + 20 ort buttons + Kontakta oss sub-card; then a related-services exit grid ("Är byte av elcentral inte det du letar efter?" — 6 cards + "Ladda fler tjänster") | Dot-map variant, button grid wraps |
| 13 | ROT-block | "Sänk kostnaden … genom 30% rot-avdrag" 3 items + "Läs mer om ROT-avdrag" | Stacked cards |
| 14 | VissteDuAtt | Dark navy editorial card, ~250-word SEO prose, swinging bulb | Stacked, long dark block |
| 15 | CEBlock | Long-form SEO (H2 + 2 sub-heads) + CTA pair ("Kostnadsfri radgivning" — missing å) + 9:16 image | Tall image + prose |
| 16 | Certificates | Logo wall (Elsäkerhetsverket, Skatteverket, Naturvårdsverket, ID06, Trygg Hansa, Rexel) | 6 logo cards stacked/wrapped |
| 17 | FooterSEO | H2 + text + CTA pair + masked image | Stacked |
| 18 | Prefooter/Footer | Populära kategorier + navy footer + another "5.0" | Link columns collapse |

**CTA inventory per page (verified in elcentral HTML):** 6 `tel:` links, 4 "Kostnadsfri rådgivning" instances, 2 "Gratis rådgivning" instances + 2 forms = **~12 competing ask-points** on one page.

---

## Customer-flow walkthrough (35–65 y/o homeowner, mobile, from a Google ad)

**0–5 s ("byta elcentral pris" click):** Page paints slowly (~9–10 s lab LCP; hero has SVG waves, gradients, webp layers). First screen: breadcrumbs, a small green "Byta elcentral", a big headline about ROT-avdrag, two same-weight gradient buttons, a bare "5.0". **No price. No form visible** (it is a viewport down on mobile — and does not exist at all until the deferred script runs). The searcher asked a price question; the first screen answers a benefit question. On Vitvaror the mismatch is worse: query "installera diskmaskin" lands on the category headline "Säker vitvaruinstallation med 30% ROT-avdrag" — diskmaskin appears first in body copy. This is the most plausible mechanical story behind the recorded 1-second Vitvaror bounce: slow paint + no visible answer to the query + no visible form.

**Scroll 1–3:** The visitor hits 12 generic review cards (only 1 of 12 mentions elcentral; none mention vitvaror), then three long SEO rows. The 17 deep-scrollers in GA4 are consistent with this: people scroll *looking for the price and the proof*, i.e. the MECLABS HealthSpire pattern in reverse — the content that answers real decision questions (pris, vem får göra jobbet, ROT, process, Elsäkerhetsverket auth) exists but sits at positions 8–16.

**Decision point:** The Swedish homeowner's checklist (Byggahus/Konsumentverket pattern: fixed vs estimated price, written offert, registered installer, "will they answer later") is finally satisfied at FAQ + MainContact — 8+ blocks down. The MainContact left pane is the single best conversion surface on the page ("Vi ringer dig inom 24 timmar", "3 000+ genomförda installationer om året", the 3-step promise) but it is the **second** form the visitor meets, below the fold of a very long page. The two recorded phone clicks (vs 0 form starts) fit this: calling is the only ask that is *always visible* (header) and *always works* (no JS dependency).

**After the form:** the related-services exit grid, ROT explainer, ~500 more words of SEO prose and two further CTA bands still follow — harmless for SEO, but the conversion story is over.

---

## What works (keep)

- **The SEO substance is genuinely good.** ~2 000 words/page, correct facts (elcentral FAQ: "mellan 6 000 och 12 000 kronor efter ROT-avdrag"; felsökning FAQ correctly says ROT does **not** apply to bare felsökning; vitvaror ties DIY install to voided hemförsäkring — exactly the fear that motivates this audience). Preserve all of it; re-sequence, never delete.
- **MainContact** is the strongest block: proof-then-form, concrete next-step promise ("Vi ringer dig inom 24 timmar"), autocomplete address, real validation.
- **Per-page intent adaptation exists** where it matters: felsökning hero correctly leads with hemförsäkring instead of ROT; VissteDuAtt prose is page-specific, not boilerplate.
- **FAQ answers are money answers** (price, legality, ROT) written in candour register — the raw material for a first-screen price block already exists.
- **VarProcess** answers "what happens after I submit" — the #1 anxiety reducer (MECLABS *a* term) — it is just placed too late and carries copy bugs (below).
- Breadcrumbs, real reviews with names/dates, Elsäkerhetsverket/Skatteverket logo wall: authentic trust assets (Cialdini authority) — wrongly sequenced, not wrong.

---

## Findings

**SVC-01 · P0 · Hero form is client-side-only and paints late — the primary conversion element is invisible to fast-bouncing paid traffic.**
Evidence (verified in raw HTML): `#ampy-form-root class="aof" data-endpoint="…supabase.co/functions/v1/hero-lead"` is an **empty div**; the string "Få kostnadsfri rådgivning!" occurs **0 times** in the served HTML; the form is injected by a `<script defer src="data:text/javascript,…">`. Combined with ~9–10 s lab LCP, a paid mobile visitor in the first seconds sees no form (or an empty navy card — the script's own comment admits "otherwise you get a visibly empty, broken form box"). GA4's **0 form_start** across 32 paid sessions and the 1 s Vitvaror bounce are both consistent. Framework: MECLABS friction; Google landing-page experience; NN/g response-time limits. **Mobile:** worse — form is additionally a full viewport below the text column. Fix: server-render the form as static HTML (JS enhances only), or at minimum a static no-JS fallback (fields + submit) inside the card. Priority arithmetic: 22 pages × 3 (hero/form) × 3 (high) = **198**.

**SVC-02 · P0 · Message match breaks on the price dimension of the ad queries.**
"byta elcentral pris" → first screen contains no price; the answer ("vanligtvis mellan 6 000 och 12 000 kronor efter ROT-avdrag") sits inside FAQ, block 8. "installera diskmaskin" → Vitvaror has **no price answer anywhere on the page** (its 4 FAQs cover säkerhet/behörighet/tips/ROT only). Google message-match doctrine: ad → H1 → first screen must repeat the query's promise; MECLABS *v* (value clarity) and the documented Swedish-homeowner anxiety (price surprises, fixed vs estimated offert) both point the same way. **Mobile:** price is 8+ swipe-scrolls down (elcentral) or absent (vitvaror). Fix: a compact "Vad kostar det?" price block (range efter ROT + "fast offert innan arbetet påbörjas" promise) directly under the hero on every page; add the missing price FAQ to vitvaror-class pages. 22 × 3 × 3 = **198**.

**SVC-03 · P0 · Internal ROT contradiction on felsokning-av-el — trust-damaging.**
The templated ROT-block asserts "**Sänk kostnaden för din felsökning av el genom 30% rot-avdrag**" while the page's own FAQ states "**Nej, Skatteverket medger inte ROT-avdrag för enbart felsökning eller lokalisering av fel.**" (Both quotes verified live.) A price-anxious visitor who reads both loses trust in every other claim; this is exactly the internal-contradiction class the candour gate exists to catch. **Mobile:** both blocks are on the same scroll path. Fix: per-page block variant logic — felsökning (and any non-ROT-eligible service) gets the Hemförsäkring twin block (which its hero already correctly leads with) instead of ROT. 1 page × 2 × 3 = 6 as scoped, but audit all 22 for eligibility mismatches (elbesiktning is the next candidate). Severity is P0 on trust grounds, not reach.

**SVC-04 · P1 · Triple simultaneous ask in the hero (two equal-weight CTAs + form + header CTA).**
"Kostnadsfri rådgivning" (green) and "Ring 010-265 79 79" (blue) sit side by side above the form card, under a header that also carries "Gratis rådgivning" — three different labels for overlapping actions before the visitor knows what anything costs. Hick's law + MECLABS friction: undifferentiated choices suppress action; the whole page carries ~12 ask-points (6 tel links, 6 rådgivning buttons, 2 forms — verified counts). Note "Kostnadsfri rådgivning", "Gratis rådgivning" and "Boka rådgivning" (form submit) are three labels for the same thing — label consistency is free conversion hygiene (Jakob's law: predictability). **Mobile:** the two buttons stack and fill the first screen, pushing the rating and form further down. Fix: ONE primary ask per funnel stage — hero: form primary + phone as compact secondary (icon + number, not an equal gradient button); standardize on one label. 22 × 3 × 2 = **132**.

**SVC-05 · P1 · Proof architecture inverted: generic proof first, specific proof late.**
Position 4 is a 12-review carousel identical on all 22 pages (verified: elcentral, vitvaror, felsökning serve the same 12; only Moa Olaussen's mentions elcentral, none mention vitvaror or felsökning). Meanwhile the proof this audience actually checks — Elsäkerhetsverket-registered installer (Certificates, position 16), "3 000+ genomförda installationer om året" + 24-timmar promise (MainContact pane, position 10), fixed-offert promise (FAQ, position 8) — all sit below the SEO meat. The Clarity 47 s visitor who navigated Contact → About Us is behavioral evidence of unsatisfied trust-seeking. Cialdini authority > generic social proof for a regulated trade; Baymard: proof adjacent to the ask. **Mobile:** carousel costs ~2 viewports before any substance. Fix: compact authority strip under the hero (Elsäkerhetsverket-auktoriserad · anchored Google rating · 3 000+ installationer/år [owner-confirm]) and move the full carousel below ContentBlock; longer-term, tag reviews per service so each page leads with 2–3 relevant quotes. 22 × 2 × 3 = **132**.

**SVC-06 · P1 · Unanchored "5.0" claims, 4–6 instances per page — candour-gate exposure.**
Verified strings: bare "5.0" (hero + header), "5 av 5 Betyg på Google" (testimonials badge + MainContact), "5.0 på Google" (MainCTA), "5.0" (footer). None carries a review count or date. Candour rule: rating must be anchored (rating + count + source) or removed; an unanchored perfect score reads as fabricated to skeptical 50-year-olds and is a compliance risk if the live GBP rating drifts. **Mobile:** same instances. Fix: one canonical pattern "5,0 av 5 · N recensioner på Google" (N = owner-confirmed, auto-synced if possible) used at most twice per page (hero strip + MainContact). 22 × 2 × 2 = **88**.

**SVC-07 · P1 · H1/H2 inversion.**
Verified markup: `<h1>Byta elcentral</h1>` is the small eyebrow; the value-prop headline "Ny elcentral installerad med 30% ROT-avdrag" is an `<h2>` (`hero_2__section-heading`). The document outline tells Google and screen readers the page's main heading is a 2-word keyword stub, while the visual hierarchy says the opposite (NN/g visual-hierarchy ≠ semantic-hierarchy defect; SEO: H1 underweights the qualified phrase). **Mobile:** identical. Fix: swap semantics, keep visuals — H1 becomes the big headline (with the keyword folded in: "Byta elcentral — fast offert med 30% ROT-avdrag"), eyebrow becomes a `<p>`/`<span>`. 22 × 3 × 2 = **132**.

**SVC-08 · P1 · Form friction front-loads low-trust fields.**
Hero `.aof` form asks Adress + Postnummer before value is established (Baymard: visible/required field count drives perceived difficulty; address is a high-sensitivity field pre-trust). MainContact shows 8 visible fields (Förnamn, Efternamn, E-post, Telefon, Adress, Postnummer, Postort, Meddelande) for what the business needs to qualify a lead: name + phone + postnr (per the established Ampy min-lead doctrine). **Mobile:** 8 fields ≈ a full viewport of typing. Fix: hero form = kundtyp + ärende + namn + telefon + postnr + GDPR (address moves to the post-submit enrichment or the call); MainContact = single Namn field, drop Postort (auto from postnr), Meddelande stays optional-collapsed. 22 × 3 × 2 = **132**.

**SVC-09 · P1 · VarProcess copy defects on the block that exists to reduce anxiety.**
Verified: on **elcentral**, step 4 "Installation utförd" carries step 2's text verbatim ("Vi går vi igenom dina behov och skickar en transparent offert och tidsförslag.") — the payoff step never happens; vitvaror/felsökning have the correct step-4 text ("Du får en rapport på allt som elektrikern gjort samt slutfaktura inklusive ROT!" — which itself is wrong for felsökning, no ROT, see SVC-03). All 22 pages carry the duplicated-pronoun typos "Vi går **vi** igenom" (step 2) and "Vi skickar **vi** ut" (step 3). A four-step process with copy-paste errors undermines the "transparent, noggrann" positioning it is selling. **Mobile:** same. Fix: one corrected canonical step set + per-page step-4 audit; ROT mention conditional. 22 × 2 × 2 = **88**.

**SVC-10 · P1 · Two forms, two backends, no funnel instrumentation.**
Hero form posts to Supabase `hero-lead`; MainContact posts to n8n (block inventory + verified data-endpoint). GA4 recorded 0 form starts across 32 sessions — with 17 deep scrolls it is near-certain the custom forms emit no `form_start`/`form_submit` events, so the funnel is unmeasurable and Google Ads gets no negative-signal. Framework: you cannot optimize an uninstrumented funnel (a/b-testing doctrine); split backends also risk divergent lead handling/dedup. **Mobile:** n/a. Fix: unified dataLayer events (form_view, form_start, field_error, form_submit + source_form id) on both forms; consolidate or at least normalize the two endpoints' payloads. 22 × 3 × 2 = **132**.

**SVC-11 · P2 · Post-form SEO tail stacks 3 prose blocks + 2 CTA bands after the conversion point.**
VissteDuAtt (~250 dark-navy words) + CEBlock + FooterSEO all sit below MainContact/Map, each CEBlock/FooterSEO with its own CTA pair — CTA dilution at the weakest funnel position and heavy dark-block contrast stacking. SEO is preserved by keeping the text; the fix is compression/consolidation (merge CEBlock+FooterSEO prose into one section, single closing CTA) not deletion. **Mobile:** adds ~4 viewports after the form. 22 × 1 × 2 = **44**.

**SVC-12 · P2 · Copy-hygiene defects visible to a detail-oriented buyer.**
Verified: "Kostnadsfri **radgivning**" (missing å) in CEBlock + FooterSEO CTAs on all pages; ROT-block ACF interpolation produces "Sänk kostnaden för **dina vitvaror kostnad**" (vitvaror); "**Vår** experter går igenom" (ROT-block, all pages); reviewer name "**dany** Hanna" lowercase in the testimonial feed. Each is minor; together on a page claiming precision they compound. 22 × 1 × 1 = **22**.

**SVC-13 · P2 · Unverified performance claims need owner anchoring (candour).**
"Prata med en elektriker **inom 60 sekunder**!" (MainCTA) and "**3 000+ genomförda installationer om året**" (MainContact) are strong, specific claims — exactly the right kind IF true and current. Neither is in the confirmed-facts canon. Candour gate: owner-confirm or soften ("Vi svarar direkt på vardagar" / verified installation count). Not a call to remove — a call to verify, because both are high-value conversion assets when anchored. 22 × 2 × 1 = **44**.

**SVC-14 · P3 · Hero paint weight.**
The hero stacks decorative SVG waves, gradient layers, webp masks and a Google-logo SVG before content; with the deferred-JS form (SVC-01) this is the LCP-critical zone (~9–10 s lab). Fix alongside SVC-01: preload hero image, strip decorative SVG from the critical path, inline critical CSS. 22 × 3 × 1 = **66**.

---

## Recommended sequence (primary wireframe)

| # | Block | Why here | New/existing/modified |
|---|---|---|---|
| 1 | Header | unchanged; demote header CTA to match single-label system | Modified (label) |
| 2 | **Hero_2 v2** | H1 = real headline w/ query keyword ("Byta elcentral — fast pris med 30% ROT-avdrag"); ONE primary ask (server-rendered short form: kundtyp/ärende/namn/telefon/postnr/GDPR), phone as compact secondary; anchored rating chip | **Modified (P0)** |
| 3 | **Pris & offert-block** | Answers the ad query on screen 1–2: "Vad kostar det?" range efter ROT + fast-offert-innan-arbete promise + "Så påverkar ROT priset" microrow. Sourced from existing FAQ copy — message match for "…pris" queries | **New** (content exists, repackaged) |
| 4 | **Authority strip** | Elsäkerhetsverket-auktoriserad · "5,0 av 5 · N recensioner på Google" · 3 000+ installationer/år [owner-confirm] — compact one-row Certificates/MainContact-pane extract; proof adjacent to the ask (Cialdini/Baymard) | **New** (extracted) |
| 5 | VarProcess | "What happens when I submit" directly after the ask — anxiety reducer moved up; corrected copy, conditional ROT step | Modified |
| 6 | ContentBlock | full SEO rows preserved, now consumed by visitors already price-anchored (HealthSpire sequencing) | Existing |
| 7 | Testimonials | full carousel here, ideally service-tagged reviews first | Modified (position + tagging) |
| 8 | ROT-block **or** Hemförsäkring variant | eligibility-gated per service (fixes SVC-03) | Modified (conditional) |
| 9 | MainCTA | phone-band for readers who prefer to talk; claims anchored | Modified (copy) |
| 10 | FAQ | remaining questions (price now also up top; keep the duplicate answer here for SEO/AEO) | Existing |
| 11 | MainContact | the closer, unchanged structure, trimmed fields (SVC-08), instrumented | Modified (fields+events) |
| 12 | MapBlock | geo internal linking | Existing |
| 13 | Related-services grid | exit ramps below the conversion zone — correct place | Existing |
| 14 | Merged SEO tail (VissteDuAtt + CEBlock + FooterSEO prose) | one editorial section, ONE closing CTA pair — all text kept in DOM | Modified (merged) |
| 15 | Certificates | full logo wall stays for the skimmer who reads bottom-up | Existing |
| 16 | Prefooter/Footer | unchanged | Existing |

## Divergent alternative (house rule): "Call-first / one-ask ladder" variant

For high-urgency or diagnostic intents (felsokning-av-el, jordfelsbrytare, elbesiktning — the Unbounce finding that repair/urgent pages convert best): **no hero form at all**. Hero = H1 problem-statement ("Elfel i huset? Vi felsöker metodiskt — ofta via hemförsäkringen") + single dominant "Ring 010-265 79 79" + "svar direkt på vardagar" [owner-confirm] + authority strip; a **sticky mobile call bar** (Eljour-block pattern, already proven in the Ampy library) persists through the scroll; the ONLY form on the page is MainContact at the close, framed as "vill du hellre bli uppringd?". Rationale: phone is the conversion that already works (2/2 recorded conversions were calls), the JS-form risk is removed entirely on the pages where urgency makes typing least likely, and the single-ask ladder gives a clean A/B against the form-first primary. Planned-improvement intents (vitvaror, kok, belysning, smarta-hem) keep the form-first primary wireframe.

---

## Test hypotheses (top 3, A/B)

1. **HYPOTES (form availability):** Server-rendering the hero form as static HTML (JS enhancement only) vs. the current deferred-JS injection will produce measurable `form_start` events and lift form submits on paid landings from ~0%; secondary metric: Vitvaror-class paid bounce rate. (Prereq: SVC-10 instrumentation, else nothing is measurable.)
2. **HYPOTES (price message match):** Adding the "Vad kostar det?"-block (range efter ROT + fast-offert promise) directly under the hero on pris-intent pages (elcentral, vitvaror, golvvarme) will increase combined conversions (calls + forms) vs. the current FAQ-only price placement, per Google message match + MECLABS value clarity.
3. **HYPOTES (single ask):** A hero with one primary ask (short form; phone as compact secondary) will beat the current dual equal-weight gradient CTAs + form triple-ask on combined conversion rate, without reducing total phone calls (Hick's law / MECLABS friction).

*Fetch note: all quoted copy above was taken from the live pages on 2026-08-02; the Hero_2 form card copy ("Få kostnadsfri rådgivning!" etc.) is quoted from the block inventory because it is absent from the served HTML — which is itself finding SVC-01.*
