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
    # Might take away narration and just show the actions in the game if possible if not leave narration
    "**WARNING: BEFORE YOU PROCEED THIS STORY IS REALLY DRAMATIC AND WAS NOT INTENDED TO OFFEND ANYONE. PLEASE DON'T SUE US!**"
    "**THIS WAS NOT INTENDED TO SOUND LIKE A FANFICTION, BUT WE CAN'T CONTROL HOW THINGS TURN OUT**"
    "It was a regular Saturday afternoon when Alex and Charlie were hanging out at her house."
    "Until suddenly..."
    "{i}Brrrrrrrriiiiiing{/i}"
    "{i}Brrrriing Brrrrrring{/i}"
    a "Awe..."
    a "Turn off your phone, we just got here. The call can't be {b}that{/b} important"
    c "Of course! I'm promised that we could hangout anyway."
    "..."
    "......"
    "........."
    "{i}Brrrrrring{/i}"
    a "Maybe if we ignore it, they'll give up."
    "..."
    "{b}BRRRRRRRRIIIIIIIINNNNNGGGG{/b}"
    c "I'll be right back. I need to take this fast."
    a "Sure, no problem. Just don't take long."
    "Alex was waiting around (being bored out of his mind if I must add) until suddenly..."
    "CRAAAASSHHHHH" with vpunch
    show alex shock
    a "The hell was that???"

    menu :
        "Investigate the sound.":
            jump investigate
        "Wait for Charlie to come back.":
            jump stay

label investigate:
    scene bg hallway
    show alex worried
    "Alex goes to the origin of the sound."
    scene bg roomdoor
    show alex worried
    a "Whose room is this?"
    "Alex knocks on the door."
    "..."
    "Silence"
    a "Whose there? Open up!"
    "No answer."
    "Alex decided to open up the room door anyways."

    scene bg room
    show alex scared
    s "{b}BOO!!{/b}"
    a "AAAAAaahhhhhh"
    "Alex turned around quickly only to see a tall slim figure in front of him dying in laughter."

    show sam laughing
    s "AHAHAHAHAH"
    s "You should have seen your face"
    show alex angry
    a "Shut UP SAM!!"
    hide sam

    "Alex walked out of the room and back to the living room."
    scene bg livingroom
    "Alex heart was beating fast."
    "He places his hand on his chest."
    a "Must be from the scare earlier."
    show charlie shock:
        xzoom 0.35 yzoom 0.35
        xalign 1.0
        yalign 1.0
    c "What scare?"
    a "Nothing"
    show charlie normal:
        xzoom 0.35 yzoom 0.35
        xalign 1.0
        yalign 1.0 
    c "O...Okay. By the way, I forgot to tell you that my brother's home but he won't be bothering us."
    show sam happy
    s "I think he knows that already."
    "Sam and Alex made eye contact"
    "Alex's heart starts beating faster."
    # Alex thought
    "{i}Why am I feeling this way? I need to leave but NOW{/i} - Alex thought"
    a "Sorry but I just remebered that I need something important to do. I guess I'll see you tommorow Charlie."
    c "It's fine Alex. Text you later."
    s "Bye Alex"
    "Alex ran home and went to his bedroom"
    scene bg bedroom
    jump discovery



label stay:
    scene bg livingroom
    show alex calm
    a "Must be the wind"
    "{b}SLAM{/b}" with vpunch
    show alex scared
    a "What was that?"
    a "Charlie, is that you? This isn't funny"
    show sam upset
    s "It's not Charlie."
    s "{b}WOW{/b} how could you not remember me."
    s "You know, Charlie doesn't live here by herself."
    a "Oh.H...HI sam."
    "Alex heart started beating fast as he turned to look at Sam."
    s "Whatever"
    "Sam leaves irritated."
    hide sam
    # alex thought
    "{i}What's happening? Why am I feeling this way?{/i} - Alex thought"
    show charlie normal:
        xzoom 0.35 yzoom 0.35
        xalign 1.0
        yalign 1.0
    c "Sorry for taking long."
    a "No problem. So, what do you want to do now?"
    c "Play video games? Oh wait, I forgot to tell you that my brother's home but he won't be bothering us."
    show sam serious
    s "I think he knows that already."
    "sam and alex make eye contact"
    "Alex's heart starts beating faster."
    # Alex thought
    "What's wrong with me? - Alex thought"
    a "Sorry, but I just remebered that I need something important to do. I guess I'll see you tommorow Charlie."
    show charlie grin
    c "It's fine, Alex. Text you later!!"
    s "Bye Alex."
    "alex ran home and went to his bedroom"
    scene bg bedroom
    jump discovery


label discovery:

    show alex worried

    a "It makes no sense!!!"
    a "I don't get it!!"
    a "I've known Sam for so long, but yet..."
    a "How come I feel this way??"
    a "Is it possible that I'm..."
    a "no....No....NO!"
    a "That can't be but....... it's not impossible"
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
    "Alex grabbed his phone."
    a "Hello Charlie, I..I need your help. I'm lost."
    c "How can you be lost don't you remember where you live? Tell me the street.."
    a "No that's not what I meant. I'M CONFUSED WITH MY FEELINGS!!"
    c "Uh, ok. But calm down."
    c "And what do you mean your feelings?"
    a "Sorry about that. But anyways, today I saw this guy and when our eyes met my heart started beating fast. I don't know what's wrong."
    c "..."
    a "Hello?"
    c "Um... Do you possibly have a thing for guys? I thought you liked girls?"
    a "I don't know... I never felt this way before for anyone."
    c "I'm sorry, Alex, but I need to go."
    a "Wait..."
    "Charlie hung up."
    scene bg living room
    c "What should I do? I never had a friend whose gay."
    c "What will others think?"
    c "I don't want them to think that I could be lesbian for having a gay friend."
    c "But Alex needs my help and he's my best friend!"

    menu:
        c "What should I do?"

        "Try to help Alex and stay friends":
            jump help
        "Stop being friends with Alex":
            jump ignore_him

label help:
    c "I can't leave Alex all alone. I need to be by his side."
    c "But I don't know how to help..."
    c "Well, time to go to the wisest thing I know."
    c "The internet!"
    "Charlie came upon a website called \"Love Connections\""
    "Parental Guide: Advice from other parents, I think my child is ___, Forums to help parents"
    c "I think I'll read the advice from other parents. It may contain something useful."
    c "I am practically his parent anyway. I woke him up that one day during the exams."
    "..."
    "Charlie finished reading the article and picks up her phone and dials a phone number"
    c "Alex. I'm sorry for not letting you finish earlier and not listening to you. I know it hard for you right now but you can trust me and be by your side."
    "{i}Wow. That article affected me a lot. Haha starting to talk like a grown up{/i} - thought Charlie"
    a "Thank You."
    a "Everything is still rather confusing though. I think I'm into guys, but I'm not sure yet..."
    c "I was going to say to follow you heart, but it seems your heart and brain are debating."
    a "Yeah, I guess you're right. Haha."
    c "Anyway, there's nothing wrong with you if you like guys. It won't change who you are."
    c "And based on what you have told me it seem like you {i}like like{/i} this guy."
    a "D-don't say it like that! It's not confirmed yet..."
    c "mmmhm"
    c "Don't hide those feelings and don't be afraid to be you. I'll be on the sidelines cheering you on!"
    a "Thank you, Charlie. I knew you were the right person to tell"
    c "Just be true to your feelings, alright?
    c "And by the way..."
    menu:
        c "Who is the guy you like?"
    
        "Tell her the truth:
            jump truth
        "Tell her a lie"
            jump lie
    

     # need to write smething that connects to end




label ignore_him :
    scene bg bedroom
    show alex cry
    a "What should I do now she just hung up on me"
    scene bg livingroom
    c "Im sorry alex but i was taught that that's wrong. Everything would have been good if you said you had feeling for a girl not guy"
    "Next morning"
    scene bg school
    show alex happy
    "I see charlie putting her things in her locker - alex"
    a "Hey Charlie"
    a "i need to talk  to you"
    c "oh. It's you. See I don't have time to listen to you. Also i don't think this friendhip is going to last so we should make new friends and also pretend you don't know me if you see me in the hallways"
    "Alex eyes became watery"
    "Does she hate me for having feelings for a guy -Alex"
    "Was I to harsh on him? he's probably alone. but how do I understand him? -Charlie"
    "Afternoon"
    "Charlie was browsing through the internet."
    c "Love Connection?"
    c "Is this a dating site? i'm going to check it out"
    c "what do they mean by closet doors closed. what's this?"
    "charlie clicks on the closet doors"
    c "A time to open the closet doors? This isn't for me but it may help me understand alex"
    c "let's check the parential guide"
    "Parental Guide: Advice from other parents , I think my child is ___, Forums to help parents"
    c "I think I'll read the advice from other parents . even though i'm not his parent it should be helpful advice"
    "Charlie finished reading the article and picks up her phone and dials a phone number"
    c "Alex. I'm sorry for ignoring you. i should have listen to you"
    a "Thank You for changing your mind. THis is rather confusing to me and I'm glad that you accepted that I may be gay"
    c "I learned that there's nothing wrong with being homosexual because at the end of it all your still the same alex, my best friend forever."
    c " I hope you forgive me for not being able to understand you and be by you side."
    # trying to add sam to the story but things aren't going good >_<
    # note: please revise later
    "sam walks in the living room where charlie is at"
    a "Thanks for understanding but i will only forgive you if we remain friends like before"
    c "Of course Alex"
    "alex and charlie say goodbye and hang up"
    s "what happened to you. why so gloomy?"
    c "I ignored Alex today because he told me that he liked guys"
    show sam shock
    s "The hell? Why would you do that?"
    c "I wasn't used to the idea of boys liking boys. But I guess love can transend genders"
    # when you try to make things funny but end up failing
    s "Well ain't that fan-freaking-tastic!!"
    show charlie grin
    c "Yup, I gotta stay woke"
    s "..."
    s "Ay, lil sis. Wanna hear a fun fact"
    show charlie normal
    c "Suurre"
    s "I'm bisexual"
    c "..."
    
    # this is terrible


    # need to write smething that connects to end


label secret:
    a "I don't quite understand these feelings yet."
    a "I should keep it a secret until it starts to make sense"
    a "What happens if they think my feelings aren't normal. Yep. keeping it a secret is for the best"
    "next morning"
    scene bg school
    show charlie happy
    c "Hello alex"
    show alex worried
    a "H...hi"
    c "whats wrong? you seem nervous"
    a "It's nothing. lets go"
    c "okay. want to hang out at my house today?"
    a "sure"
    "time skip"
    scene bg living room 
    "Alex and Charlie enter the living room only to find sam sitting on the couch"
    s "sup guys"
    a and c "hi sam"
    "Alex face began to turn red"
    # Alex thought
    " What's wrong with me? Is it possible that i like sam? - Alex"
    s "Alex are you okay?"
    "sam stood up and went to Alex and put his hand on alex forehead"
    s "Just making sure that your not sick or anything"
    a "I said I'M FINE"
    s "O..OK"
    "sam left and went to his room"
    a "No i'm sorry"
    c "I'm not the one you should be apologizing to"
    a "ok. i'll be right back"
    "alex went in front of sam's room and knock on the door"
    a "Sam can you open up? I need to tell you something"
    "..."
    # you can change the positions of the character since they are always standing and their face expression is the only thing that change.
    "Alex decided to open the door anyways and saw sam laying in bed"
    "Alex heart was beating faster at the sight of sam"
    s "Did i say to come in?(cold TONE)"
    A "no. But i came to apologize for raising my voice at you"
    s "ok. You can go now"
    "Alex heart felt hurt"
    "Alex left sam's room and went to the living room"
    c " what happened did he accept your apology?"
    a "um...i not feeling good. I'm just going to go home"
    "Alex just left charlie's house"
    c "That was weird"
    scene bg bedroom
    a "should i tell sam how I feel, yeah probably that would be for the best"
    
   
    menu:
        a "What should I do?"

        "Write sam a letter and make it annoymous":
            jump letter
        "Tell sam how i feel in person":
            jump say
            
label letter:
    "\"Dear Sam,\""
    "\"I've known you for a while now, but recently I've been developing feelings for you.\""
    "\"As of now, I don't quite understand why I feel this way for a giant prick.\""
    "\"But, I hope to cope wihtour concequence by sneding this letter.\""
    "\"If you feel the same, that'll be great!\""
    "\"However, I doubt that you'll fall in love with someone like me.\""
    "\"Sincerely Alex\""
    a "Writing my name is wayyyyy too embarrassing!!"
    "Alex hastily erased his name and replaced it with..."
    "\"Sincerely, A fellow coffe drinker\""
    a "This is good enough"
    "Next day"
    a "This letter is cappable of ruinig my life"
    a "But it's all for sam"
    
    
    
    
    
    
    
label say:
    a "I think  telling him my feelings in peron would show him that i reaaly mean it"
    a "but what happens if he rejects me or worst makes fun of me"
    a "ALEX STOP BEING SUCH A CHICKEN YOU GOT THIS"
    "Next Morning"
    scene bg school
    "Alex just tell him your feelings what's the worst that can happen -alex"
    "charlie runs behind alex"
    c "HHII"
    a"AAAAAaaaaahhhh"
    c "it's just me"
    a "Hi charlie"
    "sam comes up behind them"
    s "sup guys. CHARLIE I TOLD YOU TO WAIT FOR ME"
    c "sorry probably NEXT TIME HURRY THE HELL UP"
    a "we should get to class,people are starring"
    "End of school"
    a"Geez,charlie where are you?"
    "sam was walking behind charlie"
    s "She said she had something important to do but she will catch us later."
    a "what do you mean by us?"
    s "She said to wait for her at home she wants to tell you something"
    a "ok but before we go i must tell you something"
    s "suuurre"
    a " You see..."
    a "umm...I have feelings..."
    s "Don't we all have feelings"
    a "no..yeah... that's not what I meant"
    a " I..I think I li..like y..ou"
    a "My heart it wants to burst out at the sight of you"
    "sam face began to turn red"
    sam "..."
    a "You don't have to like me back. I need to go"
    "alex ran away as fast as he could home"
    scene bg bedroom
    "That was humiliating. he didn't even say a word or stoped me from leaving -alex"
    scene bg school
    "What he likes me? But how? -sam"
    c "SSSAAAMMM"
    "charlie came running to sam"
    c "hey why are you still here and where's alex"
    s "I decided to wait for you and he had to leave"
    c "okay let's go home then"
    
    
    
    
    s "Alex, I like gals."
    a "I'm such an idiot! I knew that this wouldn't work out..."
    s "...{i}aaand{/i} guys"
    s "Kind of like you ;)"
    "Alex's face turns completly red."
    "Good end."
    return
    
    
    
    
    
    
    
    
    # i don't know what else to write





label ignore :
    a "These feelings just happened today, probably tommorow they will be gone"
    a "Feelings come and go"
    "Next day"
    a "Why can't do these feelings grow stronger when i think of him"
    a "A guy liking a guy is wrong"
    a " why am i not normal"
    # i don't know what else to write
    menu:
        a "What should I do?"
        
        "Keep it in":
            jump keep_it_in
        "Let it go (like Elsa)":
            jump elsa
