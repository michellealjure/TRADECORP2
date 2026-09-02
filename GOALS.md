# TradeCorp (TCORPI) — Goals & Open Corrections

> Claude reads this at the start of every session, before touching any file.
> Michelle edits freely — bullets, Spanish or English, half-sentences are fine.
> Source of truth for scope: `Resumen Inicial -  TRADECORP.docx` (brief, Apr 7).

---

## North star

**Make TCORPI look like a legit, serious, established company** — the brief says this
three separate ways ("empresa legit", "empresa ordenada", "que sienta que hay
coherencia"). Buyers arrive from a business card or a phone call and check whether this
is a real operation. The site has to answer *yes* in three seconds.

Second axis, from Michelle: it must have **real UI craft — awwwards-level depth**, not
"AI-generated template". Motion alone is not craft. The site currently *has* animation
and still reads generic; the problem is typography, spacing, hierarchy and restraint,
not more movement.

---

## The four standing goals

1. **Deliver what the brief asks for** (see "From the brief" below — much is unbuilt).
2. **Look genuinely professional.** Not "too AI". Profound UI essence, awwwards-tier.
3. **Follow the branding exactly** — colors, fonts, logo. **Never change the logo.**
   **Never change copy, data, contact details or product info without asking first.**
4. **Ship on `tcorpi.com`.** Michelle prefers embedding into Wix sections. See
   "Hosting" — measured, reopened, and blocking.

---

## Working on now

- [ ] _(nothing set — resolve "The Wix question" first, it changes everything else)_

---

## Hosting — REOPENED 2026-08-22, pending Michelle's call

Michelle first chose "host outside Wix", then reconsidered: she prefers embedding into
Wix sections, proposing **one section = the whole home page**, reasoning that the scroll
motion would then be unaffected.

**Measured in a real iframe harness (not assumed).** Two findings:

**1. A taller iframe never removes the inner scrollbar — it makes it worse.** The hero
track is `250vh`, so it grows with the iframe. Measured `content = 2.5 × iframeHeight + 2854`:

| iframe height | content height | overflow |
|---|---|---|
| 800px    | 4 600px  | 3 800px  |
| 3 434px  | 11 439px | 8 005px  |
| 10 000px | 27 854px | 17 854px |
| 20 000px | 52 854px | 32 854px |

For no inner scroll you'd need `2.5H + 2854 ≤ H`, i.e. a negative height. Impossible
while any layout is expressed in `vh`.

**2. Scrolling the Wix page does not advance the embed.** Parent scrolled to 2500px →
the embed's internal `scrollY` stayed `0`. Only scrolling *inside* the box moves it.

So "one section = whole home" does **not** preserve the scroll motion by itself: you get a
nested scrollbar, and the animation only runs while the cursor is inside the embed.

**It is still achievable in Wix, three ways — all with costs:**
- **Velo `postMessage`.** Velo reads the parent scroll and feeds progress to the iframe.
  `messageDriver` was already built for exactly this. Needs Wix Studio + dev mode +
  premium; polled scroll is less smooth than native; still an iframe (no SEO).
- **Full-screen embed, Wix header/footer hidden.** One 100vh iframe as the entire page;
  the inner scroll becomes the only scroll. Closest to a normal site, but iOS momentum
  scrolling and `position: sticky` inside iframes are historically buggy — and the brief
  says the audience is on **desktop *and* mobile**.
- **Autoplay instead of scroll.** What `src/hero/` already does. No scroll dependency,
  but the two-act scroll concept is lost.

**Cost that applies to every Wix-embed option:** iframe content is not indexed as the
page, so the SEO work stays off the table.

- [ ] **DECIDE.** Nothing else should be built until this is settled.

## From the brief — required, mostly NOT built yet

### Conversion
- [ ] **Primary CTA: "Request a free sample"** — a form capturing email + shipping
      address. This is *the* action the whole site exists to drive. **Not built.**
      Current pages only have `mailto:` links.
- [ ] **Secondary CTA:** email for more information about a specific product.
- [ ] The old site's **newsletter block failed** — do not rebuild one.

### The catalog (the brief's biggest functional ask)
- [ ] Group products **by category**; buyer must not scroll all categories to find one.
- [ ] **Easy search + filter.** *(Partly done — Portfolio page has 40 products with
      accent-insensitive search/filter.)*
- [ ] **Cross-selling is an explicit goal:** someone arriving for collagen should
      discover the magnesium range.
- [ ] Product names are unpronounceable and boring — presentation must carry them.
- [ ] **Technical sheet + Certificate of Analysis per product**, but *"tanta ficha
      técnica hace ruido"* — organised and progressive, not dumped on the page.
- [ ] **Star product: HYDROLIZED BOVINE COLLAGEN** needs visual protagonism.
      Others named: Alkalized cocoa powder, Creatine Monohydrate 200 mesh, Magnesium
      Citrate / Oxide / Bisglycinate, Eggwhite protein powder, L-Carnitine Base,
      L-Arginine, Polydextrose. Plus **custom blends**.
- [ ] **In-stock inventory** — "check inventory" surface.
- [ ] **Certificates** — grass-fed collagen.

### Positioning to communicate
- [ ] **"One stop point of supply"** — everything in stock.
- [ ] **No long lead times, no large minimum orders.** *(Partly in the Why cards.)*
- [ ] **Geography as the promise:** based in Florida/Miami + Georgia → physically closer
      → dispatches faster than competitors. The brief frames this as the main hook.
      *(There are two Google Maps on About — but the speed argument isn't made.)*
- [ ] **Owner-run, preferential personal treatment**, direct line to decision-makers.
- [ ] **Formulation advice** — they work closely with manufacturers and answer
      formulation questions. Currently absent.
- [ ] **Trusted partners: client LOGOS.** *(Only quotes exist today, no logos.)*

### Site-wide
- [ ] **English site with a Spanish option.** No i18n exists. Real scope — decide early,
      retrofitting a language toggle across four pages is expensive.
- [ ] Audience: **purchasing departments at nutraceutical laboratories.** Desktop + mobile.
- [ ] Domain `www.tcorpi.com`. Growth plan: +1 US state per year, portfolio grows with
      client demand.
- [ ] Competitors to beat: Originates Inc, AIDP, Custom Collagen.

### Reference sites named in the brief
- `javvycoffee.com`, `flavcity.com`, `shopflavcity.com` — macro→micro, dense topics made
  simple, strong infographics, "todo está muy bien explicado, los colores".
- `nutritionformulators.com` — for animation.

---

## Explicit corrections from the brief's final page

- [ ] **"Que la página tenga más café."** A page-level preference for more brown, with
      no specific target named. ⚠️ **CORRECTED 2026-08-22:** the preceding sentence in the
      brief — *"las tarjetas no van a tener ese verde, sino un café con verde"* — is about
      **tarjetas de presentación personal (printed business cards)**, NOT the website's
      Why cards. Claude misread this and built audit finding 03 on it. Do not treat the
      Why cards as having a café mandate.
- [ ] **Increase font size — visibility** was called out explicitly.
- [ ] **Social media icons in the corners.**
- [ ] **More animated video** across different sections.
- [ ] **Change the colors of the profile photos.**
- [ ] **New address**, and **delete the Colombian phone number.** ⚠️ Michelle must supply
      the new address — do not invent one.
- [ ] Coffee/cacao should feature — it's in the logo ("logo café, incorporar café").

---

## Design audit — measured 2026-08-22

Full report: https://claude.ai/code/artifact/d618a2ba-3db0-4311-941c-5607aff8abab
Measured in-browser at 1440px across all four pages (computed styles, not source).

| Page | Text sizes | In 12–20px | Spacing values | Verdict |
|---|---|---|---|---|
| Home | 15 | 8 | 19 | mush |
| Ingredients | 7 | 6 | 21 | mush |
| About | 7 | 4 | 13 | close |
| Contact | 5 | 2 | 11 | **good — the model** |

Fix in priority order. 01 and 04–06 are ONE change: a token block per page, then
replacing bespoke values with the variables. No layout, copy, colour or logo changes.

- [x] **01 DONE 2026-08-22 — type scale.** Home has 8 sizes between 13–20px, steps
      of 1.04–1.08×, below the threshold where a reader perceives rank. Cause: per-element
      bespoke `clamp()`. Fix: six sizes at 1.25× as variables (14/17/21/27/34/50), map
      everything onto them. Contact already does this — normalise toward it.
- [x] **02 DONE 2026-08-22 — easing.** This is the direct
      answer to "it has the motions but doesn't look pro". Found: `ease` at .15s/.18s/.34s;
      **zero** custom cubic-beziers. Fix: `--ease-out:cubic-bezier(.16,1,.3,1)` for
      entrances, a faster curve for hovers.
- [~] **03 DOWNGRADED 2026-08-22 — café is 0% of painted surface.** The *measurement*
      stands: home is crema 82.8% / oliva 16.1% / café 0.0% / salvia 0.0%, and café is
      text-only. But the *mandate* was wrong — "las tarjetas" means printed business
      cards, not the Why cards. Only the vague "más café" preference survives, so this is
      now Michelle's aesthetic call, not a brief requirement. Three options were
      previewed and rejected as premature; the page still has no dark anchor if she
      ever wants one.
- [x] **04 DONE 2026-08-25 — spacing is off-grid.** 21 distinct values on Ingredients (11, 13,
      23, 26, 33, 67, 82, 97px were on no scale). Fixed: every authored padding / margin / gap
      on all four pages now sits on a 4px grid. Policy applied: values ≤32px became fixed grid
      px (fluidity under 32px is imperceptible — the clamp range was 2–6px); values >32px stay
      fluid but both clamp endpoints were snapped. Off-grid authored values per page went
      Home 15 → 0, Ingredients 13 → 0, About 8 → 0, Contact 9 → 0.
- [x] **05 DONE 2026-08-22 (weights; leading partial) — small text.** Kanit Light 300 used 125× on
      Ingredients; 14px set at line-height **1.00**, 15/16px at 1.20, while 50px gets 1.10.
      The other half of the brief's "aumentar letra: visibilidad". Fix: body → weight 400,
      min 16px, line-height 1.6; reserve 300 for large text.
- [x] **06 DONE 2026-08-22 — optical tracking.** Only the 216px logo has any
      letter-spacing. Fix: -.02em above 32px, -.03em above 48px, +.1em on uppercase labels.
- [x] **07 DONE 2026-08-22 — contrast.** Hero subtitle "Premium raw materials, always in
      stock." is 4.38:1 at 22px/300 (AA needs 4.5). Fixing 05 resolves it.

## Audit fixes — applied 2026-08-22, verified in browser

Backup before editing: `_backups/docs-pre-audit-20260822-184515/`.
Scope honoured: **no block, content, wording or order changed** — execution only.

Measured after (all four pages, 1440px):

| Page | Sizes before → after | Scale ratios now | Default `ease` | Contrast fails |
|---|---|---|---|---|
| Home | 15 → **7** (6 + logo) | 1.21 1.24 1.29 1.26 1.47 | none | 0 |
| Ingredients | 7 → **4** | 1.21 1.24 2.38 | none | 0 |
| About | 7 → **6** | 1.21 1.24 1.29 1.26 1.47 | none | 0 |
| Contact | 5 → **5** | 1.21 1.24 1.29 1.85 | none | 0 |

Every page now shares one token block: six type sizes (14/17/21/27/34/50 at 1440),
three easing curves, two tracking values. Kanit Light 300 is gone from small text
(Ingredients went 125 uses → 0). The hero subtitle moved salvia → crema, fixing the
only contrast failure (4.38 → 6.97:1).

Known residue, deliberate:
- Ingredients still jumps 21 → 50px. Giving product names the 27px rung wraps the long
  botanical names ("Fenugreek (Trigonella foenum-graecum)", 321px box) to a third line
  and grows every card — rejected as a layout change.
- Line-height was normalised on Home; on the other three only weights were bumped.

Still open from the audit:
- [~] **03 — café as a surface.** Previewed (café card tops / café ground / café ground
      + green cards; all pass contrast). **Not applied** — the brief mandate turned out to
      be about printed business cards. Parked as an optional aesthetic call.
- [x] **04 — spacing off-grid.** DONE 2026-08-25, see the pass below.

## Bugs reported 2026-08-22 — all three fixed

Backup before this pass: `_backups/docs-pre-audit-20260822-184515/`.

**BUG 1 — intro replayed on scroll up. FIXED.**
The hero was scroll-*scrubbed* (`scrollDriver` mapped scroll position → progress
every frame), so scrolling up ran it backwards. It is now a **one-time 2.6s autoplay**
(`easeInOutCubic`), with **no scroll listener at all** — so replay is structurally
impossible, not just suppressed. `sessionStorage['tc_intro_done']` marks completion;
on a repeat visit `finish()` applies the final frame directly. `.track` went 250vh → 100vh
(the scroll travel only existed to drive the scrub) and `finish()` releases every
`will-change`. Verified: second load reports `html.intro-done`, zoom/mark opacity 0,
card/band opacity 1, `will-change:auto`, flag `"1"`.

**BUG 2 — values band invisible. FIXED.** Root cause was BUG 1: the band's opacity is
`seg(p,0.60,0.92)` off the *hero's* timeline, so any reverse scrub drove it back to 0.
Now the timeline ends at p=1 and stops. Separately, the Why reveals were decoupled from
the hero entirely — two `IntersectionObserver`s that `unobserve` on first hit (never
re-fold), plus a `tc:intro-done` event that re-checks positions after the track collapse
changes document height, plus a 6s safety net.

**Defensive rule now enforced: no content depends on JS to be visible.** The CSS default
*is* the final state. The start state exists only under `html.intro-armed`, added by a
tiny `<head>` script **before first paint** and only when the intro will really run —
so there is no flash on repeat visits, and a total JS failure renders the composed hero.
Verified by stripping every class and inline style: card 1, band 1, why-cards unclipped,
`.why` green. (`.why` and the curve path defaults were changed cream → green for exactly
this reason — cream cards on a cream ground would have been invisible.)

**BUG 3 — pixelated logo. FIXED on the third attempt.**
(a) inline **SVG** (`viewBox="33 33 3928 743"`), not a raster. (b) yes, it scaled **up**:
`MAX_SCALE=70`, `scale()` 1 → 71. Measured: `.zoom` laid out 520 CSS px, DPR 2 → a
**1,040-device-px texture stretched to 12,346** at p=0.189.

- **Attempt 1 — remove `will-change:transform`. FAILED.** `will-change` was not the cause;
  Chrome caps raster scale and stretches past the cap regardless.
- **Attempt 2 — wrap the SVG 8x larger and pre-scale it to 1/8. ALSO FAILED.** `.zoom` is
  the composited layer, so *everything inside it flattens into `.zoom`'s 520px texture*
  before the outer scale applies. Nesting cannot escape the parent's raster.
- **Attempt 3 — move the zoom inside the svg as a `<g transform="scale()">`. IMPROVED, still soft.** A scaled group still creates a scaled rendering context Chrome can raster-cache.
- **Attempt 4 — animate the `viewBox` (move the CAMERA, scale nothing). CURRENT.** `.zoom` spans the stage with **no CSS
  transform** and the logo group has **no transform either** — verified
  `getComputedStyle(.zoom).transform === "none"` and `#logoG` has no `transform` attribute.
  **Nothing is scaled anywhere.** Path coordinates never change; `applyFrame` only narrows
  the svg `viewBox` (8570 units → 722 at p=0.189), i.e. it moves the *camera*. Skia
  re-renders the visible region at native resolution each frame, so no scaled raster
  context exists that could be cached or stretched. This is the canonical way to do vector
  zoom and it cannot pixelate by construction.

**The rule to remember: ANY scale transform — CSS on a div, or an svg `<g transform>` —
creates a scaled rendering context the browser may rasterise once and stretch. Nesting,
`will-change` and bigger inner elements all fail. For a large vector zoom, scale NOTHING:
animate the `viewBox` so the camera moves instead.**

Verified after the rewrite: rest logo 660px centred at dx/dy 0; counter still dead centre
at p=0.55; rest viewBox `-2288 -2274 8570 5356` → mid-zoom `2406 198 722 451`; p=0 → zoom 1 / card 0 / band 0; p=1 → zoom 0 / card 1 / band 1 / mark 0;
counter fill morphs to `rgb(66,79,37)`; viewBox recomputes on resize; no console errors;
and a screenshot at mid-zoom shows clean anti-aliased curves. Rest width is now computed
in JS (`stageW<=720 ? 82% : min(54%,660px)`), replacing the old CSS width rules.

⚠️ **Sharpness is now confirmed by screenshot.** The 2.6s *playback* still is not — a
hidden preview pane suspends `requestAnimationFrame`, so frames were driven by hand via
`applyFrame()`. **The motion itself still needs eyes in a real browser.**

## Browser cache — why fixes can look like they "didn't apply"

Michelle reported the intro was "still autoplay, not linked to the scroll" AFTER the
ratchet shipped. The code was correct both on disk and **on the wire** (`curl` showed
`function scrollDriver` present, `function autoplay` absent). The cause was **caching**:
`python3 -m http.server` sends `Last-Modified` and **no `Cache-Control`**, so Chrome kept
serving the previous `index.html` without revalidating.

**Use `Tradecorp/serve.py` instead** — same thing but sends `Cache-Control: no-store`:
```
python3 serve.py            # docs/ on 8090
python3 serve.py 8091 src   # any port + folder
```
And when in doubt, hard-reload with **Cmd+Shift+R**. Before concluding a fix failed,
`curl` the served HTML and grep it — that distinguishes a bad fix from a stale cache.

## Intro timing — zoom slowed 2026-08-22

The zoom occupied only 24% of the scroll timeline (`seg(p,0.06,0.30)`). Stretched to 42%
(`0.06→0.48`), with the later phases shifted so the choreography order still holds.
Verified frame by frame at 1280x800 (travel 1200px):

| p | viewBox W | zoom | card | band |
|---|---|---|---|---|
| 0    | 7618 | 1 | 0    | 0 |
| 0.2  | 2120 | 1 | 0    | 0 |
| 0.4  | 200  | 1 | 0    | 0 |
| 0.48 | 107  | 1 | 0.27 | 0 |
| 0.55 | 107  | 0 | 0.90 | 0 |
| 0.85 | 107  | 0 | 1    | 0.57 |
| 1    | 107  | 0 | 1    | 1 |

New timings: zoom `0.06→0.48`, counter colour `0.08→0.34`, zoom fades `>0.52`,
card `0.45→0.56`, recuadro `0.58→0.88`, band `0.70→0.96`.
If it still feels fast, the second lever is `.track` height (250vh → 350vh) for more travel.

## Intro driver — changed to scroll-ratchet 2026-08-22

Michelle: *"in this preview is like a video, the motions are not linked to the scrolled."*
The BUG 1 fix had made it a 2.6s autoplay, which satisfies "runs once" but throws away the
two-acts-on-one-scroll concept. Offered three options; she chose **scroll-driven,
forward-only**.

`scrollDriver()` now maps scroll → progress but **ratchets**: `maxP` is only ever assigned
when `p > maxP`, `applyFrame(maxP)` is what renders, and at `maxP >= 1` `finish()` removes
the scroll listener entirely. So scrolling up holds the frame instead of rewinding, and
replay is impossible rather than suppressed. `.track` is back to **250vh** — but only under
`html.intro-armed`; a repeat visit gets `100vh` and no dead scroll.

**`intro-armed` is deliberately NOT removed by `finish()`** — it controls the track height,
and dropping it mid-scroll would shorten the document under the user's feet and jump the page.

**Real bug found while testing: a zero-height stage produced `viewBox="NaN NaN NaN NaN"`**
and erased the logo (reproduced in a 0px-tall pane; console showed the SVG attribute error).
`measure()` now returns false and bails when the stage is under 1px, `applyFrame` refuses to
write a non-finite viewBox, and `boot()` retries on rAF + a 400ms timeout. Verified clean
afterwards: fresh tab, no console output, finite viewBox, track 250vh.

⚠️ **The ratchet itself is NOT behaviourally verified** — the driver reads inside
`requestAnimationFrame`, which a hidden preview pane suspends, so scrolling could not be
exercised here. Frame math was verified by driving `applyFrame()` directly
(p=0 → viewBox 7618 wide, p≥0.3 → 107 wide, card/band 0→1). **Scrolling up must be tested
in a real browser.**

## Round 2 corrections 2026-08-22

- [x] **#1 Side margins too wide.** The page used three different gutters (6vw/88px on
      `.card-in`, `.band`, `.why`; 5vw on the nav). Replaced all with a single
      **`--pad-x: clamp(16px,3.4vw,56px)`** so every section aligns, and raised
      `.why-inner` max-width 1100 → 1240 to use the reclaimed space.
- [x] **#3a Ingredient gap too wide.** `.ing` margin-right `clamp(24px,3.2vw,56px)` →
      `clamp(10px,1.2vw,20px)`.
- [x] **#3b Ingredients in the O frame.** From Michelle's `O ingredients.svg`. `.ing`
      aspect-ratio set to **704.681/507.72** so the frame can never distort; the photo is
      clipped with an `objectBoundingBox` `<clipPath id="oClip">` (path scaled by
      1/704.681, 1/507.72 so no coordinates had to be rewritten); the ring is a
      `.ing-frame` overlay using a data-URI SVG, fading in with the photo. Ring recoloured
      from her file's `#495430` to brand **oliva `#424f25`**. Explore button untouched.
- [x] **#4 Why motion not working — MY BUG.** The Why script had a blanket
      `setTimeout(reveal, 6000)` "safety net" that fired on a timer regardless of scroll
      position. Proven: section 2381px BELOW the viewport already had `is-in` on all cards
      and a green background. Replaced with a **visibility-gated** poll that only reveals
      when the section is actually on screen and still folded, and stops once revealed.
- [x] **#2 Values — option B chosen**, plus "needs more protagonism". Applied editorial
      treatment to `.band`: headings **`--t-md` → `--t-lg`** and recoloured cafe → oliva,
      descriptions dropped to `--t-sm` cafe/78% (so the hierarchy inverts — heading now
      dominates), hairline `border-left` dividers with generous inner padding, vertical
      padding roughly doubled. Band height 182px. **"Direct & personal" wraps to two lines
      and was knocking the other descriptions out of line** — fixed with CSS `subgrid`
      (`grid-template-rows:subgrid` on each cell) so all headings share one row and all
      descriptions the next; `@supports not` fallback reserves 2.16em. Verified: heading
      tops all 795, description tops all 870.
- [x] **#3 Explore now lives on the photo state too.** `<a class="ing-explore">` was moved
      OUT of `.ing-info` to be a direct child of `.ing`, absolutely positioned at
      `bottom:9%`, so it survives the cross-fade and sits on the O-framed photo.
      `.ing-info` inset bottom 22% to clear it. Gap tightened again
      `clamp(10px,1.2vw,20px)` → **`clamp(4px,0.5vw,10px)`** (6.4px at 1280).
- [x] **#5 Trusted partners — option B chosen.** All **16** cards (8 + 8 aria-hidden dups)
      rebuilt: `.tp-quote-by` moved ABOVE the quote and became a flex header with a 40px
      olive `.tp-avatar` circle carrying the person's initial, name in Poppins cafe, role
      in AvenirLight 13px. Card went crema → **white with a 1px rgba(56,41,21,.10) border**,
      radius 14, more padding.
      ⚠️ **Marquee seam re-verified after the width change** — offset-to-duplicate 2921 ==
      half-track 2921. The load-bearing margin maths still holds.

`docs/_proposals.html` deleted after the picks.

## Round 3 corrections 2026-08-22

- [x] **Margins — I overshot.** Gutter had gone 6vw/88px → 3.4vw/56px (44px at 1280) and
      content read as flush to the edges. Now **`--pad-x: clamp(20px,4.6vw,76px)`** = 59px
      at 1280, between the original and my over-correction.
- [x] **"Everything is too big" — type scale dialled back one step.** At 1280 the scale
      went **14/17/21/27/34/50 → 12/13/16/20/26/39**. (Note this partly walks back the
      brief's "aumentar letra: visibilidad" — if small text now reads too light, raise
      `--t-sm` alone rather than the whole scale.)
- [x] **Explore drifted away from the copy.** Pinning it at `bottom:9%` put it ~100px below
      the features. Reverted: it lives inside `.ing-info` again, `margin-top` under the
      features (**21px gap**). To keep it visible on the photo, the cross-fade now targets
      **`.ing-name` + `.ing-feat` only** — `.ing-info` itself no longer fades, so Explore
      never moves and never disappears. (Michelle: position may differ between states.)
- [x] **Why curve was covering the carousel.** `.why-curve` sits at `bottom:100%`, i.e. in
      the 90px directly above the section — which is the bottom of the ingredients. Height
      **90 → 56px**, `pointer-events:none`, and `.ingredients` bottom padding
      `clamp(56px,9vh,120px)` → **`clamp(96px,11vh,140px)`** (99px at 1280) so the curve
      always clears real content.
- [x] **Why motion.** The IO *is* firing (verified: cards get `is-in`, bg goes green). What
      could not be seen is the CSS transition — **a hidden preview pane freezes CSS
      transitions**, so `curve.style.transform` read `translateY(0px)` inline while
      computed stayed at the 100px start. Made the reveal more deliberate anyway: card IO
      `threshold .15 → .25`, `rootMargin -12% → -22%`, stagger `110ms → 170ms`, and the
      safety guard now needs **two consecutive sightings (~4s)** so it can never pre-empt
      the staggered unfold.
- [x] **Avatar was above the name, not beside it.** Two `.tp-quote-by` rules matched and the
      ORIGINAL (`flex-direction:column`) came later in the sheet and won over my new one.
      Fixed at the source rule → `row` + `align-items:center`. Verified computed
      `flexDirection:"row"`, avatar right edge 163 < name left 175, same row.

**Lesson:** when restyling an existing class, check for a competing rule later in the
stylesheet — adding a new rule earlier silently loses. Enumerate `document.styleSheets`
for the selector rather than assuming the new rule wins.

## Round 4 corrections 2026-08-22

- [x] **Why motion "still not working" — ROOT CAUSE FOUND.** The Why reveal was gated on
      `html.intro-armed`, which is the **HERO's once-per-session flag**. After the first
      load in a session `tc_intro_done` is set, `intro-armed` is never added, so the Why
      section's start state and its `transition` rule never applied and the script called
      `reveal()` immediately. **Every reload after the first showed a pre-revealed section
      with no animation** — exactly what Michelle kept seeing while reviewing.
      Proven: repeat visit with the section 1551px off-screen already had
      `clip-path:none` and `transitionProperty:"all"`.
      **Fix: fully decoupled.** The Why script no longer reads `intro-armed`; it adds its
      own **`.why-armed`** class to the section, gated only by `prefers-reduced-motion` +
      IO support, so the scroll reveal runs on EVERY visit. CSS moved
      `html.intro-armed .why-card…` → `.why.why-armed .why-card…`.
      Verified on a repeat visit: `whyArmed:true`, cards start `inset(0 0 100%)`,
      `transitionProperty:"clip-path"`, and they flip to `is-in` on scroll.
- [x] **Ingredients still too big / gap too wide — the artboard was the problem.**
      Measured the ring path's real bbox: **`97.18 0 510.33 507.72`** inside a
      704.681-wide canvas, i.e. **27.6% of every item was empty side padding** that read as
      gap. Retargeted the clip (`scale(0.00195949 0.00196959) translate(-97.18 0)`) and the
      ring's data-URI viewBox to those bounds, set `.ing` aspect-ratio to **510.33/507.72**
      (essentially square) and width `clamp(300px,32vw,460px)` → **`clamp(190px,19vw,266px)`**.
      Result at 1280: item **410x295 → 243x242**, pitch between items **451px → 250px** (-45%).
- [x] **Explore framed on the photo state.** `.ing-explore` is now a pill: `7px 16px`,
      `border-radius:999px`, with a **transparent 1.5px border and transparent background
      reserved at rest** so the pill appearing on hover cannot shift the layout. On
      hover/focus it becomes `border-color:var(--oliva)` + `background:var(--crema)` and
      drops the underline.

**Lesson (second time this bit):** do not reuse one feature's state flag to gate another
feature's animation. The hero intro is once-per-session; a scroll reveal is every-visit.

## Round 5 corrections 2026-08-22

- [x] **Hero margins now match Why / Trusted partners.** Why had `--pad-x` PLUS
      `.why-inner{max-width:1240px;margin:0 auto}`; the hero only had `--pad-x`, so on wide
      screens the hero ran wider. Added **`--content-max:1240px`** and gave `.card-in` and
      `.band` `max-width:calc(var(--content-max) + var(--pad-x)*2);margin:0 auto`.
      Verified at 1280: hero copy, band first cell and `.why-inner` all start at **x=59**.
- [x] **Ingredient gap opened slightly** — `clamp(4px,0.5vw,10px)` → `clamp(12px,1.3vw,22px)`
      (7px → 16.6px at 1280).
- [x] **Why reveal strengthened.** Proved the mechanism is sound: the browser creates a
      running `CSSTransition` for `clip-path` with keyframes
      `inset(0 0 100% round 24px)` → `inset(0 round 24px)`, and `.finish()` lands on the
      revealed value. So the logic works — it was just hard to PERCEIVE (a clip unfold on a
      flat-coloured card top). Added **`opacity 0→1` and `translateY(26px)→0`** alongside
      the unfold, lengthened the section colour + curve to 1.1s, stagger 170→200ms.
- [ ] **Ingredient text-state frame** — 5 options at `docs/_frames.html` (A O outline in
      salvia / B soft filled O 20% / C hairline O / D subtle rounded card / E none).
      Awaiting Michelle's pick. **Delete `_frames.html` before committing.**

**CSS gotcha worth remembering:** *percentage padding resolves against the containing
block's width, not the element's own.* In the frame preview `padding:0 17%` on a flex item
became 198px (17% of the 1168px row) and blew a 243px box out to 397px with zero content
width. The real page is unaffected because `.ing-info` is `position:absolute;inset:0`, so
its `8%` resolves against the 243px item. Use px/em for padding inside fixed-size boxes.

## Round 6 corrections 2026-08-22

- [x] **Margins confirmed good by Michelle.**
- [x] **"Boxes are no longer there" — regression I caused.** Round 5 added `opacity:0` to
      the card start state, so any card the reveal never reached became *invisible* rather
      than merely un-animated. Her report gave the discriminator: **green worked, boxes did
      not** → the section IntersectionObserver fired, the card one did not.
      **Rebuilt without IntersectionObserver.** The card reveal is now a plain scroll +
      rAF read (what this page used originally), with three safety properties:
      1. only cards **below the fold at init** get `.why-pending` (the hidden state);
         anything already on screen starts revealed, so nothing can be stranded;
      2. the hidden state is scoped to `.why-pending`, never to every `.why-card`;
      3. an 8s fallback calls `showAll()` if anything is still hidden while the section is
         on screen. Worst case is a delay, never permanent invisibility.
      Verified end state: `applyWhyFrame(1)` → all cards opacity 1, `inset(0px round 24px)`,
      `transform:none`, section green, curve `translateY(0)`.
- [x] **Cocoa text "too far left" — measured, it is NOT off-centre.** Every card, in both
      the preview and the real page, measures **0px from the box centre** for name,
      features and Explore. The O is centred too: bbox centre and *area centroid* (canvas
      pixel measurement) are both within 0.4px of the box centre. What is actually wrong is
      that "Alkalized Cocoa Powder" **wraps to 2 lines with a short second line**, which
      reads as unbalanced. Added `text-wrap:balance` to `.ing-name` and widened the copy
      area (`.ing-info` padding 8% → 6%).
- [x] **Frame option B chosen — soft filled O at 20%.** Implemented as `.ing::before`
      (no DOM changes): the inner O path as a salvia data-URI at `opacity:.20`, fading out
      with the name and features so the hover state stays photo-in-solid-olive-O.
- [x] **"Cocoa text too far left" — real, and now explained.** It is NOT a centring bug:
      every element measures 0px from the box centre. **The O is a tilted leaf.** Measured
      by canvas pixel centroid per horizontal band: the blob's mass sits **+8.4px RIGHT of
      centre at the name's height** and **-11.1px LEFT at Explore's height**. Box-centred
      text therefore reads left under the name — which is the element the eye goes to.
      Three fixes together: (1) `.ing-info` nudged `translateX(1.6%)` = 3.9px right, onto
      the blob's local centre at the name; (2) tighter margins; (3) `.ing-name`
      `--t-md → --t-base`, which stops "Alkalized Cocoa Powder" wrapping — text block span
      went **23.8-76.2% → 29.5-70.5%**, so less of it sits in the leaning parts.
      (Only "Hydrolyzed Bovine Collagen" still wraps to 2 lines.)
      A red centre-guide overlay was what finally made this visible — measurements alone
      said "centred" because the box was centred; the *shape inside it* was not.

**Testing limitation to remember:** in a hidden preview pane `requestAnimationFrame` is
suspended AND CSS transitions freeze, so `getComputedStyle` returns the *pre-transition*
value. Class lists and inline styles are trustworthy there; computed styles are not. To
read the true cascade target, set `el.style.transition='none'` first.

## Round 7 corrections 2026-08-22

- [x] **Title nudged further right.** Measured the blob's *extent* (not centroid) at the
      title band 29-38%: it runs x 43..488 of 511, midpoint **+1.96%** of the box. For a
      WIDE title the extent midpoint is the right target, not the centroid. `.ing-name`
      got its own `translateX(1.0%)` on top of the block's 1.6%, landing the title at
      **2.48%** — gaps to the blob edge now 0.06% left / 0.98% right, balanced.
- [x] **Why cards unfolded before you could see them.** The trigger was
      `card.top < vh*0.82` — a card began its 0.9s unfold when only its top ~160px was on
      screen, so it was finished before it was comfortably in view. Moved to
      **`vh*0.58`** (both the init arming threshold and the scroll trigger, kept identical
      so nothing can arm and then instantly fire). Section colour trigger `0.85 → 0.75`.
      At 900px viewport a card now unfolds once its top passes **522px**, i.e. while it
      occupies the middle of the screen.
- **"Only works once" is by design** — a scroll reveal that re-ran every time you passed it
      would be the hero-replay complaint all over again. Reload to see it again.

## Round 8 — Why motion restored from the backup 2026-08-22

Michelle: *"the motion worked in the other chat."* That was the decisive clue — a working
version existed. Diffed `_backups/docs-pre-audit-20260822-184515/docs/index.html` against
the current file and the difference was **fundamental, not a tuning problem**:

| | Original (worked) | Mine (felt broken) |
|---|---|---|
| Mechanism | **scroll SCRUB** — every frame recomputes `clipPath` inline and interpolates the colour | IntersectionObserver + fixed 0.9s CSS transition |
| Feel | unfold follows the scroll wheel, user-controlled | fires once at a threshold, over before you look |
| Colour | `mix(p)` interpolated continuously | snapped green with a transition |

**Restored the original scrubbed implementation verbatim** (`maxCardP` ratchet, `start=vh*.92`,
`end=vh*.45`, `i*70` stagger) plus one addition: it listens for `tc:intro-done` so it
re-reads after the hero track collapses. Removed every CSS rule I had added that fights a
scrub — `.why-armed` / `.why-pending` / `.is-in` states and the `transition` declarations on
`.why-card`, `.why` and `.why-curve`. Verified: all three transition-durations are now **0s**,
and `applyWhyFrame` steps through real intermediate colours
(cream → 217,219,190 → 200,210,171 → 183,200,152 → green) with the curve sliding 100→0.

**The lesson, and it cost several rounds:** I replaced a working scroll-scrubbed animation
with a threshold-triggered one while "fixing" something else, then spent four rounds tuning
thresholds on the wrong mechanism. **When the user says something used to work, diff the
backup before theorising.**

## Round 9 — logo flash on navigation, fixed 2026-08-22

Michelle: *"when I click the link there is a really fast glitch of the logo showing and
disappearing."* Three things lined up:

1. `history.scrollRestoration` is **"auto"**, so a back-navigation restores the previous
   scroll position — often past the hero.
2. `html.intro-armed .zoom{opacity:1}` **revealed the logo from CSS**, i.e. at first paint,
   *before any JS had decided which frame we were on*.
3. `boot()` waited for `document.fonts.ready` — several frames after that first paint.

So the logo was painted at full opacity, then JS ran, found progress ≈ 1 and snapped it
away. Exactly the reported flash.

**Three fixes:**
- **CSS no longer reveals `.zoom` / `.mark` at all.** `applyFrame()` sets their opacity, so
  they cannot appear before the frame is known. (Safe: the CSS default is the *composed*
  hero, so a JS failure still renders correctly — the logo simply stays hidden.)
- **`boot()` skips the intro when the page loads already scrolled past the hero**
  (`(-track.top)/travel >= 1` → `finish()` immediately).
- **`boot()` now runs immediately** instead of waiting on `document.fonts.ready`; fonts.ready
  only triggers a re-`measure()` afterwards. Waiting had left the stage blank for frames.

Verified: fresh load at top → `intro-armed`, track 2250px, `zoom` opacity 1 **set by JS**
(`zoom.style.opacity !== ''`), card 0. Progress probe: scroll 1400 → p 0.99 (intro still
runs), scroll 2200 → p 1.58 → `wouldSkipIntro: true`. No console errors.

## About / "Who we are" — 2026-08-22 (preview deleted after picks)

Michelle's three complaints: the pillar icons look "too icon AI", the video needs more
protagonism, and the two Google Maps contribute nothing (the intent is only "we have
warehouses in Miami and Atlanta").

**Item 1 — pillars.** Current = three generic line-art SVGs (star-medal, shield-check,
speedometer) — the stock set that reads as AI. Options: **A** typographic with hairline
rules · **B** marked with the brand O (consistent with the ingredient cards she chose) ·
**C** numbered 01/02/03.

**Item 2 — video.** Currently ~4:5 in the right column with two maps competing under it.
Options: **A** full-width 21:9 cinematic band under the copy · **B** keep two columns but
give the video the whole column at 16:9.

**Item 3 — maps.** Two `maps.google.com` iframes at `z=10` showing highways, not
warehouses, plus Google's own styling. Options: **A** two location cards that also say WHY
each site matters · **B** a route motif (two pins, dashed arc, claim line) · **C** a single
typographic line.

⚠️ **The descriptive sub-lines in every option are DRAFT COPY I wrote, not approved.**
The live pillars have labels only; the location text is my paraphrase of the brief's
*"en Florida no hay lidtimes"* and *"Georgia es el estado más hacia el sur… despachar más
rápido que nuestros competidores"*. Michelle must approve or replace the wording before any
of it ships — per the standing rule, never change or invent copy without asking.

**DECIDED + SHIPPED:**
- **Pillars → option A** (typographic, hairline-ruled). The three line-art SVGs
  (star-medal / shield-check / speedometer) are gone. Label `--t-sm → --t-md`, olive,
  left-aligned under a 2px rule. **Motion added for protagonism:** the rule *draws in*
  via `::before` `scaleX(0)→1` over .85s, with the label fading and rising, staggered
  0.05 / 0.20 / 0.35s off the existing `.who-pillars.in-view` trigger. Verified rest
  `matrix(0,0,0,1,0,0)` → revealed `matrix(1,0,0,1,0,0)`.
  **No descriptive sub-lines were added** — that copy was mine and unapproved, so the
  pillars stay label-only.
- **Maps → option C.** Both `maps.google.com` iframes deleted (0 iframes on the page).
  Replaced with a 2px olive rule, a pin + city for each site, and Michelle's exact
  wording: *"Two US warehouses, so stock ships from whichever sits closer."*
- **Video — still undecided.** Michelle: *"I don't know because the number of the
  warehouse before 10 looks weird"* (that was option A of item 3, the "Warehouse 01/02"
  labels — which option C doesn't use). Needs a clean A/B on the video alone.

**Trap hit:** the About page still carried **orphaned `.who-loc` rules** from an earlier
version — no markup used them, but `.who-loc svg{width:24px}` matched the new pins and
beat `.pin-ico` on specificity, forcing them to 24px. Removed all three dead rules.
*Before reusing a class name on an existing page, grep the stylesheet for it.*

**Video — resolved 2026-08-22.** Michelle's note was never about size: *"the warehouse
numbers look ia, there is 7,8,9,10, a weird number, and 12."* Blown up to 1240px the clip
shows **two AI tells**: a malformed dock number between 10 and 12, and a
**"KlingAI 3.0 Omni" watermark bottom-right** — the source footage is AI-generated. The
shipped `scale(1.16)` crop happened to clip the watermark by a hair, but it is in the file
and would reappear at any other framing (Wix embed, social, or if the transform is reset).
Re-framed to **`scale(1.52) translate(17.5%,4%)`**: crops from the RIGHT, dropping the
garbled number and the "12" while keeping doors 07-10 (all legible) plus the full truck
and cab. Verified across the pan at t=0.1 / 2.2 / 4.6 — the camera moves, so one frame is
not enough. Cost: effective resolution drops to **1.74x** the display width (was ~2x), so
slightly softer on Retina. A CSS comment records why the framing is what it is.
**Real footage remains the proper fix** — even a phone clip at a real dock. Flagged to
Michelle: a hero video carrying a generator watermark works directly against the brief's
core goal of looking like a legit company.

**Locations "still unnoticed" — fixed.** The cities were **19px, byte-identical to body
copy**, so they read as a caption. Promoted to **24px**, the same tier as the pillar
labels, so they register as a feature of the section rather than a footnote; pin 16 → 20px
with a heavier stroke, and more air above the rule. Hierarchy now
44 (title) / 30 (phrase) / **24 (pillars = cities)** / 19 (body) / 15 (note).

**Location pins red + names centred (2026-08-22).** Cities and the note are now centred on
the video frame — verified the city group's centre sits **0px** from the video's centre.
⚠️ **`--pin-red:#b0392a` is a NEW colour and is NOT in the brand manual** (café / oliva /
salvia / crema). Michelle asked for red pins directly; a warm brick red was used rather
than a primary red so it still sits with the palette, and it is scoped to a token used
only by `.pin-ico` so it cannot leak. The pins are `aria-hidden`, i.e. decorative, so the
3.46:1 against the ground is not a WCAG failure — but if red spreads to any *text*, it
would need to reach 4.5:1. Flagged to Michelle; easy to revert to oliva or shift toward
café if the brand owner objects.

**Video + locations — 5 layouts offered 2026-08-22, awaiting pick.**
Michelle: *"too rigid / corporate ppt."* Diagnosis: the current block is symmetrical on
every axis — rounded rectangle, full-width hairline rule, centred pair, centred caption.
Symmetry plus a rule is exactly the slide-deck signature. All five alternatives break at
least one of those. Preview `docs/about/_layouts.html` — **delete before committing.**
- **A · Lower third on the footage** — cities sit ON the video over a gradient scrim, no
  rule, no separate block. Documentary feel.
- **B · Card overlapping the frame** — cream card breaks the video's bottom-left corner.
  Editorial; kills the stacked-boxes rhythm.
- **C · Rail beside the frame** — video narrower, cities stacked to its right against a
  sage vertical rule. Asymmetric.
- **D · One typographic line** — "Shipping from ⦿Miami, FL and ⦿Atlanta, GA." Pins inline
  in running text. ⚠️ needs 4 new words ("Shipping from … and") — copy approval required.
- **E · Locations in the margin** — narrow left margin column, video shifted right.

**Layout A shipped, bigger (2026-08-22).** Cities now sit ON the footage over a bottom
gradient scrim; the separate ruled block is gone entirely. "Bigger" applied three ways:
video aspect **16/9 → 4/3**, grid columns **1.05fr .95fr → .86fr 1.14fr** (media column
now 575px vs 433px for the copy), and city labels **24px → 30px**. White text on the scrim
measures **16.58:1**. Pin uses `--pin-red-on-dark:#ff6a4d` — the brick red was too dark
against the scrim. Note sits below the frame. Re-verified the AI artefacts stay cropped at
the NEW 4/3 aspect (changing the aspect changes what `object-fit:cover` shows): doors
07-10 clean, no garbled number, no watermark.

⚠️ **Editing incident:** I corrupted this file mid-edit. `end = src.index('</div>',
src.index('who-locs-note'))` matched the **CSS rule name** rather than the markup, so
`end < start` and `src[:start] + new + src[end:]` **duplicated a 1,516-char region**,
leaving two `<figure>` opens and two `</nav>`. Repaired by splitting on the inserted block
and finding the longest suffix-of-A that prefixed B. **Rule: never slice a document by two
independently-searched indices — assert `start < end` first, or match the whole block
text.** The safe redo replaced the entire `<figure>…</figure>` by exact text.

## Michelle's own corrections

- [x] **2026-08-22 — "I don't like the blurred of the trusted partners."** Removed. It was
      a `mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent)` edge
      fade on `.tp-marquee` that dissolved the quote cards into the background at both
      sides. Cards now have clean hard edges. (The `mask-image:none` left in the
      reduced-motion block is now a harmless no-op.)

<!-- Add anything, however vague. Vague is fine — Claude asks before redesigning. -->

- [ ] Site has the motion but **still doesn't look pro**. Diagnose properly before
      adding anything: typography scale, spacing rhythm, hierarchy, restraint.

---

## Explicitly decided — do not re-litigate

- **Never change the logo.** Always the SVG, never re-typeset.
- **Never change copy, product data or contact info without asking.**
- Brand colors and fonts are fixed (Poppins / Kanit / AvenirLight; oliva, salvia, crema,
  café). *Rebalancing* toward café is wanted; *new* colors are not.
- No build step, no framework — vanilla, self-contained HTML.
- Brand tokens stay at the brief's values (`#424f25` / `#a6bf85` / `#eae4d1`).

---

## Known open items (technical debt — confirm or delete)

- [ ] **Sales email is a placeholder** — `sales@tcorpi.com` in the SSW pop-up is invented.
- [ ] **Logo out of sync** — `docs/` has the tidied master SVG; both `src/` versions
      still carry the old inline one.
- [ ] **Wix `messageDriver` never verified live** — back in play if a Wix option wins.
- [ ] **Ingredients carousel** reads airy/empty at rest; names wrap to ~3 lines.
- [ ] **Sections exist in only one place** — Ingredients / Why / Trusted Partners are in
      `hero-portal` but not in the standalone hero. Likely resolves itself when the
      `src/` vs `docs/` split is retired.
- [ ] **Uncommitted git work** — the logo refresh across all four `docs/` pages.

---

## Done

- [x] 2026-08-22 — Project `CLAUDE.md`, `GOALS.md`, preview-server config.
- [x] 2026-08-22 — Measured Wix-iframe behaviour in a real harness (see Hosting).
- [x] 2026-08-22 — Design audit across all four pages (7 findings).
- [x] 2026-08-22 — Applied audit findings 01, 02, 05, 06, 07 to all four pages.
- [x] 2026-08-25 — Applied audit finding 04 (4px spacing grid) to all four pages.
- [x] 2026-08-22 — Removed the trusted-partners edge fade.
- [x] 2026-08-22 — Fixed 3 reported bugs: intro replay, invisible values band, pixelated logo.
- [x] 2026-08-22 — Intro driver switched autoplay → scroll-ratchet; guarded zero-height stage.


## Audit finding 04 — 4px spacing grid, applied 2026-08-25

Backup: `_backups/docs-pre-grid-20260825-091046/`.

**Policy.** Authored spacing ≤32px → fixed px on a 4/8/12/16/20/24/28/32 ladder (the clamp
range under 32px was only 2–6px wide, so nothing visibly moved). Spacing >32px → still fluid
`clamp()`, but both endpoints snapped to the grid. Rounding was to nearest, ties up, so no
single value shifted more than 2px. Not touched: `--pad-x` (the page gutter Michelle tuned by
eye, already on grid), the optical `translateX(1.6% / 1.0%)` nudges inside the O frame, font
sizes, and `translateY(14px)` reveal offsets (motion distance, not layout).

**Result.** Authored off-grid values: Home 15 → 0, Ingredients 13 → 0, About 8 → 0,
Contact 9 → 0. One dead rule deleted (`.who-locs{gap:14px}` in About — no such element since
the maps were removed).

**Marquee safety — the load-bearing worry turned out not to be one.** Both carousels animate
`translateX(0) → translateX(-50%)` over a track holding the item list twice, so *any* uniform
`margin-right` stays seamless; the gap is not load-bearing. Verified in-browser rather than
assumed: for both tracks, `children[n/2].offsetLeft - children[0].offsetLeft` equals
`track.offsetWidth / 2` to within 0.6px. (`.tp-quote` also carries `margin-left:40px` for the
avatar overhang — easy to miss when checking by hand.)

**Deliberate residue.** Computed values at any one viewport are still fractional for the large
fluid clamps (e.g. `11vh` = 99px at 900px tall). That is responsive rhythm, not mush — the
finding was about small spacing having no ladder, and that ladder now exists. Do not "fix" it
by hard-coding section padding.

**Verified 2026-08-25** at 1440x900 and 375px on all four pages: 0 console errors, no
horizontal overflow, Contact cards still equal height (593/593), both marquees seamless,
search icon clearance preserved (icon `left:16px` + `padding-left:44px`).


## Hero — la O del logo con video, aplicado 2026-08-26

Backup: `_backups/docs-pre-hero-o-20260826-140456/`.

Reemplaza el círculo con `sphere.mp4`. Dos formas del SVG de marca
(`Brand/svg/logo-trade-corp video Hero frame.svg`, paths `Opacidad_O` y `Opacidad_o`)
dibujadas en un mismo canvas: la O grande lleva el video con zoom 2.00x y velo negro
23%; la o interior el mismo video a 0.70x con velo 44%. Encima, el grupo `Logo` del
SVG tal cual, con su filtro `drop-shadow-2`. El 44% no es el `.28` del archivo: en el
SVG las dos capas se superponen y el negro real es `1-(1-.23)(1-.28) = 44.6%`.

**Geometría.** El alto de la O = alto del verde visible = `min(alto de pantalla,
lo que cabe al lado del texto, 480px)`. El sobrante recorta el verde por abajo
(`--extra`), la banda sube con él, y `applyFrame` suma ese `ext` al clip-path para que
la intro aterrice en la misma geometría. Borde derecho de la O sobre el gutter del
contenido. Verificado a 1440x900: verde 480 = O 480, ambos márgenes alineados.

**Secuencia** (`SEQ`): aceite 1ª parte -> aceite 2ª parte -> cuchara -> ámbar -> cacao.
Cruces de 1.2 s. Reglas que costaron encontrar:

- El rebobinado se lleva **por reproductor**, no por posición: el aceite ocupa dos
  posiciones seguidas y no debe rebobinar entre ellas.
- Rebobinar al **entrar**, incluida la pre-carga de 0.8 s. Sin eso el clip asomaba por
  su último cuadro durante el cruce y después saltaba al principio — el "corte raro".
- `TAIL` de 0.2 s: ningún clip llega a su último cuadro, o el loop salta a la vista.
- `endAt` recorta un tramo inservible (la cuchara se voltea a los 4.3 s). El corte lo
  hace el tiempo; la pausa es red de seguridad con margen, porque congelar a la vista
  en mitad de un cruce se nota.

**Assets** (`docs/assets/hero-*.mp4`, 8.3 MB): oil 2.4, scoop 2.5, amber 1.1, cocoa 2.3.
El de la cuchara llegó en ProRes de 60 MB y se convirtió con `avconvert`, recortado en
origen a 4.4 s para no publicar los cuadros del giro. Solo el primero precarga completo.

**Pendiente / conocido.** Los clips son 1280x720 y se agrandan ~2.7x sobre el canvas;
lo ideal serían 2288 px de ancho. `.media{display:none}` en <=900px es **previo**: el
hero nunca mostró imagen en teléfonos, así que la O tampoco se ve ahí.


## Móvil — pendiente, acordado 2026-08-26

Michelle: **"después de acabar todo arreglamos lo móvil"**. No tocar hasta terminar
escritorio. Lo detectado hasta ahora, todo verificado contra
`_backups/docs-pre-hero-o-20260826-140456/` como **previo**, no introducido por el
trabajo del hero:

- **La banda va apretada.** Las dos filas de *Always in stock…* casi se tocan: la
  descripción de la primera queda pegada al título de la segunda. Posiciones idénticas
  al backup (622..723 y 723..824 a 375px), así que es de antes.
- **El hero no muestra imagen.** `.media{display:none}` en <=920px es previo: nunca se
  vio la esfera y ahora tampoco se ve la O. Ahora que la O es el centro del hero,
  vale replantearlo.
- **Ya arreglado en esta pasada:** al texto del hero le faltaban 18px por la izquierda
  (el recorte de la tarjeta entra 38px y el gutter era 20). El recorte baja a 16px en
  <=920px y el texto arranca en 32px.

## Hero — tipografía y encuadre, 2026-08-26

Medido antes de tocar: el eyebrow estaba a **29px peso 700** contra un titular de
**44px peso 400** — el 66% del tamaño y más grueso. El titular no era chico; el eyebrow
se lo comía. Ahora:

- eyebrow 14px versalita `.18em` **dentro de una cápsula** (crema 9%, borde 22%), ratio 0.27
- titular `clamp(32px,3.6vw,52px)` — fluido para que nunca caiga en tres líneas
- columna a **650px**: el titular mide 634 y el subtítulo 547, así que 680 sólo agrandaba
  el hueco del centro. El hueco visual bajó de **104px a 48px**.
- `--content-max` 1240 → **1180**: márgenes de 100 a 130px a 1440
- `.card-in` alineado a `flex-end` + `padding-bottom`: el bloque pesa abajo, no centrado
  (referencia de NFI que mandó Michelle)
- padding de las columnas de la banda 32 → 24px: con 1180 *"Direct & personal"* se partía
  por 5px

**Trampa encontrada:** el gap entre columnas estaba duplicado — 32px en el motor de la O
y `clamp(24px,4vw,72px)` = 57.6px en el CSS. Al no coincidir, la columna quedaba 26px
corta y el titular se partía en tres. Ahora `lensLayout()` **lee el gap real del DOM**;
no volver a hardcodearlo en dos lados.

## Ingredientes — rediseño de la sección, 2026-08-27
Pedido de Michelle (5 puntos) + su SVG `Ingredient frame.svg` y la lámina
`Ingredients.png` (5 recortes con alfa, 1536x1024). Backup previo en
`_backups/docs-pre-ing-20260827/`.

1. **Título que crece.** `.ing-title` lleva `scale(var(--tsc,1))`; el JS escribe
   `--tsc` de 0.74 a 1 con ease-out cúbico entre el 94% y el 52% del viewport.
   Mismo patrón que `applyWhyFrame`: **escrubea** con la rueda, no dispara una
   animación de duración fija. Origen `50% 50%` para que el subtítulo no se mueva.
2. **Tarjetas reorganizadas.** El marco es el SVG de marca (viewBox
   1024.267x982.443) puesto como **máscara**, no como imagen: así el color sale de
   `--salvia-deep` y se recolorea en una línea. Ocupa el 80% del ancho del slot
   (`left/right:10%`, `top/bottom:11.63%` = 0.8 / relación 1.0426).
   Copia centrada; en hover "Explore" **sube al centro**.
   `--ex-shift = (alto de .ing-copy + su margen)/2`, **medido por tarjeta en el JS**
   y recalculado en `document.fonts.ready`: la copia ocupa 1 o 2 líneas según el
   producto, un número fijo descuadraría la mitad de las tarjetas.
3. **Fotos nuevas.** Recortadas de la lámina con detección de componentes conectados
   (`scratchpad/ing/mask.py`) para aislar cada montón — el cacao arrastraba un
   cristal del montón vecino. Aplanadas sobre `#eae4d1` y graduadas (sat 1.12,
   contraste 1.05, lift +3) antes de salir a JPEG 560px. Externas en `assets/`,
   ya no base64: index.html bajó de 685 KB a 400 KB.
4. **Foto más grande que el marco.** `.ing-media` va a `inset:-2%` (104% del slot)
   contra un marco del 80% -> **1.30x**. Cabe porque el slot es mayor que el marco:
   sobresale ~7px por lado dentro de un gap de 20px y nunca toca el marco vecino
   (que empieza al 10% de su propio slot). `.ing-track` lleva `padding:20px 0`
   porque `overflow-y` del scroller cortaría el sobrante vertical.
5. **Barra invisible + arrastre.** El carril pasó de `@keyframes translateX` a
   **scroller nativo** con la barra oculta (`scrollbar-width:none` + `::-webkit-scrollbar`).
   El auto-scroll escribe `scrollLeft`, **nunca un transform**: si fuera transform,
   el arrastre y la animación se pelearían por la misma propiedad.
   La lista va **4 veces** y la ventana de trabajo es `[periodo, 2*periodo)`, así
   queda un periodo entero de pista a cada lado y el arrastre a la izquierda no
   choca contra el 0 del scroller (con 2 copias sí chocaba).
   Arrastre sólo con `pointerType==='mouse'`; en táctil manda el scroll nativo.
   Si `moved > 6px` se traga el `click` siguiente en captura, para que soltar
   encima de "Explore" no navegue. Verificado: clic limpio SÍ navega.

### Verificado a 1440x900
Sin desbordes horizontales (0px), sin scroll vertical en el carril, 0 errores de
consola, arrastre 1:1 en ambos sentidos y ambos envolviendo dentro de la ventana.

### Decisiones que Michelle puede querer revisar
- **`--salvia-deep:#93be83`** es un verde nuevo: viene de su SVG y NO es `--salvia`
  (#a6bf85). Se dejó tal cual lo mandó.
- **La descripción no quedó blanca** como en su mockup: blanco sobre #93be83 da
  **2.1:1** y no pasa AA ni como texto grande. Quedó `--cafe` al 85% = **4.9:1**.
- **Subtítulo**: "Hover to pause..." -> "Drag or hover to explore each ingredient",
  porque el arrastre es ahora la interacción principal.
- El desborde de 3px en móvil viene de `.site-nav__links`, no de esta sección.

### Corrección de proceso, 2026-08-27
Michelle: *"primero siempre se visualiza un cambio en un preview y luego se
aplica a la web para poder seguir haciendo las recomendaciones"*.
Yo había aplicado el rediseño directo a `docs/index.html`. **Revertido**:
`index.html` volvió al backup y el rediseño vive en `docs/_prev-ingredients.html`
(copia exacta de la página, no una maqueta aparte, para que lo aprobado sea el
mismo código). La versión ya construida quedó guardada en
`_backups/docs-pre-ing-20260827/index-CON-CAMBIOS.html` para re-aplicarla en un
paso cuando ella diga.
**Regla de aquí en adelante: preview -> ella lo ve -> aplicar.**

### Tipografía de las tarjetas, medida del SVG (2026-08-27)
`Downloads/Ingredient frame text.svg` — el texto viene en curvas, sin atributos de
fuente. Se midió: (a) los `<style>` dan los fills literales; (b) el alto de
mayúscula de cada bloque da el cuerpo; (c) el cociente **ancho de línea / alto de
mayúscula** identifica familia y peso, comparando contra las fuentes reales
renderizadas en canvas.

| | Familia · peso | Color | % del ancho del marco | px a 1440 |
|---|---|---|---|---|
| Título | Poppins 500 | `#382915` | 7.657% | 22.97 |
| Descripción | Kanit 300 | `#ffffff` | 6.597% | 19.79 |
| Explore | Poppins 500 | `#424f25` | 6.635% | 19.91 |

Familias y pesos **ya eran los correctos** en el sitio; lo que estaba mal era el
cuerpo (todo ~25% chico) y el color de la descripción.
Interlineado de la descripción **1.06** (medido baseline a baseline, 54.96 uds).
El bloque de texto NO va centrado en el marco: va **31.75px por debajo** del
centro (`--info-drop`), tal como en el SVG.

Los cuatro baselines se verificaron contra el SVG en % del alto del marco:
45.7 / 55.8 / 63.1 / 77.2 — objetivo 45.7 / 55.9 / 63.1 / 77.2. Clavado.
Método: `--info-drop` y el margen de Explore se despejaron de un sistema de dos
ecuaciones (el bloque va centrado *y* desplazado, así que mover un margen corre
las dos puntas media distancia cada una).

**`--ex-shift` pasó de fórmula a medición.** Antes era `(altoCopia+gap)/2`; ahora
el JS mide dónde quedó Explore respecto al centro de la tarjeta. Con el bloque
desplazado la fórmula ya no valía, y medir es inmune a cualquier cambio futuro
de márgenes. En hover la desviación verificada es **0.0px**.

**PENDIENTE con Michelle:** la descripción quedó blanca porque así viene en su
SVG, pero blanco sobre `#93be83` da **2.1:1** y el mínimo AA es 4.5:1.

### Ajustes del 2026-08-28 (todo en `docs/_prev-ingredients.html`)
- **Fotos nuevas** desde `Downloads/Ingredients/Most asked/` (5 PNG con alfa).
  Aplanadas sobre `#eae4d1`, grado suave (sat 1.05, contraste 1.02) y **recortadas
  al bounding box del alfa**: los PNG traían margen vacío y el montón quedaba chico
  dentro del círculo. 720px (2x del tamaño en pantalla). 553 KB los cinco.
  `scratchpad/ing2/tight.py` hace el recorte + aplanado + lienzo cuadrado.
- **Descripción: opción 3** — `--cafe` al 85% en vez del blanco del SVG. 4.9:1, pasa AA.
  El blanco del SVG daba 2.1:1. Decisión de Michelle.
- **Tarjetas más cerca**: margen 24px -> 12px. Hueco entre verdes 84px -> 72px.
  Más no se puede sin rehacer la geometría: el slot (360px) tiene que ser mayor que
  la foto (351px), así que 25px por lado son estructurales, no decorativos.

**Ojo, nombre del archivo:** la foto del collagen viene como `Bone Meal.png`.
El producto en la web sigue diciendo "Hydrolyzed Bovine Collagen" — no se tocó el
texto. Si es un cambio de producto, hay que confirmarlo con ella.

**Detalle conocido, sin efecto visual:** `--info-drop` es un `translateY` sobre un
`.ing-info` con `inset:0`, así que el carril reporta `scrollHeight>clientHeight`.
Está verificado que **ningún elemento visible** se sale del carril en reposo ni en
hover, y `overflow-y:hidden` no genera barra. Si algún día estorba, la solución es
cambiar el transform por `padding-top: calc(2 * var(--info-drop))`.

## Auditoría de espacios y scroll de la home — 2026-08-28
Pedida por Michelle. Todo aplicado en `docs/_prev-full.html` (preview de la página
completa, sin nada oculto). Medido a 1440x900.

### 1. Scroll muerto tras el intro — la causa de los dos "queda pegado"
`.track{height:250vh}` = 2250px. El intro scrubea sobre 1350px. Al terminar, el
código **dejaba** el track en 250vh a propósito; el comentario decía que quitarlo
hacía saltar la página. Resultado: **1350px de scroll donde el hero está clavado y
no pasa nada**. Bajando se siente muerto, subiendo se siente pegado — y subiendo
desde ingredientes se entra directo a ese tramo, que es el segundo síntoma.

**Arreglo:** en `finish()`, colapsar a 100vh (`html.intro-collapsed`) **y restar la
misma distancia del scroll en el mismo frame**. El comentario viejo tenía razón en
que saltaba; saltaba por no compensar, no porque colapsar estuviera mal.
Verificado: **salto visual 0.0px**, scroll muerto 1350px -> 0px,
página 4123px -> 2773px.

### 2. Scroll fantasma del carrusel
`--info-drop` era un `translateY` sobre un `.ing-info` con `inset:0`: eso le genera
scroll vertical fantasma al carril. Y el carril **es un scroller** — un scroller con
desbordamiento puede tragarse la rueda del ratón. Cambiado a
`padding-top: calc(2 * var(--info-drop))`. `scrollHeight - clientHeight` = **0**.
Baselines y hover verificados intactos tras el cambio (45.7 / 55.8+63.1 / 77.2 y
desviación de Explore 0.0px).

### 3. El hueco entre los values y los ingredientes
Al acortar el verde para que la O lo igualara sobraron **196px**, y el código se los
daba **todos** a la banda subiéndola: quedaba pegada al verde y con un hueco muerto
enorme debajo.

| | Antes | Ahora |
|---|---|---|
| aire sobre el verde | 38px | 38px |
| verde | 478px | 478px |
| verde -> banda | **14px** | **112px** |
| banda | 174px | 174px |
| bajo la banda | **196px** | **98px** |
| padding-top de ingredientes | 72px | **40px** |
| **banda -> título de ingredientes** | **268px** | **138px** |

`.band{bottom:calc(var(--extra)/2)}` reparte el sobrante a medias.

### Lo que está bien (medido, no tocado)
Ingredientes: título->subtítulo 18px, subtítulo->carril 45px.
Why: título->tarjetas 82px, tarjetas->citas 152px.

### Pendiente de decidir
Entre el carrusel y "Why Buyers Choose" hay **198px** (99 abajo + 99 arriba): es el
salto más grande de la página. Ahí entra la curva de revelado, así que puede ser
intencional. No se tocó.

### Contener los valores — 3 variantes a decidir (2026-08-28)
Michelle: la banda de valores "se siente rara y vacía" al bajar hacia ingredientes.
El diagnóstico real no es sólo el espacio: la banda **flota sobre el mismo crema**
que es también el fondo de la sección siguiente, así que no tiene borde donde
apoyarse y el ojo no sabe dónde termina el hero.

Tres variantes en `docs/_prev-full.html`, con selector abajo a la derecha:
- **A · caja** — caja `#dbdcc0` apoyada 48px bajo el verde, mismo ancho y radio.
- **B · montada 28px** — la misma caja, solapada 28px sobre el borde del verde.
- **C · pegada** — sin caja, la banda sube a 44px del verde.

**La caja se pinta con un `::before` que se desborda hasta los 38px del verde.**
Es clave: las columnas de la banda están alineadas al pixel con el titular (x=130)
y con la O (derecha x=1310). Mover la caja de la banda movería las columnas y
rompería esa alineación; el pseudo-elemento pinta la superficie sin tocarlas.

**El solape de B tiene un techo duro de 28px:** bajo los botones del hero sólo hay
41px de verde libre (botones terminan en 475, verde en 516). Con 62px de solape la
caja tapaba "Request a FREE sample". Verificado.

**La caja va opaca (`#dbdcc0`), no salvia al 22%:** en la variante montada tiene que
TAPAR el verde, o el texto café cae sobre verde oscuro y no se lee. #dbdcc0 es
exactamente salvia al 22% compuesto sobre crema, así que sobre el crema se ve igual.
Si Michelle elige A o B hay que promoverlo a token de marca.

### Valores: franja a sangre + tipografía (2026-08-28, elección de Michelle)
Eligió la variante A pero **sin márgenes**: la franja va de borde a borde. Selector
de variantes eliminado.

- `.band::before{left:-100vw;right:-100vw}` y el recorte lo pone `.stage{overflow:hidden}`:
  llega al borde real sin depender del ancho de la barra de scroll.
- Color como token: **`--salvia-veil:#dbdcc0`** (= salvia 22% sobre crema).
- La banda se ancla **bajo el verde** (`top: 38px + var(--o-h) + 48px`), ya no al pie.
- Título -> bajada: margen 12px -> **6px**.
- Bajada: `--t-sm` -> **`--t-base`** (15 -> 18px), **sin opacidad** y en `--cafe`.
  "Negro" se resolvió como `--cafe` #382915, el más oscuro de la marca — no #000,
  que no existe en la paleta. Contraste sobre la franja: **10.0:1**.

**Dos trampas que costaron encontrar:**
1. Bajo 920px la O se oculta y **`--o-h` vale `auto`**. Eso invalida el `calc()` del
   `top`, `top` y `bottom` quedan en `auto` y la banda se va al borde superior del
   stage, **detrás del verde** (z-index 1 vs 2). Guardado con
   `@media (max-width:920px){.band{top:auto;bottom:calc(var(--extra)/2)}}`.
2. La bajada a 18px **solapa las filas de la banda en móvil**, que ya venía apretada.
   El tamaño mayor se limitó a escritorio; en móvil sigue en `--t-sm`.

La alineación de las columnas se verificó intacta: 130 / 1310, igual que el titular
y el borde derecho de la O.

### Lo que se sacó de nutritionformulators.com (2026-08-28)
Medido en su DOM, no a ojo:
- **Cero huecos entre bloques.** Su hero termina en el pixel 803 y la sección
  siguiente empieza en el 803. Ningún respiro de fondo entre uno y otro.
- **La sección de después del hero lleva su propio color** (`#e8f6fa`) con 112px de
  padding arriba y abajo. El ritmo es: imagen a sangre -> banda de color pegada ->
  secciones sobre el fondo base.
- Su hero es a sangre completa, sin tarjeta redondeada ni márgenes. **Eso NO se
  copió**: la tarjeta verde con márgenes es una decisión ya tomada del diseño.

**Aplicado:** la franja de valores ahora (a) arranca exactamente donde termina el
verde (hueco = 0) y (b) llega hasta el pie del stage (falta = 0), con el contenido
centrado por `align-content:center`. El padding pasa a ser el mínimo de aire, no la
posición. Antes tenía crema arriba **y** abajo, y por eso no se ataba a nada: era
una isla del mismo color que el fondo de la sección siguiente.

Efecto secundario esperado: al reclamar la franja más alto, `bandGap` crece y el
verde baja de 478 a 450px (y la O con él, que la sigue). Es la realimentación de
`bandGap = band.offsetHeight + BAND_AIR - INSET`. 28px, se dejó así.
El padding-top de ingredientes vuelve a `clamp(56px,8vh,104px)`: ya no compensa nada,
porque la franja llega hasta el borde.

### Motion de los valores — 4 opciones a decidir (2026-08-28)
Michelle: "¿y si hacemos más bien que salga del hero?". La conexión la haría el
**movimiento**, no sólo el layout. Preview aparte: `docs/_prev-values-motion.html`,
con el hero ya compuesto y un selector + "Repetir".

1. **Cajón** — la franja entera sale de debajo del verde (`translateY(-alto)` -> 0, .95s).
2. **Persiana** — la franja se despliega hacia abajo (`clip-path inset`), texto entra a .38s.
3. **Escalonado** — igual que 2, y las columnas suben una tras otra (.28/.40/.52/.64s).
4. **Actual** — sube 14px y aparece, para comparar.

**Por qué el cajón funciona sin máscaras:** la banda va en z-index 1 y la tarjeta
verde en 2. Todo lo que la banda haga por encima de su posición final queda tapado
por el verde. No hace falta recorte ni contenedor extra.

**La trampa:** el intro escribe `opacity` y `transform` **inline** sobre la banda, y
eso le gana a cualquier regla CSS. El preview los limpia antes de cada reproducción
o no se ve ningún motion.

**OJO al verificar:** el panel de Claude Code congela las transiciones CSS, así que
ahí el motion no corre — los estados iniciales sí se verificaron uno por uno.
Hay que abrirlo en Chrome.

Recomendación: la **3**, porque además de conectar lleva el ojo por los cuatro
valores, que es para lo que está esa banda. La 1 es la respuesta más literal a
"que salga del hero".

### Corrección de forma — la tarjeta de valores, 2026-08-28
Michelle: *"el frame verde sale del frame verde oliva del título, y tiene borde
redondeado al final"*. Cuando dijo antes "pegado a los bordes" se refería a los
bordes de **la tarjeta verde**, no a los de la ventana. Yo la hice a sangre completa;
mal. Su screenshot ya lo mostraba y no lo leí.

Forma correcta, verificada:
- Superficie de **38 a 1402** = los bordes exactos del verde (medido, no estimado).
- `top:-40px`: **nace detrás del verde**. Así las esquinas redondeadas del verde
  apoyan sobre esta superficie y no sobre el crema. Ese trozo queda tapado porque
  el verde va en z-index 2 y la banda en 1.
- `border-radius:0 0 28px 28px` — redondeado sólo abajo; arriba se funde con el verde.
- Altura propia (178px), no hasta el pie del stage. Debajo queda crema que fluye
  hacia la sección de ingredientes: un solo corte, no una isla.

Con esta forma el **cajón** es el motion natural: `--band-h` (178px) es justo lo que
hay que subir la banda para que su borde inferior coincida con el del verde y
desaparezca del todo. Verificado: al inicio la superficie queda en 120-338, con el
verde terminando en 516 — completamente oculta.

La opción 3 pasó de "persiana + escalonado" a **"cajón + escalonado"**: sale la
tarjeta y las columnas suben una tras otra.

### Dos fallos del 2026-08-28 y sus causas reales
**1. "Cuando bajo vuelve y aparece el logo"** — sólo en `_prev-values-motion.html`.
Ese preview añadía `intro-collapsed` a mano para dejar el hero compuesto, pero el
`scrollDriver()` del intro **seguía enganchado**. Con el track colapsado,
`total = track.height - stage.height` da 0, `p` da 0, y como el intro nunca corrió
`maxP` seguía en 0: al hacer scroll, `applyFrame(0)` = el logo gigante.
`_prev-full.html` nunca lo tuvo porque ahí `maxP` llega a 1 de verdad y no retrocede.

Arreglado por dos vías:
- En el preview: marcar el intro como hecho **antes** del script de cabecera, para que
  `boot()` tome la rama `already` y llame a `finish()` sin enganchar el driver. La
  marca se borra en `pagehide` — `sessionStorage` es del origen entero y si se queda
  puesta, `_prev-full.html` se abriría sin su intro en la misma pestaña.
- En el intro mismo (blindaje): `if(total<=0) return;` en `read()`. Un recorrido de 0
  no es "progreso 0", es "no hay recorrido". Así el fallo no puede volver por ninguna vía.

**2. "Sigue cargando"** — el servidor, no la página. En la red del navegador quedaron
**seis `ERR_CONNECTION_RESET` seguidos** sobre el HTML antes de un 200.

Causa de fondo, encontrada: `serve.py` no ponía **timeout al socket**. Un cliente que
abre conexión y no completa la petición se queda con un hilo y un descriptor **para
siempre**. El navegador abre conexiones especulativas y aborta rangos de vídeo sin
parar, así que se acumulan; a los ~2 días el proceso agota su límite de descriptores
(256 por defecto en macOS), `accept()` falla y el servidor queda **escuchando pero sin
atender**. Coincide exacto con las dos caídas: la primera a 2 días, la segunda a
2 días 1 hora.

Arreglado en `serve.py` (backup en `_backups/serve.py.bak-*`):
- `timeout = 30` en el handler.
- `handle_error` que se traga desconexiones normales en vez de escupir traceback.
- `RLIMIT_NOFILE` subido a 4096 como segundo cinturón.
Servidor reiniciado y verificado: raíz, HTML y vídeo en 200.

Verificado tras ambos arreglos: bajando y subiendo por cinco posiciones el logo no
reaparece nunca, `readyState` completo y cero errores de consola.

### Motion 3 integrado al intro + espacio de ingredientes (2026-08-28)
Michelle eligió la **3 · cajón + escalonado**. Ya no vive en botones de preview:
va dentro de `applyFrame`, **scrubeado con el scroll** como el resto del intro.

- `bandH = band.offsetHeight` (178px), medido en `measure()`. Es justo lo que hay que
  subir la banda para que su borde inferior coincida con el del verde y quede
  escondida entera detrás (banda z-index 1, verde 2). El transform no afecta a
  `offsetHeight`, así que se puede medir en cualquier momento.
- Opacidad de la banda: `seg(p,0.45,0.56)` — **aparece con la tarjeta**, no después.
  Antes era 0.70-0.96; si aparece más tarde que el verde se la ve flotar sobre el crema.
- Cajón: `easeInOutCubic(seg(p,0.78,0.97))`. Arranca en 0.78 porque hasta 0.88 el
  recorte del verde sigue siendo mayor que su tamaño final y aún la tapa entera.
- Escalonado: cada columna con su tramo, corrido 0.023 → el último acaba en **0.999**.
  Todo tiene que caber antes de 1 o la última columna se corta.
- `html.intro-armed .band>div{opacity:0}` para que no parpadeen antes del primer frame.

Barrido verificado: p=0.78 y=-178 oculta · 0.85 y=-142 col1 0.30 · 0.90 y=-36
cols 0.96/0.80/0.40/0.00 · 0.95 y=-0.8 · 1.00 y=0 y las cuatro a 1.

**Espacio del carrusel:** el hueco real del subtítulo al verde eran **93px**, y sólo
45 el margen. Los otros 48 eran relleno invisible: 12 del carril y **36 de la propia
tarjeta**, que mide más que el círculo para que la foto pueda crecer en hover.
Reducidos margen (45→12) y carril (12→8): **93 → 56px**. Los 36 estructurales se
quedan; tocarlos encogería el marco o rompería el crecimiento de la foto.

### Textura de vidrio en los marcos — 4 opciones a decidir (2026-08-28)
Preview: `docs/_prev-frames.html`, selector abajo a la derecha.
A · Plano (actual) · B · Vidrio liso · C · Vidrio + foto tenue · D · Vidrio + foto marcada

**El "frost" se hace con degradado, no con grano** (ella pidió "liso"): un brillo
radial arriba-izquierda + un degradado de cuerpo #a9cd99 -> #93be83 -> #82ad73.
Contraste del texto verificado en los dos extremos: 7.9:1 en el claro, 5.5:1 en el
oscuro. Pasa en todo el degradado.

**La foto detrás NO usa `filter:blur()`.** Se usa una copia de **48px estirada**: el
suavizado de la ampliación hace el desenfoque gratis. 20 `blur()` en vivo arrastran
el carrusel; las cinco miniaturas pesan **7 KB entre todas**
(`assets/ing-*-blur.jpg`). Sólo queda un `saturate()`, que es barato.

**Refactor necesario:** la URL de la foto pasó de `.ing-media` al `<article>` como
`--photo` / `--photo-blur`. Así la usan las dos capas —el hover y el vidrio— sin
repetir la URL ni duplicar la descarga. Los 20 artículos reescritos.
La máscara de `.ing-shape` recorta también a sus hijos, así que la foto hereda la
forma de la O sin ningún recorte extra.

**Ojo con la D:** la tarjeta de cacao se oscurece bastante y rompe la consistencia
con las otras cuatro. Contraste calculado en el peor punto: **~4.2:1**, por debajo
del 4.5 de AA. La C se queda en ~5.2:1. Si elige la D hay que subir el velo verde.

## Ingredientes v2 — sin marco (2026-08-31)
De `Downloads/SVG Ingredients v2.svg` (viewBox 931.788 x 722.611). Preview:
`docs/_prev-ing-v2.html`. Sustituye el marco verde por una **figurita sobre el
título**: la 'o' inclinada del logo rellena con la foto del ingrediente.

**La tipografía NO cambia.** Los cuerpos medidos son idénticos a los del SVG
anterior (título cap 41.94, desc 33.49, explore 36.35 → 23.3 / 20.1 / 20.2px a un
slot de 360). Lo que cambia:
- **Descripción a `--oliva-deep:#354c1f`** (antes blanco / café al 85%). Sin el marco
  verde detrás, sobre crema da **7.5:1** — ya no hay que negociar contraste.
  Título 11.0:1, Explore 6.9:1. Los tres cómodos.
- Figura: **18.07% del ancho de la tarjeta** = 65px, caja cuadrada (168.4x168.4).
- Fuera `--info-drop`: en este SVG el bloque va centrado en la tarjeta.

**Verificado contra el SVG, al pixel:**
figura 65px · figura→cap del título 12.4 · título→desc 32.3 (obj 32.5) ·
interlineado 21 · desc→Explore 36.5 (obj 35.8). Hover: foto 351px, copia oculta,
Explore centrado en la foto con desviación **0.0px**.

**Dos trampas:**
1. `width:18.07%` en `.ing-fig` medía contra la caja de texto (`.ing-info` lleva
   10.3% de padding), no contra la tarjeta: salía 52px en vez de 65. Va como clamp
   derivado del slot.
2. `.ing-explore` necesita `margin-top:0`. Su relleno de 9px —el que reserva la
   píldora del hover— ya aporta todo el aire que pide el SVG; con margen encima se
   iba a 48px contra los 35.8 del diseño.

**Pendiente de decidir:** los polvos blancos (creatina, los dos magnesios) casi
desaparecen en la figurita: son pálidos sobre crema y la forma es pequeña. El cacao
y el collagen se leen bien. Se puede subir el contraste sólo de esas tres o poner un
fondo muy tenue detrás de la figura.

### v2 — tres correcciones de Michelle (2026-08-31)
1. **Figurita al 240%** (era 140%). La 'o' está **inclinada**, así que su contorno llega
   a las esquinas de su caja — 46px del centro en una figura de 65px. A 140% el montón
   sólo cubría 41px de radio y asomaba el crema en las puntas. A 240% pasa de 64px.
2. **Foto del hover 351 → 286px.**
3. **Tarjetas más juntas y más cerca del título.** Sin marco la tarjeta ya no tiene que
   ser cuadrada ni ancha: `318 x 250` (era `360 x 360`), margen 12 → 6px.
   Y el bloque se ancla **arriba** (`justify-content:flex-start`) en vez de centrarse:
   centrado dejaba **66px de aire muerto sobre la figurita**, que era lo que la
   separaba del subtítulo.

| | Antes | Ahora |
|---|---|---|
| subtítulo → figurita | 86px | **34px** |
| hueco entre textos de tarjetas | 85px | **57px** |
| foto del hover | 351px | **286px** |

**Trampa:** con la tarjeta a 318px, el margen lateral del SVG (8.06%) dejaba la caja
de texto en **267px** y "Alkalized Cocoa Powder" mide **267 clavados** — se partía en
dos por cero margen. Causa de fondo: al estrechar la tarjeta mantuve el cuerpo del
título (22.97px, ya aprobado) en vez de escalarlo con ella; en las proporciones del
SVG ese título mediría 20.6px y sobraba sitio. Margen bajado a 6.5%.

Verificado a 1440 y a 375: bloque dentro de la tarjeta, sin recorte vertical, sin
desbordes nuevos, 0 errores de consola.

**Sigue pendiente:** los polvos blancos se leen flojos en la figurita (son pálidos
sobre crema). El cacao y el collagen se ven bien.

### Tono de las figuritas blancas (2026-08-31)
Los polvos blancos se disuelven en el crema. Michelle pidió primero oscurecerlos y
luego se replanteó: *"maybe not darker, maybe brighter"*. Tenía razón — el crema es
**beige cálido**, así que un blanco más puro se separa igual de bien y se ve limpio,
mientras que oscurecer los vuelve grises y apagados.

Selector en el preview con las tres, **arranca en "Más brillante"**:
- oscuro: `brightness(.9) contrast(1.1)`
- brillante: `contrast(1.2) brightness(1.05) saturate(.92)`

**Más brillante NO es sólo subir `brightness`:** sobre un blanco casi puro eso lo
quema y se pierde el grano del polvo. Es el **contraste** el que abre los blancos
hacia arriba conservando las sombras que dibujan la textura.

**Decisión final de Michelle:** creatina **Original**, los dos magnesios **Más
brillante**. Selector eliminado. Yo lo había aplicado a los tres por simetría; ella
prefirió dejar la creatina sin tocar. `--fig-tone` sólo en `.img-4` y `.img-5`.

El tono va sólo en la figurita; la foto grande del hover **nunca lleva filtro**
(verificado `none` en las cinco). Se ajusta en una línea y no duplica archivos.

### Fotos del hover: mismo alto para las cinco (2026-08-31)
Michelle sospechó que el fondo transparente contaba como alto. **Tenía razón**, y era
un fallo del pipeline: yo recortaba al bounding box del alfa y luego rellenaba a un
cuadrado de `max(ancho,alto)`. En los montones anchos eso deja relleno arriba y abajo
que **sí cuenta** para el `background-size:contain`.

| | Alto del montón dentro de su cuadrado |
|---|---|
| collagen / creatina / cacao | 100% |
| magnesium oxide | 90% |
| **magnesium citrate** | **81%** |

Rehechas: el montón se escala a **80% del alto del lienzo en las cinco**, y el ancho
queda libre. **80 es el techo, no un número redondo**: el citrato es el más ancho
respecto a su alto (1.238) y por encima del 80% se saldría de los lados.
Pipeline en `scratchpad/h/mk.py` — bbox del alfa sobre una copia de 480px, escalado
de coordenadas a resolución completa, `sips -c` + `--resampleHeight`, y aplanado
sobre crema centrado.

Verificado sobre los JPEG **ya instalados**: 79.2 / 79.2 / 77.1 / 79.6 / 79.6%.
El 77.1 del cacao es ruido de medición (motitas tenues que la compresión suaviza),
no un encuadre distinto: el build colocó los cinco montones a 576px exactos.
Antes la diferencia era de 19 puntos; ahora menos de 3.

Copia de las anteriores en `docs/_old-ing/`. Miniaturas de desenfoque regeneradas.

### Sombra en las fotos del hover (2026-08-31)
Referencias de Michelle: moodboards BEMHAUS/ELEGANZA — recortes con sombra suave
abajo-derecha, luz desde arriba-izquierda.

**Por qué no se puede con CSS:** `filter:drop-shadow()` usa el canal alfa, y nuestras
fotos son JPEG aplanados sobre crema. Sombrearía el **rectángulo**, no el montón.
Volver a PNG con alfa costaría ~3 MB los cinco.

**Solución: hornear la sombra.** El fondo es un crema plano y conocido, así que una
sombra pintada en el propio archivo se ve idéntica a una en vivo y no cuesta nada en
ejecución. `scratchpad/h/shadow.py`: máscara = alfa del ingrediente desplazado
(+13,+21), difuminado con **tres pasadas de caja separable** (≈gaussiana, lineal en
el número de píxeles — una gaussiana real en Python puro sería inviable), y el crema
oscurecido por ella antes de pintar el ingrediente encima.
Sombra en **gris cálido (96,84,64) al 34%**, no negro: sobre crema el negro ensucia.

Peso: 470 KB los cinco, +14 KB respecto a las versiones sin sombra.

**Efecto colateral bueno:** los polvos blancos ya se separan del crema por sí solos —
se ven las sombras de los cristales sueltos. El ajuste de tono de los magnesios sigue
puesto, pero puede que ya no haga falta.

**Verificado que la sombra NO se cuela en la figurita:** la elipse recorta el interior
del montón, donde el ingrediente es opaco y tapa su propia sombra. (Un falso positivo
en la primera revisión resultó ser la foto del hover desvaneciéndose, no una fuga de
la máscara.)

### La sombra, estilizada — segunda pasada (2026-08-31)
Michelle: *"looks like an eraser mark"*. Tenía razón: una **sola** capa difuminada de
forma uniforme no es una sombra, es un borrón. No tiene ni anclaje al suelo ni caída.

Rehecha con **dos capas**, como en fotografía de producto (`scratchpad/h/shadow2.py`):
- **Contacto** — desplazamiento (3,5), difuminado 7, opacidad 0.44. Corta y oscura,
  justo bajo el objeto: es la que lo ancla. Con un difuminado pequeño, cada haba y
  cada cristal suelto recibe **su propia sombra nítida** en vez de fundirse todas en
  una neblina — eso era la mitad del efecto borrón.
- **Proyectada** — desplazamiento (16,26), difuminado 32, opacidad 0.15. Amplia y
  tenue, el ambiente.

Se combinan como dos capas translúcidas: `a = 1-(1-a1)(1-a2)`.
Más **gamma 1.35** sobre la máscara: aprieta la caída del borde. Sin eso el degradado
se queda plano y vuelve el aspecto de borrón, aunque sean dos capas.

Color gris cálido (88,76,58). Peso: 473 KB los cinco, +3 KB respecto a la primera
versión.

## Portafolio — tarjeta nueva (2026-08-31)
Preview: `docs/ingredients/_prev.html` (dentro de `ingredients/` para que las rutas
relativas a `../assets/` sigan valiendo). Diseño de `Downloads/Portfolio.svg`.

**Tipografías identificadas** (mismo método de siempre, ancho/alto-de-mayúscula):
título y botón **Poppins 500** (título err 0.002 — exacto); píldora, categoría y
tabla **Kanit**. Colores literales del SVG: tarjeta #fff, chip #312210 sobre #e7dec7,
título #382915, tabla #302210, botón #495430, punto verde #48b84a con resplandor,
círculo de estrella #94bd83.

**Todo en `cqw`** (1cqw = 1% del ancho de la tarjeta): cada medida del SVG dividida
por 651.236. Verificado contra el diseño: título 8.02, píldora 6.26, estrella 15.15,
foto 88.7 (obj 88.6), botón 56.6 — clavados.

**Dos trampas de `cqw`:**
1. **Mide la CAJA DE CONTENIDO del contenedor, no su caja externa.** Con el relleno
   en la propia tarjeta, ese relleno salía del ancho de referencia y todo se encogía
   (título a 7.8px en vez de 28). El relleno vive ahora en `.pf-in`.
2. Una caja **no puede medirse contra sí misma**: las propiedades de `.pf-card` en
   `cqw` se resolvían contra el viewport (relleno de 126px). Van en px.

**Tarjeta de FLUJO, no calco absoluto:** los productos tienen entre 0 y 3 variantes y
nombres de largos muy distintos. Sin `align-items:start`, las tarjetas se estiran a la
altura de su fila y la foto se pega abajo con `margin-top:auto` — así las fotos de una
fila quedan alineadas. Verificado: 483/483/483 y 411/411/411.

**Imágenes:** 36 de 40. Recortadas a 1.869:1 (la proporción del SVG) a 560x300,
en `assets/portfolio/`. 1.7 MB las 36. sips sí lee webp y avif.

### Pendiente de decidir con Michelle
- **La estrella**: ella dijo "no estoy segura". Está puesta tal cual el SVG, en los 4
  productos que ya tenían `star:true` en los datos.
- **4 sin foto**: Eggwhite Protein Powder, Magnesium Bisglycinate, L-Carnitine Base,
  Polydextrose. Llevan una trama neutra de marcador de posición.
- **11 imágenes por debajo de 560px** de ancho nativo (la más pequeña, Bhumi Amla, 335)
  — se ampliaron y se verán algo blandas.
- **Los dos Amla**: `Amla : Emblica.webp` -> Emblica officinalis y `Amla.jpg` ->
  Phyllanthus emblica. Asignación por el nombre del archivo; conviene que lo confirme.
- **"Tech Specs" y "+ Product info"** no llevan a ninguna parte todavía.

### Portafolio — datos nuevos y diagramación (2026-08-31)
- **Datos y agrupación** según la lista de Michelle: 32 productos con su categoría y
  sus variantes. Categoría nueva **"Other Functional Ingredients"** (Shilajit sale de
  Specialty). Nombres cambiados: "Amla / Emblica" y "Amla", "Centella Asiatica",
  "Licorice", "Tribulus Terrestris", "Arjuna", "Shatavari" — sin los paréntesis.
  El binomio latino va en cursiva: `<i>` es el **único** HTML que la tarjeta deja
  pasar, vía `escI()`; el resto se escapa igual que antes.
- **Los 8 que NO estaban en su lista se conservan**, marcados en el código. Borrar
  productos de un catálogo no es reversible y ella subió foto para tres de ellos —
  hay que preguntar antes.
- **Filtros actualizados** a las categorías nuevas: estaban escritos a mano en el HTML
  y habrían dejado de coincidir. Verificado: 2+7+4+23+1+3 = 40.
- **Altura igual en TODA la rejilla** (`grid-auto-rows:1fr`), no sólo por fila.
  Verificado: una sola altura distinta entre las 40.
- **Fila de una sola columna** cuando la variante no trae grado (Creatine): sin la
  división vertical que dejaba el hueco blanco, texto a la izquierda.
- **Sin regla bajo la última fila**: pegada a la foto se leía como borde de la imagen.
- Imágenes: 39. Se **borraron** las 4 que reusaban las del home (creatina, los dos
  magnesios, cacao) — Michelle no quiere repetirlas. Esas 4 + Magnesium Bisglycinate
  van con marcador hasta que mande fotos propias.

### Pendiente
- **La estrella**: quiere cambiarla, pidió ideas (van en la respuesta).
- Los 8 productos fuera de su lista: ¿se quedan o salen?
- Faltan 5 fotos.

### Portafolio — cursivas fuera y estrella -> borde (2026-08-31)
**Cursivas eliminadas** a petición de Michelle. Motivo real de que se vieran mal,
verificado: **de Kanit sólo están cargadas las caras normales** (300 y 400, ninguna
italic). El navegador estaba **inclinando la letra a mano**, no usando una cursiva de
verdad — mismo ancho en normal y en cursiva (315 vs 314.5px) lo confirma.
Si algún día se quiere el binomio en cursiva (es la convención científica), hay que
cargar la cara italic real de Kanit desde Google Fonts, no activar `font-style`.

**La estrella se fue.** Producto destacado = `border-top:4px solid var(--oliva)`.
`box-sizing:border-box` lo mete dentro del alto, así no rompe la rejilla igualada
(verificado: una sola altura, 455px). La fila superior queda sólo con la píldora
"Available", y su `min-height` bajó de 15.15 a 6.26cqw.

**Trampa que me comí:** el punto verde de "Available" era un `<i class="pf-dot">`, y
al borrar las cursiveas con un reemplazo de `</i>` le quité el cierre. Todo el
contenido de la tarjeta quedó dentro de esa etiqueta: layout roto y texto en cursiva.
Cambiado a `<span>` para que no pueda repetirse.

**Sin foto (5):** Creatine Monohydrate, Magnesium Citrate, Magnesium Oxide,
Magnesium Bisglycinate, Alkalized Cocoa Powder.

### Fotos nuevas y el .ai de sombras (2026-08-31)
Portafolio: entraron creatina, magnesium citrate y cacao. **38 de 40 con foto**;
faltan Magnesium Oxide y Magnesium Bisglycinate, que dependen de si los magnesios
siguen siendo tres tarjetas o pasan a una sola.

**`Ingredientes sombras.ai`**: por dentro es un PDF (`%PDF-1.6`). `sips` lo rechaza
por la extensión, pero copiándolo a `.pdf` lo rasteriza sin problema. Contiene el
**cacao ya con la sombra de Michelle** — ese no hay que rehacerlo.

**Los PSD de V2 NO llevan sombra** (ella lo confirmó: la puso en Illustrator y los
manda en PNG). Se convierten bien con `sips -s format png` conservando el alfa, por
si hicieran falta.

### Sombras de Michelle en el carrusel del home (2026-08-31)
Los 5 PNG de `Imagenes ingredientes v2/` (4475x4500 con alfa, sombra hecha por ella
en Illustrator) sustituyen a la sombra que yo había horneado. Mapeo por inspección:
01 cacao, 02 collagen, 03 creatina, 04 citrato, 05 óxido.
Se componen sobre crema a 720px con el montón al 80% del alto, igual que antes.
445 KB los cinco.

**Trampa:** el encuadre se toma de la parte **opaca**, no del alfa completo — el alfa
incluye la sombra, y si mandara, un montón con sombra grande saldría dibujado más
pequeño que otro con sombra corta.

**Y el umbral de "opaco" tiene que ser RELATIVO al máximo de cada imagen.** Con un
250 fijo, el collagen (cuyo alfa no pasa de **240**) quedaba descartado entero y salía
un lienzo vacío de 9 KB. Ahora: `th = max(120, maxAlfa*0.85)`, con aserción si la
caja sale degenerada.

Portafolio: 38 de 40 con foto. Faltan Magnesium Oxide y Magnesium Bisglycinate.

### Fotos del hover, más grandes (2026-08-31)
Dos palancas, no una:
1. **Dentro del archivo**: el montón pasa del 80% al **85%** del lienzo. 85 es el tope
   real — el citrato es el más ancho respecto a su alto (1.181) y por encima se saldría
   de los lados. Medido sobre las cinco imágenes nuevas.
2. **En el diseño**: la foto pasa a `width:112%` de la tarjeta = **356px** (era 250).
   Montón visible **303px contra 200 = +51%**.

**La foto se ancla ARRIBA, no al centro.** Centrada, la mitad del sobrante iba hacia
arriba y obligaba a subir el `padding-top` del carril, que es justo lo que separaba
las tarjetas del subtítulo (lo que ella había pedido apretar). Anclada arriba, todo
el sobrante cae hacia abajo y lo absorbe un `padding-bottom` de 112px en `.ing-track`,
compensado bajando el pie de la sección. Resultado: subtítulo->figurita sigue en 34px.

**Dos trampas encadenadas:**
- `inset:auto` escrito DESPUÉS de `top/left` anulaba el centrado y la foto se iba
  arriba del todo; el carril la cortaba por la mitad.
- `--ex-shift` se medía con `getBoundingClientRect()`, pero en reposo la foto lleva
  `scale(.9)` y el rect devolvía la caja encogida: Explore quedaba 17.8px descentrado.
  Ahora se mide con `offsetTop/offsetHeight`, que ignoran el transform. Verificado: **-0.4px**.

Portafolio: llegaron Magnesium Oxide y Bisglycinate. **40 de 40 con foto.**

### Foto centrada + las vecinas se apartan (2026-08-31)
- **Centrada otra vez.** Sobresale 53px arriba y abajo; el aire lo pone
  `.ing-track{padding:56px 0}` y **el de arriba se cancela con
  `.ing-carousel{margin-top:-48px}`**: el recorte de `overflow-y` queda 48px más alto
  (así la foto cabe) pero visualmente las tarjetas no se alejan del subtítulo.
  Verificado: sigue en **34px**.
- **Las vecinas se apartan 16px** al pasar el ratón. Con selectores de hermano sólo se
  alcanza la siguiente; **`:has(+ .ing:hover)`** permite alcanzar también la anterior.
  Va como variable `--nudge` y se compone con el desplazamiento vertical del hover en
  un solo `transform`. Desactivado en táctil.

**Tercera trampa seguida con `--ex-shift`** (van tres formas distintas de medirlo mal):
al centrar la foto con `top:50%` + `translateY(-50%)`, `offsetTop` sólo ve el `50%`,
nunca el `-50%` — daba un centro 178px más abajo del real y Explore se salía de la
sección. Como la foto está centrada en la tarjeta, su centro **es** el de la tarjeta:
se mide contra `c.offsetHeight/2`. Verificado: **-0.3px**.

### Recortes de verdad + espaciado de la sección (2026-08-31)
**"Se ve el fondo" — comprobado, no supuesto.** Pinté la sección de rojo: apareció una
banda crema continua. Las fotos SÍ arrastraban un cuadrado de fondo sólido; el desfase
de 1 nivel del JPEG (235,228,208 contra 234,228,209) hacía visible el canto.

**Solución: color en JPEG + transparencia en máscara aparte.**
Un PNG con alfa a 720px pesaba **4 MB** los cinco. sips **no escribe WebP** (sí lo lee).
En vez de eso: `ing-X.jpg` lleva el RGB y `ing-X-mask.png` el alfa en escala de grises.
La máscara puede ir a **400px y 16 niveles** porque es una sombra suave — pasó de
601 KB a **64 KB** las cinco. Total 690 KB contra 4 MB.
En el JPEG, las zonas transparentes se rellenan de **crema, no de negro**: el JPEG
sangra entre bloques y dejaría un halo oscuro en el borde de la sombra.

**Dos trampas de la máscara CSS:**
1. Un PNG en **escala de grises no tiene canal alfa**, y `mask-mode` por defecto
   (`match-source`) lo lee como "todo opaco": no recortaba nada. Hace falta
   **`mask-mode:luminance`** (blanco muestra, negro oculta).
2. Y tiene que ir **DESPUÉS** del atajo `mask`, que lo reinicia.

**Espaciado**, de su referencia y redondeado a la retícula de 4px del audit:
título -> subtítulo **26px** (era 18), subtítulo -> iconos **68px** (era 34).
El segundo hueco tiene que ser claramente mayor que el primero o el subtítulo se lee
pegado a las tarjetas.

## Portafolio como sistema — 2026-08-31
Brief de Michelle: que las 40 tarjetas se lean como un solo sistema, con jerarquía
y componentes que aparecen o desaparecen según la información de cada producto.

### Análisis del contenido real (medido, no supuesto)
- **Común a las 40:** nombre, categoría, foto, disponibilidad, botón de cotización.
- **Opcional:** variantes — **4 productos con 0, 25 con 1, 10 con 2, 1 con 3**.
  El grado (columna izquierda) falta en 3 de 48 filas. Destacado: 4 de 40.
- **Componente propio:** sólo la fila de variante, que es lo único repetible y de
  número variable. Lo demás son piezas únicas que se muestran u ocultan.
- **Rangos que condicionan el diseño:** nombre más largo 26 caracteres;
  descripción de variante de 7 a 63 caracteres (mediana 17).

### Decisiones
1. **La categoría baja del nombre.** Encima competía con él siendo información de
   tercer nivel. Conserva la pastilla oscura del SVG, pero más pequeña y debajo:
   la jerarquía la hacen la posición y el tamaño, no otro color.
2. **"Product info" sale del título.** Pegado al nombre le robaba peso; ahora es una
   línea propia, al 72% de opacidad.
3. **La foto ABSORBE la holgura** (`flex:1` en vez de `aspect-ratio` fijo). Un producto
   sin variantes tiene menos texto y su foto sale más alta: **301 / 264 / 180 / 161px**
   según tenga 0, 1, 2 o 3 variantes. Las tarjetas se sienten intencionadas en vez de
   incompletas, y **las 40 siguen midiendo lo mismo (486px)**.
4. **El botón sube a acción principal**: 78% del ancho, más alto, con sombra propia.
   **Sin subrayado, a propósito** — el enlace secundario también va subrayado, y con
   los dos subrayados la jerarquía se pierde. El relleno sólido ya dice "botón".
   (Se aparta del SVG, donde iba subrayado.)
5. **La pastilla "Available" baja de tono**: es idéntica en las 40, no distingue nada
   y no debe competir por atención. Sombra casi eliminada.

Orden final: disponibilidad · **NOMBRE** · categoría · variantes · product info ·
foto + **botón**.

### Alineación del título y auditoría de resolución (2026-08-31)
**El título reserva siempre dos líneas** (`min-height:17.81cqw` = 2 x 1.11 x 8.02):
así la categoría y todo lo de debajo arrancan a la misma altura en las 40. Ninguno
pasa de dos líneas — el más largo son 26 caracteres.

Los nombres de **una sola línea van centrados** dentro de esas dos líneas
(`display:flex; align-items:center`): pegados arriba dejaban el hueco justo encima de
la categoría y se leían caídos. Verificado: 11px arriba, 12px abajo.

**Trampa:** no era el título lo que desalineaba. Eran las **4 tarjetas destacadas**:
`border-top:4px` ocupa layout y bajaba su contenido 4px respecto a las otras 36.
Cambiado a `box-shadow: inset 0 4px 0`, que no ocupa nada. Verificado: nombre 46,
categoría 118, tabla 151 — un solo valor en las 40.

**Auditoría de resolución.** El alto de la foto depende del número de variantes
(301 / 264 / 180 / 161px para 0 / 1 / 2 / 3), así que los productos SIN variantes son
los que muestran la foto más grande. Cruzando alto mostrado con ancho original:
19 productos convendría re-fotografiar, y los 4 más urgentes son justo los que no
tienen variantes. Lista completa en la respuesta a Michelle.

### Fila superior de la tarjeta (2026-08-31)
- **Alineada a los bordes de la foto**: `.pf-top{margin:0 -3.1cqw}`, los mismos que
  lleva `.pf-shot`. Verificado: borde derecho de "Available" y de la foto en el mismo
  pixel (498), y el izquierdo de "Star product" con el de la foto (188).
- **El punto verde pasa a la derecha** del texto con `flex-direction:row-reverse`,
  sin tocar el marcado.
- **"Star product" vuelve como etiqueta**, a la izquierda de la fila. La línea oliva
  sola no decía qué significaba. Va en oliva al 10% — presente pero sin competir.
  `justify-content:space-between` reparte las dos; `:not(:has(.pf-star))` manda la
  única pastilla a la derecha en las 36 tarjetas sin destacado.

### Banda "Star product" (2026-08-31)
La marca de destacado pasa de línea muda a **banda oliva a sangre** con el texto
dentro, alineado a la derecha, y una estrella en la misma vertical que el punto verde
de "Available".

- **Alineación de la estrella**: la caja del icono mide **exactamente lo que el punto**
  (2.64cqw) y lleva el mismo margen derecho — `calc(5.65cqw + 3.6cqw)`, que es el
  margen de la fila más el relleno de la pastilla. Sus centros coinciden. El svg se
  dibuja mayor y desborda la caja por igual a los dos lados, así que no la descentra.
  Verificado: **0.0px**.
- **Las 36 tarjetas sin banda reciben ese alto como relleno superior**
  (`padding-top: calc(5.83cqw + 6.4cqw)`), o su contenido subiría y la retícula
  dejaría de alinear. Verificado: nombre 69, categoría 141, Available 43 — un solo
  valor en las 40.

**Error propio, corregido:** para pasar el punto verde a la derecha había cambiado el
orden en el marcado **y** aplicado `flex-direction:row-reverse`. Las dos cosas se
anulan y el punto seguía a la izquierda. Peor: lo di por bueno con una comprobación
mal planteada (`dot.left > avail.left+10`), que da verdadero aunque el punto esté a la
izquierda. La comprobación correcta es contra el **centro** de la pastilla.

### La banda no alarga la tarjeta + luz que late (2026-08-31)
**Altura recuperada: 496px**, la misma de antes de la banda. La banda mide **justo el
relleno superior de `.pf-in` (5.83cqw)** y en las destacadas ese relleno se anula:
ocupa el aire que ya existía en vez de sumarse. Se eliminó el relleno compensatorio
que llevaban las otras 36. Verificado: nombre 46, categoría 118, Available 20 — un
solo valor en las 40, y la estrella sigue a 0.0px del punto.

**Luz verde que late** en el punto y en la estrella. Se anima la **opacidad de un
pseudo-elemento con degradado radial**, no `box-shadow`: hay **44 elementos latiendo a
la vez** y la opacidad la resuelve el compositor, mientras que animar `box-shadow`
obliga a repintar en cada cuadro. 2.6s, ida y vuelta.
Con `prefers-reduced-motion` el latido se detiene y el halo queda fijo al 60%.

**El botón de las destacadas caía más abajo.** Causa: `.pf-in{height:100%}` medía la
tarjeta ENTERA, pero en las destacadas arranca debajo de la banda, así que sobresalía
por abajo esos mismos pixeles — la foto crecía y el botón bajaba (y se recortaba).
Cambiado a `flex:1` sobre `.pf-card{display:flex;flex-direction:column}`: ocupa sólo
lo que queda tras la banda. Verificado: botón a **485** y foto a **496** en las
destacadas y en las otras 36, idéntico.

### La luz, de verdad (2026-08-31)
Michelle: *"literalmente una luz, no solo un icono con difuminado"*, y la estrella en
verde como el punto. Rehecho con tres capas, que es lo que separa una luz de una
mancha:
1. **Núcleo encendido** — el punto es un degradado radial con el reflejo desplazado
   (38%/34%) y un `box-shadow` corto y muy brillante pegado a la fuente.
2. **Aureola de dos degradados** — uno casi opaco que cae rápido (46%) y otro amplio y
   tenue (70%). Con uno solo se lee como borrón; con dos, como luz.
3. **La forma iluminada** — la estrella lleva `drop-shadow` doble, que sigue su
   contorno; el halo de detrás sólo pone el ambiente.

La estrella pasa a verde (`--luz-clara:#8ede78`) en vez de blanca.
El latido ahora también escala levemente (.92 -> 1.06), que es lo que da la sensación
de emisión y no de parpadeo de opacidad.
**El tamaño del punto es una variable (`--punto`)** compartida con la caja de la
estrella: si se cambia uno sin el otro, dejan de estar alineados.
Verificado: altura 496, botón 485, estrella a 0.0px del punto.

### Fuera la luz, verde de marca (2026-08-31)
Michelle descartó el resplandor: punto y estrella planos en **`--salvia` (#a6bf85)**,
el verde claro de la marca. Eliminados el `@keyframes`, los halos, el `box-shadow` y
los `drop-shadow`.

**Trampa de alineación:** la caja del icono era más estrecha que la estrella y confiaba
en que el navegador centrara el desbordamiento. **No lo hace de forma fiable** — la
estrella quedaba 3px corrida. Ahora la caja mide lo mismo que el icono y la alineación
la da el relleno del padre, calculado hasta el CENTRO del punto:
`calc(5.65cqw + 3.6cqw + var(--punto)/2 - 2.6cqw)`.
Verificado en las 4 destacadas: **0.0px** en todas.

### Fotos V2 y catálogo re-generado a 720px (2026-08-31)
`Portfolio/V2/` trae 5 reemplazos, todos mejores que los que había: Eggwhite
(600->1080), Instant BCAA (800->1600), L-Carnitine Base (554->680),
Magnesium Bisglycinate (535->1080, archivo "Magnesium Glycinate Powder"),
Polydextrose (550->741).

**Todo el catálogo re-generado a un tope de 720px de ancho** (antes 560): la foto se
muestra a ~310px, así que 720 la deja por encima del 2x de las pantallas Retina.
Las que no llegan se quedan en su ancho nativo, sin ampliar. 40 imágenes, 2.2 MB.
Verificado: las 40 cargan, ninguna falta, altura 496, sin desbordes.

**Ojo con `V2/ Eggwhite Protein Powder.webp`**: el nombre empieza con un espacio y la
primera pasada lo dio por inexistente.

**Siguen por debajo de 720 y se ven grandes** (0-1 variantes), en orden de necesidad:
Bhumi Amla (335), Green Tea (387), Amla (387), Cissus Quadrangularis (400),
Centella Asiatica (447), Berberis Aristata (451), Amla/Emblica (462),
Magnesium Citrate (479), Alkalized Cocoa (480), L-Carnitine (500),
Nano Curcumin (500), Bacopa Monnieri (515).

## About — tres direcciones a comparar (2026-08-31)
Preview: `docs/about/_prev.html`, selector abajo a la derecha.

### Diagnóstico de la página actual
- **Se acaba en 1373px**: dos secciones y fuera. No hay historia, ni prueba, ni cierre.
- **Un solo color en toda la página**: sin bandas ni cambios de fondo, el ojo no tiene
  dónde agarrarse y no se percibe estructura.
- **Jerarquía trabada**: "Who we are" y "We make sourcing…" compiten como dos titulares
  seguidos, y Quality/Reliability/Speed están al mismo cuerpo que el subtitular, así que
  se leen como un tercer titular en vez de como apoyo.
- **"How we work" son cuatro cajas casi vacías**: el texto vive en el reverso del flip,
  así que en reposo hay mucha superficie para un número y un título. Parece sin terminar.
- **No hay llamada a la acción final.**
- **Es la página más pobre del sitio** ahora que la home tiene la O, la franja de valores
  y el carrusel, y el portafolio su sistema de tarjetas.

### Lo que se sacó de las referencias (lógica, no copia)
Etiqueta pequeña + titular grande (Mirage, Armonia) · reglas finas para separar grupos
(Armonia) · imágenes de tamaños distintos para dar ritmo (Mirage) · números como
elemento gráfico (Alora) · cierre con CTA (Armonia, certificación).

### Las tres direcciones
- **A · Editorial** — vídeo a sangre con el titular gigante encima; luego filas de
  etiqueta/contenido separadas por reglas; proceso como lista numerada.
- **B · Estructurada** — título e intro a dos columnas, imagen contenida, rejilla 2x2 de
  bloques etiquetados con reglas, proceso en cuatro columnas, cierre centrado.
- **C · Modular** — banda oliva con la declaración, tres cifras grandes (2 / 40+ / 24h),
  bloques de foto y texto alternados, proceso como línea de tiempo sobre franja salvia.

Las tres añaden lo que falta hoy: cierre con CTA y contenido de proceso visible sin
interacción.

### About A — ajustes del hero y bloque de almacenes (2026-08-31)
Michelle: le gusta la A **hasta "Our promise"**; de ahí abajo se rehace después.

- **Encuadre del vídeo: `scale(2.05)` con origen `44% 66%`.** El mp4 pesa 5,2 MB y no
  hay ffmpeg, así que el recorte se hace con `overflow:hidden` del contenedor en vez de
  recodificar. Hicieron falta tres intentos: a 1.28 se destapaban las puertas 07-10 y
  19 (numeración mal generada); sólo acercando hasta que **los remolques tapan las
  puertas** desaparecen todas. Alto 620 -> 540px y `margin-bottom` para el aire que pidió.
- **La etiqueta pega al titular**: la columna pasa de `1fr` a `minmax(120px,.42fr)`.
- **Tercera columna con los almacenes**, que antes era espacio en blanco. Tres variantes
  con selector: (1) filas con regla fina, (2) tarjeta con la foto del almacén,
  (3) las dos ciudades en grande, en oliva, con punto.
- **CTA "Request a FREE quote"** dentro de Our promise, a petición suya.

### About A — marco, pines y botón (2026-08-31)
- **El vídeo va SIN ampliar** (`transform:none`). Recorta el marco: una franja
  `aspect-ratio:100/23` (331px a 1440) que deja fuera la parte alta de las puertas,
  que es donde está la numeración mal generada. Corrige el enfoque anterior, que
  ampliaba el vídeo al 205%.
- **Pines de ubicación como SVG en línea**, no como el PNG que mandó: se recolorean con
  `color` en una línea y no pierden nitidez en Retina. En las tres variantes.
- **El botón baja a la columna derecha**, bajo el bloque de almacenes.
  `aside{display:flex}` + `margin-top:auto` lo pega al pie de la fila.
  **Y hubo que quitar el margen inferior del último párrafo** (`:last-of-type`): lo
  arrastraba y la fila terminaba 14px más abajo que el texto. Verificado: **0px**.

**Ojo:** el rojo del pin (#e02b1d) no está en la paleta. Hay precedente —la página
actual ya usa pines rojos sobre el vídeo— pero conviene que ella lo confirme.

### About A — dos columnas, almacenes con más peso (2026-08-31)
La etiqueta "Our promise" se apila **sobre** el titular en vez de ocupar su propia
columna. Ese ancho recuperado se lo lleva el bloque de almacenes: pasa del **29% al
43%** de la fila, y con más sitio sube de cuerpo (ciudades a `--t-md` en la variante 1
y a `clamp(30px,3vw,46px)` en la 3). Los dos bloques se leen ahora como pareja.
El botón sigue clavado con "Built on three things" (0px).

Nota: las demás filas conservan la etiqueta en columna propia. Queda desigual respecto
a esta, pero de "What we don't compromise on" hacia abajo se rehace igualmente.

### About A — hueco y entrada escalonada (2026-08-31)
- **Hueco vídeo -> bloques: 126px -> 71px.** Eran 63 de margen del hero más 63 de
  relleno de la fila; sumados se leían como un salto y no como continuidad.
- **Entrada escalonada**, la misma sensación que la banda de valores del home: mismo
  easing `cubic-bezier(.16,.84,.44,1)` y retardos 0 / .14 / .26 / .38s sobre cuatro
  pasos (etiqueta+titular, párrafos, bloque de almacenes, botón). Aquí no hay intro con
  scroll, así que lo dispara un IntersectionObserver.

**Blindaje, importante:** el estado por defecto es **visible**. El punto de partida
(oculto y bajado) sólo se aplica bajo `html.anim`, que pone el propio JS — misma regla
que el intro del home: *nada debe quedar invisible esperando a un script*.
Más una **red de seguridad de 1600ms** que muestra el contenido aunque el observador
no llegue a dispararse. Se vio en el panel: ahí el observador no corre y sin la red el
bloque entero quedaba en blanco.

### About A — los tres pilares suben (2026-08-31)
Quality / Reliability / Speed pasan a estar **justo bajo la frase que los anuncia**, en
la columna izquierda, en tres columnas con **regla fina encima** — el mismo recurso que
separa las filas de esta dirección, para que se lean como apoyo del párrafo y no como
otro titular. Entran con el mismo paso del escalonado que ese párrafo (`r4`).
Eliminada la fila "What we don't compromise on" que los repetía más abajo; la dirección
A queda en dos filas. Las direcciones B y C conservan la suya.

### About · dirección A · hero y CTA (2026-08-31)

**El problema no era el alto del marco, era el momento del vídeo.** `who-trucks.mp4`
dura 5,04 s y la cámara se desplaza. Medido cuadro a cuadro sobre el propio
elemento (`currentTime` + `seeked`, capturas a 0,05 / 1,2 / 2,4 / 3,6 / 4,9 s):

| t | qué se ve |
|---|---|
| 0,05 s | los dos camiones completos con "trade corp. ingredients" |
| 1,2 s | los dos camiones, cámara ya desplazada |
| 2,4 s | sólo el tráiler; entran los muelles |
| 3,6 s | muelles vacíos, sin camiones |
| 4,9 s | muelles vacíos |

Como el `<video loop>` reproducía los 5 s, la mayor parte del tiempo el hero
mostraba muelles vacíos. Ahora se reproduce sólo `[0,05 s – 1,58 s]` a
`playbackRate 0.6`, con **dos copias del vídeo encadenadas por disolvencia**
(`.hv-a` / `.hv-b`): al llegar al final del tramo arranca la otra capa desde el
principio y se cruzan las opacidades en 0,5 s. Sin eso el bucle da un corte seco,
porque el primer y el último cuadro del tramo no coinciden.

**El fundido va en `requestAnimationFrame`, no en `timeupdate`.** `timeupdate`
dispara ~4 veces por segundo; a esa resolución una disolvencia de 0,5 s se ve
escalonada.

**Marca de agua de la IA.** Bajando el `object-position` por debajo del ~88 %
asoma abajo a la derecha la firma del generador del vídeo. `50% 78%` la deja
fuera. Anotado en el CSS para que no se toque sin querer.

**Alto del marco: `aspect-ratio:100/21`, `max-height:460px`** (269 px a 1280).
100/23 tapaba "Built on three things…"; 100/18 cabía pero dejaba a los camiones
sin aire. 100/21 es el punto donde entran los dos camiones enteros y los pilares
siguen sobre la línea de flotación.

**Encuadre vertical `object-position:50% 66%`, con un límite por cada lado.**
Probados 50 / 62 / 66 / 70 / 74 / 78 % contra la referencia de Michelle:

- por **debajo del ~62 %** entran las puertas del muelle, y llevan numeración mal
  generada por la IA (se leen 10, 12, 19);
- por **encima del ~88 %** asoma abajo a la derecha la marca de agua del
  generador del vídeo;
- a **78 %** (primer intento) el tráiler se salía por arriba, sin borde superior.

**66 %** deja el borde superior del tráiler con el edificio detrás, los camiones
completos y algo de piso: la composición de su referencia.

**El CTA sube junto a "Stock ships…" y va centrado en su columna.** Antes llevaba `margin-top:auto` para
alinearse con los pilares de la izquierda (petición del 2026-08-30); se veía bien
a 900 px de alto pero caía fuera de la primera pantalla en viewports más bajos.
Ahora `margin-top:clamp(18px,2.4vh,28px)` y `align-self:center` (antes
`flex-start`), a petición suya.

Medido a 1280×720: hero 269 px (21,0 % del ancho), base del botón 663 px, base de
los pilares 715 px. Todo por encima de la línea de flotación.

**Vídeo del hero: modo `normal`** (tramo 0,05–1,58 s a velocidad real), elegido por
Michelle el 2026-08-31 sobre `lento` (0,6x) y `completo` (los 5 s). El control
`#vid-tog` del preview deja comparar los tres; al aplicar a la web se fija el modo
y se borra el control.

### About · dirección A · motion de los tres pilares (2026-08-31)

Los pilares (Quality / Reliability / Speed) dejan de usar la clase genérica
`.rise r4`: cada variante controla **por separado la regla y la palabra**, que es
lo que permite escalonarlas una detrás de otra. El retardo por columna sale de
`--d` (0 / .13 / .26 s) vía `nth-child`, y cada variante le suma el suyo.

La palabra va envuelta en `.pil-m` (`overflow:hidden`) para la variante cortina.
**`padding-bottom:.18em` con `margin-bottom:-.18em` compensado**: sin eso el
recorte se come la cola de la 'y' de "Quality" incluso en reposo. Verificado:
2,9 px de holgura bajo la caja del texto en las tres variantes.

Se le propusieron tres y **eligió "Línea"** (2026-08-31): la regla se dibuja de
izquierda a derecha (`scaleX 0→1`, origen izquierdo) y la palabra entra detrás con
un fundido de 10 px. Descartadas: "Cortina" (la palabra sube desde debajo de la
regla, recortada por la máscara) y "Escalonado" (regla y palabra juntas, +26 px,
el gesto de la banda de valores del home). El CSS de las dos descartadas se borró;
si alguna vez se quieren, están descritas aquí.

**Disparador propio (`.pillars.in`), no el `.go` de la fila.** Con el disparador
general la animación se consumía antes de que los pilares llegaran a verse, en
cualquier viewport donde no cupieran de entrada. Ahora los observa un
`IntersectionObserver` a `threshold:.5`.

**Trampa en la red de seguridad: `innerHeight` puede ser 0.** La comprobación
"¿está en pantalla?" era `r.top < innerHeight`, y en un panel oculto —o en
cualquier contexto sin layout— `innerHeight` devuelve 0, así que daba siempre
falso y los pilares quedaban invisibles **para siempre**. Ahora hay dos redes:
a los 2,5 s se comprueba con `innerHeight || clientHeight` y se dispara también
si ese valor es 0; a los 6 s se dispara pase lo que pase. Vale más gastar la
animación sin que se vea que perder las tres palabras.

**Botón de repetir (`↻ Repetir pilares`).** Quitar y volver a poner la clase en el
mismo frame no anima: el navegador agrupa los dos cambios. Hay que forzar un
reflow en medio (`void pil.offsetWidth`) y reponerla en un `setTimeout`.

**Los chips del preview pasaron al lado izquierdo.** En la derecha tapaban el CTA
de "Where we ship from", que es justo lo que había que revisar.

### About · dirección A · "How we work" con tarjetas que voltean (2026-08-31)

Michelle pidió recuperar las tarjetas volteables de la página About actual, pero
que **conecten con el lenguaje de movimiento del home**, que es fluido y continuo.
Sustituyen a la lista numerada de la dirección A. Contenido y caras (frente crema
con número + título, reverso oliva con la descripción y los enlaces) se conservan
tal cual de `about/index.html`.

**La fila pasa a ancho completo con la etiqueta encima.** En la columna estrecha
de `.abA-row` (label a la izquierda) cuatro tarjetas quedaban a ~200 px y el
reverso no respiraba. A ancho completo miden 273×364 px a 1280.

Tres variantes para comparar (`#hm-tog`):

| # | nombre | gesto | de dónde sale |
|---|---|---|---|
| 1 | Vecinos | voltea en hover y **los vecinos se apartan y se atenúan** al 58 % | `.ing:hover + .ing` del carrusel de ingredientes del home |
| 2 | Scroll | el giro no lo dispara el ratón: lo va marcando el scroll, cada tarjeta con su tramo | el hero del home (progreso normalizado, easing, sin retroceso) |
| 3 | Cortina | sin 3D: el reverso sube tapando la cara con `clip-path` | el cajón con el que la banda de valores sale del hero |

**La entrada escalonada va en `.fwrap`, no en `.fcard`.** Si el transform de
entrada y el del hover viven en el mismo elemento, el de entrada gana por
especificidad y el hover deja de moverse. Por eso cada tarjeta va envuelta.

**El recorrido de la variante 2 es corto a propósito: `grid.top` de 0.90vh a
0.45vh (324 px a 720 de alto).** Con un recorrido largo el giro de la última
tarjeta terminaba tan abajo que **la página se quedaba sin scroll antes de
completarlo** — esta sección está cerca del final. Comprobada la tabla de giros:
en p=1 las cuatro llegan a 180°, y en el trayecto siempre hay 2–3 volteando a la
vez.

`scrub()` sale sin hacer nada si `vh` es 0, misma precaución que en los pilares.

**El disparador de entrada se factorizó en `enEscena(el, umbral)`**, compartido
por los pilares y por la reja de tarjetas, con las dos redes de seguridad.

**Pista de uso: la primera tarjeta se voltea sola.** Al entrar la sección en
pantalla, la tarjeta 01 gira y vuelve (1,15 s → 2,95 s). Sin eso nadie descubre
que las tarjetas tienen reverso: un volteo en hover no se anuncia solo. El
retardo de 1,15 s es lo que tarda la entrada escalonada en asentarse (0,30 s de
retardo de la cuarta tarjeta + 0,72 s de recorrido); antes se solapaban los dos
gestos. **Se cancela si el visitante ya pasó el ratón por alguna tarjeta**:
voltearle una en la cara mientras la está leyendo es peor que no dar la pista.
No corre en la variante 2 (ahí el scroll ya las voltea todas) ni con
`prefers-reduced-motion`.

Detalle: el listener es `pointerover` y no `pointerenter` — `pointerenter` no
burbujea, así que el ratón sobre una tarjeta nunca llegaría a la reja.

**Bloque de las dos fotos (`.abA-pics`) eliminado** el 2026-08-31 a petición de
Michelle: iba entre "Our promise" y "How we work" y llevaba `warehouse.webp` más
una foto de ingrediente en polvo. Se borró también su CSS. El empalme queda:
pilares → 50 px → filete → 51 px → etiqueta "How we work", el mismo ritmo que el
resto de filas.

**Los controles del preview se recogen en un panel.** Cinco filas de chips fijas
en la esquina se comían media pantalla y tapaban las tarjetas de "How we work" y
el CTA de los almacenes — justo lo que había que revisar. Ahora hay un botón
"Opciones" abajo a la izquierda que despliega el panel (`html.prev-open`). Cerrado
por defecto: el preview se abre limpio. Nada de esto va a la web.

**Textos (2026-08-31):** el botón de cierre del About pasa de "Request a FREE
sample" a **"Quote today"** (sólo en la dirección A; B y C están descartadas). En
Contact, "Sebastian Rodriguez S." → **"Sebastian Rodriguez"** — corrección de
contenido, aplicada directo a `contact/index.html` con copia en `_backups/`,
porque no hay decisión de diseño que comparar en un preview.

Queda una inconsistencia por decidir: el About tiene ahora "Request a FREE quote"
arriba y "Quote today" al cierre. Hay que elegir una sola frase para el botón de
cotización en todo el sitio, o asumir la variación a propósito.

### Recorrido completo de previews (2026-08-31)

Michelle pidió ver el sitio entero con los cambios decididos, de home a contact.
Se armó **enlazando los previews entre sí**, sin tocar ninguna página real: cada
preview vive a la misma profundidad que su original, así que las rutas de los
assets siguen funcionando y sólo hubo que reescribir los `href` de navegación.

| página | archivo | qué trae |
|---|---|---|
| Home | `docs/_prev-ing-v2.html` | banda de valores saliendo del hero (opción 3), scroll muerto corregido, carrusel v2 sin marco |
| Portfolio | `docs/ingredients/_prev.html` | sistema de tarjetas nuevo, 40 productos |
| About | `docs/about/_prev.html` | dirección A completa |
| Contact | `docs/contact/_prev.html` | copia de la real (sólo el nombre corregido) |

48 enlaces reescritos en total. Cada página lleva un distintivo fijo
"PREVIEW · sin aplicar a la web" abajo a la derecha para no confundirlo con el
sitio real, que sigue intacto en `index.html` / `*/index.html`.

**Contact ya usaba "Quote today"** en su botón secundario. O sea que el cambio del
botón de cierre del About no introduce una frase nueva: lo alinea con lo que ya
existía. Queda "Request a FREE sample" / "Request a FREE quote" / "Quote today"
conviviendo, que sigue siendo una decisión pendiente de unificar.

### Home · "Trusted partners" a sangre (2026-08-31)

El carril de testimonios nacía y moría en el margen del CONTENIDO, no en el de la
ventana. Estaba dentro de `.why-inner` (max-width centrado) y encima `.why` lleva
`padding: … var(--pad-x)`.

**Solución: el carril cuelga directamente de `.why` y sólo anula su padding
lateral** (`margin-inline: calc(-1 * var(--pad-x))`). El título se queda dentro de
`.why-inner`. Exacto, porque el borde exterior de `.why` ES el borde de la ventana.

**No se usó `100vw` a propósito.** `100vw` incluye el ancho de la barra de scroll,
así que en Windows el carril se pasa de largo y descentra la sección entera, además
de provocar scroll horizontal. Con márgenes negativos sobre la propia variable de
padding no hay ese riesgo. Verificado: el carril mide exactamente lo mismo que
`.why` y no hay desbordamiento horizontal.

### Portfolio · dos correcciones (2026-08-31)

**La banda de destacado se queda sólo con la estrella.** Se quitó el texto "Star
product". Como la estrella pasa a ser lo único que marca la tarjeta, dejó de ser
`aria-hidden` y ahora lleva `role="img"` con `aria-label="Star product"` más un
`title` — si no, para un lector de pantalla la distinción desaparecía por completo.

**Encuadre por producto para las fotos con fondo oscuro (`SHOT_FIX`).**
`magnesium-oxide.jpg` es un montón blanco sobre negro, y el marco mostraba más
fondo que producto. Medido sobre el píxel (decodificando el JPEG): en 720×385 el
polvo ocupa **x 173..569, y 79..304**; el resto es negro.

Encuadre elegido: `background-size:195% auto; background-position:53% 49%`.
El tamaño va en **% del ANCHO** y no `cover` porque el alto del marco varía con la
retícula (`flex:1` + `grid-auto-rows:1fr`): anclar por ancho es lo único estable.
Comprobado que el recorte cae dentro de la zona de polvo tanto con el marco al
mínimo (46cqw) como cuando la tarjeta crece.

Quedan otras fotos con el mismo problema potencial; `SHOT_FIX` está listo para
añadirlas por slug.

### Correcciones de la auditoría (2026-08-31)

Copia previa en `docs/_backups/preaudit-20260831/`.

**Tokens unificados en las cuatro páginas.** Bloque idéntico: escala tipográfica,
`--content-max:1180px`, `--pad-x:clamp(20px,5vw,72px)`, escala de espacio
`--sp-1..4` toda en `vw`, y cinco derivados de marca.

**El home pasa a la escala grande.** Era un 13–18 % más pequeña. Medido a 1440
después del cambio: cuerpo 21 px (era 18), títulos de tarjeta 27 (era 23),
títulos de sección 50 (era 44,1), menú 17 (era 15).

**`--content-max` en el About.** Era el único fallo puro: el token no existía en
esa página, `max-width:var(--content-max)` se descartaba y el contenedor crecía
sin tope (1920 px en un monitor de 1920). Ahora 1180, igual que el home.

**La jerarquía invertida del portafolio se arregló con un tope de ancho de
tarjeta, NO sacando la tipografía de `cqw`** como decía la auditoría. Al mirarlo
de cerca, el sistema en `cqw` es bueno: hace de la tarjeta una pieza proporcional
y está calibrado con cuidado (el `min-height` del nombre reserva exactamente dos
líneas, la estrella y el punto comparten centro por aritmética de `cqw`...).
El fallo no era `cqw`, era que **nada limitaba el ancho de la tarjeta**: en una
columna llegaba a 504 px y el nombre salía a 40,4 px contra los 30 del titular.

`repeat(auto-fill,minmax(300px,340px))` + `justify-content:center`. `auto-fill`
cuenta columnas con el mínimo, así que el número de columnas no cambia; sólo deja
de estirarlas. Verificado a 1440 y a 560: tarjeta 340 px en ambos, nombre 27,3 px,
titular 50 y 30 → **el titular siempre gana**. Alturas de tarjeta idénticas (503).

**Texto pequeño del portafolio por encima del mínimo.** Con la tarjeta a tope:
categoría, «Available» y «Product info» 11,9–12,6 → 14,1 px; grado/descripción
13,9 → 15; «Tech Specs» 9,4 → 13,1. La geometría que los contiene creció con
ellos (`.pf-avail` y `.pf-top` de 6,26 a 7,2cqw; `.pf-cat` de 5,6 a 6,4cqw).

**Contraste.** Un solo `--gris:#6f6252` (5,6:1) reemplaza a `#8a7961` (4,21:1),
`#9a9075` (3,17:1) y `#b3ab98` (2,28:1). Los tres fallaban AA y eran casi el
mismo color.

**Pines:** pasan a `--pin:#b0392a`, el token que el propio About ya definía y no
usaba (pintaba con `#e02b1d`). Borrados `--pin-red` y `--pin-red-on-dark`.

**Ritmo vertical** de `vh` a la escala `--sp-*` en `vw`. A 1440 — home: 80/28 y
120/80; About: 28/80, 80/80, 80/120; portafolio 80/80; Contact 80/72.

**Paleta.** `--salvia-deep` borrado (0 usos desde el carrusel v2 sin marco).
Literales sustituidos por tokens en el portafolio (`#495430`, `#312210`,
`#302210`, `#312211`, `#354d1f`, `#e7dec7`, y las dos tramas beige) y en el home.

**Corrección a la auditoría:** decía que el About tenía «ocho separaciones
distintas». Ocho hay en el archivo, pero cinco son de las direcciones B y C, que
están descartadas. La dirección A tenía tres. El hallazgo era real pero estaba
inflado.

**Excepción consciente: el carrusel del home no va por token.** `.ing-name`,
`.ing-feat` y `.ing-explore` llevan valores literales del SVG v2 que entregó
Michelle. Llevarlos a la escala rompería la fidelidad con su archivo de diseño.
Anotado en el CSS; pendiente de su decisión.

### Ajustes sobre las correcciones de la auditoría (2026-08-31, tarde)

**La banda de valores del home vuelve a sus tamaños anteriores.** La escala nueva
la agrandó (título 28,9 → 34, texto 18 → 21) y Michelle la quiere como estaba: es
una pieza calibrada a ojo contra el hero del que sale, no texto corriente. Los
valores de la escala vieja quedan congelados en esa regla, con nota.

**Columna del grado del portafolio: 26,8 % → 33 %, texto 15 → 14 px.**
«1.5% Withanolides» se salía de su celda. **Regla para futuras tarjetas: el ancho
lo manda la PALABRA MÁS LARGA del catálogo, porque no se puede partir.** Hoy son
«Guggulsterones» y «Quadrangularis» (14 caracteres), que a 14 px piden 98 px
medidos con canvas; la columna da 104 útiles. Con el 26,8 % anterior había 67 y
«Withanolides» ya pedía 87. Verificado: 0 celdas desbordadas en las 40 tarjetas.

**El vídeo del About vuelve al clip original completo.** Michelle aclaró que al
elegir «normal» se refería al vídeo sin cortar; el modo `normal` que yo había
puesto seguía siendo el tramo recortado, sólo que a velocidad real. Ahora el
modo por defecto es `completo` (los 5 s enteros). Se conserva el encadenado entre
las dos capas: sin él el bucle da un corte seco al volver al principio.

**«How we work»: fuera el filete superior y `padding-top:0`.** El bloque sube a
donde estaba la línea. El hueco entre los pilares y la etiqueta lo da ahora sólo
el relleno inferior de la fila anterior: 80 px (antes 101 con la línea en medio).

### Máscaras de los ingredientes — la transparencia sí sobrevivió

Comprobado decodificando los cinco PNG de máscara: todas tienen grises
intermedios, así que la sombra suave que Michelle añadió en Illustrator está
intacta. Reparto de niveles (negro / gris / blanco): cocoa 50/48/0,
collagen 53/46/0, creatine 45/34/19, citrate 40/13/45, oxide 58/24/17.

**Pero el collagen tenía un techo de opacidad: su máximo era 238, o sea 93 %.**
La imagen entera se veía un punto lavada respecto a las otras cuatro. Viene de la
cuantización a 16 niveles: para esa foto el escalón más alto cayó en 238 y no en
255. Corregido reescalando la máscara al rango completo — sólo escala, no cambia
la FORMA, así que la sombra se conserva igual. Copia en
`assets/ing-collagen-mask-pre255.bak`.

**−3 % de opacidad a Cocoa y Bovine Collagen** (2026-08-31, petición de Michelle).
Al principio lo entendí al revés y apliqué +3 %; ella quería **mermarla**, que se
vean más transparentes. Rehecho desde el estado previo (`*.pre3pct`) con cada
píxel ×0.97. Opacidad media: cocoa 40,7 → 39,5 %; collagen 40,6 → 39,3 %.
Máximo 255 → 247 en las dos.

**Al medirlo salió que el cocoa tiene el MISMO techo que tenía el collagen.**
El 40,6 % de su imagen está en alfa 245 = 96 %, y sólo el 0,6 % llega a 255. O
sea: el cuerpo del montón nunca es del todo opaco. Antes del +3 % la meseta
estaba en 238 (93 %), exactamente el mismo valor que tenía el collagen. Es el
mismo defecto de cuantización a 16 niveles.

De referencia, la creatina —que está sana— tiene el 19,9 % de la imagen en 255 y
un degradado repartido por debajo.

Queda anotado pero **sin acción**: al ir en dirección contraria —hacia más
transparencia— el techo del cocoa deja de ser un problema práctico. Sigue siendo
una inconsistencia técnica entre imágenes (el cocoa topa antes que las otras
cuatro) por si algún día se quiere volver a subir la densidad.

## Wix — plan de Michelle (2026-08-31)

Decide **embeber en secciones de Wix**, con el HTML servido desde GitHub:

- **Menú:** nativo de Wix. Fuera `.site-nav` de todos los embeds.
- **Home, en 3 secciones:** (1) logo creciendo + hero + los 4 valores;
  (2) «Most requested ingredients» hasta «Why buyers choose TradeCorp»;
  (3) «Trusted partners».
- **Ingredients:** sin el título (va en Wix). Los PDF de especificaciones se
  guardan en carpetas de Wix → resuelven los 48 «Tech Specs» muertos.
- **About:** todo «Who we are» menos «Tell us what you need», que va en Wix.
- **Contact:** sin título ni botones, van en Wix.

### Enlaces desde un embed hacia Wix — cómo funciona

Un `<a>` normal dentro de un iframe abre el destino **dentro del iframe**: se
vería el sitio de Wix anidado en la caja. Para navegar la página entera hace
falta **`target="_top"`**; para abrir un PDF en pestaña nueva, `target="_blank"`.

**Sin verificar:** si el iframe de Wix lleva `sandbox` sin `allow-top-navigation`,
`target="_top"` no hace nada y falla en silencio. Alternativa entonces:
`postMessage` al padre y que Velo haga la navegación (el `messageDriver` ya
existe, tampoco verificado). Construido `docs/embed/_test-wix.html` para medirlo
dentro de su Wix real: sandbox, scroll del padre, qué vale `100vh`, si llegan
mensajes de Velo, y las dos pruebas de navegación.

### Dos consecuencias que el plan NO resuelve

**1. La sección 1 del home sigue rota.** El intro es un recorrido de `250vh`;
dentro de un iframe eso son 2,5 veces el alto de la caja, así que la barra de
scroll interna no desaparece (medido el 2026-08-22), y el scroll del padre no
mueve el embed. Partir el home en tres no cambia nada: es el mismo problema en
una caja más pequeña. **Salida: que la sección 1 se reproduzca sola al cargar**
en vez de con el scroll. Se pierde el gesto de «desplázate para revelar».

**2. Todas las animaciones de entrada se disparan al cargar.** Dentro de un
iframe, `IntersectionObserver` mide contra el viewport DEL IFRAME, que no se
mueve cuando el visitante hace scroll en Wix. Afecta a los pilares del About, las
tarjetas de «How we work», la banda de valores y el desplegado de las tarjetas
«Why». Sólo se salva si Wix carga el embed al acercarse — eso lo mide la prueba.

### Intro del home: reproducción automática (2026-08-31)

Decisión de Michelle: **el intro corre solo al cargar**; el resto de la página
sigue guiado por scroll. Es lo que permite meterlo en una sección de Wix.

`timeDriver()` alimenta `applyFrame` con un progreso **lineal en el tiempo**,
`AUTO_MS=3600`. Lineal a propósito: `applyFrame` ya reparte sus propias curvas
por tramos (`seg` + `easeInOutCubic`), así que suavizar aquí encima sería
suavizar dos veces y el intro saldría pastoso en las puntas. `AUTO_MS` es el
único número que hay que tocar para cambiar la velocidad.

**`html.intro-auto` se pone desde el `<head>`, antes del primer pintado**, y deja
el track en 100vh. Si se pusiera al arrancar el motor, la página mediría 2,5
pantallas durante unos frames y asomaría una barra de scroll. Medido a 1440×900:
track 900 px (antes 2250) — desaparece el scroll muerto del intro.

`?driver=scroll` devuelve el motor anterior para comparar. `?intro=1` lo obliga a
repetirse (si no corre una vez por sesión).

Verificado por estilos calculados, no visualmente: en p=0 el logo está a opacidad
1 y card/band a 0; en p=1 al revés. El panel de preview suspende
`requestAnimationFrame` (0 fotogramas en 600 ms), así que la animación no corre
ahí — sí en un navegador normal.

### Dos fallos del carrusel — misma causa: `:focus-within`

**Ingredientes:** al hacer clic en una tarjeta el foco se quedaba dentro y el
auto-scroll no arrancaba hasta hacer clic fuera. **Trusted partners:** igual, el
carril lleva `tabindex` y un clic lo dejaba parado.

La pausa por foco existe para el teclado —que no se mueva mientras alguien
tabula— pero `:focus-within` también se activa con el ratón. Cambiado a
`:focus-visible`, que sólo se activa con teclado. Verificado tras un clic
simulado: `:focus-within` true, `:focus-visible` false → ya no pausa.

**De paso, otra forma de quedarse colgado:** el hover del carrusel se llevaba en
una bandera con `pointerenter`/`pointerleave`. Durante un arrastre hay captura de
puntero y el `pointerleave` puede no llegar nunca: la bandera se quedaba en true
y no arrancaba más. Ahora se lee `car.matches(':hover')` en cada frame, que se
autocorrige.

**Pendiente de decidir:** los botones del hero del home siguen diciendo «Request
a FREE sample» y «Explore Portfolio». No entraron en la unificación de textos
(que cubrió About, Contact y portafolio). Si el formulario de muestras es una
tercera acción distinta de cotización e ingrediente, hay que nombrarla también.

**El ingrediente ya no se queda abierto al hacer clic** (2026-08-31). Era el mismo
`:focus-within` que congelaba el auto-scroll, pero en la parte visual: la tarjeta
lleva `tabindex="0"`, así que un clic la enfocaba y la foto grande se quedaba
puesta hasta hacer clic en otro sitio. Cambiado a `:focus-visible` más
`:has(:focus-visible)` —este último recoge el caso de que el foco caiga en el
enlace «Explore» que va dentro—.

**Con ratón sólo se sostiene mientras el puntero está encima**, que es lo pedido.

**En táctil se recupera `:focus-within`, dentro de `@media (hover:none)`.** Sin
hover, el toque es la única forma de abrir un ingrediente y el navegador no
aplica `:focus-visible` al tocar: sin esa excepción la foto no se abriría nunca
en móvil.

Verificado el clic de ratón: tras el clic `:focus-within` sigue en true —lo que
antes lo abría— y la foto se queda en opacidad 0. **No verificado el camino de
teclado:** el panel de preview no entrega las pulsaciones de Tab a la página, así
que no pude comprobar que al tabular la tarjeta se abra. Depende del
comportamiento estándar de `:focus-visible`; conviene que Michelle lo pruebe con
Tab en su navegador.

### Nombres: «Portfolio» → «Ingredients» (2026-08-31)

La misma página se llamaba de cuatro formas: menú «Ingredients», título del
navegador «Portfolio», H1 «Our ingredients», botón del hero «Explore Portfolio»,
y en el About «Browse our portfolio». Unificado en **ingredients**:

- botón del hero → **«Explore our ingredients»** (308 y 305 px los dos botones,
  siguen en una línea)
- `<title>` → **«Ingredients — TradeCorp»**
- texto del About → «Browse our **ingredients**»
- menú y H1 se quedan como estaban («Ingredients» / «Our ingredients»)

**Por qué «ingredients» y no «portfolio»:** en B2B «portfolio» es ambiguo —puede
ser inversiones, clientes o productos—; la marca se llama literalmente «trade
corp. **ingredients**» (lo dicen los camiones); y sobre todo, **un comprador
busca «bulk collagen supplier», no «portfolio»**. Con el plan de embeber en Wix
esto pesa el doble: el contenido del iframe no se indexa, así que el menú y los
títulos que quedan en Wix son casi el único texto que Google va a leer.

### Figurita del carrusel: mancha negra en el óxido de magnesio

Michelle señaló una mancha oscura en la píldora sobre el título. Medido: la
ventana centrada a 240% atrapa un píxel de luminancia **10 —negro—** en el borde
del montón (en 242,502 de la foto de 720×720), y sobre un polvo BLANCO eso canta.

Nuevo token **`--fig-zoom`**, 240% por defecto. `.img-4` (óxido de magnesio) pasa
a **300%**: la ventana es más pequeña, la mancha queda fuera y el píxel más oscuro
sube a 110 —gris medio, invisible a 65 px—. Barrido completo: 240%→0,73% de
mancha, 280%→0,17%, 300%→0,12%.

**No se tocó el resto.** Al medirlos, el cacao sale 99,67% «oscuro» — pero es que
el cacao ES marrón. La métrica sólo significa algo en los polvos blancos.

**Descartado mover el encuadre en vez del zoom:** buscando la mejor posición a
240% lo máximo que se consigue es bajar la mancha de 0,73% a 0,59%, y descentra
la figura. Y buscando «la ventana más clara» sin restricciones el algoritmo
elegía una esquina del fondo crema, sin polvo — por eso la búsqueda exige
textura mínima.

## Fichas técnicas — inventario (2026-08-31)

Michelle tiene 34 PDF en `~/Desktop/Tradecorp/Technical Sheets`. Cruzados contra
las 48 variantes del catálogo **por nombre botánico y porcentaje** — el cruce por
palabras del nombre comercial daba falsos positivos graves (asignaba la ficha de
Amla a Bhumi Amla, que es *Phyllanthus niruri*, otra planta).

**35 de 48 variantes tienen ficha.** Las 13 que no:

| sin ficha | por qué |
|---|---|
| BCAA, L-Arginina, L-Citrulina, L-Glutamina, L-Carnitina, L-Carnitine Base | aminoácidos |
| Citrato de potasio, los 3 magnesios | minerales |
| Creatina (3 mallas), Clara de huevo, Cacao, Polidextrosa | otros |
| Bhumi Amla | *Phyllanthus niruri*, no comparte ficha con el Amla |

**El patrón: todo lo botánico está cubierto, nada de lo sintético o mineral.**
Vienen de proveedores distintos.

**Dos correcciones al cruce automático**, hechas a mano: el colágeno SÍ tiene sus
dos fichas (Granular e Instant, una por variante) y la Moringa al 25% tiene la
suya propia — el algoritmo le había puesto la del 10%.

**4 PDF de productos que NO están en el catálogo:** Mucuna Pruriens, Andrographis
(Kalmegh), Gymnema Sylvestre y Lagerstroemia (Banaba). Son productos que podría
añadir. Sobran además dos blends (FT-CAL-607 Red, FT-CAL-608 Green) y un
"Hydrolyzed Collagen Rev32" que parece una revisión anterior.

**La ficha se enlaza por VARIANTE, no por producto:** colágeno y moringa tienen
un PDF distinto por variante, mientras que Ashwagandha, Karela, Arjuna, Tribulus,
Triphala, Shilajit, Bromelain y Guggul comparten una sola ficha entre sus dos
variantes.

## Embeds para Wix — construcción (2026-08-31)

**Se generan, no se editan.** `docs/embed/build.py` los produce a partir de los
previews: `python3 docs/embed/build.py [nombre]`. Así un cambio en un preview se
propaga con un comando y no hay que replicarlo seis veces a mano.

De cada preview quita el menú (lo pone Wix), el andamiaje del preview y las
secciones que van en otra caja o directamente en Wix.

**La fuente Avenir sale del HTML.** Iba incrustada en base64: 70 KB en CADA
archivo, y con seis embeds serían 420 KB descargados seis veces. Extraída a
`assets/avenir-light.otf` (52 KB reales — el data URI la declaraba como `ttf`
pero la firma es `OTTO`, o sea OpenType CFF). Ahora se descarga una vez y se
cachea. Sin `fonttools` en la máquina no se pudo pasar a WOFF2, que la dejaría
en la mitad.

**Rutas de assets recalculadas por origen**, porque el embed vive en `docs/embed/`
y no donde vivía su preview:
- home (`docs/`): `assets/` → `../assets/`
- ingredients y contact: ya usaban `../assets/`, misma profundidad, no cambian
- **about usa DOS raíces**: `../assets/` (compartida) y `assets/` (la suya, en
  `about/assets/`). Sólo se toca la segunda → `../about/assets/`. El regex lleva
  un `(?<!\.\./)` para no romper la primera.

**Trampa encontrada: los conmutadores se borran del HTML pero su script no.**
Tres `getElementById(...).addEventListener(...)` apuntaban a botones ya
inexistentes → `TypeError`, y el script moría ahí sin llegar a arrancar las
animaciones de los pilares y las tarjetas. Se eliminan esas tres sentencias.
Las que usan `querySelectorAll` son inofensivas: una lista vacía no falla.

| embed | antes | ahora | verificado |
|---|---|---|---|
| contact.html | 136 KB | 69 KB | sin menú, sin título ni botones, 2 tarjetas |
| ingredients.html | 106 KB | 37 KB | sin H1, 40 tarjetas, buscador y 7 filtros |
| about.html | 125 KB | 47 KB | sólo dirección A, sin cierre, 4 tarjetas, 3 pilares |

Los tres sin errores de consola. Falta partir el home en sus tres secciones.

**Las fichas técnicas «actualizadas» son las mismas.** Michelle las volvió a
descargar a `Technical Sheets/Actualizado`: 40 archivos, pero por SHA-256 son
**34 únicos — idénticos a los de la carpeta original**. Los 6 de más son
duplicados exactos con sufijo de hash (Garcinia, Tulsi, Arjuna, Moringa 25%,
Gymnema, Lagerstroemia). Ni un PDF nuevo, ni uno perdido: **el hueco de 13
variantes sin ficha sigue igual**.

### Los PDF son COA vencidos, no fichas técnicas (2026-08-31)

Extraído el texto de los 34: **24 son «Certificate of Analysis»** y **los 24
caducan en Dec-2025** — vencidos hace nueve meses. Fabricación: 22 en Jan-2023,
2 en Jan-2022. Llevan número de lote.

Sólo 3 son documento publicable de verdad: las dos «Technical Specifications» del
colágeno (Granular e Instant) y el «Rev32». Los otros 7 tienen código de lote en
el nombre, así que probablemente también son COA con otra maqueta.

**Un COA es por lote y va CON el pedido; lo que se publica en abierto es la ficha
técnica.** Publicar un COA caducado de un lote de hace tres años transmite lo
contrario de lo que busca la marca.

**Pero el COA sirve de fuente:** su columna «Specifications» ES la especificación
del producto, sin lote ni caducidad. De ahí salen, con formato consistente y
extraíbles: nombre botánico, **parte de la planta** (Root / Whole plant / Aerial
Part / Fruit), estandarización y método, descripción y color, malla,
solubilidad, pérdida por secado, cenizas, y el cumplimiento USP de pesticidas,
metales pesados y disolventes residuales.

### Qué debería resumir «Product info» — propuesta

Ahí leen tres perfiles: el formulador (¿me sirve?), compras (¿cuándo y cuánto?) y
calidad (¿lo justifico ante un auditor?). Mismos campos y mismo orden en los 40:
para quien compara cinco proveedores, poder comparar pesa más que la profundidad.

1. **Qué es** — botánico · parte de la planta · estandarización y método
2. **Ficha física** — descripción y color · malla · solubilidad · secado · cenizas
3. **Soporte/excipiente** — lo primero que pregunta quien busca *clean label*
4. **Cumplimiento** — pesticidas, metales pesados, disolventes: conforme USP
5. **Certificados** — Kosher · Halal · Non-GMO · Vegano · Orgánico
6. **Logística** — presentación · vida útil · almacenamiento · **stock FL y GA · sin mínimos**
7. **Aplicaciones** — cápsulas · gomitas · bebidas · deportiva

Los bloques 1, 2 y 4 se extraen de los COA (26 botánicos). Los bloques 3, 5, 6 y
7 **no están en ningún documento**: los tiene que aportar Michelle o el proveedor.

**La parte de la planta no es un detalle:** ashwagandha de raíz y de hoja son
cosas distintas y en varios mercados es un asunto regulatorio. Los compradores
filtran por eso.

**Decisión (2026-08-31): se publican los COA que hay** mientras el proveedor
manda documentación actualizada. El botón pasa de «Tech Specs» a **«Sample COA»**,
y el `aria-label` a «Sample certificate of analysis for <producto>».

**La palabra que hace el trabajo es «Sample», no «COA».** Lo que vuelve aceptable
un documento de 2023 es que quede claro que es **un ejemplo** y no el certificado
del lote que recibirá el comprador. Con «Sample» se lee como referencia; sin ella,
como descuido.

Verificado: 48 enlaces, texto en dos líneas, ninguno desborda su celda.

**Pendiente cuando lleguen los documentos nuevos:** sustituir los PDF y decidir si
el botón vuelve a decir «Tech Specs» —sólo si lo que mandan es ficha técnica y no
otro COA—.

### Datos de «Product info» extraídos de los COA (2026-08-31)

`docs/data/extraer.py` → `docs/data/coa.json`. Se extrae la columna
**Specifications**, no la de **Result**: la especificación es lo estable, el
resultado es del lote y caduca con él.

24 COA, 13 campos. Cobertura: descripción, malla, metales y disolventes 24/24;
ensayo 24/24; densidad y secado 23/24; parte de la planta y cenizas 22/24;
botánico 21/24; solubilidad 19/24.

**El ensayo venía en diez maquetas distintas** («Content of X» / «X Content», con
y sin método entre paréntesis, «ByGravimetric» pegado, «NLT» o «Not less than»,
y unidades % o GDU en la bromelina). Un patrón por formato no escalaba; se
generalizó a uno solo y pasó de 13/24 a 24/24.

**Sorpresa útil:** los COA traen **densidad aparente** (`Tapped bulk density`),
que es de lo que más miran los formuladores — determina el llenado de cápsula y
el tamaño del comprimido. No estaba en mi lista inicial.

### ERROR EN UN DOCUMENTO DEL PROVEEDOR

`PHYLLANTHUS EMBLICA (AMLA) DRY EXTRACT.pdf` **se contradice a sí mismo**:

| campo | dice |
|---|---|
| Product Name | «PHYLLANTHUS EMBLICA (AMLA) DRY EXTRACT — **30% BY TITRATION**» |
| Botanical name | ***Phyllanthus niruri*** — que es Bhumi Amla, otra planta |
| Plant Part | Whole Plant (el Amla es el fruto) |
| Standardization | **Bitters** (el Amla se estandariza por taninos) |
| Chemical Assay | **Bitters 5%** — el título promete 30% |

Es la ficha del **Bhumi Amla** con el nombre del **Amla**. Consecuencias: el Amla
se queda sin ficha correcta, y la del Bhumi Amla está archivada con el nombre
equivocado. Hay que reclamárselo al proveedor.

Detectado porque el dato extraído no cuadraba con el catálogo (Amla = 30% taninos,
Bhumi Amla = 5% bitters) — no por revisar los PDF a mano.

### «Product info»: panel desplegable bajo la fila (2026-08-31)

**Descartados el modal y la cajita sobre la foto.** La cajita no cabe: el área de
la foto mide ~156 px y los campos son once. Y el modal **se rompe dentro de Wix**:
`position:fixed` se ancla al IFRAME, no a la ventana, así que en un embed de
varios miles de píxeles de alto un modal «centrado» se dibuja fuera de la vista
de quien mira la mitad de la lista.

**Primera versión: panel desplegable bajo la fila. Descartada** — Michelle:
«queda abajo y hay que hacer scroll para verlo». Cierto: si la tarjeta está arriba
de la pantalla, el panel nace fuera de la vista.

**Versión final: pop-up anclado a la retícula con `position:absolute`.** Flota
sobre las tarjetas con sombra y velo, y **se abre a la altura de la tarjeta
pulsada**, así que nace donde el ojo ya está mirando.

**Por qué `absolute` y no `fixed`, ni `scrollIntoView`:** dentro de un iframe
`fixed` se ancla al iframe entero — la reja mide **8.637 px** de alto, medido —
así que un pop-up «centrado en pantalla» se dibujaría a 4.300 px de donde está
mirando el visitante. Y `scrollIntoView` haría scroll **del iframe**, no de la
página de Wix, que es la que de verdad se desplaza. Anclar a la reja es lo único
que sobrevive al embed.

Si la tarjeta está en las últimas filas y el pop-up se saldría por abajo, se sube
lo justo para caber. Verificado con la tarjeta 40: cabe sin ajuste.

Cierra con el botón, con clic en el velo y con Escape. Verificado: los tres
retiran panel y velo del DOM.

**La animación de apertura no usa `requestAnimationFrame`.** No corre en pestañas
de fondo ni en algunos contenedores, y ahí el panel se quedaba sin abrir. Se
fuerza el reflujo leyendo `offsetHeight`, que es lo único que la transición
necesita para tener valor de partida. Se anima `grid-template-rows` de `0fr` a
`1fr` — la forma de animar a altura automática sin medir en JS.

**19 de 40 productos con ficha.** Tabla explícita producto→PDF en
`docs/data/specs.json`, escrita a mano: para algo que se publica, una tabla
legible vale más que un emparejador difuso (el mío falló en Bacopa por una errata
del proveedor, «Baccopa», y en Ashwagandha porque su COA no trae el binomio).

**Fuera a propósito:** Amla y Bhumi Amla, porque su único PDF se contradice a sí
mismo. No se publica dato salido de un documento incoherente. Y Shatavari,
Amla/Emblica, Moringa y Nano Curcumin, cuyos PDF traen otra maqueta que el
extractor todavía no lee.

**El ensayo NO sale del panel a propósito:** el COA certifica UNA graduación y
varios productos tienen dos (Ashwagandha 1,5% y 20% comparten ficha del 1,5%).
Cada variante ya muestra la suya en la tabla de la tarjeta. Publicar el ensayo del
COA a nivel de producto habría afirmado que el 20% cumple una especificación del
1,5%.

Los 21 productos sin ficha muestran «Full technical data sheet available on
request» con enlace a Contact — mejor que el enlace muerto que había.

**Bug corregido:** `'<i>'+(d.botanico||'')+'</i>'.replace('<i></i>','')` — el
`.replace` se aplicaba SOLO a `'</i>'` por precedencia de operadores, así que sin
dato producía `<i></i>`, que no es cadena vacía y pintaba una fila en blanco.

### Descripciones para los 21 productos sin ficha (2026-08-31)

`docs/data/descripciones.py`. Verificado: **40 productos = 19 con ficha + 21 con
descripción + 0 sin nada.**

**Criterio: descripción de MATERIAL, no de beneficios.** Identidad química o
botánica + comportamiento físico + aplicaciones típicas. Nunca claims de salud:
un proveedor B2B que escribe «apoya la inmunidad» entra en terreno regulado
(FDA/FTC), y además el comprador ya sabe para qué sirve el ingrediente — lo que
necesita saber es qué material es.

**Tampoco se afirma nada del proceso del proveedor** —método de extracción,
origen, parte de la planta— donde no está verificado. Eso sale de la ficha. Por
eso los seis botánicos llevan sólo especie y estandarización.

Ejemplos de dato que sí decide una compra:
- **L-Carnitine:** «fuertemente higroscópica — necesita manipulación con humedad
  controlada y envase con barrera». Es la clase de cosa que un comprador necesita
  saber antes de pedirla.
- **Creatine:** para qué sirve cada malla — 80 para comprimidos y cápsulas, 200
  para polvos, 500 (micronizada) para dispersión en líquidos.
- **Magnesium Oxide:** el mayor magnesio elemental por gramo (~60%) y
  prácticamente insoluble; **Bisglycinate:** neutro de sabor pero menos magnesio
  por gramo, así que la misma dosis ocupa más volumen.

**Hallazgo:** *Emblica officinalis* y *Phyllanthus emblica* **son la misma
especie** — sinónimos. Así que «Amla» (30% taninos) y «Amla / Emblica» (45%) son
el mismo botánico en dos graduaciones, catalogados como dos productos con nombres
botánicos distintos. Anotado en la descripción; **valdría la pena unificarlos en
un producto con dos variantes**. Distinto de «Bhumi Amla», que sí es otra especie
(*P. niruri*) y lleva la advertencia explícita.

**Amla unificado en una tarjeta** (2026-08-31, decisión de Michelle). De 40
productos a **39**: «Amla» (30% taninos) y «Amla / Emblica» (45%) pasan a ser un
solo producto con dos graduaciones, como Ashwagandha o Guggul.

- Ambas variantes usan **<i>Phyllanthus emblica</i>**, el nombre aceptado.
  <i>Emblica officinalis</i> es el sinónimo. La descripción avisa de que **la
  ficha del 45% que manda el proveedor va titulada con el sinónimo**, para que
  quien cruce documentos no crea que son materiales distintos.
- De las dos fotos se queda `amla-emblica.jpg`: 462×247 contra 387×207.
- Bhumi Amla (<i>P. niruri</i>) sigue aparte — es otra especie.

Verificado: 39 productos, 19 con ficha, 20 con descripción, ninguno sin nada y
ninguna descripción huérfana.

**Nota de operación: el servidor de preview se cayó** y al reiniciarlo hay que
pasarle el puerto y la carpeta — `python3 serve.py 8094 docs` —, porque por
defecto arranca en 8090.

### El home partido en tres embeds (2026-08-31)

Michelle ya creó el menú en Wix con sus botones, así que los seis embeds van sin
`.site-nav`.

| embed | contenido | peso | alto a 1440 |
|---|---|---|---|
| `home-1.html` | logo creciendo + hero + los 4 valores | 84 KB | 900 px (100vh) |
| `home-2.html` | most requested ingredients + why buyers choose | **290 KB** | 1.371 px |
| `home-3.html` | trusted partners | 39 KB | 607 px |
| `ingredients.html` | catálogo, sin título | 55 KB | 8.308 px |
| `about.html` | who we are, sin el cierre | 46 KB | 1.268 px |
| `contact.html` | tarjetas, sin título ni botones | 67 KB | 597 px |

**El corte de «why»:** la sección contiene el bloque de tarjetas Y el carril de
testimonios (el carril cuelga de `.why` desde que se hizo a sangre). En home-2 se
quitan `.tp` y `.tp-marquee`; en home-3 sobrevive sólo eso y se quitan la curva,
el título y la reja.

**Trampa: un guion sin su sección no falla en silencio.** El del intro empieza con
`document.getElementById('stage')` y sigue con `zoom.querySelector(...)`; sin el
hero eso lanza `TypeError` en la primera línea y **el archivo entero se queda sin
ejecutar** — en home-2 eso mataba también el carrusel de ingredientes. Se añadió
`sin_guion(html, marcador)` al generador, que borra el `<script>` completo que
contiene un marcador. home-2 y home-3 pierden el guion del intro; home-3 pierde
además el del scrub de «why», que sin tarjetas no pinta nada y encima dejaría el
fondo a medio camino entre crema y salvia. Verificado: home-3 en `rgb(166,191,133)`
exacto, que es `--salvia`.

**Lo que se pierde del movimiento dentro de Wix:** en home-2 la sección «Why»
está guiada por scroll, y dentro de un iframe el scroll de la página padre no
llega. No se rompe —la única lectura inicial calcula «todo revelado» y las
tarjetas aparecen abiertas— pero el despliegue no se ve. Si Michelle lo quiere,
habría que pasarlo a reproducción automática como el intro.

**home-2 pesa 290 KB**, cinco veces más que el siguiente: lleva las fotos de las
tarjetas «Why» y del carrusel en base64. Candidato a sacarlas a archivos como se
hizo con la fuente.

### El alto del iframe: por qué hace falta Velo (2026-08-31)

El elemento de Wix es una caja de **tamaño fijo** — no crece con su contenido.
Medidos los seis embeds a 1440 y a 390 px:

| embed | 1440 px | 390 px | factor |
|---|---|---|---|
| home-1 | 900 | 844 | 0,9× |
| home-2 | 1.371 | 1.914 | 1,4× |
| home-3 | 607 | 476 | 0,8× |
| about | 1.268 | 1.860 | 1,5× |
| contact | 597 | 916 | 1,5× |
| **ingredients** | **8.308** | **24.735** | **3,0×** |

Un alto fijo no puede servir a los dos. Con altos por breakpoint (Wix Studio lo
permite sin código) se cubren cinco de los seis.

**Pero el catálogo no se arregla así**, y es el argumento decisivo: **tiene
buscador y filtros que cambian el alto en caliente**. Filtrar a «Minerals» lo deja
en ~2.000 px dentro de un iframe de 24.735 → **22.000 px de hueco en blanco**.
Ningún valor fijo lo resuelve, porque el alto correcto depende de lo que el
visitante acabe de escribir.

**Salida: el embed mide su propio alto y se lo manda al padre por `postMessage`;
Velo escucha y redimensiona el iframe.** Hay que escribir las dos mitades. La
misma tubería sirve de plan B para `target="_top"` si Wix lo bloquea, así que se
paga una vez y resuelve los dos problemas.

### PRUEBA DE WIX: `target="_top"` FUNCIONA (2026-08-31)

Medido en el sitio publicado de Michelle, modo «Dirección web del sitio» apuntando
a `michellealjure.github.io/TRADECORP2/embed/_test-wix.html`. El botón sacó del
embed y cargó tcorpi.com como página completa.

**Consecuencia: los ~140 enlaces se atan con `target="_top"` y URLs absolutas de
Wix. No hace falta Velo para la navegación.** Queda descartado el plan
`postMessage` + `messageDriver` para este fin.

Velo sigue haciendo falta para OTRA cosa: el alto del iframe del catálogo, que
cambia al filtrar (ver la sección anterior).

**Dos cosas aprendidas de sus capturas del sitio actual:**

1. **El menú real es: Home · Products · Information · Contact · Blog.** No coincide
   con lo que enlazan nuestros embeds (`ingredients`, `about`, `contact`). Hacen
   falta los slugs reales antes de atar nada.
2. **Ya existe un formulario de muestra gratis** en un popup del sitio actual:
   «Email and receive a free sample of our products», con campos Email, Name e
   Industry. O sea que la acción «muestra» ya está resuelta en Wix y no hay que
   construirla — sólo enlazarla.

### Enlaces atados a Wix (2026-08-31)

Slugs confirmados por Michelle en el panel de SEO: `tcorpi.com/` ·
`/about-us` · `/ingredients` · `/contact`. **Todo con `www.`**

**La reescritura vive en `build.py`, no en los previews.** Así los previews
siguen enlazando entre sí para revisarlos en local y sólo los embeds apuntan a
Wix. Cada `<a>` sale con `target="_top"`, sin el cual abriría el sitio de Wix
*dentro* de la cajita del embed. WhatsApp sale con `_blank`; `mailto:` y `sms:`
con `_top`, que desde un iframe pueden quedar bloqueados si no.

Verificado en el navegador: los 39 botones «Quote today» del catálogo apuntan a
`https://www.tcorpi.com/contact` con `target="_top"`.

**Bug corregido en el camino:** el primer patrón sólo miraba los atributos que
había ANTES del href. Los botones de WhatsApp ya traían `target="_blank"`
DESPUÉS, así que les añadía un segundo. El navegador se queda con el primero y
funciona, pero es HTML inválido. Ahora se inspecciona la etiqueta entera.

La comprobación tampoco podía exigir «al menos un enlace reescrito»: home-3 es
sólo el carril de testimonios y no tiene ninguno. Lo que sí se comprueba es que
no quede ningún `href` apuntando a un `_prev.html`, que sería un enlace roto.

### Ortografía: el sitio es inglés AMERICANO (2026-08-31)

Michelle pidió revisar la ortografía. **El fallo era mío y sistemático:** el texto
original del sitio está en americano («customized», «Hydrolyzed», «Alkalized»),
pero **las 20 descripciones que escribí salieron en británico**. En la misma
tarjeta el título decía *Hydrolyzed* y mi texto *hydrolysed*.

13 correcciones: `hydrolysed`, `Instantised`, `standardised`×5, `micronised`,
`flavour`×2, `flavoured`, `colour`, `fibre`.

**Y 14 fichas más desde los COA:** el proveedor escribe «Brown coloured powder».
Se normaliza al extraer —ortografía, no significado— y queda anotado en
`extraer.py` para las próximas.

Lo que queda en británico está **sólo en comentarios del código** (`centre`,
`colour` en notas de desarrollo). No es texto visible; se deja.

Barrido también de los errores frecuentes de inglés (`recieve`, `seperate`,
`occured`, `accomodate`…): ninguno.

**Dos cosas que son contenido de Michelle, no mío, y quedan por decidir:**
- **«Eggwhite Protein Powder»** → lo estándar es «Egg White», dos palabras.
- **«Terminalia bellerica»** (en Triphala) → el nombre aceptado es
  *Terminalia **bellirica***.

**Las dos correcciones de contenido, aplicadas** (2026-08-31):
«Eggwhite Protein Powder» → **«Egg White Protein Powder»**, y en Triphala
«Terminalia bellerica» → ***Terminalia bellirica*** (las dos variantes).

**Trampa: renombrar el producto rompió su foto.** El nombre del archivo se deduce
del nombre del producto (`imgSlug`), así que «Egg White…» pasó a buscar
`egg-white-protein-powder.jpg` mientras el archivo seguía siendo
`eggwhite-protein-powder.jpg` → 404 y tarjeta sin imagen. Se renombró el archivo
en vez de añadir una excepción a `IMG_FIX`: ese mapa es para desajustes reales
del catálogo, no para los que uno mismo acaba de crear.

Verificado con las 39 tarjetas: 39 fotos distintas, **ningún 404**.
