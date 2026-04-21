print("Welcome to my quiz game!")

user_input = input("Do you want to play the quiz game? (yes/no): ").strip()

if user_input.lower() != "yes":
    quit()

print("Aye! Let's play dude")
score = 0

answer = input("What's 9+10\n").strip()
if answer != ' 21':
    print("That's incorrect!")
else:
    print("That's correct!")
    score += 1

answer = input("69-x = 2, solve for x\n").strip()
if answer != ' 67':
    print("That's incorrect!")
else:
    print("That's correct!")
    score += 1

answer = input("What's the biggest club in England?\n").strip()
if answer != " Manchester United":
    print("That's incorrect!")
else:
    print("That's correct!")
    score += 1

answer = input("28.5 = 1/2 x, solve for x\n").strip()
if answer != ' 67':
    print("Thats incorrect!")
else:
    print("That's correct")


print("Great Job! You got " + str(score) + " questions correct.")
print("Out of 100, you got " + str((score/100) * 100) + "%. ")
