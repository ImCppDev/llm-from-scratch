---
name: new-lesson
description: Generates the next lesson in the "LLM from scratch" learning project — like a teacher handing out the next assignment. Use whenever the user asks for a new lesson, the next task, a new assignment, what to do next, or says things like "new lesson", "next lesson", "give me a task", "дай задание", "новый урок", "что дальше". Produces a lesson folder with a description, a plan, study links, and the actual task, plus starter code files and any needed dependencies — fully scaffolded so the user can start coding immediately without setting anything up themselves. Also use this skill to check project progress ("where am I", "what's left") by reading progress.md.
---

# New Lesson

Turns the project roadmap (`references/roadmap.md`) into one concrete,
ready-to-start lesson at a time — description, plan, links, task, and a
scaffolded folder with starter files and dependencies installed.

## Before generating a lesson

1. Read `progress.md` at the project root (create it if it doesn't exist —
   see `references/progress-template.md`). It lists which lessons are
   done, in progress, or not started.
2. Read `references/roadmap.md` in this skill. It breaks the six project
   stages into individual lessons, each with its key question and
   literature links.
3. Pick the next lesson:
   - If a lesson is marked "in progress", resume that one (ask the user
     if they want to continue it or restart).
   - Otherwise, pick the first "not started" lesson in stage order.
   - If the user names a specific stage or topic explicitly, honor that
     instead of the automatic pick.
   - Stage 00 (foundations) is a prerequisite, not optional filler —
     don't skip ahead to stage 01 just because it sounds more exciting.
     Only skip it if the user has explicitly said they already know
     backprop/MLPs well enough to skip it.

## Generating the lesson

Create a folder at `lessons/<stage-id>-<stage-slug>/<lesson-id>-<lesson-slug>/`
(e.g. `lessons/01-modern-stack/02-rmsnorm/`), matching the ids in
`references/roadmap.md`. Inside it, create:

- **`README.md`** — the lesson itself, following `references/lesson-template.md`:
  description, plan (ordered steps), study links, and the concrete task
  with a clear "done" condition. Pull the core links straight from
  `references/roadmap.md` — don't invent new ones. Then, per CLAUDE.md's
  research rule, search the web for a Russian-language article or video
  on the lesson's specific topic (e.g. this lesson's flavor of RoPE/DPO/
  quantization, not just the general subject) and add it if it's solid,
  alongside the existing links, not replacing them.
- **Starter code file(s)** (e.g. `lesson.py`) — a skeleton with function
  signatures, docstrings, and `# TODO` markers where the user implements
  the logic. Never fill in the actual implementation — that defeats the
  point of the project (see CLAUDE.md: this is a learning project, not a
  delivery project).
- **A test/check file** (e.g. `check.py`) when the lesson has a
  verifiable output (shapes match, loss decreases, outputs equal a
  reference within tolerance, etc.). Skip it for lessons that are
  inherently exploratory (e.g. reading + writing a notes file).

## Dependencies

- Maintain a single `requirements.txt` (or `pyproject.toml`, matching
  whatever the project already uses) at the project root — don't create
  a separate one per lesson.
- Before writing the lesson, check what the lesson needs (e.g. `torch`,
  `numpy`, `matplotlib` for scaling-curve plots, `tiktoken` only if
  explicitly comparing against it) and add anything missing.
- Install what's missing with `pip install --break-system-packages -r requirements.txt`
  (or the project's existing install command, if a venv is already set
  up — check for one first) so the user can run the lesson immediately.
- Don't add a library the lesson is meant to reimplement (e.g. don't add
  `sentencepiece` for the BPE-from-scratch lesson).

## After generating

- Update `progress.md`: mark the new lesson "in progress".
- Tell the user, briefly: which lesson this is, why it's next, and where
  the folder is. Don't repeat the full README content in the chat — they
  can open the file.
- Follow CLAUDE.md's response style (concise, precise, simple) and
  language rule (English, with error correction if needed) for this
  summary — the lesson content itself stays as written in roadmap.md
  (mixed English/Russian sources, as-is).

## Marking a lesson done

If the user says they finished a lesson (or asks you to check it), run
the check file if present, review their implementation against the
lesson's task, and if it holds up, update `progress.md` to "done" with
one line on what they implemented. Then offer to generate the next
lesson — don't auto-generate it without asking.

## Progress questions

If the user asks where they are or what's left, read `progress.md` and
summarize it briefly (stage-by-stage counts, what's in progress) rather
than dumping the whole file.
