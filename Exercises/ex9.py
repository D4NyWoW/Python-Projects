# program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers
# the tuples are input by console, sort criteria: name, age and by score
# name -> age -> score
# Tom,19,80
# Alex,22,80
# Daniel,14,85
# Cartel,17,93
# Matei,21,95
list = []
while True:
    s = input().split(',')
    if not s[0]:                          
        break
    list.append(tuple(s))

list.sort(key= lambda x:(x[0],int(x[1]),int(x[2])))  # the data is sorted by element priority 0>1>2 in accending order
print(list)