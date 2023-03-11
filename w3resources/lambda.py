# a lambda function that adds 15 to a given number passed in as an argument
""" r = lambda a : a + 15
print(r(10)) """
# create a lambda function that multiplies argument x with argument y and prints the result.
""" r = lambda a, b : a * b
print(r(3,5)) """

# a function that takes one argument, and that argument will be multiplied with an unknown given number.
""" def func(n):
    return lambda a : a * n
result = func(2)
print("Double number of the 15 : ",result(15))
result = func(3)
print("Triple number of the 15 : ",result(15))
result = func(4)
print("Quatruple the number of the 15 : ",result(15))
result = func(5)
print("Quintuple the number of the 15 : ",result(15))
 """

# program to sort a list of tuples using Lambda.
""" tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original tuples : ",tuples)
tuples.sort(key = lambda x: x[1]) # 88,80,97,82 -> x[1] English,Science,etc -> x[0]
print("\nSorting the list of tuples : ",tuples) """

# program to filter a list of integers using Lambda.
""" nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers : ",nums)
print("\nEven number from the list : ")
even_numbers = list(filter(lambda x: x%2 == 0, nums))
print(even_numbers)
print("\nOdds numbers from the list : ")
odds_numbers = list(filter(lambda x: x%2 != 0, nums))
print(odds_numbers) """
