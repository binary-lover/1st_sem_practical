# 2. Generate the matrix into echelon form and find its rank
import numpy
elem = [[2,3,4],
        [1,2,3],
        [7,8,9]]
matrix = numpy.mat(elem)

print("Rand of the matrix is:",numpy.linalg.matrix_rank(matrix))