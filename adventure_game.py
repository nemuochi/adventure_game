import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field,\n"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a troll is somewhere around here,\n"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty\n"
                "(but not very effective) dagger.")


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower().strip()
        for option in options:
            if option in response:
                return response


# Things that happen to the player in the field
def field(item, tresures):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    options = ['1', '2']
    choice = valid_input("(Please enter 1 or 2.)\n", options)
    if choice == '1':  # proceed to the house
        house(item, tresures)
    else:           # proceed to the cave
        cave(item, tresures)


# Things that happen to the player in the house
def house(item, tresures):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens\n"
                "and out steps a troll.")
    print_pause("Eep! This is the troll's house.")
    print_pause("Troll attacks you!")
    if len(item) >= 1:
        print_pause("It makes you jump!")
    else:
        print_pause("You feel a bit under-prepared for this,\n"
                    "what with only having a tiny dagger.")
    options = ['1', '2']
    choice = valid_input("Would you like to (1) fight or "
                         "(2) run away?\n", options)
    if choice == '1':  # proceed to fight
        choice_to_fight(item, tresures)
    else:               # proceed to runaway
        choice_to_runaway(item, tresures)


# Things that happen to the player in the cave
def cave(item, tresures):
    if len(item) == 2:
        print_pause("You are getting used to this cave.")
        print_pause("You've been here before, and gotten all the good stuff.\n"
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field(item, tresures)
    elif len(item) == 1:
        print_pause("You know this cave.")
        print_pause("You've been here before but carefully look into it again.")
        print_pause("Hey, guess what you find this time, there's a magic " +
                    tresures[1] + ".")
        print_pause("You take the " + tresures[1] + " and leave the cave.")
        item.append(tresures[1])
        field(item, tresures)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye chatches a glint of metal behind a rock.")
        print_pause("You have found the magical " + tresures[0] + "!")
        print_pause("You discard your silly old dagger and take the \n" +
                    tresures[0] + " with you.")
        print_pause("You walk back out to the field.")
        item.append(tresures[0])
        field(item, tresures)


# In house, choose to fight.
def choice_to_fight(item, tresures):
    if len(item) == 2:  # with 2 items, You "win".
        print_pause("As the troll moves to attack, you draw "
                    "your new " + item[0] + " and " + item[1] + ".")
        print_pause("The " + item[0] + " and " + item[1] + " shine brightly "
                    "in your hands as you brace yourself for the attack.")
        print_pause("But the troll takes one look at your shiny new toys "
                    "and runs away!")
        print_pause("You have rid the town of the troll. You are victorious!"
                    "--YOU WIN--\n")
        play_again(item, tresures)
    elif len(item) == 1:  # with 1 item, you have to choose again: fight or run
        print_pause("As the troll moves to attack, you draw "
                    "your new " + item[0] + ".")
        print_pause("The " + item[0] + " shines brightly "
                    "in your hand as you brace yourself for the attack.")
        print_pause("The troll takes one look at your shiny new toy\n"
                    "intimitated a second, yet still moves towards you!")
        options = ['1', '2']
        choice2 = valid_input("Would you like to keep (1)fighting or"
                              "(2) running away?\n", options)
        # proceed to fight with a item, and chance to win is 50/50.
        if choice2 == '1':
            damaged_troll(item, tresures)
        else:  # proceed to runaway
            choice_to_runaway(item, tresures)
    else:  # with no item, you "lose".
        print_pause("You do your best...")
        print_pause("But your dagger is no match for the troll.")
        print_pause("You have been defeated!--GAME OVER--\n")
        play_again(item, tresures)


# Win or lose depending on the amount of damage to the troll.
def damaged_troll(item, tresures):
    damage = random.randint(0, 10)
    if damage <= 5:
        print_pause("You do your best...")
        print_pause("But your " + item[0] + " is no match "
                    "for the troll.")
        print_pause("You have been defeated! --GAME OVER--\n")
    else:
        print_pause("You are not sure how it works...")
        print_pause("Somehow, you damaged the troll badly, "
                    "the troll retreats.")
        print_pause("You have rid the town of the troll. You are "
                    "victorious! --YOU WIN--\n")
    play_again(item, tresures)


# In house, choose to run away
def choice_to_runaway(item, tresures):
    print_pause("You run back into the field. "
                "Luckily, you don't seem to have been followed.")
    field(item, tresures)


# Will you play again?
def play_again(item, tresures):
    options = ['y', 'n']
    choice = valid_input("Would you like to play again? (y/n)", options)
    if choice == 'y':   # Yes, play again
        print_pause("Excellent! Restarting the game ...\n")
        item.clear()  # Reset the item.
        tresures = random.sample(['sword', 'wand', 'longbow', 'ring', 'flute'],
                                 k=2)  # Reset the random choice of tresures
        intro()
        field(item, tresures)
    else:  # No, I quit
        print_pause("Thanks for playing! See you next time.")


def play_game():
    tresures = random.sample(
                ['sword', 'wand', 'longbow', 'ring', 'flute'], k=2)
    item = []
    intro()
    field(item, tresures)


play_game()
