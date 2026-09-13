import random
que = int(input("Kindly guess a number btw the range of 1-100"))

if que > 100 :
    print("Too High")
elif que < 100:
    print("Too low")
number = random.randint(1,100)

print(number)

