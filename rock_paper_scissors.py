import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors: ").lower()

    if player == computer:
        print("computer played: " + computer)
        print("you played: " + player)
        print("You tied")
    elif player == "rock":
        if computer == "paper":
            print("computer played: " + computer)
            print("you played: " + player)
            print("You lose")
        if computer == "scissors":
            print("computer played: " + computer)
            print("you played: " + player)
            print("You win")
    elif player == "scissors":
        if computer == "rock":
            print("computer played: " + computer)
            print("you played: " + player)
            print("You lose")
        if computer == "paper":
            print("computer played: " + computer)
            print("you played: " + player)
            print("You win")
    elif player == "paper":
        if computer == "scissors":
            print("computer played: " + computer)
            print("you played: " + player)
            print("You lose")
        if computer == "rock":
            print("computer played: " + computer)
            print("you played: " + player)
            print("You win")
    play_again = input("Play again? (Yes/No): ").lower()

    if play_again != "yes":
        break

print("Thanks for playing")

