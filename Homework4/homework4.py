file = open("a_1.txt", "r")

file_read = file.read()

index = 0

while file_read[index] != '\n':
    index = index + 1

n = int(file_read[0:index])

def diagonal_sum(file_read):
    diagonal = []
    auxiliar = 0
    number = 0
    prev = -1
    i = 0
    j = 0
    count = 0

    nonZeroDiagonal = True

    for y in range(index, len(file_read)):
        if file_read[y] == ',':
            count = count + 1
            if count == 1:
                number = file_read[int(auxiliar):y]
                auxiliar = y + 1
            if count == 2:
                i = file_read[int(auxiliar):y]
                auxiliar = y + 1
        if file_read[y] == '\n':
            count = 0
            j = file_read[int(auxiliar):y]
            auxiliar = y + 1

            if (i == j):
                print(i)
                if (int(i) == prev + 1):
                    prev = prev + 1
                else:
                    break
    if prev == n - 1: return True
    else: return False

def GaussSneidel(file_read):  
    xk = []
    for k in range(10000):
        if k == 0:
            xk.append(0)
        for ix in range(n):
            sigma = 0
            for y in range(index, len(file_read)):
                if file_read[y] == ',':
                    count = count + 1
                    if count == 1:
                        number = file_read[int(auxiliar):y]
                        auxiliar = y + 1
                    if count == 2:
                        i = file_read[int(auxiliar):y]
                        auxiliar = y + 1
                if file_read[y] == '\n':
                    count = 0
                    j = file_read[int(auxiliar):y]
                    auxiliar = y + 1

                    if j < ix - 1:
                        sigma = sigma + number * xk[k - 1]
        # xk.append()

def matrixSum():
    file1 = open("a.txt", 'r')
    file2 = open("b.txt", 'r')

    file3 = open("auxiliar.txt", 'w')

    file_read1 = file1.read()
    file_read2 = file2.read()

    auxiliar = 0
    number = 0
    i = 0
    j = 0
    count = 0

    for y in range(index, len(file_read1)):
        if file_read1[y] == ',':
            count = count + 1
            if count == 1:
                number = file_read1[int(auxiliar):y]
                auxiliar = y + 1
            if count == 2:
                i = file_read1[int(auxiliar):y]
                auxiliar = y + 1
        if file_read1[y] == '\n':
            count = 0
            j = file_read1[int(auxiliar):y]
            auxiliar = y + 1

            auxiliar1 = 0
            number1 = 0
            prev1 = -1
            i1 = 0
            j1 = 0
            count1 = 0

            for y1 in range(index, len(file_read2)):
                if file_read2[y1] == ',':
                    count1 = count1 + 1
                    if count1 == 1:
                        number1 = file_read2[int(auxiliar1):y1]
                        auxiliar1 = y + 1
                    if count == 2:
                        i1 = file_read2[int(auxiliar1):y1]
                        auxiliar1 = y1 + 1
                if file_read2[y] == '\n':
                    count1 = 0
                    j1 = file_read2[int(auxiliar1):y1]
                    auxiliar1 = y1 + 1

                    print(i, i1)

                    if i == i1:
                        if j == j1:
                            sum = float(number) + float(number1)
                            print(str(sum) + ', ' + i + ', ' + j + '\n')
  
#matrixSum()

# if diagonal_sum(file_read):
#     GaussSneidel()
