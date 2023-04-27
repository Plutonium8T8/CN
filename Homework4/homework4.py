import tkinter as tk
from tkinter import ttk

file = open("a_3.txt", "r")

file_read = file.read()

bfile = open("b_3.txt", "r")

bfile_read = bfile.read()

a = {}

b = []

aii = []


def initializeB(b, bfile_read):
    auxiliar = 0

    for y in range(0, len(bfile_read)):
        if bfile_read[y] == '\n':
            b.append(float(bfile_read[int(auxiliar):y]))
            auxiliar = y + 1


def initializeA(a, file_read):
    auxiliar = 0
    number = 0
    i = 0
    j = 0
    count = 0

    for y in range(0, len(file_read)):
        if file_read[y] == ',':
            count = count + 1
            if count == 1:
                number = float(file_read[int(auxiliar):y])
                auxiliar = y + 1
            if count == 2:
                i = int(file_read[int(auxiliar):y])
                auxiliar = y + 1
        if file_read[y] == '\n':
            count = 0
            j = int(file_read[int(auxiliar):y])
            auxiliar = y + 1

            if i not in a.keys():
                a.update({i: [(j, number)]})
            else:
                a[i].append((j, number))


def diagonal_sum(a, aii):
    previous_key = -1

    for index_dict in a.keys():
        for index_array in a[index_dict]:
            if index_dict == index_array[0]:
                if index_dict != previous_key + 1:
                    return False
                aii.append(index_array[1])
                previous_key = previous_key + 1
    return True


def GaussSneidel(a, b, aii):
    xk = []

    for index in range(len(a.keys())):
        xk.append(0.0)

    for k in range(10000):
        convergence_factor = 0.0

        norma_partial = 0

        for index_i in a.keys():
            x_prec = xk[index_i]
            sigma = 0

            xk[index_i] = (float(b[index_i]) - sigma) / aii[index_i]

            for index_j in a[index_i]:
                if index_j[0] < index_i:
                    sigma += float(index_j[1]) * xk[index_j[0]]
                else:
                    sigma += float(index_j[1] * x_prec) 

            convergence_factor = convergence_factor + abs(xk[index_i] - ((b[index_i] - sigma) / aii[index_i]))

            norma_partial += (xk[index_i] - x_prec) ** 2
        
        norma_partial = norma_partial ** 1/2

            

        if norma_partial < 10e-8:
            print(norma_partial)

            file = open("result.txt", "w+")
            for i in range(len(xk)):
                file.write(str(xk[i]) + '\n')
            file.close()

            normalization = []

            for i in a.keys():
                normalization.append(0.0)

            for i in a.keys():
                for item in a[i]:
                    normalization[item[0]] = abs(item[1] * xk[item[0]] - b[item[0]])
        
            break

        # if convergence_factor < 10e-8:
        #     file = open("result.txt", "w+")
        #     for i in range(len(xk)):
        #         file.write(str(xk[i]) + '\n')
        #     file.close()
        #     break

    return "Done"


def matrixSum(file1, file2):
    file1 = open("a.txt", 'r').read()
    file2 = open("b.txt", 'r').read()

    a = {}

    b = {}

    b1 = {}

    initializeA(a, file1)

    initializeA(b, file2)

    for index_i in a.keys():
        if index_i in b.keys():
            a[index_i] += b[index_i]
            for item in b[index_i]:
                b[index_i].remove(item)

            auxiliar_list = []

            for item in a[index_i]:
                if item not in auxiliar_list:
                    auxiliar_list.append(item[0])

            for j in auxiliar_list:
                sum = 0

                for item in a[index_i]:
                    if item[0] == j:
                        sum += item[1]
                        a[index_i].remove(item) 
                if sum != 0:
                    a[index_i].append((j, sum))

    for index_i in b.keys():
        if index_i not in a.keys():
            a.update((index_i, b[index_i]))
            for item in b[index_i]:
                b[index_i].remove(item)

    file = open("bonus_result.txt", "w+")
    for i in a.keys():
        for j in a[i]:
            file.write(str(i) + ', ' + str(j[0]) + ', ' + str(j[1]) + '\n')
    file.close()
    return "Done"
#if diagonal_sum(a, aii):
#    matrixSum("a.txt", "b.txt")

initializeA(a, file_read)

initializeB(b, bfile_read)

# if diagonal_sum(a, aii):
#     print(GaussSneidel(a, b, aii))

def function1():
    if diagonal_sum(a, aii):
        result_label.config(text=str(GaussSneidel(a, b, aii)))
        return 

def function2():
    if diagonal_sum(a, aii):
        result_label.config(text = str(matrixSum("a.txt", "b.txt")))


root = tk.Tk()

style = ttk.Style()
style.configure("TButton", font=("TkDefaultFont", 12), padding=6)

button1 = tk.Button(root, text="GaussSneidel", command=function1)
button1.pack(padx=20, pady=10)

button2 = tk.Button(root, text="Bonus", command=function2)
button2.pack(padx=20, pady=10)

separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", padx=20, pady=10)

result_label = ttk.Label(root, font=("TkDefaultFont", 12))
result_label.pack(padx=20, pady=10)

root.mainloop()
