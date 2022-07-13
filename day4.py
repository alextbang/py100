import random

# # generate random integers including parameters
# random_integer = random.randint(1, 10)
# print(random_integer)

# #generate random floating numbers, not including the top parameter
# random_float = random.random()
# print(random_float)

############################################################

# Provide a list of names, then draw one person at random.

# take input as a string
names_list = input("Provide a list of 3 names separated by a comma. \n")
print("You provided:", names_list)

# split each name separated by commas and create a list
list_csv = names_list.split(", ")
# print("list_csv:", list_csv)

# draw a number at random
random_integer = random.randint(1, 3)
# print("random integer -->", random_integer)

# assign numbers to names
if random_integer == 1:
    print(list_csv[0], "pays for dinner!")
elif random_integer == 2:
    print(list_csv[1], "pays for dinner!")
else:
    print(list_csv[2], "pays for dinner!")