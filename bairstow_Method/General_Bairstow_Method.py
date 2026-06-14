import numpy as np

def bairstow(coeffs, r=0.1, s=0.1, tol=1e-12, max_iter=100):

    a = np.array(coeffs, dtype=float)
    n = len(a) - 1

    for iteration in range(max_iter):

        b = np.zeros(n + 1)
        c = np.zeros(n + 1)

        b[0] = a[0]
        b[1] = a[1] + r * b[0]

        for i in range(2, n + 1):
            b[i] = a[i] + r * b[i - 1] + s * b[i - 2]

        c[0] = b[0]
        c[1] = b[1] + r * c[0]

        for i in range(2, n):
            c[i] = b[i] + r * c[i - 1] + s * c[i - 2]

        R1 = b[n]
        R0 = b[n - 1]

        if abs(R1) < tol and abs(R0) < tol:
            break

        det = c[n - 2]**2 - c[n - 3] * c[n - 1]

        dr = (-R0 * c[n - 2] + R1 * c[n - 3]) / det
        ds = (-R1 * c[n - 2] + R0 * c[n - 1]) / det

        r += dr
        s += ds

    disc = r**2 + 4 * s

    root1 = (r + np.sqrt(disc)) / 2
    root2 = (r - np.sqrt(disc)) / 2

    return root1, root2, r, s


coeff_x = [1, 0, -10]

x1, x2, r, s = bairstow(coeff_x)

print("x roots:")
print(x1, x2)


coeff_y = [1, 0, -6]

y1, y2, r, s = bairstow(coeff_y)

print("\ny roots:")
print(y1, y2)
