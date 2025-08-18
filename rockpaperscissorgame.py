import random

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def display_result(user_score, computer_score, rounds):
    print("\n🏁 Game Over!")
    print(f"🧮 Total rounds played: {rounds}")
    print(f"📊 Final Score — You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("🎉 You won the game! Great job!")
    elif user_score < computer_score:
        print("😢 Computer won the game. Better luck next time!")
    else:
        print("🤝 It's a draw overall!")

def play_game():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    
    while True:
        user_score = 0
        computer_score = 0
        rounds = 0

        while True:
            user_action = input("\nChoose rock, paper, scissors or type 'quit' to end: ").lower()
            if user_action == "quit":
                break
            if user_action not in ["rock", "paper", "scissors"]:
                print("❗ Invalid choice. Try again.")
                continue

            computer_action = random.choice(["rock", "paper", "scissors"])
            print(f"\n🧍 You chose {user_action}, 🤖 computer chose {computer_action}.")

            result = get_winner(user_action, computer_action)
            rounds += 1

            if result == "tie":
                print("🤝 It's a tie!")
            elif result == "user":
                print("✅ You win this round!")
                user_score += 1
            else:
                print("💻 Computer wins this round!")
                computer_score += 1

            print(f"📈 Score — You: {user_score} | Computer: {computer_score}")

        display_result(user_score, computer_score, rounds)

        play_again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("👋 Thanks for playing! See you next time.")
            break

if __name__ == "__main__":
    play_game()
