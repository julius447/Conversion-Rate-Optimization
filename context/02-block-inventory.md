# Ampy Block Inventory (distilled from Bricks JSON, provided by owner 2026-08-02)

Every block below is a reusable Bricks section/component. CSS class prefixes are the fingerprints used to detect them in rendered HTML. This is the canonical map for the whole CRO analysis.

---

## 1. Hero_2 — `hero_2` / `.aof` (SERVICE-PAGE HERO + FORM)
The dominant hero on service pages (elservice/*, elektriker/*, elinstallation/*, laddbox geo, elektriker-för-X).
- Left column: breadcrumbs → **H1 = small green gradient eyebrow** (e.g. "Byta elcentral") → **H2 = the big white/green gradient headline** (e.g. "Ny elcentral installerad med 30% ROT-avdrag") → paragraph → TWO CTAs ("Kostnadsfri rådgivning" green-gradient + "Ring 010-265 79 79" blue-gradient) → Google 5.0 ★★★★★ row (teal stars, links to GBP).
- Right column: **the new `.aof` form card** (navy/aurora gradient, max 450px): "Få kostnadsfri rådgivning!" / "Vår behöriga elektriker återkommer via telefon!" → kundtyp toggle (Privat/BRF/Företag) → "Vad gäller arbetet?" select (per-page prefilled/locked via URL resolver) → Namn → Telefonnummer + E-post → Adress + Postnummer → "Fler detaljer (valfritt)" disclosure (beskrivning, tidsram, bilder, org fields) → GDPR checkbox → "Boka rådgivning" gradient submit → posts multipart to n8n → redirect /thank-you. Full validation, honeypot, a11y live regions.
- KNOWN TENSIONS: H1 is the *small* eyebrow (SEO oddity); two competing CTAs + form = 3 simultaneous asks; 5.0 rating unanchored (no count, candour risk); dark navy card on dark navy page bg; form asks address+postnr up front.

## 2. Hero-1 — `hero-1` (HOMEPAGE / PILLAR HERO)
Floating white banner card on #f5f9ff: H1 green-gradient (ACF) → paragraph → CTA pair ("Kostnadsfri radgivning" green-gradient w/ arrow + "Ring …" light-blue w/ pulsing phone chip — the upgraded CTA library buttons) → Google rating trust row → masked hero image right/bottom. Mobile: stacked, image absolute bottom.
- Homepage only (condition `post_url == site_url`): the **"Din elektriker för hela hemmet" 3-card mini-menu** (`ampy-elfirma`): Elservice / Laddbox / Batterilagring square photo cards with "Läs mer" sky-blue pill CTAs.

## 3. Alternativ hero — `laddbox-hero` (COMPACT DARK HERO)
Dark navy rounded card: breadcrumbs absolute top-left, H1 white→green gradient, paragraph, two decorative waves. No CTA, no form, no image. Used on product-listing/laddbox pillar & team pages (as `laddbox-hero` classes reused). Owner wants this ON TOP of lead magnets (e.g. Energikalkylatorn).

## 4. Main contact — `main-contact` (GLOBAL FORM SECTION)
Two-pane card. Left photo pane (dark overlay photo): white Ampy logo, quote "Från start till mål levererades en service i världsklass.", ★★★★★ gold + "{rating} av 5 · Betyg på Google", "3 000+ genomförda installationer om året", 3 steps (Skicka in dina uppgifter → Vi ringer dig inom 24 timmar → Kostnadsfri rådgivning av elektriker). Right form pane: "Få en kostnadsfri rådgivning" (gradient last word) → sub → Förnamn/Efternamn/E-post/Telefon (2-col) → Adress (Google Places autocomplete + manual fallback) → Meddelande (optional) → teal gradient pill "Gratis rådgivning" → integritetspolicy line. Native Bricks form → n8n webhook → /thank-you. Full validation/E.164 phone gate.
- This is the strongest conversion asset on the site. Used near page bottoms.

## 5. Main CTA — `main-cta-` (MID/LOW-PAGE CTA, updated version)
White card: trust row (Google G + "**5.0** på Google" + 5 gold stars) → teal/blue gradient H2 (ACF) → paragraph → **Ring CTA only** (library btn-ring w/ white pulsing phone chip) → team image with wave overlay right. Mobile: centered stack.

## 6. Mikro_CTA — `mikro_cta` (IMAGE-BACKED CTA BAND)
Dark photo bg (soft-light blend) rounded card: white H2 (ACF) → paragraph → CTA pair (Kostnadsfri rådgivning + Ring). 

## 7. Blue CTA — `blue-cta-` (LIGHT-BLUE PHONE BAND)
Cyan/blue gradient card w/ faint logos bg: H2 **underlined** dark text (ACF) → paragraph → single BLACK "Ring …" button. Phone-first CTA band.

## 8. Content block — `content-block` (SEO ALTERNATING ROWS)
3 × alternating image/text rows (H2 + long paragraph, ACF). Pure SEO/informational. ~550–620px images. This is the main "SEO meat" block on service/product pages.

## 9. Testimonials — `ampy-testimonials` (V1 LOCKED)
"Vad säger dina grannar om Ampy?" / "Riktiga omdömen från riktiga jobb." → Splide slider of dark navy-gradient cards (quote glyph, Google icon, text, name, mint stars, month/year) → 4 growing-dot nav → Google badge "X av 5 · Betyg på Google" (gold stars, links GBP). 12 real Google reviews, CPT-driven, shuffled.

## 10. FAQ — `faq-` (ACCORDION + IMAGE)
"Vanliga frågor" H2 → ACF-driven accordion (55% width) + image (45%). On gradient mint/blue container on some pages; article version has no image. H3 questions.

## 11. Vår process — `our-process` (4-STEP HOW IT WORKS)
H2 (ACF) + sub → 4 icon-boxes: 1. (phone icon) → 2. (edit icon) → 3. (file-check) → 4. (flash). Numbered headings + text. Light, clean.

## 12. ROT block — `rot` (ROT 30% EXPLAINER)
White card w/ blue overlay bg: H2 (blue, "Sänk kostnaden … 30% rot-avdrag") → 3 icon items (ACF) → "Läs mer om ROT-avdrag" cyan button. Twin: **Hemförsäkring/home-insurance** variant with phone CTA instead.

## 13. Grön teknik block — `gron-teknik` (GRÖN TEKNIK EXPLAINER)
Same pattern: H2 gradient → 3 process items → "Läs mer om Grön Teknik-avdrag" mint button. Used on product pages (laddbox 50%, battery 50%).

## 14. Visste du att — `visste-du-att` (AWARENESS/EDITORIAL BAND)
Dark navy #010328 card: "Visste du att.." H2 → ACF sub-heading + text → swinging lightbulb image absolute right. (Redesigned version exists per memory: killed absolute bulb/4s swing → stacked; but live block JSON here still has swing animation.)

## 15. Certificates — `certificates` (PARTNER LOGO WALL)
Navy→blue gradient full-bleed: "Certifikat och partners" + paragraph (left) → 6 white logo cards (Elsäkerhetsverket, Skatteverket, Naturvårdsverket, ID06, Trygg Hansa, Rexel) each linking out. Bg overlay wave image.

## 16. Footer SEO — `footer-seo` (BOTTOM SEO + CTA)
White section: H2 (ACF) → text (max 50%) → CTA pair (Kostnadsfri rådgivning + Ring) → large masked image bottom-right. Last block before prefooter on many pages.

## 17. Team section — `team` (ELECTRICIAN SLIDER)
H2 (ACF, gradient last words) on white floating card bg → Splide slider of team-member cards (photo ≤500px, name 26px, bio) 3-up/2-up/1-up. E-E-A-T + trust.

## 18. Team member page (E-E-A-T profile)
laddbox-hero style dark hero (name + job title + photo right) → stacked cards: short bio/key facts (mint bg) → Erfarenhet → About → Certifieringar (cyan bg) → Expertis & systemkompetens (cyan bg) → Arbetssätt → Quote (big italic) → FAQ "Vanliga frågor om {name}".

## 19. Article template
Breadcrumbs → dark hero (featured image overlay, H1 60%, excerpt) → editorial byline row (3 avatars: Skriven/Redigerad/Faktagranskad av + "Verifierad av expert" green pill + Uppdaterad date + reading time) → divider → 2-col: article (65%: "Snabbt svar" summary card w/ green left stripe → post content w/ full typographic system, markdown tables, pull quotes, pro tips, story boxes) + sticky TOC (30%, collapsible, scroll-spy) → FAQ accordion → review CTA card ("Tyckte du att artikeln var hjälpsam?" → Lämna ett omdöme på Google + 5 green stars + rating text) → share/print row → "Populära artiklar" 3-card grid.

## 20. Nyheter/artiklar block — `news` (ARTICLE CARDS ON LANDING PAGES)
"Nyheter och artiklar!" H2 → 3 post cards (date pill, image, title, excerpt 30 words, "Läs artikel" outline button). Internal linking + freshness.

## 21. Maps — `map` (GEO INTERNAL-LINKING BLOCK, 5 variants)
"Vi finns där du finns" H2 + ACF text → grid of 20 ort-buttons (per CPT: elektriker-i / eljour-i / laddbox-i / elinstallation-i / global-random) → dark navy sub-card "Osäker ifall vi finns där du bor?" + Kontakta oss button → Sweden map image right (desktop) / dot-map (mobile).

## 22. Metrics — `metrics` (3 NUMBER CARDS)
3 cards on bg image: big number (ACF), heading, text. About-us variant `about-us-metrics` without numbers. Trust/scale proof.

## 23. Visual CTA — `visual-cta` (OM OSS ONLY)
Full-bleed image bg: "Ditt hem, vår spetskompetens" centered + black "Kontakta oss" button.

## 24. EV/Battery product page (product hero `product-hero` + `product`)
Breadcrumbs → 3-col: [product image card + Teknisk specifikation accordion (15 rows) + Installationsprocess accordion] | [H1 product name, description, "Bra att veta" 2×2 icon grid (availability/install time/compatibility/warranty), Färger swatches, Totalt price + ordinarie struck + grön teknik 50% rows, "Få skräddarsydd offert" cyan CTA → **popup form**] | [expert CTA card (photo + "Rådfråga vår expert!" + phone + rating)].
Then typical page: testimonials → grön teknik → content block → FAQ → main contact → "Liknande produkter" grid (`product__product-card`: tags superkampanj/nyhet/bästsäljare, phases/effect chips, price, Läs mer) → team → visste du att → CE block → certificates → footer SEO.

## 25. CE block — `ce-block` (LONG-FORM SEO + CTA + 9:16 IMAGE)
H2 gradient (ACF) → paragraph → 2 sub-headings + paragraphs → CTA pair → tall 9:16 image right.

## 26. Popup template (product offert form)
Modal: photo header ("Boka rådgivning med en batteriexpert!") + form (Namn/E-post/Telefon/Adress/Postnummer/Meddelande) → "Få ditt förslag" → n8n → /thank-you.

## 27. Thank-you page — `ampy-tack`
Full-viewport aurora bg: glass card w/ animated mint check → "Din förfrågan har blivit mottagen!" → "En av våra rådgivare kommer att kontakta dig inom kort." → gold ★★★★★ "5 av 5 · Betyg på Google" → divider → "Utforska våra eltjänster" teal pill → "Till startsidan" ghost link.

## 28. Header (global)
Top bar #f5f9ff: logo → mega-menus **Tjänster** (4-col: Elinstallationer/Belysning/Kök & Badrum/Populära nav-menus) / **Produkter** (Laddboxar + Solcellsbatterier cards + Guider & verktyg: 4 kalkylator links) / **Lösningar** (4 photo cards: Privatperson/BRF/Företag/Kommun) → **"Gratis rådgivning" teal CTA w/ pulsing green dot** → mobile offcanvas accordion + "Ring en expert" + Google rating.

## 29. Footer (global)
Prefooter "Populära kategorier" (5 link columns on cyan gradient) → main footer (navy: logo, text, socials, Mer om Ampy / Kundtjänst / contact info + Google rating) → footer bar (© + policies).

## 30. Prefilled copy patterns seen in screenshot (Hero_2 live example)
"Byta elcentral" (H1 eyebrow) / "Ny elcentral installerad med 30% ROT-avdrag" (H2) / "Dags att byta ditt gamla proppskåp? …" / CTAs / "Få kostnadsfri rådgivning!" form.

---

## Cross-cutting observations to investigate (seed hypotheses, NOT conclusions)
- H1/H2 inversion in Hero_2 (H1 = tiny eyebrow).
- CTA proliferation: many pages have 6–10 CTA instances competing (hero 2 + form + mikro + blue + footer-seo + main-contact + header).
- "5.0 / 5 av 5" claims appear in ≥6 blocks — candour gate requires owner-confirmed current rating + review count anchor.
- Form asks (address, postnr) before value in Hero_2 vs Baymard field-count principle.
- Dark navy blocks (testimonials, visste-du-att, hero) may create heavy mid-page contrast stacking.
- Lead magnets are orphan pages (no hero/process/contact wrap).
- Trust proof (certificates, team, testimonials) usually sits BELOW SEO content — the Clarity "About Us" visitor suggests proof should move up.
- Speed: multiple hero SVG/webp layers, Splide, Google Maps SDK, animations — lab LCP 9–10s flag.
