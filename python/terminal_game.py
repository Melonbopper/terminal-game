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
while True:
    start = input("Type Start to begin your adventure!  ").strip().lower()
    if start == 'start':
        print() # blank line
        print("Initializing spaceship systems...")
        break
    else:
        print("You must type start")

print("On board computer initialized")
print() # blank line
print("Computer: ...Captain, we have been drifting for quite some time now.")
print("Computer: ...We need to find a way to repair the ship and get back to Earth.")
print() # blank line

search = 0
repair = 0
looking = 0
pull = 0
ship_repaired = 0

while True:
    print("================================")
    print("search, repair, coffee, quit")
    print("================================")
    path=input("\nWhat would you like to do?  ").strip().lower()

    if path == "search":
        print("\n...Engaging GravSweep... ")

        while True:
            action=input("\nType pull to bring in space debris, Type back to disengage the GravSweep:  ").strip().lower()
            space_debris = random.randint(0, 251)

            if action == "pull":

                if pull >=4:
                    print("\n=======================")
                    print("!GravSweep Overheated!")
                    print("=======================")
                    print("******************************************")
                    print("You're getting tired...take a coffee break")
                    print("******************************************")
                    rest = input("\nType 'back' to return for coffee.  ")
                    if rest == 'back':
                        print() # blank line
                        pull = 0 # Reset pull count
                        break #forced exit to prevent spam
                    else:
                        print("You need caffine!")

                elif pull == 0:
                        print("\n===============================")
                        print("Damn...another Null Coil Cap")
                        print("===============================")
                        pull += 1

                elif pull == 1:

                    if space_debris % 5 == 0:
                        looking = ("\nYou found a [PHASE GEAR MANIFOLD!]") #Finally found it
                        print("HEY! THERE IT IS!!!")
                        print(looking)
                        print("Finally...")
                        print("\nGo 'back' to repair the ship!")
                        repair += 1

                    else:
                        print("\n==============================================================")
                        print("Where would an Auxiliary Coupler Ring come from way out here?")
                        print("==============================================================")
                        pull += 1

                elif pull == 2:
                    print("\n===============================================")
                    print("A Plasma Spooler? That's pretty cool to see...")
                    print("===============================================")
                    pull += 1

                elif pull == 3:
                    print("\n============================================")
                    print("Huh? Looks like something really strange...")
                    print("============================================")
                    pull += 1

                if pull == 4:
                    search += 1
                    if search == 1:
                        print("\n==================================================")
                        print("The GravSweep feels warm...")
                        print("==================================================")

            elif action == "back":
                print("\nGravSweep disengaged.")
                break  # leave the search loop

            else:
                print("Invalid GravSweep command.")


    elif path == "repair":
        if  repair < 1:
            print("\nNo Parts Found")
        else:
            print("\nInstalling [PHASE GEAR MANIFOLD]")
            print("....")
            print("\nINSTALL COMPLETE!")
            ship_repaired += 1
            repair  -= 1
            
            if ship_repaired >= 1:
                print("\n===============================")
                print("Captian...the ship has been fully repaired!")
                print("We can finally return to earth!")
                print("=================================")

                next_action = input("\nType 'earth' to return home:  ")
                if next_action == "earth":
                    print("\nNavigation system engaged... Setting course for Earth.")
                    print("Congratulations! You made  it home safely.")
                    print("==== GAME OVER ====")
                    break

    elif path == "coffee":
        coffee_choice = input("\nComputer: What kind of coffee would you like? (Nebula Brew, Quantum Roast, Dark Matter Drip, Hyperfuel Espresso):  ").strip().lower()

        print(f"{coffee_choice.title()}...processing order")

        if coffee_choice == "nebula brew":
            print("Nebula Brew selected. Infusing your cup with the silence of collapsing stars.")
        elif coffee_choice == "quantum roast":
            print("Quantum Roast confirmed. Brewed simultaneously in the past and your impatient present.")
        elif coffee_choice == "dark matter drip":
            print("Dark Matter Drip engaged. Warning: gravitational pull may increase productivity.")
        elif coffee_choice == "hyperfuel espresso":
            print("Hyperfuel Espresso incoming. Strap in--this shot bends local time.")
        else:
            print("Unknown brew. The replicator sputters uncertainly.")

    elif path == "quit":
            print("Exiting game. Safe travels, captain.")
            break
    else:
        print(f"\nCommand Error: '{path}' is not a recognized command. Please type: search, repair, coffee, or quit.")

# I'm pretty sure this is the end of the game, I feel like it's pretty good for a first try
