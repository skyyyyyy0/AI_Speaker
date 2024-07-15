import random 

select = ['rock', 'paper', 'scissors']

while True:
    computer = random.choice(select)
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if user not in select:
        print("Wrong input. Try again.")
        continue

    print("Computer chose: %s" % computer)
    print("You chose: %s" % user)
    
    if user == computer:
        print("It's a tie!")
    elif (user == 'scissors' and computer == 'paper') or \
         (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock'):
        print("You win!")
    else:
        print("You lose")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
    
