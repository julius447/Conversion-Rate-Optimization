# Offert-checklistan — "10 frågor att ställa din elektriker" (trust play)

**Status: BUILD-LIGHT — ungated on-page block + print view. Explicitly NOT an email-gated PDF.**

## Job-to-be-done
**"Help me not get cheated when I compare electricians."** The Konsumentverket written-quote norm and the Byggahus anxiety list (fast vs löpande pris, dolda fel, ansvarsförsäkring, Elsäkerhetsverket-registrering, materialpåslag, "svarar de sen?") ARE the checklist — the visitor's job is due diligence, and Ampy handing them the due-diligence instrument is a costly signal (Cialdini authority + commitment): *we win on these questions, so ask them to everyone, including us.*

## Adversarial format decision — why NOT a gated PDF
The candidate was framed as a PDF lead magnet. Killed in that form, kept in this one:
1. **Gating inverts the psychology.** A trust artifact behind an email wall reads as a sales trap to exactly the skeptical 50-year-old it targets; the costly-signal value comes from giving it away. The magnet family doctrine is value-then-ask — an email gate would be the family's first wall.
2. **Email is the wrong currency.** Ampy's funnel converts on calls and forms; a cold email list has no wired nurture sequence today (CRM sequences are mid-rebuild). Harvesting emails we can't work is fake progress.
3. **Content already exists** — the 12-punkts offertchecklista inside byta-elcentral-2026 (one item even ships cut off mid-sentence: "visa hur stort avdraget." — fix during extraction, ART-08). This is repackaging, ~zero research cost.

## Anatomy
On-page block (article-width, light card): H3 "10 frågor att ställa innan du skriver på — oavsett vilken elektriker du väljer" → numbered list distilled from the existing 12-punkts checklist + Konsumentverket/Elsäkerhetsverket anchors (fast pris i skrift? registrerad hos Elsäkerhetsverket — kontrollera själv-länk? ansvarsförsäkring? hur hanteras dolda fel? ROT förräknat på offerten? …) → footer row: "Skriv ut listan" (print stylesheet) + valfritt "Få listan mailad" med ETT e-postfält (optional, never required) → one quiet close: "Ställ frågorna till oss först — Ring 010-265 79 79".
The self-check link ("kontrollera oss själv hos Elsäkerhetsverket", the pre-queried registry URL) makes this block a natural TrustStrip sibling — reuse that component's verified link, don't duplicate.

## Funnel position
| Surface | Placement |
|---|---|
| Articles: byta-elcentral-2026 + elcentral cluster + future series | Replaces the raw in-body checklist with the styled block (content stays in DOM — SEO preserved) |
| /elservice/elcentral/ and offert-adjacent service pages | Mid-page, near FAQ zone (below the ask, for the comparison-shopper who scrolled past the form) |
| /om-oss/ + /kontakt/ | Optional: the trust-verification audience (GSC shows /om-oss/ punches above its weight as the brand-verification step) |

## Lead-capture linkage
Deliberately weak, and that's correct: the block's job is trust, not capture. The optional email send posts to n8n tagged `source=checklista` (nurture-ready when CRM sequences land); the primary conversions remain the adjacent call/form. Do not measure this block on leads — measure it on assisted conversion (sessions touching the block that later convert).

## Effort & priority arithmetic
- Effort: **S** (content extraction + one block + print CSS).
- Priority: ~10 pages × 2 (mid/low-funnel) × 1–2 (low-med direct effect, higher assisted) = **20–40 → P2, month 2**. Ranked below foto-bedömning and entry-tiles because it converts indirectly.

## Candour-gate check
PASS by design — the block only works if every question is one Ampy genuinely answers well (fast pris i skrift, registrering, försäkring). Gate: before ship, verify each checklist question against Ampy's actual practice with the owner; a question Ampy itself would fail may NOT be quietly dropped — either fix the practice or keep the question (dropping it is exactly the laundering the candour gate exists to catch). Elsäkerhetsverket link must resolve to Ampy's live record (TrustStrip dependency 2).

## Test hypothesis
**HYPOTES:** Elcentral-cluster sessions exposed to the checklist block convert (call + form, same session or 7-day return) at a higher rate than unexposed sessions, via the reciprocity/authority path — with print/email interactions as the leading indicator.
