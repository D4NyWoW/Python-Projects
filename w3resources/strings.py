# calculate the length of a string.
def string_length(str1):
      count = 0
      for char in str1:
        count += 1
      return count
#print(string_length('calabria'))

# count the number of characters (character frequency) in a string.
def ex2(string):
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else: 
            dict[n] = 1
    return dict
#print(ex2("google.com"))

# get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def ex4(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    return str1
#print(ex4('restart'))

# get a single string from two given strings, separated by a space and swap the first two characters of each string. "abc, xyz" -> "xyc. abz"
def ex5(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    return new_a + ' ' + new_b
#print(ex5('abc', 'xyz'))

# add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
def ex6(string):
    new_string = string

    if len(new_string) > 2:
        if new_string[-3:] == 'ing':
            new_string = new_string + 'ly'
        else:
            new_string = new_string + 'ing'
    return new_string
#print(ex6('abc'))
#print(ex6('string')) 

