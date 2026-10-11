def matrixmul(
    a: list[list[int | float]],
    b: list[list[int | float]]
) -> list[list[int | float]] | int:

    if len(a[0]) != len(b):
        return -1

    c = []
    dim = len(a[0])

    # Create the result matrix filled with zeros
    for i in range(len(a)):
        c.append([])
        for j in range(len(b[0])):
            c[i].append(0)

    def row(a, i):
        l = []
        for k in range(dim):
            l.append(a[i][k])
        return l

    def col(b, j):
        column = []
        for k in range(dim):
            column.append(b[k][j])
        return column

    # Multiply each row of a by each column of b
    for i in range(len(a)):
        r = row(a, i)

        for j in range(len(b[0])):
            column = col(b, j)

            for k in range(dim):
                c[i][j] += r[k] * column[k]

    return c
        



    
        
