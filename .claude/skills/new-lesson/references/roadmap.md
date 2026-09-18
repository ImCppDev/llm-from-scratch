# Roadmap → lessons

Each stage from the project roadmap, broken into individual lessons.
IDs are used for folder names: `lessons/<stage-id>-<stage-slug>/<lesson-id>-<lesson-slug>/`.

Reference implementation throughout stages 01+: [nanochat](https://github.com/karpathy/nanochat)
(Karpathy, Oct 2025) — read the matching source file *after* attempting
the lesson, not before.

---

## Stage 00 — foundations (prerequisite)

**Overarching question:** what actually happens when a network "learns" —
before touching attention at all. This stage exists because attention
assumes fluency with gradients, backprop, and the train loop; skipping
it turns the later stages into cargo-culting. Skip this stage entirely
only if you can already write a training loop and explain backprop
without looking anything up.

- **00-derivatives-and-gradients** — By hand (paper or a tiny script,
  no autograd), compute derivatives of a few small expressions and the
  gradient of a 2-input function. Goal: "gradient = direction that
  increases the output" becomes obvious, not memorized.
- **01-micrograd** — Build a tiny scalar-valued autograd engine from
  scratch: a `Value` class with `+`, `*`, `tanh`, and a `.backward()`
  that does reverse-mode autodiff via a manually built computation
  graph. This is *the* lesson that makes backprop stop being magic.
  - Karpathy, ["The spelled-out intro to neural networks and backpropagation: building micrograd"](https://www.youtube.com/watch?v=VMj-3S1tku0) (video, ~2h25m)
  - Repo: [karpathy/micrograd](https://github.com/karpathy/micrograd)
- **02-neuron-layer-mlp** — On top of your own micrograd, implement a
  single neuron, a layer, and a small MLP; train it on a toy binary
  classification dataset with plain gradient descent (no PyTorch yet).
- **03-bigram-language-model** — Build the simplest possible language
  model: a character-level bigram model (first via counting, then via
  a 1-layer neural net trained with your own or real gradient descent).
  First real contact with "language model" as a concept, at the
  smallest possible scale.
  - Karpathy, ["The spelled-out intro to language modeling: building makemore"](https://www.youtube.com/watch?v=PaCmpygFfXo) (video, ~1h57m)
  - Repo: [karpathy/makemore](https://github.com/karpathy/makemore)
- **04-mlp-language-model** — Extend the bigram model into an MLP-based
  character-level language model (embedding lookup + hidden layer +
  softmax), now in real PyTorch — this is the bridge from "I built
  autograd by hand" to "I use PyTorch's autograd, but I know what it's
  doing underneath."
  - Karpathy, ["Building makemore Part 2: MLP"](https://www.youtube.com/watch?v=TCH_1BHY58I) (video, ~1h15m)

*(Optional, not required to move on: Karpathy's makemore Part 3 (BatchNorm),
Part 4 ("Becoming a Backprop Ninja" — manual backprop through a real net),
and Part 5 (WaveNet-style hierarchical model) go deeper into the same
foundations. Worth returning to later if stage 01 feels shaky in
retrospect.)*

---

## Stage 01 — bare-transformer

**Overarching question:** why is the transformer built the way it is?

- **00-self-attention** — Implement single-head self-attention from
  scratch (QK^T/√d, softmax, weighted sum of V). No `nn.MultiheadAttention`.
  - Karpathy, ["Let's build GPT"](https://www.youtube.com/watch?v=kCc8FmEb1nY) (video)
  - Jay Alammar, ["The Illustrated Transformer"](https://jalammar.github.io/illustrated-transformer/)
- **01-multi-head-attention** — Extend to multi-head; understand why
  splitting into heads instead of one big attention helps.
  - Same sources as above.
- **02-positional-encoding** — Implement sinusoidal positional encoding;
  ablate it (run without) and observe what breaks.
  - Habr (RU), ["Позиционное кодирование — разбор с собеседования"](https://habr.com/ru/articles/926368/)
  - Vaswani et al., ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762)
- **03-mlp-block** — Implement the position-wise feed-forward block.
- **04-norm-and-residuals** — Implement LayerNorm + residual connections;
  ablate both (remove residuals; move norm post-block vs pre-block) and
  observe training stability differences.
- **05-assemble-mini-gpt** — Stack blocks into a full decoder-only mini
  model; train it on a tiny toy dataset (character-level) end to end.
  - Repo: [nanoGPT-lecture](https://github.com/karpathy/ng-video-lecture)

## Stage 02 — modern-stack

**Overarching question:** what changed since GPT-2, and why, feature by feature?

- **00-rope** — Replace absolute positional encoding with RoPE.
  - Habr (RU), ["ruRoPEBert"](https://habr.com/ru/articles/797561/)
  - Su et al., ["RoFormer"](https://arxiv.org/abs/2104.09864)
- **01-rmsnorm** — Replace LayerNorm with RMSNorm; compare compute cost.
- **02-swiglu** — Replace ReLU/GELU MLP with SwiGLU.
  - Shazeer, ["GLU Variants Improve Transformer"](https://arxiv.org/abs/2002.05202)
- **03-gqa** — Implement grouped-query attention; measure memory savings
  vs full multi-head attention.
  - Ainslie et al., ["GQA"](https://arxiv.org/abs/2305.13245)
- **04-kv-cache** — Implement KV-cache for autoregressive generation;
  benchmark generation speed with/without it.
  - Karpathy, ["Let's reproduce GPT-2 (124M)"](https://www.youtube.com/watch?v=l8pRSuU81PU) (video)
  - Repo: [build-nanogpt](https://github.com/karpathy/build-nanogpt)

## Stage 03 — tokenization-and-training

**Overarching question:** how does raw text become what the network trains on, and why is training set up this way?

- **00-bpe-tokenizer** — Implement a BPE tokenizer from scratch (no library).
  - Karpathy, ["Let's build the GPT Tokenizer"](https://www.youtube.com/watch?v=zduSFxRajkE) (video)
  - Repo: [minbpe](https://github.com/karpathy/minbpe)
  - Sennrich et al., ["BPE for NMT"](https://arxiv.org/abs/1508.07909)
- **01-dataloader-and-batching** — Build a data loader with batching and
  shuffling for the toy dataset.
- **02-lr-schedule** — Implement warmup + cosine decay; plot LR over
  training and its effect on loss.
- **03-adamw-and-clipping** — Implement/use AdamW; add gradient clipping;
  observe what happens without it.
  - Loshchilov & Hutter, ["Decoupled Weight Decay Regularization"](https://arxiv.org/abs/1711.05101)
- **04-full-training-loop** — Put it all together: train the mini-GPT
  from stage 01 with the stage 02 modern-stack pieces, this tokenizer,
  and this training setup.

## Stage 04 — scaling-laws

**Overarching question:** why does bigger predictably mean better, and in what proportion?

- **00-train-multiple-sizes** — Train 3–4 model sizes (~1M/10M/50M
  params) on identical data.
  - Kaplan et al., ["Scaling Laws for Neural Language Models"](https://arxiv.org/abs/2001.08361)
  - Hoffmann et al., ["Chinchilla"](https://arxiv.org/abs/2203.15556)
- **01-plot-scaling-curve** — Plot loss vs. compute/params/tokens for
  your own runs; compare the fitted exponent to Kaplan/Chinchilla.

## Stage 05 — post-training

**Overarching question:** what's the difference between "predicts next token" and "answers questions"?

- **00-sft** — Fine-tune the pretrained mini model on a small instruction
  dataset.
  - Ouyang et al., ["InstructGPT"](https://arxiv.org/abs/2203.02155)
- **01-dpo** — Implement a simplified DPO loss and fine-tune on a small
  preference dataset.
  - Habr (RU), ["От RLHF к DPO и дальше"](https://habr.com/ru/articles/1002298/)
  - Habr (RU), ["Proximal Policy Optimization"](https://habr.com/ru/posts/861408/)
  - Rafailov et al., ["DPO"](https://arxiv.org/abs/2305.18290)

## Stage 06 — inference

**Overarching question:** why is inference a separate engineering discipline?

- **00-kv-cache-serving** — Wire the stage-02 KV-cache into a simple
  generation/serving loop; benchmark throughput.
- **01-quantization** — Quantize the trained model to int8 (simplified
  GPTQ/AWQ-style); measure quality loss vs. memory savings.
  - Habr (RU), ["Квантизация LLM"](https://habr.com/ru/articles/975468/)
  - Frantar et al., ["GPTQ"](https://arxiv.org/abs/2210.17323)
  - Lin et al., ["AWQ"](https://arxiv.org/abs/2306.00978)
- **02-batching-concepts** — Read/summarize continuous batching (no
  full implementation needed — this lesson is exploratory/notes-only).
  - Kwon et al., ["PagedAttention / vLLM"](https://arxiv.org/abs/2309.06180)

## Stage 07 — interpretability (optional)

**Overarching question:** what is the model actually doing internally?

- **00-induction-heads** — Find induction heads in a small open model
  (GPT-2 small) by hand.
  - Anthropic, [Transformer Circuits Thread](https://transformer-circuits.pub/)
  - Neel Nanda, [Mechanistic Interpretability glossary](https://www.neelnanda.io/mechanistic-interpretability/glossary)
- **01-sparse-autoencoder** — Train a small sparse autoencoder on the
  same model's activations; inspect a few learned features.
