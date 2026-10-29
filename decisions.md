# Decisions

Log of decisions made for this resume. Newest last. Each entry: what was decided and why, so future agents don't reopen settled questions.

## 2025-10-29

### Resume content

| Decision | Why |
| --- | --- |
| Added a Slack integration bullet to Convverse.ai (docs and data from the client's shared Slack channel fed the AI) | User-built feature, was missing from the resume |
| Added a client-requirements bullet to Ewokee (direct client contact, requirements turned into features) | Highlights communication with confirmed evidence: direct client contact was real |
| Rejected generic soft-skill bullets: "Owned work end-to-end without PM support" and "Ran the engagement as its own project with timelines" | Adjectives over evidence; user chose to drop both |
| Combined the two Cyces Instagram bullets into one, then split it again into two | One weighed ~45 words against the 1 to 2 line budget; the split keeps each bullet single-purpose |
| Rewrote the Chrome extension bullet to name real effects: faster loading and fewer failed requests | "Faster and more reliable" failed the portability test |
| Rewrote the Ewokee website bullet to name mechanisms: image resizing, lazy loading, leaner assets; dropped the unmeasured "high Lighthouse" claim | No confirmed score exists, so no number is claimed |
| Removed client names ITRA, WeGot AI, and FittGen from the Cyces bullets | User considers them client names; describe the work, not the brands |
| Removed "Structured Outputs" from AI/GenAI skills; added Claude API and OpenAI API | User's call on which skills they present |
| Kept company and project names in headers for now | TODO item 5 ("remove company and project name") not yet finalized |

### Writing standards

| Decision | Why |
| --- | --- |
| Created `guidelines.md` as the resume writing rulebook (truth only, evidence over adjectives, bullet shape, ATS, page budget, word hygiene, process) | One place for writing standards; AGENTS.md links to it |
| Rewrote `guidelines.md` with no hyphens or em dashes outside verbatim compound words and tool names | User request after seeing dashes in generated prose |
| Rule: resume bullets never contain em dashes or en dashes; plain sentences with commas | ATS safety and cleaner prose; example: "water-data", "LLM-as-a-Judge" keep their hyphens |
| Confirmed facts only: no invented numbers (Lighthouse score, load times) unless the user provides them | Honesty; two open questions were asked and answered before wording |

### Workflow

| Decision | Why |
| --- | --- |
| Git rule: commit or push only when the user explicitly says so | User request, stated twice; first push-only, then extended to commits |
| Push target is `origin/dev`; PDF compiles in CI on pushes to `main` only | Repo setup; dev commits leave the published PDF stale until merge |
| Skills to load every session: `caveman`, `no-ai-slop`; resume sessions also load `resume-ats-optimizer`, `resume-formatter` | User chose option 2a: AGENTS.md instruction rather than a custom command |
| TODO.md is updated in-repo when an item ships; done items marked with a leading dash and a note | Keeps TODO and resume in sync per user habit |

### Publishing

| Decision | Why |
| --- | --- |
| Published PDF renamed to `public/Esai-Keshav-Resume.pdf`; CI copies the compiled PDF to that name | GitHub Pages cannot set download filenames, so the URL basename must carry the name; resumes should download as Name Resume.pdf |
| `public/index.html`, README link, and the resume project link updated to the new URL; stale `public/resume.pdf` removed from git | Old name must die everywhere at once |
| No local LaTeX: all PDF compiles happen in CI | No LaTeX, docker, or sudo in this environment; attempts to compile locally failed |

## Open items

- Company names (Convverse.ai, Ewokee) and project names still appear in the resume. Decide the full scope of TODO item 5 before stripping.
- Dev branch PDFs stay stale between merges to main. Decide if dev pushes should also publish (workflow trigger change).
