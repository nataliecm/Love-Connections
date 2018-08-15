# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alex")
define c = Character("Charlie")
define s = Character("Sam")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg livingroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alex happy
    show charlie happy
    show sam happy

    # These display lines of dialogue.
    # might take away narration and just show the actions in the game if possible if not leave narration

    "Alex and Charlie were hanging out at her house. Charlie suddenly got a phone call"
    c "I'll be right back. i need to take this fast."
    a "sure no problem. Just don't take long."
    "CRAAAASSHHHHH"
    
    menu :
        "Should I investigate the sound?":
            jump investigate
        "Wait for Charlie to come back":
            jump stay
        
label investigate:
    scene bg hallway
    show alex worried 
    "Alex goes to where the sound is coming from"
    scene bg roomdoor
    a "Whose room is this?"
    "Alex knocks on the door"
    "..."
    "Silence"
    a "Whose there? Open up"
    "No answer. Alex decided to open up the room door anyways"
    
    scene bg room
    show alex scared 
    s "BOO!!"
    a "AAAAAaahhhhhh"
    "Alex turned around quickly only to see a tall slim figure in front of him dying in laughter"
    
    show sam laughing 
    s "HAHAHAHAH"
    s "You should have seen your face"
    show alex angry 
    a "Shut UP SAM"
    hide sam
    
    "Alex walked out of the room and back to the living room"
    scene bg livingroom
    "Alex heart was beating fast"
    "alex places a hand on his chest"
    a "Must be from the scare earlier"
    show charlie
    c "what scare?"
    a "Nothing"
    c "O...Okay. By the way i forgot to tell you that my brother's home but he won't be bothering us"
    show sam happy
    s "I think he knows that already"
    "sam and alex make eye contact"
    "Alex heart starts beating faster"
    # Alex thought
    "Why am I feeling this way? - Alex"

label discovery:
    
    show alex happy
    
    a "It makes no sense!!!"
    a "I don't get it!!"
    a "I've known Sam for so long, but yet..."
    a "How come I feel this way??"
    
    menu:
        a "What should I do?"

        "Tell someone":
            jump tell
        "Keep it a secret":
            jump secret
        "Ignore it":
            jump ignore

        
label tell:
    a "That's it!"
    a "I should probably let someone know about my feelings."
    a "That way, I would have someone to talk to when I need help."
    a "It would also give me a chance to be myself!"
label secret:
    a "I don't quite understand these feelings yet."
    a "I should keep it a scret until it starts to make sense"
    return
