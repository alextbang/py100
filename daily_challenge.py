# Day 01 Band name generator
# print("Hi, welcome to the band name generator app. \n")
# city = input("What city did you grow up in? \n")
# pet = input("What is your pet's name? \n")
# band = city + pet
# print("Your band name is " + band + ".")

# Day 02 Tip calculator
# print("Welcome to the tip calculator.")
# bill = float(input("What was the toal bill? $"))
# tip = int(input("What percentage tip wold you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# split = (round(((bill + tip)/people),2))
# print(f"Each person should pay {split}")

# Day 03 Determine leap year
'''On every year that is evenly divisible by 4
    except every year that is evely divisible by 100
        unless the year is also evenly divisible by 400'''

year = int(input("Enter the year you want to check: "))
# print(year)
# leap years: 2020, 2024, 2028

if year % 4 == 0:
    #print("It's a leap year.")
    if year % 100 == 0: 
        if year % 400 == 0:
            print("It's a leap year.")
        else:
            print("It's not a leap year.")
    else:
        print("It's a lear year.")
else:
    print("Not a leap year.")

