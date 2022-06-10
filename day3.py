
# Day 03 Determine leap year
'''On every year that is evenly divisible by 4
    except every year that is evely divisible by 100
        unless the year is also evenly divisible by 400'''

year = int(input("Enter the year you want to check: "))

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

