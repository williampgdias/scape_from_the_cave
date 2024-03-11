import time

# 1. About the game
print("Welcome to the SCAPE FROM THE CAVE game!")

time.sleep(2)

print("This is a RPG game and you have to choose options to run the game. "
    "The option that you choose, will create a different way to play the game.")

continue_exit = input("Do you wish to continue:\n Press Y or N: ").lower()

"""
    Function to tell the history about the game
"""
def about_history():
    print("You decide to go on camp in the forest with your friends.\n " 
        "When you get there, a big storm starts and you can't go back, because due "
        "to the storm, there was a landslide on the hill and the road is closed.")
    
    time.sleep(3)
    
    print("While you sleep, the floor gives way and you fall into a cave. "
        "Everyone is very hurt, and needs to find a way out.")
    
    time.sleep(3)
    
    print("Your friends trust you a lot and everyone decided that you are in charge, "
        "because you have more experience in this kind of adventure.")


# Conditional to start the game or not.
if continue_exit == "y":
    print("Uhuul!! Let's see if you can save everyone!")
    time.sleep(3)
    about_history()
else:
    print("Bye bye! Hope to see you later!")


# 2. Tell the history about the game

# 3. The user choose his name

# 4. 