def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	l=[]
	if mode=='column':
        for i in range(len(matrix[0])):
            m=0
            for j in range(len(matrix)):
                m=((matrix[j][i])/len(matrix))+m
            l.append(m)
        return l
    else:
        for i in range(len(matrix)):
            m=0
            for j in range(len(matrix[0])):
                m=((matrix[i][j])/len(matrix[0]))+m
            l.append(m)
        return l