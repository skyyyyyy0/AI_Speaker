def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

while True:
    user_input = input("Enter a year to check if it is a leap year (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        break
    
    try:
        year = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid year.")
        continue

    if is_leap_year(year):
        print("1 (Leap Year)")
    else:
        print("0 (Not a Leap Year)")