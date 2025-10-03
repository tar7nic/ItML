def echelon_form(matrix):
    if not matrix:
        return

    lead = 0
    rowCount = len(matrix)
    columnCount = len(matrix[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return

        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return

        matrix[i], matrix[r] = matrix[r], matrix[i]

        if matrix[r][lead] != 0:
            matrix[r] = [x / matrix[r][lead] for x in matrix[r]]
        for i in range(rowCount):
            if i != r:
                matrix[i] = [matrix[i][j] - matrix[r][j] * matrix[i][lead] for j in range(columnCount)]
        lead += 1

matrix = [[2, 1,-1],
          [3, 4, 2],
          [2, 1, 2]]

echelon_form(matrix)
for r in matrix:
    print(r)
