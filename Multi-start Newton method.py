
#  Multi-start Newton method

def f(x, y):
    return x**2 - y**2 - 4

def g(x, y):
    return x**2 + y**2 - 16

def fx(x, y):
    return 2*x

def fy(x, y):
    return -2*y

def gx(x, y):
    return 2*x

def gy(x, y):
    return 2*y

def newton(x0, y0, tol=1e-10, max_iter=100):

    for _ in range(max_iter):

        F = f(x0, y0)
        G = g(x0, y0)

        D = fx(x0, y0)*gy(x0, y0) - fy(x0, y0)*gx(x0, y0)

        if abs(D) < tol:
            return None

        h = ((-F)*gy(x0, y0) - fy(x0, y0)*(-G)) / D
        k = (fx(x0, y0)*(-G) - (-F)*gx(x0, y0)) / D

        x1 = x0 + h
        y1 = y0 + k

        if abs(h) < tol and abs(k) < tol:
            return round(x1, 10), round(y1, 10)

        x0 = x1
        y0 = y1

    return None

guesses = [
    (2, 2),
    (2, -2),
    (-2, 2),
    (-2, -2)
]

solutions = set()

for xg, yg in guesses:
    sol = newton(xg, yg)

    if sol is not None:
        solutions.add(sol)

print("All answers:")
for s in solutions:
    print(s)
