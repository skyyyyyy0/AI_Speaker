import random

# Computer selects a random number between 1 and 100
number = random.randint(1, 100)

# Set the number of chances
chance = 10
count = 0 

print("Guess the number between 1 and 100. You have 10 chances!")

while count < chance:
    user_input = int(input("Guess your number: "))
    count += 1
    
    if user_input == number:
        print("Congratulations! You've guessed the number {} correctly in {} tries.".format(number, count))
        break
    elif user_input < number:
        print("Your guess is too low. Try again. ({} chances left)".format(chance - count))
    elif user_input > number:
        print("Your guess is too high. Try again. ({} chances left)".format(chance - count))

if count == chance and user_input != number:
    print("Sorry, you've used all your chances. The number was {}. Better luck next time!".format(number))