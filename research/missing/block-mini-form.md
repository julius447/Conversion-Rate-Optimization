# MiniForm — server-rendered 3-fälts lead-form (the conversion-infrastructure backbone)

**Status: BUILD — a reusable component, not a page block; every other form recommendation in this program lands on it.**

## Job-to-be-done
Give any block, anywhere, a minimum-friction lead ask that (a) exists in server HTML (no JS dependency), (b) matches the established Ampy min-lead doctrine (namn + telefon + postnr + GDPR), and (c) emits the full instrumentation contract. Today the site runs **three incompatible form systems** (Hero_2 `.aof` → Supabase, MainContact → n8n, product popup → n8n; plus the /elinstallation/ legacy form) with different field sets, different submit labels, zero `form_start` events, and — on the highest-traffic templates — **no server-rendered fields at all** (GEO-02: 1 `<form>` tag total in an 820 kB geo page; "Boka rådgivning" appears 0 times in source; GA4: 0 form starts across ~32 paid sessions).

Evidence chain: GEO-02 (1 008), SVC-01 (198), H2-02/H2-07 (measurement void + JS-only paint on 260 pages), PP-04 (234 — primary product CTA hides conversion behind a 5-required-field modal), PIL-04 (pillars' first form at 55–70 % depth), MC-08 (two lead schemas on the same page), EFX-05.

## Anatomy (in words)
- **Headline (per placement, ACF):** pattern "Få ditt pris — vi ringer dig inom 24 timmar" (the promise IS the headline; 24h only if owner-confirmed, else the softer verified promise).
- **Fields:** Namn · Telefonnummer (E.164 gate) · Postnummer (5-digit gate). Nothing else visible. Optional "Fler detaljer (valfritt)" disclosure inherited from the .aof pattern (beskrivning + bilduppladdning — benefit-labelled per H2-09: "Beskriv jobbet eller ladda upp en bild — då kan vi ge ett snabbare besked").
- **Hidden context payload:** kallsida, vertical/tjänst (from the existing URL resolver), source_form id, experiment_id.
- **GDPR consent line** (one canonical pattern — the laddbox-kalkylator checkbox version, LM-11).
- **Submit:** ONE sitewide label (coordinate with GLOB-03 label unification), honeypot, aria-live status, error state with the REAL phone number (the 010-123 45 67 placeholder class of bug, LM-01/PP-02, must be structurally impossible: number comes from one config constant).
- **Events:** form_view, form_start (first focusin), field_error, form_field_abandon, form_submit, form_submit_error → dataLayer, consent-gated (ampy-webb-playbook contract).
- Rendered server-side by Bricks/PHP; JS only enhances (prefill, validation UX).

## Templates + position (initial placements)
| Placement | Pages | Replaces |
|---|---|---|
| ProductHero (laddbox + battery) | 26 | the 5-required-field popup as primary ask (popup demoted to secondary) — PP-04 |
| Pillar Hero-1 (elektriker, elinstallation, laddbox) | 3–4 | nothing (pillars have NO hero form today; geo children do — inverted hierarchy, PIL-04) |
| Article "Nästa steg" card (see block-nasta-steg-artikel) | 11 | the unstyled text link at word ~3 700 |
| Eljour two-lane contact, "kan vänta"-lane (see block-two-lane-contact) | 57 | the 7-field MainContact misfit |
| Longer term: the SSR fallback inside Hero_2's `.aof` root | 260 | empty div at first paint (H2-07 pairs; the full resolver hydrates on top) |

## Why it beats status quo
Baymard: visible/required field count drives perceived difficulty more than steps — 3 fields vs 5–8. The phone callback needs exactly these three fields (established min-lead doctrine; address is post-submit enrichment). SSR kills the blank-hero-column failure on a ~9–10 s lab-LCP site and makes the funnel measurable at all — the precondition for every A/B in this program. One schema ends the two-lead-records problem (MC-08) and gives n8n/CRM a single contract.

**Adversarial note — form proliferation risk:** adding MiniForm placements while Hero_2 + MainContact remain yields 3 forms/page in places. Resolution: MiniForm is a *replacement/fallback* instrument, never an addition next to an existing form on the same viewport; page-level rule stays "one primary ask per funnel moment" (SVC-04). Second tension: which backend? Supabase (hero-lead) vs n8n split must be resolved — recommendation: one endpoint or a normalizing relay, decided with the owner before rollout (SVC-10).

## Candour-gate check
PASS. The promise line must state the true SLA only ("inom 24 timmar" pending owner confirm — three different promises currently collide, HP-08/GEO-ELJ-03). No urgency devices. Consent explicit.

## Effort & priority
- **Effort: M** (one component + endpoint decision + instrumentation; per-placement wiring S each).
- **Priority arithmetic (committed placements):** products 26 × 3 × 3 = 234; pillars 4 × 3 × 3 = 36; articles 11 × 2 × 3 = 66; eljour lane 57 × 3 × 2 = 342 → **combined ≈ 678**, PLUS enabler value: it is the prerequisite for the Hero_2 SSR fix (260 × 3 × 3 = 2 340 block score) and for every form A/B. → **P1, month 1 — instrumentation part is week-1 P0.**

## Dependencies
1. Backend decision (Supabase vs n8n vs relay) — owner/dev call.
2. dataLayer/consent-mode contract live (Sprint-1 tracking work).
3. Label unification decision (GLOB-03) and SLA confirmation [GAP].
4. Thank-you pixel sanctity fix (TY-03) so submits are counted truthfully.
