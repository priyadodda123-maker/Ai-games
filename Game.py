import random

choices = ["rock", "paper", "scissors"]
user_history = []

user_score = 0
comp_score = 0

def predict_user_move():
    if not user_history:
        return random.choice(choices)
    return max(set(user_history), key=user_history.count)

def get_computer_move():
    predicted = predict_user_move()

    if predicted == "rock":
        return "paper"
    elif predicted == "paper":
        return "scissors"
    else:
        return "rock"

while True:
    user = input("Enter rock/paper/scissors (or 'exit'): ").lower()

    if user == "exit":
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    comp = get_computer_move()
    user_history.append(user)

    print("Computer:", comp)

    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        comp_score += 1

    print("Score -> You:", user_score, "| Computer:", comp_score)
  output:
Enter rock/paper/scissors (or 'exit'): Rock
Computer: scissors
You win!
Score -> You: 1 | Computer: 0
Enter rock/paper/scissors (or 'exit'): exit 
