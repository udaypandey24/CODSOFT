import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS =====")
print("Best of 3 Rounds")

for round_number in range(1, 4):

    print(f"\nRound {round_number}")

    player_choice = input("Enter rock, paper or scissors: ").lower()

    if player_choice not in choices:
        print("Invalid Choice! Round Skipped.")
        continue

    computer_choice = random.choice(choices)

    print("Computer Chose:", computer_choice)

    if player_choice == computer_choice:
        print("Round Tied!")

    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):

        print("You Won This Round!")
        player_score += 1

    else:
        print("Computer Won This Round!")
        computer_score += 1

print("\n===== FINAL RESULT =====")
print("Your Score:", player_score)
print("Computer Score:", computer_score)

if player_score > computer_score:
    print("Congratulations! You Won The Match.")
elif computer_score > player_score:
    print("Computer Won The Match.")
else:
    print("Match Draw.")
