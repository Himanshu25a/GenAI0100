import random

user_wins = 0
computer_wins = 0
draw_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user == "q":
        break

    if user not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("computer picked: ", computer_pick + ".")

    if user == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins += 1

    elif user == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1
        
    elif user == "scissors" and computer_pick == "paper":
        print("you won!")
        user_wins += 1

    elif user == "rock" and computer_pick == "rock":
        print("Draw!")
        draw_wins += 1
            
    elif user == "paper" and computer_pick == "paper":
        print("Draw!")
        draw_wins += 1
        
    elif user == "scissors" and computer_pick == "scissors":
        print("Draw!")
        draw_wins += 1
       
    else:
        print("you lost!")
        computer_wins += 1 

print("you won", user_wins, "times.")
print("the computer won",computer_wins,"times.")
print("draw", draw_wins , "times.")
print("Goodbye!")