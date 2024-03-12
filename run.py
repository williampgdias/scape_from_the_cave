import time

# 1. About the game
print("Welcome to the captivating adventure of 'Escape From the Cave'!")

time.sleep(2)

print("Embark on an epic RPG journey where your choices shape the course of the game.\n"
    "Each decision you make leads to a unique path, ensuring a thrilling and unpredictable experience.")

continue_exit = input("Are you ready to dive into the unknown?\n"
                    "Press Y to continue or N to exit: ").lower()


#################### PART 1 ####################

'''
    Function to tell the history about the game
'''
def about_history():
    print("You embarked on a camping trip in the heart of the forest with your closest friends.\n"
        "As the sun set, an unexpected storm unleashed its fury, triggering a landslide on the hill.\n"
        "The road back home is now blocked by fallen debris.")

    time.sleep(6)

    print("During the restless night, disaster strikes when the ground beneath your campsite collapses,\n"
        "plunging everyone into a mysterious cave. In the dim light, you realize everyone is injured\n"
        "and finding an escape becomes the top priority.")

    time.sleep(6)

    print("In the face of uncertainty, your friends turn to you, placing their trust in your leadership.\n"
        "With your seasoned experience in adventurous pursuits, you find yourself at the forefront\n"
        "of this unexpected challenge, taking charge to lead your friends to safety.")

'''
    Option that the user has to choose to keep playing the game.
'''
def explore_dark_tunnels():
    print("You decide to delve into the dark tunnels, guided only by the faint glow of your flashlight.\n"
        "As you navigate through the winding passages, you discover ancient markings on the cave walls.\n"
        "Each turn presents new challenges and mysteries. The air becomes thick with anticipation.")

'''

'''
def search_for_high_ground():
    print("Opting for the high ground, you lead your group to a steep incline within the cave.\n"
        "Climbing higher, you find a hidden chamber with a narrow opening leading to the surface.\n"
        "The ascent is perilous, but the promise of escape drives you and your friends forward.")


#################### PART 2 ####################

'''
    Functions if the user choose the explore_dark_tunnels
'''
def follow_mysterious_symbols():
    print("Intrigued by the ancient symbols, you follow their trail deeper into the labyrinth of tunnels.\n"
        "Each symbol seems to lead you further into the heart of the cave, hinting at a hidden secret.\n"
        "The air grows colder as you press onward, anticipation building with each step.")
    
def retreat_and_regroup():
    print("Sensing the increasing danger, you decide to retreat from the dark tunnels and regroup with your friends.\n"
        "Backtracking your steps, you return to the crossroads, where safety lies in familiarity.\n"
        "Though the path ahead remains uncertain, you know you must face the challenges together.")

'''
Functions if the user choose the search_for_high_ground
'''
def climb_steep_incline():
    print("Opting to climb the steep incline, you and your friends begin the arduous ascent.\n"
        "Each foothold is precarious, but the determination to escape fuels your climb.\n"
        "With every passing moment, you draw closer to the surface, freedom within reach.")

def investigate_hidden_chamber():
    print("Intrigued by the hidden chamber, you cautiously enter, your senses heightened.\n"
        "The chamber is adorned with ancient artifacts, hinting at a forgotten civilization.\n"
        "Though the allure of discovery beckons, the urgency to escape remains.")

'''
    This IF is to start the game or exit.
    If the user press Y, the game will start 
    and the user will play to the end.
    If the user press N, the game will stop
'''
if continue_exit == "y":
    print("Your journey begins...")
    time.sleep(3)
    about_history()
    
    print("\nYou find yourself standing at a crossroads within the cave.\n"
        "Two paths stretch out before you. What will you choose?")
    
    player_choose = input("Press 1 to Explore the Dark Tunnels\n"
                        "Press 2 to Search for High Ground\n"
                        ">>> ")
    
    if player_choose == "1":
        explore_dark_tunnels()
        
        time.sleep(2)
        
        print('\nAs you journey deeper, you encounter two distinct paths ahead.')
        
        user_choice_tunnel = input("1. Follow the Mysterious Symbols\n"
                                "2. Retreat and Regroup\n"
                                ">>> ")
        if player_choose == '1':
            print('')
            time.sleep(1.5)
            follow_mysterious_symbols()
        elif player_choose == '2':
            print('')
            retreat_and_regroup()
        else:
            print("Invalid choice. The adventure awaits, make a valid selection.")
            
    elif player_choose == "2":
        search_for_high_ground()
        
        time.sleep(2)
        
        print('\nAs you reach the chamber, two choices lie before you.')
        
        user_choice_high_ground = input("1. Climb the Step Incline\n"
                                    "2. Investigate the Hidden Chamber\n"
                                    ">>> ")
        
        if user_choice_high_ground == '1':
            climb_steep_incline()
        else:
            investigate_hidden_chamber()
    else:
        print("Invalid choice. The adventure awaits, make a valid selection.")
    
    
elif continue_exit == "n":
    print("Thank you for considering 'Escape from the cave'. Hope to see you soon.")
else:
    print("Invalid input. Please restart the game and choose between Y or N.")