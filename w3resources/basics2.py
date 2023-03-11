#Count Number of Characters in Text File
def var1():
 #open file in read mode
 file = open("C:\DOCUMENTE\data.txt")

 #read the content of file
 data = file.read()

 #get the length of the data
 number_of_characters = len(data)

 print("Number of characters in the text file : ", number_of_characters)
 
# program to count the number of each character in a text file.
def var2():
    import collections
    import pprint
    file_input = input('File Name: ')
    with open(file_input, 'r') as info:
      count = collections.Counter(info.read().upper())
      value = pprint.pformat(count)
      print(value)

#to add two positive integers without using the '+' operator.

def ex14():
    def add_without_plus_operator(a, b):
        while b != 0:
            data = a & b
            a = a ^ b
            b = data << 1
        return a
    print(add_without_plus_operator(2, 10))
    print(add_without_plus_operator(-20, 10))
    print(add_without_plus_operator(-10, -20))







