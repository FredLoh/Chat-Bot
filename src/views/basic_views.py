from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import random
import unirest

def help(message, match):
    help_msg = "/ping, /echo <msg>, /about, /roll, /jasonsmith /europena"
    return TextMessageProtocolEntity(help_msg, to=message.getFrom())

def echo(message, match):
    return TextMessageProtocolEntity("%s" % match.group("echo_message"), to=message.getFrom())

def ping(message, match):
    return TextMessageProtocolEntity("Pong!", to=message.getFrom())

def about_me(message, match):
    return TextMessageProtocolEntity("My name is Boto-San!", to=message.getFrom())

def thank_you(message, match):
    s = u'❤'
    return TextMessageProtocolEntity(s, to=message.getFrom())

def roll(message, match):
    if(str(message.getParticipant()) == "17204742885@s.whatsapp.net"):
        return TextMessageProtocolEntity("[10]", to=message.getFrom())
    else:
        return TextMessageProtocolEntity("[%d]" % random.randint(1, 10), to=message.getFrom())

def meaning(message, match):
    return TextMessageProtocolEntity("42", to=message.getFrom())

def caracola(message, match):
    return TextMessageProtocolEntity("Nada", to=message.getFrom())

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
    random1 = random.randint(1, (len(firstphraselist)-1))
    random2 = random.randint(1, (len(secondphraselist)-1))
    random3 = random.randint(1, (len(thirdphraselist)-1))
    tweet = firstphraselist[random1] + " " + secondphraselist[random2] + " " + thirdphraselist[random3]
    return TextMessageProtocolEntity(tweet, to=message.getFrom())

def wisdom(message, match):
    sayings = [
    "A bird does not sing because it has an answer.",
    "It sings because it has a song.",
    "A bit of fragrance clings to the hand that gives flowers.",
    "A book holds a house of gold.",
    "A book is like a garden carried in the pocket.",
    "A book tightly shut is but a block of paper.",
    "A child's life is like a piece of paper on which every person leaves a mark.",
    "A diamond with a flaw is worth more than a pebble without imperfections.",
    "A filthy mouth will not utter decent language.",
    "A fool judges people by the presents they give him.",
    "A gem is not polished without rubbing, nor a man perfected without trials.",
    "A nation's treasure is in its scholars.",
    "A rat who gnaws at a cat's tail invites destruction.",
    "Be not afraid of growing slowly, be afraid only of standing still.",
    "Be the first to the field and the last to the couch.",
    "Deep doubts, deep wisdom; small doubts, little wisdom.",
    "Dig the well before you are thirsty.",
    "Do good, reap good; do evil, reap evil.",
    "Do not employ handsome servants.",
    "Do not fear going forward slowly; fear only to stand still.",
    "Do not remove a fly from your friend's forehead with a hatchet.",
    "A small fire is soon quenched.",
    "Intention of required study, the word worth a thousand gold.",
    "Bless never come both, and accidents never come alone.",
    "Those who jump off a Paris bridge are in Seine.",
    "A cardboard belt would be a waist of paper.",
    "Those who throw dirt are sure to lose ground.",
    "One dog barks at something, the rest bark at him.",
    "Man who places head in sand will get kicked in the end.",
    "Man who run in front of car get tired.",
    "Man who run behind car get exhausted.",
    "Man with one chopstick go hungry.",
    "Man who sinks into woman's arms soon will find arms in woman's sink.",
    "Wise man give wife upright organ.",
    "All men eat, but Fu Man Chu.",
    "If you want pretty nurse, you must be patient.",
    "Wife who put husband in doghouse soon find him in cathouse."]
    random1 = random.randint(1, (len(sayings)-1))
    tweet = sayings[random1]
    return TextMessageProtocolEntity(tweet, to=message.getFrom())

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
    random1 = random.randint(1, (len(quotes)-1))
    quote = quotes[random1]
    return TextMessageProtocolEntity(quote, to=message.getFrom())

def dollar(message, match):
    response = unirest.get("https://currency-exchange.p.mashape.com/exchange?from=USD&q=1&to=MXN",
      headers={
        "X-Mashape-Key": "I4B9Cp8wPHmshVHJhXiAp9NEJ3y1p19ivP6jsno27gIAERBir8",
        "Accept": "text/plain"
      }
    )
    return TextMessageProtocolEntity(str(response.body), to=message.getFrom())

def euro_pena(message, match):
    response = unirest.get("https://currency-exchange.p.mashape.com/exchange?from=EUR&q=1.0&to=MXN",
      headers={
        "X-Mashape-Key": "I4B9Cp8wPHmshVHJhXiAp9NEJ3y1p19ivP6jsno27gIAERBir8",
        "Accept": "text/plain"
      }
    )
    euro_value = str(response.body)
    response = unirest.get("https://currency-exchange.p.mashape.com/exchange?from=MXN&q=1&to= ",
      headers={
        "X-Mashape-Key": "I4B9Cp8wPHmshVHJhXiAp9NEJ3y1p19ivP6jsno27gIAERBir8",
        "Accept": "text/plain"
      }
    )
    peso_value = str(response.body)

    euro_huf = str(float(euro_value) * float(peso_value))

    response_String = "Euro: " + euro_value + "    Forint: " + peso_value + "    Euro-HUN: " + euro_huf
    return TextMessageProtocolEntity(response_String, to=message.getFrom())

def rana(message, match):
    return TextMessageProtocolEntity("*smegma", to=message.getFrom())
