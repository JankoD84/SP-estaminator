# Repository Context

## Purpose

`SP-estaminator` estimates Agile story points from Complexity, Effort, and Uncertainty ratings and maps the score to Fibonacci points.

## Stack

- Python
- Streamlit

## Key files

- `estimator_cli.py` — CLI entry point and scoring/mapping behavior.
- `estimator_app.py` — Streamlit UI for estimation.
- `requirements.txt` — Streamlit dependency.
- `.gitignore` — repository ignore rules.
- `.github/workflows/` — CI and mirror workflows.

## Architecture

This is a simple local estimation utility. Keep CLI and Streamlit UI behavior aligned with the same scoring criteria and Fibonacci mapping.

## Ownership and non-ownership

Owns story-point estimation guidance only. Does not own team delivery commitments, external agile tooling data, Dulvarn platform governance, production services, auth, or billing.

## External dependencies

- Python runtime
- Streamlit runtime for the web UI
