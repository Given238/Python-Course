
name = input("What is your name? ")
user_input = input(
    "Welcome to this adventure game! Would you like to embark on a brand new adventure? (y/n)").lower().strip()
if user_input == "y":
    print(
        f"Situation: You are {name}, a follower of Christ. You are faced with a choice to go on the narrow road or the wide road.")
    answer = input("Which Road will you choose? (N/W)").strip()

    if answer == "N":
        print("You have chosen the narrow path.")
        answer = input(
            "Are you willing to suffer for the next 10 years of your life? (Y/N)").strip()
        if answer == "Y":
            print(
                "Even though the world has hated you. Take heart, I have overcome the world.")
            print(
                "You win, Child. Jesus has proclaimed victory over sin and shame ever since His ressurection.")
        elif answer == "N":
            print("You lose.")
        else:
            print("Not a valid option. You lose.")

    elif answer == "W":
        print("You have chosen the wide path.")
        answer = input(
            "Congrats! You are going to have fun for the next 10 years of your life. Do you want to proceed? (Y/N)").strip()
        if answer == "Y":
            print("Come back to Jesus, Child. This is not the life you want.")
        elif answer == "N":
            print("Enter through the narrow gate. For narrow is the road that leads to life, and only a few find it.")

        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option, you lose.")

print("Thank you for trying", {name})
