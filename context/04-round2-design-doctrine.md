# Round 2 — Design-level CRO doctrine (binding for every agent)

## Why round 2 exists (owner's verdict on round 1: 5/10)
Round 1 produced good STRUCTURE (block ordering per template — the one part the owner approved) but failed on DESIGN. Owner's exact criticisms, now binding:

1. **"Det känns som att du inte analyserat designen av någonting."** Round 1 analyzed HTML and numbers, not pixels. Round 2 analyzes the actual RENDERING — screenshots of every key page, mobile (390×, DSF2) and desktop (1440×), are in `data/screenshots/tiles/`. Mobile is the most important surface.
2. **The unit of work is design finesse.** Owner's example of the caliber required: *"MainCTA mår skitbra — rubrik, paragraf, call to action. Men vi borde ta bort '5.0 på Google' för att den tar så mycket fokus. Tar vi bort den blir CTA-knappen hela fokuset. DET är conversion rate optimization."* Every audit must produce findings at exactly this altitude: what steals focus, what earns its pixels, what to remove/move/resize/reweight — element by element, with visual-hierarchy reasoning.
3. **New blocks were specified without appearance.** Every proposed block must now get a full design spec: layout anatomy desktop AND mobile (described precisely: zones, elements, sizes, tokens, states), content slots, and it must be REASONED AGAINST the existing blocks it touches. No block proposal without comparing it to what it replaces/complements.
4. **Challenged calls to re-examine honestly (owner pushback):**
   - **TrustStrip:** linking visitors OUT to Elsäkerhetsverket mid-funnel is questionable — "det leder ju folk bort från sajten." Redesign the proof pattern so verification value is conveyed WITHOUT exporting the visitor (e.g., badge + microcopy, link relegated to footer/om-oss, or non-link presentation). Decide honestly whether an outbound verification link has any place, and where.
   - **"PhoneBand":** wrong frame. MainCTA ("Prata med en elektriker inom 60 sekunder" + ring button) IS Ampy's main call-CTA and is potentially very strong. Do not "replace three CTA blocks with a thin phone row." Instead: audit MainCTA/BlueCTA/MikroCTA as DESIGNS, decide which is the strongest call-asset, refine IT (the 5.0-row-focus finding above is the seed), and only then decide the fate of the others — with design reasoning, not just count-of-asks reasoning.
5. **Hero_2 needs concrete redesigns, not observations.** Owner's design hypothesis to develop seriously: service pages (/elservice/*) may not need the hero form at all — a visitor on "vitvaror" is curious about a SERVICE (show the service: image of a vitvara/elcentral installation, one CTA), while the form belongs on elektriker-i-{ort} where visitors are commercially driven and closer to conversion. Deliver 2–3 fully-described divergent hero redesigns per intent class (house rule: 3 versions for big interventions).
6. **Copy analysis continues** (owner liked it) — but always coupled to the visual carrier: which words at which weight in which position.

## Working method (mandatory)
- **Look first.** `ls data/screenshots/tiles/` — naming: `<slug>--<mobile|desktop>--NN.png`, top-to-bottom order (`tiles-index.json` has counts). Read the tiles for your assigned pages/blocks BEFORE writing a word. Quote what you SEE (spatial relationships, sizes, contrast, crowding, what dominates the first glance) — not what the JSON implies. Mobile tiles are 780px wide (DSF2); desktop 1440px.
- Cookie-consent remnants in screenshots: ignore them.
- For every block: (a) what the eye lands on first/second/third and whether that matches the block's conversion job; (b) desktop AND mobile verdicts separately; (c) concrete redesign directives (remove X / move Y above Z / demote W to caption / single CTA / new image subject), each with the visual-hierarchy or evidence rationale; (d) for major blocks: 2–3 divergent directions, not one.
- Keep round-1 structural findings as CONTEXT (files in research/templates|blocks|synthesis) — do not repeat them; reference IDs. Your file ADDS the design layer.
- Candour gate unchanged. Audience unchanged (35–65 svenska husägare — legibility, calm confidence, no gimmicks).
- Note: the eljour symptom block ("Vad har hänt?"/"Tryck på det du märker", loads 50-eljour-lead-magnet.css) is LIVE on eljour pillar + geo pages but was missed by round-1 fingerprints — the eljour screenshots show it; audit its design fully.

## Output
Write to `research/design/<slug>.md`. Dense, specific, zero filler. Structure:
`# <Scope>` → `## Vad ögat möter (mobil)` → `## Vad ögat möter (desktop)` → `## Fynd` (ID, element, problem, evidence) → `## Omdesign-direktiv` (numbered, concrete) → `## Divergenta riktningar` (for major blocks) → `## Vad som INTE ska röras` (protect what works).
