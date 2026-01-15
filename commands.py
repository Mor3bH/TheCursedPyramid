import data as d
from print_text import *
import sys
from dialogue import *
from interactions import interactions
import random

def handle_go(direction):
    if direction in d.rooms[d.currentlocation]:

        if "torch" not in d.inventory:
            print_notif("It's too dark to enter. You need to take the torch first.")
            return

        if d.rooms[d.currentlocation]["locked doors"] != direction:
            d.currentlocation = d.rooms[d.currentlocation][direction]
            print_dialogue("You moved to " + d.currentlocation)
        else:
            print_notif("The door is locked!")
    else:
        print_notif("There are no doors in that direction.")

def handle_take(targetItem):
        if targetItem in d.rooms[d.currentlocation]["item"]:
            print_dialogue("Picked up " + targetItem)
            d.inventory.append(targetItem)
            d.rooms[d.currentlocation]["item"].remove(targetItem)

            if targetItem == "diamond":
                print_notif("EARTHQUAKE!!!")
                print_notif("Scout: Oh NO! We shouldn't have taken the diamond!")
                print_notif("The pyramid collapses...")
                d.game_over = True
        else:
            print_notif("There is no " + targetItem)

def handle_use(targetItem):
    if targetItem in d.inventory:
        itemUsed = False
        for interactable in d.rooms[d.currentlocation]["interactable"]:
            if (targetItem, interactable) in interactions:
                print_dialogue(interactions[(targetItem, interactable)])
                itemUsed = True

        if (targetItem == "key"and d.rooms[d.currentlocation]["locked doors"] != "" 
            and not (d.currentlocation == "chamber")):
                d.rooms[d.currentlocation]["locked doors"] = ""
                print_notif("Unlocked!")
                itemUsed = True
                return
        
        if (targetItem, interactable) == ("shovel", "grave"):
            if "mummy" not in d.rooms[d.currentlocation]["item"]:
                d.rooms[d.currentlocation]["item"].append("mummy")
                return

        if not itemUsed:
            print_dialogue("You can do nothing with this here.")
    else:
        print_dialogue("You don't have this item.")     

def handle_dialogue(dialogue):
    current_segment = dialogue[d.currentlocation + "_talk"]

    while True:
        for line in current_segment["lines"]:
            print_dialogue(line)

        if not current_segment["options"]:
            return

        for choice in current_segment["options"]:
            print(choice, end="   ")
        print()

        dialogue_choice = input(">").strip().lower()

     
        if d.currentlocation == "chamber" and dialogue_choice == "chair":
            if d.rooms["chamber"]["locked doors"] != "":
                d.rooms["chamber"]["locked doors"] = ""
                print_notif("A hidden mechanism clicks... the door is now unlocked!")
            return   

        if dialogue_choice == "translate":
            show_scripture()
            answer = input("Type your translation:\n>").strip().upper()

            if answer == "DO NOT TOUCH THE DIAMOND":
                current_segment = dialogue["correct_translation"]
            else:
                current_segment = dialogue["wrong_translation"]
            continue

       
        if dialogue_choice not in current_segment["options"]:
            print_notif("Invalid choice.")
            continue

      
        return

def show_scripture():
    script = {
        "A": "@",
        "B": "8",
        "C": "<",
        "D": "}",
        "E": "3",
        "F": "7",
        "G": "6",
        "H": "#",
        "I": "!",
        "J": "?",
        "K": "|<",
        "L": "|_",
        "M": "^^",
        "N": "|V",
        "O": "0",
        "P": "|*",
        "Q": "0,",
        "R": "&",
        "S": "$",
        "T": "~",
        "U": "()",
        "V": "\\/",
        "W": "vv",
        "X": "*",
        "Y": ":;",
        "Z": "%"
    }

    print_instruction("Ancient Scripture:")
    for k, v in script.items():
        print_notif(f"{k} -> {v}")


def handle_combat(enemy_name):
    playerHealth = 100
    enemyHealth = 100

    print_dialogue(f"Combat started vs {enemy_name}!")



    while playerHealth > 0 and enemyHealth > 0:
        print_instruction("What do you want to do? (fight / heal )")
        choice = input(">").lower()

        if choice == "fight":
            dmg = random.randint(8, 18)
            enemyHealth -= dmg
            print_dialogue(f"You hit the {enemy_name} with your shovel for {dmg} damage!")
            print_notif(f"{enemy_name} health: {max(enemyHealth, 0)}")

        elif choice == "heal":
            heal = random.randint(8, 18)
            playerHealth = min(100, playerHealth + heal)
            print_dialogue(f"You healed {heal}.")
            print_notif(f"Your health: {playerHealth}")

        else:
            print_notif("Invalid choice.")
            continue

        if enemyHealth > 0:
            enemyDmg = random.randint(6, 16)
            playerHealth -= enemyDmg
            print_dialogue(f"The {enemy_name} hits you for {enemyDmg} damage!")
            print_notif(f"Your health: {max(playerHealth, 0)}")

    if playerHealth <= 0:
        print_notif("YOU DIED!")
        return "dead"

    print_dialogue(f"You defeated the {enemy_name}!")

    if enemy_name in d.rooms[d.currentlocation]["item"]:
        d.rooms[d.currentlocation]["item"].remove(enemy_name)
        d.rooms[d.currentlocation]["item"].append("key")

    return "won"

def handle_quit():
    print("Quitting the game...")
    d.save_data()
    sys.exit()