# Resume Writing Guidelines

Rules for writing or editing any resume content in this repo (`resume.json` only, never the generated files).

## 1. Truth Only

- Write bullets from facts the user has confirmed. Nothing invented, no assumed metrics.
- If a claim is vague or unverifiable, ask the user what actually happened before writing it.
- Remove client, company, and project names from bullets when the user says so. Describe the work, not the brand.

## 2. Evidence Over Adjectives

- Show, don't tell. A concrete action proves a skill. An adjective claims it.
  - Weak: "Improved communication across teams."
  - Strong: "Ran weekly client requirement calls and translated them into shipped features."
- Soft skill and "mindset" bullets are allowed only when they describe real behavior, and must still name the concrete action.
- Each bullet starts with an action verb and ends with the result or purpose.

## 3. Bullet Shape

- 1 to 2 lines each. One idea per bullet.
- 2 to 4 bullets per role. The most recent roles get more.
- Plain text is safe because `build.py` escapes LaTeX special characters automatically.
- Dates stay in one format: `Mon YYYY - Mon YYYY`.

## 4. ATS Rules (the template keeps these. Follow them when touching it)

- Single column. No tables for content layout, no text boxes, no images or icons for information.
- Standard section headers: Work Experience, Education, Project Work, Skills.
- Standard bullet symbol. Contact info sits in the body, not a header or footer.
- Sans serif font. 8pt body is fine for density. Template geometry handles margins.

## 5. Page Budget

- Target 1 to 2 pages. The template uses `scale=0.92` to fit. Don't pad content to fill space.
- When adding content, prefer merging or rewriting over stacking. Combine overlapping bullets into one.

## 6. Word Hygiene

- No slop phrasing: "spearheaded", "leverage synergies", "cutting edge", rule of three padding, vague attribution like "significantly improved" without a metric.
- No fake numbers. If a number exists and the user confirmed it, use it. Otherwise write without one.
- No em dashes (—) or en dashes (–) in bullets. Write plain sentences with commas. A plain hyphen (-) is allowed only in compound words ("water-data") and verbatim tool names ("LLM-as-a-Judge").
- Tool and framework names stay verbatim: Salesforce, GoHighLevel, Gemini Vision, PhonePe.

## 7. Process

- Every content change: edit `resume.json`, run `python3 build.py`, then confirm the `resume.tex` diff matches the intent.
- For word choices the user has not approved: present the draft first for factual claims. Clarify, propose, approve, then write.
