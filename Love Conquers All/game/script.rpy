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
define u = character("UNKNOWN")


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
    scene bg livingroom
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
    scene bg bedroom_door
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
    c "O...Okay. By the way, I forgot to tell you that my brother's home. He's back from his trip."
    c "But don't worry he won't be bothering us."
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
    scene bg bedroom
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
    scene bg livingroom
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
    c "Just be true to your feelings, alright?"
    c "And by the way..."
    menu:
        c "Who is the guy you like?"
    
        "Tell her the truth":
            jump truth
        "Tell her a lie":
            jump lie
    
label lie:
    a "Some guy that I recently saw in walmart but you don't know him"
    # Not sponsored by walmart. I never given been to walmart.
    c "It almost sound like love at first sight"
    c "What did he look like"
    a "Oh. You know tall, great sense of style and great pesonality"
    c "Wait how do you know he had a great personality?"
    a "I waaaas just guessing by his apperance"
    c "cool"
    a "Yeah..."
    c "Thank god it's not someone like my brother"
    c "He can be annoying like 99% of the time and his sense of style sucks"
    a "WHAT...I mean why would it be your brother?"
    c "Oh I forgot to tell you turns out my brother is bisexual"
    "could there actually be a chance for me or us - alex"
    a "Charlie I need to go. I have simething to do"
    c "ok see you soon"
    "Alex hung up"
    a "should I write him a letter"
    a "yes this would give me an opportunity"
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
    a "Because he's your brother and i'm your best friend"
    c "well as long as both of you are happy i'm happy"
    c "Wait i just had a great plan."
    a "what plan for what"
    c "Its a suprise but come to my house around 7 okay"
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
    s "YEAH...I mean i'll do it just for you"
    c "okay thanks"
    c "start getting ready you need to be ready by 7"
    s "okay"
    "charlie left sam's room"
    c "This is going to be great"
    # what scene should this be living room or kitchen
    "Charlie started stetting up the table and ordered pizza for them to eat"
    c "The pizza should be fine. It's not my fault that I never learned to cook"
    # relatable
    "Current tim 6:54"
    "Sam walks to the kitchen/living roon"
    s "i thought the date was was going to be somewhere prettier and fancier"
    s "And really PIZZA"
    c "Well sorry I'm on a buget.Someone doesn't give me enough allowence"
    s "-_-"
    s "well it's good enough"
    c "You should appericate my work more. i worked hard to make this possible"
    "Not really i just had to cover up the table with a table cloth and order pizza but he's getting on my nerves -Charlie"
    "DING DONG, ding dong"
    c "SIT down, i'll go get the door"
    "{i}He's here. Act natural{/i} -Sam"
    "Charlie get the door and lets Alex in"
    scene bg livingroom
    "Charlie leads Alex to the living room"
    "Alex walks to the living room and sees Sam sitting down"
    "{i}Is this the plan she had in mind?{/i} -Alex"
    c "Alex please sit down"
    "Alex sits down across from sam"
    c "You guys have fun. I'm going to my room"
    "Both Alex and Sam nod"
    "Charlie goes to her room"
    a "...."
    s "...."
    a "I'm sorry she dragged you into this"
    s "I'm actually happy she did"
    s "I have been waiting for this to happen"
    show alex shocked
    a "...what?"
    s "I wanted to tell you how I felt about you since the day I meet you but I felt that you might not like me back"
    a "Of course I like you back. I thought I was going insane because these feeling were new to me"
    a "You know your the first person to ever make me feel this way"
    "sam blushes"
    s "I should have asked you sooner"
    a "asked me what"
    # formal make joke
    s "Alex would you want to be with me?"
    a "Are you asking me out"
    s "ye..ah"
    a "I would love to"
    "Sam leaned in"
    "{i}Does he want to kiss.OH MY GOD my first kiss{/i} -Alex"
    "Alex leaned in as well"
    "THE END"
    return

label ignore_him :
    scene bg bedroom
    show alex cry
    a "What should I do now she just hung up on me"
    scene bg livingroom
    c "Im sorry alex but I was taught that that's wrong. Everything would have been good if you said you had feeling for a girl not guy"
    "Next morning"
    scene bg school
    show Alex happy
    "{i}I saw charlie about to go inside the building{/i} -Alex"
    a "Hey Charlie"
    a "I need to talk to you"
    c "oh. It's you. See I don't have time to listen to you. Also I don't think this friendhip is going to last so we should make new friends and also pretend you don't know me if you see me in the hallways"
    "Alex eyes became watery"
    "{i}Does she hate me for having feelings for a guy{/i} -Alex"
    "{i}Was I to harsh on him? he's probably alone. but how do I understand him?{/i} -Charlie"
    "Afternoon"
    scene bg livingroom
    "Charlie was browsing through the internet."
    c "Love Connection?"
    c "Is this a dating site? I'm going to check it out"
    c "what do they mean by closet doors closed. what's this?"
    "Charlie clicks on the closet doors"
    c "A time to open the closet doors? This isn't for me but it may help me understand Alex"
    c "let's check the parential guide"
    "Parental Guide: Advice from other parents , I think my child is ___, Forums to help parents"
    c "I think I'll read the advice from other parents . even though I'm not his parent it should be helpful advice"
    "Charlie finished reading the article and picks up her phone and dials a phone number"
    c "Alex. I'm sorry for ignoring you. I should have listen to you"
    a "Thank You for changing your mind. This is rather confusing to me and I'm glad that you accepted that I may be gay"
    c "I learned that there's nothing wrong with being homosexual because at the end of it all your still the same Alex, my best friend forever."
    c " I hope you forgive me for not being able to understand you and be by you side."
    # trying to add sam to the story but things aren't going good >_<
    # note: please revise later
    "sam walks in the living room where charlie is at" 
    show sam
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
    show charlie 
    c "Suurre"
    s "I'm bisexual"
    show cahrlie shocked
    c "..."
    s "I know it may be hard for you to understand but it was hard for me to tell you..."
    "Charlie ran to hug Sam tightly"
    c "You would always be my favorite brother. I love you no matter what"
    s "thanks...wait I'm your only brother tho"
    c "I know... It still counts though!"
    "Sometimes in life the only love that should matter is the love that you give to youself"
    "We need to love ourselves before we take the love others offer"
    "WHEN YOU KNOW YOURSELF YOU ARE EMPOWERED.WHEN YOU ACCEPT YOUSELF YOU ARE INVINCIBLE"
    "People tend not to accept themselves because of fear of their family not accepting them but they would eventually understand if their love towards you is strong."
    "And families stay together with love and respect. Someone's sexuality doesn't make some into a new person"
    "Instead of pushing other's aside because of their sexuality we should take the chance to understand them. Pushing people aside just harms both sides"
    "LEARNING TO ACCEPT YOUSELVES IS MORE IMPORTANT THAN MAKING PEOPLE ACCEPT YOU. IT'S HOW YOU SEE YOUSELF THAT REALLY MATTERS"
    "The End"
    return
  
label secret:
    scene bg livingroom
    a "I don't quite understand these feelings yet."
    a "I should keep it a secret until it starts to make sense"
    a "What happens if I did tell them about my feelings then they think my feelings aren't normal. Yep. keeping it a secret is for the best"
    "Next Morning"
    scene bg school
    show charlie happy
    c "Hello alex"
    show alex worried
    a "H...hi"
    c "Whats wrong? You seem nervous"
    a "It's nothing. Lets go"
    c "Okay. Want to hang out at my house today?"
    a "Yep"
    "Time Skip"
    scene bg living room 
    "Alex and Charlie enter the living room only to find sam sitting on the couch"
    s "sup guys"
    a and c "hi sam"
    "Alex face began to turn red"
    show alex blushing
    "{i}What's wrong with me? Is it possible that i like sam?{/i} - Alex"
    s "Alex are you okay?"
    "Sam stood up and went in front of Alex and put his hand on Alex forehead"
    s "Just making sure that your not sick or anything"
    a "I said I'M FINE"
    s "O..OK"
    "Sam left and went to his room"
    hide sam
    a "No I'm sorry"
    c "I'm not the one you should be apologizing to"
    a "ok. i'll be right back"
    hide charlie
    scene bg bedroom_door
    "Alex went in front of Sam's room and knocked on the door"
    a "Sam can you open up? I need to tell you something"
    "..."
    # you can change the positions of the character since they are always standing and their face expression is the only thing that change.
    scene bg beadroom_2
    "Alex decided to open the door anyways and saw sam laying in bed"
    "Alex heart was beating faster at the sight of sam"
    show sam mad
    s "Did I say to come in?(Cold TONE)"
    A "no. But I came to apologize for raising my voice at you"
    s "ok. You can go now"
    "Alex heart felt hurt"
    scene bg livingroom
    "Alex left Sam's room and went to the living room"
    c "What happened did he accept your apology?"
    a "um...I not feeling good. I'm just going to go home"
    "Alex just left Charlie's house"
    c "That was weird"
    scene bg bedroom
    a "Should I tell sam how I feel, yeah probably that would be for the best"
    
   
    menu:
        a "What should I do?"

        "Write sam a letter and make it annoymous":
            jump letter
        "Tell sam how i feel in person":
            jump say
            
label letter:
    scene bg bedroom
    show alex happy
    "\"Dear Sam,\""
    "\"I've known you for a while now, but recently I've been developing feelings for you.\""
    "\"My heart beats fast that i can't control it. It's got a mind of it's own.\""
    "\"As of now, I don't quite understand why I feel this way for a giant prick.\""
    "\"But, I hope to cope without any concequence by sending this letter.\""
    "\"If you feel the same, that'll be great!\""
    "\"However, I doubt that you'll fall in love with someone like me.\""
    "\"Sincerely Alex\""
    a "Writing my name is wayyyyy too embarrassing!!"
    "Alex hastily erased his name and replaced it with..."
    "\"Sincerely, A fellow coffee drinker\""
    a "This is good enough"
    "Next day"
    a "This letter is cappable of ruinig my life"
    a "But it's all for sam"
    "alex called charlie"
    a "hey charlie . do you wanna hang out tommorow after school"
    c "sure. can't wait"
    a "ok, cool"
    "alex hung up"
    "Time Skip to tommorow after school"
    scene bg school
    c "Thank god we don't have alot of homework"
    a "yeah. but where is sam?" 
    c "He went to go hang out with his friends"
    "{i}That's perfect now i can sneak the letter to his room{/i} -Alex"
    "Alex and Charlie arrived to Charlie's house"
    scene bg livingroom
    a "Before we start playing video games can I use your bathroom"
    c "ok."
    "Alex secretly went to Sam's room than the bathroom"
    # bedroom_2 = sam's room
    scene bg bedroom_2
    a "I should just leave it on top of his desk"
    "Alex left the letter of Sam's desk and went back to the living room"
    c "hey that was quick but..."
    c "are you ready to lose"
    a "Haha I NEVER lose"
    "Charlie and Alex began playing video games"
    show charlie happy
    c "see you LOST. I'm the champion"
    a "WOW it's 8 already" 
    c "what we took that long playing video games but it was worth it..."
    c "To see me win"
    show alex calm
    a "ok.bye"
    c "bye see you tommorow, loser"
    a "Wooow, you're so cruel. But i need to go home now"
    "alex left charlie's house"
    scene bg bedroom
    a "I wonder if he's home already."
    a "Or did he read the letter"
    "Beep beep"
    "alex checked his phone"
    "???: Hi"
    a "Who can this be?"
    "Alex wrote back"
    "sorry wrong number"
    "???: i like you too"
    a "Could this be sam no it's probably a prank"
    "alex wrote:"
    "who is this? This isn't funny"
    "???: since when are my feelings a joke"
    a "This is really creepy" 
    "The unknown person started to call"
    "Alex answered the call"
    a "hello. who is this"
    u "Hi alex. It's sam"
    "{i}S A M. what?{/i} -alex"
    a "um.. what do you want"
    s "what? you're the one who left a love letter on my desk!"
    a "Wait how did you know it was me"
    s "First of all your horrible at being annoymous"
    s "Who writes a love letter in print, I know how your handwriting looks like"
    s "Also you left the letter in my desk you are the only person who comes to my house and hangsout with charlie"
    s "But I need to know if what you said in the letter is true"
    a "Well yeah it's true..."
    a "that your a giant prick"
    s "I WAS TALKING ABOUT THE FEELINGS PART OF THE LETTER"
    a "I don't know"
    "alex hung up the phone"
    a "Alex your such an idiot"
    "buzz, BUZZ BUZZ,buzz"
    "Alex check the caller id it was sam's number again"
    "Alex decided to answer the call"
    a "hel..."
    s "HOW DARE YOU HANG UP ON ME."
    s "FIRST YOU SAY THAT YOU LIKE ME THEN YOU HANG UP"
    s "ARE YOUR FEELING EVEN TRUE"
    s "BUT FOR A FACT THAT I DO KNOW IS that i like you alot"
    a "You do?"
    s "YES. but I need to know what you feel is true"
    a "Of course it is. why would I lie about that"
    s "You don't know how happy I was when i read your letter beside the giant prick part"
    a "Sorry about that i wanted to sound annoymous"
    a "so now that we know each other's feeling now what?"
    s "we go to the next level"
    a "WHAT?"
    s "I mean we can go on dates to get to know each other better before we start to get in a relationship"
    a "I agree. That sounds great"
    "THE END"
    return
    
label say:
    scene bg bedroom
    a "I think telling him my feelings in person would show him that I really mean it"
    a "But what happens if he rejects me or worst makes fun of me"
    a "ALEX STOP BEING SUCH A CHICKEN YOU GOT THIS"
    "Next Morning"
    scene bg school
    "{i}Alex just tell him your feelings what's the worst that can happen.{/i} -Alex"
    "Charlie runs behind Alex"
    c "HHII"
    a "AAAAAaaaaahhhh"
    c "It's just me"
    a "Hi charlie"
    "sam comes up behind them"
    s "Sup guys. CHARLIE I TOLD YOU TO WAIT FOR ME"
    c "Sorry.Probably NEXT TIME HURRY THE HELL UP"
    a "We should get to class, people are starring"
    "End of school day"
    a "Geez, Charlie where are you?" 
    a "Do you know where is she?"
    "Sam was walking behind Alex"
    s "She said she had something important to do but she will catch us later."
    a "What do you mean by us?"
    s "She said to wait for her at home so that you guys can play your dumb video games"
    a "Ok, but before we go I must tell you something..."
    s "Suuurre WEIRDO"
    a " You see..."
    a "umm...I have feelings..."
    s "Don't we all have feelings"
    a "no..Well yeah... that's not what I meant"
    a " I..I think I li..like y..ou"
    a "My heart it wants to burst out at the sight of you"
    "Sam face began to turn red."
    show sam blushing
    Sam "..."
    a "You don't have to like me back." 
    s "..."
    a "I...I need to go"
    "Alex ran away as fast as he could home"
    hide sam
    scene bg bedroom
    "{i}That was humiliating. He didn't even say a word or stoped me from leaving{/i} -Alex"
    scene bg school
    hide alex
    show sam happy
    "{i}What he likes me? But how?{/i} -Sam"
    show charlie happy
    c "SSSAAAMMM"
    "Charlie came running to Sam"
    c "Hey, why are you still here and where's Alex?"
    s "I decided to wait for you and he had to go."
    c "Okay, let's go home then."
    scene ng living room 
    "{i}Should I tell Alex how I feel{/i} -sam"
    c "What are thinking so much about"
    s "I have feeling for this guy"
    show charlie shocked
    c "A GUY?"
    s "Yes, But should I tell him I like him back" 
    c "HE LIKES YOU TOO?"
    s "YOU know your not HELPING AT ALL"
    show chalrie calm
    c "I'm sorry i just didn't know you were um... you know"
    s "BISEXUAL"
    c "...yeah..."
    s "...So anyways what should I do?"
    c "You should just tell that person how you feel. Follow your heart."
    s "Okay.Can i borrow your phone?"
    c "Why?"
    s "Just give it to me"
    "Charlie handed her phone to Sam"
    "Sam dialed someone"
    "??? - Hi charlie"
    s "Hi Alex. Can you come over I need to tell you something"
    a "SAM?...um..sure"
    show charlie shocked
    "{i}WHAT THE GUY IS ALEX. HOW DIDN'T I NOTICE BEFORE -_- .{/i} -Charlie"
    "Sam hung up the phone"
    "{i}What alex beat me in getting a boyfriend first.{/i} -Charlie"
    show charlie happy
    c "sssoo... Alex is the guy?"
    s "Y..es. Does it bother you?"
    c "No. But i'm glad to see you happy"
    "Time Skip"
    "Ding Dong"
    show sam happy
    s "Can you go to your room i need to talk to him in private."
    c "ok."
    "charlie left to her room"
    hide charlie
    "Sam went to open the door and let Alex in"
    a "Hi Sam. Did something happen to Charlie?"
    s "NO. I called you over because I need to talk to you about something important"
    s "Remember earlier today you confessed to me"
    a "...yeah that was embarrassing"
    s "NO it wasn't. It was actually pretty brave of you"
    a "I have been feeling this way for you since that time I saw you again"
    a "I have been confused about these feeling because I never felt this way before for someone especially a guy"
    "{i}I should tell him now. I made him suffer earlier already{/i} -sam"
    s "Alex, I like gals."
    show alex sad
    a "I'm such an idiot! I knew that this wouldn't work out..."
    s "...{i}aaand{/i} guys"
    s "Kind of like you ;)"
    "Alex's face turns completly red."
    show alex blushing
    a "Y..you like me?"
    s "Of course I like you. why wouldn't I."
    s "My heart beats fast everytime your near me."
    s "I actually wanted to confess first but you beat me at that"
    s "but Alex would you like to be my boyfriend?"
    "{i}Is this really happening. Dreams do come true.{/i} -Alex"
    a "I would love to"
    "Alex hugged sam tightly. Sam hugged him back"
    
    "GOOD END."
    return

label ignore :
    scene bg bedroom
    a "These feelings just happened today, probably tommorow they will be gone."
    a "Feelings come and go, right?"
    a "Why are these feelings growing stronger when I think of him"
    a "A guy liking a guy is wrong."
    a " why am I not normal"
   
    menu:
        a "What should I do?"
        
        "Keep it in":
            jump keep_it_in
        "Let it go (like Elsa)":
            jump elsa
            
label keep_it_in: 
    scene bg bedroom
    show alex sad
    a "These feelings aren't permanent"
    a "There is no way that I can be gay"
    a "Imagine me being gay.That would be terribe"
    a "No one would want to be my friend or my family might not accept me"
    a "I must get rid of these feelings"
    a "I MUST FORCE MYSELF TO HAVE FEELINGS FOR A GIRL"
    a "I should date Charlie and forget about Sam"
    "The next day in school"
    scene bg school
    show alex happy
    a "Where are you charlie"
    "Alex looked around looking for charlie and spotted her arriving to school"
    "Alex ran to Charlie"
    a "Hey Charlie!!"
    c "Hi Alex.Whats up?"
    a "I have something to ask you"
    c "Sure. I'm listening"
    a "Would you maybe want to be my girlfriend?"
    show charlie shocked
    "{i}Why all of a sudden. I don't want to ruin our friendship but if I reject him it can be the end of it.{/i} -Charlie"
    "{i}I shouldn't be using her. This was a bad idea and why did I say it all of a sudden.{/i} -Alex"
    show Charlie happy
    c "I would like to"
    "{i}I feel so bad for giving him fake hope.{/i} -Charlie"
    "{i}She should have said no. I'm not even her type{/i} -Alex"
    a "Want to hold hands?"
    c "okay"
    "Charlie and Alex held hands to school"
    "After School: Charlie and Alex went to hangout in the park to celebrate their first day as a couple"
    scene bg park
    "{i}Should I kiss him. Its only natural since were a thing now{/i} -charlie"
    "{i}Why is she closing her eyes? NNOO open them! Why is she leaning in?{/i} -Alex"
    "{i}I should lean in for the kiss too just to play along.{/i} - Alex"
    "Alex and Charlie kissed each others lips quickly and backed away from each other"
    "They opened their eyes to realize this was a mistake"
    show charlie sad
    "{i}I felt nothing at all. None of this has meaning. I'm sorry alex.{/i} -Charlie"
    "{i}Not even once my heart skipped a beat through that kiss it just felt wrong and I hated it{/i} -Alex"
    show alex sad
    "Alex started to burst in tears"
    a "I'm sorry"
    c "You shouldn't be sorry. I'm the one who gave you false hope when I agreed to date you when I actually felt nothing at all"
    a "I lied and used you to get rid of feelings I had for someone else"
    show charlie shocked
    a "Someone who i can't give my love to."
    c "Who is this someone, Alex"
    a "I can't say I perfer to keep this between me"
    show charlie sad
    c "ok. I respect you privacy"
    a "I need some alone time"
    "alex left charlie alone"
    "{i}I should give him space to think.{/i} -Charlie"
    a "My life's a mess"
    a "I used my best friend for my selfish pursposes"
    a "And I don't like girls"
    a "WHO AM I REALLY?"
    "BAD END"
    return
    
    
label Elsa:
    scene bg bedroom
    a "I should tell someone about my feelings"
    a "I need to let this go before it kills me inside"
    a "I need to tell someone"
    a "I should tell sam about my feelings for him"
    a "Or should i tell Charlie, well she is my bestfriend"
    a "But who will understand me better?"
    
    
    menu:
        a "Who should i tell?"
        
        "Tell Sam":
            jump say
        "Tell Charlie":
            jump tell
    
    
    
    
 
