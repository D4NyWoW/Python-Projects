#  script to sort (ascending and descending) a dictionary by value.
def ex1(d):
    l=list(d.items())
    l.sort()
    print("Ascending order", l)
    l = list(d.items())
    l.sort(reverse=True)
    print("Descending order", l)   
#ex1({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})

# script to add a key to a dictionary
def ex2():
    d = {0:10, 1:20}
    print(d)
    d.update({2:30})
    print(d)

# script to concatenate the following dictionaries to create a new one.
""" dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic4= {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4) """

# ex4 script to check whether a given key already exists in a dictionary.
""" d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key(x):
    if x in d:
        print("key is present in dictionary")
    else: 
        print("key is not present in dictionary")
key(5)
key(7)
 """

#  iterate over dictionaries using for loops.
""" d = {'x': 10, 'y': 20, 'z': 30}
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value) """

#  script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
""" d=dict()
for x in range(1,16):
    d[x]=x**2
print(d) """

# script to merge two Python dictionaries.
""" d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 400}
d3 = {}
for d in (d1,d2):
    d3.update(d)
print(d3) # sau
d = d1.copy()
d.update(d2) """

