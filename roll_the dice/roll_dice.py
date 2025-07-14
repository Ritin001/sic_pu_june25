import random
number = random.randint(0,10)
chance = 1
win=False
while chance <= 3:
    guess = int(input(f"Guess the number (Chance {chance}): "))
    if guess == number :
        print("you guessed it correct")
        win = True
        break
    elif guess >=number:
        print("you guessed wrong  number, number is smaller than",guess)
    else:
        print("you guessed wrong  number, number is greater than",guess)
    chance += 1
if win:
    print("you won the game")
else:
    print("you lost the game")
    print("the number is ", number)