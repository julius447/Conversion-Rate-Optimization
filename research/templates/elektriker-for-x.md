# Elektriker-för-X vertical template (13 pages)

URLs analyzed (live-fetched 2026-08-02): https://ampy.se/restauranger/ · https://ampy.se/bostadsrattsforening/ · https://ampy.se/kommuner/ (raw HTML + decoded `.aof` resolver script inspected for all three).
Pages using this template: **13** (from block-map, category `elektriker-for-x`): `/villor/ /radhus/ /bostadsrattsforening/ /foretag/ /kontor/ /butik/ /restauranger/ /hotell/ /idrottshallar/ /kommuner/ /byggforetag/ /entreprenad/ /tredjepartsinstallationer/`. All 13 share the **identical** block sequence and near-identical word counts (1 774–1 852 words) — one template, vertical keyword substitution.

**Audience split inside the template (critical):** only 2 of 13 pages are consumer (villor, radhus). The other **11 are B2B/BRF/public-sector pages** — fastighetschefer, BRF-styrelser, restaurangägare, kommunala upphandlare, byggbolag, laddbox-återförsäljare (tredjepart). These buyers have longer sales cycles, a procurement mindset, and evaluate on org-level proof (referenser, ramavtal, försäkring, ID06, dokumentation, LOU-vana). The template's SEO body copy IS verticalized per page; the **conversion layer (proof, CTAs, bottom form, process, footer) is consumer-generic** — that mismatch is the central defect of this template.

---

## Current block sequence (verified against block-map + live fetch)

| # | Block | Desktop behavior | Mobile behavior |
|---|---|---|---|
| 1 | Header | Mega-menus + "Gratis rådgivning" teal CTA → **/kontakt/** | Offcanvas accordion + "Ring en expert" + 5.0 |
| 2 | **Hero_2 + `.aof` form** | Left: breadcrumbs → **H1 = small eyebrow** ("Elektriker för bostadsrättsföreningar") → **H2 = big headline** ("Trygg elservice med fokus på er BRF!") → paragraph → CTA pair (Kostnadsfri rådgivning → **/kontakt/**, Ring tel:) → unanchored "5.0" row. Right: `#ampy-form-root` mount — form is **100% client-rendered JS** (empty div in HTML; curl shows no form text). | Stacks; form card renders below copy + CTAs, i.e. below the fold. If JS is slow (known ~9–10s lab LCP), the right column is empty on arrival. |
| 3 | Testimonials | "**Vad säger dina grannar om Ampy?** / Riktiga omdömen från riktiga jobb." — Splide slider, **12 consumer reviews** (lägenhetsrenovering, hembatteri, "elbox", "kanonjobb på uppfarten") + "5 av 5 Betyg på Google" badge. Sits **directly after the hero** on every page incl. kommun/BRF/byggföretag. | Swipe slider, 1-up; tall dark cards push all substance far down. |
| 4 | MainCTA | "**Prata med en elektriker inom 60 sekunder!**" + du-form paragraph + Ring-only CTA + "5.0 på Google". | Centered stack. |
| 5 | ContentBlock ×3 | The vertical SEO meat — genuinely page-specific: restauranger = "Robusta elinstallationer för storkök och krog"; BRF = "Säker elbesiktning och stamrenovering", "Trapphusbelysning"; kommuner = "Expertis inom offentlig upphandling av el", gatubelysning. | Image/text rows stack; long scroll. |
| 6 | VarProcess | "Så funkar det" 4 steps. **BUG: step 3 "Bokning bekräftad" carries step 4's text** ("Du får en rapport på allt som elektrikern gjort samt fullständigt underlag!") — verified identical on all 3 fetched pages ⇒ template-level, all 13. Step 2 also reads "Vi går vi igenom dina behov" (doubled "vi"). | 4 stacked cards. |
| 7 | MainContact | Left proof pane: quote, "5 av 5 · Betyg på Google", "3 000+ genomförda installationer om året", 3 steps ("Vi ringer dig inom 24 timmar"). Right form: **Förnamn/Efternamn/E-post/Telefonnummer/Adress/Postnummer/Postort/Meddelande — no company/org/BRF field at all** (verified in visible text + markup). | Panes stack; form below proof pane. |
| 8 | FAQ | 4 vertical-specific Q&As — the best B2B substance on the page (BRF: styrelsens juridiska ansvar, Ladda bilen-bidrag; kommuner: **LOU**, Klimatklivet; restauranger: brandskyddskrav, serviceavtal). | Accordion. |
| 9 | VissteDuAtt | Dark editorial band, vertical-specific ("rätt restaurangbelysning kan öka er försäljning?"). | Stacked card. |
| 10 | MapBlock | "Vi finns där du finns" — 20 Stockholm-orter buttons + "Vi är **din** elektriker … hela Sverige" + Kontakta oss sub-card. | Dot-map variant. |
| 11 | CEBlock | Long-form SEO + generic cross-sell list "Ampys behöriga installatörer kan även hjälpa **dig** med: Akut eljour som snabbt säkrar **ditt hem**…" (identical consumer list on kommun/BRF/B2B pages) + CTA pair (**"Kostnadsfri radgivning"** — missing å). | Stacks, 9:16 image. |
| 12 | Certificates | Logo wall: Elsäkerhetsverket, Skatteverket, Naturvårdsverket, **ID06, Trygg Hansa**, Rexel — the only org-level proof on the page, at position 12 of 14. | Cards wrap. |
| 13 | FooterSEO | Vertical superlative close ("Landets främsta elektriker för din bostadsrättsförening" / "Den offentliga sektorns främsta elektriker" / "Restaurangsbranschens främsta elektriker" — note restauranger has typo "Restaurangs-") + CTA pair ("Kostnadsfri radgivning" again missing å). | Stack. |
| 14 | Prefooter/Footer | Footer tagline on ALL pages: "Framtidens elfirma **för privatpersoner** som värderar kvalitet…" — asserted on 11 B2B pages. | Columns collapse. |

### The `.aof` hero form — verified (decoded resolver from live HTML)

The assignment asked to verify kundtyp prefill. **Confirmed working, and better than the rest of the page.** The `EFX` map in the inline resolver script prefixes every one of the 13 slugs:

- `villor` / `radhus` → `kundtyp:'privat'`, generic PRIVAT_OPTS.
- `bostadsrattsforening` → `kundtyp:'brf'`, **orgLabel "Föreningens namn"**, opts led by `'Laddbox'` (matches BRF demand).
- `kommuner` → `'foretag'`, orgLabel **"Förvaltning eller enhet"**; `idrottshallar` → orgLabel "Verksamhetens namn".
- `restauranger` → `'foretag'`, opts led by **"Storkök / fläkt / trefas"**; hotell/kontor/butik/byggforetag/entreprenad/foretag/tredjepartsinstallationer → `'foretag'` with tailored option orders.
- For org segments the required fields switch to **Orgnamn + Kontaktperson + Postnummer + Telefon + E-post** (address & orgnr move to optional "Fler detaljer"); the option list follows the *current* toggle segment, so a visitor who switches Privat↔BRF↔Företag gets the right list. Honeypot, GDPR consent, E.164, posts to Supabase `hero-lead`, redirects `/thank-you`.

Judgment: this is a genuinely well-adapted B2B intake. Its two problems are delivery, not design: (1) **no SSR fallback** — the entire hero conversion surface depends on JS executing on a page with a 9–10s lab LCP flag, and GA4 shows 0 form_start events; (2) the form card injects `<h1 class="title">Få kostnadsfri rådgivning!</h1>` at runtime ⇒ **two H1s in the rendered DOM** on all pages carrying it.

---

## Customer-flow walkthrough (BRF-styrelseledamot on mobile, from Google "elektriker brf")

**0–5 s:** SERP title "Elektriker för BRF – Säkra fastigheten & sänk elkostnaderna" → lands on H1/H2 "Elektriker för bostadsrättsföreningar / Trygg elservice med fokus på er BRF!". Message match is good (Google message-match principle holds). She sees two buttons and an unanchored "5.0". The form (her likely conversion path — boards write, they don't cold-call) has not rendered yet or sits below the fold.
**Scroll 1:** the first content she meets is a consumer review slider addressed to "dina grannar" quoting private-villa jobs ("elbox på uppfarten", "belysningen i hela lägenheten"). Cialdini similarity/social-proof: proof persuades when the prover resembles the prospect — zero of 12 reviews are from a BRF, förvaltare or company. HYPOTES-level risk: she reads Ampy as a villa-firma.
**Scroll 2–3:** "Prata med en elektriker inom 60 sekunder!" (call-pressure framing for an urgent consumer, not a board doing due diligence) → then the genuinely relevant ContentBlock (stamrenovering, trapphusbelysning, styrelseansvar) → the 4-step process where step 3 and 4 say the same sentence — exactly the kind of sloppiness a procurement-minded reader screens for.
**Decision point:** MainContact form asks **Förnamn/Efternamn/Adress** — no field for the förening's name or her role. She either self-translates into a consumer form (friction + anxiety: "will they understand this is a 90-apartment property?") or scrolls back to the hero form she never noticed. MECLABS heuristic: motivation is high, value clarity OK, but *i* (incentive to act here vs. request offerter from 3 firms) is weak because org-level proof (referenser, ramavtal, försäkring, ID06) never appears until a logo wall at position 12. The Clarity "Contact → About Us" trust-seeking pattern predicts exactly this audience.

The kommun visitor's walk is harsher: an upphandlare finding LOU competence only inside FAQ item 2, consumer reviews up top, "säkrar ditt hem" in the cross-sell list, and a Stockholm-ort link wall — on a page whose job is to earn a spot on a ramavtal shortlist.

---

## What works (keep)

1. **The `.aof` hero form's per-vertical intelligence** — kundtyp prefill, org-specific labels ("Föreningens namn", "Förvaltning eller enhet"), Kontaktperson instead of Förnamn/Efternamn, vertical option orders (BRF→Laddbox first, restaurang→Storkök first), address demoted to optional. This is the template's best conversion asset; the fix is delivery/visibility, not redesign.
2. **Vertical SEO body copy is real, not doorway-thin in substance** — storkök load capacity, stamrenovering, LOU, Klimatklivet, gatubelysning, styrelsens juridiska ansvar. Preserve all of it (method doctrine: re-sequence, never delete).
3. **FAQ blocks answer genuine B2B decision questions** (MECLABS HealthSpire: content that answers real questions lifts conversion when sequenced right — these deserve promotion, not burial at position 8).
4. **Message match SERP→H-copy** is solid on all three fetched pages.
5. **Certificates content is exactly the right proof** (ID06, Trygg Hansa, Elsäkerhetsverket) — wrong position, right substance.
6. Breadcrumbs, du-tilltal voice, and the two-conversion discipline (every CTA is call or form) are intact.

---

## Findings

**EFX-01 — Consumer proof layer on 11 B2B pages** · **P0** · Evidence: Cialdini similarity + social proof; JTBD (the board's job is "defend this choice to members/kollegor"). Testimonials block headed "Vad säger dina **grannar** om Ampy?" with 12 private-consumer reviews sits directly after the hero on kommun/BRF/byggföretag/entreprenad pages; footer asserts "Framtidens elfirma **för privatpersoner**"; CEBlock cross-sell list says "säkrar **ditt hem**" on public-sector pages. Mobile: the slider is the entire second screen, so the mismatch is the first thing a mobile B2B visitor reads. Fix: B2B pages get a filtered/replacement proof block (real org reviews/case references — **[GAP]: none exist in the current review set**; interim = re-head the block "Vad säger våra kunder", drop "grannar", and pull the 2 most org-plausible quotes forward) + a vertical footer tagline variant. Priority: 11 pages × mid-funnel 2 × high 3 = **66**.

**EFX-02 — No org-level proof until position 12; no references/ramavtal/försäkring block exists** · **P0** · Evidence: MECLABS anxiety term; Konsumentverket/procurement norm (written quotes, documented credentials); Clarity About-Us trust-seeking recording. The proof a fastighetschef needs (ID06, Trygg Hansa-försäkring, Elsäkerhetsverket-registrering, serviceavtal/ramavtal capability, dokumentation) exists only as a bottom logo wall; "serviceavtal" appears in body text but has no block, no CTA, no anchor. Mobile: position 12 ≈ 8+ screens down. Fix: compact org-trust strip (logos + one line each) directly under the hero on the 11 B2B pages, and a "Serviceavtal & ramavtal" mini-block (NEW) before MainContact. Priority: 11 × 3 (hero-adjacent) × 3 = **99** — highest of the template.

**EFX-03 — Hero primary CTA leaves the page instead of using the on-page form** · **P0** · Evidence: verified href — "Kostnadsfri rådgivning" → `https://ampy.se/kontakt/` while the `.aof` form sits in the same hero; Jakob's law + friction (extra nav on a site with 9–10s lab LCP); Fitts on mobile (button above an unrendered form). Same href on header CTA, CEBlock, FooterSEO ⇒ ~5 off-page detours per page. Mobile: tapping the primary CTA triggers a full second page load. Fix: anchor-scroll to the hero form (or MainContact) on all Hero_2/CEBlock/FooterSEO instances; keep /kontakt/ only in header. Priority: 13 × 3 × 2 = **78**.

**EFX-04 — MainContact (the strongest converter) is not org-adapted** · **P0** · Evidence: verified fields Förnamn/Efternamn/E-post/Telefon/Adress/Postnummer/Postort/Meddelande — no Företag/Förening/roll field; Baymard: users judge forms by fit-to-task, and mislabeled fields create abandonment + garbage leads that the ~2 660 kr täckningsbidrag economics can't absorb in qualification time. Inconsistent with the hero form 6 screens earlier that DID ask "Föreningens namn". Mobile: this is the form most scrollers actually reach. Fix: reuse the EFX resolver to inject kundtyp + orgname/Kontaktperson into MainContact on the 11 B2B pages (component variant, not a new form). Priority: 13 × 3 × 2 = **78**.

**EFX-05 — Hero form is JS-only with no SSR fallback + no form_start signal** · **P1** · Evidence: `#ampy-form-root` is an empty div in served HTML (verified); business context: GA4 recorded **0 form starts** on paid traffic; lab LCP 9–10s. A slow or failed script = a hero with a blank right column on all 13 pages (and every other Hero_2 page). Mobile on 4G is the worst case. Fix: (a) emit `form_start`/field-interaction events from the aof script; (b) render a minimal static fallback (name+phone+GDPR) inside the root div, hydrated by JS; (c) defer non-critical scripts to protect form paint. Priority: 13 × 3 × 2 = **78**.

**EFX-06 — VarProcess step 3 duplicates step 4's text; step 2 "Vi går vi igenom"** · **P1** (trust-damaging polish, minutes to fix) · Evidence: verified identical on all 3 fetched pages: step 3 "Bokning bekräftad — Du får en rapport på allt som elektrikern gjort samt fullständigt underlag!" = step 4's text. NN/g: visible sloppiness lowers credibility of all other claims — lethal for procurement readers. Mobile: steps stack, bug fully visible. Fix: write real step-3 copy ("Vi bekräftar tid och elektriker…") — and for B2B pages reframe the 4 steps as offert → avtal → utförande → dokumentation. Priority: 13 × 2 × 1 = **26** but effort ≈ 0 → do in week 1.

**EFX-07 — Candour gate: unanchored and unverifiable claims** · **P1** · Evidence: candour doctrine — "5.0" must carry rating + count + source. Hero "5.0" row and MainCTA "5.0 på Google" have no count; "5 av 5 · Betyg på Google" (testimonials, MainContact) has no count; "**Prata med en elektriker inom 60 sekunder!**" is a service-level promise with no stated basis ([GAP]: owner-confirm or soften to "Ring oss – du kommer direkt till en elektriker"); "3 000+ genomförda installationer om året" needs owner confirmation as current. Superlatives ("Landets främsta…") are allowed per owner directive unless demonstrably false — no action, but they carry more weight once real proof is adjacent. Mobile: same. Priority: 13 × 2 × 2 = **52**.

**EFX-08 — Heading architecture: H1 = small eyebrow, big headline = H2, second runtime H1 from the form card** · **P2** · Evidence: verified heading extraction (h1 "Elektriker för bostadsrättsföreningar" as eyebrow; h2 "Trygg elservice…" as visual headline) + decoded formCard markup `<h1 class="title">Få kostnadsfri rådgivning!</h1>` injected client-side ⇒ rendered DOM has two H1s (Google renders JS). NN/g heading hierarchy + a11y. Mobile: unchanged. Fix: form title → `<p class="title">` or h2 (one-character-class change in the aof script); longer term resolve the Hero_2 H1/H2 inversion site-wide (owned by the Hero_2 block audit). Priority: 13 × 1 × 2 = **26** (template share; the block itself spans far more pages).

**EFX-09 — "Kostnadsfri radgivning" (missing å) in CEBlock + FooterSEO CTAs; "resturangmiljö" (restauranger hero); "Restaurangsbranschens"** · **P2** · Evidence: verified strings; same credibility logic as EFX-06, and Swedish-orthography errors in a CTA are noticed by exactly this 35–65 audience. 2 instances × 13 pages (+ restauranger extras). Priority: 13 × 1 × 2 = **26**, effort ≈ 0.

**EFX-10 — MapBlock: 20 Stockholm-orter + "din elektriker" consumer framing mid-page on B2B/national pages** · **P2** · Evidence: internal-linking value is real (keep for SEO), but on /kommuner/ the wall of consumer geo links interrupts the procurement narrative and the "hela Sverige" claim sits beside a purely Stockholm list (copy may claim national per owner directive; the visual contradiction is a coherence issue, not a rules issue). Mobile: a full screen of buttons. Fix: move below CEBlock on B2B pages; retitle toward "Verksamhetsområden". Priority: 11 × 1 × 2 = **22**.

**EFX-11 — Sequencing: proof-irrelevant slider occupies the decisive second screen; FAQ (best B2B content) at position 8** · **P1** · Evidence: MECLABS HealthSpire — length is fine, ORDER is the variable; NN/g F-pattern: screens 2–3 get the attention. Current order hero → consumer testimonials → phone-pressure CTA → value props inverts the B2B decision sequence (who are you / can I trust you at org level / what exactly do you do for my vertical / how do we start). Mobile: worse because each block is a full screen. Fix: see wireframe. Priority: 11 × 2 × 3 = **66**.

**EFX-12 — 13 near-identical ~1 800-word pages: differentiation is real but shallow at the decision layer** · **P2** · Evidence: word counts 1 774–1 852; identical block chain; body copy varies but every trust/process/CTA/footer element is shared. Not a delete-content case (SEO preserved) — a "one B2B layout variant" case: the template needs TWO conversion skins (consumer: villor/radhus keep current pattern; org: the other 11 get org proof + org forms). Also note /tredjepartsinstallationer/ is a partner-channel pitch ("Ni säljer, vi installerar!") wearing the same skin — it deserves the org variant most of all. Priority: 11 × 2 × 2 = **44**.

---

## Recommended sequence (wireframe — org variant, applies to the 11 B2B/BRF/public pages)

| # | Block | Why here | New/existing/modified |
|---|---|---|---|
| 1 | Header | unchanged | existing |
| 2 | Hero_2 + `.aof` form | Keep the verified per-vertical form; fix: primary CTA anchors to form, form title de-H1'd, static fallback fields, form_start events, anchored rating ("4,9 av 5 · N recensioner på Google" — [GAP] owner-confirm current) | modified |
| 3 | **Org-trust strip** (NEW, compact) | ID06 · Trygg Hansa-försäkrade · Registrerade hos Elsäkerhetsverket · "3 000+ installationer/år" (if confirmed) — the procurement screening questions answered in one band before anything else | new (recompose Certificates assets) |
| 4 | ContentBlock ×3 | The vertical value props move up to the first reading zone (HealthSpire sequencing) | existing, re-positioned |
| 5 | VarProcess (B2B-framed) | Fixed step 3; steps reframed offert → avtal → utförande → dokumentation & rapport — mirrors how orgs buy | modified |
| 6 | **Referenser/case block** | Org-matched proof at the decision point. [GAP]: no B2B reviews/cases exist today → interim: re-headed testimonials without "grannar", org-plausible quotes first; collect BRF/company reviews as an owner action | new (interim: modified Testimonials) |
| 7 | FAQ | Promoted: LOU/styrelseansvar/serviceavtal answers belong beside the decision, not below the fold ×8 | existing, re-positioned |
| 8 | **Serviceavtal/ramavtal mini-CTA** | Named offer for the long-cycle buyer ("Vill ni ha en långsiktig elpartner? Boka ett avtalsmöte") — a lower-commitment ask matching procurement pace, still ending in call/form | new (Mikro_CTA variant) |
| 9 | MainContact (org variant) | kundtyp-aware fields (orgnamn + kontaktperson via the existing EFX resolver); proof pane quote swapped to org-relevant | modified |
| 10 | VissteDuAtt | Light editorial stays — correct register per canon | existing |
| 11 | CEBlock | SEO tail intact; cross-sell list gets an org version (drop "ditt hem" on B2B); fix "radgivning" | modified |
| 12 | MapBlock | Internal linking preserved, demoted below the conversion path | existing, re-positioned |
| 13 | Certificates (full) | Full wall remains for the thorough reader | existing |
| 14 | FooterSEO + Footer | Superlative close kept; org footer tagline variant replaces "för privatpersoner" | modified |

Consumer variant (villor, radhus): keep current order but apply EFX-03/05/06/07/09 fixes; testimonials stay as-is ("grannar" is *right* there).

## Test hypotheses (top 3, A/B)

1. **HYPOTES (proof match):** On the 11 org pages, replacing the consumer testimonials slot with the org-trust strip + re-headed proof (variant B) vs. current (A) increases form submits + tel-clicks per session. Rationale: Cialdini similarity; Clarity trust-seeking pattern. Primary metric: conversions/session; guardrail: scroll depth to ContentBlock.
2. **HYPOTES (CTA destination):** Hero "Kostnadsfri rådgivning" anchor-scrolls to the `.aof` form (B) vs. navigates to /kontakt/ (A) increases form starts (once form_start is instrumented) and reduces pre-conversion exits, mobile-first. Rationale: friction + 9–10s LCP double page-cost.
3. **HYPOTES (org form fields):** MainContact with kundtyp-aware Orgnamn+Kontaktperson fields (B) vs. current consumer fields (A) on B2B pages increases *qualified* submissions (lead contains org name; sales-accepted rate as true metric) without lowering total submits — Baymard fit-to-task over raw field count.

## Owner items / [GAP]s surfaced

- [GAP] Current Google rating + review count for anchoring every "5.0"/"5 av 5" instance (≥6 blocks on this template).
- [GAP] "Prata med en elektriker inom 60 sekunder" — confirm as operationally true or soften.
- [GAP] "3 000+ genomförda installationer om året" — confirm current.
- [GAP] Zero B2B/BRF reviews or named references exist in the proof pool — start collecting (BRF chair quotes, company service-avtal references); interim wording ships without invented proof.
- Copy bugs fixable immediately: VarProcess step 3, "Vi går vi igenom", "Kostnadsfri radgivning" ×2/page, "resturangmiljö", "Restaurangsbranschens".
