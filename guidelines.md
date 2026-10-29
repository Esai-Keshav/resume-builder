# Resume Writing Guidelines

Rules for writing or editing any resume content in this repo (`resume.json` only — never the generated files).

## 1. Truth Only

- Write bullets from facts the user has confirmed. Nothing invented, no assumed metrics.
- If a claim is vague or unverifiable, ask the user what actually happened before writing it.
- Remove client/company/project names from bullets when the user says so — describe the work, not the brand.

## 2. Evidence Over Adjectives

- Show, don't tell. A concrete action proves a skill; an adjective claims it.
  - Weak: "Improved communication across teams."
  - Strong: "Ran weekly client requirement calls and translated them into shipped features."
- Soft-skill and "mindset" bullets are allowed only when they describe real behavior, and must still name the concrete action.
- Each bullet: start with an action verb, end with the result or purpose.

## 3. Bullet Shape

- 1–2 lines each. One idea per bullet.
- 2–4 bullets per role; most recent roles get more.
- Plain text is safe — `build.py` auto-escapes LaTeX special chars.
- Consistent dates format: `Mon YYYY - Mon YYYY`.

## 4. ATS Rules (kept by the template, follow when touching it)

- Single column, no tables for content layout, no text boxes, no images/icons for information.
- Standard section headers: Work Experience, Education, Project Work, Skills.
- Standard bullet symbol. Contact info in the body, not a header/footer.
- Sans-serif font, 8pt body is fine for density; margins handled by template geometry.

## 5. Page Budget

- Target 1–2 pages. The template uses `scale=0.92` to fit; don't pad content to fill space.
- When adding content, prefer merging/rewriting over stacking — combine overlapping bullets into one.

## 6. Word Hygiene

- No AI-slop phrasing: "spearheaded", "leverage synergies", "cutting-edge", rule-of-three padding, vague attribution ("significantly improved" without a metric).
- No fabricated numbers. If a number exists and is user-confirmed, use it; otherwise write without one.
- Terminology verbatim: tool/framework names spelled exactly (Salesforce, GoHighLevel, Gemini Vision, PhonePe).

## 7. Process

- Every content change: edit `resume.json` → run `python3 build.py` → confirm `resume.tex` diff matches intent.
- Word choices the user hasn't approved: present the draft first for factual claims (see the brainstorming flow — clarify, propose, approve, then write).
