# You can use this workspace to write and submit your adventure game project.
import time
import random


def print_sleep(prompt, sleep_time=0):
    print(prompt)
    time.sleep(sleep_time)


def valid_input(prompt, options):
    """Function to check if an input is valid.
    It receives a string prompt and list of string as options"""
    while True:
        response = input(prompt).lower()
        if response in options:
            return response


def play_again():
    third_choice = valid_input(
        "Would you like to play again? (y/n)", ["y", "n"])
    if third_choice == "y":
        print_sleep("Excellent! Restarting the game ...", 2)
        # Restart the game
    elif third_choice == "n":
        print_sleep("Thanks for playing! See you next time.", 2)
        # program ends
        exit(0)


def run_away():
    print_sleep("You run back into the field. Luckily, "
                "you don't seem to have been followed.\n", 2)
    # play_game


def fight(fight_texts):
    for text in fight_texts:
        print_sleep(text, 1)
    print_sleep("\n", 1)


def fight_choice(fight_texts):
    second_choice = valid_input(
        "Would you like to (1) fight or (2) run away?\n", ['1', '2'])
    if second_choice == '1':
        # fight
        fight(fight_texts)
        # play again?
        return True
    elif second_choice == '2':
        # run away
        run_away()
        return False


def knock_on_door(monster, weapon):
    is_fight = False
    print_sleep("You approach the door of the house.", 1)
    print_sleep(f"You are about to knock when the door" +
                f" opens and out steps a {monster}.", 1)
    print_sleep(f"Eep! This is the {monster}'s house!", 1)
    print_sleep(f"The {monster} attacks you!", 1)
    if weapon == "dagger":
        print_sleep("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.", 1)
        # fight
        is_fight = fight_choice([
                "You do your best...",
                f"but your dagger is no " + f"match for the {monster}.",
                "You have been defeated!"]
        )
    elif weapon == "sword":
        # fight
        is_fight = fight_choice([
                f"As the {monster} moves to attack," +
                "you unsheath your new sword.",
                "The Sword of Ogoroth shines " +
                "brightly in your hand as you " +
                "brace yourself for the attack.",
                "But the pirate takes one look at your " +
                "shiny new toy and runs away!",
                f"You have rid the town of the {monster}. " +
                "You are victorious!"]
        )
    return is_fight


def peer_in_cave(weapon):
    if weapon == 'dagger':
        print_sleep("You peer cautiously into the cave.", 1)
        print_sleep("It turns out to be only a very small cave.", 1)
        print_sleep("Your eye catches a glint of metal behind a rock.", 1)
        print_sleep("You have found the magical Sword of Ogoroth!", 1)
        print_sleep("You discard your silly old dagger and take the sword "
                    "with you.", 1)
        weapon = "sword"
    elif weapon == 'sword':
        print_sleep("You peer cautiously into the cave.", 1)
        print_sleep("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.", 1)
    print_sleep("You walk back out to the field.\n", 2)
    return weapon
    # Go back to choice 1


def intro(monster):
    print_sleep("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.", 2)
    print_sleep(f"Rumor has it that a {monster} is somewhere around here, "
                "and has been terrifying the nearby village.", 2)
    print_sleep("In front of you is a house.", 2)
    print_sleep("To your right is a dark cave.", 2)
    print_sleep("In your hand you hold your trusty "
                "(but not very effective) dagger.\n", 2)


def play_game(monster, weapon):
    while True:
        print_sleep("Enter 1 to knock on the door of the house.", 2)
        print_sleep("Enter 2 to peer into the cave.", 2)
        print_sleep("What would you like to do?", 2)
        first_choice = valid_input("(Please enter 1 or 2).\n", ['1', '2'])
        if first_choice == '1':
            # knock on the door
            is_fight = knock_on_door(monster, weapon)
            if is_fight:
                break
        elif first_choice == '2':
            # Player enters the cave
            weapon = peer_in_cave(weapon)


def adventure_game():
    village_monsters = ['dragon', 'wicked fairie', 'pirate', 'troll']
    weapon = 'dagger'
    while True:
        monster = random.choice(village_monsters)
        intro(monster)
        play_game(monster, weapon)
        play_again()


if __name__ == '__main__':
    adventure_game()
