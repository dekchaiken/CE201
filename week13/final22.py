def power_of_two(n):
    x = 0 
    bl = False
    while not bl:
        a = 2**x 
        if a > n:
            b = ('n = %d → 2^%d = %d'%(n,x-1,2**(x-1))) 
            return b
        x += 1
print(power_of_two(int(input())))