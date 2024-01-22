import math

def is_square(m):
    for i in range(len(m)):
        if len(m[i]) != len(m):
            return False
    return True

def magic(m):
    if(not(is_square(m))): 
        return False
    
    total = 0
    x = len(m)
    for i in range(x):
        total += m[i][i]

    if not(math.isclose(total, x*(x*x+1)/2)):
        return False

    total = 0
    for i in range(x):
        total += m[i][x-1-i]

    if not(math.isclose(total, x*(x*x+1)/2)):
        return False

    for i in range(x):
        total = 0
        for j in range(x):
            total += m[i][j]
        if not(math.isclose(total, x*(x*x+1)/2)):
            return False

    for i in range(x):
        total = 0
        for j in range(x):
            total += m[j][i]
        if not(math.isclose(total, x*(x*x+1)/2)):
            return False

    return True

m0 = [[2,7,6],[9,5,1],[4,3,8]]
print(magic(m0))
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))
m2 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(magic(m2))
m3 = [[1,1],[1,1]]
print(magic(m3))
m4 =  [[1,1],[1,1],[1,2]]
print(magic(m4))