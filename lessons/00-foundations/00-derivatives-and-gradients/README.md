# Lesson 00.00: Derivatives and Gradients

## Description
The first lesson of the project, before any code that resembles a
neural net. Every later stage — micrograd's `.backward()`, PyTorch's
autograd, gradient descent on a transformer — is built on one idea:
a derivative tells you how much (and in which direction) an output
changes when an input changes a little. This lesson makes that idea
concrete by hand, with no autograd library doing the work for you.

## Key question
What actually happens when a network "learns" — before touching
attention at all: "gradient = direction that increases the output"
becomes obvious, not memorized.

## Plan
1. On paper, work out the derivative of `f1(x) = x**2 + 3*x - 5`
   from the limit definition or the power rule — whichever you trust
   more right now.
2. On paper, work out `d/dx [sin(x) * x]` using the product rule.
3. On paper, work out the gradient (partial derivatives w.r.t. `x`
   and `y`) of `f3(x, y) = x**2 * y + y**3`.
4. Unsure about any of the three, or want to double-check your
   intuition before moving on? That's what the study links below are
   for — a video on what a single-variable derivative means, and an
   article on how that generalizes to a gradient and feeds gradient
   descent. Skip them if steps 1–3 already felt solid.
5. Encode the three analytical results as `df1`, `df2`, `grad_f3` in
   `lesson.py`.
6. Implement `numerical_derivative` and `numerical_gradient` in
   `lesson.py` using the central-difference formula
   `(f(x+h) - f(x-h)) / (2*h)`. This is what "derivative" means
   operationally, before any symbolic shortcut.
7. Run `check.py`. It independently verifies your `df1`/`df2`/`grad_f3`
   against finite differences at several random points.
8. Small experiment (no code file needed, just run it in a Python
   shell or scratch script): pick a starting point `(x0, y0)`, compute
   `grad_f3(x0, y0)`, then evaluate `f3` at
   `(x0, y0) + 0.01 * grad` and at `(x0, y0) - 0.01 * grad`. Confirm
   the first is bigger and the second is smaller than `f3(x0, y0)`.
9. Write 3–5 sentences in `notes.md`: what you expected the gradient
   direction to mean before step 8, what you observed, and why the
   sign of the step matters. This is the whole idea behind gradient
   descent — one line connecting this to what's coming in stage 00
   lesson 01 (micrograd) is enough.

## Study links
- 3Blue1Brown, ["The paradox of the derivative | Chapter 2, Essence of calculus"](https://www.youtube.com/watch?v=9vKqVkMQHKk) (video) — what "instantaneous rate of change" means, built up visually from first principles.
- Habr (RU), ["Градиентный спуск по косточкам"](https://habr.com/ru/articles/467185/) — geometric meaning of the derivative and how it leads to gradient descent, worked through step by step.

## Task
Implement `df1`, `df2`, `grad_f3`, `numerical_derivative`, and
`numerical_gradient` in `lesson.py` (see `# TODO` markers). Done
condition: `python check.py` prints `ALL CHECKS PASSED`. Then run the
step-8 experiment and write `notes.md`.

## Files in this lesson
- `lesson.py` — starter code, implement the TODOs
- `check.py` — run this to verify your implementation
- `notes.md` — write your findings here (stub already created)
