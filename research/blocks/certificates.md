# Certificates — partner logo wall (`certificates`)

**Used on: 290 of 326 pages** (from `data/block-map.json`): elektriker-i 56 · elinstallation-i 56 · eljour-i 56 · laddbox-i 56 · service 22 · ev-product 16 · elektriker-för-X 13 · battery-product 10 · page 5.
**Funnel position: always the 3rd block from the end** — the sequence is invariably `CEBlock → Certificates → FooterSEO` (290/290 verified), absolute position 14–21 depending on template (ev-product pos 14/16; elektriker-i pos 20/22). It sits **6–12 blocks BELOW MainContact** on 289/290 carrier pages (verified distances: 6 blocks ×48 pages, 7 ×126, 9 ×56, 12 ×57). The site's only genuine authority proof arrives after both forms and after all SEO content.

**Live copy verified** (fetched https://ampy.se/elservice/elcentral/, 2026-08-02):

> "Certifikat och partners" (H3) — "Tillsammans med ledande företag och myndigheter säkerställer vi maximal kvalitet, trygghet och service för ditt hem, företag och bostadsrättsförening!"

**Markup verified** (snapshot `data/pages/eljour.html`): navy→#5eb1bf gradient full-bleed section, 3×2 `brx-grid` (`grid-template-columns: 1fr 1fr 1fr`) of six white rounded cards, each a bare `<a>` around an `<img … alt="">`:

| Logo | Link target | Rendered size (CSS-forced) |
|---|---|---|
| Elsäkerhetsverket (`wlsa.svg`) | `https://www.elsakerhetsverket.se/kollaelforetaget/foretagsregister/?foretag=12047521` — the live registry lookup | 49×49 px |
| Skatteverket (`skatt.svg`) | `https://www.skatteverket.se/` (generic homepage) | 49×51 px |
| Naturvårdsverket (`natu.svg`) | `https://www.naturvardsverket.se/` (generic homepage) | 49×49 px |
| ID06 (`1d.svg`) | `https://id06.se/` | 65×26 px |
| Trygg Hansa (`trygg.svg`) | `https://www.trygghansa.se/` (generic homepage) | 74×44 px |
| Rexel (`960px-Rexel.svg`) | `http://rexel.se/swE` (plain http, no target=_blank) | 65×25 px |

Whole block is `data-interaction-hidden-on-load="1"` with enterView fadeIn (1.3 s) on both inner blocks plus a fadeInUp on the decorative `partner-section-overlay.svg` (1193×568) wave.

---

## What it does well

1. **It contains the single most powerful trust asset on the entire site.** The Elsäkerhetsverket card does not link to a brochure — it links straight into **"Kolla elföretaget" / företagsregistret with Ampy's record pre-queried** (`?foretag=12047521`). This is *exactly* the check Swedish authorities tell consumers to run before hiring an electrician (business-context research anchor: "Elsäkerhetsverket registration check + Konsumentverket written-quote advice = the proof a serious Swedish customer looks for"). Inviting the visitor to verify you in a government register is a costly, falsifiable signal — candour-gate-native proof, the opposite of invented social proof. Cialdini authority in its strongest legitimate form.
2. **Real credentials, no fabrication.** ID06 (workforce ID) and Trygg Hansa (insurer) are legitimate trust anchors for the risk-averse 35–65 homeowner whose stated fears (Byggahus/Reddit research) are damage responsibility and "will they answer later".
3. **Ubiquity.** At 290 pages it is already wired into every template that matters — a fix here propagates everywhere in one component edit.
4. Technically light: SVG logos, lazy-loaded, fixed aspect-ratios (no CLS from the logos themselves).

## Issues

### CERT-01 — P1 — The exact check authorities recommend is invisible and anonymous (desktop + mobile)
The Elsäkerhetsverket registry lookup is rendered as a **49×49 px unlabeled logo with `alt=""`**, third block from the footer, on position 14–21. Nothing on any page tells the visitor (a) that Ampy is a registrerat elinstallationsföretag, (b) that they can verify it themselves, or (c) that clicking the shield performs that verification. Evidence: MECLABS heuristic — this block's entire job is reducing anxiety (−2a), and anxiety relief only works **adjacent to the moment of ask**; here it sits 6–12 blocks below MainContact and ~15 blocks below the Hero_2 `.aof` form. The Clarity paid-session recording (47 s visitor going Kontakt → Om oss) is direct behavioral evidence of unmet trust-seeking while this proof sat unreachable below the fold ×20. Mobile: same 3-col grid persists (only override found at ≤780 px is `text-align:center` on the heading), so six ~90–100 px cards with 25–49 px marks — the Rexel and ID06 marks are effectively illegible on a 375 px screen.

### CERT-02 — P1 — Authority dilution: government proof mixed with a wholesaler (desktop + mobile)
Cialdini authority requires *relevant, specific* authority. Skatteverket and Naturvårdsverket link to **generic homepages** — every Swedish company "interacts" with Skatteverket; this proves nothing and a skeptical visitor who clicks learns nothing about Ampy. Rexel is a **materials wholesaler** — a supplier relationship, not a certificate — presented with equal visual weight to a government register. The heading "Certifikat och partners" concedes the confusion: half the wall is neither. Diluting one falsifiable credential across six anonymous logos converts a proof block into wallpaper (Jakob's law: users pattern-match unlabeled logo strips as decorative "as seen in" filler and skip them; NN/g banner-blindness applies to logo walls).

### CERT-03 — P2 — Six outbound exits placed just before the final CTA (desktop + mobile)
All six cards are exit links (`target="_blank"` on five, same-tab on Rexel — the Rexel `http://` link is same-tab, so it *navigates away* from ampy.se entirely) positioned immediately above FooterSEO's "Kostnadsfri radgivning / Ring 010-265 79 79" pair. On a two-conversion site, the last thing before the closing ask should not be a six-door exit row. The `target="_blank"` anchors carry no `rel="noopener"` in the rendered markup (reverse-tabnabbing hygiene; the asenha script only adds rel to `#asenha_ep`-tagged links).

### CERT-04 — P2 — `alt=""` on all six logos + heading demoted to H3 (desktop + mobile)
Every logo is `alt=""` (WCAG 1.1.1 failure for functional images: an image inside a link MUST have a text alternative naming the destination). Screen-reader users hear six unlabeled links; search engines see an empty block. The heading is an **H3** with no H2 ancestor claim — the one block that could legitimately say "auktoriserad/registrerad" in a crawlable heading says only "Certifikat och partners".

### CERT-05 — P3 — Hidden-on-load animation dependency (desktop + mobile)
`data-interaction-hidden-on-load="1"` + 1.3 s fadeIn means the block renders blank until JS runs and the viewport intersects — on a page already flagged at ~9–10 s lab LCP, more deferred-JS visual work, and if the interactions script fails the proof never appears at all. `prefers-reduced-motion` duplicate rules exist but the hidden-on-load gate itself is JS-dependent.

### CERT-06 — P3 — Copy is generic gradsmör (desktop + mobile)
"…säkerställer vi maximal kvalitet, trygghet och service…" is an unfalsifiable claim sitting next to a falsifiable one. The block's honest superpower — *kontrollera oss själv* — goes unsaid. ("!" is fine per owner directive; vagueness is the defect, not tone.)

---

## Recommended changes

**A. Placement economics — clone the proof to the decision zone, keep the wall where it is (the core recommendation).**
Do not "move the block up" wholesale — the wall is the wrong *format* for the decision zone. Instead extract a one-line **verification strip** and mount it where anxiety peaks: (1) directly under the Hero_2 `.aof` form's GDPR row / submit button, and (2) inside MainContact's left trust pane (which already carries the review quote and 3-step process). Pattern direction (not final copy, → ampy-rost): Elsäkerhetsverket mark + "Registrerat elinstallationsföretag — kontrollera oss själva i Elsäkerhetsverkets register" linking to the existing `?foretag=12047521` lookup, plus "Ansvarsförsäkrade via Trygg Hansa". The economics: the registry link already exists on 290 pages but at scroll-depth ~90%; the two forms are where the −2a term of the MECLABS heuristic is actually evaluated. One component edit to two form blocks puts the government-verifiable proof in front of every form impression on the site. HYPOTES (A/B): "Adding the Elsäkerhetsverket verification strip adjacent to the Hero_2 form increases form submits vs. control" — this is the test; the placement logic is the evidence-backed prior.

**B. Rebuild the wall as labeled claims, ranked by proof strength.**
Lead card = Elsäkerhetsverket, visually dominant, with caption naming the action ("Slå upp oss i företagsregistret"). Second tier = ID06 ("ID06-anslutna montörer") and Trygg Hansa ("Ansvarsförsäkring via Trygg Hansa"). Demote or drop Skatteverket/Naturvårdsverket/Rexel from *this* block — Skatteverket belongs in the ROT/Grön-teknik blocks where "vi sköter administrationen direkt med Skatteverket" is already the live claim (verified on /elservice/elcentral/); Rexel is at most a "materialpartner" footnote. Every remaining logo gets a one-line caption stating *what it proves*. Baymard/NN/g: labeled trust seals outperform anonymous ones because users cannot act on marks they can't decode.

**C. Mechanical fixes (same edit, near-zero cost).**
Alt texts naming the destination ("Elsäkerhetsverkets företagsregister — Ampy Nordic AB"); heading to a claim ("Kontrollera oss — registrerade, försäkrade, ID06-anslutna"; H2 or keep H3 but say something); `rel="noopener"` on `target="_blank"`; fix the `http://rexel.se/swE` link or remove it; mobile grid 3→2 columns with captions readable at 375 px; drop `hidden-on-load` so proof renders without JS.

**D. Candour check.** Everything recommended is verifiable: the registry entry is government-hosted, insurance and ID06 must be owner-confirmed current before captioning ([GAP]: confirm Trygg Hansa policy active + ID06 affiliation current + that `foretag=12047521` resolves to Ampy Nordic AB's live record). No ratings, no counts, no urgency introduced.

## Priority score (arithmetic shown)

- **In-place block fix (B+C):** 290 pages × funnel weight 1 (low-page position) × expected effect 2 (medium — labeled proof vs. wallpaper) = **580**.
- **Verification-strip promotion (A):** 290 pages × funnel weight 3 (mounted at hero-form/MainContact, the form zone) × expected effect 2 (medium; honest prior, A/B-testable) = **1740**.

**Composite priority: P1** — not conversion-blocking by itself, but it is the highest-leverage trust edit on the site: the exact proof the audience's own authorities tell them to demand already exists on 290 pages and is currently a 49-pixel anonymous logo three blocks from the footer.
