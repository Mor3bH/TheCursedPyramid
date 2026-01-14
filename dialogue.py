d1 = {
    "entrance_talk": {
        "lines": [
            "Welcome to Cursed Pyramid!",
            "Scout: Hello, Traveler!",
            "Scout: I heard there is a valuable treasure..",
            "Scout: Would you like to join me in this adventure?"
        ],
        "options": ["yes", "no"]
    },

    "no": {
        "lines": [
            "Scout: Your loss.",
            "Scout: I guess I'll be moving alone."
        ],
        "options": []
    },

    "yes": {
        "lines": [
            "Scout: Here, take this scripture and put it in your inventory.",
            "Scout: We'll need light. There is a torch here — take it before we go inside.",
            "(Tip: type: take torch)"
        ],
        "options": []
        
    },
    "hallway_talk": {
        "lines": [
            "Walking the hallway..",
            "Scout: Oh my, these are old Egyptian symbols.",
            "Scout: Now it's time to use the scripture.",
            "Translate this:",
            "}0 |V0~ ~0()<# ~#3 }!^^0|V}"
        ],
        "options": ["translate"]
    },
    "graves_talk": {
        "lines": [
            "Scout: These graves feel cursed...",
            "Scout: If you dig, be ready to fight."
        ],
        "options": []
    },

    "chamber_talk": {
        "lines": [
            "Scout: This is the King's Chamber.",
            "Scout: The air feels heavy...",
            "Scout: Something here hides the path forward.",
            "Scout: What should we inspect?"
        ],
        "options": ["skeleton", "chair", "jar", "painting"]
    },

    "skeleton": {
        "lines": [
            "Scout: This skeleton wears royal ornaments...",
            "Scout: Look—scratch marks on the floor.",
            "Scout: Someone dragged something heavy toward the chair."
        ],
        "options": []
        
    },

    "jar": {
        "lines": [
            "Scout: Just dust and dried bones.",
            "Scout: Whatever was stored here is long gone."
        ],
        "options": []
       
    },

    "painting": {
        "lines": [
            "Scout: This painting shows servants bowing to the king.",
            "Scout: Wait… the king's eyes seem to follow us.",
            "Scout: I don’t like this."
        ],
        "options": []
       
    },

    "chair": {
        "lines": [
            "Scout: The throne feels loose...",
            "Scout: There’s a click!",
            "Scout: A hidden passage opens behind the chair."
        ],
        "options": []
       
    },


    "treasure_talk": {
        "lines": [
            "Scout: This is it... the treasure room.",
            "Scout: I can see some items here.",
            "Scout: Type 'take <item>' to take what you want.",
            "Scout: ...but be careful."
        ],
        "options": []
       
    },


    "chest": {
        "lines": [
            "Scout: You opened the chest and found gold!",
            "Scout: Good choice. Let's not push our luck."
        ],
        "options": []
        
    },

    "weapons": {
        "lines": [
            "Scout: You grabbed the ancient weapons.",
            "Scout: These might be useful..."
        ],
        "options": []
        
    },

    "bad_ending": {
        "lines": [
            "Scout: NO—DON'T TOUCH IT!",
            "EARTHQUAKE!!!",
            "The pyramid collapses...",
            "GAME OVER!"
        ],
        "options": []
        
    },

    "exit_talk": {
        "lines": [
            "Scout: The exit door is right there.",
            "Scout: If you have the key, we can leave."
        ],
        "options": []
    },

    "wrong_translation": {
        "lines": [
            "Wrong translation.",
            "Scout: Try again carefully."
        ],
        "options": ["translate"]
    },
    "correct_translation": {
        "lines": [
            "Scout: Hmm, I wonder what that means, but lets keep it in mind.",
            "Scout: The graves are to the east, and the King's Chamber is to the west.",
            "Scout: You decide where to go next."
        ],
        "options": []
        
    }
}