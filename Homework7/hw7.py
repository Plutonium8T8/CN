import numpy as np

def sign(number):
    if number >= 0: 
        return 1 
    else: 
        return -1
    
def Pcomplex(poly, x):
    res = 0
    for i in range(len(poly)):
        res += poly[i] * x**i
    return res
    
def P(poly, x):
    result = 0

    for index in range(len(poly)):
        result += poly[len(poly) - index - 1] * (x ** index)
    
    return result

def Pprim(poly, x):
    poly_prim = []

    for index in range(1, len(poly)):
        poly_prim.append(poly[len(poly) - index - 1] * index)

    poly_prim = poly_prim[::-1]

    return P(poly_prim, x)

def Pprimprim(poly, x):
    poly_prim = []

    for index in range(1, len(poly)):
        poly_prim.append(poly[len(poly) - index - 1] * index)

    poly_prim = poly_prim[::-1]

    poly_prim_prim = []

    for index in range(1, len(poly_prim)):
        poly_prim_prim.append(poly_prim[len(poly_prim) - index - 1] * index)
    
    poly_prim_prim = poly_prim_prim[::-1]

    return P(poly_prim_prim, x)

def maxA(poly):
    absPoly = []

    for index in range(len(poly)):
        absPoly.append(abs(poly[index]))

    return absPoly

def H(poly, x, n):
    return ((n - 1) ** 2) * (Pprim(poly, x) ** 2) - (n * (n - 1) * P(poly, x) * Pprimprim(poly, x))

def Pdivide(dividend, divisor):
    if divisor[-1] == 0:
        raise ZeroDivisionError("Polynomial division by zero")

    quotient = [0] * (len(dividend) - len(divisor) + 1)
    remainder = list(dividend)

    for i in range(len(quotient)-1, -1, -1):
        quotient[i] = remainder[i+len(divisor)-1] / divisor[-1]
        for j in range(i+len(divisor)-1, i-1, -1):
            remainder[j] -= quotient[i] * divisor[j-i]

    while len(quotient) > 1 and quotient[-1] == 0:
        quotient.pop()
    while len(remainder) > 1 and remainder[-1] == 0:
        remainder.pop()

    return quotient, remainder


def laguerre(poly, maxK = 10000):
    epsilon = 1e-12

    k = 0

    R = (abs(poly[0]) + max(maxA(poly[1:]))) / abs(poly[0])

    _R = -R

    print("-R: ", _R, "| R: ", R)

    x = np.random.uniform(-R, R)

    n = len(poly) - 1

    # print("n: ", n)

    varP = P(poly, x)

    # print("P: ", varP)

    varPprim = Pprim(poly, x)

    # print("P\': ", varPprim)

    # varPprimprim = Pprimprim(poly, x)

    # print("P\'\': ", varPprimprim)

    varH = H(poly, x, n)

    # print("H: ", varH)
    
    deltaX = ( n * varP ) /  ( varPprim + sign(varPprim) * (varH ** 1/2) )

    while abs(deltaX) >= epsilon and k <= maxK and abs(deltaX) <= 10**8:
        if varH <0 : break

        if abs(varPprim + sign(varPprim) * (varH ** 1/2)) <= epsilon : break

        x = x - deltaX

        k = k + 1

        varP = P(poly, x)

        varPprim = Pprim(poly, x)

        varPprimprim = Pprimprim(poly, x)

        varH = H(poly, x, n)

        deltaX = ( n * varP ) /  ( varPprim + sign(varPprim) * (varH ** 1/2) )

    return x

def horner(poly, x):
    result = poly[0]
    for i in range(1, len(poly)):
        result = result * x + poly[i]
    return result

def equation(poly):
    file = open("d:/CN/Homework7/" + str(poly) + ".txt", "w")
    print("Polynome: ", poly)
    for index in range(len(poly) - 1):
        root = laguerre(poly)
        # root = np.round(root)
        divisor = [1, -root]
        poly, reminder = Pdivide(poly, divisor)

        if reminder != 0.0:
            print("Root ", index + 1, " : ", root)
            file.write("Root " + str(index + 1) + " : " + str(root) + "\n")
    print()
    file.close()

equation(np.array([1, -6, 11, -6]))

equation(np.array([1, -55/42, -1, 49/42, -6/42]))

equation(np.array([1, -38/8, 49/8, -22/8, 3/8]))

equation(np.array([1, -6, 13, -12, 4]))