# Team member pages (E-E-A-T profiles) + TeamSection usage + /om-oss/ trust hub

URLs analyzed (live fetch 2026-08-02 + raw snapshots in `data/pages/`):
- https://ampy.se/om-oss/edvin-gustavsson/ (full fetch; note: assignment said `/team/edvin-eriksson/` — that slug does not exist; real slugs verified from block-map)
- https://ampy.se/om-oss/julius-callahan/ (snapshot body extract)
- All 6 profile snapshots checked for H-tags/title/meta/schema: edvin-gustavsson, felix-calmano, julius-callahan, magnus-harald-metsniin, mio-bergenstrale, yousef-lundqvist
- https://ampy.se/om-oss/ (live fetch)
- TeamSection markup extracted from `elektriker.html` and `batterilagring.html` snapshots

**Pages using this template:** 6 team-member pages. **TeamSection block:** 85 pages (56 elektriker-i, 16 ev-product, 10 battery-product, 3 pillars: /elektriker/, /laddbox/, /batterilagring/). **/om-oss/:** 1 page. Total surface of this deep-dive: **92 pages.**

---

## Current block sequence (verified from block-map + markup)

### Team member page (identical on all 6)
1. **Header** — global mega-menu + "Gratis rådgivning" teal CTA. Desktop: visible CTA + "Ring en expert 5.0". Mobile: collapses to hamburger → the only CTAs on the page disappear behind a tap.
2. **AlternativHero** (`laddbox-hero` reuse) — breadcrumbs ("Hem / Om oss / Edvin Gustavsson") → name → job title ("Senior Elektriker, Arbetsledare & Kvalitetsansvarig") → intro paragraph → photo right (1000×1500 webp, e.g. `edvin-gustavsson.webp`). Dark navy card, no CTA, no rating, no credential chips. Mobile: stacks, photo below text.
3. **Stacked content cards** — Nyckelfakta (mint bg, "●" text bullets) → "About Edvin" (English heading) → Expertis & systemkompetens → Erfarenhet → Certifieringar → Arbetssätt → big italic quote ("En bra installation handlar inte bara om att det fungerar idag, utan att det är byggt rätt för framtiden."). All single-column; mobile identical, long scroll.
4. **FAQ accordion** — "Vanliga frågor om Edvin", 4 person-specific Q&As.
5. **Prefooter + Footer** — generic link farm.

**Verified markup facts (all 6 pages):** zero `<h1>` (the name renders as `h3`); section headings are `h3`, only the FAQ heading is `h2`. `<title>` = bare name ("Edvin Gustavsson"), **no meta description**. `schema.org Person` exists but `name` = first name only ("Edvin"), with `jobTitle` + `worksFor` but no `image`, no `sameAs`, no `knowsAbout`, no `hasCredential`; page is not typed `ProfilePage`. Body contains **0 tel: links, 0 CTA buttons, 0 forms**. Body DOES contain 5 contextual service links (smarta-hem, batterilagring, laddbox, lastbalansering, elektriker) + breadcrumb to /om-oss/.

### TeamSection block (85 pages)
"Möt våra auktoriserade elektriker" H2 (per-vertical customized on battery pages: "Specialister på solcellsbatterier – Möt teamet bakom din installation!") → Splide slider of cards: photo + **first name only** + ~90-word bio (real credentials in prose: "ECY-certifierad", "17 års erfarenhet", "Bas P/U", KNX/Plejd/SAJ HS3/Dyness Stack100). Julius (medgrundare, non-electrician) correctly excluded from the elektriker slider — candour holds. **Cards do not link anywhere.** Position in sequence: slot 14/22 on elektriker-i, 11/16 on ev-product, 12/17 on battery-product, 13–15/21–23 on pillars — always deep below FAQ and usually below MainContact. Mobile: 1-up swipe slider at the bottom of a very long page.

### /om-oss/ (the page trust-seekers actually visit)
Header → **Hero-1** (H1 "Sveriges snabbast växande elfirma, byggd för kvalitet." + CTA pair + 5.0 row) → **ContentBlock** (3 rows: "Nya generationens elfirma" / "Trygg el, utan krångel" / "Kvalitet du ser direkt") → **AboutMetrics + Metrics** ("Nöjda kunder" / "Erfarenhet i branschen" / "Personer i teamet" — the number-less variant) → **VisualCTA** ("Ditt hem, vår spetskompetens" + Kontakta oss) → **MainContact** → Prefooter. **No TeamSection. No Testimonials. No Certificates. No links to any of the 6 profile pages.**

---

## The orphan proof (hard verification)

Grep across all 38 HTML snapshots: **the only `href` to each profile page anywhere on the site is its own canonical self-reference.** Every other "mention" of e.g. `edvin-gustavsson` is the image filename in the TeamSection slider. The 6 E-E-A-T pages are unreachable by any click path — not from /om-oss/, not from the TeamSection on 85 pages, not from the header/footer. They exist only for the sitemap.

---

## Customer-flow walkthrough (35–65 yo homeowner, mobile)

**How would they even get here?** They can't — no link exists (see above). The realistic trust-seeking journey today is the one Clarity recorded: a 47s paid visitor going Contact → **About Us**. That visitor lands on /om-oss/ and gets: a growth superlative headline, three prose blocks about "AI och IT som minskar friktion" (speaks the founder's language, not a 55-year-old villaägare's), metric cards with **no numbers**, and — critically — **no faces, no reviews, no certificates**. The material that would have converted their anxiety (Edvin's full auktorisation, Magnus's 17 years, ECY, Elsäkerhetsverket) sits on six pages they cannot reach.

**If they did land on a profile** (e.g. future SERP for a name): first 5 seconds — dark hero, name, credible title, real photo: good. Scroll — genuinely strong, specific, honest content (regelverk, för-/färdiganmälningar, egenkontroller — exactly the "serious Swedish customer" proof per Konsumentverket/Byggahus research). Decision moment — nothing. No phone number in the body, no "boka rådgivning", no path to a service page beyond a few inline text links. On mobile the header CTA is behind the hamburger, so the page is a **conversion dead end**: maximum trust generated, zero harvest.

---

## What works (keep)

1. **The content itself is the best E-E-A-T raw material on the site.** Real, specific, verifiable credentials (full auktorisation, ECY, Bas P/U), named systems (KNX, Plejd, Shelly, SAJ HS3, Dyness Stack100), per-person quotes and FAQs, honest role descriptions. Nothing invented; candour-clean.
2. **Real photos**, high-res, consistent format — reusable as trust assets everywhere.
3. **Contextual internal links inside bios** already point at money pages (batterilagring, laddbox, lastbalansering) — the outbound half of the loop exists.
4. **Person schema exists at all** — rare for an elfirma; it just needs completion.
5. **TeamSection per-vertical H2 customization** (battery pages) — message-match done right.
6. **Julius excluded from the "auktoriserade elektriker" slider** — the candour gate held where it mattered.
7. **Per-person FAQ** — ready-made `FAQPage` schema candidates and long-tail answer content.

---

## Findings

**TEAM-01 · P1 · Profile pages are total internal-link orphans.**
Zero inbound hrefs site-wide (verified grep, all 38 snapshots); TeamSection cards on 85 pages show the person but never link; /om-oss/ never mentions them. Evidence: Google's quality-rater guidance treats discoverable author/expert pages as E-E-A-T support — stranded pages support nothing; NN/g: users can't use what they can't reach. Mobile: identical (no path at any breakpoint). This single defect neutralizes ~6 000 words of the site's most credible trust content.

**TEAM-02 · P1 · Profile pages close no loop — zero CTA, zero tel:, zero form in body.**
The site has exactly two conversions; this template offers neither. MECLABS heuristic: these pages maximize *m* (motivation via trust) then supply no channel — the visitor's momentum dies. The ev-product template already contains the fix pattern: the "Rådfråga vår expert!" card (photo + phone + rating). Mobile note: with the header CTA hidden in the hamburger, mobile visitors see literally no action anywhere on the page.

**TEAM-03 · P1 (SEO/E-E-A-T machine layer) · No H1, no meta description, bare `<title>`, incomplete Person schema.**
All 6 pages: name is an `h3`, no `h1` exists (block-map `h1: []` + markup verified); `<title>` lacks role/brand ("Edvin Gustavsson" vs "Edvin Gustavsson – Auktoriserad elektriker | Ampy"); Person schema `name:"Edvin"` (first name only), no `image`/`sameAs`/`knowsAbout`/`hasCredential`, no `ProfilePage` type, FAQ not marked up. These pages should be citable author entities for the article byline system ("Faktagranskad av") — currently they are semantically half-built. SEO substance itself is good; this is packaging.

**TEAM-04 · P2 · "About {name}" heading in English on all 6 Swedish pages** + "●" text-glyph bullets in Nyckelfakta. Swedish-first violation (voice canon); reads as template leftover to exactly the 35–65 audience that distrusts sloppiness. One-string fix ("Om Edvin"). Mobile: same.

**TEAM-05 · P2 · /om-oss/ is a trust hub with the least trust on the site.**
The verified sequence contains no TeamSection, no Testimonials, no Certificates — while 85 service/product pages carry the team and every service page carries reviews. The Clarity-recorded trust-seeking behavior (Contact → About Us) hits this page. Additional defects on the page as fetched: (a) metric cards render heading-only ("Nöjda kunder / Erfarenhet i branschen / Personer i teamet") — prose beneath but no anchored figures, reading as broken; (b) internal claim tension: "Över tusen genomförda installationer" (metrics prose) vs "3 000+ genomförda installationer om året" (MainContact photo pane) — flag to owner for one canonical, ownable number (candour gate: internal contradiction); (c) copy register is founder-facing ("Lägg till AI och IT som minskar friktion") not villaägare-facing; (d) "Sveriges snabbast växande elfirma" — strong superlative is allowed per owner directive, but keep only if not demonstrably false.

**TEAM-06 · P2 · TeamSection is buried after the ask on all 85 pages.**
Slot 14/22 (elektriker-i), 11/16 (ev-product), 12/17 (battery-product) — always below FAQ, usually below MainContact. Cialdini (authority before commitment) + the site-wide inverted-proof-architecture finding: the faces that de-risk the decision appear after the form asked for it. Mobile: on a 22-block page the slider is effectively unreachable (deep-scroll ~17/32 paid sessions per GA4 — HYPOTES that few reach slot 14; verify with Clarity scroll maps).

**TEAM-07 · P3 · TeamSection candour + hygiene nits.**
(a) Mio's slider bio: "funktioner som stödtjänster och ö-drift … högsta möjliga avkastning" — the revenue framing must survive the stödtjänster=0 / effektavgift=0 gate; reframe toward capability, not yield. (b) Leftover developer comment JavaScript ships inline in the team block ("// Find your slider - replace with your element ID"). (c) Cards show first names only — fine socially, but with no link and no surname the person is unverifiable (Elsäkerhetsverket check impossible).

**TEAM-08 · P3 · Profile hero carries no credential anchor.**
The dark AlternativHero shows name + title only; the certifications that matter (Auktoriserad, ECY) sit 3–4 scrolls down. For a trust page the proof should be in the first viewport (NN/g: users judge credibility in the first seconds). Mobile: photo drops below the fold, further delaying the "real person" signal.

### Priority arithmetic
- TEAM-01: 85 pages (link source) × mid-funnel 2 × high 3 = **510**
- TEAM-06: 85 × 2 × 2 = **340**
- TEAM-02: 6 × low-funnel 1 × high 3 = 18 — but multiplier understates it: these are terminal trust pages feeding the 2 conversions; treat as P1 paired with TEAM-01 (ship together, trivial effort)
- TEAM-05: 1 page × mid 2 × high 3 = 6 — but /om-oss/ is the observed trust-seeker destination (Clarity); weight up to P2-early
- TEAM-03: 6 × 1 × 2 = 12 (compounding via article bylines)
- TEAM-04/07/08: polish batch, do in the same edit session

---

## Recommended sequence (wireframe) — Team member page

| # | Block | Why here | New/existing/modified |
|---|---|---|---|
| 1 | Header | global | existing |
| 2 | **AlternativHero +credential chips** — H1 = "{Fullt namn} – {roll}", chips: Auktoriserad · ECY · {X} års erfarenhet; photo right | proof in first viewport (TEAM-08); real H1 (TEAM-03) | modified |
| 3 | Nyckelfakta card (real list markup, "Om {namn}" in Swedish) | keep the scannable summary | modified (TEAM-04) |
| 4 | **Expert CTA card** — reuse ev-product "Rådfråga vår expert!" pattern: photo + "Vill du bli uppringd? {Namn}s team ringer dig inom 24 timmar" + Ring 010-265 79 79 + link to form | closes the loop at peak trust (TEAM-02); phone-first per commercial priority | **new placement** (existing pattern) |
| 5 | Erfarenhet / Om / Expertis / Arbetssätt cards | the E-E-A-T meat — keep verbatim | existing |
| 6 | Certifieringar + **Elsäkerhetsverket-kontroll link** ("Kontrollera själv i Elsäkerhetsverkets register") | the exact proof Konsumentverket-minded Swedes seek; costless candour flex | modified |
| 7 | Quote (italic) | humanizing beat before the ask | existing |
| 8 | **"Jobb {namn} ofta gör"** — 3–4 service-page links as cards (elcentral, smarta hem, laddbox …) | routes trust into money pages; formalizes the inline links that already exist | new (light) |
| 9 | FAQ "Vanliga frågor om {namn}" + FAQPage schema | keep; add markup | modified |
| 10 | MikroCTA (existing band: Kostnadsfri rådgivning + Ring) | second close for scrollers | existing block, new placement |
| 11 | **TeamSection "Fler i teamet"** — cards LINK to siblings | keeps trust-seekers in the trust loop | modified |
| 12 | Prefooter/Footer | global | existing |

Plus template-level: meta title "{Namn} – {Roll} | Ampy", meta description from intro paragraph, Person schema completed (full name, image, jobTitle, hasCredential ECY/auktorisation, knowsAbout, worksFor) + `ProfilePage` type; article bylines ("Skriven/Faktagranskad av") should link here — the flywheel: article → expert profile → call.

## Recommended sequence — /om-oss/ (companion fix)

| # | Block | Why here | New/existing/modified |
|---|---|---|---|
| 1 | Hero-1 (headline re-aimed at the customer: quality/trygghet, not growth/AI) | message match with trust-seeking intent | modified copy |
| 2 | **TeamSection with linked cards** (full names) | the #1 thing an "About Us" visitor came for | existing block, new here |
| 3 | Metrics with owner-anchored numbers (resolve 1000+ vs 3000+/år contradiction first) | scale proof, candour-clean | modified |
| 4 | ContentBlock (story, register shifted to villaägare) | narrative depth, SEO preserved | modified copy |
| 5 | **Testimonials** | real reviews on the trust page | existing block, new here |
| 6 | **Certificates** | institutional proof (Elsäkerhetsverket, ID06, Trygg Hansa) | existing block, new here |
| 7 | VarProcess | "what happens when I call" — anxiety reducer | existing block, new here |
| 8 | MainContact | the close, now earned | existing |

**TeamSection on the 85 pages:** (a) make cards link to profiles (surname added); (b) move above MainContact/FAQ on elektriker-i template (proof before ask — coordinate with the geo-template deep-dive); (c) strip the dev-comment JS; (d) soften Mio's stödtjänster yield claim.

---

## Test hypotheses (top 3, A/B)

1. **HYPOTES (loop-closing):** Adding the expert phone-CTA card + MikroCTA to the 6 profile pages and linking TeamSection cards to them will increase phone-click conversions per trust-seeking session (sessions touching om-oss/profile pages) vs. control. Primary metric: tel: clicks; secondary: profile→service-page continuation rate.
2. **HYPOTES (proof-before-ask):** On the elektriker-i template, moving TeamSection to directly before MainContact (from slot 14 to ~slot 7) increases form submits per session vs. current order, per MECLABS sequencing (HealthSpire: order, not length) — measurable on the 56-page geo set with page-level bucketing.
3. **HYPOTES (trust hub):** The rebuilt /om-oss/ (team + testimonials + certificates + anchored metrics) increases the share of om-oss sessions that proceed to a conversion event (call click or form submit within the session) vs. the current version — directly testing the Clarity "Contact → About Us" trust-seeking pattern.
