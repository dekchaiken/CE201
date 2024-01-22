'''def stringRev (word):
    worLen = len(word)
    if worLen == 1:
        return word
    return [word[-1]] + stringRev(word[:-1])
listWord = ["hey", "there", "jim"]
print(stringRev(listWord))'''

def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
              
s = [1,2,3,4,5,0]
print (reverse(s)) 