'''str1 = [1,2,3,4,5,0]
def reverse_sequence(x):
    if x == "":
        return x
    else:
        return x[::-1]
print(reverse_sequence(str1))'''
def reverse_sequence(string):
    if len(string) == 0:
        return string
    else:
        return reverse_sequence (string[1:]) + string[0]
a = str(input())
print(reverse_sequence(a))
