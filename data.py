from interactions import *
import json

currentlocation = "entrance"

inventory = []

game_over = False

rooms = {
    "entrance": {
        "north" : "hallway",
        "item" : ["torch"],
        "interactable" : [],
        "locked doors" : []
    },
    "hallway" : {
        "south" : "entrance",
        "east" : "graves",
        "west" : "chamber",
        "item" : [],
        "interactable" : [],
        "locked doors" : "west"
    },
    "graves" : {
        "west" : "hallway",
        "item" : ["shovel"],
        "interactable" : ["grave"],
        "locked doors" : ""
    },
    "chamber" : {
        "south" : "hallway",
        "north" : "treasure",
        "item" : [],
        "interactable" : ["skeleton", "chair", "jar", "painting"],
        "locked doors" : "north"
    },
    "treasure" : {
        "west" : "exit",
        "south" : "chamber",
        "item" : ["chest", "weapons", "diamond",],
        "interactable" : [],
        "locked doors" : ""
    },
     "exit" : {
        "east" : "treasure",
        "item" : [],
        "interactable" : [],
        "locked doors" : ""
    }
}

def save_data():
    full_data = {
    "location": currentlocation,
    "inventory": inventory,
    "rooms": rooms
    }

    data_string = json.dumps(full_data, indent=4)

    f = open("savefile.json", "w")
    f.write(data_string)

    f.close()

def load_data():

    try:
        f = open("savefile.json", "r")

    except:
        print("No save file found!")
        return
    
    full_data = json.load(f)
    
    global currentlocation
    currentlocation = full_data["location"]
    global inventory
    inventory = full_data["inventory"]
    global rooms
    rooms = full_data["rooms"]

    f.close()