import random
lotto_num = []

def getRandomNumber():
    number = random.randint(1,46)
    return number
count = 0
while True:
    if count > 5:
        break
    random_number = getRandomNumber()
    if random_number not in lotto_num: # It's to prevent duplicate numbers.
        lotto_num.append(random_number)
        count = count + 1
        
print(lotto_num)