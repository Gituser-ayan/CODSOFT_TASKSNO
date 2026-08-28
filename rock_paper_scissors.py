import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    
    beats = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if beats[user] == computer:
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("=== Rock, Paper, Scissors ===")
    
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()

        if user_choice == 'quit':
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
