import numpy as np

# P(x)=2x^5+5x^3-7x^2+34

a1 = 2
a2 = 0
a3 = 5
a4 = -7
a5 = 0
a6 = 34


def b_values(r, s):

    b1 = a1

    b2 = a2 + r*b1

    b3 = a3 + r*b2 + s*b1

    b4 = a4 + r*b3 + s*b2

    b5 = a5 + r*b4 + s*b3

    b6 = a6 + r*b5 + s*b4

    return b1, b2, b3, b4, b5, b6




def f(r, s):

    _, _, _, _, b5, _ = b_values(r, s)

    return b5


def g(r, s):

    _, _, _, _, _, b6 = b_values(r, s)

    return b6



def fx(r, s):

    return (
        8*r**3
        + 10*r
        - 7
        + 12*r*s
    )


def fy(r, s):

    return (
        6*r**2
        + 5
        + 4*s
    )


def gx(r, s):

    b4 = (
        -7
        + 5*r
        + 2*r**3
        + 4*r*s
    )

    return (
        f(r, s)
        + r*fx(r, s)
        + s*(5 + 6*r**2 + 4*s)
    )


def gy(r, s):

    b4 = (
        -7
        + 5*r
        + 2*r**3
        + 4*r*s
    )

    return (
        r*fy(r, s)
        + b4
        + 4*r*s
    )


r0 = 1.0
s0 = 1.0

tol = 1e-10
max_iter = 100

print("iter           r                 s")


for i in range(max_iter):

    F = f(r0, s0)
    G = g(r0, s0)

    D = (
        fx(r0, s0)*gy(r0, s0)
        - fy(r0, s0)*gx(r0, s0)
    )

    if abs(D) < 1e-14:
        print("Jacobian = 0")
        break

    # h
    h = (
        (-F)*gy(r0, s0)
        - fy(r0, s0)*(-G)
    ) / D

    # k
    k = (
        fx(r0, s0)*(-G)
        - (-F)*gx(r0, s0)
    ) / D

    r1 = r0 + h
    s1 = s0 + k

    print(
        f"{i+1:2d}      "
        f"{r1:.12f}      "
        f"{s1:.12f}"
    )

    if abs(h) < tol and abs(k) < tol:
        break

    r0 = r1
    s0 = s1




b1, b2, b3, b4, b5, b6 = b_values(r1, s1)

print("\n b :")

print("b1 =", b1)
print("b2 =", b2)
print("b3 =", b3)
print("b4 =", b4)
print("b5 =", b5)
print("b6 =", b6)


# x²-rx-s=0

print(f"x² - ({r1})x - ({s1}) = 0")

D2 = r1**2 + 4*s1

x1 = (r1 + np.sqrt(D2))/2
x2 = (r1 - np.sqrt(D2))/2

print("\n roots :")

print("x1 =", x1)
print("x2 =", x2)
