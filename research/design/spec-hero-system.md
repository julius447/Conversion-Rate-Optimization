# SPEC — Hero-systemet (Hero_2 v2 + intent-varianter)

**Status:** Buildable spec. Finaliserar de tre riktningarna från `research/design/hero2-design.md` (Riktning A/B/C) och `research/design/eljour-design.md` (call-first) till ETT koherent hjälte-system med tre produktionsvarianter, dirigerade **efter besökarens intent**, inte efter mall. En Bricks-byggare ska kunna bygga varje variant härifrån utan fler frågor.

**Källa i pixlar (verifierat mot tiles):** `svc-elcentral` (mobil 01–02, desktop 01), `geo-elektriker-tyreso` (mobil 01), `geo-eljour-taby` (mobil 01), `pillar-elektriker` (mobil 01 = Hero-1-referensen). Struktur-kontext (ej upprepad): H2-01…H2-10 (`research/blocks/hero2-form.md`), E-01…E-12 (`eljour-design.md`).

---

## 0. Systemöversikt — tre hjältar, en intent-router

Dagens problem (bekräftat i pixlar): **en enda Hero_2-mall körs på 260 sidor** oavsett om besökaren är nyfiken (service), köpredo (geo) eller stressad (eljour). Samma tre-asks-hjälte (grön /kontakt/-CTA + blå Ring + helt formkort), samma tomfälts-vägg, samma döda navy-kvadrant, samma oankrade 5.0. En design-fix träffar alla — men fel design på fel intent kostar leads.

Systemet delar hjälten i **tre varianter som väljs av CPT/URL**:

| Variant | Intent | Sidor (CPT) | Hjärtat | Formulär i hjälten? |
|---|---|---|---|---|
| **HERO-S** (service image-hero) | Nyfiken på en TJÄNST | `/elservice/*` — elcentral, vitvaror, belysning, kök/bad m.fl. | Riktig installationsbild + EN CTA som scrollar till formuläret längre ner | **Nej** — formuläret bor i `main-contact` nedanför |
| **HERO-G** (geo form-hero) | KÖPREDO, lokal sökning | `elektriker-i-{ort}`, `laddbox-i-{ort}`, `elinstallation-i-{ort}`, `elektriker-för-X` | Kompakt 3-fälts SSR-formkort, ring som lugn sekundär | **Ja** — 3 synliga fält |
| **HERO-E** (eljour call-hero) | STRESSAD, akut | `eljour-i-{ort}` + eljour-pelarens geo-yta | Dominant grön nödknapp + live-pill + reassurance-bullets; symptom-triage direkt under | **Nej i hjälten** — degraderad till "Hellre bli uppringd? ↓" |
| *(oförändrad)* **Hero-1** | Awareness / pelare / hem | homepage, pillar-sidor | Ägarens vita flytande banner + bild. **Kvalitetsreferens — RÖRS INTE.** | Nej |

**Router-logik (Bricks condition / ACF):** `hero_variant` sätts av post-type:
`elservice → HERO-S` · `elektriker-i|laddbox-i|elinstallation-i|elektriker-for → HERO-G` · `eljour-i → HERO-E` · `page == front || pillar → Hero-1 (befintlig)`.

Alla tre delar **samma token-DNA** (nedan) så systemet läser som ETT system, inte tre block.

---

## 1. Delade tokens & primitiver (gäller alla tre varianter)

Grundade i ampy-design-system (ap*-skalan). Där jag anger px men inte känner det exakta token-namnet: `[token-GAP → design-system äger]`.

### Färg
| Roll | Värde | Användning |
|---|---|---|
| `--ap-midnight` | `#090b32` | Hjältens grundyta (navy). ALDRIG `#010328` (token-defekt, se `visste-du-att`-fyndet). |
| `--ap-navy-aurora` | midnight + radiell aurora-blob (befintlig) | Hjälte-bakgrund; behåll den mörka blobben uppe-höger (syns i alla tiles). |
| `--ap-teal` | `#00a991` | Accent, kicker-gradient, kortkant, stjärnor. **Ej på vit knapp-yta** (klarar ej 4.5:1 mot vitt — se nödknapp). |
| `--ap-mint-grad` | mint→teal gradient (dagens "Boka rådgivning"-yta) | **Den ENDA handlings-gradienten per hjälte.** Submit (HERO-G) / primär CTA (HERO-S). |
| `--ap-emerald-solid` | `#0b8f5a`–`#0e7a4e` mörkgrön solid | **Nödknappen** (HERO-E) — vit text passerar 4.5:1. Kanon från symptomkortets gröna knapp. |
| `--ap-card-glass` | ljusare blå-navy glas (dagens formkort-yta) | Formkort. **Höjs** med 1px `--ap-teal` @ 40% kant + skugga `0 12px 40px rgba(0,0,0,.35)`. |
| `--ap-ink-on-navy` | `#c9d4e0` | Labels/microtext på navy — **höjt från dagens grå** (WCAG AA). Dagens grå faller på D-05/E-nn. |
| `--ap-white` | `#ffffff` | H2, fältytor. |
| severity | röd `Akut` / amber `Varning` | Enbart HERO-E:s symptom-koppling (se §4). |

### Typografi (Outfit)
| Element | Storlek mobil / desktop | Vikt | Färg |
|---|---|---|---|
| Kicker (eyebrow, = H1 semantiskt) | 15px / 16px, **versal-spärrad `letter-spacing:.08em`** | 600 | `--ap-teal` (solid, EJ gradient — se D-08-fix) |
| H2 (visuell rubrik) | 40px / 48px, line-height 1.08 | 700 | vit m. grön gradient på nyckelord (behåll) |
| Paragraf | 17px / 18px, line-height 1.5, **max 3 rader** (`-webkit-line-clamp:3` / redaktionell disciplin) | 400 | vit @ 92% |
| Knapp-label | 17px / 17px | 600 | per knapp |
| Fält-label | 14px | 600 | `--ap-ink-on-navy` |
| Trust-microrad | 13px | 500 | `--ap-ink-on-navy` |

### Spacing / form
- Hjälte-kort radius: **`--ap-radius-xl` ~28px** (matchar dagens stora rundade navy-kort).
- Hjälte-inre padding: mobil 24px, desktop 56–64px.
- Knapp-höjd: **56px mobil**, 52px desktop; radius `--ap-radius-lg ~16px`; full bredd mobil.
- Fält-höjd: 56px; vit yta; radius 14px; inre 16px.
- Kort-max-bredd (formkort): 450px (behåll dagens).

### Delade knapp-primitiver (biblioteket — definieras EN gång, återanvänds)
1. **`btn-primary-mint`** — mint→teal gradient, mörk ink-text, radius 16px, 56px. Den enda gradient-knappen som får finnas per hjälte.
2. **`btn-emergency-green`** — `--ap-emerald-solid`, vit text, vänster telefonglyf, höger liten pulserande grön prick (`● jour öppen`). Kanon för RING på akut-ytor.
3. **`btn-ring-ghost`** — transparent yta, 1px `--ap-ink-on-navy` @ 40% kant, vit text, telefonglyf-chip vänster. **Ersätter dagens lysande ljusblå Ring-gradient överallt** (D-06/E-03). Lugn sekundär.
4. **`link-quiet`** — ren textlänk, telefonikon, `--ap-teal`, understruken vid hover. För "eller ring…" / "Hellre bli uppringd? ↓".

**Regel som binder hela systemet (löser D-01, D-06, E-03):** *En hjälte får bära exakt EN gradient-knapp. Allt annat interaktivt är ghost/text/solid-emergency.* Dagens tre lysande gradienter (grön /kontakt/ + blå Ring + mint submit) reduceras alltid till en.

---

## 2. HERO-S — Service image-hero (`/elservice/*`)

**Intent:** besökaren sökte "installera diskmaskin" / "byta elcentral pris" — hen vill SE att Ampy gör detta tryggt. Visa jobbet, inte en blankett. (Riktning A, ägarens hypotes.)

**Konvertering:** EN primär CTA som scrollar till `#kontakt`-ankaret (det befintliga `main-contact`-blocket på samma sida) + ett permanent synligt ring-nummer. **Inget formulär i hjälten.**

### Zoner
```
DESKTOP (navy-kort, split 50/50)          MOBIL (stack)
┌───────────────┬───────────────┐         ┌───────────────┐
│ breadcrumb    │               │         │  TJÄNSTEBILD   │ 16:9, ~40vh
│ kicker        │  TJÄNSTE-     │         ├───────────────┤
│ H2 (2 rad)    │  BILD         │         │ breadcrumb     │
│ paragraf 3rad │  (fyller      │         │ kicker         │
│ [CTA mint]    │   höger,      │         │ H2             │
│ "eller ring"  │   teal-kant,  │         │ paragraf (3)   │
│ mikrotrust    │   rundad)     │         │ [CTA mint full]│
│               │               │         │ "eller ring…"  │
└───────────────┴───────────────┘         │ mikrotrust     │
   vänster centreras vertikalt            └───────────────┘
```

### Element-lista (uppifrån)
1. **Breadcrumb** — "Hem › Elcentral" (behåll dagens grå; höj till `--ap-ink-on-navy`).
2. **Kicker** — versal-spärrad teal, t.ex. `BYTA ELCENTRAL`. (Semantiskt H1; visuellt liten kicker → löser D-08.)
3. **H2** — vit + grön gradient-nyckelord, max 2 rader. Behåll copyn: "Ny elcentral installerad med 30% ROT-avdrag". **Storlek och gradient-behandling RÖRS INTE.**
4. **Paragraf** — max 3 rader (kap: dagens elcentral-paragraf är redan ~4 rad mobil → trimma sista meningen till content-blocket). Behåll ampy-röst-copyn ("Dags att byta ditt gamla proppskåp?…").
5. **`btn-primary-mint`** — `Få kostnadsfri rådgivning ↗`. **href = `#kontakt`** (on-page anchor scroll, INTE `/kontakt/`). Löser D-01/H2-01: knappen levererar till formuläret på SAMMA sida.
6. **`link-quiet`** — `eller ring 010-265 79 79` (`tel:+46102657979`), telefonikon, under CTA:n.
7. **Mikrotrust-rad** — `Behörig elektriker · ROT 30% direkt på fakturan` (13px, `--ap-ink-on-navy`). **Ingen 5.0 här** (löser D-07). Candour: inga siffror utan ankare.
8. **Tjänstebild (höger desktop / topp mobil)** — riktigt foto av den faktiska tjänsten:
   - elcentral → öppen modern elcentral med automatsäkringar
   - vitvaror → inkopplad tvättmaskin/diskmaskin
   - belysning → monterad taklampa/spotlights
   Rundade hörn (radius-xl), 1px teal-kant @ 40%, mjuk skugga. **Ingen text ovanpå.** Löser D-03 (död kvadrant) + D-04 (ingen tjänstebild).

### States
- CTA: hover → mint-gradient ljusnar 6% + lyft `translateY(-1px)`; focus-visible → 2px teal outline + offset.
- `link-quiet`: hover → understrykning + teal.
- Bild: `loading="eager"` + `fetchpriority="high"` (LCP-kandidat), fast `aspect-ratio` för att undvika CLS.

### Vad ögat möter först → varför
Bilden av tjänsten + H2. Matchar intent: bekräftar "de gör detta, tryggt". Den enda CTA:n har noll rivaler → all uppmärksamhet till ett ask. **Detta ÄR ägarens 5.0-rad-logik uppskalad:** ta bort det som stjäl fokus (formulär + extra CTA + 5.0-rad) → tjänst + en handling blir hela fokuset.

---

## 3. HERO-G — Kompakt geo form-hero (`elektriker-i-*`, `laddbox-i-*`, `elinstallation-i-*`, `elektriker-för-X`)

**Intent:** "elektriker i Tyresö" = lokal, köpredo. Ge det minsta möjliga formuläret omedelbart. (Riktning B, visuellt förfinad.)

**Konvertering:** SSR 3-fälts formkort (primärt) + ring ghost (sekundärt).

### Zoner
```
DESKTOP (navy-kort, split 45/55)          MOBIL (stack, formkort ~1,3 vy in)
┌────────────┬────────────────┐           ┌───────────────┐
│ breadcrumb │  FORMKORT       │          │ breadcrumb     │
│ kicker     │  (glas, teal-   │          │ kicker         │
│ H2 (2 rad) │   kant, skugga) │          │ H2 (2 rad)     │
│ paragraf 2 │  ├ rubrik       │          │ paragraf (2)   │
│ [ring ghost]│  ├ [chip]       │          │ [ring ghost]   │
│            │  ├ 3 fält        │          ├───────────────┤
│ (bild-bakgr│  ├ "fler uppg→" │          │  FORMKORT       │
│  fyller    │  ├ [submit mint]│          │  ├ rubrik       │
│  botten)   │  └ trust-fot    │          │  ├ [chip]       │
└────────────┴────────────────┘           │  ├ Namn         │
   dämpad tjänstebild i vänster botten     │  ├ Telefon     │
                                           │  ├ Postnummer  │
                                           │  ├ "fler uppg→"│
                                           │  ├ [submit mint]│
                                           │  └ trust-fot    │
                                           └───────────────┘
```

### Vänster kolumn (desktop) / topp (mobil)
1. Breadcrumb → 2. Kicker (`ELEKTRIKER TYRESÖ`) → 3. H2 (behåll "Boka en pålitlig elektriker i Tyresö!") → 4. Paragraf **max 2 rader** (dagens tyresö-paragraf är 5 rader → kapa hårt, resten till content) → 5. **`btn-ring-ghost`** `Ring 010-265 79 79`. **Ingen grön /kontakt/-knapp** (D-01). Ingen 5.0-rad i vänsterspalten (flyttas in i formkortets fot).
6. **Bakgrund:** dämpad tjänstebild (elektriker vid elcentral / servicebil) med mörk overlay 70% fyller nedre vänstra kvadranten → dödar den döda ytan (D-03).

### Formkort (höger desktop / under text mobil) — det förfinade `.aof` v2
Glas-yta, **1px teal-kant @ 40%**, skugga `0 12px 40px rgba(0,0,0,.35)` → lyfter tydligt från hjälten (löser D-05/H2-06).

**SSR-innehåll (server-renderat skelett, löser D-11/H2-07):**
1. **Rubrik** — "Få kostnadsfri rådgivning" (17px semibold vit).
2. **Underrubrik** — "Vår behöriga elektriker återkommer via telefon" i **`--ap-ink-on-navy` (AA)**, inte dagens låg-kontrast grå.
3. **Låst service-chip** (endast där URL bestämmer tjänsten, t.ex. `laddbox-i`): liten pill `Gäller: Laddbox` med lås-glyf — **INTE en full dropdown** (löser D-10, halva "Vad gäller arbetet?"-friktionen). På ren `elektriker-i` visas **ingen** chip (tjänsten obestämd — behåll den skillnaden, se "INTE röras").
4. **3 synliga fält** (löser D-02, tomfälts-väggen → 3 vita rektanglar i stället för 5):
   - `Namn` (text, required)
   - `Telefonnummer` (tel, required, E.164-gate på blur)
   - `Postnummer` (text, required, 5 siffror — driver geo-routing)
5. **Disclosure-länk** `Fler uppgifter (e-post, adress) →` → fäller ut `E-post` + `Adress` (Google Places autocomplete + manuell fallback). Progressiv avslöjning: minsta kvalificerande lead synligt, resten på begäran.
6. **Kundtyp-segment** `Privat · BRF · Företag` — **default Privat, flyttad UNDER fälten** som liten segment-kontroll (bara B2B klickar). Löser D-10: ingen kundtyp-toggle som första element.
7. **`btn-primary-mint`** `Boka rådgivning` — **den enda gradienten i hela blocket** (D-06). Posts multipart → n8n → redirect `/thank-you`.
8. **Trust-fot** (i kortets sidfot, precis ovanför submit): **ANTINGEN** `Behörig · F-skatt · ROT direkt på faktura` (rekommenderad — relevant vid formuläret) **ELLER** `★★★★★ · {N} omdömen på Google` **endast med ägarbekräftad räknare** (candour). **Aldrig oankrad "5.0".** (Löser D-07/E-08.)

### States (formkort)
- Fält: default vit; focus → 2px teal ring; error → 1.5px röd kant + hjälptext under (aria-describedby, live-region behålls).
- Submit: disabled tills required + GDPR ok; loading → spinner + "Skickar…"; success → in-place bekräftelse (ingen sid-reload innan redirect).
- Honeypot + a11y live-regions: behåll dagens.
- SSR: kort-chrome + rubrik + 3 fält renderas i Bricks statiskt; JS hydrerar URL-resolvern (chip) + Places. **Minst skelettet SYNS som "ett formulär" vid first paint** → betald besökare ser money-blocket direkt (Clarity 1s-studs-motgift).

### Vad ögat möter först → varför
Desktop: formkortet (ljusare massa, teal-kant) — money-blocket vinner. Mobil: H2 → kompakt formkort inom ~1,3 vy (inte 2+). Tre fält sänker upplevd svårighet (Baymard), submit-gradienten är oomtvistad.

---

## 4. HERO-E — Eljour call-hero (`eljour-i-*`)

**Intent:** elfel 22:30, stressad. Snabbaste, lägsta-friktions-konverteringen är SAMTALET. (Eljour Riktning A + hero2 Riktning C, sammanslagna.)

**Konvertering:** dominant grön nödknapp (primärt) + form degraderad till opt-in. Symptom-triage direkt under (§4b).

### Zoner (mobil — den avgörande ytan)
```
┌───────────────────────────┐
│ breadcrumb "Hem › Eljour i Täby"        │
│ kicker  ELJOUR I TÄBY                    │
│ H1/H2  "Akut elfel i Täby?              │
│         Ring så rycker vi ut."          │
│ ● Jour öppen just nu   ← live-pill UPP  │
│ ┌─────────────────────────────────────┐ │
│ │ 📞  Ring eljouren · 010-265 79 79   │ │ ← btn-emergency-green
│ │     ● (puls)                        │ │   56px, full bredd, DOMINANT
│ └─────────────────────────────────────┘ │
│ ✓ Dygnet runt  ✓ På plats inom en timme │ ← 4 reassurance-bullets
│ ✓ Behörig elektriker, inte en växel     │   DIREKT under (svarar "kommer någon nu?")
│ ✓ Tydligt pris, inga dolda avgifter     │
│ Hellre bli uppringd? Fyll i formuläret ↓ │ ← link-quiet (opt-in)
├───────────────────────────┤
│  SYMPTOM-TRIAGE (§4b)      │ ← direkt under hjälten
```

### Element-lista
1. **Breadcrumb** → 2. **Kicker** `ELJOUR I TÄBY` (teal).
2. **H1/H2** — **kortas**: "Akut elfel i Täby? Ring så rycker vi ut." Numret som `tel:`-länk i knappen, inte i rubriken (dagens "Ring 010-265 79 79!" i H1 läses inte som knapp — E-02).
3. **Live-pill** `● Jour öppen just nu` — flyttad UPP hit (realtidsförsäkran = starkaste motivator, E-04/behåll-listan). Grön prick + solid pill.
4. **`btn-emergency-green` (DOMINANT)** — full bredd, 56px, `Ring eljouren · 010-265 79 79`, vänster telefonglyf, höger pulsprick. Hjältens tyngdpunkt. Kanon-nödknappen (löser E-01/E-02/E-03 — ETT samtalsspråk).
5. **4 reassurance-bullets** direkt under (behåll texten ordagrant — candour-perfekt): `Dygnet runt · På plats inom en timme · Behörig elektriker, inte en växel · Tydligt pris, inga dolda avgifter`.
6. **`link-quiet`** `Hellre bli uppringd? Fyll i formuläret ↓` → scrollar till bottenformuläret. Formuläret degraderas till opt-in, försvinner inte (fångar skriv-hellre-än-ring-leads).
7. **Bakgrund:** dämpad bild (elektriker vid elcentral / servicebil) mörk overlay → fyller hela hjälten, ingen tom yta.

**Bort ur HERO-E:** inline-formkortet (E-01), den gröna /kontakt/-CTA:n, den bleka ljusblå Ring (E-02/E-03), 5.0-hero-raden (E-08). "1000+ kunder"-kortet (E-07 candour-BLOCK) ligger nedströms — ej i hjälte-scope men flaggat: ersätt med snabbhets-/behörighetsbevis.

### 4b. Sticky call-bar (mobil) — hör till HERO-E-systemet
- `position:fixed`, botten, full bredd; dyker upp efter att hjälten scrollat ur bild (IntersectionObserver på hjälten).
- Höjd **64px** + `env(safe-area-inset-bottom)`; tap-target ≥ 48px i tummens primärzon.
- Yta **`--ap-emerald-solid`** (vit text 4.5:1; teal klarar EJ mot vitt).
- Innehåll: telefonglyf + `Ring eljouren` 17px semibold + `010-265 79 79` + liten grön puls-prick. EN handling, ingen form-knapp (skiljer från sticky-headerns "Gratis rådgivning").
- **Sticky-headerns pill byts per intent:** på eljour-mallar → `Ring 010-265 79 79`, inte formulär-CTA (E-04).

### 4c. Symptom-triage-koppling (block bor separat men hjälten leder in i det)
HERO-E:s jobb slutar där triagen tar vid. Direktivet till triage-blocket (från `eljour-design.md`, ej dubblerat här): severity-sortera (Akut röd först), hela raden tryckbar, expanderad Akut-rad bäddar in `btn-emergency-green` inline. Hjälten får INTE upprepa symptomlistan — den pekar in i den.

### Vad ögat möter först → varför
Nödknappen, entydigt. Matchar 22:30-mentaliteten: samtalet är snabbast och lägst friktion, och Ampy har redan ett starkt samtals-erbjudande. Formuläret degraderas till val, inte vägg. Enda riktningen som gör Ampys starkaste tillgång (det snabba samtalet) till hjältens tyngdpunkt.

---

## 5. H1/H2-fixen (gäller alla tre — visuell, ej semantisk teardown)

**Problemet (D-08/H2-03):** dagens gröna eyebrow ("Byta elcentral") ÄR sidans H1 men renderas som liten label; den stora rubriken är H2. Visuell och dokument-hierarki pekar olika håll.

**Fixen (visuell disciplin, ingen tag-omskrivning i detta block):**
- Eyebrow behålls som H1 semantiskt (SEO), men **stylas entydigt som kicker**: versal, `letter-spacing:.08em`, 15/16px, teal SOLID (ej gradient) → ögat läser den korrekt som kategori-label, inte som en förvirrad andra-rubrik.
- H2 bär budskapet (stor, vit+gradient) — orörd.
- Resultat: dokumenthierarki intakt, visuell hierarki entydig, ingen tävlan. (Om SEO senare vill flippa H1/H2-taggning löses det i seo-guard, inte här — detta block ändrar bara vikt/behandling.)

---

## 6. SSR mini-formulärets visuella design (HERO-G, 3 fält)

Detaljspec eftersom formkortet är money-blocket och måste målas vid first paint.

| Slot | Design |
|---|---|
| **Kort** | Glas-yta över navy; radius 28px; **1px `--ap-teal` @ 40% kant**; skugga `0 12px 40px rgba(0,0,0,.35)`; inre padding 28px (desktop) / 20px (mobil); max-bredd 450px. |
| **Rubrik** | "Få kostnadsfri rådgivning" — 20px/700 vit. |
| **Underrubrik** | "Vår behöriga elektriker återkommer via telefon" — 14px/500 `--ap-ink-on-navy` (AA). |
| **Service-chip** | `Gäller: {tjänst}` — pill, teal-tint bg 12%, teal text, lås-glyf 12px, radius 999px, 8×12px padding. Endast på tjänste-bestämda geo-sidor. |
| **Label** | 14px/600 `--ap-ink-on-navy`, 8px över fältet. |
| **Fält** | Vit yta, radius 14px, 56px höjd, inre 16px, text 16px `--ap-midnight`. Focus: 2px teal ring + offset 1px. |
| **Disclosure** | `Fler uppgifter (e-post, adress) →` — 14px teal textlänk, chevron, 12px topp-marginal. Expanderar E-post + Adress med samma fält-stil. |
| **Kundtyp-segment** | 3-segment pill under fälten; aktiv = teal-fylld/vit text; inaktiv = ghost; default Privat. Höjd 40px. |
| **Submit** | `btn-primary-mint` "Boka rådgivning" — full kort-bredd, 56px, mint→teal gradient, mörk ink-text 17px/600. Enda gradienten. |
| **Trust-fot** | 13px `--ap-ink-on-navy`, centrerad, 12px över submit: `Behörig · F-skatt · ROT direkt på faktura` (default) eller ankrad Google-räknare. |
| **GDPR** | Checkbox + "Jag godkänner att Ampy behandlar mina uppgifter enligt integritetspolicyn" — 13px, länk teal. Under submit eller precis över (behåll dagens plats, höj text-kontrast). |

**Fält-ordning fast:** Namn → Telefon → Postnummer → (Fler: E-post → Adress). Motiv: namn+telefon+postnr = minsta kvalificerande lead + geo-routing; adress är säljstöd, inte kvalificering → bakom disclosure.

---

## 7. Candour-grindar (alla varianter)

1. **Ingen oankrad "5.0 / 5 av 5"** i någon hjälte. Betyg visas endast med ägarbekräftad räknare, och då EN gång per sida (i formkortets fot eller MainCTA — aldrig i hero-raden mellan CTA och form). Default: ersätt med behörighets-trust (`Behörig · F-skatt · ROT`).
2. **Ingen fejk-brådska/scarcity.** Live-pillen `● Jour öppen just nu` (HERO-E) är tillåten ENDAST om den speglar verklig jourstatus (realtid), annars statisk `Jour dygnet runt`.
3. **"Vi svarar oftast inom 60 sekunder"** (om använd) — "oftast", aldrig garanti.
4. **Inga påhittade siffror.** Reassurance-bullets ("på plats inom en timme", "1 800 elbränder/år · Elsäkerhetsverket") är verifierade → behåll ordagrant; allt nytt tal → `[GAP]`.
5. **"Hela Sverige" tillåtet i copy** (ägardirektiv 2026-07-18) — geo-routing är separat ops.
6. Ampy-röst: du-tilltal, ärlig, "!" metered, starka superlativ ok om ej bevisligen falska.

---

## 8. Resonerat mot befintliga block ("Reasoned against existing blocks")

| Befintligt block | Relation till hero-systemet | Beslut |
|---|---|---|
| **Hero_2 `.aof` (dagens)** | Det som ersätts. Splittras i HERO-S/G/E. | Ersätt; behåll navy-yta, H2-skala, mint-submit, per-sida service-prefill (som chip). |
| **Hero-1 (homepage/pillar)** | Ägarens godkända vita banner + bild = **kvalitetsreferens**. | **RÖRS INTE.** HERO-S/G/E ärver dess disciplin (en tydlig hierarki, en handling) men inte dess yta (navy vs vit). Awareness/pillar behåller Hero-1. |
| **Alternativ hero `laddbox-hero`** | Kompakt navy utan CTA/form, för lead-magnets & listor. | Oförändrad. HERO-G är INTE denna — HERO-G bär formkort, `laddbox-hero` bär inget. Ingen kollision. |
| **Main contact `main-contact`** | HERO-S:s CTA scrollar hit (`#kontakt`). Detta är sajtens starkaste konverteringsasset. | HERO-S lägger AVSIKTLIGT formuläret här (MECLABS HealthSpire: mer värde före ask). `main-contact` orört; hjälten pekar in i det. Undviker dubbel-formulär på service-sidor. |
| **Main CTA `main-cta`** | Mid-page ring-CTA. Ägarens 5.0-rad-lärdom kom härifrån. | Hero-systemet applicerar samma princip (ta bort fokustjuven). HERO-E:s nödknapp = samma kanon-språk som `main-cta` bör anta. Ej ändrat här, men samordnas: EN grön nödknapp överallt. |
| **Blue CTA `blue-cta`** | Svart Ring-knapp — fjärde samtalsspråket (E-03). | Flaggat: byt till `btn-emergency-green` för konsistens. Utanför hero-scope men samma primitiv. |
| **`.aof`-formulärets service-select** | Per-sida prefill via URL-resolver. | Logiken behålls (smart message-match), presentationen ändras: dropdown → låst chip (HERO-G) / borttagen (HERO-S). |
| **Symptom-block (eljour)** | HERO-E leder in i det. | Hjälten dupleceras INTE med symptom; den pekar. Triage-redesign i `eljour-design.md`. |
| **Header (global, sticky pill)** | "Gratis rådgivning"-pill = formulär-CTA. | På eljour-mallar byts pill-logiken till Ring (E-04). Övriga mallar oförändrade. |

---

## 9. Vad som INTE ska röras (skydda det som funkar)

- **H2:ns storlek + vit/grön gradient-behandling** — vinner första glimten korrekt på alla sidor; läsbar, självsäker, on-brand.
- **Den mörka navy-hjälten som YTA** — premium och särskiljande. Problemet var tomrummet + bristen på bild, inte färgen. Behåll navy (#090b32); fyll den.
- **Mint-gradient-submit "Boka rådgivning"** — sajtens starkaste färgsignal; SKA förbli den enda handlings-gradienten per hjälte. Rör inte färgen; ta bort rivalerna.
- **Per-sida förifylld/låst service** — smart message-match; behåll logiken, ändra bara till chip.
- **Kicker→H2→paragraf-copyn i ampy-röst** — candour-ren, du-tilltalande; bland det bättre på sajten. Endast paragraflängd kapas, inte tonen.
- **Att ren `elektriker-i` saknar service-chip** — rätt (tjänsten obestämd); behåll skillnaden mot tjänste-bestämda geo-sidor.
- **Ring-numret 010-265 79 79 som permanent synlig konverteringsväg** — försvinner aldrig; ändras bara från lysande blå gradient till lugnare vikt (ghost) resp. dominant grön solid (eljour).
- **Den mörkgröna nödknappen med glow-prick + live-pillen + de 4 reassurance-bullets** (eljour) — sidans bästa element; görs till kanon, ändras inte.
- **Hero-1 (homepage/pillar)** — ägarens referens. Orört.

---

## 10. Build-checklista (Bricks)

- [ ] Sätt `hero_variant` via post-type-condition (S/G/E/Hero-1).
- [ ] Definiera de 4 knapp-primitiverna EN gång (mint / emergency-green / ring-ghost / link-quiet).
- [ ] HERO-S: split 50/50 desktop, bild-topp mobil, CTA href=`#kontakt`, ingen form, mikrotrust utan 5.0.
- [ ] HERO-G: split 45/55, 3-fälts SSR-formkort (teal-kant, skugga, AA-microtext), chip ej dropdown, kundtyp under fälten, bg-bild i döda kvadranten, EN mint-submit, trust-fot.
- [ ] HERO-E: single-col, live-pill upp, dominant emergency-green, 4 bullets, form→opt-in-länk, sticky call-bar + IntersectionObserver, eljour-header-pill=Ring.
- [ ] Alla: kicker versal-spärrad teal-solid; paragraf max 3 rader (G: 2); microtext `--ap-ink-on-navy` (AA); bild `fetchpriority=high`; SSR-skelett för formkort.
- [ ] Candour-grind: sök & ta bort oankrad "5.0" ur alla hjälte-rader; behåll endast ankrat betyg på EN plats.
- [ ] `[token-GAP]`: bekräfta exakta ap*-token-namn (radius/spacing/emerald-solid) mot design-system innan bygge.
