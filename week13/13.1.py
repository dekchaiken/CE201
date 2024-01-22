def neg_expo(a, n):
    if a == 0: 
        return 0
    if n < 0:
        return (1/a) * neg_expo(a, n+1)
    if n == 0:
        return 1
    else:
        return a * neg_expo(a, n-1)
print(neg_expo(float(input()), int(input())))

