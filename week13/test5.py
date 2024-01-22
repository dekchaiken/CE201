def has_duplicate(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i]==list[j]:
                return True
    return False
has_duplicate([1, 2, 3, 4, 5, 1])


a = (2.5*2)*(2.5*2)
b = 22/7*((5/2)(5/2))
print(a-b)