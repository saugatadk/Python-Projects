import random

def computer_choice():
    random_number = random.randint(1,3)
    options = {1: "rock", 2: "paper", 3: "scissors"}
    choice_value = options[random_number]
    return choice_value

def user_choice():
    user_input = input("Enter rock/paper/scissors: ")
    user_input = user_input.lower()
    return user_input

def get_result(user_pick, computer_pick):
    if(user_pick == computer_pick):
        return "draw"
    elif (user_pick == "rock" and computer_pick == "scissors"):
        return "win"
    elif (user_pick == "paper" and computer_pick == "rock"):
        return "win"
    elif(user_pick == "scissors" and computer_pick == "paper"):
        return "win"
    else:
        return "lose"

while True:
    user_pick = user_choice()
    if user_pick in ["rock", "paper", "scissors"]:
        break
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")

computer_pick = computer_choice()
result = get_result(user_pick, computer_pick)

print(f"Your pick: {user_pick}")
print(f"Computer's pick: {computer_pick}")
print(f"You {result}")