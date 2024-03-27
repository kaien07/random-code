import random

gamemode = input("Would you like to guess the number or have the computer guess the number? Pick G to guess or C to have the computer guess. ")

if gamemode == "G":
    upp_lim_G = int(input("Pick the upper limit of the range of numbers that you will guess from. "))
    low_lim_G = int(input("Pick the lower limit of the range of numbers that you will guess from. "))
    answer = random.randint(low_lim_G, upp_lim_G)
    guess = int(input(f"A number from {low_lim_G} to {upp_lim_G} has been generated. Make your guess! "))
    num_try_G = 1
    while guess != answer:
        if guess > answer:
            guess = int(input("Too high! Try again. "))
            num_try_G += 1
        elif guess < answer:
            guess = int(input("Too low! Try again. "))
            num_try_G += 1
    if guess == answer:
        print(f"Congratulations! The number was {answer} and you took {num_try_G} tries to guess it.")

if gamemode == "C":
    upp_lim_C = int(input("Pick the upper limit of the range of numbers that the computer will guess from. "))
    low_lim_C = int(input("Pick the lower limit of the range of numbers that the computer will guess from. "))
    guess = random.randint(low_lim_C, upp_lim_C)
    feedback = input(f"Is your number {guess}? (Y) Or is it too high (H) or too low? (L) ")
    num_try_C = 1
    while feedback != "Y":
        if feedback == "H":
            upp_lim_C = guess - 1
        if feedback == "L":
            low_lim_C = guess + 1
        guess = random.randint(low_lim_C, upp_lim_C)
        num_try_C += 1
        feedback = input(f"Is your number {guess}? ")
    if feedback == "Y":
        print(f"Your number is {guess} and it took me {num_try_C} tries to guess it!")
