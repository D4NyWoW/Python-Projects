# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
input_string = input('Enter elements of a list separated by space ')
print("\n")
list = input_string.split()
# print list
print('list: ', list)

tuple = tuple(list)

print('tuple: ', tuple)

