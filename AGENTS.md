# SP-estaminator / Agent Entry Gate

## Repository purpose

`SP-estaminator` is a small Python Agile story-point estimator. It scores Complexity, Effort, and Uncertainty and maps the combined score to Fibonacci story points. It provides a CLI entry point in `estimator_cli.py` and a Streamlit UI in `estimator_app.py`.

## Ownership boundaries

This repository owns only the story-point estimation utility and its local CLI/UI surfaces.

It does not own Dulvarn platform governance, external agile tooling data, authoritative delivery commitments, production services, billing, authentication, or other calculator repositories.

## Actual stack

- Python
- Streamlit (`streamlit>=1.32.0`)

There is no FastAPI service, database, or tracked test suite in this repository.

## Protected areas

Ask before changing:

- `requirements.txt`
- `.gitignore`
- `.github/workflows/`
- scoring criteria, Fibonacci mapping, or estimation labels

Never edit `.git/`, virtual environments, caches, generated files, or secrets.

## Branch and edit safety

Before implementation, run and report:

```bash
git status --short
git branch --show-current
git log -1 --oneline
git diff --stat
```

Do not work directly on the default integration branch unless explicitly requested. Do not push or force-push without explicit approval.

## Progressive disclosure

Use this order:

1. `AGENTS.md` — repository entry gate.
2. `.ai/README.md` — Standards V2 Lite hierarchy.
3. `.ai/repo/context.md` — repository-specific context and key files.
4. `.ai/governance/engineering.md` — engineering constraints.
5. `.ai/process/implementation.md` — implementation workflow.
6. `estimator_cli.py`, `estimator_app.py`, and `requirements.txt` for current behavior.

`docs/ai/` is compatibility/reference material only.

## Validation

Use commands that exist here:

```bash
python estimator_cli.py
streamlit run estimator_app.py
git diff --check
```

For governance-only changes, `git diff --check` is sufficient.

## Completion report

Report repository, branch, HEAD, files changed, validation, risks/rollback notes, and a concise commit message.

## Universal AI Governance Contract

`AGENTS.md` is the universal AI-agent entrypoint for Devin, Windsurf/Cascade, Cursor, VS Code + Roo Code, and Zed. Repository-specific rules in this file override generic ecosystem guidance.

Before implementation work, check and report:

```bash
git status
git branch --show-current
git diff --stat
```

Then read the repository AI context that is relevant to the task:

- `.ai/repo/profile.md`
- `.ai/repo/boundaries.md`
- `.ai/repo/commands.md`
- `.ai/governance/source-of-truth.md`
- `.ai/governance/safety-policy.md`
- `.ai/governance/quality-gates.md`

Source-of-truth precedence:

1. Current repository source code
2. Current tests, schemas and contracts
3. Current runtime / Git state
4. Repository `AGENTS.md`
5. Canonical repository documentation
6. `.ai/repo/` navigation/context
7. Task-specific `.agents/skills/`, when present
8. Historical reports, summaries, RAG output and chat context

Canonical AI governance lives in `AGENTS.md`, `.ai/`, and `.agents/skills/` when skills exist. IDE-specific directories such as `.zed/`, `.cursor/`, `.roo/`, `.windsurf/`, and `.vscode/` are execution adapters only and must not redefine repository engineering standards.

Do not modify provider credentials, model routing, LiteLLM, MCP runtime configuration, OAuth, AWS, Azure, ChatGPT subscription settings, production infrastructure, secrets, or `.env*` files as part of repository-governance work.
