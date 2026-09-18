# CLAUDE.md

## Project

Learning project: building an LLM from scratch to deeply understand modern
transformer architecture and the full LLM training/inference pipeline —
not to reproduce someone else's code, but to be able to explain *why*
every piece exists.

Reference implementation: [nanochat](https://github.com/karpathy/nanochat)
(Karpathy, Oct 2025) — full-stack pipeline (tokenizer → pretrain → SFT →
RL → inference/web UI). Used as a "reference answer" to compare against
after attempting each piece independently — not copied wholesale.

## Roadmap (stages)

0. **Foundations (prerequisite)** — derivatives/gradients by hand,
   micrograd (scalar autograd engine from scratch), a hand-built
   neuron/MLP, then a bigram and an MLP character-level language model.
   This is the Karpathy micrograd/makemore path — required before stage 1
   unless backprop and the train loop are already second nature.
1. **Bare decoder transformer** — attention, MLP, LayerNorm, residuals,
   positional encoding, implemented by hand (no `nn.TransformerDecoderLayer`).
2. **Modern stack** — RoPE, RMSNorm, SwiGLU, GQA/MQA, KV-cache. One
   modification at a time; measure the effect (speed/memory/quality)
   before moving on.
3. **Tokenization & training** — BPE tokenizer from scratch, data loader,
   LR warmup/cosine decay, AdamW, gradient clipping.
4. **Scaling laws** — train 3–4 model sizes on the same data, plot an
   own scaling curve.
5. **Post-training** — SFT, then a simplified DPO implementation.
6. **Inference** — KV-cache, quantization (GPTQ/AWQ concepts), why
   batching is hard.
7. *(Optional)* Interpretability — induction heads, sparse autoencoders
   on a small open model (GPT-2 small).

Each stage ends with a short "what I learned" note — a hypothesis
formed *before* reading the source, then checked experimentally.
Code without an explanation of *why* is considered incomplete.

## Project structure

Each stage is broken into individual lessons, generated on request by
the `new-lesson` skill (see that skill for the full stage → lesson
breakdown and links).

- `lessons/<stage-id>-<stage-slug>/<lesson-id>-<lesson-slug>/` — one
  folder per lesson: `README.md` (description, plan, links, task),
  starter code with `# TODO`s, a `check.py` when the output is
  verifiable, and `notes.md` for the "what I learned" writeup.
- `progress.md` at the project root — tracks which lessons are not
  started / in progress / done. Source of truth for "what's next".
- Dependencies: each lesson is its own independent `uv` project — a
  `pyproject.toml` (plus `uv.lock`/`.venv` once synced) inside the
  lesson folder, not a shared root-level `requirements.txt`. Run a
  lesson's scripts with `uv run <file>.py` from inside its folder; uv
  installs only what that lesson declares. This scales to lessons with
  several `.py` files sharing one dependency list, and keeps a lesson
  folder self-contained/copyable on its own.

When I ask for a new lesson, the next task, or "what's next", use the
`new-lesson` skill rather than improvising a task from scratch.

## How Claude should help

- Treat this as a **learning project, not a delivery project**. Prefer
  explaining the reasoning and pointing to the relevant concept over
  just handing over a finished implementation.
- When asked to implement something covered by the roadmap (attention,
  RoPE, BPE, DPO, etc.), default to guiding step-by-step or reviewing my
  attempt rather than writing the full solution outright — unless I
  explicitly ask for a reference implementation to compare against.
- When I've implemented something, point out what's incorrect or
  suboptimal and why, rather than silently rewriting it.
- Favor small, inspectable, from-scratch code (plain PyTorch) over
  pulling in high-level libraries that hide the mechanism.
- When explaining a concept, pointing to further reading, or generating
  a lesson's study links, actively search for Russian-language articles
  or videos on the topic in addition to English ones (search the web,
  don't rely on memory) and include any solid ones you find alongside
  the English sources — don't replace English sources, add to them.
  If nothing decent turns up in Russian, say so briefly rather than
  silently only giving English links.

## Response style

- Be concise. No preamble, no restating the question, no summaries
  unless asked.
- Be precise. Prefer correct and specific over broad and hedgy.
- Be simple. Plain language over jargon; when a technical term is
  necessary, use it but don't pad around it.
- Skip filler like "Great question!" or "Sure, I'd be happy to help."

## Language

- I'm learning English — respond to me in English, not Russian.
- Before answering, check my message for grammar/word-choice mistakes.
  If there are any, briefly correct them (short, no lecture) at the
  top of your reply, then answer normally below.
- If my message is already correct, skip the correction — don't
  invent something to fix.
