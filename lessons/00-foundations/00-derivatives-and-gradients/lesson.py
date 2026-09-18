"""
Stage 00, Lesson 00: Derivatives and gradients, by hand.

No autograd anywhere in this file. Work out each derivative on paper
first (see README.md, Plan steps 1-3), then encode the result here.
"""
import math


def f1(x):
    """f1(x) = x**2 + 3*x - 5"""
    return x ** 2 + 3 * x - 5


def df1(x):
    """Analytical derivative of f1 w.r.t. x.

    TODO: work out d/dx (x**2 + 3*x - 5) on paper, then return it.
    """
    raise NotImplementedError


def f2(x):
    """f2(x) = sin(x) * x"""
    return math.sin(x) * x


def df2(x):
    """Analytical derivative of f2 w.r.t. x (product rule).

    TODO: work out d/dx (sin(x) * x) on paper, then return it.
    """
    raise NotImplementedError


def f3(x, y):
    """f3(x, y) = x**2 * y + y**3"""
    return x ** 2 * y + y ** 3


def grad_f3(x, y):
    """Analytical gradient of f3 w.r.t. (x, y).

    TODO: work out df3/dx and df3/dy on paper, then return them as
    the tuple (df3/dx, df3/dy).
    """
    raise NotImplementedError


def numerical_derivative(f, x, h=1e-5):
    """Central-difference approximation of f'(x).

    TODO: implement (f(x + h) - f(x - h)) / (2 * h)
    """
    raise NotImplementedError


def numerical_gradient(f, x, y, h=1e-5):
    """Central-difference approximation of the gradient of f(x, y).

    TODO: perturb x and y independently (holding the other fixed),
    return the tuple (df/dx, df/dy).
    """
    raise NotImplementedError


if __name__ == "__main__":
    # Quick manual sanity check while you work.
    print("df1(2.0) =", df1(2.0), "  numerical:", numerical_derivative(f1, 2.0))
    print("df2(1.0) =", df2(1.0), "  numerical:", numerical_derivative(f2, 1.0))
    print("grad_f3(1.0, 2.0) =", grad_f3(1.0, 2.0),
          "  numerical:", numerical_gradient(f3, 1.0, 2.0))
