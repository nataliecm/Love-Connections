# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg livingroom = "bg_livingroom.jpg"
image charlie normal = "charlie_normal.png"
image charlie shock = "charlie_shock.png"
image charlie grin = "charlie_grin.png"

define a = Character("Alex")
define c = Character("Charlie")
define s = Character("Sam")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it
    scene bg livingroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alex happy:
        xalign 0.0
        yalign 1.0
    show charlie normal:
        xzoom 0.35 yzoom 0.35
        xalign 1.0
        yalign 1.0

    # These display lines of dialogue.
    # might take away narration and just show the actions in the game if possible if not leave narration
    " WARNING: BEFORE YOU PROCEED THIS STORY IS REALLY DRAMATIC AND WAS NOT INTENDED TO OFFEND ANYONE. PLEASE DON'T SUE US"
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
    "Why am I feeling this way? I need to leave but NOW - Alex"
    a "Sorry but I just remebered that I need something important to do. I guess I'll see you tommorow Charlie"
    c "It's fine Alex. Text you later"
    s "Bye Alex"
    "alex ran home and went to his bedroom"
    scene bg bedroom
    
    
    
    
label stay:
    scene bg livingroom
    show alex calm
    a "Must be the wind"
    "SLAM"
    show alex scared
    a "What was that?"
    a "Charlie is that you. This isn't funny"
    show sam upset 
    s "It's not charlie. WOW how could you not remember me"
    s" You know Charlie doesn't live here by herself"
    a "Oh.H...HI sam."
    "Alex heart started beating fast as he turned to look at sam"
    s "Whatever"
    "Sam leaves irritated"
    hide sam
    # alex thought
    "What's happening? Why am I feeling this way? -Alex"
    show charlie
    c "Sorry for taking long"
    a "No problem. So what do you want to do now?"
    c "Play video games? oh wait i forgot to tell you that my brother's home but he won't be bothering us"
    show sam serious
    s "I think he knows that already"
    "sam and alex make eye contact"
    "Alex heart starts beating faster"
    # Alex thought
    "What's wrong with me? - Alex"
    a "Sorry but I just remebered that I need something important to do. I guess I'll see you tommorow Charlie"
    c "It's fine Alex. Text you later"
    s "Bye Alex"
    "alex ran home and went to his bedroom"
    scene bg bedroom
    

label discovery:
    
    show alex worried
    
    a "It makes no sense!!!"
    a "I don't get it!!"
    a "I've known Sam for so long, but yet..."
    a "How come I feel this way??"
    a "Is it possible that I'm...NO NO no that can't be but its not impossible"
    
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
    a "That way, I would have someone to help me figure out whats wrong."
    a "It would also give me a chance figure out who I really am!"
    "alex grabbed his phone"
    a "hello Charlie, I..I need your help. I'm lost"
    c "How can you be lost don't you remember where you live? Tell me the street.."
    a "No that's not what I meant. I'M CONFUSED WITH MY FEELING"
    c "uh.ok. But calm down and what do you mean your feelings"
    a "Sorry about that. But anyways today I saw this guy and when our eyes met my heart started beating fast. i don't know what's wrong"
    c "..."
    a "hello?"
    c "um. Do you possibly have a thing for guys. i thought you liked girls?"
    a " I don't know. I never felt this way before for anyone"
    c "i'm sorry charlie but i need to go"
    a "Wait..."
    "Charlie hung up"
    scene bg living room 
    c "What should i do? i never had a friend whose gay"
    c "what will others think"
    c "I don't want them to think that i could be lesbian for having a gay friend"
    c "But Alex needs my help and he's my best friend"
   
   menu:
        a "What should I do?"

        "Try to help Alex and stay friends":
            jump help
        "Stop being friends with Alex":
            jump ignore him
        
 label help :
    c "I can't leave alex all alone. I need to be by his side"
    c "But i don't know how to help i will just search up ways to help him"
    "charlie came upon a website called love Connections"
    "Parental Guide: Advice from other parents , I think my child is ___, Forums to help parents"
    c "I think I'll read the advice from other parents . even though i'm not his parent it should be helpful advice"
    "Charlie finished reading the article and picks up her phone and dials a phone number"
    c "Alex. I'm sorry for not letting you finish earlier and not listening to you. i know it hard for you right now but you can trust me and be by your side"
    "Wow. That article affected me alot. haha starting to talk like a grown up - Charlie"
    a "Thank You. i still not sure if i'm gay or or not"
    c "I was going to say to follow you heart but it seems your heart and brain are debating"
    c "there's nothing wrong with you if you like guys. It won't change who you are"
    c "And based on what you have told me it seem like you like like this boy. Don't hide those feelings and don't be afraid to be you. i will always support you"
    a "Thank you charlie i knew you were the right person to tell"
     # need to write smething that connects to end
    
 
 
 
 label ignore him :
    scene bg bedroom
    show alex sad/crying 
    a "What should i do now she just hung up on me"
    scene bg livingroom
    c "Im sorry alex but i was taught that that's wrong. Everything would have been good if you said you had feeling for a girl not guy"
    "Next morning"
    scene bg school
    show alex happy
    "i see charlie putting her things in her locker - alex"
    a "HEY charlie"
    a "i need to talk  to you"
    c "oh. It's you. See I don't have time to listen to you. Also i don't think this friendhip is going to last so we should make new friends and also pretend you don't know me if you see me in the hallways" 
    "Alex eyes became watery"
    "Does she hate me for having feelings for a guy -Alex"
    "Was i to harsh on him? he's probably alone. but how do I understand him?
    "Afternoon"
    "charlie was browsing through the internet"
    c "Love Connection?"
    c "Is this a dating site? i'm going to chec it out"
    c "what closet doors closed while loading. what's this"
    "charlie clicks on the closet doors"
    c "A time to open the closet doors? This isn't for me but it may help me understand alex"
    c "let's check the parential guide"
     "Parental Guide: Advice from other parents , I think my child is ___, Forums to help parents"
    c "I think I'll read the advice from other parents . even though i'm not his parent it should be helpful advice"
    "Charlie finished reading the article and picks up her phone and dials a phone number"
    c "Alex. I'm sorry for ignoring you. i should have listen to you"
    a "Thank You for changing your mind. But i have something to say I'm homosexual and i like males not females"
    c "I learned that there's nothing wrong with being homosexual because at the end of it all your still the same alex, my best friend for ever."
    c "hope you forgive me and for not being able to understand you and be by you side."
    # need to write smething that connects to end
    

label secret:
    a "I don't quite understand these feelings yet."
    a "I should keep it a scret until it starts to make sense"
    a "What happens if they think my feeling aren't normal. Yep. keeping it a secret is for the best"
    "next morning"
    scene bg school
    show charlie happy 
     c "Hello alex"
    show alex worried
    a "H...hi"
    c "whats wrong? you seem nervous"
    a "It's nothing. lets go"
    # i don't know what else to write
    
    
  
    
label ignore it :
    a "These feelings just happened today, probably tommorow they will be gone"
    a "Feelings come and go"
    "Next day"
    a "Why can't do these feelings grow stronger when i think of him"
    a "A guy liking a guy is wrong"
    a " why am i not normal"
    # i don't know what else to write
    
