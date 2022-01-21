# %%
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
# %%

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

# %%
# ------------------------------------------------------------- #
# 17.3 - Nested Dictionaries - Check Your Understanding       #
# ------------------------------------------------------------- #

