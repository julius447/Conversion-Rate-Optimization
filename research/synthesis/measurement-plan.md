# Measurement & experimentation plan — making the CRO program learnable

Synthesis lens: measurement/experimentation. Integrates all 14 template deep-dives + 20 block audits.
Adversarial mandate applied: where template agents proposed A/B tests, this file rules on **fix vs test**
based on statistical power at real traffic (~10–20 organic visitors/day + small paid ≈ 450–900
sessions/month sitewide), and names the trade-offs.

**The governing fact:** GA4 recorded ~32 paid sessions, ~17 deep scrolls, 2 phone clicks and **0 form
starts** — while at least **six distinct form systems** run in production (`.aof` Supabase `hero-lead` on
260 pages, MainContact→n8n on 295, product popups 29890/29891 on 26, the legacy /elinstallation/ form,
the calculator REST forms `ampy-calc/v1/lead`, and elcentral-kollen's client-rendered form). The `.aof`
script emits exactly ONE dataLayer event (`ampy_lead_submit`, at submit); everything else emits nothing
(hero2-form H2-02, MC-07, PU-4). The conversion itself fires on a bare `/thank-you` **pageview** on a
page that is `index,follow` and directly reachable (TY-1). **Until this layer is fixed, no CRO change on
this site is measurable, and current lead counts are untrustworthy in both directions** (magnet webhooks
may drop real leads — LM-02; the thank-you pixel can mint fake ones — TY-1).

---

## 1. Instrumentation spec — P0, ships before any A/B or any redesign

### 1.1 Event dictionary (one dataLayer contract for ALL form systems)

Per the ampy-webb-playbook instrumentation contract: consent-gated, bucketed, `experiment_id` carried on
every event. Field **names** only in payloads, never values (GDPR).

| Event | Trigger | Parameters |
|---|---|---|
| `form_view` | form block enters viewport (enterView) | `source_form` (aof / main_contact / product_popup / calc_energi / calc_laddbox / calc_batteri / calc_led / elcentral_kollen / legacy_elinstallation), `page_template`, `vertical` |
| `form_start` | first `focusin` on any field | + `first_field` |
| `form_field_error` | validation error shown | + `field`, `error_type` |
| `form_field_abandon` | pagehide/unload with form started, not submitted | + `last_field` |
| `form_submit` | successful POST (before redirect) | + `kundtyp`, `tjanst`, `kallsida` (the aof resolver already builds these dims — extend to all systems) |
| `form_submit_error` | fetch/POST failure | + `error_class` |
| `disclosure_open` / `kundtyp_switch` | aof "Fler detaljer" / segment toggle | `source_form` |
| `tel_click` | click on any `tel:` link | `cta_block` (header / hero / main_cta / blue_cta / eb_panel / sticky_bar / expert_card / footer), `page_template`, `vertical` |
| `eb_panel_open` | eljour symptom accordion panel opened | `symptom_id`, `severity` — prerequisite for the eljour sticky-bar test (geo-eljour hypothesis 2) |
| `calc_start` / `calc_result` / `calc_share` | first input change / result rendered / share-row click | `calc_id` |
| `sticky_bar_view` / `sticky_bar_click` / `sticky_bar_dismiss` | when the mobile sticky bar ships | `action` (ring / form) |
| `block_view` | enterView on tracked blocks: main_contact, testimonials, faq, var_process, team, certificates, footer_seo | `block_id`, `block_index` |

Prerequisites folded in:
- **Standardize tel: URIs to E.164** (`tel:+46102657979`) — the product expert card uses a space-formatted
  URI (PP-12); inconsistent hrefs fragment click tracking.
- **`block_view` doubles as a bug detector** for the verified enterView/`opacity:0` failure (live-browser
  observation #2: whole sections invisible after scroll). A page that fires scroll-depth 90% but no
  `block_view` for mid-page blocks = the fadeIn gate failed. This is measurement AND monitoring for a
  P0-class rendering bug on hidden-on-load blocks (MainContact MC-09, Metrics, VarProcess VP-7,
  AlternativHero all carry it).
- **`experiment_id` + `variant` pushed once per session** when a test is live; joined onto every event.

### 1.2 Thank-you / conversion integrity (TY-1 — the P0 of P0s)

1. `/thank-you/`: `noindex,nofollow`; Swedish `<title>` ("Tack – vi hör av oss inom 24 timmar").
2. GA4 key event + Google Ads conversion move from **pageview** to the **`form_submit` event** (or a
   session flag set at submit and read on /thank-you). Direct loads, bots, bookmarks then count nothing.
3. **Parallel-run both definitions for 2–4 weeks** (quasi-experiment from om-oss-kontakt.md TY test 2):
   the delta quantifies current conversion pollution and recalibrates true CPL **before** any bidding
   decision. Trade-off named: during the parallel window Ads optimizes on the old polluted signal —
   acceptable at current micro-spend; do not scale spend until the event-based conversion is primary.
4. Verify the aof redirect preserves the dataLayer push order (`ampy_lead_submit` fires before
   `location.href` — verified present in the decoded script; keep it).

### 1.3 Lead-pipe integrity audit (week 1, manual — before trusting ANY number)

Submit one test lead through **each** of the six form systems and confirm: (a) arrival in n8n/Supabase →
CRM, (b) /thank-you or in-place success shown, (c) events fired. Known risks: energikalkylator webhook
recorded as a stub (leads dropped — LM-02); batterikalkylator + /solcellsbatterier/ + all 10 battery
product pages show placeholder **010-123 45 67** in the error state (LM-01/CAT-02/PP-02) — a hot lead
whose submit fails is told to call a dead number. Fix the string the same day. Until this audit passes,
treat all historical magnet/product lead counts as unreliable.

### 1.4 Call tracking

- `tel_click` (above) is the on-site proxy; the truth layer is **Nimbata call tracking** (already in the
  Marknadsmotor sprint-1 scope): call duration, answered/missed, business hours.
- Qualified-call definition: **>90 s duration AND marked contact-relevant in CRM disposition**. HYPOTES:
  90 s separates real service inquiries from wrong numbers/spam — validate against the first month of CRM
  dispositions and adjust the threshold from data, not assumption.
- Missed-call rate becomes a guardrail: the site work drives calls; if pickup can't absorb them, the "60
  sekunder" promise (unverified, flagged in ≥6 templates) breaks in public.

### 1.5 Clarity tagging taxonomy (CXL session-replay coding)

Low traffic is an advantage here: **every paid session can be watched**. Tag each session so replays
aggregate instead of anecdote:

| Tag | Values |
|---|---|
| `src` | paid-google / paid-meta / organic-brand / organic-nonbrand / direct / referral (from UTM + referrer) |
| `intent` | service / eljour / laddbox / battery / brand-verify / research (landing template + query class) |
| `device` | mobile / desktop |
| `landing` | template id (homepage / service / geo-elektriker / geo-eljour / product / magnet / article / kontakt / om-oss) |
| `deepest_block` | last `block_view` fired |
| `cta` | none / tel / form-cta / kontakt-nav |
| `form_state` | none / start / error / submit |
| `exit` | exit block or exit URL (flag Contact→Om-oss trust loops explicitly — the recorded 47 s pattern) |

Smart-events to configure: rage clicks on the dead /elservice/ grid (CAT-01), dead clicks on the
unlinked "Få en kostnadsfri konsultation!" footer heading (GLOB-11), quick-backs on paid landings.

### 1.6 Ownership & change log

Every ship gets a dated annotation in GA4 + Clarity + a `run-log` row (date, change, pages, expected
metric). Without change annotations, before/after inference — the workhorse method at this traffic level
(§3) — is impossible.

---

## 2. KPI tree

**North star (weekly): Qualified leads** = qualified calls (>90 s, CRM-relevant) + form submits that
reach the CRM and are contactable. Two conversions only; nothing else is a "lead".

```
Qualified leads / week
├─ Phone lane:  sessions → tel_click → call answered → >90 s / CRM-relevant
├─ Form lane:   sessions → form_view → form_start → form_submit → CRM-received → contacted ≤24 h → sales-accepted
└─ Economics:   CPL per channel vs max CPL 1 300–2 000 kr (locked service economics, ~2 660 kr täckningsbidrag,
                50–75 % close of CONTACTED leads → first-call answer rate is a top-3 lever, owned by the
                thank-you page calibration work TY-2)
```

**Guardrails (every test and every "ship as fix" carries them):**
1. **Lead quality** — CRM disposition per `source_form`/`vertical`: contactable %, sales-accepted %,
   Closed Won. A field-diet win on submits that degrades contactability is a loss (MC-03 explicitly
   requires quality tracked to close).
2. **Phone/form mix** — total leads must not drop when one lane is optimized (cannibalization check in
   nearly every template hypothesis).
3. **Bounce / engaged-session rate** on the changed template.
4. **LCP field data** (CrUX + Clarity dead-time) — the ~9–10 s lab flag means any block added above the
   fold must not worsen paint; speed is a conversion precondition, tracked monthly.
5. **Pillar/product entrances** for re-sequencing changes (homepage HP test 1 guardrail: /laddboxar/*
   sessions must not fall >20 %).

**Diagnostic funnel steps (GA4 funnel exploration, per GA4 lead-gen funnel guidance):**
`session_start → engaged session → block_view(form) → form_start → form_submit → CRM-accepted`, and the
phone twin `session_start → tel_click → qualified call`. Segmented by device × template × src. The
form_view→form_start and form_start→form_submit ratios are the two numbers that finally distinguish
"nobody reached the form" from "everyone abandoned at Adress" — indistinguishable today (H2-02).

**Diagnostic sub-metrics per open question:**
- Message match: paid landing bounce + quick-back rate per query-class (the 1 s Vitvaror bounce class).
- Trust-seeking: % of sessions detouring to /om-oss/ or team pages before converting (Clarity `exit` tag).
- Answer rate: first outbound call answered % (CRM/Nimbata) — the thank-you rebuild's primary metric.
- Magnet health: calc_start → calc_result → form_submit per calculator.

---

## 3. The A/B roadmap — power-honest triage of all template hypotheses

### 3.1 Sample-size reality check (the adversarial ruling)

Two-proportion test, α=0.05, power 80 %: n/arm ≈ 16·p̄(1−p̄)/Δ².

| Metric & effect | n per arm | Reality at today's ~450–900 sessions/mo |
|---|---|---|
| Session→lead 1 % → 2 % (+100 % rel) | ~2 350 | **5–10 months for ONE sitewide test** |
| Session→lead 1 % → 1.2 % (+20 % rel) | ~44 000 | **impossible (years)** |
| form_start 5 % → 7.5 % (+50 % rel) | ~1 500 | ~6 weeks **if** paid scales to ≥500 sessions/wk on the tested surface |
| tel_click 4 % → 5 % (+25 % rel) | ~6 900 | ~28 weeks even at 500/wk — micro-metric tests need big effects |

(Baselines are placeholders — **no true baselines exist until §1 has run for 4 weeks**. First
instrumented month = baseline-setting, not testing.)

**Consequence, stated plainly:** at current traffic, classic A/B testing is not available for
bottom-line metrics. The program's learning engine for the next 2–3 months is: (a) fix-and-monitor
(interrupted time-series on the weekly KPI tree with change annotations), (b) watched-session
qualitative evidence (Clarity, every paid session), (c) CRM outcome reconciliation. True A/B unlocks
only on surfaces where **paid spend concentrates volume** — service/geo landing pages, and the eljour
set when that campaign launches — and only on micro-conversions (form_start, tel_click) with large
expected effects. Any agent's "run this A/B now" recommendation on organic-only surfaces is overruled.

### 3.2 Tier 0 — fix immediately, NEVER test (broken baselines, candour-gate mandates, bugs)

Testing against a broken or dishonest control is theatre. These ship week 1–2 regardless of measurement:

1. Thank-you noindex + event-based conversion (TY-1) · 2. Lead-pipe audit + placeholder phone
010-123 45 67 (LM-01/PP-02/CAT-02) · 3. /elservice/ dead grid — 22 cards, zero `<a href>` (CAT-01) ·
4. Literal `[ort]` on /eljour/ (PIL-01) · 5. "Kostnadsfri radgivning" missing-å on ~290 pages
(GLOB-01/PIL-02) · 6. VarProcess duplicated/wrong step text (SVC-09/EFX-06/CAT-10) · 7. ROT-block on
non-ROT-eligible pages contradicting the page's own FAQ (SVC-03, GEO-ELJ-02) · 8. Fake-sale
strike-through "Ordinarie pris = exactly 2× net" reframed to "Pris före/efter Grön Teknik" (PP-03 —
candour gate, not a test) · 9. Rating anchoring "5,0 av 5 · N recensioner på Google" everywhere or
removal (candour gate requires it regardless of test outcome — homepage hypothesis 3, PIL test 3 and
testimonials test 1 are hereby **reclassified from test to mandate**; owner must supply current N) ·
10. Reconcile "1000+ / 3 000+ / 60 sekunder / 24 timmar" claim contradictions to one owner-confirmed
canon (OM-1, GEO-04, GEO-ELJ-03) · 11. Remove `hidden-on-load` from form/trust blocks (MC-09 — a form
must never depend on an animation to exist; also mitigates the verified opacity:0 bug).

### 3.3 Tier 1 — ship as best practice, measure before/after (evidence priors strong; power absent)

Deduped from 30+ template hypotheses into 9 workstreams. Each gets: change annotation, 4-week
pre/post on the KPI tree, guardrails from §2. Trade-off named where agents disagreed.

| # | Workstream (deduped sources) | Surface | Monitoring metric |
|---|---|---|---|
| F1 | **CTA retarget: every "Kostnadsfri rådgivning" → on-page form anchor** instead of /kontakt/ (HP-03, GEO-01 ×2 templates, EFX-03, GLOB test 2, cta-bands, OM-7, PP-09) — the single most-repeated recommendation in the corpus | ~300 pages | form_start/session; guardrail tel_click |
| F2 | **Server-render the aof form shell + minimal fields** (SVC-01, GEO-02, EFX-05, H2-07). Agents proposed this as a test; overruled — the control arm is "form may not exist at paint", not a legitimate baseline | 260 pages | form_view fire-rate at first paint; form_start from paid |
| F3 | **Field diet v1: Adress→optional on aof + MainContact, single Namn field** (H2-04, MC-03, KO-3, SVC-08). Ship the Baymard-backed floor now; the finer 3-vs-5-field question is the Tier-2 test T3 | 295+260 pages | form_start→submit ratio; guardrail CRM contactability |
| F4 | **/kontakt/ phone row + H1 + label ladder** (KO-1/KO-2, GLOB-02/03/14) — destination of ~900 CTA instances | 1 page, sitewide reach | tel_click on /kontakt/; combined conversions/kontakt-session |
| F5 | **Homepage re-sequence** (HP-01/02/13: ServiceRouter up, ProductGrid → 2-card teaser) | 1 page, ~89 % of organic clicks | weekly qualified leads from homepage sessions; guardrail pillar entrances −20 % max |
| F6 | **Price message-match blocks** ("Vad kostar det?" under hero from existing FAQ copy — SVC-02, GEO-03; laddbox grid/FAQ price reconciliation GEO-09/PP-01) | 22 service + 112 geo | paid bounce per query-class; quick-backs |
| F7 | **Magnet wrap rollout** (LM-03: AlternativHero+VarProcess+FAQ+MainContact), energikalkylator first (owner's own example) | 5–7 pages | leads per 1 000 magnet sessions; calc completion unchanged |
| F8 | **Article conversion layer** (ART-01/02/03: fix the 2 broken footer-linked posts; inline photo-bedömning CTA + "Nästa steg" card; review ask demoted) | 11 posts | article→form_start/tel_click (today ~0) |
| F9 | **Om-oss/team trust loop** (OM-2, TEAM-01/02: team+testimonials+certificates on /om-oss/, profile links, profile CTA card) | 92-page surface | trust-session conversion rate (Clarity `intent=brand-verify` segment) |

Trade-off acknowledged: shipping F1–F9 untested means we can never attribute lift to a single change.
Accepted deliberately — the alternative (holding fixes hostage to unreachable significance) costs real
leads for a certainty low volume can't deliver anyway. The KPI tree + annotations give directional
attribution; the Tier-2 tests give causal proof later, on the few questions where variants are genuinely
contested.

### 3.4 Tier 2 — the true A/B queue (armed when the tested surface sustains ≥500 sessions/week, i.e. paid scale-up)

Ranked by (traffic reachability × expected effect × implementation cost). All require §1 live + 4 weeks
of baseline. Bucketing: user-level via `experiment_id` (webb-playbook contract); for template families,
page-level bucketing by ort (28/28 split of a geo set) is acceptable second-best — trade-off: ort
heterogeneity adds noise; mitigate by matched pairs on impressions.

| Rank | Test (deduped sources) | Arms | Primary metric | Why it earns a test rather than a fix |
|---|---|---|---|---|
| T1 | **Hero ask architecture on paid service/geo landers** (SVC test 3, H2-01, GEO-07): A = SSR form + phone secondary; B = phone-primary + "Till formuläret" | 2 | form_start + tel_click composite; guardrail total qualified leads | Genuinely contested: form-first vs call-first evidence points both ways (2/2 recorded conversions were calls; but boards/evening users write) |
| T2 | **Mobile sticky bar** "Ring · Få offert" ≥40 % scroll (GEO-10, ART test 3, GLOB test 1-B) | vs none | tel_click/mobile session; guardrails dismiss <40 %, bounce neutral | Real downside risk (annoyance) justifies a controlled test; run AFTER T1 to avoid interaction |
| T3 | **Field set: minimal (Namn/Telefon/Postnr) vs current-minus-address** (MC-03, hero2 H2-04, HP secondary) | 2 | submit rate; guardrail CRM contactability + sales-accepted | Quality trade-off is empirically undecidable from priors; n8n-level split works across the form estate |
| T4 | **Eljour phone-dominant hero + sticky call panel** (GEO-ELJ tests 1–2, PIL test 2) — armed when the eljour campaign launches (Unbounce: best intent class on the site) | 2 | tel_click/session ≥+30 % target; eb_panel_open-conditioned | 56-page set + paid volume = the first surface likely to reach power; effects expected large |
| T5 | **laddbox-i ProductGrid rewiring** — dual CTA "Få pris installerad i {ort}" prefilling the on-page form vs "Läs mer"-only (GEO test 2, PP hypothesis 1) | 2 | geo-page form submits; watch product-popup cannibalization | Revenue-relevant and reversible; needs laddbox paid volume |
| T6 | **Light vs navy aof form card** (H2-06) + first-FAQ-open (faq.md), review-pinning (testimonials), nearest-N ort list (map-block) | 2 each | form_start / micro-engagement | Micro-test backlog: cheap, only when T1–T5 done; individually small effects → need the most volume, hence last |

**Explicitly deferred/rejected test proposals:** anchored-rating A/B (mandated, §3.2); SSR-vs-JS form
(broken control); homepage sequence A/B (1 page × organic volume → never powers; before/after only);
"benefit H1 on magnets" (ship with F7, monitor); enterView-removal (bug fix, not variant).

### 3.5 Decision rules (pre-registered, per test)

Fixed-horizon: MDE, n/arm, and horizon date written into the run-log BEFORE launch. No peeking-to-stop;
one interim look at 50 % n allowed for **harm only** (guardrail breach or bug → stop). At horizon:
significant → ship winner; not significant → declare inconclusive, keep the cheaper/candour-cleaner
variant, log the learning. Never extend a running test "until it wins".

---

## 4. The weekly learning ritual

**Monday, 45 minutes, standing agenda (owner + whoever runs ads):**

1. **Scorecard (10 min):** qualified leads by lane (calls >90 s / CRM-accepted forms) × channel ×
   template; CPL vs the 1 300–2 000 kr cap; first-callback answer rate; missed-call rate.
2. **Funnel diagnostics (10 min):** form_view→start→submit per form system; tel_click per template;
   paid landing bounce per query-class. **Zero-event tripwire:** any instrumented form showing 0
   form_view over a week with >50 sessions = instrumentation or rendering breakage (the opacity:0
   class of bug) — investigate before interpreting anything else.
3. **Watch the tape (15 min):** every new paid-session Clarity recording (volume permits 100 % review),
   coded with the §1.5 taxonomy; tally the codes (message-match miss / trust-detour / form-friction /
   speed-blank / dead-click). Three sessions with the same code = a backlog item with evidence attached.
4. **Experiments (5 min):** for each live test — n accrued vs plan, guardrails green, horizon date. Call
   tests ONLY per §3.5 rules. For Tier-1 ships in their 4-week windows: KPI vs pre-period, annotated.
5. **Ship log (5 min):** what ships this week; write the GA4/Clarity annotations NOW, not after.

**Monthly supplements:** CRM disposition reconciliation (lead quality per source_form/vertical —
closes the loop the weekly can't); CWV field data vs the 9–10 s lab flag; GSC brand/non-brand split
(is the trust-verifier share changing?); review-of-the-canon (are "3 000+", "N recensioner", "60
sekunder" still owner-confirmed current — candour claims decay).

**Kill criteria for the ritual itself:** if after 8 weeks the funnel events still show <5 form_start/wk
sitewide, the constraint is traffic, not conversion — the learning agenda shifts to paid scale-up and
message-match economics, and Tier-2 testing stays parked. Stated now so nobody optimizes an empty funnel.

---

## Open [GAP]s this plan needs from the owner
1. Current Google rating + review count (unblocks the sitewide anchoring mandate).
2. One canonical installations figure + unit; "60 sekunder" and "24 timmar" SLA truth.
3. Nimbata (or equivalent) call-tracking activation + CRM disposition fields (contactable /
   sales-accepted / won) per lead source.
4. Confirmation that n8n/Supabase/CRM can carry `source_form`, `vertical`, `experiment_id` through to
   disposition (lead-quality guardrails depend on it).
5. Paid scale-up decision + budget: Tier-2 testing is gated on ≥500 sessions/wk reaching the tested
   surface.
