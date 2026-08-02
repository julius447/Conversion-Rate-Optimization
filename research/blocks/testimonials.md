# Testimonials slider — `ampy-testimonials` (V1 LOCKED)

Used on: **291 of 326 pages** (from `data/block-map.json`) | Funnel position(s): high-mid — body position 2–5, one of the very few trust blocks ABOVE the SEO content on money templates.

**Category breakdown (pages / body position, Header excluded):**

| Category | Pages | Position | Immediately after |
|---|---|---|---|
| elektriker-i | 56 | 5 | Metrics → MainCTA |
| elinstallation-i | 56 | 3 | Hero_2 + aof-form |
| eljour-i | 56 | 5 | Metrics → MainCTA |
| laddbox-i | 56 | 4 | ProductGrid |
| service | 22 | 3 | Hero_2 + aof-form |
| ev-product | 16 | 2 | ProductHero |
| elektriker-for-x | 13 | 3 | Hero_2 + aof-form |
| battery-product | 10 | 3 | ProductHero/Calculator-UI |
| page (incl. homepage) | 6 | 2–6 | varies (homepage: after BlueCTA, pos 5 incl. MiniMenu) |

Not present on: lead-magnet (7), post/articles (11), team-member (6), 11 misc pages. Neighbor stats sitewide: preceded by MainCTA (114), Hero_2-aof-form (91), ProductGrid (57); followed by MainCTA (128), VarProcess (113).

**Verified live** (fetched https://ampy.se/elservice/armatur/, 2026-08-02): header "Vad säger dina grannar om Ampy?" / "Riktiga omdömen från riktiga jobb." → 12 review cards (e.g. "Proffsig rådgivning inför vår installation. Känns tryggt att anlita experter." — Adam Andersson, mars 2026; "Ampy visade sig i konkurrens med andra aktörer både kunnigare och billigare. … Följdfrågor som uppstått efter en tids användning har besvarats kunnigt och utan dröjsmål." — Jan Fernström, juni 2026) → badge "**5 av 5** Betyg på Google" (gold stars, links to the Ampy GBP maps URL, `target="_blank"`).

**Verified mechanics** (from `data/pages/elektriker.html` markup): Splide loop, `perPage: 3` desktop → `2` @≤1024px → `1` @≤759px, `perMove: 1`, autoplay 4000 ms + 500 ms speed, `pauseOnHover/pauseOnFocus`, `arrows: false, pagination: false`, custom 4-dot growing nav (dot = `splide.index % 4`), client-side shuffle (`data-att-shuffle="1"`), server-rendered static fallback if Splide fails, `prefers-reduced-motion` kills autoplay. Cards: `linear-gradient(-27deg, #0b0f30 0%, #2d516d 60%)`, body text `font-weight: 300`, `rgba(255,255,255,0.95)`. Mobile CSS hides the sub-line: `.att-sub { display: none; }` @≤759px. JSON-LD Organization carries `aggregateRating: ratingValue 5.0, reviewCount 25` — the count exists in schema but is **never shown visibly**.

---

## What it does well

- **Real reviews, real names, real dates.** 12 genuine Google reviews with name + month/year (mars–juni 2026 — 2–5 months old at audit date, acceptably fresh). This is exactly the proof a trust-seeking 35–65 Swedish homeowner looks for (business context: the 47 s Clarity visitor who went Contact → About Us was trust-hunting). Candour-clean content — no invented proof.
- **Right altitude on the money templates.** On service, elinstallation-i, elektriker-for-x and product pages it sits at body position 2–3, directly under the hero + form — proof adjacent to the ask (MECLABS: reduce anxiety `−2a` at the point of decision). One of the only blocks above the SEO meat; the instinct is correct.
- **Specificity gems in the set.** Jan Fernström (price vs competitors + post-job follow-up), Mohammed Abduljaleel ("priset var rimligt … anlita dom igen"), Daniel Hellström ("var en annan firma här tidigare men dem klarade inte av det") answer the exact Byggahus/Reddit anxieties: final price, "will they answer later", competence. Filip Eriksson ("Blev rekommenderad av en granne") literally enacts the "grannar" headline.
- **Solid engineering & a11y for a slider.** Static server-rendered fallback, reduced-motion respected, pause on hover/focus, `aria-label` on section/badge/stars, badge links out to the verifiable GBP source (Cialdini social proof done honestly).
- **Headline framing.** "Vad säger dina grannar om Ampy?" is warm, local, on-voice.

## Issues

**T-01 — "5 av 5" badge is unanchored (candour gate + credibility).** Severity **P1**. Desktop & mobile identical. The visible badge says only "5 av 5 · Betyg på Google" — no review count, no "hämtat"-date. The schema on the same page says `reviewCount: 25`, and the badge links to the GBP where the count is one tap away — so the anchor exists but is withheld from the visible layer, which is the worst of both worlds: candour-gate exposure on the page AND a "why didn't they say how many?" moment on click-through. Evidence: candour gate ("5.0 must be anchored — rating + count + source — or removed"); Cialdini social proof is strongest when verifiable; NN/g trust research — vague superlatives are discounted, specifics are believed. Header, footer, MainCTA and Hero_2 repeat unanchored "5.0" ≥6 times sitewide (cross-block issue, logged here because this block owns the review evidence).

**T-02 — Shuffle destroys message match; proof is not vertical-relevant.** Severity **P1**. Desktop shows 3 random cards of 12; mobile shows 1 random card. On the armatur (lighting) page fetched live, only 1 of 12 reviews mentions belysning (Josephine Lundqvist: "Fick hjälp med belysningen i hela lägenheten"), while laddbox ("elbox"), hembatteri, elcentral and uppfart reviews rotate through. A visitor from "installera taklampa" (a real top search term per the paid investigation) has a ~1-in-12 chance of the first mobile card being about lighting. Evidence: Google message-match doctrine (ad → H1 → first screen must agree; proof is part of that chain); MECLABS `4m + 3v` — relevance is the heaviest coefficient. The shuffle is cache-safe engineering, but relevance was traded for rotation-fairness.

**T-03 — Mobile 1-up: weak swipe discoverability and misleading dots.** Severity **P2**. Mobile only (≥65% of paid/local traffic — doctrine: mobile is the primary rendering). At ≤759px the block renders ONE full-width card, `arrows: false`, no peek/partial-next-card (no `padding` in the breakpoint config), and 4 dots for 12 slides (dot = index mod 4), so the pagination under-reports the content 3×. Autoplay does advance the deck, but a user who touches the card pauses it (`pauseOnFocus`) and then has no visible cue that 11 more reviews exist. Evidence: NN/g carousel research — users need a visible signifier that content continues (cut-off/peek), dots are weak signifiers on touch; Baymard carousel findings — item counts must be honest. Additionally `.att-sub { display: none; }` on mobile deletes "Riktiga omdömen från riktiga jobb." — the one line that pre-frames the reviews as genuine — precisely on the primary rendering.

**T-04 — Auto-rotating slider suppresses 9 of 12 proofs (design-locked, log only).** Severity **P2**, flagged for the next design window since V1 is locked. Desktop: NN/g's carousel findings are unambiguous — auto-forwarding carousels are frequently ignored (banner blindness), users rarely interact past the first view, and motion next to reading text harms comprehension; a static 3×2/3×4 grid or a "load more" grid would expose the strongest reviews deterministically. The 4 s interval is also brisk for a 35–65 audience reading 40–60-word Swedish reviews (Jan Fernström's card is ~45 words — HYPOTES below).

**T-05 — Inconsistent slot on the trust-hungriest templates.** Severity **P2**. Desktop & mobile. On elektriker-i and eljour-i (112 geo pages — thin doorway pages where the visitor's trust question is loudest, and eljour is the Unbounce-benchmark best-converting urgent intent) the block sits at position 5, AFTER Metrics and MainCTA — i.e. the page asks for the call (MainCTA) before it has shown a single human proof. Service/elinstallation-i pages place it at 3, right under the form. Evidence: MECLABS anxiety reduction must precede or accompany the ask; Jakob's law — users transfer the "reviews near the top" pattern from marketplaces.

**T-06 — Dark navy cards, 300-weight text (design-locked, log only).** Severity **P3**. Cards are `#0b0f30→#2d516d` gradient with `font-weight: 300` white body text. Contrast ratio itself passes (white on navy), but thin-weight light-on-dark type is a known legibility risk (halation) for older eyes — the core 35–65 audience. Also contributes to the documented "dark block stacking" on pages where Hero_2 (navy) → Testimonials (navy) run back-to-back. Print CSS already inverts — the team knows. Note separately for V2; do not touch V1.

**T-07 — No refresh contract for recency.** Severity **P3**. The 12 reviews are a CPT snapshot (mars–juni 2026). Today they read fresh; by Q1 2027 every visible date will be >6 months old, which actively signals staleness ("riktiga omdömen" from long ago). No owner process is documented for rotating in new reviews. HYPOTES-territory prevention, not a current defect.

## Recommended changes

1. **Anchor the badge (T-01, content-only, no design change).** Change badge text pattern from "5 av 5 · Betyg på Google" → "**5,0 av 5 · [N] omdömen på Google**" where N is the owner-confirmed current GBP count (schema says 25 — confirm before shipping; keep schema and visible layer in sync). Direction, not final copy — route through ampy-rost. If the owner declines to show the count, the candour gate says soften the claim, not hide the anchor.
2. **Vertical-aware ordering instead of blind shuffle (T-02, JS/CPT change, zero visual change).** Tag each review in the CPT with vertical(s) (belysning, laddbox, batteri, elcentral, eljour, allmänt). Pin matching-vertical reviews to slides 1–2 (mobile slide 1), shuffle the remainder. On geo pages pin the most specific/price-addressing reviews (Fernström, Mohammed, Daniel) first. This is a 291-page relevance upgrade with V1's pixels untouched.
3. **Restore the sub-line on mobile (T-03, one CSS rule).** Delete `.att-sub { display: none; }` @≤759px (or shorten the line) — "Riktiga omdömen från riktiga jobb." is candour framing, not decoration. NOTE: this is a visual diff on a locked block → owner-gated per the approved-rendering rule; present as a 1-line before/after.
4. **Mobile peek (T-03, config-only).** Add `padding: { right: '3rem' }` (or `focus`+partial width) to the 759 breakpoint so the next card visibly enters the viewport — the NN/g-sanctioned continuation cue. Config value, not a card redesign; still owner-gated visual diff.
5. **Normalize the slot (T-05, re-sequencing, no block change).** On elektriker-i and eljour-i, move Testimonials from position 5 to position 3 (directly after Hero_2 + form, before Metrics/MainCTA) to match service/elinstallation-i. Proof before the second ask. 112 pages.
6. **Review-refresh contract (T-07, process).** Quarterly: pull newest GBP reviews, swap the 3 oldest cards, update the badge count. Add to the ops checklist, not the code.
7. **For the V2 window (T-04/T-06, parked):** static curated grid (top 6 by specificity) as the A/B challenger vs the slider; heavier body weight (400) on cards; consider per-vertical review sets.

**Test hypotheses (A/B-phrased):**
- HYPOTES: Anchoring the badge ("5,0 av 5 · 25 omdömen på Google") vs unanchored "5 av 5" increases form-submit + tel-click rate on service templates, because verifiable specificity is discounted less (Cialdini/NN/g).
- HYPOTES: Pinning a vertical-matched review as slide 1 vs random shuffle increases conversion on paid landing pages, because proof participates in message match (MECLABS 4m).
- HYPOTES: On mobile, a visible next-card peek vs full-width 1-up increases slider interaction and reviews-read-per-session (NN/g continuation cue), with downstream lift on trust-dependent geo pages.

## Priority score (arithmetic shown)

- Pages affected: **291**
- Funnel position weight: **2** (mid-page trust layer — adjacent to the hero form on most templates, but not itself the hero/form)
- Expected effect: **2** (medium — supporting evidence for the primary ask; the headline fixes are content/ordering, not a new conversion path)

**Priority score = 291 × 2 × 2 = 1164 → P1** (fix in month 1: badge anchor + vertical pinning + geo-slot move are low-effort, 291- and 112-page levers; locked-design items park to V2).
