# program that accepts a sentence and calculate the number of letters and digits.
# input=My name is Alex! 18.12.2000
# output= letters: 12, digits: 8
word = input()
letter = 0
digit = 0

for i in word:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        letter+=1
    if '0'<=i and i<='9':
        digit+=1

print("letters {0}\ndigits {1}".format(letter,digit))