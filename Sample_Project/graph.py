x = int(input("Input x-coordinate: "))
y = int(input("Input y-coordinate: "))

if x > 0:
    if y > 0:
        print("The point ({}, {}) is in quadrant 1.".format(x, y))
    elif y < 0:
        print("The point ({}, {}) is in quadrant 4.".format(x, y))
    else:
        print("The point ({}, {}) is on the positive x-axis.".format(x, y))
elif x < 0:
    if y > 0:
        print("The point ({}, {}) is in quadrant 2.".format(x, y))
    elif y < 0:
        print("The point ({}, {}) is in quadrant 3.".format(x, y))
    else:
        print("The point ({}, {}) is on the negative x-axis.".format(x, y))
else:
    if y > 0:
        print("The point ({}, {}) is on the positive y-axis.".format(x, y))
    elif y < 0:
        print("The point ({}, {}) is on the negative y-axis.".format(x, y))
    else:
        print("The point ({}, {}) is at the origin.".format(x, y))