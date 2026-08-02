# Magnet-wrap standard — the per-magnet fix for the 7 orphan pages

**Status: BUILD (retrofit, not new construction). Gated on two week-1 prerequisites (below).**
This file turns the lead-magnets template finding LM-03 (orphan-wrap gap, score 30 — highest structural score in the family) into a per-magnet execution spec, per the owner's own example: *Energikalkylatorn should get AlternativHero on top + Vår process + Main contact form below.*

## Job-to-be-done
The visitor's job after "vad kan jag spara / får jag göra det här själv?" is **"kan jag lita på de här människorna att göra jobbet?"** — currently unanswered on-page (JTBD; MECLABS HealthSpire: added content that answers real decision questions lifts conversion). 5 of 7 magnets end at the tool; none of the 7 carries MainContact — the site's strongest converter is absent from exactly the pages that pre-qualify visitors hardest.

## Week-1 prerequisites (nothing below matters until these are done)
1. **LM-01:** replace the dead placeholder "010-123 45 67" in the batterikalkylator error state (and the identical string on the /solcellsbatterier/ embed, CAT-02/PP-02) with 010-265 79 79.
2. **LM-02:** submit a test lead on all 5 form-bearing magnets and verify arrival in n8n/CRM + thank-you flow. Project history records the energikalkylator webhook as a stub (leads dropped). Until proven, every magnet lead count is untrustworthy — and instrumenting all 5 forms with the standard dataLayer contract (form_view/form_start/form_submit + source_form) is part of this item.

## The standard wrap (family invariant)
`AlternativHero (benefit-H1 + breadcrumbs + 1-line promise) → Calculator/tool (UNCHANGED — approved rendering is canon) → VarProcess (per-magnet copy: "Skicka kalkylen → vi ringer inom 24 h → kostnadsfri rådgivning → fast offert i skrift") → FAQ (magnet-specific, in-DOM) → MainContact (anchored proof) → Prefooter/Footer.`
VarProcess copy must use the corrected canonical step set (the "Vi går vi igenom"-typo class from SVC-09/CAT-10 must not be cloned onto 7 more pages).

## Per-magnet spec

| Magnet | Current state | Wrap actions (delta only) | Notes / divergences |
|---|---|---|---|
| **/energikalkylator/** | Half-wrapped: calc + form, no hero/FAQ/process/close | Full standard wrap + meta description + benefit-H1 ("Vad drar ditt hus — och vad kan du spara per år?" direction, final via ampy-rost). Keep share row + sticky summary bar. | The owner's named example — ship FIRST as the pattern proof. |
| **/laddboxkalkylator/** | Half-wrapped: good H1/meta, no hero/FAQ/process/close | Standard wrap + new laddbox FAQ set (content exists in the vertical); breadcrumbs via AlternativHero. | Commercial priority #2 — second in rollout order, ahead of batteri polish (fixes the CAT-13-class inversion inside the magnet family too). |
| **/batterikalkylator/** | Wrapped-ish: hero + FAQ, ends at FAQ | Add VarProcess + MainContact. **Fix the missing H1** (hero heading renders `<h3>`; copy led-kalkylator's markup, LM-04). | Priority #3 lane — do not spend design time beyond the two adds. |
| **/led-kalkylator/** | Wrapped-ish: the family benchmark (H1/title/meta correct) | Add VarProcess + MainContact only. | Keep its FAQ→Elkollen internal link. |
| **/elcentral-kollen/** | Naked shell + invisible to Google | Standard wrap **plus the server-rendered Swedish summary layer** (LM-05): real H1, what the tool checks, the Säker?/Redo? axes, service links — with correct å/ä/ö (the current crawlable fallback is ASCII-broken). Fix title "Ampy – Elcentral-kollen – Ampy". | Flagship service lane ("byta elcentral pris" is a live paid query) — the SEO layer is as important as the wrap. |
| **/elkollen/** | Naked, no lead form at all | Wrap steps 1–4 + **verdict bridge** (LM-09): "kräver behörig elektriker"-verdicts deep-link to the matching service page with `?arbete=` prefill (the Hero_2 URL-resolver already supports this) BEFORE MainContact — capture at intent peak. | DIY audience: MainContact is the fallback, the prefilled service-page form is the primary bridge. |
| **/ampy-eljour/** | Naked, call-only by design | AlternativHero-variant with H1 + meta ONLY. **No form, no MainContact** — substitute a ring-only close (existing sticky call panel already does this job). | A form here would fight the urgent JTBD (Unbounce: urgent-repair converts on the call). Also resolve LM-08: /ampy-eljour/ vs /eljour/ same-intent duplication — owner call: canonicalise, merge, or noindex as paid-only landing. |

Cross-cutting: fix nav labels in "Guider & verktyg" to match destination H1s and add the missing tools (LED-kalkylatorn, Elkollen are in no navigation surface today — LM-08); consolidate consent microcopy on the laddbox pattern (LM-11).

## Lead-capture linkage
All embedded magnet forms keep their value-then-ask 4-field pattern (Baymard-compliant — do not add fields). MainContact instances added by the wrap post to the same n8n endpoint as everywhere else with a hidden `source_form=magnet-{slug}` so magnet-attributed leads become visible in CRM for the first time.

## Effort & priority arithmetic
- Effort: **S–M per page** (all blocks exist; work = instances + per-magnet copy + FAQ content ×3 + elcentral SSR layer M).
- Priority: 5 pages needing structural wrap × 3 (adds a form-stage block) × 2 (medium-high) = **30**; plus batteri/LED adds 2 × 2 × 2 = 8. → **P1, month 1** (after the two P0 week-1 prerequisites). Rollout order: energikalkylator → laddboxkalkylator → elcentral-kollen → elkollen → batteri/LED adds → ampy-eljour hero/meta.

## Candour-gate check
PASS with conditions: MainContact's "3 000+ genomförda installationer om året" and any "5 av 5" instance must use the owner-confirmed anchored canon (rating + count + source — same gate as TrustStrip; do not clone unanchored claims onto 7 more pages). Methodology boxes ("inte ett erbjudande, inte bindande") stay verbatim — they are the candour register done right. No urgency added anywhere.

## Test hypothesis
**HYPOTES:** On /energikalkylator/, the standard wrap below the unchanged calculator increases (form submits + phone clicks)/session vs. the naked page, without reducing calculator completion. Primary metric: qualified leads per 1 000 sessions. (= lead-magnets template hypothesis 1; this file is its execution spec.)
