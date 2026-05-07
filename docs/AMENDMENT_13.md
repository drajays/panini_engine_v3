# Amendment — CONSTITUTION Article 13 (universal sūtra architecture)

## Proposal

Add **Article 13** to `CONSTITUTION.md`, update **Article 10** to count
fourteen Articles (0–13), add `docs/SUTRA_UNIVERSAL_RULE_ARCHITECTURE.md`,
add `.cursor/rules/panini-sutra-universal-architecture.mdc`, and reference
both from `.cursorrules`.

## Rationale

Codifies engineering practice already implied by **Article 2** (what
`cond` may read) and **Article 12** (no shortcuts): sūtra files should fire
from linguistic `State`/`Term` signals, not from ad hoc recipe-only
`state.meta` arms. Legacy arms remain until per-file refactors; new code
must not extend that pattern.

## Acceptance

- Text merged as described; Article 10 count updated.
- No engine behaviour change in this amendment (documentation + policy
  layer only).
