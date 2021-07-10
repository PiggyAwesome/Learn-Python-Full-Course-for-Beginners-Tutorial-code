# If Statements

#  I wake up
#  If I'm hungry
#     I eat breakfast
#
#  I leave my house
#  if it's cloudy
#      I bring an umbrella
#  otherwise
#     I bring sunglasses
#
#  Im at a restaurant
#  if I want meat
#      I order a steak
#  otherwise if i want pasta
#      I order spaghetti & meatballs
#  otherwise
#      I order a salad.
'''

is_male = False
if is_male:
    print("You are a male")
else:
    print("You are not a male")


is_male = False
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both"

'''

is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are a male and not tall")






