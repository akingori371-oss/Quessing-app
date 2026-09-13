import random
que = int(input("Kindly guess a number btw the range of 1-100"))

def checker() :

  if que > 100 :
    print("Too High")
    exit()

  elif que < 1:
    print("Too low")
    exit()

  else:
     determiner()
 
number = random.randint(1,100)

start = 5

def determiner( ) :
   
   global start

   if que == number:
    print("You have quessed correctly")

   else:
    print("You have guessed the wrong number")
    print(f"The correct number was {number}" )

    start -= 1

    print(f"You are now remaining with {start} chances to guess correctly")

checker()
