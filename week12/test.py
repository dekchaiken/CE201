def has_duplicate(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i]==list[j]:
                return True
    return False
has_duplicate([1, 2, 3, 4, 5, 1])
