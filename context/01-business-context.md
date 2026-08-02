# Ampy — Business Context for CRO Analysis

## Company
- **Ampy Nordic AB** — modern Swedish elfirma (electrical services company). Site: https://ampy.se
- National footprint in copy ("hela Sverige" allowed per owner directive 2026-07-18); operational lead-routing concentrated on 27 Stockholm kommuner.
- Serves **privatpersoner, företag, BRF:er** with everything electrical.
- Target audience: **homeowners/bostadsrättsägare, 35–65 years old, upper middle class, men and women**. NOT tech-savvy startup people. The current design was made by a 24-year-old founder/designer — there is a known taste mismatch risk vs. the audience.

## Conversion paths (ONLY TWO)
1. **Phone call** — Ring 010-265 79 79 (tel:+46102657979)
2. **Form fill** — leads to /thank-you (GA4/Ads conversion fires on that pageview)

There is no e-commerce. No booking calendar. Every page's job: produce a call or a form submission of a *qualified* lead.

## Commercial priority
service > laddbox > battery (owner-confirmed). Batteries are OFF Google Ads. Google = capture service intent; Meta = demand-gen.

## Economics (locked)
- Service job: ~3 500 kr net/job, ~2 660 kr täckningsbidrag, 50–75% close rate → max CPL ~1 300–2 000 kr.
- 2026 rates canon (owner-confirmed, do NOT re-check): grön teknik solar 15% / battery 50% / laddbox 50% (cap 50k); ROT 30%; 60-öre abolished.

## Current traffic reality (from paid specialist investigation, July 2026)
- Google Ads: 33 clicks / 436 impr / ~1 167 SEK spend / CTR 7.57% / **0 confirmed form leads**.
- GA4: ~32 paid sessions arrived fine (tracking to arrival works). ~20 engaged, ~17 deep-scrolled, 2 phone clicks, **0 form starts recorded** (custom form may not emit form_start).
- Clarity (3 identifiable paid recordings): 1s bounce on Vitvaror; 23s no-click on Belysning; 47s visitor who went Contact → **About Us** (trust-seeking behavior hypothesis).
- Diagnosis: the leak is AFTER arrival — combination of message match, page sequencing, trust proof placement, form friction, speed risk (~9–10s lab LCP vs ~2s CrUX-ish Clarity), and incomplete conversion signals.
- Search terms mostly relevant: "installera taklampa", "installera diskmaskin", "byta elcentral pris", "byta proppskåp", "elfel i huset".

## Key research anchors the specialist flagged (use as evidence base)
- MECLABS conversion heuristic: C = 4m + 3v + 2(i−f) − 2a (motivation, value clarity, incentive, friction, anxiety).
- MECLABS HealthSpire: LONGER page +638% leads when extra content answers real questions — length is not the variable, sequencing is.
- Baymard: number of fields visible/required drives perceived difficulty more than steps.
- Swedish homeowner concerns (Byggahus/Reddit): final price surprises, fixed vs estimated offert, material markups, damage responsibility, "will they answer later". Elsäkerhetsverket registration check + Konsumentverket written-quote advice = the proof a serious Swedish customer looks for.
- Unbounce professional services benchmark: repair/urgent pages convert far better than planned-improvement pages (Eljour campaign is the strongest future candidate).
- Google: message match ad → H1 → first screen is mandatory.

## Brand & voice guardrails (candour gate — NON-NEGOTIABLE)
- Voice: "tradesperson who tells you the truth" — Swedish, du-tilltal, candour register (ampy-rost). "!" allowed metered; strong superlatives allowed unless demonstrably false.
- BANNED: fake urgency/scarcity/countdowns, invented social proof, "1000+ kunder" or "5.0 på Google" as asserted fact unless owner-confirmed current.
- Tokens: teal #00a991 / midnight #090b32 / Outfit font / ap* scale. Real Bricks tokens win over any generic aesthetic.
- Warmth grounded in truth is on-brand; fear is one tool, not the house style. Awareness blocks ("Visste du att") should be light and inviting.

## Existing lead magnets (standalone pages today — a known problem: they are "orphans" with no hero, no process, no contact close)
- Energikalkylatorn (/energikalkylator/) — v36 live
- Laddboxkalkylatorn (/laddboxkalkylator)
- Batterikalkylatorn (/batterikalkylator)
- Elcentral-kollen (/elcentral-kollen/)
- Elkollen, LED-kalkylatorn (various states)
Owner's own example fix: Energikalkylatorn should get Alternativ Hero on top + Vår process + Main contact form below.

## What the owner asked for (the deliverable)
A 3–6 month CRO master strategy, delivered as research files + a designed HTML report:
1. **Deep analysis of what exists today** — every template, every block, desktop + mobile, from the customer's perspective.
2. **Ultimate page structures (wireframes)** — per template: homepage, service pages, product pages, programmatic geo pages (elektriker-i / eljour-i / elinstallation-i / laddbox-i), elektriker-för-X, om oss, kontakt, articles, team, lead magnets, thank-you.
3. **Block-by-block improvement audit** — what's wrong, how to fix, priority ranked by (pages affected × conversion impact).
4. **Missing blocks & lead magnets** — what to build, where it goes, priority.
Everything grounded in named best practices (MECLABS, Baymard, NN/g, Unbounce, CXL, message match, Jobs-to-be-Done) — no invented statistics, no fake certainty. Where a claim is a hypothesis, label it as a test hypothesis.

## House rule for big interventions
For large design/funnel changes, present the primary recommendation AND note divergent alternatives (owner QA rule: 3 divergent versions for big interventions). In this strategy phase: primary wireframe + explicitly noted alternative variants for the highest-stakes templates (homepage, service page hero).
