# TradeCorp — Project Rules

Read this before doing anything in this repo.

TradeCorp Investments is a food-ingredient importer/distributor. This repo holds the
brand assets and the website. The site is **hand-built, self-contained HTML** — no
framework, no build step, no npm. Keep it that way.

---

## 0. Workflow — do this first, every time

0. **Read `GOALS.md` before anything else.** It holds the north star, the one item
   we're working on now, and Michelle's running list of corrections. Treat its
   "Explicitly decided" section as closed — do not re-propose those. When a goal is
   finished **and verified in the browser**, move it to "Done" with today's date and
   say so. If Michelle describes a new complaint mid-session, add it to "Open
   corrections" as you go, in her words — don't rely on remembering it.
   Corrections there are often vague on purpose ("feels cramped", "too dark"). That
   is not a spec — ask which page and what "better" looks like before redesigning.
1. **Invoke the `web-delivery-workflow` skill before writing any page code.** It is
   installed globally and encodes how this user expects web work to be built, verified
   and shipped. Do not skip it, even for a "small" change.
2. **Consult the design skills before inventing a layout.** For anything visual —
   a new section, a component, a layout, a restyle — pull from the installed design
   skills (`design`, `ui-styling`, `emil-design-eng`, `design-system`,
   `design:design-critique`) rather than producing a generic default. Never ship the
   first stock layout that comes to mind.
3. **Match the existing brand system** (§2). This site has a real corporate identity
   manual behind it. Brand fidelity outranks novelty.
4. **Verify in the browser before saying "done"** (§4).

## 1. The user

Michelle is a **designer, not an engineer**. Communicate in plain Spanish, step by
step, and always show the visual result (a screenshot beats a description). Do not
explain code unless asked. When something is missing, use a clearly-marked
placeholder and ask at the end, all at once — not in a drip of interruptions.

## 1b. Never change content on your own

The brand and the copy are **Michelle's to change, not yours.**

- **Never edit copy, product names, prices, certifications, addresses, phone numbers or
  emails** because they look wrong, outdated or inconsistent. Point it out and ask.
- **Never change the logo.** Not the file, not the colors, not the spacing, never
  re-typeset the wordmark. (See §2.)
- **Never introduce a color or font** outside the brand system, however good it looks.
- Rewording marketing copy counts as changing content. Ask.
- If a value is missing, use a **clearly-marked placeholder** and list it at the end —
  never invent a plausible-looking address, email or phone number.

The one standing exception: the brief asks the palette to lean **more café/brown**.
Rebalancing *existing* brand tokens is wanted. Adding new ones is not.

## 2. Brand system — non-negotiable

Source of truth: `TRADE CORP MANUAL.pdf` (identity manual by VIBO Design House).

**Color tokens** (already defined in every page's `:root` — always use the variable,
never a raw hex):

| Token       | Value     | Name       |
|-------------|-----------|------------|
| `--oliva`   | `#424f25` | dark green |
| `--salvia`  | `#a6bf85` | sage       |
| `--crema`   | `#eae4d1` | cream      |
| `--cafe`    | `#382915` | coffee     |

*(The manual's canonical values are ~1 unit off — `#434f25`, `#a7c086`, `#ebe4d1`.
The tokens above come from the user's approved briefs. Leave them as they are.)*

**Three-font system** — also already defined as variables:

| Variable          | Font          | Used for                                        |
|-------------------|---------------|-------------------------------------------------|
| `--font-display`  | Poppins       | titles and headings                              |
| `--font-body`     | Kanit         | body copy                                        |
| `--font-small`    | AvenirLight   | smallest text — labels, meta, chips, captions    |

Poppins and Kanit load from Google Fonts. Avenir is **not** on Google Fonts and is
embedded as a base64 `@font-face` at the top of each page's `<style>`. Keep it inlined.

**The logo is proprietary type. Never re-typeset the wordmark with a web font.**
Always use the SVG: `Brand/svg/logo-trade-corp.svg` (tidied copy at
`docs/assets/logo-trade-corp.svg`, `viewBox="33 33 3928 743"`).

> **Logo gotcha:** the hero animation morphs the "o" counterform from cream to olive
> via `counter.setAttribute('fill', …)`. A CSS rule beats a presentation attribute, so
> `#o-counter` must **not** carry `class="cls-1"` (`fill:none`) — if it does, the color
> morph silently breaks. Give it `fill="#eae4d1"` inline and no class.

## 3. Repo layout — two separate deliverables

```
docs/     → the live website (GitHub Pages). Has the sticky nav. THIS IS THE SITE.
            index.html · ingredients/ · about/ · contact/
src/      → standalone Wix-embed versions. No nav, fully self-contained.
            hero/ · hero-portal/ · about/ · contact/ · portfolio/
Brand/    → logos, fonts, palette. Source assets — do not edit to fit a layout.
_backups/ → gitignored local safety copies.
```

**`docs/` and `src/` are NOT the same files.** Changing a page in one does not change
the other. If an edit should appear in both, edit both — and say which you touched.

## 4. Verify before you claim it works

Use the browser preview tools (there is a `.claude/launch.json` — start the
**tradecorp-docs** server). Screenshot the result and check the console for errors.
Never ask the user to check manually; verify it yourself and show them.

> **Never convert a scroll-scrubbed animation into a threshold-triggered one.** The hero
> and the Why section both *scrub*: each scroll frame recomputes the frame inline, so the
> motion follows the user's scroll. Swapping that for an IntersectionObserver plus a CSS
> transition reads as broken — the animation is over before the section is comfortably in
> view, and it stops responding to the scroll. This was done by accident once and took
> four rounds to undo. Also: never put a CSS `transition` on a property a scrub rewrites
> every frame; they fight and it lags.

> **Never slice a file with two independently-searched indices.** A class name usually
> appears in the CSS *before* the markup, so `src.index('x')` can land in the stylesheet
> and produce `end < start` — `src[:start] + new + src[end:]` then silently DUPLICATES a
> whole region instead of replacing it. Assert `start < end`, or match the entire block
> by its exact text. This corrupted `docs/about/index.html` once.

> **When the user says "it used to work", diff `_backups/` before theorising.**

> **Preview-pane gotcha:** an idle or hidden pane **freezes** `requestAnimationFrame`,
> CSS transitions and IntersectionObserver. Scroll animations and autoplay video will
> look broken when they are fine. Verify end state by forcing inline styles or querying
> the DOM with JS — never conclude "the animation is broken" from a frozen pane.

**Turn the screenshot loop off when working on animated backgrounds or moving
carousels** — motion between frames makes visual comparison meaningless.

## 5. Page requirements

Every page ships with:

- **Self-contained** — no build step, everything inlined, pasteable as one file.
- **Animate only `transform` and `opacity`.** Never animate layout properties.
  (The hero's shrink uses `clip-path: inset(… round …)` for exactly this reason.)
- **`prefers-reduced-motion` support** on every animation — fade or disable.
- **Images lazy-loaded** with meaningful `alt` text.
- **Relative links only** (`ingredients/` from home, `../ingredients/` from sub-pages)
  so the GitHub Pages subpath keeps working.

Third-party component libraries (21st.dev, shadcn, etc.) ship **React + Tailwind**.
This project is vanilla HTML/CSS. Never paste that code in directly — re-express the
idea as plain CSS/JS that matches the brand tokens above.

## 6. Git — the push gotcha

Repo: `github.com/michellealjure/TRADECORP2`, branch `main`, over SSH.

```
git push --no-thin origin main
```

**A plain `git push` is rejected** with `remote: fatal error in commit_refs`. Always
pass `--no-thin`. This is not local corruption — `git fsck --full` is clean.

Commit messages in English, descriptive. **Do not push on your own** — finish the
change, show the user, and offer to push.

## 7. Deployment

**Decided 2026-08-22: the site is hosted OUTSIDE Wix and `tcorpi.com` points at it.**
Wix is domain-only. Do not build for Wix HTML embeds, and do not shape work around
iframe constraints — sandboxed-iframe limits (no parent scroll, fixed height, isolated
document) are what forced the old autoplay hero, and they no longer apply.

Currently live at `https://michellealjure.github.io/TRADECORP2/`, served from `docs/`
on `main`. `docs/.nojekyll` disables Jekyll. Push to `main` → Pages redeploys.

Local preview: `python3 -m http.server 8090 --directory docs`

Because the site is now the real indexed page (not iframe content), **SEO is in scope**:
per-page `<title>`, meta description, Open Graph tags, favicon, sitemap.

**DNS is Michelle's to change, never yours.** Do not touch registrar or domain settings.

## 8. Security

Never handle, enter, store or print tokens, credentials, passwords or private keys.
If the user pastes one, refuse to use it and direct them to do it themselves. With SSH,
only ever surface the **public** key.
