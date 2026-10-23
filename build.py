#!/usr/bin/env python3
"""Generate resume.tex from resume.json. Stdlib only, no dependencies."""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# Colors used in the template (must match resume.tex)
C_MAIN = "1C033C"
C_HEAD = "371e77"
C_SUB = "4B28A4"

PREAMBLE = r"""\documentclass[a4paper,8pt]{article}

\usepackage{parskip}
\usepackage{hologo}

% REPLACEMENT FOR FONTSPEC (Works with standard pdflatex)
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault} % Sets the font to sans-serif (like Arial)

%other packages for formatting
\usepackage{graphicx}
\usepackage[usenames,dvipsnames]{xcolor}

% --- MARGIN SETTINGS ---
\usepackage[scale=0.92, top=0.13in, bottom=0.13in]{geometry}

%tabularx environment
\usepackage{tabularx}

%for lists within experience section
\usepackage{enumitem}

% centered version of 'X' col. type
\newcolumntype{C}{>{\centering\arraybackslash}X}

%to prevent spillover of tabular into next pages
\usepackage{supertabular}
\newlength{\fullcollw}
\setlength{\fullcollw}{0.42\textwidth}

%custom \section
\usepackage{titlesec}
\usepackage{multicol}
\usepackage{multirow}

%CV Sections settings
\titleformat{\section}{\Large\scshape\raggedright}{}{0em}{}[\titlerule]
\titlespacing{\section}{1pt}{2pt}{2pt}

%for publications
\usepackage[style=authoryear,sorting=ynt, maxbibnames=2]{biblatex}

%Setup hyperref package
\usepackage[unicode, draft=false, hidelinks]{hyperref}

\color[HTML]{110223}
\setlength\bibitemsep{1em}

%for social icons
\usepackage{fontawesome5}

% For underline
\usepackage[normalem]{ulem}

\begin{document}

% non-numbered pages
\pagestyle{empty}
"""

HEADER = r"""
% HEADER
\begin{tabularx}{\linewidth}{@{} C @{}}
\color[HTML]{__C_MAIN__} \Huge{__NAME__} \\[6pt]
\\
\textcolor[HTML]{__C_HEAD__}{{{{\faEnvelope} __EMAIL__}} $|$}
% PHONE NUMBER WITH CALL LOGO (\faPhone)
\textcolor[HTML]{__C_HEAD__}{{{\faPhone} __PHONE__}} $|$
\textcolor[HTML]{__C_HEAD__}{{{\faMapMarker*} __LOCATION__}}

% GITHUB LINK
\href{__GITHUB_URL__}{\textcolor[HTML]{__C_HEAD__}{\underline{{\raisebox{-0.05\height}{\faGithub} __GITHUB_LABEL__}}}} $|$
% LINKEDIN LINK
\href{__LINKEDIN_URL__}{\textcolor[HTML]{__C_HEAD__}{\underline{{\raisebox{-0.05\height}{\faLinkedin} __LINKEDIN_LABEL__}}}}
\end{tabularx}
"""

EXPERIENCE = r"""
\begin{tabularx}{\linewidth}{ @{}l r@{} }
\color[HTML]{__C_MAIN__} \textbf{{__COMPANY__}} \hfill \color[HTML]{__C_HEAD__} __DATES__ \\[4pt]
\color[HTML]{__C_HEAD__}\textbf{\textit{__ROLE__}}\ \hfill \color[HTML]{__C_SUB__} \\[5pt]
\begin{minipage}[t]{\linewidth}
    \begin{itemize}[nosep,after=\strut, leftmargin=2em, itemsep=2pt]
__BULLETS__
    \end{itemize}
\end{minipage}
\end{tabularx}
"""

EDUCATION = r"""
\begin{tabularx}{\linewidth}{ @{}l r@{} }
\color[HTML]{__C_MAIN__} \textbf{__INSTITUTION__} & \hfill \color[HTML]{__C_HEAD__} __DEGREE__ \\
\color[HTML]{__C_HEAD__} Specialization: __SPECIALIZATION__ & \hfill \color[HTML]{__C_SUB__} \textit{\textbf{GPA: __GPA__}} \\[5pt]
\multicolumn{2}{@{}X@{}}{
    \begin{minipage}[t]{\linewidth}
        \begin{itemize}[nosep,after=\strut, leftmargin=1.5em, itemsep=2pt]
__HIGHLIGHTS__
        \end{itemize}
    \end{minipage}
}
\end{tabularx}\\[3pt]
"""

PROJECT = r"""
        \item \textbf{__PNAME__:} __DESC__ \\
        \textit{Tech Stack: __TECH__.} \\
        \textit{Link: \href{__URL__}{__LINK_LABEL__}}
"""

SKILL_LINE = r"\color[HTML]{__C_MAIN__}\textbf{__KEY__:} __VALUES__\\[3pt]"

SKILLS_TAIL = r"""

\end{document}
"""

ESCAPE_MAP = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}
_ESCAPE_RE = re.compile("|".join(re.escape(ch) for ch in ESCAPE_MAP))


def esc(value):
    """Escape LaTeX special characters in any JSON value."""
    return _ESCAPE_RE.sub(lambda m: ESCAPE_MAP[m.group(0)], str(value))


def fill(template, values):
    for key, val in values.items():
        template = template.replace(f"__{key}__", val)
    return template


def itemize(items, indent):
    return "\n".join(f"{indent}\\item {esc(i)}" for i in items)


def build(data):
    contacts = data["contacts"]
    out_m = [PREAMBLE]

    out_m.append(fill(HEADER, {
        "C_MAIN": C_MAIN, "C_HEAD": C_HEAD, "C_SUB": C_SUB,
        "NAME": esc(data["name"]),
        "EMAIL": esc(contacts["email"]),
        "PHONE": esc(contacts["phone"]),
        "LOCATION": esc(contacts["location"]),
        "GITHUB_LABEL": esc(contacts["github"]["label"]),
        "GITHUB_URL": esc(contacts["github"]["url"]),
        "LINKEDIN_LABEL": esc(contacts["linkedin"]["label"]),
        "LINKEDIN_URL": esc(contacts["linkedin"]["url"]),
    }))

    out_m.append("\n% WORK EXPERIENCE\n\\section{Work Experience}\n")
    for n, e in enumerate(data["experience"], 1):
        out_m.append(f"% Experience {n}\n")
        out_m.append(fill(EXPERIENCE, {
            "C_MAIN": C_MAIN, "C_HEAD": C_HEAD, "C_SUB": C_SUB,
            "COMPANY": esc(e["company"]),
            "ROLE": esc(e["role"]),
            "DATES": esc(e["dates"]),
            "BULLETS": itemize(e["bullets"], "        "),
        }))

    edu = data["education"]
    out_m.append("\n% EDUCATION\n\\section{Education}\n")
    out_m.append(fill(EDUCATION, {
        "C_MAIN": C_MAIN, "C_HEAD": C_HEAD, "C_SUB": C_SUB,
        "INSTITUTION": esc(edu["institution"]),
        "DEGREE": esc(edu["degree"]),
        "SPECIALIZATION": esc(edu["specialization"]),
        "GPA": esc(edu["gpa"]),
        "HIGHLIGHTS": itemize(edu["highlights"], "            "),
    }))

    out_m.append("\n% PROJECTS\n\\section{Project Work}\n")
    proj_items = []
    for i, p in enumerate(data["projects"]):
        item = fill(PROJECT, {
            "PNAME": esc(p["name"]),
            "DESC": esc(p["description"]),
            "TECH": esc(p["tech"]),
            "URL": esc(p["link"]["url"]),
            "LINK_LABEL": esc(p["link"]["label"]),
        })
        proj_items.append(item)
        if i < len(data["projects"]) - 1:
            proj_items.append("\n        \\vspace{3pt}\n")
    out_m.append(
        "\\begin{tabularx}{\\linewidth}{ @{}l r@{} }\n"
        "\\begin{minipage}[t]{\\linewidth}\n"
        "    \\begin{itemize}[nosep,after=\\strut, leftmargin=2em, itemsep=2pt]\n"
        + "".join(proj_items)
        + "    \\end{itemize}\n"
        "    \\end{minipage}\n"
        "\\end{tabularx}\\\\[3pt]\n"
    )

    out_m.append("\n% SKILLS\n\\section{Skills}\n")
    skill_lines = "\n".join(
        fill(SKILL_LINE, {
            "C_MAIN": C_MAIN,
            "KEY": esc(k),
            "VALUES": esc(", ".join(v)),
        })
        for k, v in data["skills"].items()
    )
    out_m.append(skill_lines + SKILLS_TAIL)

    # squeeze runs of 3+ newlines (from template joins) into a single blank line
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out_m))


def main():
    with open(os.path.join(ROOT, "resume.json"), encoding="utf-8") as f:
        data = json.load(f)

    tex = build(data)

    out = os.path.join(ROOT, "resume.tex")
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f:
            if f.read() == tex:
                print("resume.tex unchanged")
                return

    with open(out, "w", encoding="utf-8") as f:
        f.write(tex)
    print("resume.tex generated")


if __name__ == "__main__":
    sys.exit(main())
