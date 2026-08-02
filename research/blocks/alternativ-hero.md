# AlternativHero (`laddbox-hero`) — compact dark hero

**Used on: 12 unique pages** (13 block-map entries; /nyheter/ is double-counted as both `page` and `post`):
- **Hub/pillar pages (3):** /elservice/ (pos 2 of 9), /laddboxar/ (pos 2 of 10), /solcellsbatterier/ (pos 2 of 11)
- **Team-member pages (6):** /om-oss/{edvin-gustavsson, felix-calmano, julius-callahan, magnus-harald-metsniin, mio-bergenstrale, yousef-lundqvist}/ (pos 2 of 6)
- **Lead magnets (2):** /batterikalkylator/ (pos 2 of 6), /led-kalkylator/ (pos 2 of 6)
- **News archive (1):** /nyheter/ (pos 2 of 3 — the page is literally Header → AlternativHero → Prefooter plus the post loop)

**Funnel position:** always block #1 after Header — it owns the first screen on every page it appears on. Owner intends to ALSO put it on top of the remaining orphan lead magnets (e.g. Energikalkylatorn), so this audit treats it as a growing template, not a legacy one.

**Verified structure (fetched live /laddboxar/ + /nyheter/; markup from snapshots laddboxar.html, elservice.html, batterikalkylator.html, om-oss-edvin-gustavsson.html):**
Dark navy rounded card (`background-color: #1b1d4a`, radius `--apradius-m`) floating on #f5f9ff → breadcrumbs absolutely positioned top-left (`top: 2rem; left: 2rem`, white, `--aptext-s`) → **`<h3 class="laddbox-hero__heading">`** with white→brightgreen gradient text, `font-size: var(--aptext-2xl)`, `font-weight: 400` → one paragraph (`max-width: 50%` desktop) → two decorative SVG waves (`Vector-4.svg` etc., absolute, 70%/90% height). Team variant adds a 1000×1500 portrait right (`fetchpriority="high"`). **No CTA, no form, no trust element** in any variant. The whole container carries `data-interaction-hidden-on-load="1"` + a `contentLoaded → fadeIn` interaction.

Real copy in the wild: "Laddboxar över hela Sverige" / "Vi installerar marknadsledande laddboxar av högsta kvalitet för dig som vill ladda elbilen hemma eller till företag och bostadsrättsföreningar." (laddboxar) · "Elinstallationer över hela Sverige" (elservice) · "Batterikalkylator: räkna ut vad du tjänar på ett solcellsbatteri" (batterikalkylator) · "Nyheter" (nyheter, no paragraph at all) · "Edvin Gustavsson / Senior Elektriker, Arbetsledare & Kvalitetsansvarig" (team).

**Mobile behavior (from the block's own CSS, @max-480px):** card padding *increases* to `--apspace-4xl` top/bottom, content stacks column at 100% width, waves shrink to 40%/50% height, no heading-size override (stays `--aptext-2xl`). Breadcrumbs remain absolute at top 2rem over the enlarged padding.

---

## What it does well
- **Compactness is right for its job on listing hubs.** On /laddboxar/ the product grid ("Zaptec Go … Fr. 4 490 kr Läs mer" ×16) starts immediately below — Baymard category-page findings and Jakob's law both favor getting users to the list fast. A tall Hero_2-style hero here would be worse.
- **Message match is clean.** "Laddboxar över hela Sverige" and "Elinstallationer över hela Sverige" state page scope in plain candour register; the paragraph on /laddboxar/ even segments (villa / företag / BRF) with real internal links.
- **Breadcrumbs orient** the visitor on every instance (Hem › Om oss › Edvin Gustavsson) — good NN/g wayfinding, and the only navigational schema-relevant element in the block.
- **On-voice.** No hype, no fake urgency; the batterikalkylator intro honestly frames outputs as "en uppskattad payback-tid". Candour gate: PASS as-is.

## Issues

### AH-01 — **No H1 exists on ANY of the 12 pages; the hero heading is an `<h3>`** · Severity: P0-class defect inside a P1 block
Verified in markup on laddboxar, elservice, batterikalkylator, and Edvin's team page: `<h3 class="brxe-heading laddbox-hero__heading">Laddboxar över hela Sverige</h3>`, and block-map records `"h1": []` for all 13 entries. Three commercial hub pages, both calculators, all six E-E-A-T team profiles and the news archive ship with zero H1. Evidence: basic on-page SEO + WCAG 2.4.6/heading-structure accessibility (screen-reader users land on a page whose first heading is level 3). Mobile: identical (semantic, viewport-independent). This directly undermines the pillar strategy the hubs exist for.

### AH-02 — First-screen container is hidden until JavaScript runs · Severity: P1
`data-interaction-hidden-on-load="1"` + `contentLoaded → fadeIn` on the hero container means the most valuable viewport renders **empty** until the interaction fires. With the site's known ~9–10s lab LCP flag, this delays first meaningful paint on all 12 pages and blanks the hero entirely if JS fails/times out. On team pages the portrait inside the hidden container is even marked `fetchpriority="high"` — the browser prioritizes an image the user can't see yet. Mobile (slow 4G, mid-range Android — the 35–65 homeowner's real device): worst-case surface. HYPOTES: removing hidden-on-load (CSS-only entrance or none) improves LCP and reduces first-screen bounce; testable via before/after CrUX + Clarity dead-time.

### AH-03 — Zero conversion pathway in the most valuable viewport · Severity: P1 on hubs/lead-magnets, P3 on team/news
The block offers no CTA, no phone number, no anchor, no trust row. MECLABS heuristic: first screen delivers title-only value clarity (v weak), zero incentive (i=0), and no next step. On /elservice/ — a page whose whole job is routing service intent (the #1 commercial priority) — the first phone number appears in MainCTA, 2 blocks and several scrolls down. A phone-preferring 55-year-old with "elfel i huset" gets a decorative navy card. Contrast: Hero_2 and Hero-1 both pair CTAs + Google-rating row at the same position. Mobile: the enlarged 4xl padding means the first viewport is ~entirely this CTA-less card. Desktop: paragraph capped at `max-width: 50%` leaves the right half of the card to waves — literal decoration in the F-pattern's hottest zone (NN/g).

### AH-04 — Mobile spends MORE viewport on decoration than desktop · Severity: P1 (mobile is primary)
The 480px query raises vertical padding to `--apspace-4xl` top+bottom while content is still just H3 + 2 lines. On a 812px-high phone, dark card chrome + waves + breadcrumbs consume the first screen to deliver ~15 words. Guidance question answered: **yes, it wastes the most valuable viewport on decoration — and most severely on mobile.**

### AH-05 — One undifferentiated shell for four different jobs + off-token surface · Severity: P2
The same anonymous navy card fronts a product hub, a calculator, an electrician's E-E-A-T profile, and a news archive. Nothing signals "16 laddboxar below", "2-minute tool, no personal data", or "auktoriserad elektriker" — the differentiation cost of a shared block with no variant slots. Also: card bg `#1b1d4a` is off-token (canon midnight = #090b32; teal #00a991 absent), heading weight 400 is light for a page title, and the white→green gradient text is the known gradient-taste risk vs. the 35–65 audience. NOTE: any pixel change is owner-gated (approved-rendering-is-canon rule).

### AH-08 — Breadcrumb label defects in the block's only navigational element · Severity: P3
Verified in markup: on /elservice/ the hero breadcrumb renders **"Hem / Services"** — an English CPT-archive label leaking into an otherwise all-Swedish customer journey (the 35–65 homeowner reads "Services" where every menu item says "Tjänster"). On /batterikalkylator/ the trail reads **"Hem / Ampy batterikalkylator"** — brand-prefixed and redundant on Ampy's own site. Small trust/polish frictions sitting at `top: 2rem; left: 2rem` of the first screen on those pages. Desktop+mobile identical (same absolute element).

### AH-06 — No trust element where sibling heroes carry one · Severity: P2
Hero-1/Hero_2 establish the pattern "hero = headline + CTA + Google-rating row". AlternativHero pages get their first trust proof only at MainCTA/MainContact ("5.0 på Google", "3 000+ genomförda installationer om året") far below. The Clarity trust-seeking visitor (Contact → About Us) suggests proof belongs early (Cialdini authority/social proof). Candour gate: any added rating row must be anchored (score + count + "Betyg på Google" + GBP link) — same requirement as the sitewide unanchored-"5.0" issue.

### AH-07 — On lead magnets it fronts pages with NO conversion close (cross-ref) · Severity: page-level P0, noted here
/batterikalkylator/ verified sequence: Header → AlternativHero → Calculator-UI → FAQ → Prefooter — no MainContact, no form, no process block. The hero can't fix an orphan page alone, but since the owner's stated plan is "AlternativHero on top + Vår process + Main contact below" for all magnets, the block should ship with a **built-in anchor link/CTA slot** pointing to the on-page form so the wrap pattern is self-completing. (Full treatment in the lead-magnet template file.)

## Recommended changes (concrete)
1. **Week-1 semantic fix (near-zero effort, zero visual diff):** change `laddbox-hero__heading` from `h3` → `h1` in the Bricks template (heading text/gradient CSS is class-bound, so rendering is untouched — passes approved-rendering gate). Instantly gives 12 pages an H1. Fixes AH-01.
2. **Remove `hidden-on-load`** on the hero container; if an entrance is wanted, use a CSS-only animation that never hides content pre-JS. Fixes AH-02.
3. **Add two optional ACF-driven slots, off by default** (team/news stay exactly as approved):
   a. **CTA slot** — on hubs: compact pair (green "Kostnadsfri rådgivning" + "Ring 010-265 79 79") reusing the library buttons; on lead magnets: an anchor CTA ("Till formuläret" / scroll-to-calc) closing the AH-07 loop. Copy direction: candour, benefit-first, no urgency.
   b. **Trust/meta slot** — anchored Google row (score + count + GBP link, candour-gated) on hubs; a differentiator line per role: "16 laddboxar att jämföra" (hub), "Tar ~2 minuter · inga personuppgifter krävs" (calculator), certification line (team). Fixes AH-03/AH-05/AH-06 without forking the block.
4. **Mobile viewport budget:** drop @480px padding from 4xl → xl and cap total hero height so H1 + paragraph + the first row of real content (product card / calculator input) are visible within ~700px. Fixes AH-04. HYPOTES: showing the first product/calc row in viewport 1 raises scroll-past-hero engagement; measure via Clarity scroll-depth on /laddboxar/.
5. **Token alignment (owner-gated visual diff):** #1b1d4a → #090b32, consider heading weight 400→500. Present as a before/after screenshot for sign-off, per approved-rendering-is-canon.
6. **Breadcrumb label sweep (zero-risk copy fix):** rename the elservice CPT-archive breadcrumb "Services" → "Tjänster" and drop the "Ampy " prefix from tool breadcrumbs ("Batterikalkylator"). Fixes AH-08.

## Test hypotheses (A/B-phrased)
- HYPOTES: On /elservice/ + /laddboxar/, adding the CTA + anchored-rating slots to AlternativHero (variant B) vs. current (A) increases phone-click + form-start rate per session. Primary metric: tel: clicks + form_start.
- HYPOTES: Removing hidden-on-load fadeIn (B) vs. current (A) reduces bounce on paid landings by improving perceived load; metric: engaged-session rate + LCP field data.
- HYPOTES: Mobile padding 4xl→xl exposing first content row (B) vs. current (A) increases product-card CTR on /laddboxar/.

## Priority score (arithmetic)
- Pages affected: **12**
- Funnel position weight: **3** (block #1, first screen / hero position on every instance)
- Expected effect: **2** (medium — conversion elements live further down these pages, but the block gates the first impression of 3 commercial hubs + 2 lead magnets, and carries the no-H1 + hidden-until-JS defects)
- **Priority score = 12 × 3 × 2 = 72 → P1** (fix in month 1), with AH-01 (h3→h1) and AH-02 (un-hide) pulled forward as week-1 quick wins because effort is trivial and visual diff is zero.
