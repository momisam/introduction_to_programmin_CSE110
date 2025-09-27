# Adventure Game
# Description: A simple text-based game with at least 3 levels of choices.

print("Welcome to the Haunted House Adventure!")
print("You slowly walk inside a dark, creaky house...")

choice1 = input("You enter a haunted house. Do you go LEFT or RIGHT? ").lower()

if choice1 == "left":
    choice2 = input("You see a FRIDGE and a CABINET. Which do you open? ").lower()
    if choice2 == "fridge":
        print("Rotten food! You faint. GAME OVER.")
    elif choice2 == "cabinet":
        print("You find a hidden passage! YOU WIN!")
    else:
        print("That’s not a valid choice.")

elif choice1 == "right":
    choice2 = input("You see a TV, a SOFA, and a DOOR. Which do you check? ").lower()
    if choice2 == "tv":
        print("The TV turns on by itself. GAME OVER.")
    elif choice2 == "sofa":
        choice3 = input("You find a creepy note. Do you RUN or HIDE? ").lower()
        if choice3 == "run":
            print("You run outside and escape. YOU WIN!")
        elif choice3 == "hide":
            print("You hide but the shadows find you. GAME OVER.")
        else:
            print("That’s not a valid choice.")
    elif choice2 == "door":
        print("You are trapped in the basement. GAME OVER.")
    else:
        print("That’s not a valid choice.")

else:
    print("That’s not a valid choice.")
