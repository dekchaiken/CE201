M = [[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
def is_upper_triangular(M):
    for i in range(1, len(M)):
        for j in range(0, i):
            if(M[i][j] != 0):
                    return False
    return True
 
is_upper_triangular(M)
