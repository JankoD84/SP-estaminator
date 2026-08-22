# Implementation Process

1. Run Git preflight:

   ```bash
   git status --short
   git branch --show-current
   git log -1 --oneline
   git diff --stat
   ```

2. Read `AGENTS.md`, `.ai/repo/context.md`, and `.ai/governance/engineering.md`.
3. Inspect `estimator_cli.py`, `estimator_app.py`, and `requirements.txt` before changing behavior.
4. Make the smallest scoped change.
5. Preserve CLI/UI consistency for estimation criteria and Fibonacci mapping.
6. Run relevant validation:

   ```bash
   python estimator_cli.py
   streamlit run estimator_app.py
   git diff --check
   ```

7. Update documentation if commands, scoring assumptions, or user-facing behavior change.
8. Report files changed, validation, risks, and commit message.
