# BRF-laddguiden — "Laddplatser i föreningen: beslut, bidrag, ansvar" (B2B track)

**Status: BUILD — phase 2 (months 2–3). The one B2B magnet worth building; strategic pre-positioning, not a quick win.**

## Job-to-be-done
The BRF-styrelseledamot's job is not "buy a laddbox" — it is **"prepare a decision the board can defend to members"**: teknik (lastbalansering, elkapacitet), ekonomi (bidrag, debiteringsmodell per medlem), juridik (styrelsens ansvar, avtal), process (offert → stämma → installation). No consumer calculator answers that; a decision-guide does. JTBD social dimension is dominant here: the artifact must be *forwardable* to the rest of the board — which is why this one, unlike the checklist, earns a downloadable/printable version.

## Evidence base (why this is white-space worth taking)
- The `.aof` resolver already leads BRF visitors with `Laddbox` as first option (verified in EFX research) — Ampy's own form data model says BRF-intent = laddbox-first.
- /bostadsrattsforening/ has 546 GSC impressions at position 57.7 — demand exists, rankings don't yet; a substantive guide is exactly the E-E-A-T asset that lane lacks (EFX-12: differentiation is "shallow at the decision layer").
- EFX-01/02: the B2B pages have consumer proof and no org-level trust until position 12; the guide is also a proof artifact ("they understand BRF-specifics") that no review set currently provides [GAP: org references].
- Laddbox = commercial priority #2, and BRF jobs are multi-charger installations — higher order value than the consumer lane.

## Anatomy
- **Primary form: a guide page** on the article shell (the site's best template: byline trio, Snabbt svar, TOC, FAQ) at e.g. /brf-laddguide/ — NOT a bare PDF page. ~2 500–3 500 words: beslutsprocessen steg-för-steg → elkapacitet & lastbalansering i flerbostadshus → bidrag och ekonomi → debiteringsmodeller → styrelsens ansvar & avtalspunkter → vanliga misstag → FAQ.
- **Forwardable version:** "Ladda ner guiden som PDF att dela med styrelsen" — soft-gated at most (namn + e-post + föreningens namn, optional telefon); the on-page HTML version stays fully ungated so SEO and the candour posture are intact. This is the one place a soft gate is defensible: the download's JTBD is literally "send to colleagues", and the org context makes the contact exchange a fair trade.
- **Close:** org-adapted ask — "Vi gör en kostnadsfri förstudie för er förening" → the EFX org form (kundtyp=brf prefilled, orgLabel "Föreningens namn", Kontaktperson) — reusing the resolver intelligence that already exists, per EFX-04's MainContact org-variant.

## Funnel position
| Surface | Placement |
|---|---|
| /bostadsrattsforening/ | Featured guide tile under the (new) org-trust strip — the page's missing "prove you understand BRF" artifact |
| /laddboxar/ hub | Secondary tile: "Sitter du i en BRF-styrelse? Läs BRF-laddguiden" (the hub's B2B fork) |
| laddbox articles + future BRF cluster | Verktygs-tile B2B variant |
| Meta/outbound (out of scope here) | Natural demand-gen asset for the Meta engine's BRF segment — noted for the ads track |

## Lead-capture linkage
PDF download → n8n `source=brf-laddguide` with föreningens namn = an org-qualified marketing lead (long cycle — route to a nurture lane, NOT the 24-timmar call queue; mixing cycle speeds would break the SLA promise). Förstudie form → standard hero-lead pipeline with kundtyp=brf.

## Effort & priority arithmetic
- Effort: **M–L** — the only candidate needing real new content + fact verification; needs an author lane (Edvin/Magnus per the editorial trio pattern) and owner sign-off on BRF process claims.
- Priority: direct arithmetic is modest — ~4 placement pages × 2 × 2 = **16** — but the strategic case (priority-#2 lane, higher order values, the 546-impression latent demand, first org-level proof artifact) justifies **P2, months 2–3**. Do not let the low arithmetic pull it into month 1: it must not queue ahead of the wrap/foto-bedömning work that fixes live leaks.

## Candour-gate check
PASS with one CRITICAL fact gate: **Grön Teknik-avdraget (50 %) is a privatperson skattereduktion — a BRF as juridisk person is NOT the grön-teknik claimant; the relevant support for föreningar is the Naturvårdsverket laddinfrastruktur-bidrag ("Ladda bilen"-class), with its own rates and conditions.** The site's own BRF FAQ already references Ladda bilen-bidrag, so the distinction exists in-house — but the guide must state it precisely, with current rates owner/expert-verified before publish `[GAP: bidragsrate + villkor + vem söker]`. Never transplant the consumer "50 % direkt på fakturan" framing into BRF copy — that would be exactly the internal-contradiction class (SVC-03) this program keeps finding. All juridik claims get the "kan"-register (legal/safety caution) and expert fact-check (Faktagranskad byline).

## Test hypothesis
**HYPOTES:** Adding the guide tile + org-trust strip to /bostadsrattsforening/ increases org-form submissions (kundtyp=brf) per session vs. the current consumer-skinned page, and PDF downloads predict 30-day förstudie requests (validating the soft gate; if downloads don't convert downstream within a quarter, un-gate the PDF).
