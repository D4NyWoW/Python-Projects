# generate a list of numbers

# input_string = input('Enter elements of a list separated by space ')
# print("\n")
# user_list = input_string.split()
# # print list
# print('list: ', user_list)


# sum all the items in a list.
def ex1(item):
    sum = 0
    for n in item:
        sum = sum + n
    return sum
#print(ex1([1,2,3,4]))

# multiply all the items in a list.
def ex2(item):
    new_list = 1
    for x in item:
        new_list *= x
    return new_list
#print(ex2([3,1,2,3]))

#get the largest number from a list
def ex3(item):
    max = item[0]
    for i in item:
        if i > max:
            max = i
    return max
#print(ex3([-4,-15,-6,-6]))

# get the smallest number from a list.
def ex3(item):
    min = item[0]
    for i in item:
        if i < min:
            min = i
    return min
#print(ex3([-4,-15,-6,-6]))

# remove duplicates from a list.
def ex7(list):
    dup_items = set()
    uniq_items = []
    for x in list:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
    return dup_items
#print(ex7([10,20,30,20,10,50,60,40,80,50,40]))
