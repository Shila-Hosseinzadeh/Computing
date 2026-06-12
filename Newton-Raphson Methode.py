

# Newton-Raphson Methode

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

x0 = 4
y0 = 1.0


tol = 1e-10
max_iter = 100

print("iter             x                y                 D                   h                  k ")

for i in range(max_iter):
 
    F = f(x0, y0)
    G = g(x0, y0)

    D = fx(x0, y0)*gy(x0, y0) - fy(x0, y0)*gx(x0, y0)


    if abs(D) == 0:
        print(" Jacobian = 0 ")
        print(" Warning : The initial answers were not selected correctly.")
        print(" Change the initial default values.")
        break

    h = ((-F)*gy(x0, y0) - fy(x0, y0)*(-G)) / D

    k = (fx(x0, y0)*(-G) - (-F)*gx(x0, y0)) / D

    x1 = x0 + h
    y1 = y0 + k

    print(f" {i+1:2d}    {x1:.10f}    {y1:.10f}     {D:.10f}   {h:.10f}     {k:.10f}")

    if abs(h) < tol and abs(k) < tol:
        break

    x0 = x1
    y0 = y1

print("\n final answers:")
print("x =", x0)
print("y =", y0)
