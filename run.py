import time

# 1. About the game
import time

print("Welcome to the captivating adventure of 'Escape From the Cave'!")

time.sleep(2)

print("Embark on an epic RPG journey where your choices shape the course of the game.\n"
    "Each decision you make leads to a unique path, ensuring a thrilling and unpredictable experience.")

continue_exit = input("Are you ready to dive into the unknown?\n"
                    "Press Y to continue or N to exit: ").lower()


"""
    Function to tell the history about the game
"""
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


# Conditional to start the game or not.
if continue_exit == "y":
    print("Uhuul!! Let's see if you can save everyone!")
    time.sleep(5)
    about_history()
else:
    print("Bye bye! Hope to see you soon!")


# 2. Tell the history about the game

# 3. The user choose his name

# 4. 