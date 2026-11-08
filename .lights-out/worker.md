# Brief for the dev-worker: attached

Drafted by ./go init on 2026-11-08 (docs/adr/0042 §6) from what the repository
declares; edit it before committing. What this repository tells the
lights-out dev-worker (docs/adr/0037 §6): where its code is and how its
tests run.

## Scope

Your entire task is inside `textkit/` and `tests/`. Read only those paths, plus the
ticket. `.lights-out/` is the platform's contract: leave it alone.

## Tests

From the repository root, `uv run --locked pytest tests -q -p no:cacheprovider`. Use exactly this command.
