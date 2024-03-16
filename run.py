import time

print("Welcome to the captivating adventure of 'Escape From the Cave'!")

time.sleep(2)

print("Embark on an epic RPG journey where your choices shape the course of the game.\n"
    "Each decision you make leads to a unique path, ensuring a thrilling and unpredictable experience.")

'''
    Default function if the user choose the high ground to reuse in different parts
'''
def user_choice_high_ground():
    
    user_input = input("1. Climb the Step Incline\n"
                                    "2. Investigate the Hidden Chamber\n"
                                    ">>> ")
    
    if user_input == '1':
        climb_steep_incline()
        
        # WIN THE GAME
    elif user_input == '2':
        investigate_hidden_chamber()
        
        # GAME OVER
        
        play_again()
    else:
        
        print("Invalid choice. The adventure awaits, make a valid selection.")

'''
    Default function if the user wants to play again
'''
def play_again():
    while True:
        play_again_input = input("\nDo you wish to play again?\n"
                        "Y to play again or N to quit the game\n"
                        ">>> ").lower()
        
        if play_again_input == 'y':
            if intro():
                print("\nYou find yourself standing at a crossroads within the cave.\n"
                        "Two paths stretch out before you. What will you choose?")
                
                while True:
                    player_choose = input("1. Explore the Dark Tunnels\n"
                                    "2. Search for High Ground\n"
                                    ">>> ").lower()
                    if player_choose == '1':
                        explore_dark_tunnels()
                        break
                    elif player_choose == '2':
                        search_for_high_ground()
                        break
                    else:
                        print("Invalid choice. The adventure awaits, make a valid selection.")
        elif play_again_input == 'n':
            print("Thanks for playing Scape from the Cave. Hope to see you soon.")
            exit()
        else:
            print("Invalid choice. Please, make a valid selection.")

#################### PART 1 ####################

def intro():
    print("\nYou embarked on a camping trip in the heart of the forest with your closest friends.\n"
        "As the sun set, an unexpected storm unleashed its fury, triggering a landslide on the hill.\n"
        "The road back home is now blocked by fallen debris.")

    time.sleep(6)

    print("\nDuring the restless night, disaster strikes when the ground beneath your campsite collapses,\n"
        "plunging everyone into a mysterious cave. In the dim light, you realize everyone is injured\n"
        "and finding an escape becomes the top priority.")

    time.sleep(6)

    print("\nIn the face of uncertainty, your friends turn to you, placing their trust in your leadership.\n"
        "With your seasoned experience in adventurous pursuits, you find yourself at the forefront\n"
        "of this unexpected challenge, taking charge to lead your friends to safety.")
    
    print("\nYou find yourself standing at a crossroads within the cave.\n"
            "Two paths stretch out before you. What will you choose?")
        
    player_choose = input("1. Explore the Dark Tunnels\n"
                        "2. Search for High Ground\n"
                        ">>> ").lower()
    
    if player_choose == "1":
        explore_dark_tunnels()
    elif player_choose == '2':
        search_for_high_ground()
    else:
        print("Invalid choice. The adventure awaits, make a valid selection.")
    
    return True

'''
    Option that the user has to choose to keep playing the game.
'''
def explore_dark_tunnels():
    print("\nYou decide to delve into the dark tunnels, guided only by the faint glow of your flashlight.\n"
        "As you navigate through the winding passages, you discover ancient markings on the cave walls.\n"
        "Each turn presents new challenges and mysteries. The air becomes thick with anticipation.")
    
    time.sleep(2)
    
    print("\nAs you journey deeper, you encounter two distinct paths ahead.")
    
    user_choice_tunnel = input("1. Follow the Mysterious Symbols\n"
                            "2. Retreat and Regroup\n"
                            ">>> ").lower()
    
    if user_choice_tunnel == '1':
        follow_mysterious_symbols()
        print('')
        
    elif user_choice_tunnel == '2':
        print('')
        retreat_and_regroup()
        
        print('')
        search_for_high_ground()
    else:
        print("Invalid choice. The adventure awaits, make a valid selection.")
        
'''
    Function to the user explore the high ground
'''
def search_for_high_ground():
    print("\nOpting for the high ground, you lead your group to a steep incline within the cave.\n"
        "Climbing higher, you find a hidden chamber with a narrow opening leading to the surface.\n"
        "The ascent is perilous, but the promise of escape drives you and your friends forward.\n")
    
    user_choice_high_ground()


#################### PART 2 ####################

# Functions if the user choose the explore_dark_tunnels

'''
    This function leads to GAME OVER
'''
def follow_mysterious_symbols():
    print("\nIntrigued by the ancient symbols, you follow their trail deeper into the labyrinth of tunnels.\n"
        "Each symbol seems to lead you further into the heart of the cave, hinting at a hidden secret.\n"
        "The air grows colder as you press onward, anticipation building with each step.")
    
    time.sleep(5)
            
    print("\nSuddenly, the tunnel ahead narrows, and you find yourself trapped in a dead-end.\n"
        "Desperate attempts to backtrack are met with frustration as the passages shift and twist,\n"
        "leaving you lost in the maze of darkness.")

    time.sleep(2)
    
    print("\nAs hope begins to fade, you realize too late the true nature of the symbols.\n"
        "They were not guides but warnings, marking the path to your demise.")
    
    time.sleep(2)

    print("\nYour journey ends here, lost forever in the depths of the cave. Game Over.")
    
    time.sleep(3)
    
    play_again()
    
'''
    This function leads to the new path of the game
'''
def retreat_and_regroup():
    print("Sensing the increasing danger, you decide to retreat from the dark tunnels and regroup with your friends.\n"
        "Backtracking your steps, you return to the crossroads, where safety lies in familiarity.\n"
        "Though the path ahead remains uncertain, you know you must face the challenges together.")
    
    time.sleep(2)
    
    print("\nAs you reunite with your friends, you find renewed determination in their eyes.\n"
        "Together, you stand ready to face whatever challenges lie ahead,\n"
        "knowing that your bond and resilience will see you through.")

    time.sleep(2)

    print("\nWith newfound resolve, you return to the crossroads, ready to continue your journey.\n"
        "The path awaits, and the adventure continues.")
    
    time.sleep(2)
    
    print("\nYour collective experiences and shared strength have prepared you for the trials ahead.\n"
        "With unity as your shield, you embark once more into the depths of the cave,\n"
        "ready to confront whatever mysteries await.")


#################### PART 3 ####################
'''
    Functions if the user choose the search_for_high_ground  -- WIN THE GAME --
'''
def climb_steep_incline():
    print("\nOpting to climb the steep incline, you and your friends begin the arduous ascent.\n"
        "Each foothold is precarious, but the determination to escape fuels your climb.\n"
        "With every passing moment, you draw closer to the surface, freedom within reach.")

    time.sleep(2)

    print("\nAs you reach the surface, a wave of relief washes over you.\n"
        "You emerge from the cave, victorious, and bask in the warmth of the sunlight.\n"
        "Congratulations! You have successfully escaped the cave. You win the game!")
    
    play_again()

'''
    Function to investigate the hidden chamber  -- GAME OVER --
'''
def investigate_hidden_chamber():
    print("\nIntrigued by the hidden chamber, you cautiously enter, your senses heightened.\n"
        "The chamber is adorned with ancient artifacts, hinting at a forgotten civilization.\n"
        "Though the allure of discovery beckons, the urgency to escape remains.")

    time.sleep(6)

    print("\nSuddenly, the chamber begins to shake violently as ancient traps are triggered.\n"
        "The ceiling collapses, sealing your fate within the depths of the cave.\n"
        "Your journey ends here. Game Over.\n")
    
'''
    This IF is to start the game or exit.
    If the user press Y, the game will start 
    and the user will play to the end.
    If the user press N, the game will stop
'''
while True:
    continue_exit = input("Are you ready to dive into the unknown?\n"
                        "Press Y to continue or N to exit\n"
                        ">>> ")
    
    if continue_exit == "y":
        print("\nYour journey begins...")
        
        time.sleep(3)
        
        intro()
        
        break
    elif continue_exit == "n":
        print("Thank you for considering 'Escape from the cave'. Hope to see you soon.")
        break
    else:
        print("Invalid input. Please press Y or N.")