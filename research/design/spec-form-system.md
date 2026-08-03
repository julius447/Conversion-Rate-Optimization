# Formulärsystemet — ONE visual form language (mini-form · MainContact-restack · thank-you)

Scope: the three surfaces where an Ampy visitor meets a form, specced as **one** system so a Bricks
builder can build all three from this file alone. Depends on and completes two round-2 audits:
`research/design/hero2-design.md` (Hero_2 `.aof`) and `research/design/maincontact-design.md` (MainContact).
Round-1 structural facts are context: `research/blocks/hero2-form.md` (H2-01…10),
`research/blocks/main-contact.md` (MC-01…09). This file adds the **pixel + component contract**.

Tokens (canon, `ampy-foretagsdata` §11 / `ampy-design-system`): teal `#00a991`, midnight `#090b32`,
Outfit. Mint submit-gradient = the site's single "action" gradient. Spacing/type given in **px** (390px
mobile / 1440px desktop CSS reference); map each to the nearest `ap*` token — px is authoritative here.

---

## The problem this spec solves (why "one language")

Today the **same job — capture a qualified lead** — is rendered in **three unrelated visual dialects**:

- **Hero_2 `.aof`** (`svc-elcentral--mobile--02`): **pure-white fields** with big radius floating on a
  **navy-blue glass card**, white labels, mint submit "Boka rådgivning". Bright, high-contrast, 5 fields.
- **MainContact** (`kontakt--mobile--01/02`): **faint grey fields** (light grey fill, no border) on a
  **white card**, dark labels, teal-gradient pill "Gratis rådgivning". Low-contrast, 6 fields, 2-col pairs.
- **Thank-you `ampy-tack`** (`thank-you--mobile--01`): not a form but the form's **destination** — a glass
  card on aurora bg, empty mint circle (no visible check-glyph in the render), one headline, unanchored
  "5 av 5", one teal pill, a "Till startsidan" dead-end.

Three field treatments (white-bordered / grey-borderless), two submit colours (mint vs teal), two label
colours, two radii, two field-count philosophies. A visitor who sees the Hero_2 form up top and the
MainContact form lower on the *same page* meets two different-looking forms for one company. **This spec
declares ONE field component, ONE submit, ONE label style, ONE reassurance pattern**, then instantiates it
at three densities: **mini (3 fields)**, **full (MainContact)**, **confirmation (thank-you)**.

---

## 0. The shared form language (the component contract — all three inherit this)

### 0.1 Field component `ampy-field` (the single input primitive)

| Prop | Value | Notes |
|---|---|---|
| Height | **56px** (mobile), 52px (desktop) | thumb-comfortable, 35–65 audience |
| Radius | **12px** | one radius everywhere (kills Hero_2's ~16px vs MainContext mismatch) |
| Fill (on light card) | `#ffffff` | |
| Fill (on navy card) | `#ffffff` at 100% | keep Hero_2's white field — it reads as a real field |
| Border (rest) | **1px solid `#d5dde5`** on light · **1px solid rgba(255,255,255,.14)** on navy | **borders are mandatory** — kills MainContact's borderless grey "field wall" (MCD-04) |
| Border (focus) | **2px solid `#00a991`** + `0 0 0 3px rgba(0,169,145,.18)` glow | one teal focus ring, both cards |
| Border (error) | 1.5px `#e5484d` + helper text below | |
| Label | Outfit **600, 15px**, `#3a4658` on light / `#dbe3ec` on navy (≥AA on navy, fixes D-05) | label ABOVE field, 6px gap |
| Placeholder | Outfit 400, 16px, `#8a97a6` | never used as a label |
| Padding | 16px horizontal | |
| Required mark | **none visible** — required is the default; mark the *optional* ones "(valfritt)" instead | removes the `*` asterisk noise |

### 0.2 Submit button `ampy-submit` (one action signal on the whole site)

- **Mint action-gradient only** (`#00d9a3 → #6ee787`-family, the existing "Boka rådgivning" fill), dark
  midnight text `#090b32`, **600/17px**, height 60px mobile / 56px desktop, radius 14px, full-width.
- This is the **single** gradient allowed in any form context. MainContact's teal-gradient pill is
  **retired** and replaced by this mint submit (unifies MCD-09 + D-06). No other gradient button may sit
  in the same block as a form.
- States: rest → hover (`translateY(-1px)` + shadow lift) → active → **loading** (label swaps to spinner +
  "Skickar…", button disabled) → success handled by redirect.

### 0.3 Reassurance line `ampy-reassure` (the de-risk microcopy, ALWAYS above the submit)

One line, `#00a991` check-glyph + text, Outfit 500/14px, placed **immediately above** the submit on every
form: **"Skicka in — vi ringer dig inom 24 timmar. Kostnadsfritt."** This is the load-bearing fix: the 24h
promise must precede the click on every surface (MCD-02). One sentence, one place, every form.

### 0.4 The three densities

| Instance | Visible fields | Where | Card |
|---|---|---|---|
| **mini** | 3 (Namn · Telefon · Postnummer) | Hero_2 geo/commercial, lead-magnet wrappers, sticky | small |
| **full** | 2 default + disclosure (MainContact) | page-bottom close | two-pane |
| **confirmation** | 0 (post-submit) | /thank-you | glass |

---

## PART A — SSR inline mini-form (3 fields)

The compact instrument for **köpredo** intent (Hero_2 Riktning B geo/commercial pages) and as the form
that wraps orphan lead-magnets. Server-rendered skeleton so it is **visible at first paint** (kills
D-11/H2-07 — today the JS-injected form paints last; a paid visitor at LCP ~9–10s sees a blank box).

### A.1 Vad ögat möter (mobil, 390px)

Target: the whole form reaches the thumb **inside the first ~1.3 viewports**, and the first glance reads
**three fields, not a wall** (fixes D-02 — today 5 white rectangles fill an entire navy screen).

Stack, top→bottom, on the navy glass card:
1. **Locked service chip** (only where URL fixes the service): a small pill `Gäller: Elcentral` — teal
   1px outline, 13px, lock glyph. **Not a dropdown** (kills D-10's locked select). Omitted on plain
   `elektriker-i-{ort}`.
2. **Card heading** "Få kostnadsfri rådgivning" (Outfit 700, 26px, white) + sub (15px, `#dbe3ec` AA) "Vi
   ringer dig inom 24 timmar — kostnadsfritt."
3. **Namn** field.
4. **Telefonnummer** field (`inputmode="tel"`, `+46` prefix chip inside left).
5. **Postnummer** field (`inputmode="numeric"`, maxlen 6, `123 45` placeholder).
6. **Disclosure link** "Fler uppgifter (e-post, adress) →" — text link, teal, 15px. Reveals E-post +
   Adress (Places autocomplete lives INSIDE here, not up top).
7. **`ampy-reassure`** line (24h promise).
8. **Mint submit** "Boka rådgivning".
9. **Micro-trust** row (13px, `#aeb9c6`): "Behörig elektriker · F-skatt · ROT direkt på fakturan".
10. GDPR: **collapsed to one small line** with checkbox — "Jag godkänner [integritetspolicyn]" 13px. Not a
    heavyweight block above the submit.

**Kundtyp (Privat/BRF/Företag):** moved **below** the fields as a small segment control, default Privat
pre-selected (90%+), so it is not the first thing the visitor must decide (D-10). B2B visitors self-select.

### A.2 Vad ögat möter (desktop, 1440px)

Two-pane navy hero, form = right pane (~44%). Same field set, but Telefon+Postnummer may pair 2-col to
shorten the card. The **dead lower-left quadrant** (D-03) is filled by a muted service photo behind the
left text (70% midnight overlay). Card gets a **1px teal edge + soft shadow** so it lifts off the navy
hero (D-05). Reassure line + mint submit anchor the card floor.

### A.3 Zones & element list (build)

```
[ampy-mini-form]  (SSR, wrapper-scoped .amf-*)
├ .amf-chip        (optional locked-service pill)
├ .amf-head        h3 + p.sub
├ .amf-fields
│  ├ ampy-field  name="namn"        label "Namn"
│  ├ ampy-field  name="telefon"     label "Telefonnummer"  prefix +46
│  └ ampy-field  name="postnummer"  label "Postnummer"
├ .amf-more        <button> "Fler uppgifter →"  → reveals:
│  ├ ampy-field  name="epost"   label "E-post (valfritt)"
│  └ ampy-field  name="adress"  label "Adress (valfritt)"  Places autocomplete + manual fallback
├ .amf-segment     Privat|BRF|Företag  (default Privat)
├ .amf-reassure    24h promise
├ .amf-gdpr        checkbox + integritetspolicy link
├ ampy-submit      "Boka rådgivning"
└ .amf-microtrust  "Behörig · F-skatt · ROT"
```

Sizes: card padding 24px mobile / 32px desktop; field gap 16px; heading→first field 20px;
reassure→submit 12px; submit→microtrust 12px.

### A.4 SSR / performance contract (D-11)

- The **card chrome + heading + 3 fields + submit** are server-rendered in Bricks HTML (static markup),
  NOT injected by JS. JS only **hydrates**: the URL→service resolver (fills the chip), Places autocomplete
  (lazy, only after "Fler uppgifter" is opened), validation, honeypot, submit→n8n.
- At first paint the visitor must **see a form**, even before JS. Skeleton = real inputs, disabled until
  hydrate, then enabled. Never a blank blue box.

### A.5 States

Rest · focus (teal ring) · error (per-field helper, aria-live) · disclosure open/closed · segment
selected · submit loading ("Skickar…") · network-fail (inline retry banner, never a lost lead).

### A.6 Copy patterns (Swedish, ampy-röst — du-tilltal, candour)

- Heading: **"Få kostnadsfri rådgivning"** (never "!"-suffixed here — it's a working form, calm).
- Sub: **"Vi ringer dig inom 24 timmar — kostnadsfritt."**
- Submit: **"Boka rådgivning"** (keep — it is the strongest existing action label).
- Disclosure: **"Fler uppgifter (e-post, adress) →"**
- Reassure: **"Skicka in — vi ringer dig inom 24 timmar. Kostnadsfritt."**
- Micro-trust variants by page type: service → "Behörig elektriker · F-skatt · ROT på fakturan";
  laddbox → "Behörig · Grön teknik 50% direkt · fast pris"; eljour → "Behörig · jour dygnet runt".

### A.7 Candour gates (A)

- **No unanchored "5.0 / 5 av 5"** inside or beside the mini-form. If a rating is shown it MUST carry a
  count ("★★★★★ · {N} omdömen på Google") pulled from `ampy-foretagsdata`; missing count → omit the row,
  use micro-trust instead. (Kills D-07 at the form.)
- No fake urgency, no countdown, no "endast X platser".
- "Hela Sverige" allowed in copy (owner directive 2026-07-18); geo-routing is ops-only.

---

## PART B — MainContact mobile restack (the full form)

Baseline = Riktning **C** from `maincontact-design.md` (cheap reorder+resize, kills the P1 mobile
inversion MCD-01/02/03) with the field-diet of Riktning **A** and the phone line of Riktning **B** adopted
regardless. Desktop two-pane is **kept** (its best state) — only details change. This section specs the
**mobile sequence** and the shared-language retrofit.

### B.1 Vad ögat möter (mobil) — the required new order

Today (`kontakt--mobile--01`): a **3-line display-set quote fills the entire first screen**; the form is a
full scroll down; the 24h promise lands *after* the submit. Restack to:

1. **Header** (unchanged).
2. **Compact proof header** — NOT the giant quote. One anchored line **"3 000+ genomförda installationer
   om året"** (Outfit 700, 22px, white) + small ★★★★★ · {N} på Google (only if count exists) on the navy
   photo, ~30vh, base-scrimmed (navy→transparent bottom, fixes MCD-07). The 15ch display quote is **killed
   as a hero**; it returns lower as a small card (step 6).
3. **"Så går det till" — 3 steps**, horizontal, small icons (✈ Skicka in · ☎ Vi ringer inom 24 h · ☑
   Kostnadsfri rådgivning). This reassurance now sits **before** the form (MCD-02).
4. **Form card** (white), using `ampy-field`:
   - Heading "Få en kostnadsfri **rådgivning**" (last word teal) + sub "Bli uppringd av vår behöriga
     elektriker som konsulterar dig från start till mål." (both KEPT — on-voice).
   - **Namn** (single field — collapse Förnamn/Efternamn) + **Telefonnummer** (`+46`). These two are the
     default-visible callback minimum (MCD-05).
   - **Postnummer** (only if lead-routing needs it).
   - **Disclosure "Lägg till detaljer (valfritt) →"** wrapping E-post · Adress (Places) · Meddelande.
   - **`ampy-reassure`** 24h line.
   - **Mint submit "Bli uppringd"** (retires the teal pill + the noun label; a verb naming the outcome,
     MCD-09).
   - **Phone line** directly under submit: **"Hellre prata direkt? Ring 010-265 79 79"** — calm secondary,
     teal text + phone glyph, `tel:` link. This block must present **both** conversion routes (MCD-06);
     2 of 3 identifiable paid sessions were phone clicks.
5. **Micro-trust** row (behörig · F-skatt · ROT).
6. **Quote as a small card** — the testimonial now at body size below the submit, supporting not
   dominating (MCD-01).
7. **`#f5f9ff` spacer row** before the cyan "Populära kategorier" prefooter, softening the hard
   dark→cyan seam (MCD-10).

### B.2 Vad ögat möter (desktop) — keep the two-pane, fix details

- **Left photo pane:** top-align the quote+proof cluster (fills the empty upper third, MCD-08); add a
  short eyebrow "Vad kunder säger" near the wordmark. **Base scrim** behind the 3-step row so white icons
  hold contrast over the lit windows (MCD-07).
- **Right form pane:** swap grey borderless inputs for `ampy-field` (1px border + teal focus). Namn single
  field + Telefon 2-col with E-post *inside* the disclosure; Adress/Meddelande in disclosure. Mint submit
  "Bli uppringd" replaces the teal pill. Add the "Ring 010-265 79 79" secondary line under the submit.
- Keep the 48/52 photo/form split, the emotion-left/mechanism-right frame — its best state.

### B.3 Zones & element list (mobile)

```
[main-contact  mobile restack]
├ .mc-proof      (navy photo ~30vh, scrimmed)
│  ├ eyebrow "Vad kunder säger"
│  ├ h-count "3 000+ genomförda installationer om året"
│  └ rating  ★★★★★ · {N} på Google        (only if N exists)
├ .mc-steps      3-step "Så går det till"
├ .mc-card       (white)
│  ├ h3 "Få en kostnadsfri rådgivning"  (teal last word)
│  ├ p.sub
│  ├ ampy-field namn
│  ├ ampy-field telefon (+46)
│  ├ ampy-field postnummer            (conditional)
│  ├ .mc-more "Lägg till detaljer (valfritt) →"  → epost · adress(Places) · meddelande
│  ├ .amf-reassure  24h
│  ├ ampy-submit "Bli uppringd"
│  └ .mc-phone "Hellre prata direkt? Ring 010-265 79 79"
├ .mc-microtrust
├ .mc-quote-card (testimonial, body size)
└ .mc-spacer #f5f9ff
```

### B.4 States & data

Same field states as §0.5. Field diet is an **A/B** tracked to Closed Won (per MC-03/07) — variant A =
Namn+Telefon only; control = current 6. Native Bricks form → n8n webhook → /thank-you (unchanged plumbing;
E.164 phone gate, honeypot, a11y live regions retained).

### B.5 Candour gates (B)

- **"3 000+…"** stays on **every** breakpoint (strongest candour-safe proof — MCD-03); it must NOT be the
  line dropped on mobile.
- **"5 av 5" only with a review count**, else omit (MC-02). Never assert "5.0" bare.
- One vocabulary: heading, submit and /thank-you all say **callback within 24h** — no "gratis rådgivning"
  vs "kostnadsfri rådgivning" split (MC-06).

---

## PART C — Thank-you `ampy-tack`: the Efter-submit design

Today (`thank-you--mobile--01`, `--desktop--01`) is a **dead-end**: aurora bg, glass card, an **empty mint
gradient circle with no visible check-glyph**, "Din förfrågan har blivit mottagen!", one sub line, an
**unanchored "5 av 5 · Betyg på Google"**, a teal "Utforska våra eltjänster →" pill that pushes the
just-converted lead back into browsing, and a "Till startsidan" ghost. It answers *nothing* the anxious
converter now asks: **when will you call, what should I have ready, who are you, how do I reach you if I
miss the call.** This is the highest-trust moment on the site and it is spent on a decorative check + a
detour link.

Redesign = a **post-submit workspace**: confirm → set expectation → prepare the visitor → humanise the
team → let them save the number. Four zones on the existing aurora glass card.

### C.1 Vad ögat möter (mobil) — new stack

1. **Confirmation zone** — a **real animated check** (mint circle with a drawn `✓` stroke, 300ms
   draw-on), then "Tack — vi har fått din förfrågan" (Outfit 700, 28px, midnight) + **the concrete SLA**:
   "En behörig elektriker ringer dig **inom 24 timmar**." (the promise made on the form is now *kept* in
   writing). Replace the empty circle bug (no glyph today).
2. **Förberedelse-checklista** — "Så förbereder du dig till samtalet" (Outfit 600, 18px) + 3–4 check-items
   in a light `#f5f9ff` card, each `#00a991` check glyph + one line:
   - "Ha din adress och postnummer redo"
   - "Fundera på vad du vill ha gjort (t.ex. byta elcentral, koppla in vitvara)"
   - "Ta gärna ett foto på det som ska åtgärdas"
   - "Kolla om ROT-utrymme finns — vi drar av 30% direkt på fakturan"
   This is the MECLABS HealthSpire logic applied post-submit: give the converter something *useful* to do
   in the wait, which also **pre-qualifies the call** (better lead, shorter call).
3. **Team-faces zone** — "Du kommer att prata med en av oss" + a **row of 3–4 real electrician avatars**
   (round, 56px, from the Team CPT) with first names under. Humanises the "will they answer later" fear
   (Byggahus/Reddit anxiety in business-context). No fake faces — real team photos only.
4. **Spara-numret zone** — a calm card: "Missar du vårt samtal? Spara vårt nummer så känner du igen det:"
   + **"Ring 010-265 79 79"** as a `tel:` action (secondary weight) + an **"Lägg till i kontakter"**
   `.vcf` download link (a real vCard). This closes the "unknown number → ignored call" leak — the single
   most common way a callback lead is lost.
5. **Quiet footer** — a small "Under tiden: läs våra vanligaste frågor om {service}" text link (internal,
   low weight) replaces the loud teal "Utforska våra eltjänster" pill. Keep "Till startsidan" ghost.

**Removed:** the unanchored "5 av 5" trust row (candour — this page has no space for a bare rating), and
the browse-detour primary pill (a just-converted lead should be reassured, not re-shopped).

### C.2 Vad ögat möter (desktop)

Same four zones, centred ~640px column on the aurora bg. Confirmation + SLA top; checklista and
team-faces can sit **2-col** (checklista left ~58%, team-faces + spara-numret stacked right ~42%);
footer link centred. The glass card widens to hold the checklista comfortably; the today-desktop card is
mostly empty whitespace around one headline — this fills it with substance, not decoration.

### C.3 Zones & element list

```
[ampy-tack  redesign]
├ .tack-confirm
│  ├ .check   (animated ✓ draw, mint circle)   ← fix empty-circle bug
│  ├ h1 "Tack — vi har fått din förfrågan"
│  └ p.sla "En behörig elektriker ringer dig inom 24 timmar."
├ .tack-prep        (card #f5f9ff)
│  ├ h2 "Så förbereder du dig till samtalet"
│  └ ul.check-list  (3–4 items, teal glyphs)
├ .tack-team
│  ├ h2 "Du kommer att prata med en av oss"
│  └ .avatars  (3–4 real Team-CPT photos, first names)
├ .tack-save       (card)
│  ├ p "Missar du samtalet? Spara vårt nummer:"
│  ├ a.tel  "Ring 010-265 79 79"
│  └ a.vcf  "Lägg till i kontakter"
└ .tack-footer
   ├ a "Läs vanliga frågor om {service} →"  (quiet)
   └ a.ghost "Till startsidan"
```

Sizes: card padding 32px mobile / 48px desktop; check circle 72px; avatar 56px; zone gaps 28px; SLA line
17px `#3a4658`.

### C.4 States & data

- The check animates **once** on load (respect `prefers-reduced-motion` → static check).
- `{service}` and the checklist's service-specific line are populated from the **submitted form's service
  value** (URL param or n8n redirect param) — e.g. laddbox thank-you shows "Grön teknik 50%" not "ROT
  30%". Fallback = generic wording.
- Avatars pull from Team CPT (same source as the Team block); if unavailable → omit the row, never
  placeholder faces.
- The `.vcf` is a static file (name "Ampy", org, tel) — no PII collected, safe.
- GA4/Ads conversion still fires on this pageview (unchanged — do not move the pixel).

### C.5 Candour gates (C)

- **No unanchored "5 av 5"** on the page (removed). If a rating returns it needs a count from
  `ampy-foretagsdata`.
- The **24h SLA is a written promise** — it may only appear if the ops SLA is owner-confirmed (memory:
  callback-promise still SLA-gated). If not confirmed, soften to "hör av oss så snart vi kan" — but never
  invent a tighter number than ops can keep. `[GAP]` = confirm 24h SLA before this ships.
- Team faces = **real** electricians only.

---

## Reasoned against existing blocks

- **vs Hero_2 `.aof` (block 1):** the mini-form IS the Riktning-B form-in-hero, but re-skinned to the
  shared language and SSR'd. It **removes** the second green "/kontakt/" CTA and the blue "Ring" gradient
  from the hero (D-01/D-06), leaving mint submit as the only gradient. It keeps Hero_2's white fields
  (they already read as fields) but **adds the 1px border + teal focus** and **cuts 5→3 visible fields**.
  Nothing about the navy hero surface, the H2 scale, or the mint submit colour changes — only field count,
  the two rival CTAs, and paint order.
- **vs MainContact (block 4):** MainContact becomes the **full** density of the *same* language. Its
  faint borderless grey fields are replaced by `ampy-field`; its teal-gradient pill is replaced by the
  mint submit (so a page carrying both Hero_2 and MainContact no longer shows two different green
  buttons). The desktop two-pane frame is **protected** — only the mobile order and the field affordance
  change. The mini-form and MainContact are now visibly the same product at two sizes.
- **vs MainCTA / BlueCTA / Mikro_CTA (blocks 5/7/6):** these are **call** assets, not forms — out of this
  spec's scope, but the shared-language rule "one gradient owns the action per block" means where a form
  and a CTA co-exist, the CTA drops to secondary (ghost/outline) so it never competes with the mint
  submit. (The owner's 5.0-row-focus finding for MainCTA is handled in that block's own audit.)
- **vs Testimonials (block 9, LOCKED):** the thank-you team-faces and the MainContact quote-card **do not
  duplicate** the testimonials slider — they are single, static, contextual trust (one quote / a face
  row), not the 12-review carousel. No overlap, no second slider.
- **vs Thank-you `ampy-tack` (block 27):** same aurora glass shell, same GA4 pixel — but the empty
  decorative body is replaced with four working zones. It stops being a dead-end and becomes the wait-
  management surface the converted lead actually needs.
- **vs lead-magnet orphans (business-context):** the **mini-form** is the reusable "contact close" the
  orphan calculators lack — dropped under Energikalkylatorn et al. (owner's own fix: Alt-hero on top, Vår
  process, then a contact form below). The mini-form IS that below-form, in the shared language.

---

## Vad som INTE ska röras (protect what works)

- **Mint submit-gradient** as the site's single action colour — it stays; rivals around it are what get
  demoted. Never recolour it.
- **Hero_2's white fields on navy** — they already read as fields; only add border + focus, don't darken.
- **MainContact desktop two-pane** (emotion-left / mechanism-right) — best state on the site; keep the
  frame, restack only mobile.
- **"3 000+ genomförda installationer om året"** — strongest candour-safe proof; elevate, never drop.
- **The MainContact sub-line** ("Bli uppringd av vår behöriga elektriker…") and the **testimonial words**
  — on-voice; keep, only resize/reposition.
- **Thank-you aurora glass shell + the GA4/Ads conversion pixel on the pageview** — keep the surface and
  never move the pixel; only the card's body content changes.
- **The per-page locked service** (message-match) — keep the logic; present as a chip, not a dropdown.
- **Ring 010-265 79 79 as a permanent second conversion route** — now present in the mini-form, MainContact
  and thank-you; always calm-secondary weight, never a rival gradient to the mint submit.
