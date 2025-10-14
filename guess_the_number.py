import random

number = random.randint(0, 100)
attempts = 5


while attempts > 0:
    try:
        guess = input()
        guess = int(guess)

        attempts -= 1

        if guess == number:
            print("You got it right!")
            break
        else:
            if guess > number:
                print("Guess bigger than number") 
            else:
                print("Guess smaller than number") 

    except:
        print("not a valid guess type another number")
        continue

if attempts == 0:
    print("You've lost!")