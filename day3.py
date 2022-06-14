
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

## Order Pizza (multiple if statements)

greetings = """

Welcome to Python Pizza Deliveries!

MENU

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: +$1
"""

print(greetings)

size = input("What size pizza do you want? S, M, or L? ")
size = size.upper()
print(f"Your ordered {size}. ")

add_pepperoni = input("Do you want pepperoni? Y or N ")
add_pepperoni = add_pepperoni.upper()
print(f"You said {add_pepperoni} to pepperoni. ")

extra_cheese = input("Do you want extra cheese? Y or N ")
extra_cheese = extra_cheese.upper()
print(f"You said {extra_cheese} to extra cheese. ")

sm_price = 15
md_price = 20
lg_price = 25

# determine size, toppings, price
if size == "S" :
    if add_pepperoni == "Y":
        sm_price +=2
    if extra_cheese == "Y":
        sm_price +=1
    print(f"Your total is ${sm_price}. ")
elif size == "M":
    if add_pepperoni == "Y":
        md_price +=3
    if extra_cheese == "Y":
        md_price +=1 
    print(f"Your total is ${md_price}. ")
elif size == "L":
    if add_pepperoni =="Y":
        lg_price +=3
    if extra_cheese == "Y":
        lg_price +=1
    print(f"Your total is ${lg_price}. ")