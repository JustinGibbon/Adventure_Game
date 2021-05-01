# Name: Justin Gibbon
# Date: 2020/02/26

import random
import time

monsters = ["Basilisk", "Cerberus", "Goblin",
            "Troll", "ex girlfriend", "Giant Bread Monster"]
weapons = ["dagger", "sword", "battle-Axe", "bow and quiver", "qauterstaff"]
satchel = ["sunglasses", "health-potion", "goose"]
weather = ["sunny", "cloudy", "rainy"]


starting_weapon = (random.choice(weapons))


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            break
        elif option2 == response:
            break
        elif option3 == response:
            break
        else:
            print_pause("Please select a valid option")
    return response


def intro_message():
    print_pause("Hello brave adventurer!")
    name = input("What is your name?\n")
    print_pause("OK then "+name+" let's get this adventure started!!")
    print_pause("")
    print_pause("Sunlight is shining through the crack in your door"
                "..its morning,time to wake up")
    print_pause("Ever so slowly you climb out of you bed,winching"
                " in pain, youre getting old you think to yourself")
    print_pause("While standing outside, on your porch you look "
                "over the valley and see today is"
                " a " + random.choice(weather) + " day")
    print_pause("Deciding it's stil early you head back inside"
                " to brew a pot of coffe and get dressed")
    print_pause("After getting dressed you head outside "
                "to drink your coffe, on your way "
                "you notice your " + starting_weapon +
                " and decide to strap it on, you never know"
                " when you might need it")
    print_pause("Looking over the valley you see ypu realise "
                "you have three ways to spend the day")
    print_pause("1:a Ominous looking cave with a musky smell")
    print_pause("2:a pleasent looking meadow filled with"
                " fruit trees and a clean mountain spring.")
    print_pause("3:or are you going to be a lazy troglodite"
                " and go back into your home.")


def choose_path(rand_monster):
    response = valid_input("What wil the choice be?"
                           "\nPlease select 1:The cave"
                           ",2:The meadow or 3:stay at"
                           " home\n", "1", "2", "3")
    if response == "1":
        cave(rand_monster)
    elif response == "2":
        meadow(rand_monster)
    elif response == "3":
        home(rand_monster)
    else:
        print_pause("Please choose a valid path")
        choose_path(rand_monster)


def cave(rand_monster):
    print_pause("\nWalking into the ominous cave"
                " you see a blurry shape in the distance")
    print_pause("Ever so slowly you approach the"
                " shape...trying not te be noticed")
    print_pause("Something crunches underneath you"
                " foot...you look down and see the crushed remains of a skull")
    print_pause("The blurry shape turns around and"
                " pounces... it's a " + rand_monster)
    print_pause("Escape is impossible, as you are of"
                " low intelligence and havew gotten yourself"
                " lost in this cave...thus you must fight on")
    print_pause("You pull out your " + starting_weapon)
    if "dagger" in starting_weapon:
        print_pause("You can do nothing against this"
                    " foul beast with that puny weapon")
        print_pause("Through sheer luck you manage to stab the beast "
                    "in it's eye, unfortunatly that only"
                    " angers the beast further..."
                    "and thus our brave adventurer meets his untimely fate.")
        play_again()
    else:
        print_pause("You slay the beast and exit the cave")
        print_pause("As you walk out in to the daylight,"
                    " the smell of flowers waft over you")
        print_pause("You go lay down in the field and decide that"
                    " this is where you will be spending the rest of the day.")
        print_pause("Softly you say to yourself: 'Today was a good day.'")
        play_again()


def meadow(rand_monster):
    print_pause("Aaahh so you chose the pleasent"
                " looking meadow...good choice."
                "or so you'd think.")
    print_pause("You're feeling a bit sleepy"
                " from the hike and decide to"
                " go take a nap under a nearby tree")
    print_pause("a Noise a few feet away from you wakes you voilently")
    print_pause("To your dismay it's a " + rand_monster)
    print_pause("You can either try and run away or stand and face this beast")
    response = valid_input("Will you:\n1:Fight\n2:Run\n"
                           "Please choose either 1 or 2\n", "1", "2", "1")
    if response == "1":
        print_pause("You step up and face the beast")
        if "dagger" in starting_weapon:
            print_pause("The beast kills you and"
                        " uses your boddy as flavouring in its soup")
            play_again()
        else:
            print_pause("You slay the beast and dance on its corpse.")
            print_pause("Today was a good day")
            play_again()
    if response == "2":
        print_pause("You run away like a coward and"
                    " now have another choice to make")
        print_pause("Unfortunatley the monster now"
                    " has you scent and will pursue"
                    " you anywhere you go in the wild")
        choose_path(rand_monster)


def home(rand_monster):
    print_pause("So..you decided to stay at home.")
    print_pause("A few hours have passed and you "
                "reconsider if you want to actually do something today")
    response = valid_input("Would you like to go out?\n"
                           "Type either 'yes' or no\n", "yes", "no", "y")
    if "yes" in response:
        choose_path(rand_monster)
    else:
        print_pause("So you decided to take a day off")
        print_pause("No shame in that, you just "
                    "spend your day in the house and relax")
        play_again()


def play_again():
    response = valid_input("Would you like to play"
                           " again?\nType either yes"
                           " or no\n", "yes", "no", "yes")
    if "yes" in response:
        play_game()
    if "no" in response:
        print_pause("Ok bye and thanks for playing")


def play_game():
    rand_monster = random.choice(monsters)
    intro_message()
    choose_path(rand_monster)


play_game()
