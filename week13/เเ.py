def reverse_sequence(string):
    if len(string) == 0:
        return string
    else:
        return reverse_sequence (string[1:]) + string[0]
a = str(input("Enter a string: "))
print(reverse_sequence(a))