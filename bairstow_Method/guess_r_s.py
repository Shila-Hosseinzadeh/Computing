import numpy as np

def f(r, s):
    b = 2 * r
    d = 34 / s
    c = -(r * d) / s

    return c - r*b - 2*s + 6


def g(r, s):
    b = 2 * r
    d = 34 / s
    c = -(r * d) / s

    return d - r*c - s*b - 7


def derivative_x(func, r, s, eps=1e-8):
    return (func(r + eps, s) - func(r, s)) / eps


def derivative_y(func, r, s, eps=1e-8):
    return (func(r, s + eps) - func(r, s)) / eps


r = 1.0
s = 2.0

tol = 1e-10

print("iter        r               s")

for i in range(50):

    F = f(r, s)
    G = g(r, s)

    fx = derivative_x(f, r, s)
    fy = derivative_y(f, r, s)

    gx = derivative_x(g, r, s)
    gy = derivative_y(g, r, s)

    # دترمینان ژاکوبین
    D = fx*gy - fy*gx

    h = ((-F)*gy - fy*(-G)) / D
    k = (fx*(-G) - (-F)*gx) / D

    r_new = r + h
    s_new = s + k

    print(i+1, r_new, s_new)

    if abs(h) < tol and abs(k) < tol:
        break

    r = r_new
    s = s_new


print("\nr =", r)
print("s =", s)



disc = r**2 + 4*s

x1 = (r + np.sqrt(disc)) / 2
x2 = (r - np.sqrt(disc)) / 2

print("\n roots:")
print(x1)
print(x2)
