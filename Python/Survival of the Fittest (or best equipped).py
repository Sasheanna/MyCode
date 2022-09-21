
import random
import time
import sys

print("Welcome to 'Survival of the Fittest (or the best equipped)'.  Here, you will be given a situation, and you must answer each question that follows about who you are,")
print("who is with you, and so on.  To make the game more fun, try and include both luxurious and useless items.  At the end, an item will be picked randomly")
print("from each category, making a story and giving you your items.  It's also more fun to play with multiple people.  Enjoy!")
print("")


def game():
    # Set up, people is a list
    people = []
    goOn = '0'
    condition = ("Hela (the goddess of death) has come to Earth", "Dr. Octopus has released Devil's Breath (a bio weapon), the Sinister Six are loose, and escaped criminals are taking over entire blocks.", "Dormammu is taking over Earth through the Dark Dimension.", "A dragon swoops in and attacks Earth, destroying everything in it's path.", "The Capitol is bombing your district.", "A McDonald's has opened near you.", "Thanos has all the infinity stones, and has killed half the population.", "You're on a cart with rebel Stormcloaks, headed to certain death.", "Voldemort and his Death Eaters have taken over the Ministry of magic.", "Alien ('buggers') are heading for Earth.", "Dementors are invading Hogwarts (School of Witchcraft and Wizardry).", "Orcs are carrying away *cough hack hack* two of your...hobbit friends.", "You are trapped in a hidden cellar, while bandits have taken over your house (they do not know you're there).", "There's a storm brewing, Orpheus is working on a song, and Eurydice is starving.", "Adorable but incredily dangerous (and intelligent) bunnies are taking over the world.", "You wake up and find yourself in the woods...where are you? There's no civilization in sight.", "The Ruin has destroyed Earth, and you are orbiting a strange planet in a destroyed ship.", "Monsters from space are taking over New York City.", "You wake up and find a strange...diamond imbedded in your left forearm.  Strange.  Wait, is that a DINOSAUR coming towards you?", "You are fighting for the Varden (good guys in Eragon), when you see that the enemy has a dragon on it's side.  Oh boy.", "You are in the woods with your spirit animal.  You got lost a LONG time ago.", "You find yourself atop a mountain.  How'd you get here?  Doesn't matter--what's more important is how you're going to survive.", "You're on a deserted island, and the ocean stretches out before you infinitely...", "You wake up and find yourself in a desert, just as the sun is about to rise.", "You're at the Cornucopia, surrounded by allies and enemies alike.")


    goOn = '0'

    def invalid():

        if goOn != '0' or goOn != '1':  # HERE
            print("That is an invalid answer, please try again.")
            #goOn = '0'

    def rollDie():
        print(random.sample(condition,1))

        reroll = input("Reroll? ")

        if reroll == "yes":
            rollDie()

        else:
            pass

    rollDie()

    # weather conditions
    weather = ("It is pouring buckets of rain.", "The sun is shining brightly, and there's not a cloud in sight.", "Fog is thick in the air, and it's cloudy.", "It's lightly sprinkling", "It's lightly snowing.", "It JUST rained, but right now there's a rainbow in the sky, and it's very pretty out.", "It's blisteringly hot out, and the sun is shining brightly.", "The wind is howling fiercely.", "Snow is falling quick and thick.", "It is currently hailing chunks the size of golfballs.", "It's hailing ice as big as your head at the smallest.", "It's really dry out, with not a cloud of rain in the sky.", "It's raining, with lightning flashing and thunder pounding all around you.", "Is that...a tornado headed your way?")

    print("The weather conditions are:", random.sample(weather,1))

    

    # This while loop causes these questions to be asked forever, or until the user types in any number other than zero
    while goOn == '0':
        people.append(input("Who are the characters? "))
        goOn = input("More?  Type the number zero.  If not, type '1': ")

        invalid()

    # This resets everything for the next 'while' loop
    shelters = []
    goOn = '0'

    # shelter
    while goOn == '0':
        shelters.append(input("What shelter options are there? "))
        goOn = input("... ")

        #invalid()

    items = []
    goOn = '0'

    # items
    while goOn == '0':
        items.append(input("What items do you have?  (there must be AT LEAST three) "))
        goOn = input("... ")

        #invalid()

    # apparel

    apparel = []
    goOn = '0'

    while goOn == '0':
        apparel.append(input("What apparel (in addition to what your character is wearing) is available (you must have AT LEAST three)? "))
        goOn = input("... ")

        #invalid()

    food = []
    goOn = '0'

    # food
    while goOn == '0':
        food.append(input("What food is available? "))
        goOn = input("... ")

        #invalid()


    # things to drink
    drink = []
    drink.append("There is no source of anything to drink")
    goOn = '0'
    
    while goOn == '0':
        drink.append(input("Is there anything to drink (or a resource, like a pond)? "))
        goOn= input("... ")

        #invalid()
    

    assistance = []
    assistance.append("No one.  You are all alone.")
    goOn = "0"

    # nearby people who can help
    while goOn == "0":
        assistance.append(input("Who is nearby to help? "))
        goOn = input("... ")

        #invalid()

    # This prints everything out randomly
    print("You are", random.sample(people,1))
    print("Have", random.sample(shelters,1), "as shelter")
    print("And have:", random.sample(items, 2))
    print("Apparel (in addition to the clothes you already have) is:", random.sample(apparel,2))
    print("Available food is:", random.sample(food,1))
    print("Available source of something to drink is:", random.sample(drink,1))
    print("Nearby people who might be able to help are:", random.sample(assistance,1))
    print("Chances of survival: ", end = '')
    print(random.randint(-1,101), end = '')
    print("%")

    print("")
    again = input("Play again? ")

    if again == "yes":

        print("")
        game()

    else:
    
        print("Ok.  Shutting down...")
        time.sleep(1)
        print("...")
        time.sleep(3)
        sys.exit

game()

    
# Things to add:
# The ability to restart the game.  DONE
# A "start-up screen", a welcome.  DONE
# Another thing to do would be to add a "things to drink" category. DONE
# Add "apparrel" category  DONE
# add "weather conditions" category DONE (more or less)
# Add safety feature that if input is not 1 or 0 it gives you a second chance
