from ctsLS import *

A = [[0,1,0,0],[-48.6, -1.25, 48.6, 0],[0,0,0,1],[19.5,0,-16.7,0]]
B = [[0], [0], [0], [-3.33]]
C = [0,0,1,0]
D = 0

roboarm = LS(A, B, C, D)

rank = numpy.linalg.matrix_rank(A)
