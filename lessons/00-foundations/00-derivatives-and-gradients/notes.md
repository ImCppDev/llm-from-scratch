# Notes — Lesson 00.00: Derivatives and Gradients

## Hypothesis (before)
Before doing the step-7 experiment: what do you expect `grad_f3(x0, y0)`
to mean, directionally? What do you expect to happen to `f3` when you
step *with* the gradient vs. *against* it?

## Observation
What actually happened when you evaluated `f3` at
`(x0, y0) + 0.01 * grad` and `(x0, y0) - 0.01 * grad`?

## Why
Why does stepping with the gradient increase `f3`, and against it
decrease `f3`? Tie this back to the key question: why is this the
same idea gradient descent (coming in lesson 00.01, micrograd) uses
to make a network "learn"?
