# Nested Data and Nested Iteration

# ------------------------------------------------------------- #
# 17.1.1 - Lists with Complex Items - Check Your Understanding  #
# ------------------------------------------------------------- #

# 1. Below, we have provided a list of lists. Use indexing to assign the element ‘horse’ to the variable name idx1.

animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]

idx1 = animals[1][0]

print(idx1)
# %%

# 2. Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable plant.

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]

plant = data[7][0][0]

print(plant)
# ------------------------------------------------------------- #
# 17.1.1 - Nested Dictionaries - Check Your Understanding       #
# ------------------------------------------------------------- #

# 1. Extract the value associated with the key color and assign it to the variable color. Do not hard code this.

info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

color = info['personal_data']['physical_features']['color']

print(color)

# ------------------------------------------------------------- #
# 17.4 - Nested Iteration - Check Your Understanding            #
# ------------------------------------------------------------- #

#2. Below, we have provided a list of lists that contain information about people. Write code to create a new list that contains every person’s last name, and save that list as last_names.

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]

last_names = []

for person in info:
  last_names.append(person[1])

print(last_names)

# 3. Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings.

L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]

b_strings = []

for lst in L:
  for sublst in lst:
    if 'b' in sublst:
      b_strings.append(sublst)

print(b_strings)
