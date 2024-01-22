def cumsum(lst):
    new_lst=[]
    a = 0
    for i in range(len(lst)):
        a += lst[i]
        new_lst.append(a)
    return list(new_lst)
lst1=[1,3,5]
lst2=[0,1,2]
lst3=[3,3,3]
print(cumsum(lst1))
print(cumsum(lst2))
print(cumsum(lst3))
