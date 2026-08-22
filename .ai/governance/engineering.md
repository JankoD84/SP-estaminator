# Engineering Governance

- Keep the tool simple: CLI and Streamlit UI should remain thin around the same estimation criteria and mapping.
- Do not introduce a service backend, database, auth, or deployment surface unless explicitly requested.
- Changes to criteria labels, input validation, score ranges, or Fibonacci mapping should be deliberate and documented in the completion report.
- Do not change dependencies, `.gitignore`, or CI workflows without explicit scope.
