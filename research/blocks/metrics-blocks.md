# Metrics (`metrics`) + AboutMetrics (`about-us-metrics`) + VisualCTA (`visual-cta`)

**Used on:** 115 pages total (verified in `data/block-map.json`).
- **Metrics (number variant):** 114 pages — 56 × `elektriker-i` geo pages, 56 × `eljour-i` geo pages, plus the `/elektriker/` and `/eljour/` pillar pages.
- **AboutMetrics (no-number variant):** 1 page — `/om-oss/` only. NOTE: the block map double-counts `/om-oss/` as both "AboutMetrics" (idx 3) and "Metrics" (idx 4); the live page has exactly ONE `<section class="brxe-section metrics about-us-metrics">` — it is a single section carrying both class fingerprints. True unique-page total for the family: **115**.
- **VisualCTA:** 1 page — `/om-oss/` only (idx 5 of 9 blocks).

**Funnel position(s):** Prime post-hero real estate. On all 112 geo pages Metrics sits at **index 3 — the first block after `Hero_2` + `Hero_2-aof-form`** (verified sequence, e.g. `/eljour/akersberga/`: Header → Hero_2 → Hero_2-aof-form → **Metrics** → MainCTA → Testimonials …). On `/elektriker/` and `/eljour/` pillars it is index 2, directly after Hero-1. Mean position fraction 0.15 — top-of-page. On `/om-oss/` the sequence is Header → Hero-1 → ContentBlock → **AboutMetrics** → **VisualCTA** → MainContact → Prefooter.

**Verified live copy** (fetched 2026-08-02 from `https://ampy.se/elektriker/akersberga/`, identical on `/eljour/` and `/elektriker/` pillar snapshots):

> **1000+** / Nöjda kunder / "Över tusen genomförda installationer är vårt absolut starkaste kvalitetsbevis. Det är resultatet av att vi konsekvent levererar högsta elsäkerhet, snygga montage och håller vad vi lovar."
> **25+** / Erfarenhet i branschen / "Vår samlade yrkeskunskap resulterar i att vi aldrig behöver gissa. Vi dimensionerar och installerar din anläggning med en precision du alltid kan lita på."
> **20+** / Personer i teamet / "Vi jobbar med egna, auktoriserade elektriker istället för osäkra mellanhänder. Det ger oss förmågan att hantera alla installationer med full kvalitetskontroll i varje steg."

Live `/om-oss/` (fetched 2026-08-02) carries the **same three cards with the numbers stripped out** — headings "Nöjda kunder / Erfarenhet i branschen / Personer i teamet" + the same body text, no `1000+ / 25+ / 20+`. VisualCTA live copy: heading **"Ditt hem, vår spetskompetens"** + single black button **"Kontakta oss"** → `https://ampy.se/kontakt/`, over a full-bleed lazy-loaded image (`bk-img.webp`).

**Rendering (from snapshot CSS):** three dark cards (`numbers-bg.webp` navy background, white text `--color-3`), `min-height: 380px`, `max-width: 400px`, number at `--aptext-3xl` weight 600. Desktop: 3-across grid. ≤780px: cards go **full-width and stack vertically**; ≤480px flex column. Every card is `data-interaction-hidden-on-load="1"` with an enterView fadeIn (staggered delays 0 / 0.5 / 1.5s — note the third card's delay is authored as `"1,5"` with a comma, a locale-format bug worth checking in Bricks).

---

## What it does well

- **Right instinct, right position.** Placing scale/authority proof immediately after the hero+form is exactly where the trust-seeking Swedish homeowner wants it (Cialdini authority; the Clarity recording of a paid visitor going Contact → About Us is direct behavioral evidence of trust-seeking). The slot is correct — the contents are the problem.
- **Body copy is genuinely good candour voice.** "Vi jobbar med egna, auktoriserade elektriker istället för osäkra mellanhänder" answers a real Byggahus-class anxiety (who actually shows up?) and "auktoriserade" is a verifiable, regulated Swedish term. This is the strongest sentence in the block.
- Consistent token usage (ap* scale, radius, navy cards); clean stacking on mobile with no horizontal overflow.
- VisualCTA is at least honest: no fake urgency, one clear action.

## Issues

### MET-01 — "1000+ Nöjda kunder" is an explicitly banned claim — **P0** (desktop + mobile identically)
The business context bans asserting "1000+ kunder" as fact unless owner-confirmed current. It is live, in the largest type on the card, on **114 pages — including every geo page paid Google traffic lands on**. Candour gate: unanchored round-number social proof. Either the number is owner-confirmed and gets an anchor (source + "genomförda installationer sedan 20XX"), or it goes. **Evidence:** candour gate (business context §Brand guardrails); Cialdini — social proof only persuades when the skeptical reader can verify it; NN/g — users discount unattributed marketing numbers.

### MET-02 — Internal contradiction with MainContact on the same pages — **P0**
Metrics says "Över tusen genomförda installationer … vårt absolut starkaste kvalitetsbevis" (reads as ~1 000 total, ever). MainContact's photo pane — present on the **same** geo pages a few scrolls down — claims "**3 000+ genomförda installationer om året**". A visitor who reads both gets: strongest-ever proof = 1 000+, but also 3 000+/year. One of these is wrong, or the copy is sloppy; either way it is trust-corrosive for a risk-averse 35–65 audience, and rule 5 of the canon (flag internal contradictions) fires. **This is the single most important fix in the block.**

### MET-03 — Number/label/body mismatch on card 1 — P1 (both viewports)
The number says "1000+", the label says "Nöjda kunder" (customers), the body talks about "genomförda installationer" (jobs). Customers ≠ installations. MECLABS clarity: every element of a proof unit must point at the same referent, or the reader's System-2 flags it as marketing.

### MET-04 — "25+ Erfarenhet i branschen" is ambiguous to the point of being misleading — P1
No unit ("25+" what — år?), and positioned where every competitor writes "25 år i branschen" it reads as **company age**. The body reveals it is actually *combined team* experience ("Vår samlade yrkeskunskap"). But `/om-oss/`'s own H1 is "Sveriges snabbast växande elfirma" — a fast-growing challenger that appears to claim 25+ years in business will fail the allabolag.se sniff test that exactly this audience performs. HYPOTES (A/B): reframing card 2 as a *verifiable* authority claim ("Auktoriserade elektriker · registrerade hos Elsäkerhetsverket — kontrollera oss själv") beats "25+" on form-submit rate; Elsäkerhetsverket registration is the #1 proof a serious Swedish customer checks (business-context research anchor).

### MET-05 — "20+ Personer i teamet" unverifiable on-site — P2
The site's own team section/profile pages surface ~6–7 named electricians. If the real headcount is 20+, nothing on the site evidences it; if not, it's another inflated round number. `[GAP]` — owner to confirm current headcount; anchor it ("20 anställda, varav X auktoriserade elektriker — träffa teamet →" linking to the team slider) or drop the number.

### MET-06 — Zero message match with eljour intent on 56 eljour-i pages — P1
The eljour visitor's JTBD is urgent repair ("elfel i huset" is a real captured search term); Unbounce home-services benchmark: urgent/repair pages are the highest-converting category. Yet the first post-hero block shows them the identical installations/team trivia that elektriker-i pages get. The prime slot should carry jour-relevant proof (response promise "Vi ringer dig inom 24 timmar" — already claimed in MainContact — coverage hours, real jour jobs). Google message-match chain (ad → H1 → first screen) currently breaks at the first screen after the hero.

### MET-07 — Mobile cost: ~1 100–1 200 px of dark number-cards between the form and the real proof — P2 (mobile-specific)
Three stacked full-width cards at `min-height: 380px` push Testimonials (12 real Google reviews — the site's genuinely verifiable proof) a full ~1.5 viewports further down on the primary rendering. Baymard/NN/g mobile: every low-information screenful between arrival and credible proof raises abandonment risk. Compact the mobile rendering (single row of number chips, or horizontal scroll cards ≤160px) rather than deleting content.

### MET-08 — `hidden-on-load` + enterView fadeIn on a 9–10 s lab-LCP site — P2 (mobile-weighted)
Cards render invisible until Bricks interactions JS runs. On slow devices the first post-hero band is a blank navy strip. Also the third card's `animationDelay:"1,5"` (comma decimal) may not parse as 1.5 s. HYPOTES: removing hidden-on-load on this block is a free perceived-speed win; content should never be JS-gated on a trust block.

### ABT-01 — AboutMetrics is "metrics" with the metrics amputated — P1 (the one page it lives on)
On `/om-oss/` — the page trust-seekers demonstrably visit (Clarity: paid visitor went Contact → About Us) — the same three 380 px cards appear with **no numbers at all**: heading + paragraph floating in a card sized for a big numeral. It reads as a broken template. The about page is where the deepest proof belongs (founders, org.nr, Elsäkerhetsverket registration, real photos, review count) and it currently has a 725-word thin page whose "proof" block is the weakest variant on the site. If the numbers were removed *because* they couldn't be substantiated, that logic must apply to the other 114 pages too (candour consistency).

### VIS-01 — VisualCTA routes off-page while the site's best converter sits one block below — P2
"Kontakta oss" links to `/kontakt/`, but MainContact — "the strongest conversion asset on the site" per the inventory — is the **very next block** on the same page. The button adds a page load (9–10 s lab LCP) between intent and form: pure friction `f` in the MECLABS heuristic, for zero gain. Jakob's law: a CTA labelled "Kontakta oss" that jumps to a new page when the form is one scroll away surprises no one pleasantly.

### VIS-02 — VisualCTA headline is a slogan, not a value statement — P3
"Ditt hem, vår spetskompetens" states no outcome, no next step, no reason-why (Ogilvy/MECLABS clarity). Combined with an off-token black button (teal #00a991 is the brand accent) over a decorative photo, the block is a full-bleed image band whose entire measurable job duplicates the section below it. Mobile: same rendering, full-width image + centered heading + button.

---

## Recommended changes

1. **(P0, weeks 1–2) Resolve the number canon once, then propagate.** One owner session fixes 114 pages: confirm the true, current figures for installations (total vs per-year), team headcount, and what "25+" actually measures. Then rewrite the three cards so **number, label and body agree and every number carries an anchor** — copy-pattern direction: `"3 000+ installationer om året"* / *"Siffran från vår orderstock 2025"` or drop to the verifiable tier: `"Auktoriserad elinstallatör — sök oss hos Elsäkerhetsverket"`, `"4,9 av 5 · 120+ omdömen på Google"` (only with owner-confirmed rating + count; the unanchored "5.0" pattern elsewhere fails the same gate). Kill the MET-02 contradiction in the same pass by making Metrics and MainContact quote the *same* canonical figure.
2. **(P1) Fork the block per intent.** Keep one shared component, two ACF content sets: *elektriker-i* = authority set (auktorisation / installations / real review count); *eljour-i* = urgency-relevant set (response promise, jour coverage, real avg time-to-callback if measurable). No new block needed — this is content, not structure. SEO substance preserved (text stays in DOM, only differentiated — which also chips at the doorway-sameness problem flagged in the SEO audit).
3. **(P1) Rebuild AboutMetrics as the site's deepest proof unit, not its emptiest.** On `/om-oss/`: restore anchored numbers + add the verifiable artifacts (org.nr, Elsäkerhetsverket check link, team photo count matching claims). The Clarity evidence says this page is on the paid-conversion path — treat it as such.
4. **(P2) Compact the mobile rendering** of Metrics (chip row or reduced min-height) so Testimonials arrives ≤1 viewport sooner; remove `hidden-on-load` from the cards; fix the `"1,5"` delay value.
5. **(P2) VisualCTA — repurpose or retire.** Verdict on "worth keeping?": **not in current form.** Cheapest good option: change the button to an anchor-scroll to the MainContact form directly below (removes a page load) and give the heading a value line ("Berätta vad du behöver — vi ringer dig inom 24 timmar", reusing the already-claimed promise). Equally defensible: delete the block; nothing measurable is lost on a 9-block page whose next section is the form. Do NOT roll it out to more pages as-is.

## Test hypotheses (top 3, A/B-phrased)

1. HYPOTES: On eljour-i pages, replacing the generic Metrics set with an urgency-relevant proof set (response promise + coverage + anchored review count) increases calls+form submits vs. control.
2. HYPOTES: On elektriker-i pages, an anchored/verifiable card set (Elsäkerhetsverket + anchored Google rating + real installation figure) outperforms the current unanchored 1000+/25+/20+ set on form-submit rate.
3. HYPOTES: On /om-oss/, VisualCTA-as-anchor-scroll (vs. link to /kontakt/) increases same-session form submissions from om-oss visitors.

## Priority score (arithmetic)

| Block | Pages | Funnel weight | Expected effect | Score |
|---|---|---|---|---|
| Metrics | 114 | 2 (first block after hero/form; trust adjacency argues 3, scored conservatively) | 3 (banned claim + internal contradiction = trust-damaging, high) | **114 × 2 × 3 = 684** |
| AboutMetrics | 1 | 2 (mid-page on the trust-path page) | 2 (med) | 1 × 2 × 2 = **4** |
| VisualCTA | 1 | 2 (mid-page, pre-form) | 1 (low) | 1 × 2 × 1 = **2** |

**Family total ≈ 690, carried by Metrics. Severity P0** — not because the block design is broken (position and body copy are good) but because it broadcasts an explicitly banned claim and a self-contradicting number on every paid-landing geo page. The fix is cheap (one owner data session + one shared-component copy edit) relative to 114-page reach.
