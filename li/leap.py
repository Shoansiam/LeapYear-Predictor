def is_leap_year(year):
    # Leap years are divisible by 4
    if year % 4 == 0:
        # If a year is divisible by 100, it must also be divisible by 400 to be a leap year
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Input year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year and display the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")