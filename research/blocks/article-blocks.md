# Article template blocks + NewsBlock

**Blocks covered:** EditorialByline · ArticleTOC · "Snabbt svar" summary card · review-CTA ("Tyckte du att artikeln var hjälpsam?") · share/print row · ArticleCards ("Populära artiklar") · NewsBlock (`news`, "Nyheter och artiklar!") on landings.

**Used on (verified from `data/block-map.json`, 326 pages):**
- **Full article template** (Header → EditorialByline → ArticleBody → FAQ-accordion → ArticleTOC → ArticleCards → Prefooter): **8 posts** — byta-elcentral-2026, elbilsladdning-hemma-2026, elcentral-guide-2026, elcentral-varningssignaler, fasadmatarskap-huvudsakring, jordfelsbrytare-typ-a-eller-b, kwp-kw-…-solceller, sakringar-jordfelsbrytare-overspanningsskydd. Word counts 1 909–4 879.
- **Legacy bare posts** (Header → ArticleBody → Prefooter only — no byline/TOC/FAQ/cards): rot-avdrag-2026, gron-teknik-2026 (+1 more post per category count).
- **Legal pages** reuse ArticleBody: cookiepolicy, integritetspolicy, kopvillkor, tillganglighet (4 pages) — out of CRO scope, noted for count only.
- **NewsBlock:** verified on **1 page only — the homepage** (grep across all 36 HTML snapshots; the block-map crawler has NO NewsBlock fingerprint at all, so detection on the other 290 landings is a mapping gap, but the snapshot evidence says homepage-only). Position: after MapBlock's "Osäker ifall vi finns där du bor? Kontakta oss", dead last before Prefooter.
- **Positions within articles:** EditorialByline = slot 2 (directly under hero). ArticleTOC = desktop sticky right column (30 %, `position: sticky; top: 8rem`), DOM slot 5. ArticleCards = slot 6, last content block. Review-CTA + share/print live inside ArticleBody's tail, after the FAQ.

**Funnel position:** top-of-funnel/awareness (articles), freshness + internal-linking (NewsBlock). These pages feed SEO/E-E-A-T; their conversion job is *assist* — hand a warmed reader to a service page, a call, or a form.

**Live page fetched:** https://ampy.se/elcentral-varningssignaler/ (560 kB, fetched 2026-08-02). All quotes below are from that fetch or from `data/pages/home.html`.

---

## What it does well

1. **EditorialByline is genuinely strong E-E-A-T, not theatre.** Three roles, each a real link to a team profile: `Skriven av <a href="https://ampy.se/om-oss/julius-callahan/">Julius Callahan</a>` / `Redigerad av … Magnus Harald Metsniin` / `Faktagranskad av … Edvin Gustavsson`, plus "Verifierad av expert" pill, "Uppdaterad juni 14, 2026" and "16 min läsning". Schema backs it: `BlogPosting` + 3 × `Person` + `FAQPage` in JSON-LD. This is exactly the Cialdini-authority + Google E-E-A-T pattern most competitors fake. **Keep.**
2. **"Snabbt svar" is a model answers-first card** (green-stripe summary + "Nyckelpunkter" bullets: "Brännlukt eller smält plast = slå av huvudbrytaren samma sekund", "Säkring som löser direkt = kortslutning…"). MECLABS value-clarity delivered in the first screen; also featured-snippet bait. **Keep.**
3. **TOC responsive behavior is correct.** Desktop: sticky white card, right 30 %. Mobile ≤780 px: `#brxe-meojam { flex-direction: column-reverse }` flips the DOM so the TOC renders as a collapsed accordion ("Innehållsförteckning", `aria-expanded="false"`) ABOVE the article — the right mobile pattern (NN/g: long-page wayfinding without pushing content down). Scroll-spy via `data-heading-selectors="h2, h3"`, `data-collapse-inactive="true"`.
4. **The review-CTA rating is anchored** — "5.0 · 25 omdömen på Google" — one of the few places on the site where the candour gate's "rating + count + source" requirement is actually met. The anchor pattern should be exported to the other blocks; the CTA itself has problems (ART-02).
5. **Article body content quality is high and decision-oriented** (symptom → risk → "Första åtgärd" decision matrix; Elsäkerhetsverket-sourced; innehavaransvar legal framing). Per MECLABS HealthSpire, length is an asset here — the sequencing at the end is the problem, not the word count.
6. **Contextual internal links exist in-body** ("ring en jour elektriker" → /eljour/, "vår kompletta guide om elcentraler" → guide, elbilsladdare → laddbox) — currently the ONLY conversion path besides the header.

---

## Issues

### ART-01 — **P1** — The article template has ZERO conversion blocks: no form, no CTA band, no phone number in the body
- **Evidence:** block-map for all 8 articles shows no MainContact, MikroCTA, BlueCTA, or MainCTA — the only blocks after ArticleBody are ArticleCards and Prefooter. The live page contains exactly **2 `tel:` links on the entire page, both in header/footer chrome** (`tel:+46102657979`), zero in the article column. The most damning detail: the acute-symptom decision matrix instructs *"Slå av huvudbrytaren direkt, utrym vid rök, ring eljour"* — and the reader must hunt the header or scroll 4 900 words to the footer to find a number. An article whose explicit advice is "ring en elektriker" never offers the call.
- **Framework:** MECLABS heuristic — motivation is peaking at the end of "när ska du agera?" content, and the funnel supplies no channel (i = 0 at the decision moment). NN/g: users finish long-form with "what now?"; Jakob's law says they expect a next-step CTA where every other publisher puts one. Unbounce home-services benchmark: urgent/repair intent converts best — these elcentral-warning readers ARE that intent, currently exported to Google via the review ask.
- **Desktop:** end-of-article sequence is FAQ → review beg → Dela/Skriv ut → "Populära artiklar" — three content off-ramps, zero conversion on-ramps. **Mobile:** identical, and worse — the sticky TOC is gone (static accordion at top), so nothing persistent points anywhere; the header CTA has scrolled away 16 minutes ago.

### ART-02 — **P1** — The review-CTA occupies the prime conversion slot, points AWAY from conversion, and asks the wrong audience
- **Evidence (quoted):** *"Tyckte du att artikeln var hjälpsam? Ampy är Sveriges modernaste elfirma. Hjälpa oss att kunna skriva fler artiklar genom att recensera oss. Ditt omdöme gör stor skillnad för oss och vår verksamhet, tack för du tar dig tiden! ⚡ Lämna ett omdöme om oss på Google"*.
- Three distinct problems: **(a) Funnel inversion** — the single CTA card at the article's decision point sends warmed prospects to google.com instead of to /offert or a call. **(b) Policy/candour risk** — article readers are mostly *prospects, not customers*; soliciting Google reviews from people who never bought ("recensera oss" for reading an article) invites reviews that don't reflect a genuine service experience — the exact pattern Google's review policy prohibits, and a threat to the GBP asset (25 reviews) the whole site leans on. The candour gate says no manufactured social proof; this manufactures it politely. **(c) Broken Swedish** — "**Hjälpa** oss att kunna skriva" (should be "Hjälp oss") and "tack **för du** tar dig tiden" (should be "tack för att du tar dig tid") — two grammar errors inside the block that sits directly under "Faktagranskad av … Verifierad av expert". For a 35–65 Swedish homeowner, sloppy Swedish next to an expert-verification badge actively erodes the credibility the byline just built.
- **Desktop/mobile:** identical rendering both; on mobile it is the last thing read before the thumb reaches "Populära artiklar".

### ART-03 — **P2** — All dates are identical ("juni 14, 2026" everywhere): freshness signal becomes a bulk-content tell
- **Evidence:** the article shows "Uppdaterad juni 14, 2026"; homepage NewsBlock shows all three cards "juni 14, 2026". Every post in the block-map appears mass-published the same day.
- **Framework:** E-E-A-T / trust-heuristics — a date pill only adds value when dates differ; identical dates across an entire "Nyheter" section reads as bot-batch publishing to a skeptical homeowner and to Google's helpful-content classifiers. **Desktop/mobile:** visible on both (date pill on cards, byline row on articles).

### ART-04 — **P2** — Legacy money-adjacent posts (rot-avdrag-2026, gron-teknik-2026) run the bare template: no byline, no TOC, no FAQ, no cards
- **Evidence:** block-map: `['Header', 'ArticleBody', 'Prefooter']` for both. These two topics (ROT 30 %, grön teknik 50 %) are the closest-to-money content on the blog — they feed directly into service and product intent — yet they carry the least E-E-A-T and (like all articles) no conversion close. **Desktop/mobile:** both.

### ART-05 — **P3** — NewsBlock craft defects on the homepage
- **Evidence (quoted from home.html):** excerpts hard-truncate mid-clause — *"…vilka komponenter ska finnas där, och vad kräver SS 436 40 00 av din installation under Läs artikel"*, *"…30 mA jordfelsbrytare för Läs artikel"*. All three cards are from the elcentral/jordfelsbrytare cluster; commercial priority is service > laddbox > battery, and the homepage card mix shows no laddbox/service spread. Naming is inconsistent across surfaces: block H2 "Nyheter och artiklar!", article breadcrumb "Hem > Nyheter", cards link "Läs artikel", article-page link "Se alla guider" → /nyheter, footer "Nyheter & Artiklar" (Jakob's law: one name per concept).
- **Position is actually fine** (below MainContact, pure freshness/internal-linking, no conversion cost). **Mobile:** cards stack; truncation looks worse at narrow widths. **P3** because 1 page, low slot.

### ART-06 — **P3** — NewsBlock/ArticleCards absent from the 22 service pages where the clusters would pre-sell
- **Evidence:** no landing page in the 326-page map carries article cards except the homepage; e.g. the elcentral service pages don't surface the 5-article elcentral cluster. The reverse link exists (articles → service); the forward link (service → supporting proof-of-expertise reading) does not. HYPOTES-grade opportunity, not a defect of an existing block.

### ART-07 — **P3** — Minor byline/TOC polish
- "Verifierad av expert" pill is anonymous — the expert IS named one line above; the pill wastes its authority (say the credential: e.g. "Faktagranskad av behörig elektriker" — only if owner confirms Edvin's formal credential; otherwise leave). Every article + every card is "Skriven av Julius Callahan" (founder) — single-author uniformity slightly dilutes the three-role theatre. TOC accordion ships `aria-expanded="false"` with `data-expand-item="0"`; verify the first item actually auto-expands on desktop load — a collapsed sticky card on desktop would waste the 30 % column. In-article stat *"40 procent av alla surrande centraler vi rycker ut på har glapp…"* is a first-party claim with no provenance tag — owner-confirm or soften ([GAP] discipline).

---

## Recommended changes (concrete; copy-pattern direction, not final copy)

1. **Give every article a topic-mapped conversion close (fixes ART-01).** New end-of-article sequence: FAQ → **service-mapped MikroCTA or Blue-CTA band** ("Misstänker du fel i din elcentral? Vi felsöker och åtgärdar — ring 010-265 79 79 / Kostnadsfri rådgivning") → **MainContact form** → review-CTA (demoted, see 3) → share/print → ArticleCards. Mapping via article category: elcentral cluster → /elservice/elcentral/ + form prefilled "Byta elcentral"; laddbox articles → laddboxkalkylatorn + laddbox form; solceller/kWp → batterikalkylatorn. SEO substance untouched — this is pure re-sequencing/appending.
2. **Click-to-call inside acute content.** In the symptom decision matrix, make the "Akut"-row action *"ring eljour"* a literal `tel:+46102657979` link (mobile-first; Fitts — the action at the point of highest motivation). Same for every in-body "ring en elektriker/eljour" phrase.
3. **Repair and demote the review-CTA (fixes ART-02).** (a) Move it below the new conversion close. (b) Fix the Swedish ("Hjälp oss…", "tack för att du tar dig tid"). (c) Re-target the ask: gate the Google-review ask to customers (thank-you page, post-job email — it already exists on /thank-you) and let the article card ask something a *reader* can honestly give — e.g. share the article or a lighter "Var det här hjälpsamt?" feedback widget. Keep the exemplary "5.0 · 25 omdömen på Google" anchor wherever the rating appears.
4. **Upgrade rot-avdrag-2026 + gron-teknik-2026 to the full template** (byline, TOC, FAQ, cards, and the new conversion close) — highest-intent posts, cheapest wins (ART-04).
5. **NewsBlock craft pass (ART-05):** fix excerpt truncation (whole-sentence clamp or ellipsis before the button), diversify homepage cards toward service/laddbox topics, unify the label ("Artiklar & guider" everywhere is the honest one — most items are guides, not news), and stagger real "Uppdaterad" dates as articles genuinely get maintained (never fake-rotate dates — candour gate).
6. **Add a topical ArticleCards instance to matching service pages (ART-06)** — e.g. 3 elcentral-cluster cards on /elservice/elcentral/ above FooterSEO: internal linking, E-E-A-T by association, and a soft answer to "kan jag lita på dem?" HYPOTES: service pages showing expert articles lift form-start rate vs. control — testable per-template.

**Test hypotheses (A/B-phrased):**
- HYPOTES 1: Adding a service-mapped CTA band + MainContact after the FAQ on the 8 articles increases article→form/call conversions vs. current (0-CTA) template, without hurting scroll depth.
- HYPOTES 2: Making "ring eljour" a tel: link in the Akut matrix rows increases phone-click rate from article traffic (mobile) vs. plain text.
- HYPOTES 3: Replacing the reader-facing Google-review ask with a customer-only placement does not reduce review velocity (reviews actually come from jobs), while removing prospect-facing policy risk.

---

## Priority score (arithmetic shown)

Doctrine formula: pages affected × funnel-position weight (hero/form 3, mid 2, low 1) × expected effect (high 3, med 2, low 1).

| Finding | Pages | Weight | Effect | Score | Priority |
|---|---|---|---|---|---|
| ART-01 missing conversion close (adds form/CTA = weight 3) | 11 posts | 3 | 3 | **99** | P1 |
| ART-02 review-CTA misdirection + policy + grammar | 8 | 1 (low slot) | 3 (trust-damaging) | **24** | P1 (trivial fix, trust-risk elevates it) |
| ART-03 identical dates | 15 | 1 | 2 | 30 | P2 |
| ART-04 legacy posts bare template | 2 | 2 | 2 | 8 | P2 (high intent per page) |
| ART-05 NewsBlock craft | 1 | 1 | 1 | 1 | P3 |
| ART-06 cards on service pages (new) | 22 | 1 | 2 | 44 | P3 (opportunity, test-gated) |

**Block-file headline score: 99 (ART-01) → P1, month 1.** The article estate is the best-crafted content on the site with the worst-connected funnel: it builds real authority (linked byline, anchored 25-review proof, decision-grade content) and then, at the exact moment the reader is told to call an electrician, offers them a Google-review form instead of a phone number.
