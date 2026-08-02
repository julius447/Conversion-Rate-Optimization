# Funnel & CTA architecture — the ONE site-wide conversion system

Synthesis lens: adversarial integration of the 14 template deep-dives + 20 block audits (research/templates/*, research/blocks/*), grounded in context/01–03, data/gsc-summary.md and data/live-browser-observations.md. Where template files disagree, this file resolves the conflict, names the overruled file and the trade-off. Nothing here invents data; every count is from the cited audits.

**The one-sentence diagnosis this architecture answers:** the site has ~13–17 undifferentiated asks per money page, ≥8 labels for one identical action, ~900 CTA instances converging on a broken /kontakt/ page, a JS-only hero form that GA4 cannot see, and its proof architecture inverted (trust below the ask) — which together explain "33 paid clicks, 2 phone clicks, 0 form starts" better than any single defect does.

---

## 1. THE CANONICAL CTA DOCTRINE

### 1.1 Label taxonomy (resolves Gratis / Kostnadsfri / Boka / offert / förslag / konsultation)

Verified census (global-nav.md GLOB-03, 36 snapshots): "Gratis rådgivning" 59 · "Kostnadsfri radgivning" [typo] 41 · "Kostnadsfri rådgivning" 29 · "Få en kostnadsfri rådgivning" 24 · "Boka rådgivning" 16 · "Få skräddarsydd offert" 16 · "Få ditt förslag" 16 · "Få en kostnadsfri konsultation!" (footer) · "Ring 010-265 79 79" 55 · "Ring en expert" 35. Eight-plus labels for two actions. Jakob's law + NN/g consistency: one action, one name.

**CANON (form path):**

| Role | Canonical string | Replaces |
|---|---|---|
| Form-path CTA button (all bands, hero, header) | **"Kostnadsfri rådgivning"** | "Gratis rådgivning" (header, Map sub-card), "Kostnadsfri radgivning" (typo, ~290 pages — week-1 library fix, GLOB-01/CE-1/F1), "Kontakta oss", "Support" |
| Form section heading | **"Få kostnadsfri rådgivning"** | "Få en kostnadsfri konsultation!" |
| Form submit button (aof + MainContact + calculators) | **"Boka rådgivning"** | "Gratis rådgivning" (MainContact submit), "Få ditt förslag", "Skicka offertförfrågan" variants |
| Callback promise (everywhere incl. /thank-you) | **"Vi ringer dig inom 24 timmar"** [GAP: owner-confirm SLA] | "inom kort", "snarast", "inom 60 sekunder" |

**CANON (phone path):** **"Ring 010-265 79 79"** — the number is always in the label (55–65-year-olds dial from what they see; Fitts + Jakob). "Ring en expert" retired. Eljour context only: **"Ring eljouren 010-265 79 79"**.

**Where each retired word is still allowed:**
- **"Gratis"** — retired from CTAs entirely. It survived only in the header and one submit; "kostnadsfri" is the candour register and already the majority correct form.
- **"Offert"** — allowed as an *outcome noun* in body copy and process steps ("skriftlig offert", "fast pris i offerten", VarProcess step 2 "Kostnadsfri offert"), and in product-page descriptor copy. **Banned as a standalone competing CTA verb** — "Få skräddarsydd offert" retires with the product popup (product-blocks.md PU-1/PU-3). Rationale: the deliverable of every form on the site is the same thing — a callback from an electrician; two CTA nouns for one funnel forced visitors to model two funnels.
- **"Förslag" / "konsultation"** — retired everywhere.
- **"Boka rådgivning"** — submit-only. Never a link label (a link that "books" but navigates breaks expectation).

**60-second promise:** "Prata med en elektriker inom 60 sekunder!" (268 pages, MainCTA) collides with "inom 24 timmar" on the same pages (MC-3, GEO-ELJ-03, HP-08). Candour ruling: the two promises may only coexist if explicitly framed as the two lanes — "Ring nu — svar direkt" (phone) vs "Skicka formuläret — vi ringer inom 24 timmar" (form). Until the owner confirms a real <60s time-to-human SLA [GAP], the phone-band headline pattern is "Prata direkt med en elektriker — ring 010-265 79 79".

### 1.2 The anchor-vs-navigate rule

Evidence: 5–6 of 8 non-phone asks per geo page navigate to /kontakt/ while two forms sit on the same page (GEO-01 ×2 files, EFX-03, FS-2, CTA-01, GLOB-05); at ~9–10 s lab LCP each navigation is a full funnel restart (MECLABS friction; NN/g interaction cost).

**RULE:**
1. **Body CTAs anchor, never navigate**, whenever a form exists on the page. Hero primary → focus/scroll the adjacent `.aof` form (desktop: focus first field; mobile: smooth-scroll to card). All mid/tail CTAs (incentive, Map sub-card, SEO-tail, terminal close) → smooth-scroll `#main-contact`. This covers ~600 body instances across 290+ pages.
2. **Navigate to /kontakt/ only where no on-page form exists** — and after Phase L (lead-magnet/team/article wraps) that set shrinks to legal pages, /nyheter/ and edge pages.
3. **Header CTA stays a uniform navigate → /kontakt/ on all pages.** This *overrules* header-audit HDR-02's per-page anchor suggestion. Trade-off, named: per-page-variable chrome behaviour breaks Jakob's-law predictability and is untestable as one unit; the cheaper unit of work is fixing the destination once (§4). Run "header CTA anchors on form-bearing pages" as a later A/B (HYPOTES), not as doctrine.
4. **One deterministic chrome exception:** on the eljour CPT (57 pages) the header CTA becomes "Ring eljouren 010-265 79 79" (tel:). Trade-off: it violates chrome uniformity, but eljour is a different JTBD class (Unbounce: urgent/repair converts on the call) and the swap is per-template deterministic, not per-scroll.
5. **Hard prerequisite before ANY retargeting:** remove `data-interaction-hidden-on-load` from MainContact (MC-09) and from every anchor target. The live-browser session verified enterView fadeIn leaving whole sections at `opacity:0`; an anchor that scrolls a visitor to an *invisible* form is strictly worse than today's navigation. Sequence in §4.

### 1.3 Phone vs form dominance by intent temperature

GA4 reality check: the only recorded paid conversions are 2 phone clicks; the form path recorded 0 starts (instrumentation + friction both implicated). Phone is the path that demonstrably works; form is the path with the bigger untapped ceiling once SSR + instrumentation land.

| Temperature | Templates | Primary ask | Secondary | Mechanics |
|---|---|---|---|---|
| **URGENT** | eljour-i (56), /eljour/ pillar, /ampy-eljour/, acute article rows (varningssignaler, jordfelsbrytare) | **PHONE** — single dominant Ring CTA, "Jour öppen just nu" status, phone number in the H1 pattern | Form demoted to explicit two-lane: "Inte akut? Bli uppringd" (namn+telefon only) | Sticky desktop call panel + **fixed mobile call bar** (port owned Eljour-block v3, owner-gated visual diff); header CTA = phone on this CPT; `tel:` links inside symptom/акut content |
| **HIGH (transactional service/product)** | service (22), elektriker-i (56), elinstallation-i (56), laddbox-i (56), product (26), elektriker-för-X (13) | **FORM** — server-rendered short hero form (kundtyp-silent, ärende, namn, telefon, postnr, GDPR) is the hero's ONE primary ask | Phone as compact co-equal (icon + number, not a second gradient button); ONE phone band after first proof | Kills the verified triple-ask (H2-01: 2 CTA buttons + form + header = 3 mechanisms on screen 1). Felsökning/jordfelsbrytare/elbesiktning service pages may run the call-first divergent variant (service-pages.md alternative) |
| **MID (brand/verification/routing)** | homepage, Hero-1 pillars, hubs, om-oss | Form at the close (MainContact) via anchored CTAs; hero CTA = anchor to `#main-contact` / compact capture | ONE phone band after first proof block | GSC: 73 % of organic clicks are branded → homepage/om-oss are the *verification step of a warm funnel*; proof before any hard ask |
| **LOW (research/assist)** | articles (11), lead magnets (7), /nyheter/, team pages (6) | Value first; then a contextual micro-offer at the point the content answers the price question (photo-bedömning / matching kalkylator), then "Nästa steg" close (form anchor + tel) | Mobile sticky mini-bar (Ring · Kostnadsfri rådgivning) after ~40–60 % scroll, dismissible (HYPOTES — test before rollout) | Review-ask demoted below the business ask (ART-02/ART-03); tools keep their own embedded value-then-ask forms untouched |

### 1.4 Max asks per page + the job of each remaining slot

Verified current state: 13 body asks + 2 chrome on elektriker-i (cta-bands ledger), ~17 on geo-elektriker, ~12 on service, ≥7 mechanisms on product pages. Three bands say the same sentence ("Prata med en elektriker…") — repetition without progression trains banner-blindness (NN/g; MECLABS: no new m/v, added a).

**BUDGET: maximum 5 body asks per page + 2 chrome (header CTA + header phone). Every surviving ask has a distinct job:**

| # | Slot | Ask type | Its ONE job |
|---|---|---|---|
| 0 | Chrome (header) | "Kostnadsfri rådgivning" → /kontakt/ + **visible "010-265 79 79" tel** (new, HDR-01 — desktop text link, mobile icon-button OUTSIDE the hamburger) | Always-available exit for both paths, any scroll depth |
| 1 | **Hero ask** | Form (HIGH) / Phone (URGENT) / anchor (MID) | Capture the already-decided arrival at message-match moment |
| 2 | **PhoneBand** (the ONE merged MainCTA×BlueCTA band, §3) — placed directly after Testimonials | Phone only, anchored trust row | Convert the caller the first proof just persuaded (Cialdini → ask; cta-bands rec 3) |
| 3 | **Contextual micro-ask** (optional, max one) | Differentiated, never generic: incentive block's inline "räkna med en elektriker" line, calculator entry tile, B2B serviceavtal card, article inline CTA | Answer the objection live at that scroll depth — the only justification for a mid-page ask |
| 4 | **The close**: FAQ → MainContact `#main-contact` | The form moment (3 required fields: Namn · Telefon · Postnummer; E-post/Adress optional — MC-03, H2-04, Baymard) | Convert the reader whose objections the page just answered |
| 5 | **Terminal close** (reframed FooterSEO folded into prefooter, §3) | Phone-first "Fortfarande osäker? Prata med en elektriker först — det kostar inget" + anchor to #main-contact | Last-chance catch for bottom-scrollers; the ONLY tail ask |

Everything else — second/third phone bands, duplicate CTA pairs in CEBlock, Map sub-card's own /kontakt/ button, MikroCTA "Vill du veta mer?" — is retired or retargeted (§3). Net per geo page: 13 body asks → 5.

---

## 2. THE FINAL BLOCK SEQUENCE PER TEMPLATE (one table)

Header first and Prefooter/Footer last on every row (implied). **Bold** = new or merged block. `↑`/`↓` = moved vs live. `*` = overrules a template file (footnotes below). Shared definitions: **TrustStrip** = one-row Elsäkerhetsverket-registrerad (link to the live `?foretag=12047521` lookup, CERT-A) + "5,0 av 5 · N recensioner på Google" [GAP: owner count] + ONE canonical volume fact [GAP: resolve 1000+ vs 3000+/år]. **PhoneBand** = merged MainCTA×BlueCTA (§3). **SEO-tail** = VissteDuAtt + CEBlock prose merged, ONE anchored CTA pair. **Terminal** = FooterSEO reframed into prefooter top.

| Template (pages) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **homepage** (1) | Hero-1 (CTA→`#main-contact`, anchored rating) | **ServiceRouter** (MiniMenu+ServiceGrid merged, service-first) | Testimonials | VarProcess (typos fixed) | **PhoneBand** | **ProductTeaser** (2 cards: laddbox→battery) | Certificates ↑new-here | MainContact `#main-contact` | MapBlock | News | | | | |
| **service** /elservice/* (22) | Hero_2 v2 (SSR form, H1=big headline) | **Prisblock** (range efter ROT + fast-offert-löfte, from FAQ copy) | **TrustStrip** | Testimonials ↑\*¹ (vertical-pinned) | **PhoneBand** | ContentBlock | ROT **or** Hemförsäkring (eligibility-gated, SVC-03) | VarProcess ↓\*² | FAQ (6–7 Q) | MainContact | MapBlock + related-services | **SEO-tail** | Certificates | **Terminal** |
| **elektriker-i** (56) | Hero_2 (SSR, "fast pris i offerten" H1) | **TrustStrip** | Metrics (candour-fixed set) | Testimonials ↑\*³ | **PhoneBand** | ServicesGrid | ContentBlock ↑ (idx 15→7) | ROT ↑ | VarProcess | TeamSection ↑ (pre-form, TB-02) | FAQ ↑ (ESV-frågan first) | MainContact | MapBlock | **SEO-tail** → Certificates → **Terminal** |
| **eljour-i** (56) | Hero_2-Eljour (**phone-primary**, call panel, no aof form) | Symptom-block (sticky panel + **fixed mobile call bar**) | **JourProof-strip** (replaces Metrics) | VarProcess-Jour (Ring-först steps) | **Pris & hemförsäkring** (replaces ROT; fast inställelseavgift [GAP]) | FAQ | Testimonials (emergency-sorted) | **Two-lane contact** ("Akut? Ring" / "Kan vänta? namn+telefon") | **SEO-tail** (VDA↓+Content+CE) | Certificates | MapBlock ↓ | **Terminal** | | |
| **elinstallation-i** (56) | Hero_2 (SSR; honest pris-title, GEO-03) | **TrustStrip** | Testimonials | **PhoneBand** | ServiceGrid | ContentBlock | ROT ↑ (pre-form, INC-04) | VarProcess | FAQ ↑ (GEO-17) | MainContact | MapBlock (proximity-sort) | **SEO-tail** | Certificates | **Terminal** |
| **laddbox-i** (56) | Hero_2 ("fr. X kr efter 50 %" H1, reconciled price GEO-09) | **TrustStrip** | Testimonials ↑ | ProductGrid (3 cards, **dual-CTA → on-page form**, price-caveat) | GrönTeknik ↑ (idx 16→5) | **PhoneBand** | **VarProcess** (new laddbox variant, GEO-08) | ContentBlock | FAQ | MainContact | MapBlock | **SEO-tail** | Certificates | **Terminal** |
| **elektriker-för-X** org-skin (11) | Hero_2 + EFX form (kept; SSR + de-H1'd title) | **OrgTrustStrip** (ID06 · Trygg Hansa · ESV) | ContentBlock ↑ (vertical value props) | VarProcess-B2B (offert→avtal→utförande→dokumentation; step-3 bug fixed) | **Referenser** (re-headed Testimonials, no "grannar"; [GAP: B2B reviews]) | FAQ ↑ (LOU/styrelseansvar) | **Serviceavtal-CTA** (MikroCTA repurposed) | MainContact-org (EFX fields) | VissteDuAtt | CEBlock | MapBlock ↓ | Certificates | **Terminal**-org | |
| — consumer-skin (villor/radhus, 2) | = elektriker-i spine with EFX form kept | | | | | | | | | | | | | |
| **product** (26) | ProductHero-v2 (**inline 3-field form** replaces popup; "Pris före/efter Grön Teknik" — no fake strike, PP-03; named expert; anchored rating) | **"Vad ingår i priset?"** (popup-30855 content surfaced on-page) | Calculator-UI (battery keep / **ev: embed Laddboxkalkylatorn**; error-phone fixed P0) | Testimonials | GrönTeknik | ContentBlock | VissteDuAtt ↑ | FAQ (price aligned w/ hero, PP-01) | MainContact | TeamSection (category-matched bios) | ProductGrid ("Liknande", cap 4, no load-more) ↓ | CEBlock | Certificates | **Terminal** |
| **pillar** Hero-1 ×3 (elektriker/elinstallation/laddbox) | Hero-1 + **compact capture** (namn/tel/postnr) or anchor; typo+staging-404 fixed | Metrics (canonical numbers) + ESV badge | ServiceGrid / ProductGrid (w/ prices) | **Signature device** (laddbox: Laddboxkalkylatorn embed; elektriker/elinstallation: pris-tabell from FAQ) | **Proof band** (Testimonials vertical-sorted + Certificates merged) | VarProcess | MainContact | FAQ | ContentBlock + CE tail | TeamSection → VissteDuAtt → ROT/GT | MapBlock + **"Alla områden" hub-link** | **Terminal** (ONE band; Blue/Mikro cut) | | |
| — /eljour/ pillar (1) | Hero-1 **phone-primary** (image: electrician not cabin) | Symptom-block | Jour-trust-strip | Jour-FAQ | Hemförsäkring (button fixed, PIL-03) | MainContact non-acute framing | SEO-tail | MapBlock | **Terminal** | | | | | |
| — /batterilagring/ (1) | keep live spine; fix H1/H2 (PIL-05), calc error-phone (PIL-09), reduce 3 form systems→2 | | | | | | | | | | | | | |
| **hub** (elservice/laddboxar/solcellsbatterier) (3) | AlternativHero-v2 (**real H1**, Swedish breadcrumb, trust row) | Routing grid (**links repaired** CAT-01; grouped, Eljour first; product hubs: filter chips + "Osäker? → kalkylatorn" tile) | GrönTeknik / ROT (surfaced from FAQ, CAT-07) | Calculator embed (battery keep; laddboxar: port; elservice: Elcentral-kollen teaser) | **PhoneBand** (claims anchored) | VarProcess (typos fixed) | Compressed SEO section | MainContact | FAQ | | | | | |
| — /nyheter/ (1) | AlternativHero-v2 (H1 + intro) | Featured/pillar row | Article loop + filter chips + pagination | **PhoneBand**-light | | | | | | | | | | |
| **om-oss** (1) | Hero-1 (headline re-aimed at trygghet, not growth/AI; typo fixed) | **TeamSection** (new here; linked cards, full names) | Metrics **with real numbers** (OM-1 contradiction resolved) | Testimonials (new here) | ContentBlock (people photos, compressed) | Certificates + **facts line** (org.nr, ESV-kontroll link) | MainContact (VisualCTA **cut**, §3) | | | | | | | |
| **kontakt** (1) | **Contact header** (H1 "Kontakta Ampy — kostnadsfri rådgivning" + tel-CTA + öppettider [GAP]) | MainContact (mobile: form first, condensed trust strip; Adress optional) | **"Vad händer sen?"** (24 h + "samtalet kommer från 010-265 79 79") | Mini-FAQ (pris/bindande/tid/fast pris) | **Company-facts card** (adress, org.nr, ESV-check, karta) | | | | | | | | | |
| **article** (11) | Breadcrumbs + H1 + excerpt | EditorialByline (retrofit onto rot/grön-teknik bare posts, ART-02/04) | Snabbt svar + body pt 1 + sticky TOC | **Inline CTA A** (~30 % depth, category-contextual: bild-bedömning / kalkylator; quiet, article-width) | Body pt 2 (`tel:` on every "ring eljour" string) | **"Nästa steg" card** (Kostnadsfri rådgivning → form + Ring + kalkylator) | FAQ | MainContact (test presence; Nästa-steg primary anchors here) | Review-card ↓ (demoted, customer-framed) | Share + Populära artiklar | *M: sticky mini-bar ≥40 % scroll* | | | |
| **team** member (6) | AlternativHero + **credential chips** (real H1) | Nyckelfakta ("Om {namn}", Swedish) | **Expert-CTA card** (Ring + "vi ringer inom 24 h") | E-E-A-T cards (verbatim) | Certifieringar + **ESV-kontroll link** | Quote | **"Jobb {namn} ofta gör"** service links | FAQ + schema | MikroCTA-variant close | TeamSection "Fler i teamet" (**linked**) | | | | |
| **lead-magnet** (7) | AlternativHero (benefit-H1, breadcrumbs) | Tool/Calculator (**untouched** — approved rendering; webhook + error-phone verified week 1, LM-01/02) | VarProcess (magnet copy: "skicka kalkylen → vi ringer inom 24 h") | FAQ (build for energi/laddbox/elcentral) | MainContact | | | | | | | | | |
| — /ampy-eljour/ | AltHero-H1 → symptom block → **call-only close** (MainCTA-ring, no form) | | | | | | | | | | | | | |
| — /elkollen/ | wrap + **verdict bridge** → prefilled service-page form before MainContact (LM-09) | | | | | | | | | | | | | |
| **thank-you** (1) | Confirmation card (calibrated: "inom 24 timmar" + "samtalet kommer från 010-265 79 79 — spara numret", tel:/vCard) | **"Så förbereder du dig"** checklist (per form_type) | **"Du kommer att prata med"** (2–3 team faces) | **"Medan du väntar"** (ROT/GT + relevant kalkylator, service-first order) | Anchored review snippet | *Tech: noindex + conversion on submit-event, TY-1/TY-03* | | | | | | | | |

### Named overrules (where this table contradicts a template file, and why)

- **\*¹ service-pages.md** placed Testimonials at slot 7 (below ContentBlock) arguing the 12 reviews are generic. Overruled to slot 4: the generic-proof objection is solved at block level by vertical-pinning (testimonials.md T-02 fix), after which early proof wins on Cialdini/Clarity-trust-seeking grounds and matches 5 of the other 6 money templates. Trade-off: until the CPT review-tagging ships, service pages show generic reviews one slot earlier — acceptable, because the TrustStrip above already carries the verifiable proof.
- **\*² service-pages.md** put VarProcess at slot 5 ("directly after the ask"). Overruled: VarProcess sits in the pre-close stack (…→ VarProcess → FAQ → MainContact) on ALL templates. One rule beats two; var-process.md verified this placement already correct on 132/212 pages, and its step-1 copy ("Fyll i formuläret…") only makes sense when the form is adjacent (VP-4). Trade-off: hero-form submitters read the process *after* their submit — mitigated by the 24 h-microcopy under the hero submit button.
- **\*³ geo-elektriker.md** ordered Metrics → MainCTA → ServicesGrid → Testimonials (slots 3–6). Overruled per testimonials.md T-05: Testimonials moves ahead of the phone band on elektriker-i/eljour-i (112 pages) — the page must show one human proof before its first hard phone ask. The ServicesGrid drops one slot; its routing job is not time-critical.
- **FAQ position is unified above MainContact everywhere** (faq.md FAQ-01) — this overrules the live order on 131 pages and the block-map order in elektriker-i/elinstallation-i/elektriker-för-X files' "current" sections; the laddbox-i order (FAQ→form) was already right and becomes the site rule (objections answered, then the ask — MECLABS HealthSpire).
- **Incentive blocks (ROT/GrönTeknik) move above the form** on all geo/service templates (incentive-blocks.md INC-04 overrides live idx 11–16); product pages already correct. The eljour Hemförsäkring twin replaces ROT wholesale (INC-01 P0: "Läs mer om ROT-avdrag" button on an insurance block, 57 urgent pages).
- **homepage.md's owner-floated sequence** was already adjusted inside that file (ServiceGrid preserved, ProductTeaser instead of deletion, MainCTA after VarProcess); this table adopts that verdict unchanged.

---

## 3. BLOCKS TO KILL / MERGE (reconciled across all 20 block audits)

### Kill as standalone (retire the instance, keep any SEO text in DOM)

| Block | Scope | Verdict + source |
|---|---|---|
| **MikroCTA** | 173 geo/pillar pages | **KILL.** Its two jobs (form-ask, phone-ask) are done better by anchored CTAs and the PhoneBand; "Vill du veta mer?" is the weakest ask on any page and carries the unanchored "Sveriges snabbast växande" superlative (cta-bands CTA-02/03; geo-eljour, geo-elektriker, elinstall/laddbox wireframes all cut it). **The shell survives in exactly three repurposed roles:** B2B Serviceavtal-CTA (elektriker-för-X org pages), team-page close, and the article "Nästa steg" base component. |
| **BlueCTA** | 230 pages | **MERGE → PhoneBand.** One phone band per page: keep Blue's single-button clarity + light surface (visual relief between navy blocks), take MainCTA's trust row *once anchored*, fix the fake-link underlined H2 and the off-token black button (#212121 → midnight #090b32) (cta-bands rec 3; main-cta MC-4). Homepage instance replaced by PhoneBand *below* Testimonials (proof-then-ask, CTA-05). |
| **MainCTA** | 268 pages | **MERGE → PhoneBand** (the surviving half). "60 sekunder" claim owner-verified or reworded; rating anchored; intent-matched H2 per CPT (laddbox/eljour variants). |
| **FooterSEO** | 290 pages | **MERGE → Terminal.** Retired as a standalone section; reframed last-chance close ("Fortfarande osäker? …") folded into the top of the Prefooter — one fewer full-height section on every page, ACF text kept in DOM, CTA pair → `#main-contact` + tel, "radgivning"/"{Ort}'s" defects fixed (footer-seo rec 3–4). |
| **Product popup offert form** (29890/29891) | 26 money pages | **KILL as primary path.** Replaced by inline 3-field product-prefilled form in ProductHero ("vi ringer inom 24 timmar"). If kept at all: 3 required fields + standard consent checkbox + events, as secondary only (product-blocks PU-1/PU-3; product-pages PP-04). |
| **Popup 30855 (installation scope)** | 26 pages | **Content promoted on-page** as "Vad ingår i priset?" accordion (best candour copy on the site, currently hidden behind a popup-inside-an-accordion, PP-06); popup demoted to secondary. |
| **Legacy /elinstallation/ pillar form** ("Alltid fasta priser… Få ditt förslag") | 1 page | **KILL**, replace with MainContact — third form system, contradicted claim (PIL-08). |
| **VisualCTA** | /om-oss/ only | **KILL** (metrics-blocks VIS-01/02: duplicates the form one block below at the cost of a page load; "equally defensible: delete" — this file picks delete for ask-budget discipline). |
| **MainContact's embedded 3-step strip** | 295 pages | **KILL where VarProcess directly precedes** (the double-process defect, VP-6/MC-04): the pane keeps quote + anchored rating + anchored volume line; "Vi ringer dig inom 24 timmar" moves to microcopy directly under the submit button (mobile-critical). |
| **Homepage 8-card ProductGrid + homepage BlueCTA** | 1 page | **KILL / replace** with the 2-card ProductTeaser (HP-01/02: commercial-priority inversion + 33 000-kr price anchor + 8 pre-proof exits). Grids live on in full on their pillar/hub pages. |
| **MiniMenu + homepage ServiceGrid** | 1 page | **MERGE → ServiceRouter** — one decision surface after the hero (HP-13, Hick's law); service row first, 2 slim category cards second. |
| **Duplicate mobile spec/process accordions** (ProductHero) | 26 pages | **DE-DUPE** to one instance repositioned with CSS order (PH-1 — LCP-viewport weight). |
| **`hidden-on-load` enterView gates on conversion/trust blocks** | site-wide | **KILL** on MainContact, Metrics, VarProcess, Certificates, ContentBlock text, AlternativHero, FooterSEO/Terminal, elservice grid. Verified live: sections render at opacity:0 for fast scrollers (browser observation #2) — a form must never depend on an animation to exist (MC-09, MET-08, VP-7, CERT-05, AH-02, CAT-01). |
| **Reddit social link + "Support" label** (footer) | 325 pages | **KILL/rename** (FTR-03). |

### Keep — explicitly, because someone proposed otherwise

- **ServiceGrid** (homepage + geo): homepage.md rejected the owner's deletion instinct — it is the #1-priority router and the /elservice/* internal-link hub. Moved up, never removed.
- **ProductGrid on laddbox-i**: elinstall/laddbox file's verdict stands — keep near top (its "Fr."-prices are the best price-anxiety reducer on the template) but rewire: 3 cards, dual CTA where primary "Få pris installerad i {ort}" pre-fills the on-page form, caveat line reconciling grid vs FAQ price (GEO-05/09). Overrules any instinct to treat it like the homepage grid: geo laddbox intent is partly product-choice; homepage intent is not.
- **Testimonials slider V1** (locked): config-level fixes only (anchored badge, vertical pinning, mobile peek + sub-line restore — owner-gated visual diffs); static-grid challenger parked to V2 (T-04).
- **MapBlock**: keep as the geo link engine, but deterministic list (kill the random 20-of-56 lottery), sub-card rewritten to *answer* not ask ("Vi täcker hela Sverige. Hittar du inte din ort? Ring…" → tel:/anchor, not /kontakt/), + the new **"Alla områden" hub** as the stable mesh anchor (MAP-01/02/03/07). Week-1 candour fix: the eljour "Se alla områden … i listan nedan" sentence (MAP-04).
- **VarProcess**: becomes THE one process block (see kill of MainContact's strip); timed steps synced to the 24 h promise; step 2 becomes the price-transparency step ("Kostnadsfri offert — skriftlig, fast pris där det går"); eljour gets a Ring-först variant (VP-1/2/5).
- **Certificates wall**: stays at the tail for bottom-up readers, but its verifiable core is **cloned upward** as the TrustStrip + a verification line inside MainContact's pane — the ESV registry deep-link (`?foretag=12047521`) is the single strongest trust asset on the site and currently a 49 px anonymous logo three blocks from the footer (CERT-01/A). Skatteverket/Naturvårdsverket/Rexel demoted out of the wall (CERT-02). |

### New blocks this architecture requires (build list)

**TrustStrip** (site-wide, extracted from Certificates+rating) · **Prisblock** (service pages; content exists in FAQs) · **PhoneBand** (MainCTA×BlueCTA merge) · **ServiceRouter** (homepage merge) · **ProductTeaser** (homepage) · **JourProof-strip** + **Pris & hemförsäkring** + **Two-lane contact** (eljour) · **OrgTrustStrip** + **Serviceavtal-CTA** + **Referenser** interim (B2B) · **"Vad ingår i priset?"** (products) · **"Nästa steg" card** + inline article CTA + mobile sticky mini-bar (articles) · **Expert-CTA card** (team, pattern exists on products) · **Contact header / Vad händer sen / facts card** (kontakt) · thank-you blocks 2–5 · **"Alla områden" hub** (1 per CPT or tabbed).

---

## 4. THE /KONTAKT/ PARADOX — sequencing the fix

**The paradox:** ~900 CTA instances converge on /kontakt/ (header CTA ×325, CEBlock ×~290, FooterSEO ×~290, hero buttons, Map sub-cards, VisualCTA — GLOB-02, priority 2 925, the highest single score in the audit), and the destination is the weakest page on the site: no H1, 386 words, no visible phone number above the footer, 5 required fields incl. street address, trust pane before form on mobile. Meanwhile ~600 of those instances *shouldn't navigate at all* — a form sits on their own page. Which do you fix first?

**Resolution: destination first, retarget second — with two hard prerequisites before any retargeting.** Reasoning: (a) fixing /kontakt/ is ONE page edit that instantly improves all ~900 instances, including the ~325 header clicks that will keep navigating there forever; (b) retargeting without prerequisites is actively dangerous — the enterView bug means `#main-contact` can be an *invisible* block, and with zero form instrumentation no retargeting effect is measurable; (c) retarget-first would strand header traffic on a broken page for weeks while 224 templates are edited.

| Phase | Week | Work | Why this order |
|---|---|---|---|
| **0 — Prerequisites** | 1 | (a) Instrument every form: `form_start` on first focus, field-abandon, error, submit events, consent-gated (H2-02, MC-07, SVC-10 — GA4's "0 form starts" makes everything else unmeasurable). (b) Remove `hidden-on-load` from MainContact + give it the stable `#main-contact` id on all templates. (c) /thank-you: `noindex` + conversion moved from pageview to submit-event (TY-03 — protects the dependent variable of the whole program). | You cannot judge any CTA change without (a); you must not anchor to an invisible target without (b); every conversion count is corruptible without (c). |
| **1 — Fix the destination** | 1–2 | /kontakt/ per §2 row: H1, phone row + öppettider [GAP], label canon ("Kostnadsfri rådgivning" chain end-to-end), Adress → optional, mobile form-first, "Vad händer sen" + mini-FAQ + facts card. Same sprint: header gains the visible phone number (HDR-01) and the header CTA label unifies. Also GLOB-14: on /kontakt/ itself the header CTA becomes the phone CTA (self-link today). | One edit, ~900-instance blast radius, and the header path (which stays a navigate per §1.2) is fixed permanently. KO-1 evidence: the page currently *suppresses* the one conversion (phone) that demonstrably works. |
| **2 — Retarget body CTAs to anchors** | 2–4 | Template-by-template, biggest reach first: geo CPTs (224 pages: hero → aof focus; Mikro-before-kill/Map/CE/Terminal → `#main-contact`), then service (22), products (26: CE/FooterSEO → on-page MainContact), elektriker-för-X (13), om-oss. Ship the SSR hero form (H2-07/GEO-02) in the same template pass — the anchor target on screen 1 must exist at first paint. | This is the ~600-instance friction removal (GEO-01 ×2, EFX-03, FS-2, CTA-01: each removed navigation saves a ~800 kB / 9–10 s page load at peak intent). Measured via the Phase-0 events. HYPOTES (primary A/B): anchor vs navigate lifts form starts/session without reducing tel clicks. |
| **3 — Thin the asks** | 4–8 | Kill/merge rollout from §3 (Mikro retire, PhoneBand merge, Terminal fold, popup→inline). Only after Phase 2: retargeted-but-redundant bands reveal in the new event data which slots genuinely earn clicks before deletion. | Retarget-then-thin is reversible and evidence-generating; thin-then-retarget destroys the baseline. |
| **4 — Later tests** | 8+ | HYPOTES: header CTA anchor-on-form-pages vs uniform navigate (only after Phases 1–2 are stable). HYPOTES: /kontakt/ ends up serving mostly header + no-form-page traffic — measure whether it should become a phone-first micro-page. | Chrome experiments last; they ride on a fixed destination and clean events. |

**What /kontakt/ is *for* after this:** the permanent destination of chrome + form-less pages, and the fallback for shared/external links — not the site's conversion engine. The engine is the on-page form every body CTA now scrolls to.

---

## 5. Candour-gate ledger the architecture depends on (owner inputs, [GAP])

1. Current Google rating + review count → unlocks the anchored "5,0 av 5 · N recensioner på Google" pattern used in TrustStrip, PhoneBand, hero rows, MainContact, thank-you (unanchored "5.0" verified in ≥6 blocks/page; article template's "5.0 · 25 omdömen" is the model).
2. ONE canonical volume fact with unit ("3 000+ installationer om året" vs "över tusen genomförda") — the 1000+/3000+ contradiction ships on the same scroll on 114+ pages (MET-02, OM-1, GEO-04).
3. "Prata med en elektriker inom 60 sekunder" — confirm as SLA or the two-lane rewording ships instead (MC-3).
4. Jour: real phone-answer SLA + fast inställelseavgift (dag/kväll/helg) for the eljour Pris-block (GEO-ELJ-03/07).
5. "SUPERKAMPANJ" tags, "Sveriges snabbast växande elfirma", "marknadens billigaste priser" — anchor, verify, or drop (PG-3, F7, PIL-10).
6. B2B reference collection start (EFX proof gap) + review vertical-tagging in the CPT (T-02).

## 6. Top test hypotheses at the architecture level (A/B)

1. **HYPOTES (anchor vs navigate):** Retargeting all body "Kostnadsfri rådgivning" CTAs from /kontakt/ to `#main-contact`/aof anchors on geo+service templates increases form submits per session without reducing tel clicks (prereq: Phase-0 instrumentation + SSR form).
2. **HYPOTES (ask budget):** The 5-slot ask ladder (13→5 body asks) on elektriker-i does not reduce total conversions (calls+forms) and increases per-ask CTR — validating that repetition, not opportunity, was the constraint (cta-bands CTA-02).
3. **HYPOTES (temperature split):** Phone-primary hero on eljour-i lifts tel-clicks/session ≥30 % vs the form-first control; form-primary SSR hero on service pages lifts form starts from ~0 — the two halves of the dominance rule tested against each other's controls.
4. **HYPOTES (proof-before-ask):** Testimonials at slot 4 + TrustStrip at slot 2 vs live order lifts combined conversion on the 112 elektriker-i/eljour-i pages (T-05, MECLABS anxiety-before-ask).
5. **HYPOTES (destination fix):** The /kontakt/ rebuild alone (Phase 1, before any retargeting) lifts conversion-per-/kontakt/-session — isolating destination quality from routing friction.
