"""
Checks lesson.py's analytical derivatives/gradient against an
independent finite-difference reference (not the student's own
numerical_derivative/numerical_gradient, so a bug in one can't hide
a bug in the other), plus a sanity check that the student's own
finite-difference implementation is also correct.
"""
import random

import lesson


def _ref_derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def _ref_gradient(f, x, y, h=1e-6):
    dfdx = (f(x + h, y) - f(x - h, y)) / (2 * h)
    dfdy = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return dfdx, dfdy


def check_close(name, got, expected, tol=1e-3):
    if isinstance(expected, tuple):
        ok = all(abs(g - e) < tol for g, e in zip(got, expected))
    else:
        ok = abs(got - expected) < tol
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {name}: got={got}, expected~={expected}")
    return ok


def main():
    random.seed(0)
    all_ok = True

    for x in [random.uniform(-5, 5) for _ in range(5)]:
        all_ok &= check_close(f"df1({x:.3f})", lesson.df1(x), _ref_derivative(lesson.f1, x))

    for x in [random.uniform(-5, 5) for _ in range(5)]:
        all_ok &= check_close(f"df2({x:.3f})", lesson.df2(x), _ref_derivative(lesson.f2, x))

    for x, y in [(random.uniform(-5, 5), random.uniform(-5, 5)) for _ in range(5)]:
        all_ok &= check_close(
            f"grad_f3({x:.3f}, {y:.3f})", lesson.grad_f3(x, y), _ref_gradient(lesson.f3, x, y)
        )

    # Sanity-check the student's own finite-difference implementations
    # against the same independent reference.
    all_ok &= check_close(
        "numerical_derivative(f1, 2.0)",
        lesson.numerical_derivative(lesson.f1, 2.0),
        _ref_derivative(lesson.f1, 2.0),
    )
    all_ok &= check_close(
        "numerical_gradient(f3, 1.0, 2.0)",
        lesson.numerical_gradient(lesson.f3, 1.0, 2.0),
        _ref_gradient(lesson.f3, 1.0, 2.0),
    )

    print()
    print("ALL CHECKS PASSED" if all_ok else "SOME CHECKS FAILED")


if __name__ == "__main__":
    main()
