# mupliply list

def list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = list(100)
#print(my_list)

# find the Max of three numbers. 3 , 5, 7 -> 7
def max(a, b, c):
    if a > b > c or a > c > b:
        print("max is: ",a)
    elif b > a > c or b > c > a:
        print("max is: ",b)
    elif c > a > b or c > b > a:
        print("max is: ",c)
#max(15,25,3)

# sum all the numbers in a list.
def ex2(item):
    sum = 0
    for n in item:
        sum = sum + n
    return sum
#print(ex2((8,2,3,0,7)))

# reverse a string.
#txt = input("")
def ex4(x):
    return x[::-1]
#print(ex4(txt))

# function that accepts a string and calculate the number of upper case letters and lower case letters.
txt = input("")
def ex7(x):
    lower = 0
    upper = 0
    for i in x:
        if i.islower():
            lower = lower + 1
        elif i.isupper():
            upper = upper + 1
    print("lower: ",lower,"upper: ",upper)
ex7(txt)
