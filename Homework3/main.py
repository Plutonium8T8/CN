import numpy as np
import math
from copy import copy, deepcopy
import tkinter as tk
from tkinter import ttk
import numpy.linalg
import sys


def StrToMatrix(matrix_str):
    matrix = []
    row_array = []
    auxiliar = 0
    for index in range(len(matrix_str)):
        if matrix_str[index] == ' ':
            row_array.append(float(matrix_str[auxiliar:index]))
            auxiliar = index + 1
            row_array

        if matrix_str[index] == '\n':
            row_array.append(float(matrix_str[auxiliar:index]))
            matrix.append(row_array)
            row_array = []
            auxiliar = index + 1

    return matrix


input = 2  # 1 - read from file, 2 - random input
if input == 1:
    file = open("matrix1.txt", "r")
    matrix_str = file.read()
    matrix = StrToMatrix(matrix_str)
    matrix = np.array(matrix)
    matrix2 = deepcopy(matrix)
    s = [3, 2, 1]
    n = 3
else:
    n = np.random.randint(2, 10)
    matrix = np.random.rand(n, n).tolist()
    matrix2 = deepcopy(matrix)
    s = np.random.rand(n)

# 1
b = []  # create empty vector b
for i in range(n):
    bi = 0  # initialize value of b at position i
    for j in range(n):
        bi += s[j] * matrix[i][j]  # compute the dot product of row i and vector S
    b.append(bi)  # append the result to vector b

b2 = deepcopy(b)
print("B: ")
print(b)
print()
EX1 = "B: " + str(b)
# 2
Q = np.identity(n)
epsilon = sys.float_info.epsilon
k = 0
beta = 0
u = [0] * (n + 1)
gamma = 0

for r in range(n - 1):
    # constructia matricei Pr- constanta beta si vectorul u
    sigma = 0
    for i in range(r, n):
        sigma = sigma + matrix[i][r] * matrix[i][r]
    if sigma <= epsilon:
        break
    k = math.sqrt(sigma)
    if matrix[r][r] > 0:
        k = k * (-1)
    beta = sigma - k * matrix[r][r]
    u[r] = matrix[r][r] - k
    # matrix = Pr * matrix
    # transformarea coloanelor j = r+1, ..., n
    for i in range(r + 1, n):
        u[i] = matrix[i][r]
    for j in range(r + 1, n):
        suma = 0
        for i in range(r, n):
            suma += u[i] * matrix[i][j]
        gamma = suma / beta
        for i in range(r, n):
            matrix[i][j] = matrix[i][j] - gamma * u[i]
    # transformarea coloanei r a matricei matrix
    matrix[r][r] = k
    # b = Pr * b
    for i in range(r + 1, n):
        matrix[i][r] = 0
    suma = 0
    for i in range(r, n):
        suma = suma + u[i] * b[i]
    gamma = suma / beta
    for i in range(r, n):
        b[i] = b[i] - gamma * u[i]
    # Q = Pr * Q
    for j in range(0, n):
        suma = 0
        for i in range(r, n):
            suma += u[i] * Q[j][i]
        gamma = suma / beta
        for i in range(r, n):
            Q[j][i] = Q[j][i] - gamma * u[i]
print("Q folosind householder")
print(Q)
print("R folosind householder")
print(np.array(matrix))

# 3
q_numpy, r_numpy = np.linalg.qr(matrix2)

print()
print("Q folosind numpy:")
print(q_numpy)
print(("R folosind numpy"))
print(r_numpy)
print()

print("X_householder:")
print(np.linalg.solve(matrix, np.dot(Q.transpose(), b2)))
print("X_QR:")
print(np.linalg.solve(r_numpy, np.dot(q_numpy.transpose(), b2)))

print("X_QR - X_householder")
print(numpy.linalg.norm(
    np.linalg.solve(matrix, np.dot(Q.transpose(), b2)) - np.linalg.solve(r_numpy, np.dot(q_numpy.transpose(), b2))))
print()
# 4

print("A_init x_Householder - b_init:")
print(numpy.linalg.norm(np.dot(matrix2, np.linalg.solve(matrix, np.dot(Q.transpose(), b2))) - b2))
print("A_init x_QR - b_init:")
print(numpy.linalg.norm(np.dot(matrix2, np.linalg.solve(r_numpy, np.dot(q_numpy.transpose(), b2))) - b2))
print("(x_Householder - s) / s")
print(numpy.linalg.norm(np.linalg.solve(matrix, np.dot(Q.transpose(), b2)) - s) / numpy.linalg.norm(s))
print("(x_QR - s) /s")
print(numpy.linalg.norm(np.linalg.solve(r_numpy, np.dot(q_numpy.transpose(), b2)) - s) / numpy.linalg.norm(s))
print()

# 5
matrix = np.array(matrix)
R_inv = np.zeros_like(matrix)
m = matrix.shape[0]

# inverse of matrix (R)
for i in range(m - 1, -1, -1):
    R_inv[i, i] = 1 / matrix[i, i]
    for j in range(i + 1, m):
        R_inv[i, j] = -np.dot(R_inv[i + 1:j + 1, j], matrix[i, i + 1:j + 1]) / matrix[i, i]
# transpose of Q
Q_t = Q.T

# inverse of matrix using R_inv and Q_t
matrix_inv = np.dot(R_inv, Q_t)
print("Inversa lui A folosind householder:")
print(matrix_inv)

R_inv_numpy = np.zeros_like(r_numpy)
m_numpy = r_numpy.shape[0]
for i in range(m_numpy - 1, -1, -1):
    R_inv_numpy[i, i] = 1 / r_numpy[i, i]
    for j in range(i + 1, m_numpy):
        R_inv_numpy[i, j] = -np.dot(R_inv_numpy[i + 1:j + 1, j], r_numpy[i, i + 1:j + 1]) / r_numpy[i, i]

Q_numpy_t = q_numpy.T

matrix_numpy_inv = np.dot(R_inv_numpy, Q_numpy_t)
print("Inversa lui A folosind numpy:")
print(matrix_numpy_inv)
print("A_householder^-1 - A_bibl^1")
print(numpy.linalg.norm(matrix_inv - matrix_numpy_inv))


def approximate_limit(e=sys.float_info.epsilon):
    iteration = 10
    n = 5
    A = np.zeros((n, n))

    # rand matrix dominant diag elem
    for i in range(n):
        A[i, i] = np.sum(np.abs(A[i, :i])) + np.random.rand() * n
        for j in range(i + 1, n):
            A[i, j] = np.random.rand()
            A[j, i] = A[i, j]

    Aini = np.round(A.copy())

    for k in range(iteration):
        Q, R = np.linalg.qr(A)
        A_k_1 = np.dot(np.triu(R), Q)
        # check convergence
        if np.linalg.norm(A_k_1 - A, 'fro') < e:
            break
        A = A_k_1
    print("test1123:" +'\n')
    print(R)
    print()
    return Aini, np.round(A_k_1)


A_init, A_k_1 = approximate_limit()
print()
print("Bonus:")
print(str(A_init) + '\n' + str(A_k_1))


def function1():
    result_label.config(text=EX1)


def function2():
    result_label.config(text=str(Q))


def function3():
    result_label.config(text=str(matrix))


def function4():
    result_label.config(text=str(q_numpy))


def function5():
    result_label.config(text=str(r_numpy))


def function6():
    result_label.config(text=str(np.linalg.solve(matrix, np.dot(Q.transpose(), b2))))


def function7():
    result_label.config(text=str(np.linalg.solve(r_numpy, np.dot(q_numpy.transpose(), b2))))


def function8():
    result_label.config(text=str(numpy.linalg.norm(
        np.linalg.solve(matrix, np.dot(Q.transpose(), b2)) - np.linalg.solve(r_numpy,
                                                                             np.dot(q_numpy.transpose(), b2)))))


def function9():
    result_label.config(
        text=str(numpy.linalg.norm(np.dot(matrix2, np.linalg.solve(matrix, np.dot(Q.transpose(), b2))) - b2)))


def function10():
    result_label.config(
        text=str(numpy.linalg.norm(np.dot(matrix2, np.linalg.solve(r_numpy, np.dot(q_numpy.transpose(), b2))) - b2)))


def function11():
    result_label.config(
        text=str(numpy.linalg.norm(np.linalg.solve(matrix, np.dot(Q.transpose(), b2)) - s) / numpy.linalg.norm(s)))


def function12():
    result_label.config(text=str(
        numpy.linalg.norm(np.linalg.solve(r_numpy, np.dot(q_numpy.transpose(), b2)) - s) / numpy.linalg.norm(s)))


def function13():
    result_label.config(text=str(matrix_inv))


def function14():
    result_label.config(text=str(matrix_numpy_inv))


def function15():
    result_label.config(text=str(numpy.linalg.norm(matrix_inv - matrix_numpy_inv)))


def function16():
    result_label.config(text=str(A_init) + '\n' + '\n' + str(A_k_1))


root = tk.Tk()

style = ttk.Style()
style.configure("TButton", font=("TkDefaultFont", 12), padding=6)

button1 = tk.Button(root, text="Ex 1 ", command=function1)
button1.pack(padx=20, pady=10)

button2 = tk.Button(root, text="Q with Householder", command=function2)
button2.pack(padx=20, pady=10)

button3 = tk.Button(root, text="R with HouseHolder", command=function3)
button3.pack(padx=20, pady=10)

button4 = tk.Button(root, text="Q with numpy", command=function4)
button4.pack(padx=20, pady=10)

button5 = tk.Button(root, text="R with numpy", command=function5)
button5.pack(padx=20, pady=10)

button6 = tk.Button(root, text="X_householder", command=function6)
button6.pack(padx=20, pady=10)

button7 = tk.Button(root, text="X_QR", command=function7)
button7.pack(padx=20, pady=10)

button8 = tk.Button(root, text="norm(X_QR - X_householder)", command=function8)
button8.pack(padx=20, pady=10)

button9 = tk.Button(root, text="norm(A_init x_Householder - b_init)", command=function9)
button9.pack(padx=20, pady=10)

button10 = tk.Button(root, text="norm(A_init x_QR - b_init)", command=function10)
button10.pack(padx=20, pady=10)

button11 = tk.Button(root, text="norm((x_Householder - s)) / norm(s)", command=function11)
button11.pack(padx=20, pady=10)

button12 = tk.Button(root, text="norm(x_QR - s) / norm(s)", command=function12)
button12.pack(padx=20, pady=10)

button13 = tk.Button(root, text="Inversa lui A folosind householder", command=function13)
button13.pack(padx=20, pady=10)

button14 = tk.Button(root, text="Inversa lui A folosind numpy", command=function14)
button14.pack(padx=20, pady=10)

button15 = tk.Button(root, text="norm(A_householder^-1 - A_bibl^1)", command=function15)
button15.pack(padx=20, pady=10)

button16 = tk.Button(root, text="Bonus", command=function16)
button16.pack(padx=20, pady=10)

separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", padx=20, pady=10)

result_label = ttk.Label(root, font=("TkDefaultFont", 12))
result_label.pack(padx=20, pady=10)

root.mainloop()
