import random

options = ("rock", "paper", "scissor")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock, paper, scissors):")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie !")
    elif player == "rock" and computer == "scissor":
        print("You win !")
    elif player == "paper" and computer == "rock":
        print("You win !")
    elif player == "scissor" and computer == "paper":
        print("you win !")
    else:
        print("you lose !")

    if not input("Play again ? (YES/NO):").upper() == "YES":
        running = False

    print("Thanks for playing!")