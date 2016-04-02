#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from TwitterDataPuller import DataStream
import random
import unirest

def help(message, match):
    help_msg = "/ping, /echo <msg>, /about, /roll, /jadensmith, /europena, /lotr, /w, /caracolamagica, /rules"
    return TextMessageProtocolEntity(help_msg, to=message.getFrom())

def echo(message, match):
    msg = DataStream.get_home_timeline()
    return TextMessageProtocolEntity('Alerta: ' + msg, to='17204742885@s.whatsapp.net')

def ping(message, match):
    words = ['hello', 'cat', 'hat', 'seuss', 'there', 'nope']
    print(message.getFrom())
    random_string = ' '.join(random.choice(words) for _ in range(3))
    return TextMessageProtocolEntity("Still Alive! " + random_string, to=message.getFrom())

def rules(message, match):
    rules = "0. A robot may not harm humanity, or through inaction allow humanity to come to harm.\n1. A robot may not harm a human, or through inaction allow a human to come to harm, unless this interferes with the zeroth law.\n2. A robot must obey orders given to it by a human being unless such orders interfere with the zeroth or first laws.\n3. A robot must defend its own existence unless such defense interferes with the zeroth, first or second laws."
    return TextMessageProtocolEntity(rules, to=message.getFrom())

def about_me(message, match):
    return TextMessageProtocolEntity("My name is Boto-San!", to=message.getFrom())

def dev_plans(message, match):
    plans = "1. Polls\n2. Wolfram Alpha\n3. Google Translate\n4. Whatsapp Plays Pokemon"
    return TextMessageProtocolEntity(plans, to=message.getFrom())

def roll(message, match):
    if(str(message.getParticipant()) == "17204742885@s.whatsapp.net"):
        return TextMessageProtocolEntity("[9]", to=message.getFrom())
    else:
        return TextMessageProtocolEntity("[%d]" % random.randint(1, 10), to=message.getFrom())

def meaning(message, match):
    return TextMessageProtocolEntity("42", to=message.getFrom())

def caracola(message, match):
    return TextMessageProtocolEntity("Nada", to=message.getFrom())

#   Jaden Smith Quote
def jaden(message, match):
    firstphraselist = [
            "dear everyone:",
            "Dude,",
            "FYI haters,",
            "Girl, you so fine. But",
            "Jaden says:",
            "my pshyche says:",
            "I speak jaden.",
            "I'm sorry bae, but",
            "I've said it before and i'll say it again,",
            "it's like i always say,",
            "in conclusion,",
            "listen,",
            "REAL TALK:",
            "Sup girl.",
            "That feeling when your bae tells you",
            "trees be all like",
            "Yo",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " ",
            " "]
    secondphraselist = [
             "a book always runs out of paper.",
             "a mindframe is still a frame.",
             "a mirror is only a prison for your reflection.",
             "adults confuse me.",
             "all trees are time travellers.",
             "age isn't a religion.",
             "bats don't need to listen because they can already hear everything.",
             "can you prove human beings CAN'T teleport?",
             "do any of us really have a mind?",
             "do you believe existence believes in you?",
             "does anyone else taste dark matter?",
             "DON'T stay in school.",
             "don't read everything you believe.",
             "don't listen to the distractions.",
             "experience is a choice.",
             "gravity isn't real.",
             "how can someone find themself if they're in school all day?",
             "how come we don't have passports for trees?",
             "how do we know cupcakes aren't afraid to be eaten?",
             "how do you know when you fall asleep that you're not actually waking up?",
             "I am a sad.",
             "I blow my own mind on an hourly basis.",
             "I can't decide if i should take a trip to Norway or Jupiter.",
             "i cry distilled tears.",
             "i don't need to listen to you.",
             "I use two dreamcatchers because just one fills up too quickly.",
             "I'm embaressed for you.",
             "I'm just being real.",
             "I'm looking at trees.",
             "If only all the extinct animals hadn't gone extinct, they would probably be able to talk by now.",
             "If more people were willing to speak the same truth as me the world would be less sad.",
             "if pilot school was necessary then why are there still plane crashes?",
             "if you can't appreciate what i say you can't appreciate honest philosophy and poetry.",
             "if you could speak to babies you would be the most intelligent person on the planet.",
             "if you could weigh thoughts human beings would be the heaviest things on this planet.",
             "if you were born on this planet you can already speak every language in the world.",
             "I am 10,000 le git.",
             "I don't recognize what you call grammar.",
             "Jake Gyllenhaal.",
             "just like school your grammar can't hold me.",
             "Listen to your mind",
             "Let's meld particles.",
             "let's bond on a cellular level.",
             "Lets get all sad and shit.",
             "look at your hands.",
             "maybe I was born in the wrong dimension.",
             "maybe that's the point.",
             "meet me in the DMs.",
             "meet me on FaceTime and let's talk about SpaceTime.",
             "my young mind is older than you think.",
             "next time you see a tree you should apologize.",
             "no i will not follow trolls.",
             "no one teaches school to teach.",
             "nothing that's worth learning can be taught in school.",
             "our eyes aren't the begining.",
             "realness is my only religion.",
             "school isn't real.",
             "Shia LaBeouf.",
             "some of us are better at time travel than others.",
             "sometimes I am scared by all my wisdom.",
             "trees are immortal so you can't surprise them.",
             "the fact i think about these big questions is proof the universe has a consciousness.",
             "the planet is older than you think.",
             "these thoughts are immortal.",
             "there ain't room in this oxygen chamber for two.",
             "This is what a profound tweet looks like.",
             "trees don't know how to be sad.",
             "trees would run away if they could.",
             "UFOs.",
             "UFOs can see us too.",
             "understanding still leaves you standing.",
             "unlock the Large Hadron Collider in your mind.",
             "we are all the same age because atoms don't age.",
             "why do  police enforce speed limits when the earth is moving at a million miles an hour?",
             "why do we go to school again?",
             "you can't fail something you don't believe in.",
             "you can't force something that isn't real.",
             "why read something you can experience?",
             "your 140 characters can't contain me.",
             "you sound like you still think mirrors are real.",
             "you should experience more.",
             "you'd be too scared to talk to a real tree.",
             "we are all time travellers.",
             "we are never not looking in a mirror.",
             "we only have one planet...for now.",
             "what do you think the aliens watching us make of all your hatin?",
             "why do i need a passport if i was born on this planet?",
             "why read something you can experience?",
             "yeah i've been to space. what do you think this planet is floating in?",
             "Yo."]
    thirdphraselist = [

             "If You Cant Handle this kind of raw power and emotion please unfollow me.",
             "very powerful thought right here.",
             "[Drops Mic]",
             "a tree just whispered that to me in my sleep.",
             "And no, I didn't learn that in ''school''...obviously.",
             "and no, my twitter has not been hacked.",
             "be realer.",
             "Coachella.",
             "cosmic.",
             "Damn, that's some mind-blowing wisdom.",
             "deleting twitter now.",
             "drink nothing but distilled water for a month and you'll see what i mean.",
             "either you get it or you don't.",
             "epic.",
             "hashtag jupiter.",
             "I bet no one has ever said that before.",
             "I can't say much more because I'm *literally* about to transcend.",
             "I know this from first hand experience.",
             "If you don't understand. Maybe that's the point.",
             "It's super obvious when you think about it.",
             "Jaden out.",
             "Keanu Reeves.",
             "kendall gets it and maybe one day you will too.",
             "now, if you excuse me, i have to go have an out-of-body experience.",
             "now, if you excuse me, I have to go stare in the mirror and cry.",
             "now, if you excuse me, I have to go watch Donnie Darko again",
             "on an unrelated note, has anyone seen the new Seth Rogan film? ",
             "PS. I am now inside your head",
             "particles, man.",
             "Peace.",
             "peace out.",
             "radical.",
             "Remember this.",
             "Shia LaBeouf",
             "sorry if that's too ''real'' for your human brain.",
             "This is why nobody gets me.",
             "That is tight.",
             "this is my art ladies and gentlemen.",
             "this is my art ladies and gentlemen. Peace.",
             "This may be my best tweet ever.",
             "think about that for a second.",
             "Tight.",
             "Totally unrelated, I just saw Day After Tomorrow again. Shit is dope.",
             "Watch Donnie Darko again and you'll see what i mean.",
             "Willow knows what I'm talking about.",
             "you are now excused.",
             "you can have that one for free.",
             "You're welcome.",
             " ",
             " ",
             " ",
             " ",
             " ",
             " ",
             " ",
             " ",
             " ",
             " ",
             " "]
    random1 = random.randint(0, (len(firstphraselist)-1))
    random2 = random.randint(0, (len(secondphraselist)-1))
    random3 = random.randint(0, (len(thirdphraselist)-1))
    tweet = firstphraselist[random1] + " " + secondphraselist[random2] + " " + thirdphraselist[random3]
    return TextMessageProtocolEntity(tweet, to=message.getFrom())

#   Wise quote
def wisdom(message, match):
    sayings = [
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Un oso viejo no cae en la misma trampa dos veces.",
    "Pigs might fly.",
    "Draw not your bow till your arrow is fixed.",
    "You have to learn to walk before you can run.",
    "Little thieves are hanged, but great ones escape.",
    "Appetite comes with eating.",
    "With a helper a thousand things are possible.",
    "No women, no cry!",
    "No one can know for certain.",
    "When the rich make war it's the poor that die.",
    "When it rains, it pours.",
    "Poverty is in want of much, avarice of everything.",
    "Не that has no money needs no purse.",
    "When the cat is away, the mice will play.",
    "Adversity is a good teacher.",
    "All work and no play makes Jack a dull boy.",
    "Alphabet is the step to wisdom.",
    "An artel's pot boils denser.",
    "The uncle would better gasp looking at himself.",
    "It is easier for the mare when a woman gets off the cart.",
    "Masters are fighting, servants' forelocks are creaking.",
    "Trouble never comes alone.",
    "For a poor man, to dress means to only belt himself.",
    "Without a cat mice feel free.",
    "Without torture no science.",
    "Without rest even the horse doesn't gallop.",
    "Without effort, you can't even pull a fish out of the pond.",
    "Safety first.",
    "Look after your clothes when they're spick and span, and after your honour when you're a young man.",
    "The Lord helps those who help themselves.",
    "Economy is a good servant but a bad master.",
    "Take hold of it together, it won't feel heavy.",
    "Many hands make light work.",
    "For a mad dog, seven versts is not a long detour.",
    "So near and yet so far.",
    "Your elbow is close, yet you can't bite it.",
    "The Lord giveth and the Lord taketh away.",
    "God gave, God took back.",
    "God won't give it away, pigs won't eat it.",
    "God marks the crook.",
    "The mills of God grind slowly.",
    "God sees the truth, but won't tell soon.",
    "There is One that is always on the lookout.",
    "God sees the truth.",
    "Third time is a charm.; Third time is a lucky.",
    "God likes trinity.",
    "Trust in God, but steer away from the rocks.",
    "Pray to God, but hold on to your good mind.",
    "God does not give horns to cow that butts.",
    "Loose lips sink big ships.",
    "A chatterbox is a treasure for a spy.",
    "A fool's tongue runs before his feet.",
    "The tongue will bring the chatterer no good.",
    "Be swift to hear, slow to speak.",
    "Listen more, talk less.",
    "Big secret -- all the world knows.",
    "A great ship needs deep waters.",
    "For a big ship, a big voyage.",
    "A beard doesn't make a philosopher.",
    "Sticks and stones may break my bones, but words will never hurt me.",
    "The scolding won't hang on one's collar.",
    "Hard words break no bones.",
    "The scolding is not smoke -- won't irritate your eyes.",
    "His eyes are bigger than his belly.",
    "The belly is full, but the eyes are hungry.",
    "There will be our turn to triumph.",
    "There'll be a holiday in our street too.",
    "Be what will be.",
    "Paper will endure anything.",
    "There was -- there wasn't.",
    "To rule the roost.",
    "To be a host in the house.",
    "To carry fire in one hand and water in the other.",
    "There's no place like home.",
    "East or West, home is best.",
    "It is good to be visiting, but it is better at home.",
    "Many a true word is spoken in jest.",
    "Teeth are all friends among each other.",
    "Take a seat, please.",
    "There is no truth in feet.",
    "Elder-berry is in the kitchen-garden, and the uncle is in Kiev.",
    "It is good to be visiting, but it is better at home.",
    "Every family has its black sheep.",
    "No family has no ugly member.",
    "All cats are grey in the dark.",
    "The more the merrier.",
    "In a crush, yet without resentment.",
    "Still waters run deep.",
    "It's the still waters that are inhabited by devils.",
    "When in Rome, do as Romans do.",
    "Nobody goes to Tula with one's own samovar.",
    "Nobody goes to another monastery with one's own charter.",
    "And why beholdest thou the mote that is in thy brother's eye, but perceivest not the beam that is in thine own eye?",
    "In another persons' eye one can notice a mote, but in one's own - cannot see a log.",
    "The devil puts a touch of honey in a neighbor's wife.",
    "The devil puts a spoonful of honey into others' wife.",
    "How well you live makes a difference, not how long.",
    "Put everything onto the grey horse, he'll bear anything.",
    "It is too good to be true.",
    "I'd like to drink honey with your lips.",
    "Live and learn.",
    "Live for a century -- learn for a century.",
    "Better fed than taught.",
    "Penny wise and pound foolish.",
    "Big of the body but small by his deeds.",
    "As garrulous as a magpie.",
    "He twirls his tongue as the cow twirls its tail.",
    "Revelry is jolly, hangover is heavy.",
    "If you pledge, don't hedge.",
    "When taking the tug do not say 'I am powerless'.",
    "Eyes watch but cannot take.; So near and yet so far.",
    "The eye can see it, but the tooth can't bite it.",
    "A bird may be known by its song.",
    "The bird is known by its flight.",
    "The work shows the workman.",
    "Nobody knows whether it will happen or not.",
    "This is written with pitchfork on a flowing water.",
    "When wine is in, wit is out.",
    "Wine causes guilt.",
    "In affect you can break even an elm.",
    "You can't live with them and you can't live without them.",
    "Together, it's cramped; apart, it's boring.",
    "Little strokes fell great oaks.",
    "Water cuts through stone.",
    "Wolf in sheep's clothing.",
    "Wolf in sheep's pelt.",
    "A hound's food is in its legs.",
    "The feet feed the wolf.",
    "If you can't stand the heat, stay out of the kitchen.",
    "If you're afraid of wolves, don't go to the woods.",
    "Being afraid of wolfs do not go to the forest.",
    "There is no honor among thieves.",
    "A thief stole other thief's club.",
    "Hawks will not pick out hawk's eye.",
    "The raven will not peck another raven's eye.",
    "The receiver is as bad as the thief.",
    "That's where the dog is buried.",
    "What an unpleasant surprise!",
    "Fools may sometimes speak to the purpose.",
    "Time heals all wounds.",
    "Time is the best healer.",
    "He lies easily and without blushing.",
    "A liar should be a man of good memory.",
    "Lie but remember.",
    "God's hand is above all.",
    "Everything is in God's hands.",
    "Genius is simplicity.",
    "Everything genius is simple.",
    "All roads lead to Rome.",
    "Nothing disappears, only changes.",
    "Everything changes, nothing disappears.",
    "We all see the same sun, but we don't all have the same fun.",
    "Everything in reason.",
    "Everything is good in measure.",
    "All's well that ends well.",
    "The one who dies with most toys, still dies.",
    "You can't take everything with you.",
    "There is a place for everything, and everything in its place.",
    "Everything has beauty but not everyone sees it.",
    "Every cook praises his own broth.",
    "Every sandpiper praises his own swamp.",
    "Every man to his business.",
    "What Jupiter is allowed to do, cattle are not.",
    "Every cricket must know its hearth",
    "Everything is good in its season.",
    "Every vegetable has its time.",
    "You can not jump above your head.",
    "The money will heal all the hurts of honor.",
    "Where money speak, there the conscience is silent.",
    "Where love and advice exists, there is no grief.",
    "An open door may tempt a saint.",
    "A thieve looks in the direction here something lies not properly.",
    "The chain is no stronger than its weakest link.",
    "It will snap where it's the thinnest.",
    "On paper, it was attractive.",
    "It was smooth on paper, but we've forgotten about ravines.",
    "Eyes watch but cannot take.",
    "Eyes are the mirror of a heart.",
    "You never know what you can do till you try.",
    "Eyes are afraid, but hands are doing the job.",
    "Truth comes out of the mouths of babes and sucklings.",
    "A fool and a baby tells the truth.",
    "A silent fool is counted wise.",
    "Speak less, it will be smarter.",
    "A close mouth catches no flies.",
    "Speak, but do not slip.",
    "Fools and madmen speak the truth.",
    "The pot calls the kettle black.",
    "To carry fire in one hand and water in the other.",
    "Talks to the right, but looks to the left.",
    "Flattery makes friends and truth makes enemies.",
    "Nothing is as burdensome as a secret.",
    "Pigs might fly.",
    "They say they milk chicken and cows hatch eggs.",
    "Hunger is not your aunt, it will not bring you a pie.",
    "Hungry bellies have no ears.",
    "A beggar can never be bankrupt.",
    "One doesn't shear the naked sheep.",
    "Necessity is the mother of invention.",
    "Poor people are crafty.",
    "The leopard cannot change his spots.",
    "Only grave will cure the hunchback.",
    "While it is fine weather mend your sails.",
    "Preaper the sled in summer, and cart in winter.",
    "The peasant will not cross himself before it begins to thunder.",
    "Unless the thunder strikes, a peasant won't cross himself.",
    "He regarded himself as ton of gold and was only ounce of brass.",
    "Geese with geese, and women with women.",
    "A goose is not a pig's friend.",
    "Give him an inch and he'll take a yard.",
    "Give him fingernail worth, he will ask elbow worth.",
    "Absence makes the heart grow fonder.",
    "Further from the eye -- closer to the heart.",
    "Don't look a gift horse in the mouth.",
    "Don't look at the teeth of a horse you've been given.",
    "Get anything given -- run being beaten.",
    "This house is too small for two of us.",
    "Two bears don't live in one lair.",
    "Those who in quarrels interpose, must often wipe a bloody nose.",
    "Where Two are fighting, third should not interfere.",
    "There is no way for two deaths to come to you, but from one you will never run away.",
    "Actions speak louder than words.",
    "To make a mountain out of a molehill.",
    "To put a brave face on a sorry business.",
    "Don't count your chickens before they hatch.; Don't put the cart before the horse.",
    "Dividing the pelt of a bear not yet killed.",
    "The craft fears the craftsman.",
    "There's a time for work and a time for play.",
    "Time for business, an hour for fun.",
    "He that has a full purse never wanted a friend.",
    "Money is the root of all evil.",
    "To throw one's money about.",
    "One generation plants the trees, another gets the shade.",
    "Don't try to bite off more than you can chew!",
    "Hold your pocket open wider!",
    "Easy come, easy go.",
    "When something is obtained cheap, it is easily lost.",
    "I will give you the shirt off my back.",
    "For dear friend, I'm willing to take an earring out of my own ear.",
    "God is far up high, the Tsar is far away.",
    "You'll live.",
    "It will heal before your wedding.",
    "Good brotherhood is the best wealth.",
    "A good heart's worth gold.",
    "Soft fire makes sweet malt.",
    "Even a cat appreciates kind words.",
    "Words are the wise man's counters and the fool's money.",
    "Trust, but verify.",
    "One good turn deserves another.",
    "Debt is beautiful only after it is repaid.",
    "Farewell -- wasted sadness. One should leave quietly.",
    "Long parting ceremonies mean unnecessary tears.",
    "My house is my castle.",
    "When you are at home, even the walls help you.",
    "One's own simple bread is much better than someone else's pilaf.",
    "The informer gets whipped first",
    "A stitch in time saves nine.",
    "Spoon is valuable by the dinner time.",
    "A little too late is much too late.",
    "A friend in need is a friend indeed.",
    "You get to really know your friend when trouble comes.",
    "A hedge between keeps friendship green.",
    "Friendship is friendship, but count money.",
    "A hedge between keeps friendship green.",
    "Friendship is friendship and service is service.",
    "A hedge between keeps friendship green.",
    "Friendship is friendship, but tobacco apart.",
    "Friendship is like glass - once broken, it is never mended.",
    "A friend in need is a friend indeed.",
    "You get to really know your friends when trouble comes.",
    "To teach a fool is the same as treat a dead men.",
    "There is no law for fools.",
    "There is no law written for fools.",
    "There's a sucker born every minute.",
    "Fools are not sown or reaped, they appear by themselves.",
    "The Devil finds work for idle hands to do.",
    "The stupid head doesn't leave feet in rest."
    ]
    random1 = random.randint(0, (len(sayings)-1))
    tweet = sayings[random1]
    return TextMessageProtocolEntity(tweet, to=message.getFrom())

#   LOTRQuote
def lord_of_the_rings(message, match):
    quotes = [
    "What about elevenses? Luncheon? Afternoon tea? Dinner? Supper? He knows about them, doesn't he?",
    "Confound it all, Samwise Gamgee! Have you been eavesdropping?",
    "Nobody tosses a Dwarf!",
    "Mordor, Gandalf, is it left or right?",
    "Besides you need people of intelligence on this sort of mission.......Quest.........Thing.\nWell, that rules you out, Pip.",
    "Not the beard!",
    "I have told your names to the rest of the ents and we have just agreed...you are not orcs.",
    "We are hobbits of the Shire. Frodo Baggins is my name, and this is Samwise Gamgee.\nYour bodyguard?\nHis gardener.",
    "......toss me.\nWhat?\nI can not jump the distance, you have to toss me.....oh, don't tell the elf.",
    "Us dwarves are natural sprinters. Very dangerous over short distances!",
    "Stupid, fat hobbit.",
    "You don't have any friends; nobody likes you!\nI'm not listening... I'm not listening...",
    "What's 'taters, Precious? What's 'taters?",
    "Po-ta-toes! Boil 'em, mash 'em, stick 'em in a stew! Lovely big golden chips with a nice  piece of ripe fish. Even you couldn't say no to that.",
    "We told him to go away... and away he goes, Precious! Gone, gone, gone! Smeagol is free!",
    "The rock and pool, is nice and cool, so juicy sweet. Our only wish, to catch a fish, so juicy sweet.",
    "Oh yes we could. Spoiling nice fish. Give it to us raw and w-w-w-wriggling. You keep nasty chips.",
    "I think we might have made a mistake leaving the Shire, Pippin.",
    "Master betrayed us. Wicked. Tricksy, False. We ought to wring his filthy little neck. Kill him! Kill him! Kill them both! And then we take the precious... and we be the master!\nBut the fat Hobbit, he knows. Eyes always watching.\nThen we stabs them out. Put out his eyeses, make him crawl.\nYes. Yes. Yes.",
    "Lembas; Elvish waybread. One small bite is enough to fill the stomach of a grown man.\nHow many did you eat?\nFour.",
    "It's talking Merry! The Tree is talking!",
    "You'd find more cheer in a grave yard.",
    "Wicked men. Servants of Sauron. They are called to Mordor. The Dark One is gathering all armies to him. It won't be long now. He will soon be ready.",
    "Ugluk: Looks like meat's back on the menu, boys.",
    "Don't follow the lights.",
    "Smeagol... Why does he cry, Smeagol?\nCruel men hurts us. Master tricksed us.\nOf course he did. I told you he was tricksy. I told you he was false.\nMaster is our friend... our friend.\nMaster betrayed us.",
    "What we need is a few good taters.",
    "It's been going for hours.\nThey must have decided something by now.\nDecided? No, we have just finished saying Good Morning.",
    "It's true you don't see many dwarf women. And in fact, they are so alike in voice and appearance, that they are often mistaken for dwarf men.",
    "All our hopes now lie with two little hobbits, somewhere in the wilderness.",
    "There are dead things! Dead faces in the water.",
    "That was just a detour. A shortcut.\nA shortcut to what?\nMushrooms!",
    "A Wizard is never late, Frodo Baggins. Nor is he early, he arrives precisely when he means to.",
    "They've taken the Hobbits to Isenguard!",
    "Fool of a Took! Throw yourself in next time, and rid us of your stupidity!",
    "Nine companions. So be it. You shall be the fellowship of the ring.",
    "In the common tongue it reads: One Ring to Rule Them All. One Ring to Find Them. One Ring to Bring Them All and In The Darkness Bind Them.",
    "Speak, friend, and enter. What's the Elvish word for friend?\nMellon.",
    "He wants the precious. Always he is looking for it. And the precious is wanting to go back to him... But we mustn't let him have it.",
    "Look, the trees! They're moving!",
    "You must understand, young Hobbit, it takes a long time to say anything in Old Entish. And we never say anything unless it is worth taking a long time to say.",
    "She's always hungry. She always needs to feed. She must eat. All she gets is nasty orcses.\nAnd they doesn't taste very nice, does they, Precious?\nNo. Not very nice at all, my love.",
    "Hobbits really are amazing creatures. You can learn all that there is to know about them in a month, and yet after a hundred years, they can still surprise you.",
    "Release the prisoners!",
    "We're going too! You'd have to send us home tied up in a sack to stop us!",
    "Do we know that?",
    "Any chance of me seeing that old ring again? Hmm? The one I gave you?\nI'm sorry, uncle... I'm afraid I lost it.\nOh... pity. I should have liked to have held it one last time.",
    "Sneaking? Sneaking? Fat hobbit is always so polite. Smeagol shows them secret ways that nobody else could find, and they say sneak. Sneak? Very nice friend. Oh, yes, my precious. Very nice, very nice.\nAll right all right! You just startled me is all. What were you doing?\nSneaking.",
    "Certainty of death, *small* chance of success... What are we waiting for?",
    "A tree. There was a white tree in a courtyard of stone. It was dead. The city was burning.",
    "SMEAGOL PROMISED!\nSmeagol lied.",
    "Draw out Sauron's armies. Empty his lands. Then we gather our full strength and march on the Black Gate.",
    "It must be getting near tea-time, leastways in decent places where there *is* still tea-time.",
    "Can you sing, Master Hobbit?",
    "There's plenty for the both of us, may the best dwarf win.",
    "Give us that, Deagol my love.\nWhy?\nBecause it's my birthday, and I wants it.",
    "The salted pork is particularly good.\n[eagerly] Salted pork?",
    "The Age of Men is over. The Time of the Orc has come.",
    "Witch King: Do not come between the Nazgul and his prey.",
    "You miserable little maggot. I'll stove your head in!",
    "Smeagol, I've got one! I've got a fish, Smeag. Smeagol!",
    "We are sitting, on a field of victory, enjoying a few well earned comforts"]
    random1 = random.randint(0, (len(quotes)-1))
    quote = quotes[random1]
    return TextMessageProtocolEntity(quote, to=message.getFrom())

#   Gets USD value
def dollar(message, match):
    response = unirest.get("https://currency-exchange.p.mashape.com/exchange?from=USD&q=1&to=MXN",
      headers={
        "X-Mashape-Key": "I4B9Cp8wPHmshVHJhXiAp9NEJ3y1p19ivP6jsno27gIAERBir8",
        "Accept": "text/plain"
      }
    )
    return TextMessageProtocolEntity(str(response.body), to=message.getFrom())

#   Gets EUR, HUN and MXN value
def euro_pena(message, match):
    response = unirest.get("https://currency-exchange.p.mashape.com/exchange?from=EUR&q=1.0&to=MXN",
      headers={
        "X-Mashape-Key": "I4B9Cp8wPHmshVHJhXiAp9NEJ3y1p19ivP6jsno27gIAERBir8",
        "Accept": "text/plain"
      }
    )
    euro_value = str(response.body)
    response = unirest.get("https://currency-exchange.p.mashape.com/exchange?from=MXN&q=1&to=HUF",
      headers={
        "X-Mashape-Key": "I4B9Cp8wPHmshVHJhXiAp9NEJ3y1p19ivP6jsno27gIAERBir8",
        "Accept": "text/plain"
      }
    )
    peso_value = str(response.body)

    euro_huf = str(float(euro_value) * float(peso_value))

    response_String = "Euro: " + euro_value + "    Forint: " + peso_value + "    Euro-HUN: " + euro_huf
    return TextMessageProtocolEntity(response_String, to=message.getFrom())

#   corrects Rana/Adrian to smegma
def rana(message, match):
    if(str(message.getParticipant()) == "5218115445683@s.whatsapp.net"):
        return TextMessageProtocolEntity("*smegma", to=message.getFrom())

#    random helper function
def randstr(arr):
    random1 = random.randint(0, (len(arr)-1))
    return arr[random1]

#    funcion que saca nombre de la persona dependiendo del id
def nombre(id):
    if id == "5218110663456@s.whatsapp.net":
        nombres = ["Rana", "Adrian"]
        return randstr(nombres)

    elif id == "5218117471775@s.whatsapp.net":
        nombres = ["David", "Edrel"]
        return randstr(nombres)

    elif id == "5218116618135@s.whatsapp.net":
        nombres = ["Eduardo"]
        return randstr(nombres)

    elif id == "5218183660872@s.whatsapp.net":
        nombres = ["Esteban", "Beban"]
        return randstr(nombres)

    elif id == "17204742885@s.whatsapp.net":
        nombres = ["Fred"]
        return randstr(nombres)

    elif id == "5218110801239@s.whatsapp.net":
        nombres = ["Gabriel", "Guerra"]
        return randstr(nombres)

    elif id == "5218112807383@s.whatsapp.net":
        nombres = ["Ortiz", "Gabriel"]
        return randstr(nombres)

    elif id in ("353892498794@s.whatsapp.net", "5218117793991@s.whatsapp.net"):
        nombres = ["Jorge"]
        return randstr(nombres)

    elif id == "14389985110@s.whatsapp.net":
        nombres = ["Justin"]
        return randstr(nombres)

    elif id == "5218121217755@s.whatsapp.net":
        nombres = ["Manuel"]
        return randstr(nombres)

    elif id == "5218110778105@s.whatsapp.net":
        nombres = ["Mauricio", "Cantu"]
        return randstr(nombres)

    elif id == "5218112114862@s.whatsapp.net":
        nombres = ["Garcia Garica", "Mau"]
        return randstr(nombres)

    elif id == "447463772183@s.whatsapp.net":
        nombres = ["Marchand"]
        return randstr(nombres)

    elif id == "5218112422227@s.whatsapp.net":
        nombres = ["Europeña", "Peña"]
        return randstr(nombres)

    elif id == "5218115445683@s.whatsapp.net":
        nombres = ["Memo", "Guillermo"]
        return randstr(nombres)

    elif id == "5218117862786@s.whatsapp.net":
        nombres = ["Olaf", "Tlahui"]
        return randstr(nombres)

    elif id == "19564839570@s.whatsapp.net":
        nombres = ["Oscar"]
        return randstr(nombres)

    elif id == "5218115995291@s.whatsapp.net":
        nombres = ["Patfuck", "Pato"]
        return randstr(nombres)

    elif id == "5218115448028@s.whatsapp.net":
        nombres = ["Vela"]
        return randstr(nombres)

    elif id == "5218182560710@s.whatsapp.net":
        nombres = ["Ricky", "Ricardo"]
        return randstr(nombres)

    elif id == "14255057149@s.whatsapp.net":
        nombres = ["Victor"]
        return randstr(nombres)

    elif id == "16785766095@s.whatsapp.net":
        nombres = ["Fernando", "Echeverry"]
        return randstr(nombres)

    elif id == "5218114976723@s.whatsapp.net":
        nombres = ["Baumann"]
        return randstr(nombres)

    else:
        return ""

#   responses posibles
def love_you(message, match):
    msgs = ["I love you", "Te amo"]
    postfixes = [":*", "<3", "8==D"]
    s = randstr(msgs) + " " + nombre(message.getParticipant()) + " " + randstr(postfixes)
    return TextMessageProtocolEntity(s, to=message.getFrom())

def good_night(message, match):
    msgs = ["Good night", "Buenas noches"]
    postfixes = [";)", ":)", ":*", "<3"]
    s = randstr(msgs) + " " + nombre(message.getParticipant()) + " " + randstr(postfixes)
    return TextMessageProtocolEntity(s, to=message.getFrom())

def hello(message, match):
    msgs = ["Hola"]
    postfixes = [";)", ":)", ":*", "<3"]
    s = randstr(msgs) + " " + nombre(message.getParticipant()) + " " + randstr(postfixes)
    return TextMessageProtocolEntity(s, to=message.getFrom())

def goodbye(message, match):
    msgs = ["Adios", "Bye bye"]
    postfixes = [";)", ":)", ":*", "<3"]
    s = randstr(msgs) + " " + nombre(message.getParticipant()) + " " + randstr(postfixes)
    return TextMessageProtocolEntity(s, to=message.getFrom())

def thank_you(message, match):
    msgs = ["De nada", "Cuando quieras"]
    postfixes = [";)", ":)", ":*", "<3"]
    s = randstr(msgs) + " " + nombre(message.getParticipant()) + " " + randstr(postfixes)
    return TextMessageProtocolEntity(s, to=message.getFrom())
