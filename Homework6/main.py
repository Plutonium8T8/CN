import random
import math
import tkinter as tk
from tkinter import ttk


def f_x(x):
    return x * x - 12 * x + 30
    # return math.sin(x) - math.cos(x)
    # return 2 * pow(x,3) - 3 * x + 15


def gen_xi(x0, xn, n):
    X = [x0, xn]
    for i in range(n - 2):
        X.append(random.uniform(x0, xn))
    X.sort()
    return X


def diferente_divizate(X, Y):
    n = len(X)
    f = [[None] * n for i in range(n)]
    for i in range(n):
        f[i][0] = Y[i]
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (X[i + j] - X[i])
    return f[0]


# a doua forma Newton a polinomului de interpolare Lagrange:
# Ln(x) = y0 + [x0, x1]f (x − x0) + [x0, x1, x2]f (x − x0)(x − x1) + [x0, . . . , xn]f (x − x0)(x − x1)· · ·(x − xn−1)
def lagrange(X, Y, x_bar):
    n = len(X)
    f = diferente_divizate(X, Y)
    y = f[n - 1]
    for i in range(n - 2, -1, -1):
        y = f[i] + (x_bar - X[i]) * y
    return y


def xi_in_Y(X):
    Y = []
    for x in X:
        Y.append(f_x(x))
    return Y


# x0 = 1
# xn = 5

x0 = 0
xn = 1.5

# x0 = 0
# xn = 2

n = 7  # nr elem

X = gen_xi(x0, xn, n)
Y = xi_in_Y(X)

X_bar = x0
while X_bar in X:
    X_bar = random.uniform(x0, xn)

Ln_x = lagrange(X, Y, X_bar)

print("X:", X)
print("Y:", Y)
print()
print("X_bar:", X_bar)
print("f(x_bar):", f_x(X_bar))
print()
print("Polinomul de interpolare Ln(x) este:", Ln_x)
print("|Ln(x) - f(x)| este:", abs(Ln_x - f_x(X_bar)))


def function1():
    result_label.config(text=str(X))


def function2():
    result_label.config(text=str(Y))


def function3():
    result_label.config(text=str(X_bar))


def function4():
    result_label.config(text=str(f_x(X_bar)))


def function5():
    result_label.config(text=str(Ln_x))


def function6():
    result_label.config(text=str(abs(Ln_x - f_x(X_bar))))


root = tk.Tk()

style = ttk.Style()
style.configure("TButton", font=("TkDefaultFont", 12), padding=6)

button1 = tk.Button(root, text="X", command=function1)
button1.pack(padx=20, pady=10)

button2 = tk.Button(root, text="Y", command=function2)
button2.pack(padx=20, pady=10)

button3 = tk.Button(root, text="X_bar", command=function3)
button3.pack(padx=20, pady=10)

button4 = tk.Button(root, text="f(x_bar)", command=function4)
button4.pack(padx=20, pady=10)

button5 = tk.Button(root, text="Ln(x)", command=function5)
button5.pack(padx=20, pady=10)

button6 = tk.Button(root, text="|Ln(x) - f(x)|", command=function6)
button6.pack(padx=20, pady=10)

separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", padx=20, pady=10)

result_label = ttk.Label(root, font=("TkDefaultFont", 12))
result_label.pack(padx=20, pady=10)

root.mainloop()
