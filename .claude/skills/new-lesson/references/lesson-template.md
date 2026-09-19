# Lesson <stage-id>.<lesson-id>: <Title>

## Description
2–4 sentences: what this lesson is about and where it fits in the
project (what came before, what it sets up next).

## Key question
One sentence — the "why" this lesson exists to answer. Copy from
roadmap.md, don't paraphrase into something vaguer.

## Plan
Ordered steps to get from nothing to done. Concrete enough to follow
without re-reading the source material first, e.g.:

1. Implement `<function>` in `lesson.py` (see TODOs).
2. Run `uv run check.py` to confirm shapes/behavior.
3. Run the ablation described below and note the result.

## Study links
Pulled from roadmap.md for this lesson — don't add extra links here.

## Task
The concrete, gradable task. State the "done" condition explicitly
(e.g. "uv run check.py passes", "loss decreases below X").

## Files in this lesson
- `lesson.py` — starter code, implement the TODOs
- `check.py` — run this to verify your implementation (if present)
- `pyproject.toml` — this lesson's own uv project and dependencies

## Running

This lesson is its own uv project. All commands below run from
*inside this folder*.

Run a script:
```
uv run check.py
uv run lesson.py
```
`uv` resolves/installs this lesson's dependencies on first run — no
manual `pip install` or shared venv needed.

Add a dependency (updates `pyproject.toml` + `uv.lock`, syncs `.venv`):
```
uv add <package>          # needed to run the lesson
uv add --dev <package>    # only needed for your own dev/exploration, e.g. jupyter
```

Open a Python REPL in this lesson's environment:
```
uv run python
```

Run Jupyter (after `uv add --dev jupyter`):
```
uv run jupyter lab
```
Or try it once without adding it permanently:
```
uv run --with jupyter jupyter lab
```
