import random

max_number = input("Enter the maximum number for the game:").strip()

if max_number.isdigit():
    max_number = int(max_number)

    if max_number <= 0:
        print("Please print a number greater than 0..")
        quit()

else:
    print("Please type a number next time: ").strip()
    quit()

rand_numb = random.randint(0, max_number)
total_guess = 0

while True:
    total_guess += 1
    user_input = input("Make your first guess: ").strip()
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Please type a valid number next time. Bozo")
        continue

    if user_input == rand_numb:
        print("You got the answer right! hoki asem")
        break
    elif user_input > rand_numb:
        print("You went above the answer")
    else:
        print("You went below the answer")

print("Lol finally, congrats you got it in ", total_guess, "guesses")
