# Foto-bedömningen — "Skicka bilder, få en bedömning" micro-offer

**Status: BUILD — the highest-priority NEW magnet in the program, and the only one in the service lane (commercial priority #1).**
This is the buried gold the article research surfaced (ART-06): the offer already exists as one plain-text sentence at word ~3 700 of byta-elcentral-2026 — *"Skicka ett par skarpa bilder på din central till oss, så återkommer vi med en kostnadsfri bedömning och ett prisförslag inom två arbetsdagar."* — linking to generic /kontakt/, whose hero says nothing about photo assessment (message-match break). The capability also already exists: the Hero_2 `.aof` form's "Fler detaljer" disclosure supports bilder upload via multipart to n8n. This build is packaging, not invention.

## Job-to-be-done
**"Get price certainty for MY specific case without letting a stranger into my house or committing to anything."** This attacks the #1 documented Swedish-homeowner anxiety head-on (Byggahus/Konsumentverket anchor: final-price surprises, fixed vs estimated offert) with near-zero perceived friction — Baymard: perceived difficulty tracks visible fields, and "ta en bild" is not a field, it's something the visitor already knows how to do. It also pre-qualifies harder than any form: a photo of a proppskåp IS the ärende description, and it filters tire-kickers at ~2 660 kr täckningsbidrag economics.

## Why it beats every other new-magnet candidate
All 7 existing magnets skew energi/laddbox/battery/DIY — the service lane (priority #1, the lane Google Ads buys into, the lane with "byta elcentral pris"/"elfel i huset" queries and 0 confirmed form leads) has NO magnet. A calculator can't price a 60-tals proppskåp; a photo can. Unbounce: repair/urgent-adjacent offers convert best in home services. And it is candour-native: the offer's honesty ("kostnadsfri bedömning", human answer, no obligation) is the brand.

## Anatomy
- **Micro-form (the whole magnet):** Namn → Telefon → Postnummer → bilder-upload (1–5 bilder, mobile camera-capture enabled) → valfri en-rads beskrivning → GDPR → submit. Nothing else. Multipart → n8n (existing pipeline), redirect /thank-you (conversion fires).
- **Framing copy direction (final via ampy-rost):** "Skicka ett par bilder på din elcentral. En behörig elektriker tittar och återkommer med en ärlig bedömning och ett prisförslag inom två arbetsdagar. Kostnadsfritt — och du bestämmer själv om du vill gå vidare."
- **Expectation row:** vad händer sen (3 steg: bilder in → elektriker bedömer → vi ringer/mailar prisförslag) — the VarProcess pattern in miniature.
- **Disclaimer (candour):** en bedömning på bilder är ett prisförslag, inte en bindande offert — den fasta offerten kommer efter bekräftelse. State it; do not bury it.

## Funnel position (template + where)
| Surface | Placement | Format |
|---|---|---|
| **Articles, elcentral cluster (5–6 posts)** | Inline CTA block A slot (~25–35 % depth) + "Nästa steg" end card — this is the elcentral-cluster variant of the Verktygs-tile (see magnet-entry-tiles.md, one component) | Tile → anchor to on-page micro-form, or inline micro-form directly |
| **Service pages, elcentral cluster** (/elservice/elcentral/, elbesiktning, jordfelsbrytare, ~6 pages) | The Pris & offert block's micro-CTA gets a second honest route: "Osäker på just din central? Skicka bilder — bedömning inom två arbetsdagar" | Anchor into the hero form with the bilder disclosure pre-opened |
| **Own landing /foto-bedomning/** (S-size page: AlternativHero + micro-form + VarProcess-mini + FAQ + anchored trust) | Message-match target so article/ad links stop dumping into generic /kontakt/ | Standalone page |
| **Elcentral-kollen verdict layer** | "Osäker?"-verdicts route here (the diagnostic's natural next step) | Verdict CTA |

NOT on: eljour surfaces (urgent JTBD = call, a 2-arbetsdagar promise is anti-matched), laddbox/battery product pages (price is already listed; the calculator lane owns those).

## Lead-capture linkage
Hidden `source_form=foto-bedomning` + `src` page param; photos land in n8n as attachments routed to the assessing electrician; SLA timer starts at submission. Requires an owner-side operational commitment (below) — the form is trivial, the promise is the product.

## Effort & priority arithmetic
- Effort: **S–M** (form variant of existing `.aof` capability + one small landing page; the real cost is the ops routine).
- Priority: articles 6 × 2 × 3 = 36; service elcentral cluster 6 × 3 × 2 = 36; landing 1 × 3 × 2 = 6; elcentral-kollen bridge 1 × 2 × 2 = 4 → **≈82, P1, month 1** — and strategically over-weighted because it is the ONLY service-lane magnet and directly serves the paid queries currently converting at 0.

## Candour-gate check
PASS with two hard gates:
1. **"Inom två arbetsdagar" is an operational promise — owner must confirm the SLA is real and staffed [GAP].** If it cannot be guaranteed, soften to "inom några arbetsdagar" BEFORE launch; a broken response promise to a photo-sender is worse than no promise (the "will they answer later" anxiety from the Byggahus research).
2. Bedömning ≠ offert disclosure ships in v1 (above). No urgency, no "just idag", no invented queue-length.
Also: GDPR — photos of a home interior are personal data; retention/deletion routine needs one line in integritetspolicyn [owner/legal item].

## Test hypothesis
**HYPOTES:** On elcentral-cluster articles, the foto-bedömning inline block produces a higher lead rate (submits + calls) than a generic "Kostnadsfri rådgivning" inline CTA in the same slot, because the offer is case-specific and lower-commitment. Guardrail: assessment SLA compliance ≥95 % (measured in n8n) — if ops can't hold the promise, kill the promise, not the leads.
