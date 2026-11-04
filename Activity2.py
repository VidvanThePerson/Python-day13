import random
while True:
    user_action = input("Enter a choice(rock,paper,scissors)").lower()
    while user_action not in ["rock","paper","scissors"]:
        print("Wrong Choice")
        user_action = input("Enter a choice(rock,paper,scissors)").lower()
    possible_actions = ["rock","paper","scissors"]
    comp_action = random.choice(possible_actions)
    print(f"You chose {user_action}, computer chose {comp_action}")
    if user_action == comp_action:
        print("Tie!")
    elif user_action == "rock":
        if comp_action == "scissors":
            print("You Win!")
        elif comp_action == "paper":
            print("You Lose.")
    elif user_action == "scissors":
        if comp_action == "paper":
            print("You Win!")
        elif comp_action == "rock":
            print("You Lose.")
    elif user_action == "paper":
        if comp_action == "rock":
            print("You Win!")
        elif comp_action == "scissors":
            print("You Lose.")
    play_again = input("Play again?(y/n)").lower()
    if play_again == "n":
        break