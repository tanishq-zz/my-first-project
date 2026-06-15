import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    score = {"user": 0, "computer": 0}

    while True:
        user_choice = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower()

        if user_choice == "quit":
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            score["user"] += 1
        else:
            print("Computer wins this round!")
            score["computer"] += 1

        print(f"Score -> You: {score['user']} | Computer: {score['computer']}")

    print("\nFinal Score:")
    print(f"You: {score['user']} | Computer: {score['computer']}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
