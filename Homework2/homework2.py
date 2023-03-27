import sys
import numpy as np
from numpy import linalg
import math
import copy
import tkinter as tk
from tkinter import ttk

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

def CholeskyDecomp(A):
    n = A.shape[0]
    L = np.zeros((n,n))
    D = np.zeros((n,n))
    for i in range(n):
        for j in range(i):
            if i > j:
                L[i,j] -= (A[i,j] - sum(L[i,k]*L[j,k]*D[k,k] for k in range(j))) / D[j,j]  
        L[i,i] = 1
        D[i,i] = A[i,i] - sum(L[i,k] * L[i,k] *D[k,k] for k in range(i))
    return L, D

def Bonus(A, L, D, Lt):
    matrix = np.matmul(L, np.matmul(D, Lt))
    delta = 0.0
    for index1 in range(len(matrix)):
        for index2 in range(len(matrix[0])):
            delta += np.abs( np.abs(matrix[index1][index2]) -  np.abs(A[index1][index2]))

    return "{:.16f}".format(delta)

def Ecuation(L, D, Lt, B):
    Z = []
    Y = []
    X = []

    auxiliar = 0

    for index1 in range(0, len(B) - 1):
        sum = 0
        for index2 in range(0, index1):
            sum = L[index1][index2] * Z[index2]

        Z.append(B[index1] - sum)

        auxiliar = index1

    for index in range(auxiliar + 1, len(B)):
        Z.append(0)

    auxiliar = 0

    for index in range(0, len(D) - 1):
            Y.append(Z[index] / D[index])
            auxiliar = index

    for index in range(auxiliar + 1, len(B)):
        Y.append(0)

    for index1 in range(len(Y) - 1, -1, -1):
        sum = 0
        for index2 in range(len(Y) - 1, index1, -1):
            sum = Lt[index1][index2] * X[len(Y) - index2 - 1]

        X.append(Y[index1] - sum)

    X = X[::-1]

    return Z, Y, X


file = open("matrix1.txt", "r")
matrix_str = file.read()
matrix = StrToMatrix(matrix_str)

detA = 1

L, auxD = CholeskyDecomp(np.array(matrix))
D = []
for index in range(len(auxD)):
    D.append(auxD[index][index])
    detA *= auxD[index][index]
Lt = np.transpose(L)
T = np.matmul(L, auxD)
U = Lt

print("DetA = ", detA)

file = open("B.txt", "r")
matrix_str = file.read()
auxB = StrToMatrix(matrix_str)

B = []

for index in range(len(auxB)):
    B.append(auxB[index][0])

DStr = ''
for i in range(len(D)):
    DStr += str(D[i]) + '\n'

EcuationStr = ''
for i in range(len(Ecuation(L, D, Lt, B))):
    if i == 0:
        EcuationStr += 'Z = ' + str(Ecuation(L, D, Lt, B)[i]) + '\n'
    elif i == 1:
        EcuationStr += 'Y = ' + str(Ecuation(L, D, Lt, B)[i]) + '\n'
    else:
        EcuationStr += 'X = ' + str(Ecuation(L, D, Lt, B)[i]) + '\n'

def MatrixToStr(x):
    strx = ''
    for row in x:
        for element in row:
            strx = strx + str(element) + '   '
        strx = strx + '\n'

    return  strx

def function1():
    result_label.config(text="L: \n" + MatrixToStr(L))

def function2():
    result_label.config(text="D: \n" + str(DStr))

def function3():
    result_label.config( text="Lt: \n" + MatrixToStr(Lt))

def function4():
    result_label.config( text="T: \n" + MatrixToStr(T))

def function5():
    result_label.config( text="U: \n" + MatrixToStr(U))

def function6():
    result_label.config( text="Epsilon = " +  str(Bonus(matrix, L, auxD, Lt)))

def function7():
    result_label.config( text=EcuationStr)

def function8():
    result_label.config( text=EcuationStr)

root = tk.Tk()

style = ttk.Style()
style.configure("TButton", font=("TkDefaultFont", 12), padding=6)

button1 = tk.Button(root, text="L ", command=function1)
button1.pack(padx=20, pady=10)

button2 = tk.Button(root, text="D", command=function2)
button2.pack(padx=20, pady=10)

button3 = tk.Button(root, text="Lt", command=function3)
button3.pack(padx=20, pady=10)

button4 = tk.Button(root, text="T", command=function4)
button4.pack(padx=20, pady=10)

button5 = tk.Button(root, text="U", command=function5)
button5.pack(padx=20, pady=10)

button6 = tk.Button(root, text="Bonus", command=function6)
button6.pack(padx=20, pady=10)

button7 = tk.Button(root, text="Ecuation(L, D, Lt, B)", command=function7)
button7.pack(padx=20, pady=10)


separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", padx=20, pady=10)

result_label = ttk.Label(root, font=("TkDefaultFont", 12))
result_label.pack(padx=20, pady=10)

root.mainloop()
