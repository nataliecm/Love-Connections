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
    

    "Alex and Charlie were hanging out at her house. Charlie suddenly got a phone call"
    c "I'll be right back. i need to take this fast."
    a "sure no problem. Just don't take long."
    "Sound of something break"
    
    menu :
    "shuld i investigate the sound?":
        jump investigate
    "
    
    # This ends the game

label discovery:
    
    show alex happy
    
    a "It makes no sense!!!"
    a "I don't get it!!"
    a "I've known Sam for so long, but yet..."
    a "How come I feel this way??"
    menu:
    
    "What should I do?"
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
