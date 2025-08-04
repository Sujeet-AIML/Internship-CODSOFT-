import random

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

def get_winner(user, computer):
    if user == computer:
        return 'tie'
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'paper' and computer == 'rock') or \
       (user == 'scissors' and computer == 'paper'):
        return 'user'
    return 'computer'

while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice.")
        continue
    computer = random.choice(choices)
    print("Computer chose:", computer)
    winner = get_winner(user, computer)
    if winner == 'user':
        print("You win!")
        user_score += 1
    elif winner == 'computer':
        print("Computer wins!")
        computer_score += 1
    else:
        print("It's a tie!")
    print(f"Score - You: {user_score} | Computer: {computer_score}")
    if input("Play again? (yes/no): ").lower() != 'yes':
        break
