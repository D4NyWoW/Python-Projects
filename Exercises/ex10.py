# program to compute the frequency of the words from the input 
# the output should output after sorting the key alphanumerically
# input="big black bug bit a big black dog on his big black nose"

sequence = input().split()
dict = {}
for i in sequence:
    i = dict.setdefault(i,sequence.count(i))    # setdefault() function takes key & value to set it as dictionary.

dict = sorted(dict.items())               # items() function returns both key & value of dictionary as a list
                                          
for i in dict:
    print("%s:%d"%(i[0],i[1]))
