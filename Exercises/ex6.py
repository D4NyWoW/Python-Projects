# program that accepts a sequence of whitespace separated words as input and prints 
# the words after removing all duplicate words and sorting them alphanumerically.
# input= "big black bug bit a big black dog on his big black nose"
# output = "a big bit black bug dog his nose on"

word = input().split()

for x in word:
    if word.count(x) > 1:    #count function returns total repeatation of an element that is send as argument
        word.remove(x)     # removes exactly one element per call

word.sort()
print(" ".join(word))