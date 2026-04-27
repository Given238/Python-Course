import random

wins = 0
computer_wins = 0

moves = ["rock", "paper", "scissors"]

while True:
    user_input = input("What move do you want to use on the computer?").lower()
    if user_input == "q":  # essentialy q means stop/quit a program
        break
    if user_input not in moves:
        continue

    random_number = random.randint(0, 2)
    computer_moves = moves[random_number]
    print("The computer used" + computer_moves + "on you.")

    if user_input == "rock" and computer_moves == "scissors":
        print("You win!")
        wins += 1
    elif user_input == "paper" and computer_moves == "rock":
        print("You win!")
        wins += 1
    elif user_input == "scissors" and computer_moves == "paper":
        print("You win!")
        wins += 1
    else:
        print("You lost!")
        computer_wins += 1

    print(f"You got a total of {wins} wins.")
    print(f"The computer got a total of {computer_wins} wins.")
    if wins > computer_wins:
        print(f"You are leading by {wins - computer_wins} wins")
    elif computer_wins > wins:
        print(f"The computer is leading by {computer_wins - wins} wins")
    else:
        print("It is currently a tie!")
    print("Goodbye!")
