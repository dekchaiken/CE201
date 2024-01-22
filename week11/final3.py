def real_multiply(x, y):
    if y == 0:
        return x
    else:
        return x * real_multiply(x,(2**y)-1)
    
real_multiply(2,0)