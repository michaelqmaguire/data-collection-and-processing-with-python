# Map, Filter, and List Comprehensions

# -------------------------------------- #
# 23.2 - Map - Check Your Understanding  #
# -------------------------------------- #

# 1. Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = list(map((lambda x: x * 2), lst))

print(greeting_doubled)

# 2. Below, we have provided a list of strings called abbrevs. 
# Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper = list(map((lambda x: x.upper()), abbrevs))

print(abbrevs_upper)

# ----------------------------------------- #
# 23.3 - Filter - Check Your Understanding  #
# ----------------------------------------- #

# 1. Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = list(filter((lambda word: "w" in word), lst_check))

print(filter_testing)

# 2. Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2. Do not hardcode this.

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

lst2 = list(filter((lambda word: "o" in word), lst))

print(lst2)

# ------------------------------------------------------ #
# 23.3 - List Comprehensions - Check Your Understanding  #
# ------------------------------------------------------ #

# 2. The for loop below produces a list of numbers greater than 10.
# Below the given code, use list comprehension to accomplish the same thing. Assign it the the variable lst2.
# Only one line of code is needed.

L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

lst2 = [element for element in L if element > 10]

# 3. Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the dictionary tester.
# Do this using a list comprehension.

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

compri = [n['name'] for n in tester['info']]

# -------------------------------------- #
# 23.3 - Zip - Check Your Understanding  #
# -------------------------------------- #

# 1. Below we have provided two lists of numbers, L1 and L2.
# Using zip and list comprehension, create a new list, L3, that sums the two numbers if the number from L1 is greater than 10 and
# the number from L2 is less than 5. This can be accomplished in one line of code.

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2)) if (x1 > 10) & (x2 < 5)] 