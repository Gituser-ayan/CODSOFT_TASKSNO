import random


def get_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower().strip()

        if choice in ["rock", "paper", "scissors"]:
            return choice

        print("Invalid choice. Try again.")


def winner(player, computer):
    if player == computer:
        return "tie"

    if (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "player"

    return "computer"


def main():
    player_score = 0
    computer_score = 0
    tie_score = 0

    print("=== Rock Paper Scissors ===")

    while True:
        player = get_choice()
        computer = random.choice(["rock", "paper", "scissors"])

        print("You chose:", player)
        print("Computer chose:", computer)

        result = winner(player, computer)

        if result == "player":
            print("You win!")
            player_score += 1
        elif result == "computer":
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")
            tie_score += 1

        print(
            f"Score -> You: {player_score}, "
            f"Computer: {computer_score}, Ties: {tie_score}"
        )

        again = input("Play again? (y/n): ").lower().strip()

        if again != "y":
            break

    print("\nFinal Score")
    print("You:", player_score)
    print("Computer:", computer_score)
    print("Ties:", tie_score)


if __name__ == "__main__":
    main()
