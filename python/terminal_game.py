#Start of a simple terminal game in Python
#This game wil be a text-based space adventure game
#The player will search for items through space to obtain parts to fix the spaceship
#Once repaired the player can then choose to send player into space or return to earth
#The game will be played in the terminal

import random

print('=====================================')
print("Welcome to the Space Adventure Game!")
print('=====================================')

# Start the game
start = str(input("Type Start to begin your adventure!  "))

if start == 'Start' or start == 'start':
    print() # blank line
    print("Initializing spaceship systems...")


print("On board computer initialized")
print() # blank line
print("Computer: ...Captain, we have been drifting for quite some time now.")
print("Computer: ...We need to find a way to repair the ship and get back to Earth.")
print() # blank line
print("==========================================================================")

search = 0
repair = 0
looking = 0
pull = 0
ship_repaired = 0
space_debris = random.randint(1, 26)
looking = ("You found a [PHASE GEAR MANIFOLD!]") #Finally found it


while True:
    print("\nsearch. repair. coffee. quit.")
    path=input("\nWhat would you like to do?  ")
    if path == "search":
        print("\n...Engaging GravSweep... ")
        action=input("\nType pull to bring in space debris:  ")
        if action == "pull" and space_debris % 3:
            pull = pull + 1
            print("===============================")
            print("Damn...another Null Coil Cap")
            print("===============================")
        elif pull < 1:
            pull = pull + 1
            print("==============================================================")
            print("Where would an Auxiliary Coupler Ring come from way out here?")
            print("==============================================================")
        elif pull >= 10:
                print("=======================")
                print("\nGravSweep Overheated")
                pull = 0 # Reset pull count
        elif pull >= 1 and space_debris % 5:
            print(looking)
            repair = repair + 1
        elif pull >= 4:
            search == search + 2  

    elif path == "repair":
        if  repair < 1:
            print("\nNo Parts Found")
        else:
            print("\nInstalling [PHASE GEAR MANIFOLD]")
            print("....")
            print("INSTALL COMPLETE!")
            ship_repaired = ship_repaired + 1

    elif path == "coffee":
        coffee_choice = (input("\nComputer: What kind of coffee would you like? " " Nebula Brew. Quantum Roast. Dark Matter Drip. Hyperfuel Espresso.   "))
        if coffee_choice == "Nebula Brew.":
            print("Nebula Brew selected. Infusing your cup with the silence of collapsing stars.")
        elif coffee_choice == "Quantum Roast.":
            print("Quantum Roast confirmed. Brewed simultaneously in the past and your impatient present.")
        elif coffee_choice == "Dark Matter Drip.":
            print("Dark Matter Drip engaged. Warning: gravitational pull may increase productivity.")
        elif coffee_choice == "Hyperfuel Espresso.":
            print("Hyperfuel Espresso incoming. Strap in--this shot bends local time.")

    elif quit:
        if path == "quit":
            print("Exiting game. Safe travels, captain.")
            break

    else:
        print("\nWhat are you doing? You have no other choice but to say one of 4 options...")