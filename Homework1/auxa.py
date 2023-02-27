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