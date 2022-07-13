
# # Day 03 Determine leap year
# '''On every year that is evenly divisible by 4
#     except every year that is evely divisible by 100
#         unless the year is also evenly divisible by 400'''

# year = int(input("Enter the year you want to check: "))

# # leap years: 2020, 2024, 2028

# if year % 4 == 0:
#     #print("It's a leap year.")
#     if year % 100 == 0: 
#         if year % 400 == 0:
#             print("It's a leap year.")
#         else:
#             print("It's not a leap year.")
#     else:
#         print("It's a lear year.")
# else:
#     print("Not a leap year.")


####################################################################### 

# ## Order Pizza (multiple if statements)

# greetings = """

# Welcome to Python Pizza Deliveries!

# MENU

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: +$1
# """

# print(greetings)

# size = input("What size pizza do you want? S, M, or L? ")
# size = size.upper()
# print(f"Your ordered {size}. ")

# add_pepperoni = input("Do you want pepperoni? Y or N ")
# add_pepperoni = add_pepperoni.upper()
# print(f"You said {add_pepperoni} to pepperoni. ")

# extra_cheese = input("Do you want extra cheese? Y or N ")
# extra_cheese = extra_cheese.upper()
# print(f"You said {extra_cheese} to extra cheese. ")

# sm_price = 15
# md_price = 20
# lg_price = 25

# # determine size, toppings, price
# if size == "S" :
#     if add_pepperoni == "Y":
#         sm_price +=2
#     if extra_cheese == "Y":
#         sm_price +=1
#     print(f"Your total is ${sm_price}. ")
# elif size == "M":
#     if add_pepperoni == "Y":
#         md_price +=3
#     if extra_cheese == "Y":
#         md_price +=1 
#     print(f"Your total is ${md_price}. ")
# elif size == "L":
#     if add_pepperoni =="Y":
#         lg_price +=3
#     if extra_cheese == "Y":
#         lg_price +=1
#     print(f"Your total is ${lg_price}. ")


####################################################################### 

## Love calculator

'''
Love Calculator

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"

T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times

Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times

Total = 3
Love Score = 53

Print: "Your score is 53."
'''

# # Don't change the code below
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# # name1 = name1.lower()
# name2 = input("What is their name? \n")
# # name2 = name2.lower()

# combined_name = name1 + name2
# new_name = combined_name.lower()
# # Don't change the code above

# # Get total count for TRUE from two names
# letterT = new_name.count('t')
# letterR = new_name.count('r')
# letterU = new_name.count('u')
# letterE = new_name.count('e')
# countTRUE = letterT + letterR + letterU + letterE
# print("TRUE:", countTRUE)

# # Get total count for LOVE from two names
# letterL = new_name.count('l')
# letterO = new_name.count('o')
# letterV = new_name.count('v')
# letterE = new_name.count('e')
# countLOVE = letterL + letterO + letterV + letterE
# print("LOVE:", countLOVE)

# # Convert scores to string
# scoreTRUE = str(countTRUE)
# scoreLOVE = str(countLOVE)
# score = scoreTRUE + scoreLOVE
# print("score:", score)

# # interpret results
# result = int(score)
# # print(type(result))
# if result < 10 or result > 90:
#     print("Like coke and mentos!")
# elif result > 40 and result < 50:
#     print("You guys are alright.")
# else:
#     print(f"Your score is {result}.")

########################################################################

