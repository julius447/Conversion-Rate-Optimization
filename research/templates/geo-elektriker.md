# Template deep-dive: Programmatic geo — elektriker-i

URLs analyzed (fetched live 2026-08-02): https://ampy.se/elektriker/tyreso/ · https://ampy.se/elektriker/sollentuna/
Pages using this template: **56** (block-map.json category `elektriker-i`; 57 URLs under `/elektriker/` minus the pillar `/elektriker/` itself, which is the single outlier using Hero-1 with a shuffled block order). Word count 2 431–2 576 per page (genuinely varied copy, not duplicated); HTML document size **790–855 KB** per page.

**Visitor psychology (the lens for everything below):** "elektriker tyresö" is a high-intent, near-bottom-funnel local query from a 35–65 Swedish homeowner. Their three questions, in order: (1) *Kommer ni hit — och hur snabbt?* (2) *Vad kostar det — blir jag lurad på priset?* (3) *Är ni behöriga/pålitliga?* (Byggahus/Konsumentverket research: written quote, Elsäkerhetsverket registration, price-surprise fear). They will convert on THIS visit or bounce to the next SERP result. Mobile-first (assume ≥65% mobile for local intent).

---

## Current block sequence (VERIFIED against live `<section>` markup, not block-map)

Live order on both pages (19 sections). **Note:** block-map.json omits one block — a `services-loop` grid sits between MainCTA and Testimonials on the live pages (data-hygiene fix needed in block-map).

| # | Block (live class) | Desktop behavior | Mobile behavior |
|---|---|---|---|
| 1 | **Hero_2** (`hero_2`) | Breadcrumbs → **H1 = small eyebrow** "Elektriker Tyresö" → H2 headline "Boka en pålitlig elektriker i Tyresö!" → paragraph → 2 CTAs (**"Kostnadsfri rådgivning" → links OFF-PAGE to /kontakt/**; "Ring 010-265 79 79" tel:) → 5.0 ★ row (links to GBP, no count) → right column `<div id="ampy-form-root" class="aof">` — **EMPTY container; entire form is injected client-side by inline JS** (`formCard()` builds it, including a second `<h1>Få kostnadsfri rådgivning!</h1>`) | Columns stack; form renders below text/CTAs, ~1.5–2 screens down. Until JS executes there is no form at all (lab LCP flagged 9–10 s) |
| 2 | **Metrics** (`metrics`) | 3 number cards: "**1000+** Nöjda kunder / Över tusen genomförda installationer…", "**25+** Erfarenhet i branschen / Vår samlade yrkeskunskap…", "**20+** Personer i teamet" | Cards stack vertically |
| 3 | **MainCTA** (`main-cta-`) | "**Prata med en elektriker inom 60 sekunder!**" + "5.0 på Google" trust row + single Ring CTA + team image | Centered stack |
| 4 | **Services grid** (`services-loop`) — *not in block-map* | "Vårt utbud av eltjänster i {ort} – installerat & klart med 30 % ROT-avdrag": 6 cards (Belysning/Elcentral/Köksrenovering/Luftvärmepump/Smarta hem/Spotlights) each linking to its /elservice/ page + "Ladda fler tjänster" (`href="#"`, JS load-more) | Card grid stacks/2-up |
| 5 | **Testimonials** (`ampy-testimonials`) | "Vad säger dina grannar om Ampy?" — Splide slider, 12 real Google reviews (Adam Andersson mars 2026 … Filip Eriksson mars 2026), "5 av 5 Betyg på Google" badge, no count | Swipe slider, 1-up |
| 6 | **VarProcess** (`our-process`) | "Så funkar det" — 4 steps (Samtal → Offert & tidsförslag → Bokning bekräftad → Installation utförd) | 4 icon-boxes stack |
| 7 | **MainContact** (`main-contact`) | Two-pane: left photo pane (quote + "5 av 5 · Betyg på Google" + "**3 000+ genomförda installationer om året**" + 3 steps incl. "Vi ringer dig inom 24 timmar") · right = the only **server-rendered** form (Förnamn/Efternamn/E-post/Telefonnummer/Adress/Postnummer/Postort/Meddelande → "Gratis rådgivning") | Panes stack; 8 visible fields on one screen |
| 8 | **FAQ** (`faq-`) | "Vanliga frågor" — 4 localized accordions (Tyresö: småjobb/proppskåp/serviceavtal/hur snabbt; Sollentuna incl. the gold question "Hur kontrollerar jag att en elfirma… är registrerad hos Elsäkerhetsverket?" → 'Kolla elföretaget') | Accordion full-width |
| 9 | **ROT-block** (`rot`) | "Sänk din elektriker kostnad genom 30% rot-avdrag" — 3 icon items + "Läs mer om ROT-avdrag" (nav away) | Stack |
| 10 | **MikroCTA** (`mikro_cta`) | "Vill du veta mer? … Sveriges snabbast växande elfirma" + CTA pair (Kostnadsfri rådgivning → **/kontakt/**; Ring tel:) | Stack |
| 11 | **TeamSection** (`team`) | "Möt våra certifierade elektriker i {ort}" — 5 bios (Mio/Magnus/Felix/Edvin/Yousef); bios are battery/laddbox-heavy (Mio: "stödtjänster och ö-drift… SAJ HS3 och Dyness Stack 100") | Slider 1-up |
| 12 | **MapBlock** (`map`) | "Vi finns där du finns" — 20 ort links to sibling geo pages + "Osäker ifall vi finns där du bor? **Kontakta oss** → /kontakt/" + Sweden map | Dot-map + link grid |
| 13 | **ContentBlock** (`content-block`) | 3 alternating SEO rows, genuinely localized (Tyresö: "Trollbäcken och Tyresö Strand"; Sollentuna: "Edsviken till Rotebro") | Rows stack, image-first |
| 14 | **BlueCTA** (`blue-cta-`) | "Prata med en elektriker!" + single black Ring button | Band stacks |
| 15 | **VissteDuAtt** (`visste-du-att`) | Localized awareness essay ("Dolda elfel är en vanlig orsak till bostadsbränder?") | Dark card, long text |
| 16 | **CEBlock** (`ce-block`) | "Certifierad expertis för trygga elsystem i {ort}" + "Kan jag få 30% ROT-avdrag?" + services list + CTA pair ("Kostnadsfri **radgivning**" [sic, missing å] → /kontakt/; Ring) | Stack, 9:16 image |
| 17 | **Certificates** (`certificates`) | 6 partner logo cards (Elsäkerhetsverket, Skatteverket, …) | 2-up grid |
| 18 | **FooterSEO** (`footer-seo`) | "**Tyresö's bästa elektriker nära mig**" [sic, English genitive] + CTA pair ("Kostnadsfri **radgivning**" [sic] → /kontakt/; Ring) | Stack |
| 19 | Prefooter + Footer | Link columns, 5.0 badge (no count), contact info | Accordion columns |

**Total conversion asks per page (counted in `<main>`):** 6 links to /kontakt/ + 7 `tel:` links + 2 forms = **15 asks**, plus header "Gratis rådgivning" + mobile "Ring en expert" ≈ **17 competing asks**.

---

## Customer-flow walkthrough (Tyresö, mobile-first)

**0–5 s:** Arrives from SERP result "Elektriker i Tyresö - fast pris & snabb service". First screen: tiny "Elektriker Tyresö", big "Boka en pålitlig elektriker i Tyresö!", paragraph, two gradient buttons. **The promised "fast pris" appears nowhere in the page body** (verified: 4 occurrences in `<title>`/og/twitter/dc meta, **0 in `<main>`**) — the #1 price-anxiety question is never re-affirmed after the click. The form is not yet painted (client-side render; lab LCP 9–10 s risk).

**Scroll 1–3:** Metrics ("1000+ Nöjda kunder") → "Prata med en elektriker inom 60 sekunder!" (Ring only) → services grid. A caller-type visitor may convert at MainCTA — this is the healthiest path on the page. A form-type visitor has, so far, been offered: a button that leaves the page (/kontakt/), a late-rendering hero form, and a Ring button.

**Scroll 4–7:** Testimonials (real, but zero ort anchors — nothing says any job happened in Tyresö) → process → **MainContact form** (the strongest asset, correctly reachable by mid-page) → FAQ *after* the form.

**Scroll 8–19:** A 12-block tail where **every remaining "Kostnadsfri rådgivning" ask navigates to /kontakt/** — a second ~800 KB page load — instead of anchoring back to the form two screens up. The deeper a reader engages with the SEO content (the exact behavior MECLABS HealthSpire says predicts conversion), the more likely their eventual ask-click costs them a full extra page load on a slow stack.

**Decision moment:** The trust-seeking visitor (the Clarity "Contact → About Us" pattern) finds behörighet proof scattered: Elsäkerhetsverket appears as a logo (block 17), inside one FAQ answer (block 8, Sollentuna only), and in body copy — never as a checkable claim near the ask.

---

## What works (keep)

- **Genuinely unique programmatic copy.** Word counts vary 2 431–2 576; ContentBlock/VissteDuAtt/CEBlock name real local areas ("Trollbäcken och Tyresö Strand", "Edsviken till Rotebro"); FAQs differ per ort. This is far above typical doorway-page quality — preserve it (SEO substance rule).
- **MainContact at position 7 of 19** — the strongest converter is not buried at the very bottom.
- **VarProcess before the form** — the 4-step "Så funkar det" answers "vad händer när jag skickar in?" exactly where MECLABS anxiety-reduction wants it.
- **12 real Google reviews** with names and dates — candour-compliant social proof raw material.
- **Sollentuna's Elsäkerhetsverket FAQ** ("Kolla elföretaget") — precisely the proof Konsumentverket-minded Swedish customers seek; the best trust copy on the site, currently buried.
- **MainCTA "Prata med en elektriker inom 60 sekunder!"** — phone-first, single-ask, high-clarity block that matches urgent local intent (Unbounce: urgent/repair framing converts best in home services).
- **Localized services grid** — six real service links with ort-injected copy: good message-match bridging AND internal linking.
- The MapBlock as SEO internal-linking backbone (fine where it is, late).

---

## Findings

### GEO-01 · P0 · CTA routing: 6 of 8 non-phone asks navigate OFF-page to /kontakt/ instead of anchoring to the on-page form
Evidence: verified hrefs — hero, MikroCTA, MapBlock, CEBlock, FooterSEO "Kostnadsfri rådgivning/Kontakta oss" all point `https://ampy.se/kontakt/`, on a page that carries **two** forms of its own. Framework: MECLABS friction (needless extra step); Baymard (each added page load sheds users); site speed multiplies the cost (~800 KB/9–10 s-lab pages). The hero's PRIMARY button leaving the page while a form sits in the same hero is a self-inflicted attention leak (MECLABS attention ratio). **Mobile:** worst case — a deep-scrolled mobile reader is 15+ screens from the hero form; the tail CTAs trigger a full navigation instead of a smooth-scroll to `#main-contact`. Fix: retarget all of them to the MainContact anchor. Priority: 56 pages × 3 (hero/form) × 3 (high) = **504**.

### GEO-02 · P0 · Hero form is 100 % client-side rendered — no fields exist in HTML
Evidence: hero right column is `<div id="ampy-form-root" class="aof" data-endpoint="…supabase.co/functions/v1/hero-lead">` — empty; `formCard()` in inline JS builds every field. "Få kostnadsfri rådgivning!" occurs **0 times** in served markup (only URL-encoded inside the script). Consequences: (a) at 9–10 s lab LCP the form paints late or, on JS failure, never; (b) HYPOTES: this is the direct cause of the analytics finding "0 form starts recorded" — a custom-DOM form that GA4's enhanced measurement never sees; (c) SEO: the injected card contains a **second `<h1>`** ("Få kostnadsfri rådgivning!"), giving every geo page two H1s post-render (see GEO-05). Framework: NN/g progressive enhancement; Baymard form visibility. **Mobile:** the late-painting form is below the fold anyway, so the failure is silent. Fix: server-render at least the initial fields (or the whole card) and emit `form_start`/`form_submit` events. Priority: 56 × 3 × 3 = **504**.

### GEO-03 · P0 · Message-match break: SERP promise "fast pris" never appears on the page — and there is zero price content at all
Evidence: Tyresö `<title>` = "Elektriker i Tyresö - fast pris & snabb service"; body occurrences of "fast pris": **0**. Sollentuna's meta promises "fasta priser" — same absence. Actual paid search terms are price-loaded ("byta elcentral pris", "byta proppskåp"). Framework: Google message match (ad/SERP → H1 → first screen mandatory); Byggahus research — final-price surprise is the #1 Swedish homeowner fear; MECLABS value clarity (v). The page answers "who/where" but never "vad kostar det", the visitor's second question. **Mobile:** no price signal in any of the first 5 screens. Fix: a compact price-anchor element in/under the hero ("Fast pris i offerten – 30 % ROT dras direkt på fakturan"; real job-price examples require owner data → [GAP]). Priority: 56 × 3 × 2 = **336**.

### GEO-04 · P0 (candour) · "1000+ Nöjda kunder" asserted + internal proof contradiction + "5.0" unanchored ×6
Evidence (quoted): Metrics card 1: "**1000+** Nöjda kunder — Över tusen genomförda installationer är vårt absolut starkaste kvalitetsbevis." Business-context ban: "1000+ kunder" may not be asserted unless owner-confirmed current. Two blocks later MainContact asserts "**3 000+ genomförda installationer om året**" — if 3 000+/year is true, "över tusen genomförda installationer" as the *lifetime* "starkaste kvalitetsbevis" is internally incoherent; one of the two numbers must be wrong or mis-framed (internal-contradiction flag per canon; no external re-check needed). "5.0"/"5 av 5 · Betyg på Google" appears ≥6× per page (header, hero, MainCTA, testimonials badge, MainContact pane, footer) — never once with a review count. Tyresö meta description adds "över 25 års erfarenhet", which a reader parses as company age; the on-page card carefully says "Vår **samlade** yrkeskunskap" — the meta drops the qualifier. Framework: candour gate; Cialdini social proof only works when verifiable — an unanchored 5.0 reads as fabricated to skeptical 45-year-olds. Fix: owner-confirm all three numbers; anchor rating as "5,0 av 5 · N omdömen på Google" (live count); reconcile installations claims to ONE framing. Priority: 56 × 2 × 2 = **224**.

### GEO-05 · P1 · H1 semantics inverted, then duplicated
Evidence: `<h1 class="hero_2__section-subheading">Elektriker Tyresö</h1>` is the *small eyebrow*; the visually dominant line is an `<h2>`. Post-JS, `formCard()` injects a second `<h1>Få kostnadsfri rådgivning!</h1>`. Rendered DOM therefore has two H1s, and the second is a generic CTA string identical across all 56 pages. Framework: SEO semantic hierarchy; NN/g visual hierarchy = information hierarchy. **Mobile:** the tiny H1 is the first text after breadcrumbs — visually a label, not an answer. Fix: make the big headline the H1 (keyword-bearing: "Elektriker i Tyresö – …"), demote the eyebrow, change the form title to a `<p>`/`<h3>`. Priority: 56 × 3 × 1 = **168**.

### GEO-06 · P1 · Zero ort-anchored proof on a local-intent page; team bios sell the wrong vertical
Evidence: all 12 testimonials are ort-less ("Snabb hjälp när elcentralen strulade…" — could be anywhere); TeamSection headline claims "Möt våra certifierade elektriker **i Tyresö**" but the first bio leads with "komplexa batterilösningar… stödtjänster och ö-drift… SAJ HS3 och Dyness Stack 100" — battery/product language on a *service*-intent page (commercial priority is service > laddbox > battery; the headline's "i Tyresö" claim is itself a candour stretch since the same 5 bios appear on every ort page). Framework: JTBD (the job is "someone comes to MY house"); Cialdini similarity — "grannar" proof works when it demonstrably IS grannar; the testimonials block literally asks "Vad säger dina **grannar**…" and then shows none. Fix: if real reviews carry orts, surface them and rotate ort-matched reviews first ([GAP]: owner/GBP export); reorder team so service electricians (Magnus, Edvin) lead; soften headline to "Möt våra certifierade elektriker". Priority: 56 × 2 × 2 = **224**.

### GEO-07 · P1 · ~17 competing conversion asks; hero alone runs 3 simultaneous asks
Evidence: counted 6 /kontakt/ links + 7 tel: links + 2 forms in `<main>`; hero presents form + 2 buttons at once. Framework: MECLABS attention ratio; Hick's law. The duplicate CTA bands (MikroCTA at #10, BlueCTA at #14, CEBlock CTA pair at #16, FooterSEO pair at #18 — four near-identical asks in the tail) add length without new information. **Mobile:** four consecutive tail screens are CTA bands. Fix: one primary ask per funnel moment — hero (call + form), one mid-page phone band, form, one closing band anchored to the form; delete or merge the rest (re-sequence, don't delete SEO copy). Priority: 56 × 2 × 2 = **224**.

### GEO-08 · P1 · FAQ sits AFTER the MainContact form; the best trust answer is buried
Evidence: live order …VarProcess(6) → MainContact(7) → FAQ(8)… Objection-handling placed after the ask contradicts MECLABS sequencing (answer anxiety before the conversion moment); Sollentuna's Elsäkerhetsverket "Kolla elföretaget" answer — the single strongest trust proof for the Swedish buyer — sits mid-accordion below the form. Fix: FAQ (or at least 2–3 top objections) above MainContact; add an explicit "Kontrollera oss hos Elsäkerhetsverket" trust line with org-check reference near the form ([GAP]: exact registration entry to cite). Priority: 56 × 2 × 2 = **224**.

### GEO-09 · P2 · Page weight: ~855 KB of HTML alone, 19 sections, inline mega-CSS/JS, data-URI images
Evidence: fetched Tyresö document = 877 062 bytes before images/fonts; form JS ships URL-encoded inline; header Google logo is a base64 PNG inside inline SVG; Splide + map assets load regardless of scroll depth. Correlates with the 9–10 s lab LCP flag. Framework: CWV/LCP as conversion precondition (speed risk already named in the paid-traffic diagnosis). **Mobile:** worst on 4G. Fix direction: extract/dedupe inline CSS-JS, lazy-load below-fold sections, SSR the form (pairs with GEO-02). Priority: 56 × 3 × 1 = **168** (site-wide fix, larger true reach).

### GEO-10 · P2 · Copy defects shipped ×56: English genitive + missing diacritics
Evidence (quoted): FooterSEO H2 "**Tyresö's** bästa elektriker nära mig" / "**Sollentuna's** bästa elektriker nära mig" — Swedish genitive takes no apostrophe (Tyresös); "nära mig" is a first-person SERP keyword pasted into second-person copy — reads machine-written to exactly the 35–65 audience the brand must convince it is a careful tradesperson. CEBlock + FooterSEO buttons: "Kostnadsfri **radgivning**" (missing å) — twice per page, 56 pages. Framework: credibility heuristics (NN/g) — surface sloppiness is read as workmanship sloppiness in trades. Note: "bästa elektriker" superlative is ALLOWED per owner directive (2026-07-18) — the apostrophe and å are the defects, not the claim. Priority: 56 × 1 × 2 = **112**.

### GEO-11 · P2 · Promise inconsistency: "inom 60 sekunder" vs "inom 24 timmar"
Evidence: MainCTA "Prata med en elektriker inom 60 sekunder!" (phone path) vs MainContact pane "Vi ringer dig inom 24 timmar" (form path). Both can be true, but nothing on the page explains the difference; a skeptic reads the 60-second line as hype (candour risk — needs owner confirmation it reflects real answer times). Fix: frame explicitly — "Ring nu – svar direkt" vs "Skicka formuläret – vi ringer inom 24 timmar" — which also becomes a genuine reason to prefer calling. Priority: 56 × 2 × 1 = **112**.

### GEO-12 · P3 · Data/asset hygiene
(a) block-map.json omits the `services-loop` block on all 56 pages — downstream analyses using block-map will mis-sequence this template. (b) "Ladda fler tjänster" is `href="#"` — verify JS load-more works, else it's a dead control. (c) The /elektriker/ pillar (Hero-1, no aof form, "Elektriker för privatpersoner över hela Sverige!") is a different animal and should be audited with the pillar templates, not this one.

---

## Recommended sequence (wireframe)

Principle: keep every SEO block (re-sequence, never delete); one ask per moment; all form CTAs anchor to `#main-contact`; proof before ask; price signal above the fold.

| # | Block | Why here | New/existing/modified |
|---|---|---|---|
| 1 | **Hero_2** — H1 = "Elektriker i {ort} – fast pris i offerten & behörig elfirma"; single primary CTA on mobile (Ring), secondary = "Till formuläret" anchor; **server-rendered** form card desktop-right; anchored rating "5,0 · N omdömen" | Message match with SERP title incl. "fast pris"; kills 3-way ask; fixes H1 (GEO-01/02/03/05) | Modified |
| 2 | **Trust strip (compact)** — "Registrerad hos Elsäkerhetsverket · 30 % ROT direkt på fakturan · Vi ringer inom 24 h" | The three checkable claims the Swedish buyer looks for, in screen 2 (Konsumentverket/Byggahus proof pattern) | **New** (thin band, reuses Certificates assets) |
| 3 | **Metrics** — candour-fixed numbers (owner-confirmed; one installations framing) | Scale proof early, now believable | Modified |
| 4 | **Services grid** (`services-loop`) | "Do they do MY job?" answered before any deep scroll; internal links preserved | Existing |
| 5 | **MainCTA** — "Ring nu – prata med en elektriker direkt" (reconciled promise) | The phone path peaks here for urgent visitors | Modified |
| 6 | **Testimonials** — ort-tagged reviews first where real ones exist [GAP] | Proof directly before the ask sequence; "grannar" claim made honest | Modified |
| 7 | **VarProcess** | Anxiety reduction immediately pre-form | Existing |
| 8 | **FAQ** — Elsäkerhetsverket "Kolla elföretaget" answer promoted to slot 1 on all pages | Objections answered BEFORE the form (GEO-08) | Modified (moved up) |
| 9 | **MainContact** (`#main-contact`) — target of every form CTA on the page | The proven strongest asset, now the single form destination | Modified (anchor id) |
| 10 | **ROT-block** | Economic reinforcement right after the ask for hesitators | Existing |
| 11 | **TeamSection** — service-first bio order; headline without false ort claim | E-E-A-T without vertical mismatch (GEO-06) | Modified |
| 12 | **ContentBlock** (3 localized rows) | SEO meat intact, mid-tail | Existing |
| 13 | **VissteDuAtt** | Editorial/awareness depth preserved | Existing |
| 14 | **CEBlock** — CTA pair retargeted to `#main-contact`; "radgivning" typo fixed | Long-form SEO + a correctly-routed ask | Modified |
| 15 | **MapBlock** | Internal-linking backbone, late where it can't bleed mid-funnel attention | Existing |
| 16 | **Certificates** | Authority close | Existing |
| 17 | **FooterSEO** — "Tyresös bästa elektriker" (fixed genitive), CTA → `#main-contact` + Ring | Final ask, correctly spelled and routed | Modified |

Removed as standalone: **MikroCTA** and **BlueCTA** (merged — their copy lives on in blocks 5 and 17; two of four duplicate tail CTA bands cut per MECLABS attention ratio). No SEO text is deleted anywhere.

---

## Test hypotheses (top 3, A/B-phrased)

1. **HYPOTES (anchor vs navigate):** Retargeting all "Kostnadsfri rådgivning" CTAs from `/kontakt/` to a smooth-scroll `#main-contact` anchor on geo pages will increase form submissions per session vs control, because it removes a full ~800 KB page load from the conversion path (MECLABS friction). Primary metric: form submits/session; guardrail: phone clicks.
2. **HYPOTES (SSR form + events):** Server-rendering the Hero_2 form fields (and firing `form_start`) will increase measured form starts from ~0 and raise hero-form submissions vs the JS-injected control, because the form becomes visible at first paint and measurable at all (Baymard visibility; fixes the "0 form starts" blind spot — this test simultaneously repairs instrumentation).
3. **HYPOTES (price anchor / message match):** Adding a hero-adjacent "fast pris"-substantiating element (fixed-price promise + example job prices after ROT, owner-supplied [GAP]) will lift combined call+form conversion on geo pages entered via price-modified queries, because it closes the SERP-promise gap and the #1 Swedish homeowner anxiety (Google message match; Byggahus price-surprise research).

Runner-up: FAQ-above-form vs below-form (GEO-08) as a cheap sequencing test.

---

*Verification note (anti-theatre): both URLs fetched live 2026-08-02; block order read from raw `<section>` classes; CTA hrefs, form mount (`#ampy-form-root` + Supabase endpoint), double-H1 injection, "fast pris"=0-in-body, and both typos verified in saved HTML (`scratchpad/tyreso.html`, 877 KB). Mobile behaviors are derived from the block inventory + CSS breakpoints in the fetched document, not from device rendering — no mobile screenshots were taken in this pass.*
