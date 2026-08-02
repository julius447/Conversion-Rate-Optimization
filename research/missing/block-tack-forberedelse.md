# Efter-submit-paketet (thank-you expectation + preparation blocks)

**Status: BUILD — my addition (not on the candidate list; surfaced independently by two audit files). One page, but 100 % of form conversions pass through it, and it is the cheapest lever on the metric that decides revenue: does the callback get ANSWERED?**

## Job-to-be-done
Convert the post-submit moment from a 32-word dead end into the answer-rate machine. Economics: close rate is 50–75 % **of contacted leads** — the binding constraint after submit is whether the lead picks up an unknown 010-number. Today /thank-you/ says "inom kort" (downgrading the "inom 24 timmar" promise the form just made — a message-match break at the exact moment reassurance is cheapest, TY-2), shows zero images, zero tel: links, no number to save, and offers two generic links (TY-01/TY-02). Also P0-adjacent: the page is indexable with the GA4/Ads conversion firing on pageview — phantom-conversion risk (TY-03/TY-1) that corrupts the entire program's dependent variable.

## Anatomy (in words) — four stacked elements under the kept confirmation card
- **Element 1 — kalibrerad förväntan (modifies the existing card):** "Vi ringer dig **inom 24 timmar** (vardagar 07–16 [GAP: verkliga tider]). Samtalet kommer från **010-265 79 79** — spara gärna numret så du vet att det är vi." + tap-to-save/tel affordance on mobile (the number lands in recents/contacts). Optionally dynamic: submitted Friday evening → "senast måndag förmiddag".
- **Element 2 — "Så förbereder du samtalet":** 3-item checklist, per-ärende where form_type exists ("Ta en bild på din elcentral" / "Mät avståndet till p-platsen" / "Lista vad som krånglar") — primes a better first call, signals professionalism, feeds the fixed-offert wish.
- **Element 3 — "Du kommer att prata med":** 2–3 real team portraits + names/titles (assets exist on the 6 orphaned profile pages) — unknown number becomes known person.
- **Element 4 — "Medan du väntar":** ROT 30 %/Grön Teknik 2026 links + the relevant kalkylator, service > laddbox > battery ordering; PLUS this is the correct home for the **Google-review ask** relocated from the article template (ART-03) — shown to people who can actually be customers.
- Anchored review snippet ("5,0 av 5 · N omdömen på Google", linked) replaces the bare "5 av 5" (TY-4). Swedish title ("Tack — vi hör av oss inom 24 timmar") replaces `<title>Thank you</title>`.
- **Technical rider (P0, week 1, before any content):** noindex; conversion fired on submit-event/one-time token, not bare pageview; form_start emission upstream. Owner-gated regression-test against the live GTM container (approved-rendering + pixel-sanctity rule).

## Templates + position
/thank-you/ (1 page — terminus of every form on 295+ pages; product popups and hero forms all redirect here). Elements stack below the confirmation; nothing competes with or precedes the confirmation itself.

## Why it beats status quo
Cialdini consistency/commitment: post-commitment is peak receptivity; NN/g confirmation-page doctrine: state what happens next, when, by whom; peak-end rule: this page is the "end" of the site experience that the lead remembers when the phone rings. Every element is additive — the conversion already happened, so there is no attention-ratio cost. The review-ask relocation simultaneously fixes the article template's ask inversion without losing review volume.

**Adversarial note — why rank a 1-page block above multi-hundred-page blocks?** Because page-count arithmetic understates funnel position: every single form lead the entire program generates crosses this page, and the measured business bottleneck (0→N leads, then 50–75 % close *of contacted*) is downstream of answer rate, not of one more mid-page block. The doctrine's own precedent: TY-03 was "treated as P0 by sanctity override". Same override applies. Trade-off named: none of this is A/B-able on-page at current volumes — measure in CRM (first-attempt answer rate), per the om-oss-kontakt file's hypothesis 1.

## Candour-gate check
PASS with owner inputs: the 24h/vardagar window must be the real SLA [GAP]; the named callers must be the people who actually call [GAP: who does first-contact — rådgivare vs elektriker]; rating anchored with owner-confirmed N; no cross-sell pressure (Element 4 is educational, service-first).

## Effort & priority
- **Effort: S** (one page; assets exist — team photos, article links, calculators; the technical rider is GTM/robots config).
- **Priority arithmetic:** 1 page × 3 (conversion endpoint) × 3 (high — answer-rate lever + measurement sanctity) = **9 nominal → P0/P1 by sanctity-and-lead-value override** (mirrors the TY-03 precedent). Technical rider week 1; content elements month 1.

## Dependencies
1. Owner: real callback SLA + hours, first-contact roles, review count N [GAP].
2. GTM conversion re-wiring sign-off (pixel sanctity — owner-gated, regression-tested).
3. form_type passthrough from the forms (exists in the .aof payload) for per-ärende checklists.
4. Coordinates with: article review-ask demotion (block-nasta-steg-artikel.md), MainContact promise unification (MC-06).
