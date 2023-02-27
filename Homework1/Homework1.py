import sys
import numpy as np

# 1:

def Ex1():
    u = 1

    while (1 + u != 1):
        u = u / 10

    return u

print("1: The machine precision is: ", Ex1())  


# 2:

def Ex2_1():
    x = 1.0
    y = Ex1()
    z = Ex1()

    return (x + y) + z == x + (y + z)

print("2.1: The result to the operation \"(x +c y) +c z == x +c (y +c z)\" is: ", Ex2_1())

def Ex2_2():
    x = sys.float_info.max
    y = 1 + Ex1()
    z = Ex1()

    return (x * y) * z == x * (y * z)

print("2.2: The result to the operation \"(x *c y) *c z == x *c (y *c z)\" is: ", Ex2_2())


# 3:

def StrToMatrix(matrix_str):
    matrix = []
    row_array = []
    auxiliar = 0
    for index in range(len(matrix_str)):
        if matrix_str[index] == ' ':
            row_array.append(int(matrix_str[auxiliar:index]))
            auxiliar = index + 1
            row_array

        if matrix_str[index] == '\n':
            row_array.append(int(matrix_str[auxiliar:index]))
            matrix.append(row_array)
            row_array = []
            auxiliar = index + 1

    return matrix

def MatrixAddition(matrix1, matrix2):
    returnMatrix = []
    for index1 in range(len(matrix1)):
        returnRow = []
        for index2 in range(len(matrix1[0])):
            returnRow.append(matrix1[index1][index2] + matrix2[index1][index2])
        returnMatrix.append(returnRow)

    return returnMatrix

def MatrixSubtraction(matrix1, matrix2):
    returnMatrix = []
    for index1 in range(len(matrix1)):
        returnRow = []
        for index2 in range(len(matrix1[0])):
            returnRow.append(matrix1[index1][index2] - matrix2[index1][index2])
        returnMatrix.append(returnRow)

    return returnMatrix

def Strassen(matrix1, matrix2):

    print("Matrix1: ", matrix1)
    print("Matrix2: ", matrix2)
    print(len(matrix1))
    print()

    if len(matrix1) == 2:
        p1 = (matrix1[0][0] + matrix1[1][1]) * (matrix2[0][0] + matrix2[1][1])
        p2 = (matrix1[1][0] + matrix1[1][1]) * matrix2[0][0]
        p3 = matrix1[0][0] * (matrix2[0][1] - matrix2[1][1])
        p4 = matrix1[1][1] * (matrix2[1][0] - matrix2[0][0])
        p5 = (matrix1[0][0] + matrix1[0][1]) * matrix2[1][1]
        p6 = (matrix1[1][0] - matrix1[0][0]) * (matrix2[0][0] + matrix2[0][1])
        p7 = (matrix1[0][1] - matrix1[1][1]) * (matrix2[1][0] + matrix2[1][1])

        c11 = p1 + p4 - p5 + p7
        c12 = p3 + p5
        c21 = p2 + p4
        c22 = p1 + p3 - p2 + p6 

        return [[c11, c12], [c21, c22]]

    if len(matrix1) in {4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048}:
        matrix111 = []
        matrix112 = []
        matrix121 = []
        matrix122 = []

        matrix211 = []
        matrix212 = []
        matrix221 = []
        matrix222 = []

        for index in range(0, int(len(matrix1) / 2)):
            matrix111.append(matrix1[index][0:int(len(matrix1) / 2)])

        for index in range(0, int(len(matrix1) / 2)):
            matrix112.append(matrix1[index][int(len(matrix1) / 2):int(len(matrix1))])

        for index in range(int(len(matrix1) / 2), int(len(matrix1))):
            matrix121.append(matrix1[index][0:int(len(matrix1) / 2)])

        for index in range(int(len(matrix1) / 2), int(len(matrix1))):
            matrix122.append(matrix1[index][int(len(matrix1) / 2):int(len(matrix1))])

        
        for index in range(0, int(len(matrix2) / 2)):
            matrix211.append(matrix2[index][0:int(len(matrix2) / 2)])

        for index in range(0, int(len(matrix2) / 2)):
            matrix212.append(matrix2[index][int(len(matrix2) / 2):int(len(matrix2))])

        for index in range(int(len(matrix2) / 2), int(len(matrix2))):
            matrix221.append(matrix2[index][0:int(len(matrix2) / 2)])

        for index in range(int(len(matrix2) / 2), int(len(matrix2))):
            matrix222.append(matrix2[index][int(len(matrix2) / 2):int(len(matrix2))])

        returnMatrix1 = Strassen(matrix111, matrix211)
        returnMatrix2 = Strassen(matrix112, matrix212)
        returnMatrix3 = Strassen(matrix121, matrix221)
        returnMatrix4 = Strassen(matrix122, matrix222)

        returnMatrix = []

        for index1 in range(len(returnMatrix1)):
            matrixRow = []
            for index2 in range(len(returnMatrix1[index1])):
                matrixRow.append(returnMatrix1[index1][index2])
            for index2 in range(len(returnMatrix2[index1])):
                matrixRow.append(returnMatrix2[index1][index2])
            returnMatrix.append(matrixRow)

        for index1 in range(len(returnMatrix3)):
            matrixRow = []
            for index2 in range(len(returnMatrix3[index1])):
                matrixRow.append(returnMatrix3[index1][index2])
            for index2 in range(len(returnMatrix4[index1])):
                matrixRow.append(returnMatrix4[index1][index2])
            returnMatrix.append(matrixRow)
        
        return(returnMatrix)

def Ex3():
    file = open("matrix1.txt", "r")
    matrix_str = file.read()
    matrix1 = StrToMatrix(matrix_str)

    file = open("matrix2.txt", "r")
    matrix_str = file.read()
    matrix2 = StrToMatrix(matrix_str)

    print(Strassen(matrix1, matrix2))

Ex3()