import datetime 

# Get user input for year, month, and day
year = int(input("What year were you born? "))
month = int(input("What month were you born? "))
day = int(input("What day were you born? "))

# Create a datetime object for the birthday
bday = datetime.datetime(year, month, day)

# Dictionary to map weekday numbers to names
weekday_dict = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

# Get the weekday and print the result
weekday = bday.weekday()
print("You were born on a {}.".format(weekday_dict[weekday]))