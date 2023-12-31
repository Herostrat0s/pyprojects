import random 

while True: # by making the loop we will make sure our program works until we decide to stop it
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None
    while player not in choices: # if player's choice is not equal one of the elements from choices it will ask again
        player = input("Rock, Paper, Scissors?: ").lower() # we use lower() here to accept any kind of 
                                                           # input while turning them into desirable one


    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose")
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You win")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You win")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose")
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You win")
    play_again = input("Play again?: (Yes/No)").lower()

    if play_again !=  "yes":
        break
print("Bye!")