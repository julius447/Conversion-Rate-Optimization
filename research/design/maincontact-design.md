# MainContact (`main-contact`) — design audit (round 2)

Scope: the two-pane contact card (foto-panel + formulär) as a *rendering*. Canonical clean
instance = **/kontakt** (full-bleed, both panes visible). On home/svc-elcentral/geo-tyreso the block
sits far below the fold after 6–10 blocks (round-1 **MC-05**) and the form duty up top is carried by
Hero_2 — so /kontakt is where the block is seen whole and is audited here. Structural facts
(placement, field contract, candour claims) are round-1: `research/blocks/main-contact.md` (MC-01…09).
This file adds the pixel layer those findings did not cover.

---

## Vad ögat möter (mobil)

Screen 1 (`kontakt--mobile--01`): under the header the page turns into a **dark navy photo pane that
fills the entire first viewport**, and on it sits one thing — the testimonial quote *"Från start till
mål levererades en service i världsklass."* set as a **huge 3-line white display headline**, then a gold
★★★★★ row + *"5 av 5 · Betyg på Google"*. That is the whole first screen. **No form, no CTA, no
offer headline, no phone number is visible.** The eye's first, second and third landing are all the
quote. The conversion mechanism starts one full screen down.

Then (`--01` bottom → `--02`) the white form card floats over the photo: *"Få en kostnadsfri
**rådgivning**"* (last word teal) → sub → a **single-column stack of six low-contrast field boxes**
(Förnamn, Efternamn, E-post, Telefonnummer `+46`, Adress `Sök efter din adress` + *Ange adress manuellt*,
Meddelande `Valfritt meddelande`) → a **teal gradient pill "Gratis rådgivning →"** → integritets-line.

Below the card (`--02`) the dark photo continues as a band holding the **3 steps** — ✈ *Skicka in dina
uppgifter* · ☎ *Vi ringer dig inom 24 timmar* · ☑ *Kostnadsfri rådgivning av elektriker* — white text on
the dark base of the photo, then a hard cut into the **cyan "Populära kategorier" prefooter**.

Two things are wrong on sight: (1) the 3-step reassurance — including **the 24-timmar promise — lands
*after* the submit button**; the visitor is asked to press before being told what pressing does. (2) the
*"3 000+ genomförda installationer om året"* volume line that is on desktop **is gone on mobile**; mobile
keeps only the weaker, unanchored *"5 av 5"*.

## Vad ögat möter (desktop)

`kontakt--desktop--01`: a clean **two-pane card**, photo-left / form-right, roughly 48/52.

- **Left photo pane** (dark-navy-overlaid photo of a black gable house at dusk, warm-lit windows): white
  `ampy` wordmark top-left → a large empty upper third → vertically-centred cluster: quote (white,
  ~2 lines) + ★★★★★ *5 av 5 · Betyg på Google* + *3 000+ genomförda installationer om året* → then at the
  pane floor a **horizontal 3-step row** with thin white line-icons. The composition is calm and
  competent; the flaw is that the steps sit **over the brightest part of the photo** (the glowing
  windows), so *"Kostnadsfri rådgivning av elektriker"* is the lowest-contrast text on the page.
- **Right form pane** (white): heading *"Få en kostnadsfri **rådgivning**"* → sub *"Bli uppringd av vår
  behöriga elektriker som konsulterar dig från start till mål."* → **Förnamn / Efternamn** (2-col) →
  **E-post / Telefonnummer** (2-col, `+46`) → **Adress** (full-width, Places search, *Ange adress
  manuellt* top-right) → **Meddelande** (full-width, *Valfritt*) → **teal gradient pill "Gratis
  rådgivning →"** full-width → integritets-line.

The desktop pane is the block at its best: emotion left, mechanism right, one dominant green button. The
defects are quieter — field affordance, label vocabulary, the photo-scrim, and a **missing phone number
on a contact page** (see Fynd).

---

## Fynd

**MCD-01 — The giant quote eats the entire first mobile screen; the form is a full scroll away.**
`kontakt--mobile--01` spends the most valuable viewport on a 3-line display-set testimonial. On a
`/kontakt` visit (highest intent on the site) the first screen shows zero conversion affordance. This is
the visual mechanism behind round-1 **MC-04** (mobile inverts proof vs. reassurance) — the pixel cause is
the **15ch display treatment** of the quote. Decoration is dominant; the ask is invisible.

**MCD-02 — The reassurance strip (incl. "Vi ringer dig inom 24 timmar") is below the submit on mobile.**
The one piece of content that answers *"what happens if I press this / is it free / how fast"* renders
**after** the CTA (`--02`). MECLABS: anxiety (−2a) must be reduced *before* the click, not after. Desktop
places the steps beside the form (visible during fill); the mobile restack strands them. (MC-04.)

**MCD-03 — Volume proof is dropped on mobile; only the weaker claim survives.** *"3 000+ genomförda
installationer om året"* (a concrete count) is present desktop, absent mobile; *"5 av 5"* (no review
count — round-1 **MC-02** candour flag) is kept on both. Backwards: the anchored, candour-safer number is
the one that should survive the small screen.

**MCD-04 — Input fields read as faint grey bars, not fields.** Boxes are a very light grey fill on white
with **no border and no visible focus-affordance in the static render**; labels are dark and fine. For a
35–65 audience the six empty low-contrast rectangles read as an undifferentiated "field wall" — a form,
not a conversation. The affordance problem is worst on mobile where all six stack full-width single-column
(the desktop 2-col pairing that shortens the wall is gone), producing a long grey ladder.

**MCD-05 — Six fields, incl. required full street address, for what is a phone callback.** The offer is
*"Bli uppringd … via telefon"* — functionally that needs **Namn + Telefon**. Yet Adress is required
(`*`) with a heavyweight Places autocomplete, plus E-post and Efternamn. This is round-1 **MC-03** seen as
a design mass: the pane *looks* like a long form because it *is* one, for a job that doesn't need it.

**MCD-06 — /kontakt's primary contact block offers no phone number.** The MainContact card has **only a
form**; the number `010-265 79 79` appears solely in the footer (`kontakt--desktop--02`). On a page whose
entire purpose is contact, and where 2 of 3 identifiable paid sessions were **phone clicks** (business
context), hiding the phone below the form is a lost path. The block presents one of the site's *two*
conversion routes and omits the other.

**MCD-07 — Photo-pane steps sit over the photo's bright zone.** Desktop `--01`: the thin white icons +
white step labels cross the warm-lit windows of the house; contrast dips below comfortable on the third
step. No base scrim/gradient protects the text from the photo's variable luminance.

**MCD-08 — Left-pane vertical rhythm wastes the upper third.** Desktop: logo, then a large void, then the
centred cluster, then steps at the floor. The quote is vertically centred, leaving the top third (sky +
lone wordmark) empty. The pane is well-composed but under-fills; the void reads as "unfinished" beside the
dense form.

**MCD-09 — Vocabulary and verb are loose.** Heading says *"kostnadsfri rådgivning"*, the button says
*"Gratis rådgivning"* — two words for one idea (round-1 **MC-06**). And *"Gratis rådgivning →"* is a
**noun, not an action**: it names the reward, not what the press does. For a callback the button should
say the human outcome (*"Bli uppringd"* / *"Ring upp mig"*).

**MCD-10 — Heavy dark→cyan seam under the block on mobile.** The photo band closes straight into the
bright cyan prefooter with no transition — a jarring luminance jump right after the CTA zone, pulling the
eye off the button toward the "Populära kategorier" links (a competing exit).

---

## Omdesign-direktiv

1. **Mobile: demote the quote, promote the mechanism.** Kill the 15ch display treatment; render the quote
   at body/large-body size as a normal testimonial line. Reclaim the first screen for a compact proof
   header (**one** hard line — the anchored volume count, once MC-01 is confirmed) + the offer heading +
   the first fields. The quote becomes supporting, placed as a small card *below* the submit, not the
   hero. (MCD-01, MCD-03)

2. **Move the reassurance above the button.** On mobile, place the 3-step strip — or at minimum *"Skicka
   in — vi ringer dig inom 24 timmar"* as microcopy — **directly under the fields and above/around the
   submit**, so the 24h promise de-risks the click before it happens. Keep the desktop side-by-side.
   (MCD-02)

3. **Give fields a real edge.** Add a 1px border (or a clearly darker fill) + an explicit teal focus ring
   to every input, so the six boxes read as fields at a glance. Cheapest, highest-legibility fix for the
   "field wall". (MCD-04)

4. **Field diet to the callback minimum** (A/B, lead-quality tracked to Closed Won per MC-03/MC-07):
   default-visible = **Namn (one field) + Telefonnummer**; **Postnummer** if routing needs it; collapse
   **E-post / Adress / Meddelande** into one *"Lägg till detaljer (valfritt)"* disclosure. Keep the Places
   widget *inside* that disclosure as the postnummer-filler. The pane shrinks to ~2 boxes + button — it
   stops *looking* like a form. (MCD-05)

5. **Surface the phone in the block.** Add `Ring 010-265 79 79` as a first-class action in the MainContact
   card (a light-blue btn-ring beside/above the submit, or a *"Hellre prata direkt? Ring …"* line under
   the button). This block must present *both* conversion routes, especially on /kontakt. (MCD-06)

6. **Scrim the photo base.** Add a bottom-up dark gradient (navy → transparent) behind the 3-step row so
   the white icons/labels hold contrast over the lit windows. (MCD-07)

7. **Fill the upper third.** Top-align (not centre) the quote+proof cluster so it starts higher, or add a
   short eyebrow (*"Vad kunder säger"*) near the logo — close the void without adding noise. (MCD-08)

8. **One verb, one vocabulary.** Button = an action naming the outcome: **"Bli uppringd"** (or *"Ring upp
   mig"*). Align heading + button + /thank-you on one callback promise (24h, once SLA-confirmed).
   (MCD-09, MC-06)

9. **Soften the seam.** Give the block a white or `#f5f9ff` base row below the card on mobile before the
   cyan prefooter, so the CTA zone isn't cut straight into a bright competing block. (MCD-10)

10. **Keep the anchored count on every breakpoint.** Whatever else the mobile drops, *"3 000+ …"* (once
    anchored per MC-01) stays; it is the strongest candour-safe proof the block owns. (MCD-03)

---

## Divergenta riktningar (major block — three)

**Riktning A — "Callback-minimal" (reduce the ask).** Photo pane keeps quote + anchored count. Form pane
collapses to **Namn + Telefonnummer + button "Bli uppringd"**, with a single *"Lägg till detaljer
(valfritt)"* disclosure for the rest, and a compact *"Så går det till"* 3-step strip **above** the button.
Reads as a 30-sekunders återuppringning, not a form. Best matches the block's actual job (callback) and
Baymard field-count logic. *Risk:* less lead enrichment up front — mitigate by asking the rest on the call
or in the disclosure.

**Riktning B — "Två spår" (two explicit paths).** Top of the form pane offers a **first-class phone
action** — big *"Ring 010-265 79 79"* — *and* the callback form below, with a quiet *"eller"* divider. Directly
answers the missing-phone gap (MCD-06) and the Clarity phone-click behaviour: high-intent /kontakt
visitors who just want to talk get a one-tap path; the rest fill the form. *Risk:* two CTAs re-introduce a
choice — resolve with clear hierarchy (phone = calm secondary line, form = primary green button), never
two equal-weight buttons.

**Riktning C — "Trygghets-first restack" (mobile-led rewrite of order).** Re-author the *mobile* sequence:
header → compact proof header (anchored count + stars, small) → **"Så går det till" 3 steps** → form →
**quote as a small card below submit**. The reassurance and the offer own the first screen; the quote
supports instead of dominating. Lowest build cost (reorder + resize, no new components), directly kills
MCD-01/02/03. *Risk:* least differentiated visually — it fixes the hierarchy without making the pane feel
new; pair with directive 3 (field edges) so it still looks upgraded.

Recommended: **C as the baseline restack** (cheap, fixes the P1 mobile inversion), **A layered on** as the
field-diet A/B, **B's phone line** adopted regardless (it is a gap fix, not a variant).

---

## Vad som INTE ska röras

- **The desktop two-pane split** (emotion-left / form-right, one dominant green button). It is the block's
  best state and a proven pattern — keep the frame; fix only the details above.
- **"3 000+ genomförda installationer om året"** as *content*. Once anchored (MC-01) it is the strongest,
  most candour-safe proof on the block — elevate it, never delete it.
- **The teal gradient submit pill's prominence** — full-width, on-brand, high-contrast, the clear focal
  point of the form pane. Change only its *label* (MCD-09), never its weight or colour.
- **The testimonial quote itself** — a genuine, on-voice review. Keep the words; only resize/reposition on
  mobile (MCD-01).
- **The sub-line "Bli uppringd av vår behöriga elektriker som konsulterar dig från start till mål."** —
  clear, warm, on ampy-röst. Keep.
- **The 3-step "what happens next" content** (Skicka in → Vi ringer inom 24h → Kostnadsfri rådgivning) —
  exactly the right trust content; keep the content, only move it (MCD-02) and scrim it (MCD-07).
- **Google Places autocomplete + manual fallback** — good UX *when* address is actually needed; keep it,
  just relocate it into the optional disclosure (directive 4).
