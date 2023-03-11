# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# input=0100,0011,1010,1001
# output=1010

data = input().split(',')
data = [num for num in data if int(num, 2) % 5 == 0]
print(','.join(data))