# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# The join method is for joining a list of strings together, so they will need to be converted to strings first
num=[]
for x in range(2000, 3201):
    if (x%7==0) and (x%5==0):
        num.append(str(x))
print(','.join(num))
