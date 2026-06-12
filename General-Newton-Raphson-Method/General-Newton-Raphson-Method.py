# General-Newton-Raphson-Method
import numpy as np


def poly(coeffs, x):
    """
    coeffs = [a1,a2,...,an]
    a1*x^n + a2*x^(n-1)+...
    """
    n = len(coeffs) - 1
    s = 0

    for i, a in enumerate(coeffs):
        s += a * x**(n - i)

    return s


def dpoly(coeffs, x):

    n = len(coeffs) - 1
    s = 0

    for i, a in enumerate(coeffs[:-1]):
        power = n - i
        s += power * a * x**(power - 1)

    return s


# f = x^2 - y^2 -4
ax = [1, 0, 0]
ay = [-1, 0, -4]

# g = x^2 + y^2 -16
bx = [1, 0, 0]
by = [1, 0, -16]


def f(x, y):
    return poly(ax, x) + poly(ay, y)


def g(x, y):
    return poly(bx, x) + poly(by, y)


def fx(x, y):
    return dpoly(ax, x)


def fy(x, y):
    return dpoly(ay, y)


def gx(x, y):
    return dpoly(bx, x)


def gy(x, y):
    return dpoly(by, y)


x = 3
y = 2

tol = 1e-10

for i in range(100):

    F = f(x, y)
    G = g(x, y)

    D = fx(x, y)*gy(x, y) - fy(x, y)*gx(x, y)

    if abs(D) < 1e-14:
        print("Jacobian is 0")
        break

    h = ((-F)*gy(x, y) - fy(x, y)*(-G)) / D

    k = (fx(x, y)*(-G) - (-F)*gx(x, y)) / D

    x_new = x + h
    y_new = y + k

    print(i+1, x_new, y_new)

    if abs(h) < tol and abs(k) < tol:
        break

    x = x_new
    y = y_new


print("\n Answers:")
print("x =", x)
print("y =", y)
