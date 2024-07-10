Coffee = '$$$'
Menu = '''- menu -
1. Ice coffee = $3.7
2. Latte = $4.7
3. Ice tea = $4.3
'''
print(Coffee)
print(Menu)
print("=" *45)
coffee_price = 0
total_price = 0
change = 0
order = int(input("choose your coffee : "))
if order == 1:
    coffee_price = 3.7
elif order == 2:
    coffee_price = 4.7
elif order == 3:
    coffee_price = 4.3
    
cups = int(input("How many? "))
total_price = coffee_price * cups
received = int(input("Total price is ${:.2f}. Insert coin : ".format(total_price)))

if received >= total_price:
    change = received - total_price
    print("We got ${:.2f}. Here some change ${:.2f}".format(received,change))
else:
    print("Insufficient funds1")