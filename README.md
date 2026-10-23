# Resume Builder

Link => https://esai-keshav.github.io/resume-builder/resume.pdf

## How it works

```
resume.json  →  build.py  →  resume.tex  →  GitHub Actions  →  resume.pdf
   (edit)      (generator)   (generated)     (compiles PDF)    (deployed to GitHub Pages)
```

`resume.json` is the single source of truth. You never edit `resume.tex` or `resume.pdf` by hand.

## Usage

### One-time hook setup (required)

```sh
git config core.hooksPath .githooks
```

After this, every commit that changes `resume.json` automatically regenerates `resume.tex`
and includes it in the commit.

### Manual generation (optional)

```sh
python3 build.py
```

The PDF itself is compiled by CI (`.github/workflows/build.yml`) on every push to `main`
and deployed to GitHub Pages — no local LaTeX needed.

## Notes

- All values from `resume.json` are auto-escaped for LaTeX (`& % $ # _ { } ~ ^ \`),
  so plain text is always safe.
- `resume.tex` is only rewritten when its content actually changes.
