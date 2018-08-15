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
    

    c "aaaaaa"

    s "aaaaaaaaaaa"
    
    a "Aaaaaaaaaaaaaaaaaaaaa"

    # This ends the game

label discovery:
    
    show alex happy
    
    "It makes no sense!!!"
    "I don't get it!!"
    "I've known Sam for so long, but yet..."
    "How come I feel this way??"
    ""
    return
