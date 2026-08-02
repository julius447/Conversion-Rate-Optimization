# Template deep-dive: Programmatic geo — `elinstallation-i` + `laddbox-i`

URLs analyzed (live-fetched 2026-08-02): https://ampy.se/elinstallation/vaxholm/ , https://ampy.se/laddbox/nacka/ — cross-checked against https://ampy.se/elinstallation/sollentuna/ and https://ampy.se/laddbox/taby/ for template invariance and content uniqueness.
Pages using these templates: **112** (56 elinstallation-i + 56 laddbox-i, from block-map.json — each template has exactly ONE block sequence across all 56 orter).

Intent profile: `elinstallation-i` = generic install intent ("elinstallation [ort]", "elinstallatör [ort]") — a service capture page. `laddbox-i` = mixed product+service intent ("laddbox [ort]", "installera laddbox [ort]", "laddbox pris") — the #2 commercial priority (service > laddbox > battery). Both are prime organic/paid landing candidates for the 35–65 Swedish homeowner.

---

## Current block sequence (verified: block-map.json + live DOM text + raw HTML)

### elinstallation-i (Vaxholm instance, 1 908 words, 808 KB HTML)
| # | Block | Verified live content | Desktop | Mobile |
|---|---|---|---|---|
| 1 | Header | Mega-menus + "Gratis rådgivning" teal CTA → **/kontakt/** | Sticky top bar | Offcanvas + "Ring en expert" + 5.0 |
| 2 | Hero_2 | Breadcrumbs → **H1 (small eyebrow) "Elinstallation i Vaxholm"** → H2 (big gradient) "Elinstallationer för ditt hem i Vaxholm!" → paragraph ("…full dokumentation och 30 % ROT-avdrag") → CTAs "Kostnadsfri rådgivning" (→ **/kontakt/**) + "Ring 010-265 79 79" → unanchored "5.0" row | Two-col, form card right | Stacked; form card below fold |
| 3 | Hero_2-aof-form | "Få kostnadsfri rådgivning!" card — **entirely JS-injected** (0 `<input>` in server HTML; even "Boka rådgivning" submit label absent from source; built via URL-encoded `createElement`/`innerHTML` script with per-page vertical resolver `vertical:'service'`, opts `'elinstallation','Belysning','Laddbox'…`) | Right column, 450px | Below hero text, ~screen 2 |
| 4 | Testimonials | "Vad säger dina grannar om Ampy?" — 12 real named Google reviews w/ dates (mars–juni 2026), badge "5 av 5 · Betyg på Google" (no count) | Splide slider, dark navy cards | 1-up swipe |
| — | **ServiceGrid** (NOT in block-map — data-layer gap) | "Vårt utbud av elinstallationer i Vaxholm – installerat & klart med 30 % ROT-avdrag": 6 cards (Belysning/Elcentral/Köksrenovering/Luftvärmepump/Smarta hem/Spotlights) + "Ladda fler tjänster" | 3-col grid | Stacked cards |
| 5 | MainCTA | "Prata med en elinstallatör inom 60 sekunder!" → Ring-only CTA + "5.0 på Google" | Text left, team image right | Centered stack |
| 6 | ContentBlock | 3 SEO rows: "Trygga lösningar för ditt hem i Vaxholm" / "Auktorisation och dokumenterad säkerhet" / "Energieffektivisering…" — **genuinely unique per ort** (0.11 similarity vs Sollentuna after ort-name normalization) | Alternating img/text | Stacked |
| 7 | VarProcess | "Så funkar det" — 4 steps (Samtal → Offert & tidsförslag → Bokning → Installation utförd) | 4-up icons | Stacked |
| 8–9 | MainContact + card | Photo pane (quote, "5 av 5 · Betyg på Google", **"3 000+ genomförda installationer om året"**, 3 steps incl. "Vi ringer dig inom 24 timmar") + form: Förnamn/Efternamn/E-post/Telefonnummer/Adress/Postnummer/Postort/Meddelande (7–8 visible fields) | Two-pane | Form under photo pane |
| 10–11 | FAQ + accordion | 4 Q — incl. real price candour: "normalt mellan **650 och 950 kronor i timmen efter ROT-avdrag** … tillkommer ofta en startavgift för servicebil och materialkostnader" | 55/45 w/ image | Stacked |
| 12 | ROT-block | "Sänk din elinstallations kostnad genom 30% rot-avdrag" — 3 steps + "Läs mer om ROT-avdrag". Copy defect: "**Vår experter** går igenom…" | White card | Stacked |
| 13 | BlueCTA | "Prata med en elinstallatör!" → black Ring button | Cyan band | Stacked |
| 14 | VissteDuAtt | "Gamla kablar ökar risken för bostadsbränder?" — fear-register, locally flavored ("skärgårdsnära orter som Vaxholm") | Dark navy card, swinging bulb | Stacked |
| 15 | MapBlock | "Vi finns där du finns" + 20 ort links (incl. far-off Nynäshamn, Södertälje) + templated defect "**Vi erbjuder expertis på several orter**" (English "several", confirmed on Sollentuna too = all 56 pages) | Grid + Sweden map | Dot-map |
| 16 | CEBlock | "Certifierad expertis för din elinstallation i Vaxholm" + typo "**varje elinstallaation**" + CTA "Kostnadsfri **radgivning**" (missing å, 2×/page) | Text + 9:16 image | Stacked |
| 17 | Certificates | Elsäkerhetsverket, Skatteverket, Naturvårdsverket, ID06, Trygg Hansa, Rexel | 6 logo cards | Stacked |
| 18 | FooterSEO | "Certifierad elinstallation i Vaxholm" + CTA pair | Img bottom-right | Stacked |
| 19 | Prefooter/Footer | "Populära kategorier" + navy footer w/ third unanchored "5.0" | 5 columns | Accordion |

### laddbox-i (Nacka instance, 2 003 words, 820 KB HTML) — differences from sibling
Sequence: Header → Hero_2 (+JS aof form) → **ProductGrid (position 3 — unique to this template)** → Testimonials → MainCTA ("Prata med en laddboxinstallatör inom 60 sekunder!") → ContentBlock ("Trygg installation…", "Optimera din laddning med lastbalansering", "Förberedelser inför nya lagkrav 2026") → **MikroCTA** ("Vill du veta mer? … hur **Sveriges snabbast växande elfirma** kan hjälpa dig") → **FAQ** → MainContact → MapBlock → BlueCTA ("Prata med vår laddboxexpert!") → VissteDuAtt ("En laddstation kan öka din fastighets värde?" — warm register, correctly matched) → **GronTeknik** ("Sänk din laddbox kostnad genom 50% Grön Teknik-avdrag") → CEBlock → Certificates → FooterSEO → Prefooter.

ProductGrid verified content: "Våra laddboxar – installerat & klart med 50 % Grön Teknik-avdrag" → 4 cards: Zaptec Go "SUPERKAMPANJ … Fr. 4 490 kr", Zaptec Go 2 "NYHET … Fr. 5 890 kr", Easee Charge Up "Fr. 4 390 kr", NexBlue Edge 2 "Fr. 4 190 kr" — each "Läs mer" → product page; "Ladda fler produkter" loader. Desktop: 4-up row. Mobile: stacked = **~4 screens of product cards between hero and first social proof**.

Structural deltas: laddbox-i has ProductGrid + MikroCTA + GronTeknik but **no VarProcess and no ROT-block**; FAQ sits BEFORE MainContact (elinstallation-i has FAQ AFTER MainContact — the two siblings disagree on objection-vs-ask order).

CTA plumbing (both): every "Kostnadsfri rådgivning" button (hero, CEBlock, FooterSEO — 3–4 per page) links to **https://ampy.se/kontakt/**, not to the on-page form. 7–8 `tel:+46102657979` links per page. No sticky mobile call bar.

---

## Customer-flow walkthrough (35–65 homeowner, mobile-first)

**First 5 seconds (elinstallation/vaxholm, from Google "elinstallation vaxholm" or "byta elcentral pris"):** SERP promised "fast pris & säker installation". Landing: small green "Elinstallation i Vaxholm" (H1), big headline "Elinstallationer för ditt hem i Vaxholm!" — which only restates the query, offering no price, no speed, no differentiator. Two buttons + a "5.0" with no review count. On a slow connection (lab LCP flag 9–10s) the form card slot is empty until JS executes. The visitor's #1 question — "vad kostar det?" — is answered nowhere above the fold; the "fast pris" they were promised never appears on the page at all (the FAQ instead quotes hourly rates + startavgift + material).

**Scroll:** real reviews with names and dates (strong — this is the trust the Clarity "About Us" visitor went hunting for) → service grid (helpful orientation, but 6 more exit doors) → "Prata med en elinstallatör inom 60 sekunder!" ring-CTA → three long SEO sections → process steps → the big form. A patient visitor reaches MainContact at roughly screen 10–12 on mobile. Everything after (8 more blocks) is anticlimax; the ROT incentive — the single best economic motivator — appears only AFTER the form ask.

**laddbox/nacka:** hero says "50 % skatteavdrag för grön teknik direkt på fakturan" (good) but headline "När du behöver en laddbox i Nacka!" is empty calories. Immediately: 4 product cards with prices. This DOES answer "vad kostar det" (Fr. 4 190 kr) — the strongest anxiety-reducer on either template — but presents a 4-way comparison decision before a single proof element, and every card's only CTA ("Läs mer") exits to a product page whose conversion path is a popup form. A visitor who taps Zaptec Go leaves the geo page for good. The visitor who scrolls past instead gets reviews → ring-CTA → SEO → FAQ (excellent price candour: "mellan 5 000 och 12 000 kronor efter … avdraget") → form. But the FAQ's "från ca 5 000 kr inklusive installation och avdrag" quietly contradicts the grid's "Fr. 4 190 kr … installerat & klart" — the exact price-surprise anxiety Swedish homeowners report on Byggahus.

**Decision:** the motivated caller converts (phone is well served: 7–8 tel links + ring-CTAs). The form-preferring visitor faces: a JS-dependent hero form asking address+postnummer up front, or a 7–8-field MainContact ten screens down, or a "Kostnadsfri rådgivning" button that ejects them to /kontakt/ for another 9-second page load. GA4's "0 form starts" on paid traffic is exactly what this plumbing predicts.

---

## What works (keep)

1. **Genuinely unique programmatic content.** ContentBlock/FAQ/VissteDuAtt/CEBlock similarity across orter = 0.07–0.16 after ort-name normalization (measured Vaxholm↔Sollentuna, Nacka↔Täby). These are NOT doorway pages; unique headings per ort too. Preserve this asset — re-sequence, never flatten to a shared template text.
2. **Exact-match H1** ("Elinstallation i Vaxholm" / "Laddbox i Nacka") — clean message match for the core geo query (Google message-match principle).
3. **Testimonials at position ~4** — 12 real, named, dated Google reviews near the top. Best proof placement of any Ampy template family; matches the Clarity trust-seeking evidence.
4. **FAQ price candour** — real numbers ("650–950 kr/h efter ROT", "5 000–12 000 kr efter avdrag"), real caveats (startavgift, markarbeten). This is the candour brand executed; it must move UP, not out.
5. **ProductGrid price anchors** (laddbox) — concrete "Fr. X kr" quiets the dominant price anxiety (MECLABS *a*); the block itself earns its keep.
6. **Local texture** — "skärgårdsnära orter som Vaxholm", "skärgårdskommunens olika bostadsområden" (Nacka): genuine local relevance, not token ort-insertion.
7. **Per-page form vertical resolver** — the aof form pre-scopes options to the page's vertical (`'elinstallation','Belysning','Laddbox'…`); smart friction reduction worth keeping when the form is fixed.
8. **VissteDuAtt register match** — laddbox uses the warm value-uplift angle, elinstallation the fire-safety angle; both appropriate to intent stakes.

---

## Findings

**GEO-01 — Primary CTA ejects to /kontakt/ instead of the on-page form. P0.**
All "Kostnadsfri rådgivning" buttons (hero + CEBlock + FooterSEO, 3–4/page) link to https://ampy.se/kontakt/ although the page has a hero form AND MainContact. On a site with a 9–10s lab LCP, the primary CTA imposes a full extra page load between intent and form (MECLABS friction term; NN/g: every step sheds users). Mobile: identical — the tap leaves the page. Fix: anchor-scroll to the on-page form (hero → aof; lower CTAs → MainContact). Priority: 112 pages × 3 (hero/form) × 3 (high) = **1 008**.

**GEO-02 — Hero form is 100 % JS-injected; nothing exists server-side. P0.**
Verified in raw HTML: 1 `<form>` tag total (MainContact); `class="aof"` contains only scoped CSS + a URL-encoded script building fields via `createElement`/`innerHTML`; the submit label "Boka rådgivning" appears 0 times in source. Consequences: (a) slow devices/paid mobile traffic can meet an empty hero column during the long JS window; (b) analytics can't auto-capture — consistent with GA4 recording **0 form starts** across ~32 paid sessions; (c) form invisible to crawlers. Mobile note: the form card is the second screen — the page's best-placed ask renders last. Fix: server-render at least a minimal 3-field version (namn/telefon/postnummer + GDPR per the locked min-lead contract) and progressively enhance; emit `form_start`/`form_submit` dataLayer events. Priority: 112 × 3 × 3 = **1 008**.

**GEO-03 — elinstallation-i SERP promise "fast pris" is broken on the page. P0.**
Title tag: "Elinstallation Vaxholm - **prisvärd installation med fast pris**"; meta: "**fasta priser**". The page never states a fixed price; the FAQ instead says hourly "650–950 kr i timmen" plus "tillkommer ofta en startavgift … och materialkostnader". This is message-match failure (Google) landing directly on the documented #1 Swedish homeowner anxiety (Byggahus/Reddit: final-price surprises) — and a candour-gate breach: the SERP asserts what the page retracts. Fix: either introduce real fixed-price packages ("Fast pris fr. X kr — [3 vanligaste jobben]") mirroring laddbox-i, or rewrite title/meta to the honest offer ("prisvärd" + transparent offert). Mobile: identical. Priority: 56 × 3 × 3 = **504**.

**GEO-04 — Hero H2 (the big visual headline) carries zero value. P1.**
"Elinstallationer för ditt hem i Vaxholm!" and "När du behöver en laddbox i Nacka!" restate the H1 above them. The largest element on 112 pages says nothing the eyebrow didn't (MECLABS value clarity: the value proposition must survive the 5-second glance). Service pages already prove the pattern works: "Ny elcentral installerad med 30% ROT-avdrag". Copy direction: "[Tjänst] i [Ort] — installerat & klart med [30 % ROT / 50 % Grön Teknik]-avdrag" or a from-price + speed promise. Mobile: H2 dominates the first screen, so the waste is worst there. Priority: 112 × 3 × 2 = **672**.

**GEO-05 — laddbox-i ProductGrid at position 3: helps the intent, hijacks the funnel. P1.**
Assigned question, verdict: **keep the block, rewire its exits, don't move it far.** Help: "laddbox nacka" intent is part product-choice — "Fr. 4 190–5 890 kr, installerat & klart med 50 % avdrag" is the strongest price-anxiety reducer on either template and honors the "fast pris" title. Hijack: (a) each card's only CTA "Läs mer" navigates to the product page → its conversion is a *popup* form — the geo page loses the visitor before ANY proof block; (b) a 4-option comparison task lands before trust is established (Hick's law: decision load before motivation); (c) mobile: 4 stacked cards + "Ladda fler produkter" push Testimonials ~4 screens down, inverting the proof architecture the template otherwise gets right. Fix: dual CTA per card — primary "Få pris installerad i {ort}" pre-filling the on-page form with the product, secondary "Läs mer"; cap at 3 cards + "Jämför alla laddboxar" link; consider swapping ProductGrid↔Testimonials (proof then choice). Priority: 56 × 3 × 2 = **336**.

**GEO-06 — Incentive blocks placed AFTER the main form ask. P1.**
elinstallation-i: ROT-block is block 12, below MainContact (8–9). laddbox-i: GronTeknik is block 16 of 20, below MainContact (11). The avdrag is the single largest economic motivator (MECLABS *i*: incentive offsets friction only if seen BEFORE the ask; HealthSpire: order, not length, drives conversion). Mobile: incentive is 15+ screens deep. Fix: move ROT/GronTeknik immediately above MainContact (or fold the 3-step avdrag strip into MainContact's left pane). Priority: 112 × 2 × 2 = **448**.

**GEO-07 — Unanchored "5.0"/"5 av 5" ×5–6 per page + "3 000+ installationer" unverified. P1.**
Hero "5.0", MainCTA "5.0 på Google", Testimonials badge "5 av 5 Betyg på Google", MainContact pane "5 av 5 · Betyg på Google" + "3 000+ genomförda installationer om året", footer "5.0" — none carries a review count or date. Candour gate + Cialdini social proof: unanchored perfection reads as fabricated to a skeptical 55-year-old; Baymard notes rating displays without volume depress trust. Fix: one canonical anchored badge ("5,0 av 5 · N recensioner på Google", owner-confirmed) reused everywhere; "3 000+" needs owner provenance or removal `[GAP]`. Mobile: identical. Priority: 112 × 2 × 2 = **448** (site-wide in reality).

**GEO-08 — laddbox-i has no VarProcess (process/how-it-works) block. P1.**
elinstallation-i shows "Så funkar det" (4 steps); laddbox-i — a 5 000–12 000 kr considered purchase with a survey/lastbalansering step buyers don't understand — has none. JTBD: the job includes "know what happens after I submit"; NN/g: process visibility reduces abandonment on service purchases. Fix: add the existing VarProcess block (laddbox variant: Samtal → Teknisk genomgång/offert → Installation 1–2 veckor → Avdrag på fakturan — the meta description already promises "inom 1–2 veckor", currently substantiated nowhere on the page). Priority: 56 × 2 × 2 = **224**.

**GEO-09 — Internal price contradiction on laddbox-i. P1.**
ProductGrid: "Fr. 4 190 kr" under "installerat & klart med 50 % Grön Teknik-avdrag". FAQ: "kostar vanligtvis mellan 5 000 och 12 000 kronor efter … avdraget" and "ofta med ett nettopris från ca 5 000 kr inklusive installation och avdrag". A price-comparing homeowner sees 4 190 vs "från ca 5 000" on the same page — precisely the offert-surprise anxiety this audience reports. Rule-5 internal contradiction: reconcile (one canonical "fr." figure, or a grid caveat line "pris efter avdrag, standardinstallation; exakt pris i offerten"). Mobile: grid and FAQ are far apart, but comparison shoppers screenshot prices. Priority: 56 × 2 × 2 = **224**.

**GEO-10 — No mobile sticky call bar despite call being conversion #1. P1→test.**
7–8 scattered `tel:` links but nothing persistent; the header CTA ("Gratis rådgivning") even routes to /kontakt/. Fitts + mobile thumb-zone: a fixed bottom bar ("Ring 010-265 79 79" | "Få offert" → form anchor) keeps both conversion paths one tap away through a 19-block scroll. HYPOTES — see tests. Priority: 112 × 3 × 2 = **672** if the test wins.

**GEO-11 — 8–9 blocks of anticlimax after the main form; authority proof buried at the bottom. P2.**
After MainContact: elinstallation-i still runs FAQ→ROT→BlueCTA→VissteDuAtt→Map→CE→Certificates→FooterSEO. Certificates (Elsäkerhetsverket — the exact proof Konsumentverket-minded Swedes check) sits at position 17. Fix: pull an authority strip (Elsäkerhetsverket-registrerad + anchored rating) up under the hero; merge CEBlock+FooterSEO into one SEO tail; keep all SEO text (re-sequence, never delete). Mobile: the tail is ~10 swipe-screens of diminishing signal. Priority: 112 × 1 × 2 = **224**.

**GEO-12 — CTA proliferation: ~9–10 asks, 3 visual systems, 2 destinations. P2.**
Hero pair + JS form + MainCTA ring + MikroCTA pair (laddbox) + MainContact + BlueCTA ring + FooterSEO pair + header CTA. Ring-CTAs alone appear in 4 different block styles. Hick's law + MECLABS attention: one primary form ask + one persistent phone ask per viewport. Fix inside re-sequencing (below): each scroll-zone gets ONE ask. Priority: 112 × 2 × 1 = **224**.

**GEO-13 — Templated copy defects multiplied ×56. P2 (trust-corrosive, trivial to fix).**
Verified templated (present on both spot-checked orter per template): "Vi erbjuder expertis på **several** orter" (English word, all elinstallation-i MapBlocks); "**Vår experter** går igenom ditt projekt" (ROT + GronTeknik blocks, both templates); "Kostnadsfri **radgivning**" missing å (2×/page, CEBlock+FooterSEO); "varje **elinstallaation**" (Vaxholm CEBlock). For a 35–65 audience judging craftsmanship by proxies, misspelled Swedish on an "auktoriserad" page is anti-proof (Cialdini authority undermined). Priority: 112 × 1 × 2 = **224**.

**GEO-14 — Unverifiable operational/superlative claims. P2 (candour).**
"Prata med en elinstallatör **inom 60 sekunder**!" (MainCTA H2, both templates) — a service-level claim; owner must confirm phone pickup actually meets it or soften ("Svar direkt på telefon"). "**Sveriges snabbast växande elfirma**" (laddbox MikroCTA) — strong superlative allowed per owner directive unless demonstrably false; needs an owner basis on file `[GAP]`. Priority: 112 × 2 × 1 = **224**.

**GEO-15 — MapBlock ort list is random, not proximity-ranked. P3.**
Vaxholm's list leads with Värmdö (good) but includes Nynäshamn/Södertälje (~60 km). Weak local-relevance signal for users and internal-link equity. Fix: proximity-sort the 20 links per ort. Priority: 112 × 1 × 1 = **112**.

**GEO-16 — Page weight: 808–820 KB of HTML alone, inline URL-encoded JS payloads. P2 (site-wide speed program).**
Feeds the 9–10s lab LCP flag; compounds GEO-01 (every /kontakt/ redirect re-pays the cost) and GEO-02. Note for the speed workstream; not solvable at template level alone.

**GEO-17 — Sibling templates disagree on FAQ-vs-form order. P3 (standardize).**
elinstallation-i: MainContact → FAQ. laddbox-i: FAQ → MainContact. The laddbox order (objections answered, then ask — MECLABS anxiety before ask) is correct; standardize both to FAQ → MainContact.

**Data note:** the live elinstallation-i template contains a **ServiceGrid** ("Vårt utbud av elinstallationer i {ort}", 6 service cards, confirmed Vaxholm + Sollentuna) that block-map.json does not list — the block-map fingerprint set should add it (it is the elinstallation sibling of laddbox's ProductGrid, at the post-Testimonials slot).

---

## Recommended sequence (wireframe)

### elinstallation-i (56 pages)
| # | Block | Why here | Status |
|---|---|---|---|
| 1 | Header | — | Existing |
| 2 | Hero_2 + form | H2 rewritten to value ("Elinstallation i {ort} — utfört av auktoriserad elektriker med 30 % ROT-avdrag" + from-price if GEO-03 resolves to packages); "Kostnadsfri rådgivning" → **#form anchor**; form **server-rendered**, 3 core fields + progressive disclosure | Modified |
| 3 | TrustStrip | Anchored Google badge ("5,0 · N recensioner") + Elsäkerhetsverket-registrerad + "3 000+…" (if owner-confirmed) — authority at the decision point (Cialdini), replaces bottom-buried Certificates duty | **New** (compressed Certificates + rating) |
| 4 | Testimonials | Keep high — proven placement | Existing |
| 5 | ServiceGrid | Orientation for the generic intent; add per-card "eller ring oss" microcopy | Existing (add to block-map) |
| 6 | ContentBlock | SEO meat preserved intact, unique per ort | Existing |
| 7 | ROT-block | **Moved above the ask** (incentive before form, GEO-06); fix "Vår experter" | Moved |
| 8 | VarProcess | Process reassurance directly before the ask | Existing (moved up) |
| 9 | FAQ | Objections (price candour) answered BEFORE the form (GEO-17) | Moved |
| 10 | MainContact | The closer; consider trimming to Baymard-minimal visible fields | Existing |
| 11 | MapBlock | Internal linking; proximity-sorted; fix "several" | Modified |
| 12 | CEBlock + FooterSEO (merged) | One SEO tail + final CTA pair (→ #form); fix å/typos | Merged |
| 13 | VissteDuAtt | Editorial close (fear block sits better after the ask than between incentive and form) | Moved down |
| 14 | Prefooter/Footer | — | Existing |

### laddbox-i (56 pages)
| # | Block | Why here | Status |
|---|---|---|---|
| 1 | Header | — | Existing |
| 2 | Hero_2 + form | H2: "Laddbox installerad i {ort} — fr. X kr efter 50 % Grön Teknik-avdrag" (X = the reconciled canonical figure, GEO-09); CTA → #form; server-rendered form w/ product select | Modified |
| 3 | TrustStrip | As above | **New** |
| 4 | Testimonials | Proof BEFORE the comparison decision | Moved up one slot |
| 5 | ProductGrid | **Kept near top** (price anchors earn it) but: 3 cards + "Jämför alla laddboxar" → /laddboxar/; dual CTA — primary "Få pris installerad i {ort}" pre-fills the on-page form, secondary "Läs mer"; candour caveat line reconciling grid vs FAQ pricing | Modified |
| 6 | GronTeknik | Incentive up from position 16 to before the mid-page ask | Moved |
| 7 | VarProcess (laddbox variant) | NEW for this template — substantiates the meta's "inom 1–2 veckor" promise | **New instance** |
| 8 | ContentBlock | SEO preserved (lastbalansering/2026-lagkrav are genuine decision content) | Existing |
| 9 | FAQ | Price candour before the ask (already correct order — keep) | Existing |
| 10 | MainContact | The closer | Existing |
| 11 | MapBlock | Proximity-sorted | Modified |
| 12 | CEBlock + FooterSEO (merged) | SEO tail + final CTA → #form | Merged |
| 13 | VissteDuAtt | Warm editorial close | Moved down |
| 14 | Prefooter/Footer | — | Existing |

(Cut from both flows as standalone blocks: MainCTA "60 sekunder" band, BlueCTA, MikroCTA — their phone ask is absorbed by the mobile sticky bar test + one ring-CTA inside TrustStrip/MainContact. Their H2 copy lines survive as microcopy; no SEO text is deleted anywhere — blocks are merged or moved, never removed with content.)

---

## Test hypotheses (top 3, A/B-phrased)

1. **HYPOTES — CTA target:** On geo pages, changing all "Kostnadsfri rådgivning" buttons from `→ /kontakt/` (A) to smooth-scroll `→ #on-page-form` (B) will increase form starts and reduce exit rate on paid+organic geo sessions, because it removes a full page load (~9–10s lab LCP) between intent and ask (MECLABS friction). Primary metric: form_start /session; guardrail: phone-click rate.
2. **HYPOTES — ProductGrid rewiring (laddbox-i):** Replacing the cards' single "Läs mer" (A) with dual CTA where primary "Få pris installerad i {ort}" pre-fills and scrolls to the on-page form (B) will lift geo-page form submissions without reducing total laddbox conversions, because it converts product-choice momentum on-page instead of exporting it to a popup-gated product page (Hick's law, funnel-step removal). Metric: form submits attributed to geo landing; secondary: product-page popup submits (watch for cannibalization).
3. **HYPOTES — Server-rendered minimal hero form:** A server-rendered 3-field hero form (namn/telefon/postnummer + GDPR) with "Fler detaljer" disclosure (B) will outperform the current JS-injected 6+-field card (A) on mobile paid traffic in form starts AND qualified submits, because fields-visible drives perceived difficulty (Baymard) and render-dependency currently suppresses the ask entirely on slow devices. Metric: form_start and submit rate; guardrail: lead-quality score from CRM callback outcomes.

(Backlog test 4: mobile sticky bottom bar "Ring" | "Få offert" vs none — Fitts/thumb-zone; run after 1–3 to avoid interaction effects.)
