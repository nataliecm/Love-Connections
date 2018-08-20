# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg livingroom = "bg_livingroom.jpg"
image charlie normal = "charlie_normal.png"
image charlie shock = "charlie_shock.png"
image charlie grin = "charlie_grin.png"
image alex annoyed = "alex_annoyed.png"
image alex happy = "alex_happy.png"
image alex shock = "alex_shock.png"
image alex shock2 = "alex_shock2.png"
image alex sad = "alex_sad.png"
image alex shock blush2= "alex_shockblush2.png"
image bg hallway = "hallway.jpg"

define a = Character("Alex")
define c = Character("Charlie")
define s = Character("Sam")
define ??? = character("UNKNOWN")


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
        xzoom 0.35 yzoom 0.35
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
    hide charlie
    "Alex was waiting around (being bored out of his mind if I must add) until suddenly..."
    show alex shock2
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
    show alex sad:
        xzoom 0.35 yzoom 0.35
        xalign 0.0
        yalign 1.0
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
    show alex shock:
        xzoom 0.35 yzoom 0.35
        xalign 0.0
        yalign 1.0
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
    show alex shock blush2:
        xzoom 0.35 yzoom 0.35
        xalign 0.0
        yalign 1.0"Alex heart was beating fast."
    "He places his hand on his chest."
    a "Must be from the scare earlier."
    show charlie shock:
        xzoom 0.35 yzoom 0.35
        xalign 1.0
        yalign 1.0
    c "What scare?"
    a "Nothing"
    show charlie normal
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
    "Charlie finished reading the article"
    "sam walks in the living room"
    s "what happened to you. you look tired"
    c "i was reading an article about the lgbtq+ community andaccept and help the peole who are close to you that are part of that community."
    c "At fist i wasn't used to the idea of boys liking boys. But I guess love can transend genders. Alex told me he hadfeelings for a guy"
    # when you try to make things funny but end up failing
    s "Well ain't that fan-freaking-tastic!!"
    show charlie grin
    c "Yup, I gotta stay woke"
    s "..."
    s "Ay, lil sis. Wanna hear a fun fact?"
    show charlie normal
    c "Suurre"
    s "I'm bisexual"
    c "..."
    c "I gues i'm GLAD you came out."
    c" but you know i still love you no matter what right"
    "sam smile brightly"
    s "thanks"
    "sam goes back o his room happily"
    "Charlie picks up her phone and dials alex phone number"
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
    
label lie:
    a "Some guy that i recently saw in walmart but you don't know him"
    # Not sponsored by walmart. I never given been to walmart.
    c "It almost sound like love at first sight"
    c "what did he look like"
    a "oh. You know tall, great sense of style and great pesonality"
    c "wait how do you know he had a great personality?"
    a "I waaaas just guessing by his apperance"
    c "cool"
    a "Yeah..."
    c "Thank god it's not someone like my brother"
    c "He can be annoying like 99% of the time and his sence of style sucks"
    a "WHAT...I mean why would it be your brother?"
    c "Oh i forgot to tell you turns out my brother is bisexual"
    "could there actually be a chance for me or us - alex"
    a "charlie i need to go. i have simething to do"
    c "ok see you soon"
    "alex hung up"
    a "should i write him a letter"
    a "yes this would give me an opportunity":
        jump letter



label truth:
    a "Well, It's kind of hard for me to tell"
    c "Come on Alex you know you can tell me anything.Just let it go"
    a "it's sam"
    c "YOU MEAN MY BROTHER SAM. My brother?"
    a "yeah(sad tone)"
    c "That's great"
    a "what?"
    c "well it turns out my brother is bisexual?"
    a "so...your not mad"
    c "Why would i be mad?"
    a "Becaus ehe's your brother and i'm your best friend"
    c "well as long as both of you are happy i'm happy"
    c "Wait i just had a great plan."
    a "what plan for what"
    c "its a suprise but come to my house around 7 okay"
    a "o..okay"
    "both charlie and alex hung up"
    "charlie went to sam's room"
    s "hey have you ever heard of something called knocking"
    c "would you go to a blind date"
    s "NO"
    c "Please not even for your sister"
    s "..."
    show charlie sad
    s "Fine but whose the person"
    c "My friend..."
    "when she said her friend my heart started to beat faster because i knew for a fact it was about alex -sam"
    s "YEAH...i mean i'll do it just for you"
    c "okay thanks"
    c "start getting ready you need to be ready by 7"
    s "okay"
    "charlie left sam's room"
    c "This is going to be great"
    # what scene should this be living room or kitchen
    "Charlie started stetting up the table and ordered pizza for them to eat"
    c "The pizza should be fine. It's not my fault that I never learned to cook"
    # relatable
    "current tim 6:54"
    "sam walks to the kitchen/living roon"
    s "i thought the date was was going to be somewhere prettier and fancier"
    s "And really PIZZA"
    c "well sorry i'm on a buget.Someone doesn't give me enough allowence"
    s "-_-"
    s "well it's good enough"
    c "You should appericate my work more. i worked hard to make this possible"
    "Not really i just had to cover up the table with a table cloth and order pizza but he's getting on my nerves -Charlie"
    "DING DONG, ding dong"
    c "SIT down, i'll go get the door"
    "he's here. act natural -sam"
    "charlie get the door and lets alex in":
            jump ending_1
            
            
label ending_1:
    scene bg kitchen/livingroom
    "Charlie leads Alex to the living room/kitchen"
    "Alex walks to the kitchen/living room and sees Sam sitting down"
    "Is this the plan she had in mind? -Alex"
    c "Alex please sit down"
    "alex sits down across from sam"
    c "You guys have fun. I'm going to my room"
    "Both alex and sam nod"
    "charlie goes to her room"
    a "...."
    s "...."
    a "I'm sorry she dragged you into this"
    s "I'm actually happy she did"
    s "I have been waiting for this to happen"
    show alex shocked
    a "...what?"
    s "I wanted to tell you how i felt about you since the day i meet you but i felt that you might not like me back"
    a "of course i like you back. I thought I was going insane because these feeling were new to me"
    a "You know your the first person to ever make me feel this way"
    "sam blushes"
    s "I should have asked you sooner"
    a "asked me what"
    # formal make joke
    s "Alex would you do me the honor and be by my side"
    
    a "Are you asking me out"
    s "ye..ah"
    a "i would love to"
    "sam leaned in"
    "does he want to kiss.OH MY GOD my first kiss -alex"
    "Alex leaned in as well"
    "THE END"
    
    
    
    
    
    

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
    s "I know it may be hard for you to understand but it was hard for me to tell you..."
    "charlie ran to hug sam tightly"
    c "You would always be my favorite brother. i love you no matter what"
    s "thanks...wait i'm your only brother tho"
    c "i know... It still counts though!":
        jump to ending_2
        
label ending_2:
    "Sometimes in life the only love that should matter is the love that you give to youself"
    "We need to love ourselves before we take the love others offer"
    "WHEN YOU KNOW YOURSELF YOU ARE EMPOWERED.WHEN YOU ACCEPT YOUSELF YOU ARE INVINCIBLE"
    "People tend not to accept themselves because of fear of their family not accepting them but they would eventually understand if their love towards you is strong."
    "And families stay together with love and respect. Someone's sexuality doesn't make some into a new person"
    "Instead of pushing other's aside because of their sexuality we should take the chance to understand them. Pushing people aside just harms both sides"
    "LEARNING TO ACCEPT YOUSELVES IS MORE IMPORTANT THAN MAKING PEOPLE ACCEPT YOU. IT'S HOW YOU SEE YOUSELF THAT REALLY MATTERS"
    
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
    "alex called charlie"
    a "hey charlie . do you wanna hang out tommorow after school"
    c "sure. can't wait"
    a "ok, cool"
    "alex hung up"
    "time skip to tommorow after school"
    c "Thank god we don't have alot of homework"
    a "yeah. but where is sam?" 
    c "He went to go hang out with his friends"
    "{i}That's perfect now i can sneak the letter to his room{/i} -alex"
    "alex and charlie arrived to charlie's house
    scene bg livingroom
    a "before we start playing video games can i use your bathroom"
    c "yeah sure."
    "alex left to go to the bathroom but instead went to sam's room"
    a "i should just leave it on top of his desk"
    "alex left the letter of sam's desk and went back to the living room"
    c "hey that was quick but..."
    c "are you ready to lose"
    a "Haha i NEVER lose"
    "Charlie and alex began playing video games"
    c "see you lost. i'm the champion"
    a "WOW it's 8 already" 
    c "what we took that long playing video games but it was worth it"
    c "to see me win"
    a "bye"
    c "bye see you tommorow, loser"
    a "Wooow, you're so cruel. But i need to go home now"
    "alex left charlie's house"
    scene bg bedroom
    a "i wonder if he's home already."
    a "or did he read the letter"
    "Beep beep"
    "alex checked his phone"
    "???: Hi"
    a "who can this be?"
    "alex wrote back"
    "sorry wrong number"
    "???: i like you too"
    a "could this be sam no it's probably a prank"
    "alex wrote:"
    "who is this? This isn't funny"
    "???: since when are my feelings a joke"
    a "this is really creepy" :
        jump ending_3
        
 label ending_3:
    "The unknown person started to call"
    "Alex answered the call"
    a "hello. who is this"
    ???  "hi alex. it's sam"
    "S A M. what? -alex"
    a "um.. what do you want"
    s "what? you're the one who left a love letter on my desk!"
    a "wait how did you know it was me"
    s "first of all your horrible at being annoymous"
    s "Who writes a love letter in print, i know how your handwriting looks like"
    s "Also you left the letter in my desk you are the only person who comes to my house and hangout with charlie"
    s "but i need to know if what you said in the letter is true"
    a "Well yeah it is true..."
    a "that your a giant prick"
    s "I WAS TALKING ABOUT THE FEELINGS PART OF THE LETTER"
    a " i don't know"
    "alex hung up the phone"
    a "Alex your such an idiot"
    "buzz, BUZZ BUZZ,buzz"
    "Alex check the caller id it was sam's"
    "Alex decided to answer the call"
    a "hel..."
    s "HOW DARE YOU HANG UP ON ME."
    s "FIRST YOU SAY THAT YOU LIKE ME THEN YOU HANGE UP"
    s "ARE YOUR FEELING EVEN TRUE"
    s "BUT FOR A FACT THAT I DO KNOW IS 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
label say:
    a "I think  telling him my feelings in person would show him that i really mean it"
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
    "Sam was walking behind charlie"
    s "She said she had something important to do but she will catch us later."
    a "What do you mean by us?"
    s "She said to wait for her at home she wants to tell you something"
    a "Ok, but before we go I must tell you something..."
    s "Suuurre"
    a " You see..."
    a "umm...I have feelings..."
    s "Don't we all have feelings"
    a "no..yeah... that's not what I meant"
    a " I..I think I li..like y..ou"
    a "My heart it wants to burst out at the sight of you"
    "Sam face began to turn red."
    Sam "..."
    a "You don't have to like me back. I need to go"
    "Alex ran away as fast as he could home"
    scene bg bedroom
    "{i}That was humiliating. He didn't even say a word or stoped me from leaving{/i} -Alex"
    scene bg school
    "What he likes me? But how? -Sam"
    c "SSSAAAMMM"
    "Charlie came running to Sam"
    c "Hey, why are you still here and where's Alex?"
    s "I decided to wait for you and he had to leave."
    c "Okay, let's go home then."
    scene ng living room 
    "should I tell Alex how i feel-sam"
    c "what are thinking so much about"
    s "I have feeling for this guy"
    show charlie shocked
    c"A GUY?"
    s "Yes, But should I tell him I like him back" 
    c "HE LIKES YOU TOO?"
    s "YOU know your not that HELPFUL"
    c "I'm sorry i just didn't know you were um... you know"
    s "BISEXUAL"
    c "...yeah..."
    s "...so anyways what should i do?"
    c "You should just tell that person. Follow yur heart"
    s "okay but can i borrow yoour phone?"
    c "why?"
    s "Just give it to me"
    "sam handed her phone to sam and sam dialed someone"
    "??? - hello charlie"
    s "Hi Alex. Can you come over i need to tell you something"
    a "sam?...um..sure"
    "WHAT THE GUY IS ALEX. HOW DIDN'T I NOTICE BEFORE -_- .-charlie"
    "sam hung up the phone"
    "Is this what LOVE is - charlie"
    c "sssoo... Alex is the guy?
    s "Y..es. does it bother you?
    c "No. but i'm glad to see you happy"
    "Time Skip"
    "Ding Dong"
    s "Can you go to your room i need to talk to him in private."
    c "ok."
    "charlie left to her room"
    "sam went to open the door and let alex in"
    a "Hi sam. did something happen to charlie?"
    s "no. i called you over because i need to talk to you about something important"
    s "Remember earlier today you confessed to me"
    a "yeah that was embarrassing"
    s "NO it wasn't. it was actually pretty brave of you"
    a "I have been feeling this way for you since that time i saw you again"
    a "i have been confused about these feeling because i never felt this way before for someone especially a guy"
    "I should tell him. I made him suffer earlier already -sam"
        jump ending_4
      
    
label ending_4:   
    s "Alex, I like gals."
    a "I'm such an idiot! I knew that this wouldn't work out..."
    s "...{i}aaand{/i} guys"
    s "Kind of like you ;)"
    "Alex's face turns completly red."
    a "Y..you like me?"
    s "of course i like you. why wouldn't i."
    s "my heart beats fast everytime your near me."
    s "i actually wanted to confess first but you beat me at that"
    s "but Alex would you like to be my boyfriend?"
    "{i}Is this really happening. Dreams do come true.{/i} -alex"
    a "I would love to"
    "alex hugged sam tightly. sam hugged him back"
    
    "GOOD END."
    return
    
    
    
  





label ignore :
    a "These feelings just happened today, probably tommorow they will be gone."
    a "Feelings come and go"
    "Next day"
    a "Why do these feelings grow stronger when I think of him"
    a "A guy liking a guy is wrong."
    a " why am i not normal"
    # i don't know what else to write
    menu:
        a "What should I do?"
        
        "Keep it in":
            jump keep_it_in
        "Let it go (like Elsa)":
            jump elsa
            
            
 label keep_it_in:
    a "these feelings aren't permanent"
    a "there is no way that i can be gay"
    a "imagine me being gay. that would be terribe"
    a "no onewould want to be my friend or my family might not accept me"
    a "i must get rid of these feelings"
    a "I MUST FORCE MYSELF TO HAVE FEELINGS FOR A GIRL"
    a " i should date charlie and forget about sam"
    "the next day in school"
    a "where are you charlie"
    "Alex looked around to looking for charlie and spotted her arriving to school"
    "alex ran to charlie"
    a "hey charlie!!"
    c "hi alex. whats up?"
    a "I have something to ask"
    c "Ok. im listening"
    a "Would you want to be my girlfriend"
    "why all of a sudden. i dont want to ruin our friendship but if i reject him it can be the end of it -charlie"
    "i shouldn't be using her. this was a bad idea and why did i say it all of a sudden -alex"
    c "i would like to"
    "i feel so bad for giving him fake hope -Charlie"
    "she should have said no. i'm not even her type -alex"
    a "want to hold hands"
    c "okay"
    "charlie and sam holded hand to school":
        label ending_5
        
label ending_5:
    "after school. charlie and alex went to hangout in the park to celebrate their first day as a couple"
    "should i kiss him. its only natural since were a thing now -charlie"
    "why did she close her eyes? why is she leaning in? -alex"
    "i should lean in for the kiss too - alex"
    "alex and charlie pecked each others lips fast and backed away from each other"
    "they opened their eyes to realize this was a mistake"
    "I felt nothing at all. None of this has meaning. I'm sorry alex. -charlie"
    "Not even once my heart skipped a beat through the kiss it just felt wrong and i hated it -alex"
    "Alex started to burst in tears"
    a "I'm sorry"
    c "You shouldn't be sorry. i'm the one who gave you false hope that this would work"
    a "I lied and used you to get rid of feelings i had for someone else"
    show charlie shocked
    a "Someone who i can't give my love to."
    c "who is this someone, alex"
    a "i can't say i perfer to keep this between me"
    c "ok. i respect you privacy"
    a "I need some alone time"
    "alex left charlie alone"
    a "My life's a mess"
    a "I used my best friend for my selfish pursposes"
    a "And i don't like girls"
    a "who am i really?
    "BAD END"
    return
    
    
    
    
    
 
