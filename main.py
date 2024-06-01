import random

def coin_flip():

    while True:

        choices = ("head", "number")
        pc_choice = random.choice(choices)

        print("\n")
        player_choice = input("Please type in Head or Number to continue: ").lower()

        print(f"The player has chosen: {player_choice}")
        print(f"The PC has chosen: {pc_choice}")

        if player_choice not in choices:
            print("Invalid choice. Please type in 'Head' or 'Number' to continue.")
            continue

        if player_choice == pc_choice:
            print("Player won, good job! \n")
        else:
            print("PC won, try again next time. \n")

        while True:
            continue_choice = input(
                "Please type 'continue' if you want to continue the game or \n"
                "'break' if you want to end the game: ").lower()

            if continue_choice == "continue":
                print("Okay, you will continue the game.")
                break

            elif continue_choice == "break":
                print("Thank you for playing this little game. Goodbye!")
                return
            
            else:
                print("Invalid input. Please type 'continue' or 'break'.")

coin_flip()

