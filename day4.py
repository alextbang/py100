import random

# # generate random integers including parameters
# random_integer = random.randint(1, 10)
# print(random_integer)

# #generate random floating numbers, not including the top parameter
# random_float = random.random()
# print(random_float)

############################################################

# Prompt for a list of names, then draw one person at random to pay the bill!

# take input as a string
names_list = input("Provide a list of names separated by a comma. \n")
print("You provided:", names_list)

# split each name separated by a comma and create a list
list_csv = names_list.split(", ")
print("number of names -->", len(list_csv))

number_people = len(list_csv)
# print("list_csv:", list_csv)

# draw a number at random to represent random person to be drawn
random_integer = random.randint(1, number_people)
# print("random integer -->", random_integer)

# get the name of person from the list by using their index
print(list_csv[random_integer - 1], "pays for dinner!")
