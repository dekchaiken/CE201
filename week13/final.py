def exponentiation (a,n):
    if(n==1):
        return(a)
    if(n!=1):
        return(a*exponentiation (a,n-1))
a=float(input(""))
n=int(input(""))
print(exponentiation (a,n))

