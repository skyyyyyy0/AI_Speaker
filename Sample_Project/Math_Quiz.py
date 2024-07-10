import random
import time

playing = True
score = 0
count = 0
start_time = time.time()

while playing:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    answer = num1 * num2 - num3
    user_input = int(input("{0} X {1} - {2} = ".format(num1, num2, num3)))
    count += 1
    if answer == user_input:
        score += 1
        print("Correct! Your score is now {}".format(score))
    else:
        playing = False
        print("Incorrect. The correct answer was {}.".format(answer))

end_time = time.time()
print("You attempted {} questions. Your total time was {:.2f} seconds.".format(count, end_time - start_time))