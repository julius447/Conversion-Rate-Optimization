# Article template (posts) — deep-dive

URLs analyzed (live fetch, full text + markup): https://ampy.se/byta-elcentral-2026/ · https://ampy.se/rot-avdrag-2026/ · https://ampy.se/gron-teknik-2026/ (targeted grep) · https://ampy.se/elbilsladdning-hemma-2026/ (link-structure extraction).
Pages using this template: **11 posts** (block-map category `post`). Three sub-variants verified in block-map:

- **Full editorial shell (8 posts):** byta-elcentral-2026, elbilsladdning-hemma-2026, elcentral-guide-2026, elcentral-varningssignaler, fasadmatarskap-huvudsakring, jordfelsbrytare-typ-a-eller-b, kwp-kw-matenheter…, sakringar-jordfelsbrytare-overspanningsskydd — `Header → EditorialByline → ArticleBody → FAQ-accordion → ArticleTOC → ArticleCards → Prefooter`.
- **Bare dump (2 posts):** gron-teknik-2026, rot-avdrag-2026 — `Header → ArticleBody → Prefooter` only. No byline, no TOC, no Snabbt svar, no FAQ accordion, no review card; raw WP content with inline `font-weight:400` spans.
- **Archive (1):** /nyheter/ — `Header → AlternativHero → Prefooter` (out of scope here; noted for completeness).

Word counts 1,909–4,879 (median ~3,400). These are the pages that capture the exact research queries the paid account is buying ("byta elcentral pris", "byta proppskåp" are live Google search terms per business context).

## Current block sequence (verified, full-shell variant — byta-elcentral-2026)

1. **Header (global)** — mega-menus + "Gratis rådgivning" teal CTA (`→ /kontakt/`) + mobile "Ring en expert" (`tel:+46102657979`). *Desktop: persistent top bar. Mobile: offcanvas; once the reader scrolls into a 3,900-word article the header CTAs leave the viewport — no sticky replacement exists (verified: no sticky CTA element in markup; `sticky` hits belong to the TOC).*
2. **Breadcrumbs** — "Hem > Nyheter > Byta elcentral 2026…". Plain section — **no dark featured-image hero on this post**; H1 (`.brxe-post-title`, correct H1 semantics, unlike Hero_2's eyebrow-H1) + excerpt paragraph ("Att byta elcentral 2026 landar oftast på 12 600 till 24 500 kr efter ROT 30 %…").
3. **EditorialByline** — avatar trio (Julius Callahan Skriven / Magnus Harald Metsniin Redigerad / Edvin Gustavsson Faktagranskad, each linked to /om-oss/ profile), "Verifierad av expert" green pill, "Uppdaterad juni 8, 2026", "17 min läsning". *Mobile: avatars stack per `ampy-editorial-avatars` flex (overlap −10px), row wraps.*
4. **ArticleBody 2-col** — left 65%: "Snabbt svar" summary card (Sammanfattning + Nyckelpunkter bullets, green left stripe) → full typographic body: price-matrix tables, "Pro tip … Verifierad av Magnus Harald Metsniin" boxes, pull quote from Edvin Gustavsson ("Senior Elektriker, Arbetsledare & Kvalitetsansvarig"), "En berättelse från Ampy" story box, timme-för-timme table, 12-punkts offertchecklista. Right 30%: sticky scroll-spy TOC ("Innehållsförteckning", collapsible). *Mobile: single column; TOC collapses to a disclosure (verified `toc` collapsible markup); the sticky rail disappears.*
5. **FAQ accordion** — "Vanliga frågor", 4 H3 questions (ROT amount, tidsåtgång, måste jag vara hemma, el samma kväll).
6. **Review CTA card** — "Tyckte du att artikeln var hjälpsam? … Lämna ett omdöme om oss på Google" (⚡ button → Google) + 5 stars + "**5.0 · 25 omdömen på Google**" (anchored rating+count — candour-compliant, verified in markup).
7. **Share/print row** — "Dela · Skriv ut".
8. **ArticleCards** — "Populära artiklar" 3-card grid + "Se alla guider".
9. **Prefooter/Footer** — Populära kategorier link columns; footer "Kundtjänst" column links **ROT avdrag 2026** and **Grön Teknik 2026** (i.e. the two broken bare posts are footer-linked from every page on the site).

### Conversion affordances actually present in a full-shell article (exhaustive, verified)
- `tel:` links on the whole page: **2**, both chrome (header "Ring en expert" + footer "010-265 79 79"). **Zero in the article body.**
- Links to /kontakt/ from the body: **1** — a plain text link in the very last paragraph of Summering (~word 3,700): "Skicka ett par skarpa bilder på din central till oss, så återkommer vi med en [kostnadsfri bedömning och ett prisförslag](https://ampy.se/kontakt/) inom två arbetsdagar."
- Styled CTA blocks in the body: **0**. The only styled CTA card in the template is the **Google-review ask**.
- On elbilsladdning-hemma-2026 (laddbox — a commercial vertical): **0** tel links in `<main>`, **0** /kontakt/ links, **0** links to Laddboxkalkylatorn — despite the site owning that exact calculator. Body links go to product pages (Zaptec Go, Easee Charge up, Nexblue Edge 2), /laddbox/, /eljour/ and sibling articles.

## Customer-flow walkthrough (35–65 y/o homeowner, mobile)

**0–5 s:** Googles "byta elcentral pris" (a verified live search term with 0 form leads to date). Lands on a page whose H1 + excerpt answer the query instantly: "landar oftast på 12 600 till 24 500 kr efter ROT 30 %". Message match: excellent. Byline trio + "Verifierad av expert" reads as a serious publication, not a sales page. This is exactly the trust-seeking behavior Clarity showed (the paid visitor who went Contact → About Us).

**Scroll (2–17 min):** The content answers every decision question the Byggahus/Reddit research surfaced — fixed vs löpande pris ("Kräv ett fast pris"), dolda fel ("Hur hanteras dolda fel? Står det tydligt i avtalet…"), damage responsibility ("Finns ansvarsförsäkring?"), Elsäkerhetsverket registration ("Är företaget registrerat hos Elsäkerhetsverket? Det är ett lagkrav…"). Per MECLABS HealthSpire, this length is an asset, not a liability — the page is building motivation and reducing anxiety for 3,900 words. Meanwhile the header CTA scrolled away hundreds of screens ago and nothing replaced it.

**Decision moment:** The reader reaches Summering convinced ("den ärliga elektrikern [är] värd mer än den billigaste" — the article literally argues Ampy's own value prop). The next step offered is one unstyled text link, followed by a large styled card asking the *reader* to do Ampy a favor: "Hjälpa oss att kunna skriva fler artiklar genom att recensera oss." A non-customer cannot honestly review; a ready-to-buy reader gets no form, no phone button, no calculator. The funnel ends by asking for value instead of offering the next step. On the two bare posts it is worse: rot-avdrag-2026 ends "Kontakta oss på Ampy idag för en kostnadsfri offert" — **as unlinked plain text** — followed by the published editor note "FAQ: Vanliga frågor om ROT 2026 **(ADD FAQ SECTION)**".

## What works (keep — do not touch in the CTA retrofit)

- **The E-E-A-T shell is the best on the site.** Real named trio linked to team profile pages, expert pull quotes with titles, "Pro tip … Verifierad av", story boxes, timme-för-timme table, 12-punkts checklist. Cialdini authority done honestly.
- **Answer-first structure** (H1 → excerpt with price range → Snabbt svar with Nyckelpunkter) — ideal for both the impatient reader and AI-overview/featured-snippet capture.
- **Correct H1 semantics** — the article template does NOT have the Hero_2 H1-eyebrow inversion.
- **Anchored social proof** — "5.0 · 25 omdömen på Google" is the candour-gate model the rest of the site should copy (six other blocks assert "5.0" unanchored).
- **Anti-sell candour content** — "När vi avråder från byte — komplettering räcker" ("vi vill inte sälja på dig dyra lösningar som du egentligen inte behöver") is the brand's moat in article form. Any CTA insertion must preserve this register: consultative, no urgency.
- **Internal-link discipline in shell posts** — service-page links exist in-body (3× /elservice/elcentral/ in byta-elcentral), sibling-cluster links, geo links (Bromma, Tyresö, Sollentuna, Täby).

## Findings

**ART-01 · P0 · No in-article conversion path (all 11 posts).**
Verified: 0 in-body tel links, 0 styled CTA blocks, 1 end-of-body text link to /kontakt/ (byta-elcentral); 0 of any of these on elbilsladdning-hemma-2026. Evidence: MECLABS heuristic — the article maximizes m (motivation) and v (value clarity) and lowers a (anxiety), then supplies no channel; conversion requires an offer to accept. JTBD: the reader's job is "get a trustworthy fixed quote" — the article proves trustworthiness for 17 minutes and never offers the quote. Business context: the exact paid queries these pages rank/land for produced **0 confirmed form leads**. Mobile note: worst on mobile — header CTAs leave viewport immediately, no sticky element exists; for the entire read there is literally no visible conversion affordance. Priority arithmetic: 11 pages × funnel weight 2 (mid-funnel content) × effect 3 (high) = **66**.

**ART-02 · P0 · rot-avdrag-2026 + gron-teknik-2026 shipped broken, and they are footer-linked from every page.**
Verified live: both pages publish the raw editor note "**(ADD FAQ SECTION)**" inside an H2; no byline, no TOC, no Snabbt svar styling, no FAQ accordion, no review card; content is inline-styled WP spans; the sole closing ask "Kontakta oss på Ampy idag för en kostnadsfri offert" is **unlinked text** (NN/g: no affordance → no action). Byline absence also means no author/date credibility on the two money-adjacent tax-rule pages, and the footer "Kundtjänst" column ("ROT avdrag 2026", "Grön Teknik 2026") routes sitewide traffic straight into them. A visible placeholder note is trust-damaging (Cialdini authority in reverse) on pages whose whole subject is "can I trust the numbers on my faktura". Priority: 2 pages × 2 × 3 = **12**, plus sitewide footer exposure (qualitative multiplier). Fix = editorial-shell retrofit + real FAQ + linked CTA; content itself is already good (correct 2026 canon: 30 % ROT, 50 000 kr cap, 75 000 kr ROT+RUT tak, grön teknik separate).

**ART-03 · P1 · The end-of-article ask is inverted: review ask replaces the business ask.**
Verified: the review card ("Lämna ett omdöme om oss på Google") is the only styled CTA in the template and sits at the natural decision point after FAQ. A prospect cannot review; a customer rarely reads "byta elcentral pris". Wrong audience, right position. Sequencing per MECLABS: offer the next step (offert/photo-bedömning/ring) at the decision point; move the review ask to audiences who can act on it (thank-you page — which already exists as `ampy-tack` — and post-job email). Keep the review card in the template but demote it below the next-step block. 11 pages × 2 × 2 = **44**.

**ART-04 · P1 · Calculator/tool cross-sell absent where it is most natural.**
Verified: elbilsladdning-hemma-2026 never links Laddboxkalkylatorn; elcentral-cluster articles never link Elcentral-kollen; rot/grön-teknik articles never link Energikalkylatorn. The site owns the exact interactive next step each reader wants (a price/fit estimate — the softest possible ask for a not-yet-ready researcher). This is also the lead-magnet-orphan problem in mirror image: articles don't feed the tools, tools don't wrap in contact blocks. 11 pages × 2 × 2 = **44**. HYPOTES-linked (see H2/H3 below).

**ART-05 · P1 · Mobile: no persistent CTA during a 17-minute read.**
Verified in markup: only sticky element is the desktop TOC rail; mobile collapses it. Fitts/thumb-zone: a bottom mini-bar (Ring · Få prisförslag) is the established home-services pattern; Unbounce benchmark logic says urgent/repair-adjacent readers (varningssignaler, jordfelsbrytare articles) convert disproportionately by phone. Must be dismissible and appear only after meaningful scroll (~40–60 %) to protect reading experience. 11 pages × 2 × 2 = **44** (mobile share ≥65 % assumed per doctrine).

**ART-06 · P2 · The photo-bedömning micro-conversion — the template's best offer — is buried as plain text, once, at word ~3,700.**
Verified copy: "Skicka ett par skarpa bilder på din central till oss, så återkommer vi med en kostnadsfri bedömning och ett prisförslag inom två arbetsdagar." This is a superb low-friction, candour-true offer (Baymard: perceived difficulty ≈ zero fields; it directly answers the #1 Swedish homeowner anxiety — final-price surprise) and it even matches an existing capability (Hero_2 form's "Fler detaljer" bilder upload). It deserves packaging as the inline CTA block (ART-01's fix) rather than a body sentence linking to generic /kontakt/ — message-match break: /kontakt/ hero says nothing about photo assessment. 11 × 2 × 2 = 44 shared with ART-01 fix; standalone polish = **P2**.

**ART-07 · P2 · Candour/provenance check on in-article field statistics.**
The article asserts internal data as fact: "Baserat på vårt mönster från över 600 centralbyten", "I 8 av 10 villor från 60- och 70-talet hittar vi dolda fel", "Cirka 35 procent av villor…", "ungefär 12 procent", "cirka 28 procent", "cirka 8 procent", "45 procent". These are persuasive and on-voice, but the candour gate requires them to be owner-verifiable (job-log evidence) or reframed ("i våra jobb ser vi ofta…"). Not a delete recommendation — a provenance confirmation task. Also: "Ampy är Sveriges modernaste elfirma" in the review card is a strong superlative — allowed per owner directive 2026-07-18 unless demonstrably false; no action, noted for the record.

**ART-08 · P3 · Date-format inconsistency and micro-polish.**
"Uppdaterad juni 8, 2026" (Anglicized order; Swedish = "8 juni 2026") vs rot-avdrag's "Publicerad 30/01/26". One typo-class error in byta-elcentral body ("60- och 75-talet", "kostnaden för installation av din elcentral", "avdraget." checklist item cut off mid-sentence: "visa hur stort avdraget."). Copy-edit pass, no structural change.

## Recommended sequence (wireframe — full-shell template, applied to all 11 posts)

| # | Block | Why here | New/existing/modified |
|---|---|---|---|
| 1 | Header | Global | Existing |
| 2 | Breadcrumbs + H1 + excerpt | Answer-first entry; correct H1 kept | Existing |
| 3 | EditorialByline (trio, Verifierad, Uppdaterad, läsning) | E-E-A-T shell — **retrofit onto rot-avdrag-2026 + gron-teknik-2026** | Existing (extend to 2 bare posts) |
| 4 | Snabbt svar + body part 1 + sticky TOC | SEO substance untouched; snippet capture | Existing |
| 5 | **Inline CTA block A** (after the first price table / ~25–35 % depth): category-contextual micro-offer — elcentral cluster: "Osäker på just ditt proppskåp? Skicka en bild — kostnadsfri bedömning och prisförslag inom två arbetsdagar" + one light button; laddbox cluster: Laddboxkalkylatorn link; rot/grön-teknik: Energikalkylatorn / "vi sköter Skatteverket-administrationen — få en offert med avdraget förräknat" | Converts at the moment price curiosity peaks; consultative register, no urgency (candour gate). Narrow, article-width, visually quiet (Blue-CTA-derived, not Mikro_CTA dark band) so reading flow survives | **New** (one reusable block, ACF-driven per category) |
| 6 | Body part 2 (dolda kostnader → checklista → Summering) | SEO preserved in full — re-sequencing only adds, never deletes | Existing |
| 7 | **"Nästa steg" end-of-article card**: H3 + primary "Kostnadsfri rådgivning" (form route) + secondary "Ring 010-265 79 79" (tel:) + tertiary contextual calculator link | The decision point gets a business ask; replaces the review card's slot; mirrors the owner's own orphan-fix philosophy (wrap content in a contact close) | **New** (or Main CTA variant adapted to article width) |
| 8 | FAQ accordion | Objection handling adjacent to the ask | Existing (build real FAQ for the 2 bare posts — kill "(ADD FAQ SECTION)") |
| 9 | Main contact (`main-contact`) — full form section | Strongest conversion asset on the site; after all content so the reading experience is intact. HYPOTES: test presence vs Nästa steg card alone (avoid triple-ask stacking with #7 — if both, #7 primary button anchors down to this form instead of navigating away) | Existing block, new placement (test) |
| 10 | Review CTA card — demoted, reframed toward actual customers ("Har vi hjälpt dig tidigare?") | Keeps the loyalty/review engine without hijacking the prospect's decision point; primary review ask lives on thank-you page + post-job email | Existing, modified + moved |
| 11 | Share/print + Populära artiklar | Continuation path for not-ready readers | Existing |
| 12 | Prefooter/Footer | Global | Existing |
| M | **Mobile sticky mini-bar** (Ring · Få prisförslag), appears ≥40 % scroll, dismissible | Only persistent affordance on a 17-min mobile read; Fitts thumb zone | **New** (test first, see H3) |

Rollout order: (1) fix ART-02 bare posts (days, footer-linked, trust-critical); (2) ship inline CTA block + Nästa steg card template-wide (one template edit → 11 pages); (3) mobile sticky bar as an experiment; (4) main-contact placement test.

## Test hypotheses (top 3, A/B)

1. **HYPOTES (inline CTA):** Adding one contextual inline CTA block after the first price table ("Skicka en bild på din central — kostnadsfritt prisförslag inom två arbetsdagar") will increase article→/kontakt/+form-start rate versus the current single end-text-link control, without reducing scroll depth or avg. time on page. (MECLABS HealthSpire: conversion elements at the point where content has just answered the price question.)
2. **HYPOTES (ask inversion):** Replacing the end-of-article Google-review card with a "Nästa steg" card (rådgivning + ring + calculator), review ask demoted below it, will produce measurable form starts/phone clicks from post pages (currently ~0 attributable) with no material drop in review volume, since the review ask is duplicated on /thank-you and post-job email where actual customers are.
3. **HYPOTES (mobile sticky bar):** A dismissible bottom mini-bar (Ring · Få prisförslag) shown after 40–60 % scroll on posts will increase tel-click rate on mobile versus no bar, with bounce/engagement neutral (guardrail: dismiss rate <40 % and no drop in read completion).
