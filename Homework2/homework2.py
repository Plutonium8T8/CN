import sys
import numpy as np
from numpy import linalg
import math
import copy

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
                L[i,j] = (A[i,j] - sum(L[i,k]*L[j,k]*D[k,k] for k in range(j))) / D[j,j]  
        L[i,i] = 1
        D[i,i] = A[i,i] - sum(L[i,k] * L[i,k] *D[k,k] for k in range(i))
    return L, D

def Bonus(A, L, D, Lt):
    matrix = np.matmul(L, np.matmul(D, Lt))
    delta = 0.0
    for index1 in range(len(matrix)):
        for index2 in range(len(matrix[0])):
            print(np.abs(matrix[index1][index2]))
            print(np.abs(A[index1][index2]))
            delta += np.abs( np.abs(matrix[index1][index2]) -  np.abs(A[index1][index2]))

    return "{:.16f}".format(delta)

def Ecuation(A, D, B):
    pass

file = open("matrix1.txt", "r")
matrix_str = file.read()
matrix1 = StrToMatrix(matrix_str)

L, auxD = CholeskyDecomp(np.array(matrix1))
D = []
for index in range(len(auxD)):
    D.append(auxD[index][index])
Lt = np.transpose(L)
T = np.matmul(L, auxD)
U = Lt

print(L)
print(D)
print(Lt)
print(T)
print(U)
print(Bonus(matrix1, L, auxD, Lt))