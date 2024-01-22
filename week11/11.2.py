def is_identity(matrix):
    ans = 0
    for i in range(len(matrix)):
        if matrix[i][i] == 1:
            ans += 1
    
    if ans == len(matrix):
        return True
    else:
        return False

is_identity([[1,1,1],[-2,1,3]])