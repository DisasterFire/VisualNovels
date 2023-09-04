# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mw = Character("Laura Varkus")

define mx = Character ("Kara Kenton")

define jhm = Character ("John Marks")

define rc = Character("Receptionist")

define pm = Character("Paul Mannings")

define ft = Character("Francis Ticonderoga")

define gm = Character("Gustavo Marcus")

define ahv = Character("Automated Voice")

define mcc = Character("Monarch Call Center")

define cm1 = Character("Cartel Member #1")

define cm2 = Character("Cartel Member #2")

define cl = Character("Client")

define mv = Character("Mysterious Voice")

define asshole_pts = 0

define wallet = 0

define evidence_check = 3

define blood_sample = 0
define match_book = 0
define fabric_piece = 0
define all_evidence = 3

define blood_examine = 0
define match_examine = 0
define fabric_examine = 0
define fabric_content = 0

define smelled = 0
define chewed = 0
define burned = 0
define cut = 0
define linked_name = 0

define hush_money = 0
define arrest = 0
define scorched_earth = 0

define therapy = 0

define run_gus = 0
define run_jon = 0

define call_2 = 0

define frantic_life = 3

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg office

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    show maslow base

    "Sunday, November 3rd. 4:20 P.M. 2 days before Election Day."

    "Grimhel is falling apart. "

    "Half the population wants to suck up to those suits at Monarch."

    "The other half, well, they want all the superhumans out of here."

    "On two ends of this political clusterfuck are the candidates:"

    "One who wants superhumans, specifically Monarch-branded superhumans, in the military."

    "And the other one who wants them gone for good."

    "Kara, my love, I hope that we can both get out of here safely."

    "The sharp ring of a vintage phone fills the dead silence"

    show paul base

    pm "Hey Laura, I just wanted to check in. How are you doing?"

    menu:

        "Act Aggressively":

            mw "Paul, this is my business line, please just cut to the chase here."

            pm "Laura? Have you been checking in with your counselor lately?"

            menu:

                "Assert that this is the professional line":

                    mw "Paul, as I said. Business calls on the professional line only."

                    mw "If you need to talk to me about literally anything else...call my fucking personal line."

                    mw "I told you about that when you were first recommended to me."

                    pm "Fine fine, I'll stop pushing."

                    jump casework

                "Tell him the truth.":

                    mw "It hasn't been working out Paul."

                    pm "What do you mean?"

                    mw "It's been coming out of me again..."

                    pm "You mean...?"

                    mw "Yeah...With all of the rising tension, I can feel their urges coming back to me."

                    pm "Oh god...that sounds terrible."

                    pm "Have you been able to stay sober?"

                    mw "Paul...the shit I saw with Project Anubis, you need to drink heavily to forget that ever happened."

                    mw "The bodies that were buried that day..."

                    pm "Laura, the point of therapy is to try and work through these issues, not try and forget they ever existed."

                    menu:

                        "Work through these issues":

                            mw "Fine...I know that the courts mandated this whole relationship, but fine."

                            mw "Doesn't change the fact that I can never unsee what I saw, but whatever."

                            mw "For the sake of the courts and my old bosses, I'll humor you."

                            $ therapy += 1

                        "Brush it off":

                            mw "Spoken like someone who hasn't seen shit."

                    jump casework

        "Act Casually":

            mw "You know, things are going the way they have been for some time."

            pm "Have you been keeping notes in your journal."

            mw "Almost daily. It's been incredibly helpful."

            mw "Actually, me and Kara have been working on doing journals together, it's been really helpful for the two of us."

            pm "I'm glad to hear things are going smoothly."

            jump casework

    label casework:

        pm "Look, anyways, I have a new client who says they need your help in an investigation."

        mw "What kind?"

        pm "Homicide. It's pretty brutal."

        mw "Can you give me any more details?"

        pm "And break attourney-client privilege? I'm afraid not."

        pm "However my client has informed me that a letter is on its way to your office."

        mw "Yeah, I think I saw something like that in the mail when I came in today."

    label whyTheyCalled:

        menu:

            "Ask about why he called you":

                mw "Now I gotta wonder, why do they want me?"

                mw "Can't they go to Grimhel PD for this?"

                pm "Afraid not. Apparently the client worries about the departments 'conflict of interest' with the case."

                pm "They said something about involvement by Monarch Labs."

                mw "Damn, I bet the lab techs already tried cleaning it up."

                pm "Yeah, law enforcement has fuck all in terms of records on this case. Something's definitely up with that."

            "Continue asking about case details":

                mw "Well is there anything else you can tell me?"

                pm "Well first off, the crime took place in an alleyway on Morrison St. Gonna need you to check that out."

                menu:

                    "Be snarky about it":

                        mw "And? Should I just look around there?"

                        pm "No, dumbass. I need you to also be collecting evidence."

                        pm "Do you not know how the legal system works?"

                    "Go along with it":

                        mw "I'll be sure to also keep any clues I find."

                        pm "Of course. And if you could bag that up for me that would be fantastic."

    mw "By the way, you might be getting paid legal fees, but I also need my due here."

    pm "I remember, Laura. I've factored the cost on my end. You're taking 40%%."

    menu:

        "Alright. A deal's a deal Paul. I'll check it out.":

            jump aDealIsADeal

        "No. We're in this 50/50. I want a cut":

            jump iWantMore

    label aDealIsADeal:

        mw "Alright. Sounds fair. I'll look into it"

        pm "Thanks for doing this, Laura. You're a good friend"

        jump investigation

    label iWantMore:

        $ asshole_pts += 1

        mw "No Paul. When we entered this business we agreed to be partners."

        pm "I'm already eating a lot of cost here. Do you know how much I've had to lower fees to compete with big name legal here in Grimhel?"

        pm "Too much. I'm barely making a living here."

        mw "Me neither. We're both losing here."

        pm "Fine. 50/50. Now get to solving the case...asshole"

        mw "Love you too, Paul"

        jump investigation

    
    label investigation:

        hide paul base

        "Well, I'd better check out this letter. It'll be a good idea to see what I'm working with."

        show letter 

        cl "Dear Offices of Laura Varkus,"

        cl "I come to you bearing horrible news...my brother is dead, and I suspect it wasn't just a mistake."

        cl "I have been speaking with your partner attorney trying to build a case against whoever did this, but everything is such a blur."

        cl "All I know is that one night, he went out to meet up with some friends but come the next morning...he never returned."

        cl "I searched all over Grimhel, fearing that the worst had happened, and what I saw was even more terrifying..."

        cl "Whoever is responsible must face the consequences, and while I may not know you, I trust Mr. Mannings' word on you."

        cl "Please detective. My brother deserves justice."

        hide letter

        "Jesus Christ...well then I guess Morrison St. it is."

        jump crimeScene

    
    label crimeScene:

        scene bg morrison

        show maslow base

        "Eugh...this alley reeks of rotting flesh."

        "Great, the body is missing too. Looks like the law caught up to the situation first."

        "At least with the funding they're getting, Crime Scene Investigation should do a little better housekeeping here."

        "I can make out a few things: A pool of blood, a random matchbook, and a stray piece of fabric."

        jump firstEvidence

    label firstEvidence:

        menu:

            "Examine blood" if blood_sample == 0:

                $ blood_sample += 1

                $ all_evidence -= 1

                "Hmm..thankfully I have something on my person to store the blood in, but I can probably do fuck all with it."

                "Looks murkier than normal...like there's something different about this blood sample."

                if all_evidence > 0:

                    "There's still some more evidence to look at, should I do so?"

                if all_evidence == 0:

                    "Well, there's nothing left, what should I do now?"

                menu:

                    "Look for more clues" if fabric_piece == 0 or match_book == 0:

                        jump firstEvidence

                    "Head back now" if all_evidence == 0:

                        scene bg office

                        show maslow base

                        "Well, let me look at the evidence I've gathered and see if I can draw anything from them."

                        jump examination

            "Pick up matchbook" if match_book == 0:

                $ match_book += 1

                $ all_evidence -= 1

                "Matchbooks can usually tell a lot about someone...or at least they used to."

                "Question is...why in the hell would someone use one today?"

                "Oh well, let's check it out."

                "Hmm..."

                "Monarch Liquor-branded matches. Strange. I didn't even think that company even made matches, but that's odd."

                if all_evidence > 0:

                    "There's still some more evidence to look at, should I do so?"

                if all_evidence == 0:

                    "Well, there's nothing left, what should I do now?"

                menu:

                    "Look for more clues" if blood_sample == 0 or fabric_piece == 0:

                        jump firstEvidence

                    "Head back now" if all_evidence == 0:

                        scene bg office

                        show maslow base

                        "Well, let me look at the evidence I've gathered and see if I can draw anything from them."

                        jump examination


            "Examine Fabric" if fabric_piece == 0:

                $ fabric_piece += 1

                $ all_evidence -= 1

                "Strange...this isn't like normal fabric at all."

                "It's stretchy...rubbery, yet also seemingly very tough."

                "Colored bright yellow too...I wonder who this could have belonged too"

                if all_evidence > 0:

                    "There's still some more evidence to look at, should I do so?"

                if all_evidence == 0:

                    "Well, there's nothing left, what should I do now?"

                menu:

                    "Look for more clues" if blood_sample == 0 or match_book == 0:

                        jump firstEvidence

                    "Head back now" if all_evidence == 0:

                        scene bg office

                        show maslow base

                        "Well, let me look at the evidence I've gathered and see if I can draw anything from them."

                        jump examination

    label examination:

        menu:

            "Compare the blood sample" if blood_sample == 1:

                $ blood_sample -= 1

                $ blood_examine += 1

                "Maybe if I examine some of my own blood, I can figure out if something is weird"

                "Let me just pull out a knife..."

                "...there we go"

                "Hmm..."

                "That's strange. The coloration on this blood is much darker than my own."

                "And there's other flecks of color in it too...what the fuck?"

                "Maybe the coloration could be because of how long the blood's oxidized..but there's something off about the sample."

                "What should I do?"

                menu:

                    "Call Paul. Maybe he has an answer." if asshole_pts != 3:

                        jump callPaulBlood

                    "Look through the other evidence.":

                        jump examination

                jump conclusions

            "Read Matchbook" if match_book == 1:

                $ match_book -= 1

                $ match_examine +=1

                "A Monarch Liquor-branded matchbook. Now what kind of deranged kiss-ass would want to use these?"

                "Maybe the inside of it will have some more clues..."

                "Hmm..."

                "There's a couple phone numbers in here. One of these has to have a lead, but should I call? or ask Paul first?"

                menu:

                    "Call Paul":

                        jump callPaul

                    "Call the matchbook number":

                        jump callMatch

                    "Look through the other evidence":

                        jump examination
                    

            "Closely examine fabric" if fabric_piece == 1:

                $ fabric_piece -= 1

                $ fabric_examine += 1

                "I keep testing it like earlier...it's super stretchy...yet seems incredibly durable"

                "What can I do to keep testing this?"

                jump selfTestFabric

            "Call Paul":

                "I guess I'd better call Paul. He might have some answers."

                jump callPaul

        label selfTestFabric:

            menu:

                "Light a match" if burned == 0:

                    $ burned += 1

                    $ fabric_content += 1

                    "Taking one of the matches out of the matchbook should be useful to seeing if this burns easily"

                    "The match is struck against the table, lighting the flame. What an odd color..."

                    "Oh well...anyways"

                    "I put the match up to the fabric and...well"

                    "it catches fire...but it isn't burning"

                    "Guess I should put it out now, but...weird"

                    if cut == 1:

                        "Extremely durable and can't easily be burned..."

                    "Anyways, what else should I do with it?"

                    jump selfTestFabric

                "Put a knife up to it" if cut == 0:

                    $ cut += 1

                    $ fabric_content += 1

                    "I try whatever I can with this freakin knife"

                    "Stabbing, cutting, whatever"

                    "Nothing is making a dent here."
                    
                    if burned == 1:
                        
                        "Hyper durable..."

                    if burned == 0:

                        "Hyper durable and flame resistant..."

                    "What else can I do to test this?"

                    jump selfTestFabric

                "Bite it" if chewed == 0:

                    $ chewed += 1

                    $ fabric_content += 1

                    "Rubbery, chewy...very leathery."

                    if burned == 1:

                        "Eugh...the flavor profile is all burnt"

                    "Wait a minute...this druggy aftertaste...I recognize that"

                    "It's speed..."

                    "Interesting, but what else can I do?"

                    jump selfTestFabric
                    
                "Smell it" if smelled == 0:

                    $ smelled += 1

                    $ fabric_content += 1

                    if burned == 1:

                        "Welp...smells like matches and burned...that's for sure."

                    if chewed == 1:

                        "Hmm....ew, and my coffee breath too. Disgusting"

                    "Wait a minute...I recognize this smell."

                    "It's a combination of sweat, dirt, and drugs..specifically the drugs pouring out of the sweat."

                    "More information, but what to do with it all?"

                    jump selfTestFabric

                "Look over the other evidence":

                    jump examination

        label callPaulBlood:

            "The phone is dialing..."

            hide maslow base

            show phone

            rc "Offices of Paul Mannings, Grimhel independent attorney at law"

            mw "Hi there, I'm looking to talk to Paul Mannings."

            rc "Okay, and are you a client wanting to talk about an appointment."

            if asshole_pts == 0: 
            
                mw "No. Tell Paul that Detective Varkus is on the line and needs to speak with him."

                rc "Okay. I'll forward you to him right now"

                "The line is busy...sounds like he's in a meeting. Oh well. I'll wait."

                "Waiting..."

                "Still waiting..."

                hide phone

                show paul base

                pm "This is Paul Mannnings calling. How can I help you?"

                mw "It's Laura. I have some updates from the investigation."

                pm "Oh really? What did you find?"

                mw "Blood samples. This one I got looks weird compared to what I have-"

                pm "Wait what? How did you compare blood samples?"

                mw "I cut my arm open to see."

                pm "Laura...you can't do this to yourself. Seriously, don't go off the rails...again. Take care of yourself."

                mw "Fine..but this is still super weird."

                pm "Exactly how is the blood 'weird'"

                jump paulBlood

                

            if asshole_pts == 1: 
                
                mw "Tell Paul its his mother calling. She wants to speak with him about his time in Connecticut."

                rc "Alright, he'll answer right away Mrs. Mannings."

                "Welp...I get connected quickly. Guess my con worked."

                hide phone

                show paul base

                pm "Mom, what the hell did my friends tell you. Nothing happened in Connecticut I swear-"

                mw "Realx Paul, it's just me."

                pm "Dick move, Laura."

                mw "Well it got you to pick up the phone so-"

                pm "Can it, dipshit. What do you want?"

                mw "I found a blood sample at the crime scene. Looks weird and not like my own blood."

                pm "Okay...super weird but what did you find?"

                jump paulBlood


        label paulBlood:

            $ blood_examine -= 1

            mw "Well, the sample's very discolored and there's all these different flecks of colors in it."

            pm "Look...I may not be the expert here, but I have a friend downtown who works in a Forensics lab."

            mw "Forensics? Aren't they backed by-"

            pm "Yeah I know...unfortunately we can't avoid Monarch Labs here. It's inevitable."

            mw "They've somehow managed to get themselves into every nook and cranny possible in this shithole."

            pm "Look Laura, sometimes you have to accept that this is going to happen whether you like it or not..."

            mw "Paul...what happened?"

            pm "Monarch lawyers came to my office, said they were interested in becoming partner. It would seriously help business for me."

            mw "Paul...you can't take that offer. We're the last few honest people untouched by-"
            
            pm "I'm still going over the offer. It's pretty shady, but honestly with the way my office has been tanking, it's not a bad offer."

            menu:

                "Convince him he's wrong.":

                    $ asshole_pts += 1

                    mw "Don't take it. Don't even consider it."

                    pm "Laura, my business is failing. I can't afford to keep my doors open much longer."

                    mw "It's not about the money, Paul. Your integrity is at stake."

                    pm "Who gives a fuck about integrity when I'm barely keeping everything together trying to survive."

                    pm "Just back off about this, now or else I'm dropping you from the case."

                    mw "What?"

                    if asshole_pts == 2:

                        pm "You've been a dick to me ever since I called asking for your help."

                        mw "Well I want to be treated equally here."

                        pm "I want us to be equal too, but right now I can barely afford to make that work."

                        pm "I need to take the offer from Monarch's legal team. It's the only thing that will let me make things better."
                        
                        mw "You know, I thought better of you Paul."

                        mw "I really thought we could do this on our own."

                        hide paul base

                        "There's a long silence..."

                        "...he's not responding"

                        show maslow base

                        mw "Paul...?"

                        hide maslow base

                        show paul base

                        pm "I really thought you were my friend Laura."

                        pm "I'm taking the deal whether you like it or not. You can keep working the case, but you're on your own now."

                        pm "Goodbye Laura..."

                        hide paul base

                        show maslow base

                        "The phone then hangs up"

                        menu:

                            "Didn't need that spineless idiot anyways":

                                $ asshole_pts += 1

                                "Oh well, I'd better get back to investigating the evidence"

                                jump examination

                            "Maybe I'm the asshole here?":

                                $ asshole_pts -= 1

                                "Maybe I should apologize to Paul..."

                                "Dialing"

                                hide maslow base

                                show paul base

                                pm "What now?"

                                mw "Look, I'm about to get back into investigation, but I wanted to say I'm sorry for reacting the way I did."

                                mw "It was completely uncalled for...especially consideringt the situation right now."

                                pm "I forgive you Laura. Do you need anything else?"

                                mw "No, I was just about to go back into examinations again. I'll give you a call when I get more information"

                                pm "Alright then, take care"

                                hide paul base

                                show maslow base

                                "He hangs up."

                                "Guess I better get back to work."

                                jump examination

                    if asshole_pts == 1:

                        pm "You can't keep pushing people like this Laura, especially if we're friends here."

                        mw "Think about it though. Something about this situation isn't right. We can't get Monarch involved here."

                        pm "Maybe you're right, but I'm barely managing to scrape by here."

                        menu:

                            "Talk about your problems.":

                                mw "What about me, Paul? Therapy hasn't been working out."

                                pm "...It sounds like it"

                                mw "Me and Kara are planning a big move out of Grimhel as soon as we can."

                                mw "I'm saying that I am barely making a living here as well."

                                pm "You're right, but what about me too?"

                                pm "You're not the only one with people to take care of."

                                pm "I've been taking care of the kids...not to mention dealing with Jack's family knocking on my door..."

                                mw "What? What have they been doing?"

                                pm "Jack's dad still blames me for...everything that happened to him."

                                menu:

                                    "What happened?":

                                        mw "What happened with Jack?"

                                        pm "Supposed car accident off the highway."

                                        pm "Foul play had been suspected, but law enforcement dropped the case when they realized there were Monarch connections."

                                        pm "Now Jack's dad never liked me, but...this incident really hurt him."

                                        pm "He says I dragged him down with me."

                                        pm "He refuses to even see his granddaughter."

                                        mw "Poor Melissa..."

                                        pm "Melissa's really the one being hurt by all of this."

                                        pm "With me working all the time to keep us afloat and her other father gone...I wonder how she manages to keep such a big smile on her face everyday."

                                        mw "She's a fighter, just like you Paul."

                                        pm "I don't know how much fight in me I have left."

                                    "Continue talking.":

                                        mw "I'm sorry to hear that...must be rough. I hope Melissa's doing okay."

                                        pm "She really is. That damn smile keeps me going."

                            "Defend the client.":

                                mw "Maybe so, but don't we owe it to ourselves to keep trying, for the client?"
                                
                                pm "What do you mean?"

                                mw "I mean, if the problem here is abuse of power, this case could set a precedent."

                                pm "You're saying?"

                                mw "What I'm saying is, this investigation could bring a truly evil monster to justice."

                                mw "With all that is going on in the city, we owe it to the people to do this."

                                pm "I mean...you're right but-"

                                menu:

                                    "Tell him he's wrong":

                                        mw "No buts. We have to do this."

                                        pm "Why?"

                                        mw "Because if I fail this case then I fail my reason for being here."

                                        mw "Do you know why I got into this business?"

                                        pm "Why?"

                                        mw "Because of this one day back in 5th grade when my best friend went missing."

                                        pm "Oh no..."

                                        mw "After two weeks, the search was given up."

                                        mw "Police were more concerned with finding a body than with catching who's responsible."

                                        mw "And when they did find the man responsible, he was let off with a light sentence because of his father's connection to Monarch Labs."

                                        pm "Oh my god..."

                                        mw "Since then all I've felt for Monarch was nothing."

                                        mw "For all i care, they could die in a fire because of what they did to my best friend."

                                        mw "That's why I want justice at all costs. Because you never know how deep these problems are rooted."

                                        pm "I see what you mean, but my point still stands. I have to take this deal. I'm in a tight spot right now and I can't afford to lose anything here."

                                        mw "Fine. Then take the deal, but I will keep working this case."

                                        pm "Why would you do that?"

                                        mw "Because, I believe in finishing what I started."

                                    "Hear Paul out":

                                        pm "Remember back in 2023 when you were just starting out?"

                                        mw "Yeah...Grimhel was a whole different kind of bad then."

                                        pm "Look, you had just been discharged by your commanding officer and I had been assigned to monitor your progress as the agency felt like your behavior was 'beyond concerning'"

                                        mw "Right...you were pretty much just there to make sure I didn't leak government secrets."

                                        pm "Maybe for a time, yes, but I wanted you to be able to heal after all of the things I heard."

                                        pm "Grimhel's underworld may not have been the best place to vent your anger, but I knew it would keep you out of 'annoying bureaucracy' as you referred to it."

                                        mw "The private sector was always prime for business."

                                        pm "I felt like the best way for you to heal would be to keep some distance, but still be within arms reach."

                                        pm "Since your skills with detective work were unmatched, I figured why the fuck not."

                                        mw "What does this have to do with solving the case?"

                                        pm "I'm getting there."

                                        pm "Our first case we worked...the revenge plot?"

                                        mw "I remember that..."

                                        pm "The man was being charged with physical assault, but do you remember the notes you took?"
                                        
                                        mw "Hold on...I need to refer to the journal archive."

                                        mw "Hmmm..."

                                        mw "May 3rd, 2023: my first case is coming to an end."

                                        mw "Seems fairly open and shut. Physical assault and battery. Perpetrator is clearly in the wrong."

                                        mw "...but something seems off about the whole ordeal."

                                        mw "Nothing seemed right about what happened."
                                        
                                        pm "And then it hits you..."

                                        mw "So I did some digging and realized that..."

                                        mw "The man had apparently lashed out at this young man because he had killed his dog."

                                        mw "...retaliation for a crime comitted against him"

                                        mw "What's your point?"

                                        pm "My point is we can't expect ourselves to be purely good all the time."

                                        pm "We need to find the gray areas where we can really help those that need our help."

                                        mw "I see what you're getting at now."

                                        pm "You do?"

                        mw "Take the deal and do what Monarch asks of you, but I will still work this case after hours."

                        mw "We have to get to the bottom of this, for your client."

                        pm "Right."
                        
                        mw "Remember, justice at all costs."

                        pm "Yeah...I'll talk to you soon Laura. Call me if you have any updates."
                        
                        mw "Will do Paul."

                        hide paul base

                        show maslow base

                        "He hangs up the phone"

                        "What do I do now?"

                        menu:

                            "Call the matchbook number" if match_examine == 1:

                                jump callMatch

                            "Look back at the evidence":

                                jump examination

                "Let it go":

                    mw "Alright Paul. It's probably best you make this decision yourself."

                    pm "Thank you. I appreciate your respect."

                    menu:

                        "Trust Paul":

                            mw "Your gut has helped us so many times in the past. I'm going to trust you to make the right decision here."

                            mw "Remember that time you helped out me and Kara?"

                            pm "Yeah, right. You were talking about needing a roomate for your apartment or something and my spouse at the time said that they knew somebody new to town looking for an apartment."

                            mw "And then you set us all up for some kind of dinner or what not."
                            
                            mw "I was really skeptical at first, but honestly after meeting her, something just clicked."

                            pm "And then Jack's telling me all about how you and Kara have been hanging out a lot more."

                            pm "How Kara's going on and on about how much of a wonderful person you are."

                            if asshole_pts >= 1:

                                pm "Something that I don't see in our interactions."

                            pm "And then one day you tell me that it's been your 1 year anniversary with Kara."

                            pm "How did we ever get here."

                            mw "I don't know Paul, but if there's one person to thank, it's your husband."

                            pm "Hey!"

                            mw "...and if there's another one, it's you Paul."
                            
                            pm "There we go."

                            mw "Moral of the story: I trust your judgement here."

                            pm "I trust yours as well."

                        "Question his decision":

                            mw "Still though, are we doing the right thing here?"

                            pm "Look, between upholding the firm, paying my bills, and taking care of my daughter, I have to take this."

                            pm "That money could probably keep me aloat until I find my bearings again."

                            menu:

                                "Ask about his daughter":

                                    mw "Oh by the way, how is Melissa doing?"

                                    pm "She's been doing wonderful. She just started 4th Grade."

                                    mw "4th Grade? Wow, it's been so long. It feels like yesterday that me and Kara were celebrating her 5th birthday with you all."

                                    pm "Yeah, she is adorable. Light of my life honestly."
                                    
                                    pm "And while the past year has been hard on both of us, she's still managing to make it through with the biggest smile that I've ever seen."

                                    mw "Yeah, she's so adorable."

                                "Confront him about Monarch.":

                                    mw "But you know what Monarch did to Kara..."

                                    pm "I am well aware of Kara's relationship with Monarch."

                                    mw "They wanted her to be something she wasn't."

                                    mw "Kara's powers are something that she deeply regrets and fears."

                                    mw "Monarch thought that turning her into some flashy, powerful icon would be beneficial."

                                    mw "I've talked to her several times, and hearing about all of the things that lab techs did was gut-wrenching."

                                    mw "All Kara ever wanted was just a quiet, normal life where she could be herself."

                                    mw "Away from Monarch's influence, away from everything, and where did she find it?"

                                    pm "Where?"

                                    mw "She found it with me. Safety, comfort, identity, whatever."

                                    mw "I can't let you get Monarch involved because of this."

                                    mw "But I also recognize that you need to do what's best too, for your family."

                            mw "I'm sorry about the situation, Paul."

                            pm "Me too..."

                    mw "Oh wait...one more thing!"

                    pm "Yeah?"

                    menu:

                        "Mention the matchbook numbers" if match_examine == 1:

                            mw "I found this Monarch Liquor-branded matchbook at the scene."

                            pm "Huh, weird. Anything about them you found interesting?"

                            jump paulMatches

                        "Mention the fabric" if fabric_examine == 1 and fabric_content == 4:

                            jump paulFabric

                        "Nevermind":

                            mw "Nothing. I'll call if I need anything though."

                            pm "Okay. My line should be open then."

                            mw "Thank you."

                            mw "Goodbye Paul."

                            "The line hangs up"

                            "Anyways, what should I do now?"

                            menu: 

                                "Go back to the evidence":

                                    jump examination

        label callPaul:

            "The phone is dialing..."

            hide maslow base

            show phone

            rc "Legal Offices of Paul Mannings. How can I help you?"

            mw "I'm here to talk again to Paul about a case. This is Detective Varkus."

            rc "Alright. I'll send you to him in a moment."

            if asshole_pts == 0:

                "He picks up instantly."

                hide phone

                show paul base

                pm "Laura, how are you doing? What can I help you with?"

            if asshole_pts == 1:

                "Waiting a bit"

                "Hold music is annoying..."

                "Still going..."

                hide phone 

                show paul base

                pm "Detective Varkus. Do you have any updates for me."

            if asshole_pts == 2:

                "Waiting a bit"

                "Hold music is annoying..."

                "Still going..."

                ahv "We appreciate you staying on the line. Your call is very important to us."

                "Yeah yeah yeah,...like I haven't heard that bullshit before."

                "..."

                "Goddammit how long is he taking to answer?"

                ahv "Your call will be answered shortly. Thank you for your patience."

                mw "Fucking hell Mannings! Answer your goddamn phone!"

                hide phone

                show paul base

                pm "Detective Varkus...what are you still doing on this line?"

                mw "I have updates about the case."

                pm "Fine, but make this quick. You're testing my patience."

            if asshole_pts == 3:

                "He picks up immediately"

                hide phone

                show paul base

                pm "I told you never to call again. Leave now, asshole"

                hide paul base

                show maslow base

                "The phone hangs up"

                "Oh well...guess he doesn't have the nerve to stand up to Monarch"

                $ asshole_pts += 1

                "Well, what to do now?"

                menu:

                    "Re-examine evidence":

                        jump examination

                    

            menu:

                "Ask about the blood sample" if blood_examine == 1:

                    mw "Look, I've been doing some work on a blood sample I found at the crime scene."

                    pm "And? What have you found?"

                    jump paulBlood

                "Ask about the matchbook" if match_examine == 1:

                    mw "I found this Monarch Liquor-branded matchbook at the scene."

                    pm "Huh, weird. Anything about them you found interesting?"

                    jump paulMatches

                "Ask about the piece of fabric" if fabric_examine == 1 and fabric_content == 4:

                    jump paulFabric

                "Return to examination":

                    mw "Sorry...I need to give some stuff another look over"

                    hide paul base

                    show maslow base

                    jump examination

        label paulMatches:

            $ match_examine -= 1

            if linked_name == 0:

                mw "I found some phone numbers in here. I was figuring I'd give them a call. See where they lead."

                pm "I mean, that is a very helpful lead but be careful. If Monarch catches wind of this...we could be in danger of shutting down."

                mw "I'll be careful"

                pm "Good."

                hide paul base

                show maslow base

                "Hanging up. Let's try those matchbook numbers"

                jump callMatch

            if linked_name == 1:

                jump paulCheckIn

        label paulFabric:

            $ fabric_examine -= 1

            mw "The fabric I found. It's really weird."

            pm "Explain how?"

            mw "Like, it's really stretchy and light, but incredibly durable."

            pm "I see, anything else?"

            mw "It's fire proof,or at least resistant. I lit it with a match and it didn't burn."

            pm "Go on..."

            mw "And the profile of it all. It was sweaty and reeked of an old drug...speed"

            pm "I think we may have an idea of who is behind this"

            mw "Who?"

            pm "An ex-super of Monarch. Francis Ticonderoga."

            mw "Also known by the name of Frantic."

            mw "Originally a part of a new superhuman pilot program, but that got shutdown after he was busted for speed abuse."

            pm "But the real question is..."

            jump weHaveAName

        label callMatch:

            "Dialing now...please be something good"

            "...stupid hold music"

            hide maslow base

            show phone

            ahv "We thank you for calling the Monarch Liquor Company. Please be patient as we are taking a lot of calls right now."

            "Great...now I have to deal with this bullshit"

            mcc "Thank you for calling Monarch Liquor Customer Service. How may I help you?"
            
            mw "Yeah, I'm calling to ask if you have any matchbooks?"

            mcc "Yes, we do have matchbooks, but they are in limited quantity and reserved for only esteemed Monarch guests."

            mw "Well that's great because I'm calling about a loose matchbook I found and I want to know who it belongs to."

            mcc "I'm sorry, but we're not allowed to divulge confidential customer information."

            mw "So they're confidential I see..."

            menu:

                "Hang up and re-examine evidence":

                    mw "Let me get back to you on this..."

                    mcc "Alright, thank you for calling Monarch Customer Service"

                    hide phone

                    show maslow base

                    jump examination

                "Ask about the suit fabric" if fabric_content == 4:

                    mw "Well, I found it at the scene alongside this really durable and stretchy piece of fabric."

                    mw "Mind telling me about that?"

                    mcc "Well...that...uh-"

                    "They start whispering"

                    mcc "Look, I can get in a lot of trouble for dropping a name here but..."

                    mw "Tell me. Who is it and who are they?"

                    mcc "...Francis Ticonderoga"

                    $ linked_name += 1

                    mw "What?"

                    "He starts talking loudly now"

                    mcc "I'm sorry, but unfortunately I can't help you with that problem. Your uhhh...warranty has expired."

                    mcc "Have a good day and uhm, goodbye"

                    hide phone 

                    show maslow base

                    "The phone hangs up"

                    "Francis Ticonderoga...well now I have a name"

                    "That should be enough information, but...what's next?"

                    menu:

                        "Check in with Paul" if linked_name == 1:

                            jump paulCheckIn

                        "Re-examine evidence":

                            "I guess giving the evidence another look would be helpful"

                            jump examination


        label paulCheckIn:

            "Dialing him now..."

            if asshole_pts >= 1:

                hide maslow base

                show paul base

                pm "Detective Varkus, what do you want? It's after hours and I want to go home"

                mw "I just had a really big break in the case, but I need your thoughts."

                pm "Wait what? Really?"

                mw "Believe it"

                $ asshole_pts == 0

            if linked_name == 1:

                hide maslow base

                show paul base

                pm "What do you got for me, Laura?"

                mw "well..."

                mw "We have a name now. Francis Ticonderoga."

                pm "Wait...you mean?"

                mw "Yeah, Frantic himself."

                jump weHaveAName


        label weHaveAName:

            pm "Why would an ex-Super Enforcer murder someone for no reason?"

            mw "Exactly. That's what I'm wondering."

            pm "We've delved into dangerous territory, Laura...I don't know if we should continue"

            mw "It's a big lead, Paul. We have to take it."
                
            pm "Yes, but also...they're onto us Laura"

            mw "Who?"

            pm "Monarch Labs. I just got a call from the CFO who wanted to follow up about my deal."

            mw "You mean...?"

            pm "Yeah, Gustavo Marcus himself. He's really trying to push forward with a contract."

            mw "I see...and are you going to take it?"

            pm "I don't know. And I'm not sure I can keep working on this case with his eye on us..."

            mw "We have to keep doing this. Justice for the client, remember?"

            pm "Yes I remember, but this can get dangerous."

            pm "Have you heard the rumors about the journalists?"

            mw "What journalists?"

            pm "These people from the Grimhel Gazette. They wanted to know more about the Crowned Capes. Big documentary kind of deal."

            mw "What happened to them?"

            pm "Well supposedly Monarch told them many times to stop, but after a long time the lead of the gazette made a statement saying the documentary was scrapped at the request of Monarch Labs"

            mw "...so is that a legal issue or?"

            pm "You don't understand, the leader would never have said anything like that. She was extremely anti-Monarch."

            pm "I'm saying Monarch must've had her and the entire documentary team killed. No one has seen them in weeks. The stories coming out of the gazette haven't been the same since."
                
            mw "Jesus Christ..."

            pm "For legal and safety concerns, I'm afraid I have to shut down the investigation."

            menu:

                "Rationalize with Paul":

                    jump rationalizeWithPaul

                "Concede":

                    mw "Fuck...if Gustavo was the one who called you, we're in deep shit."

                    pm "Yeah, I was trying to imply that."

                    mw "Fuck fuck fuck...did he offer any sort of payment?"

                    pm "I mean, he did mention that he'd be willing to offer money if we handed over a case to his legal department."

                    mw "Shit...that might be the best course right now..."

                    pm "Really?"

                    "Is this really what I want to do?"

                    menu: 

                        "Take the hush money":

                            jump hushMoney

                        "Try and rationalize with Paul":

                            mw "No..you know what...no"

                            pm "Huh?"

                            jump rationalizeWithPaul

                        "Angrily yell at Paul":

                            $ asshole_pts = 5

                            mw "You know what your problem is Paul? You're a spineless idiot who'll give in to anyone who just seems to be better than you."

                            pm "Excuse me?"

                            mw "You heard what I said, you dumbass. Fuck you and your deal. I'm going to continue this investigation myself."

                            pm "Detective Varkus...I can't allow this."

                            mw "No, fuck you Paul"

                            pm "Fuck you too!"

                            mw "What ever happened to 'Justice at all costs'? Huh?"

                            pm "There are lines we're not prepared to cross. We can't push this further"

                            mw "Fuck you and your lines. A superhero needs to be brought to justice. I'm going to do that however I can."

                            mw "Justice at all costs. Spare no expense."

                            pm "Laura...you can't do this."

                            mw "Watch me, asshole."

                            "I hang up the phone, slamming it on the desk."

                            "Paul doesn't know what he's doing."

                            "Frantic has to be stopped at all costs."

                            "I feel tired...I should call it a night."

                            jump conclusions

        label hushMoney:

            $ hush_money += 1

            mw "We have no other choice. We have to take the money?"

            pm "I mean...it will certainly help with funding."

            mw "We can't risk it. Gustavo is too powerful."

            mw "Do you really want the Crowned Capes on our ass?"

            pm "Oh god, that's a terrifying thought."

            mw "Exactly. We go against Gustavo's wishes, we going to get brutalized by The Patriot."

            pm "Shame no one understands how much of a cruel monster he is."

            mw "One look into those eyes of his and you won't see anything."

            mw "All you see is a cold, dead, heartless man who has the gall to call himself a 'hero'."

            pm "On that note...I better leave the office."

            mw "Stay safe Paul."

            if asshole_pts >= 1:

                pm "Yeah, watch yourself as well Detective Varkus"

                hide paul base

                show maslow base

                "He hangs up"

                "I feel dirty...but it had to be done."

                jump conclusions

            if  asshole_pts == 0:

                pm "Stay safe as well, Laura. You're all I got right now."

                mw "You as well, friend."

                hide paul base

                show maslow base

                "I hang up the phone"

                "...that deal makes me feel dirty."

                "Did I make the right choice?"

                jump conclusions

        label rationalizeWithPaul:

            $ arrest += 1

            mw "Remember what we agreed to when we got in this business?"

            pm "...I do"

            mw "What did we say we would always stick to?"

            pm "...justice at all costs"

            mw "Exactly. Justice at all costs."

            mw "And especially considering the culprit here, justice is deserved."

            pm "But you don't understand. Monarch could ruin us both."

            mw "Who gives a damn if we get ruined."

            mw "Arresting Frantic could set a precident."

            mw "We take care of one superhuman abusing power, we can get the ball rolling for other cases like this."

            mw "Other 'Frantics' might be out there doing far worse and getting away with this."

            pm "But you don't understand. The people abusing their power are the ones in power."

            pm "What could we even do to stop them?"

            mw "We'll find a way...we always do."

            pm "I don't know but...I trust you Laura."

            mw "Remember. Justice at all costs."

            pm "Yeah. Spare no expense."

            pm "I'm going to leave the office now. Take care of yourself now, alright?"

            mw "I will, goodnight Paul"

            if asshole_pts >= 1:

                pm "Goodnight Detective Varkus."

                hide paul base

                show maslow base

                "He hangs up"

                jump conclusions

            if asshole_pts == 0:

                pm "Goodnight Laura. Please...be careful."

                mw "Justice at all costs"

                hide paul base

                show maslow base

                "He hangs up"

                jump conclusions

        label conclusions:

            "Francis Ticonderoga...the superhuman Frantic."

            "What goes through someone's mind that pushes them to do something like that?"

            "Drugs? No...couldn't be"

            "Frantic went to rehab back in 2022. He's been very public about his progress...so I don't understand."

            "Why would he do this?"

            "More importantly, I thought Monarch axed all connections with him"

            if hush_money == 1:

                "Well, at least I'll be getting payment from Monarch."

            if arrest == 1:

                "I hope that he gets brought to justice."

            "Welp...tomorrow's another day, better get some rest."

            jump dayTwo

        
        label dayTwo:

            scene apartment

            show maslow base

            "Monday, November 4th. 7:06 A.M. One day before the presidential election"

            "I wake up groggily. Sleep has been difficult these past few nights."

            if hush_money == 1:

                "At least taking this money will help me stay on my feet."

                "But what about my integrity?"

            if arrest == 1:

                "This case is weighing heavily on me."

                "So many horrible faces in this situation."

                "I feel like sleep over these next few days will become a difficult chore."

            mw "I get out of my bed and go to the kitchen in my apartment."

            mw "Seems Kara must still be asleep. Lucky her."

            "..."

            mw "The growls of my stomach interrupt my own thoughts."

            mw "I must find something to satiate this feeling. Maybe that will wake me up."

            mw "I open the fridge to see some small things:"

            mw "A can of chili"

            mw "Half a dozen eggs"

            mw "Leftover pizza"

            mw "and some slices of cheese"

            mw "What can be made with this?"

            menu:

                "Scrambled eggs and toast":

                    mw "Pretty standard breakfast, but decent enough for the morning ahead."

                    jump KaraBreakfast

                "Grilled Cheese":

                    mw "Not necessarily a breakfast food, but it's comforting."

                    mw "Maybe if I maybe soe extra I can do my meal prep for the day."

                    jump KaraBreakfast

                "Cold pizza":

                    "I don't have time to think about this, let alone warm up a slice."

                    jump lonelyBreakfast

                "An omlette":

                    mw "Get the creative juices flowing with a chili cheese omlette. Might as well make breakfast exciting."

                    mw "Mmm. That smells good. The flavors of the chili and the texture of the eggs and cheese. It pairs together so well."

                    jump KaraBreakfast

            
        label KaraBreakfast:

            hide maslow base

            show journalist

            mx "Who's making breakfast at this ungodly hour?"

            mw "Oh, looks like someone is awake. With some messy bedhead too. I wonder why?"

            mx "You were monologuing again, Lar. That and food."

            mx "My stomach sensed you were making food."

            mw "Right, I got to stop doing that."

            mx "Don't. It makes you sound like a serious hero."

            mw "Right."

            mx "How are you going to save the world today?"

            mw "I've told you, I don't have that kind of power."

            mx "But come on. I ask you it every morning and you give the same answer"

            if asshole_pts >= 1:

                mw "I don't have time to play games right now. There's a lot weighing on me."

                mx "Wow, sounds like someone's grumpy."

            if asshole_pts == 0:

                mw "Alright. I'll try my darndest to make the world a better place for one person for at least one second."

                mx "There it is."

                "She says this while giving me possibly the biggest smile I've seen from her in awhile."

            "Kara draws in for a small hug while walking off."

            mx "I'll let you get breakfast done. I have to get myself ready for the day"

            mw "Alright then."

            "God I love her."

            "Everything about her screams happiness."

            "The Kara I've known for years now doesn't have a single bad bone in her body."

            "She's honestly the only person in Grimhel who still holds out hope for change."

            jump workDayTwo

        label lonelyBreakfast:

            mw "Suddenly, out of the corner of my eye, I see Kara."

            mx "Morning you monologuer."

            mw "Good morning to you too sleepyhead. Looks like you're well rested."

            mw "What got you out of bed."

            mx "You were monologuing again, Laura."

            mw "What?"

            mx "That thing you do where you think you're narrating your journal but really you're just talking to yourself."

            mw "Oh, sorry about that."

            mx "Don't stop that. It's cute."

            mw "Fine, I guess that's true but what are you doing?"

            mx "I came to check on you, see how you were doing."

            mx "When you came home last night, it seemed like there was a lot of unresolved tension."

            mw "It's this new case, babe. lots of crossed wires, big names tied up in it, you know. The usual stuff."

            mx "Are you going to be okay?"

            menu:

                "Tell her the truth.":

                    mw "We're working a murder case involving Monarch."

                    mx "Oh my god..."

                    mw "Yeah...I know. Frantic too. Incredibly bad."

                    mx "That speedy motherfucker?"

                    mw "Yeah..."
                    
                    mx "God, he was annoying whenever I ran into him."

                    mx "You think he relapsed?"

                    mw "Maybe. From what I gathered the drugs were still very much a part of his aura."
                    
                    mx "You think Paul's going to be okay?"

                    mw "Uhhhh..."

                    menu:

                        "Tell Kara about the deal.":

                            mw "...Paul got contacted by Monarch. They're trying to set up business with him."

                            mx "Oh my god I...I can't even..."

                            mw "I know...it's awful."

                            mx "How can he? After all that they've done to me...and to Jack...and to you..."

                            mw "He's not doing well, and he has to find a way to support his business and take care of Melissa."

                            mx "That poor girl..."

                        "Keep the details hidden.":

                            mw "We're still working through the case. Obviously I'm not at lengths to talk about many of the details involved."

                            mx "Oh...okay"

                            mx "Is there anything at all you can tell me?"

                            mw "I would if I could, but I can't."

                "Lie and say its okay.":

                    mw "Yeah, everything's going to be fine. I think me and Paul can handle it really well."

                    mx "That sounds alright, but are you sure? When you came home last night you were dead tired."

                    menu:

                        "Say its fine":

                            mw "I just was working out some extra details, you know, do my job perfectly and all that."

                            mx "I mean, are you really sure? If something's wrong you can tell me."

                            mw "Everything's great, sweetie. I think I probably am just stressed about the move."

                            mx "I know its stressful, but I really think it's for the best we get out of here as soon as we can."

                            mw "I know, but think about everything that we've done here. I mean, my job, your career. We'd be uprooting a lot of our lives."

                            mx "I know it's a lot to think about, but you have to understand Grimhel just isn't safe."

                            mw "You're right."

                        "Tell her the truth":

                            mw "Look, the whole of this case is stressing me out beyond relief."

                            mw "The ties to monarch, superhumans, all of that."

                            mw "On top of that the election is in a few days."

                            mw "Seems like everything's getting worse and worse here each day."

                            mw "The whole moving situation to. It stresses me out beyond relief."

                            mx "That sounds like a lot to deal with..."

                            mx "...have you been journaling like your therapist suggests?"

                            menu:

                                "Tell her about your latest entries.":

                                    mw "Take a look for yourself."

                                    mx "Oh my god..."

                                    mw "Yeah...it's not pretty."

                                    mx "How long have you been feeling like this?"

                                    mw "The visions keep coming back to me...I don't know why."

                                    mw "I feel like the next time I snap...someone's going to die."

                                    mx "Don't say that, Lar."

                                    mw "How do you know that won't happen?"

                                    mw "How do you know what will set me off and what won't?"

                                    mx "Lar, you've done a lot of growing these past few years."

                                    mx "I really believe you have good control over these things."

                                    mw "Really?"

                                    mx "Yes I do. Now let me get ready for the day. Don't you have to go into work?"

                                    mw "Shiiiiiiiiiit you're right. Love you, honey."

                                    hide journalist

                                    show maslow base

                                "Hide them.":

                                    mw "I mean, I have but...I really don't think you should see them."

                                    mx "Laura...if somethings not okay I have to know."

                                    mx "You know what the doctor said about communication."

                                    mw "Yeah...communication helps heal wounds...what a load of bullshit."

                                    mx "It's not entirely wrong."

                                    mw "There's some wounds talking can't fix."

                                    mw "You know how much I want to forget my time with the CIA? I'd love to forget it."

                                    mw "But everyone's always saying that I need to 'talk things through' with others and 'sort out my emotions'."

                                    mw "I just want to forget what happened. Is that too much to ask?"

                                    mx "Laura...you can't shut people out like this."

                                    mw "I have to get into work, Kara...I'll see you later tonight."

                                    mw "...I love you."

                                    mx "I love you too."

                                    hide journalist

                                    show maslow base

            "How in all of this madness can Kara be the only one holding onto their sanity?"

            "It's like she's more human than any of the rest of us."

            "All I hope for is that the we can both get out of here soon"

            "...for both of our sakes."

            jump workDayTwo

        label workDayTwo:

            "Well, enough breakfast time. I'd better get myself together for the day."

            "I know I have a long day ahead of myself."

            scene bg streets

            show maslow base

            "Everything is dark, drab, and grey."

            "The city is crumbling...and it seems like everyone has given up."

            "Trash piles up on the streets and no one takes care of it."

            "Protests occur from opposing ends of the spectrum. Monarch supporters and anti-superhumans."

            "A political clusterfuck if I've ever seen one."

            "Crap...there's a protest taking place on my usual work route, but I could take a detour to avoid it."

            "Things keep getting more and more violent each day, so it might be in my best interest to avoid it, but I do want to make it to my office on time."

            "What should I do?"

            menu:

                "Take the usual route":

                    "Well, let's stick to the tried and true method."

                    "As I pass by the protest, I can hear the erratic and flammatory words of the anti-superhuman leader"

                    "Jonathan Hanson Marks."

                    $ run_jon += 1

                    "He's been making speeches all across Grimhel that target not only Monarch, but superpowered individuals as well."

                    hide maslow base

                    show john marks

                    jhm "YOU THERE! WHAT IS YOUR NAME?"

                    "Shit...I think he's talking to me."

                    mw "Uh my name is Ms. Yabis. First name Non"

                    jhm "I'm being serious. Who are you?"

                    mw "Fine, I'm Laura Varkus. Exasperated resident of this current moment right here."

                    jhm "Laura Varkus...as in the private detective down on Moore Avenue?"

                    mw "Yeah, who's asking?"

                    jhm "I hear some folks saw you on Morrison St. yesterday investigating a crime. Murder was it?"

                    mw "I'm not at length to disclose that information."

                    jhm "Well apparently, that alley was the sight of a murder conducted by a MONARCH BRANDED SUPERHUMAN"

                    jhm "As an ally to humankind, will you spare no mercy to this high and mighty asshole who thinks they're better than us?"

                    if hush_money == 1:

                        mw "As I said, I'm not at length to discuss private case details."

                        jhm "Well, I should trust that you're on the side of humanity then."

                    if arrest == 1:

                        mw "I'm doing everything I can to be assured that justice gets served properly."

                        jhm "Exactly. Justice for Humanity! Death to Monarch"

                    "The crowd starts chanting loudly, but I can see a way out of the situation."

                    hide john marks
                    
                    show maslow base

                    "...finally time to head into work."

                    jump officeDayTwo

                "Try the detour":

                    "Well, maybe the detour will keep me out of that nonsense."

                    "Hold on...who is that?"

                    $ run_gus += 1

                    hide maslow base

                    show gustavo marcus

                    gm "Hello there, Detective Varkus."

                    mw "...how do you know my name?"

                    gm "I know lots of things Varkus. It's useless to ask me how I know your name."

                    mw "So...what do you want from me?"

                    gm "I came to ask about that case you're working."

                    mw "Yeah? What about it?"

                    if  hush_money == 1:

                        gm "I believe I owe you some payment for your discretion."

                        mw "Wait, you're serious?"

                        gm "Yes, of course."

                        gm "What kind of businessman would I be if I didn't uphold my end of the bargain."

                        $ wallet += 500000

                        "Mr. Marcus just gave me $500,000."

                        gm "Use that as you see fit."

                        gm "And don't worry, I've already taken care of your lawyer friend."

                        mw "I don't know what to say..."
                        
                        gm "Then don't."

                    if arrest == 1:

                        gm "I should trust that we both have each other's best interests at heart here?"

                        mw "I don't know. I'm just a small-time private detective doing whatever I can to get paid."

                        mw "Why should I care about what the CFO of Monarch Labs has to say?"

                        gm "Because, Detective Varkus, I am a man of my word."

                        gm "...and I swear upon everything I believe in"
                        
                        gm "If you do not comply..."

                        gm "...I will have your head and the heads of everyone you love."

                        gm "So don't rock the boat."

                        "What do I do? Marcus seems like he'll make good on his threats if I don't bend to his will."

                        menu:

                            "Drop the case immediately.":

                                mw "Look...fine, I'll drop the case. Just don't hurt anyone"

                                gm "That's what I thought."

                                $ arrest -= 1

                                $ hush_money += 1

                                gm "Here's something for your troubles."

                                $ wallet += 125000

                                "He just handed me $125,000"

                                menu:

                                    "Negotiate the payment":

                                        mw "You sure this is enough for what I'm due?"

                                        gm "Well you didn't take the deal the first time around, so I cut the price."

                                        gm "But as long as you keep quiet and drop the case."

                                        $ wallet += 125000

                                        "He just handed me another $125,000"

                                        gm "I'm sure that's enough now."

                                        gm "Ask for any more and I'll just silence you myself."

                                        gm "Use that as you see fit"

                                    "Accept the money":

                                        mw "Thank you, Mr. Marcus"

                                        gm "The pleasure is all mine Detective."

                                        gm "Happy to do business with you"

                            "Continue in defiance":

                                mw "Just watch me Marcus."

                                mw "Your threats mean nothing to me."

                                "His face loses any and all expression it had before."

                                gm "Scorched Earth it is then."

                                gm "Tell me, do you want to watch your city burn?"

                                mw "I will do anything to protect the innocent of Grimhel."

                                gm  "You'd even watch your precious Kara burn down in flames?"

                                "I backed down in shock. Threatening Kara...how does he know about her?"

                                gm "Aw, what's that? You care about Kara too much to let her go...but what was your slogan again?"

                                gm "Ah yes, 'Justice at all costs'"

                                gm "Whata beautiful phrase you have there."

                                gm "But how far are you willing to go to make due on that promise."

                                gm "Will you really give up everything to save this pathetic and broken city?"

                                "...Kara...no...I can't let Marcus hurt her."

                                gm "You just see how far this charade of justice goes then."

                                gm "We're both people of our word..."

                                $ scorched_earth += 1

                    hide gustavo marcus

                    show maslow base

                    "Gustavo then leaves."

                    "...I guess it's time I head into work."

                    scene bg office
                
                    show maslow base

                    "I may be a little late, but somehow my answering machine is completely free of any messages."

                    "That's very odd...usually Paul makes the first call whenever he gets to the office."

                    "Maybe he's running late too..."

                    "What should I do?"

                    jump officeDayTwo

            label officeDayTwo:

                scene bg office

                show maslow base

                menu:

                    "Call Paul's Office" if call_2 == 0:

                        $ call_2 += 1

                        hide maslow base

                        show phone

                        "The phone is ringing."

                        "Dammit...I went to voicemail"

                        ahv "Thank you for calling the Offices of Mannings and Associates. We're not here right now. Please leave a message after the tone."
                        
                        mw "Hey Paul, it's me, Laura. Just calling because I came into the office and I noticed you hadn't called yet. I had an interesting morning to say the least."

                        if run_jon == 1:

                            mw "I ran into a John Marks protest."

                            mw "He seems very volatile right now. I tried to keep our situation under wraps though as best as I could."

                            mw "...though I don't know how much more violence this city can handle."

                        if run_gus == 1:

                            mw "I ran into Gustavo Marcus today"

                            if scorched_earth == 1:

                                mw "He's making all sorts of threats to everyone and I'm really worried he'll do something to Kara."

                                mw "I don't know what to do here right now."

                                mw "Just please...I need help here..."

                            if hush_money == 1:

                                mw "I got the payment from him directly."

                                mw "Was this the right option though? I feel like we just sold out our business here."

                                mw "I mean, I know our motto is justice at all costs...but was this worth it?"

                        hide phone

                        show maslow base

                        "I then hang up the phone."

                        "What could this all possibly mean?"

                        "...anyways, what should I do now?"

                        jump officeDayTwo

                    "Look into Francis Ticonderoga" if arrest == 1:

                        "Maybe I should look more into Frantic. See where he's hiding out these days."

                        "Looking through all these documents should help."

                        jump searchFrantic

                    "Turn on the TV" if hush_money == 1:

                        if run_gus == 0:

                            "Let's see what's on the news."

                            "Huh, another John Marks protest."

                            "His language...it's riling people up."

                            "If Grimhel's being destroyed by anyone, it's him for sure."

                            "Hold on, who could be calling now?"

                            mw "Varkus Investigative Services. What do you need?"

                            gm "Is this Detective Varkus?"

                            mw "Yeah, this is them speaking."

                            gm "Excellent. I'm calling about the deal you made with your partner, Paul Mannings."

                            gm "Something about...payment being due?"

                            mw "Exactly."

                            gm "Good. I understand that I can trust you to keep this all under wraps then?"

                            mw "Of course."

                            gm "I'll hold you to that."

                            gm "Because someone is only as good as their word, and well, if you break my trust, then..."

                            gm "There will be more to face than just lawsuits, Detective."

                            mw "What?"

                            $ wallet += 500000

                            "He hangs up the phone"

                        if run_gus == 1:

                            "Let's see what's on TV."

                            "Another anti-superhuman protest led by John Marks."

                            "If anyone is destroying Grimhel more than Monarch, it's him for sure."
                            
                            "All of that hate bundled up into one man...how does he live like that?"

                            "The phone sharply breaks the silence."

                            mw "Varkus Investigative Services. What do you want?"

                            gm "Ah, Detective. So glad to be speaking again."

                            mw "Marcus...what do you want?"

                            gm "I just want to talk to you, after all, we did make a deal, no?"

                            mw "What did you do?"

                            gm "Relax, I haven't hurt that precious Kara of yours yet."

                            mw "You better stay away from him..."

                            gm "I'll keep out of your personal life if you uphold yourself to the deal we made."

                            "He hangs up the phone."

                        "I can't let him hurt Kara..."

                        "...oh god, what if Kara finds out about the money?"

                        jump dayTwoNight

            label searchFrantic:

                "Francis Ticonderoga. A young man who was an all star runner until things went sour."

                "It came out that he had been abusing performance enhancing drugs to run faster than all of his competitors."
                    
                "Disgraced and disowned from his championship title, he believed that he had nowhere else to go."

                "That was until he met a fortunate member of Monarch Labs who offered him money to partake in an experiment."

                "One that would turn him into a legend, likened to the messenger god, Hermes."

                "Eventually all records of Francis's track career were scrubbed from the public eye, as he was given a new identity..."

                "...Frantic. The Yellow Streak."

                "After years of a successful career, it all came to a head when he was busted for using speed to enhance his powers."

                "Any and all programs involving Frantic's name or likeness were shut down and/or scrapped..."

                "To this day, Frantic's drug abuse has not become public knowledge, only to the point here he talks about his recovery."

                "However,...some dealers within Grimhel still cite the appearance of the Yellow Streak at their bases of operations"

                "...potentially hinting at his involvement in Grimhel's underground drug ring."

                "Last known sighting...a warehouse on the outskirts of the city."

                "Guess I know where I'm going then..."

                jump warehouse

            label warehouse:

                scene bg desert

                show maslow base

                "An old abandoned warehouse..."

                "Damn, what a cliche place for a drug smuggling ring. What next? Will there be a standoff in the desert?"

                "...shit. There's people here...I have to hide."

                cm2 "How long is this guy taking? I thought he was much faster"

                cm1 "Just be patient. He'll be here any second."

                cm2 "Dude, we've been waiting all night for this bozo. I mean, trusting a guy in a leotard. What have we come to?"

                cm1 "This guy delivers. Now just shut up and be ready."

                "And just like that, the dirt kicks up in my face and a strong breeze pushed me back"

                hide maslow base

                show frantic

                ft "Sorry about the delay. I have had way too many press releases talking about 'overcoming the demons within'"

                ft "Apparently my ghost writers are working on a memoir about the whole situation."

                cm1 "Whatever man. Do you have our money?"

                ft "Of course, Damien. You think just because I'm a superhero that I'll disrespect the cartel? A man's gotta make money somehow."

                cm2 "Yeah, whatever. Just take these out for us now. Spread them wherever you can. We'll meet in another week to retrieve payment"

                "He pulls out two large, brown bricks."

                ft "Two whole kilos. Gentlemen, I love your enthusiasm, but two pounds is too much to push in just a week especially with the public's eye on me."

                cm1 "Do it, or we tell the media about your little frenzy the other night."

                ft "Alright, alright. I'll push it."

                hide frantic

                show maslow base

                "Now's my chance...I should be able to catch them off guard, but with Frantic..."

                "...should I risk it all right now? Or play it safe?"

                menu:

                    "Catch Frantic and the cartel members off guard" if scorched_earth == 1:

                        "I draw my gun, hoping that this will be enough to handle the situation"

                        jump catchFrantic

                    "Keep hiding":

                        "I keep hiding in the hopes that I'm not found out."

                        "Maybe I can observe more of the situation."

                        hide maslow base

                        show frantic

                        cm1 "Wait, did someone hear that noise?"

                        ft "Hold on..."

                        "Frantic runs towards me and grabs me by the jacket."

                        ft "It's just some fucking person."

                        "Those words offended me."

                        jump getCaught

                    "Attempt to run away":

                        "I make a quick dash for it."

                        hide maslow base

                        cm1 "Quick. We got a runner."

                        show frantic

                        ft "No worries. I got it."

                        "Frantic grabs me by the jacket"

                        cm2 "Who is it?"

                        ft "Just some fucking person."

                        jump getCaught

            label getCaught:

                hide frantic

                show maslow base

                mw "Do you have any idea who I am?"

                hide maslow base

                show frantic

                ft "No. You're just a nobody, about to die a nobody."

                hide frantic

                show maslow base

                mw "My name is Detective Laura Varkus."

                mw "I used to work as a CIA Black Ops Unit"

                hide maslow base

                show frantic

                ft "Yeah, so? I have you caught. CIA operative or not, you're dead."

                ft "Who holds all the power here, huh?"

                ft "Me. The one with superpowers. What are you going to do about it?"

                menu:

                    "Arrest Him":

                        hide frantic

                        show maslow base

                        mw "I have orders to take you in by my client on charges of homicide."

                        "He loosens his grip."

                        "As Frantic does that, I reach for the handgun in my coat."

                        mw "I just have a couple questions for you."

                        hide maslow base

                        show frantic

                        ft "Fuck no. I'm not answering anything."

                        mw "Fine then."

                        "Three shots to his legs."

                        ft "Fuck! What was that for?!"

                        mw "It was so you would talk."

                        jump franticInterro

                    "Fight back":

                        hide frantic

                        "A square punch to his face sends him falling."

                        "I have the advantage now."

                        "Do I capitalize on it and make sure he's done for?"

                        menu:

                            "Interrogate him":

                                jump franticInterro

                            "Beat him senseless":

                                $ frantic_life = 0

                                show maslow base

                                "I keep punching him."

                                "Blood starts to coat my fists."
                                    
                                "I see nothing but the face of a depraved murder."

                                "My eyes are seeing red...my vision cloudy"

                                "..."

                                "Several minutes go by...and I eventually come down from the high."

                                "I see Frantic's face in the dirt, completely disfigured."

                                "A pile of red..."

                                "I guess it's time I head back to the office..."

                                jump dayTwoNight

            label catchFrantic:

                hide frantic

                show maslow base

                mw "Stop right now! I have orders to take in Francis Ticonderoga on charges of homicide."

                cm1 "You wanna go? It's 3 against 1. Are you sure bout this?"

                hide maslow base

                show frantic

                ft "Besides, you expect to stop me with just a gun. How naive are you?"

                hide frantic

                show maslow base
                    
                mw "Naive enough to do this."

                "...I proceed to make three quick shots to Frantic's leg. They all hit."

                hide maslow base

                show frantic

                ft "Fuck! Dammit."

                cm2 "Shit...we gotta get out of here."

                cm1 "I agree"

                "Both cartel members take off in fear of what's about to happen."

                hide frantic

                show maslow base

                mw "Do you have any idea who I am?"

                hide maslow base

                show frantic

                ft "Sure...I know who you are. You're a fucking dickweed who shot me in the leg."

                hide frantic

                show maslow base

                mw "Wrong."

                menu:

                    "Shoot him":

                        $ frantic_life -= 1

                        hide maslow base

                        show frantic

                        ft "Aghhhh...why.."

                    "Continue Interrogation":

                        mw "Name's Laura Varkus. ex-CIA Black Ops Unit and current private detective in the city of Grimhel."

                        mw "Can I ask about your involvement in a case related to a client of mine."

                        hide maslow base

                        show frantic

                        ft "No..."

                        hide frantic

                        show maslow base

                        mw "I was thinking you'd say that."

                        menu:

                            "Continue the interrogation":

                                jump franticInterro

                            "Shoot him again":

                                $ frantic_life -= 1

                                "I decide to shoot him in his other leg. Best to keep him from running."

                                hide maslow base

                                show frantic

                                ft "GODDAMMIT! AGHHH!"

                                hide frantic

                                show maslow base

                                mw "Now are you going to talk?"

                                hide maslow base

                                show frantic

                                ft "Yeah..."

                                jump franticInterro

            label franticInterro:

                mw "Now answer me...what were you doing on the night of October 24th?"

                ft "Routine interviews. Publicity tours...all that stuff."

                mw "Bullshit. You were on Morrison St."

                ft "...how did you know?"

                mw "I know lots of things, Francis."

                ft "What do you want from me?"

                menu:

                    "Arrest him":

                        mw "You're coming with me. Your court date should be soon for everything that you have done."

                        hide frantic

                        show maslow base

                        "I handcuff Frantic and call for an emergency ambulance."

                        "He can bounce back from this quickly, but hopefully by the time he recovers, the bastard will be behind bars and depowered."

                        $ arrest += 1

                        jump dayTwoNight

                    "Get justice":

                        mw "I want justice."

                        $ frantic_life = 0

                        "I shoot one final bullet in the bastard's brain."

                        hide frantic

                        show maslow base

                        "He keels over, dead."

                        mw "Like I said, Paul. Justice at all costs."

                        jump dayTwoNight

            label dayTwoNight:

                scene bg office

                show maslow base

                "Well, it seems that I've done my work for the night."

                "Maybe I should give Paul one last call?"

                menu:

                    "Call Paul":

                        "Dialing his office phone"

                        "...he actually picks up this time."

                        hide maslow base

                        show phone

                        mv "Good evening Detective."

                        mw "...Paul?"

                        mv "I'm afraid that Paul is unfortunately no more."

                        mw "What?"

                        if scorched_earth == 1:

                            hide phone

                            show gustavo marcus

                            gm "Well I'm afraid that Paul was a bit hesitant on our original offer, and it seems you've gone rogue too."

                            mw "What do you mean?"

                            gm "You have frantic's blood on your hands."

                            gm "And it seems you were hiding a lot there, huh?"

                            gm "I mean ex-CIA Black Ops. Outstanding really."
                                
                            mw "What's this have to do with Paul?"

                            gm "Well for one, he was about to betray our trust."

                            gm "And don't you remember our deal about scorched earth?"

                            mw "So what? You take my best friend and business partner and I take a snivelling lowlife who you were trying to distance yourselves from."

                            mw "Honestly, I probably did you all a favor."

                            gm "You're going to regret what you have done."

                            mw "What are you going to do, huh?"

                            gm "What was her name...Kara?"

                            mw "You wouldn't..."

                            gm "Oh, but we would"

                            "He hangs up the phone"

                            "What is happening to the city?"

                            jump finalDay

                        if run_gus == 1:

                            hide phone

                            show gustavo marcus

                            gm "Well I'm afraid that Paul was a bit hesitant on our original offer, and it seems you've gone rogue too."

                            mw "What do you mean?"

                            gm "Frantic's supposedly behind bars now. I thought I made the consequences very clear."

                            mw "Scorched earth. I remember."

                            gm "I'm coming for you, Laura."

                            gm "You're going to regret your decision."

                            "He hurridly hangs up the phone."

                            "Oh no...what if he hurts Kara?"

                            jump finalDay

                        if run_jon == 1:

                            hide phone

                            show john marks

                            mw "Wait a minute...John Marks?"

                            jhm "That's right. Apparently your friend here was making deals with all of the wrong people."

                            jhm "Luckily, they can't get to him anymore."

                            mw "Why would you do this?"

                            jhm "It's about setting a precendent. Sending a message to those who needs to see it."

                            jhm "...especially Monarch."

                            mw "But what do you want with me?"

                            jhm "Oh, your case."

                            jhm "I handled all the loose ends. Frantic is no more."
                            
                            mw "Jesus...why did you do that?"

                            jhm "Like I said, setting a precedent. And apparently you're harboring a superhuman too."
                            
                            jhm "Kara, I believe her name was..."

                            mw "No, you wouldn't."

                            jhm "But I would."

                            jhm "Take care of him by tomorrow or you're both done for."

                            "He hangs up the phone."

                            "What am I going to do?"

                            jump finalDay

                        if hush_money == 1:

                            hide phone

                            show john marks

                            jhm "See...I've found out about that little deal you had with Gustavo Marcus."

                            jhm "He paid you a lot of money to keep quiet."

                            jhm "But now I'm told I need to clean up his loose ends."

                            mw "You're...the John Marks?"

                            jhm "That's right."

                            mw "But I thought you were anti-Monarch?"

                            jhm "Yeah, well, a job's a job. I'm sure as an ex-operative you know what that's like, right?"

                            jhm "Of course...I'd be willing to forget about all of this...if you do me a favor."

                            mw "What do you mean?"

                            jhm "I take it you're living with a superhuman yourself?"

                            mw "No...no no no you can't be talking about."

                            jhm "Ah yes, Kara I recall her name was."

                            jhm "As someone against the cause of superhumans, I would be willing to ignore the job offer"

                    "Head Home":

                        "I think the best course of action is to just go home."

                        "I'm insanely tired, and having to deal with more of this shit tomorrow sounds like a fucking nightmare."

                        "On my way back, I go to pick up the mail."

                        "Funny, there's a letter from Paul's office...weird."

                        "Hmm..."

                        hide maslow base

                        show letter

                        pm "Dear Laura,"

                        pm "By the time you read this, I'll be dead."

                        pm "I hate that it had to come to this, but unfortunately that's just the way this world works."

                        pm "I regret withholding a lot from you, but in the next few days, the events that unfold will disrupt all of Grimhel."

                        pm "My death is one of several thousand that will happen in the wake of the election."

                        pm "Make your choice. Do the right thing."

                        pm "Take care of Melissa too."

                        pm "Make sure she's safe."

                        pm "Justice at all costs."

                        pm "Signed,"

                        pm "Partner for life; Paul Mannings"

                        "Dear god...what has this city turned to. "

                        jump finalDay

            label finalDay:

                scene apartment

                show maslow base

                "Tuesday, November 5th. Election Day."

                "I awake to a loud banging at my door."

                menu:

                    "Answer":

                        if run_gus == 1:

                            hide maslow base

                            show gustavo marcus

                            gm "The election is today, I take it you've done your due diligence?"

                            mw "Keep superhumans out of the military you mean? Yeah."

                            gm "I fail to see the reasoning behind your actions, but I nonetheless respect your determination."

                            gm "Let's cut the the chase, shall we?"

                            mw "What have you done?"

                            gm "Follow me, up to the roof."

                            mw "WHAT HAVE YOU DONE?"

                            jump rooftops

                        if run_jon == 1:

                            hide maslow base

                            show john marks

                            jhm "I believe you know why I came?"

                            mw "You're not taking Kara...you can't."

                            jhm "I'm not taking Kara anywhere."

                            jhm "This is your decision to make."

                            jhm "Your decision alone."

                            menu:

                                "Take care of Kara": 

                                    hide john marks

                                    show journalist

                                    "I'm sorry Kara..."

                                    "I really am sorry..."

                                    mx "Lar, what are you-?"

                                    hide journalist

                                    show maslow base

                                    "Three shots...that's all it took."

                                    "The moment she saw me...I knew she was dead."

                                    "That look in her eyes...I couldn't bear to see it."

                                    "Pleading with me to save her life, but feeling a sense of despair..."

                                    "...like she knew she couldn't stop me."

                                    "Her heart broke before any bullet hit her."

                                    hide maslow base

                                    show john marks

                                    if scorched_earth == 0:

                                        jhm "Didn't think you had it in you."

                                        jhm "That took some real guts there."

                                    if scorched_earth == 1:

                                        jhm "I knew you could do it."

                                        jhm "But I know it's hard doing what you did."

                                    jhm "Come on now. We have some real work to do."

                                    hide john marks

                                    show maslow base

                                    jump jhmKillMonologue

                                "Fight off John":

                                    hide john marks

                                    show maslow base

                                    mw "Back the fuck off now."

                                    hide maslow base

                                    show john marks

                                    jhm "What are you doing?!"

                                    hide john marks

                                    show maslow base

                                    mw "Finishing what I started"

                                    "The ensuing brawl destroys the apartment."

                                    "Furniture breaks. Floors and walls get demolished."

                                    "I end up getting the advantage..."

                                    menu:

                                        "Really finish what you started":

                                            "I strike John square in the face."

                                            "...and again"

                                            "...and again"

                                            "...and again"

                                            "...and again"

                                            "...and again"

                                            "...and again"

                                            "I don't have time to pause. He's here to hurt Kara..."

                                            "...I can't let that happen."

                                            hide maslow base

                                            show journalist

                                            mx "What are you doing?!"

                                            "She pulls my arm away from John's bloodied corpse."

                                            mx "Why did you...?"

                                            mw "He was going to...I mean..."

                                            mx "I didn't think you were capable of this..."

                                            mw "Kara...he was going to kill you..."

                                            mw "I wanted you to be safe."

                                            mx "I looked into your eyes then Lar. You're not the woman I love."

                                            mw "Kara, I can explain."

                                            mx "I don't want to hear it. Clearly you've been lying to me about a lot of things lately."

                                            mx "As far as the move is concerned, I'm leaving Grimhel on my own now."

                                            mx "Goodby, Laura..."

                                            mw "Please...don't go."

                                            hide journalist

                                            show maslow base

                                            "Kara shuts the door on me without a second of hesitation."

                                            jump KaraLeaves

                                        "Offer mercy":

                                            mw "I can't do this."

                                            hide maslow base

                                            show john marks

                                            jhm "Well then allow me."

                                            hide john marks

                                            "A sharp pain hits my stomach..."

                                            "...blood"

                                            "a bullet wound...."

                                            "Why does the room start spinning?"

                                            "My head makes a hard thud against the floor."

                                            show john marks

                                            jhm "You're weaker than I thought you were."

                                            jhm "Well...someone's only as good as their word."

                                            hide john marks

                                            "Darkness."

                                            "Emptiness..."

                                            "...death"

                                            show maslow base

                                            jump mwDeathEnding

                    "Leave it":

                        "The knocks get louder."

                        mw "Get the fuck away from this apartment. This is my own private residence and I won't allow you to harrass me or my partner."

                        if run_gus == 1:

                            hide maslow base

                            show gustavo marcus

                            gm "I thought I made myself very clear, Laura."

                            if hush_money == 1:

                                gm "I thought we had a deal."

                            gm "Now I have to rightfully uphold my end of the bargain."

                            mw "No, please, you can't."

                            gm "Come with me. Now"

                            jump rooftops

                        if run_jon == 1:

                            hide maslow base

                            show john marks

                            jhm "I think you know why I am here, Laura."

                            mw "Get the fuck out of here, now."

                            jhm "I don't want any trouble. I just want rid of that superhuman you're harboring here."

                            mw "Kara..."

                            jhm "What's it going to be? Will you side with your own kind? Or are you just as blind as those fucking bureaucrats in congress."

                            menu:

                                "Save yourself.":

                                    hide john marks

                                    show journalist

                                    "I think about this long and hard...but one of us has to live."

                                    mx "Lar...? What are you doing?"

                                    "I'm sorry Kara, but this has to be done..."

                                    mx "Please...you don't have to do this."

                                    menu:

                                        "Listen to Kara.":

                                            mw "Kara...you don't understand...John Marks...he's here to kill us."

                                            mx "Then why are you trying to kill me?"

                                            mw "He said he'd spare my life...if I took yours."

                                            mx "What the fuck? Why?"

                                            mw "You know what John is like...the bastard hates superhumans."

                                            mx "But why us."

                                            hide journalist

                                            show john marks

                                            jhm "What seems to be taking so long?"

                                            hide john marks

                                            show maslow base

                                            mw "What does this have to do with us?"

                                            hide maslow base

                                            show john marks

                                            jhm "You wanna know why I'm really here?"

                                            menu:

                                                "No time for explanations.":

                                                    hide john marks

                                                    show maslow base

                                                    mw "You don't get that privilege."

                                                    "I shoot him in the foot to keep him from running away."

                                                    mw "You are going to pay right here, right now."

                                                    hide maslow base

                                                    show journalist

                                                    mx "Laura, wait!"

                                                    hide journalist

                                                    show maslow base

                                                    mw "Don't stop me now. He was going to kill us."

                                                    hide maslow base

                                                    show journalist

                                                    mx "No, I mean, let me do it."

                                                    mw "Are you sure?"

                                                    mx "Just trust me."

                                                    "For the first time in her life...Kara uses her powers."

                                                    "She picks up John by the throat and throws him through the wall."

                                                    mx "I've been waiting to use these powers for a long time."

                                                    hide journalist

                                                    show john marks

                                                    jhm "...what,...what are you doing?"

                                                    "He says this while coughing up blood."

                                                    hide john marks

                                                    show journalist

                                                    mx "This."

                                                    "She then throws John out the window."

                                                    mx "Well...I think our security deposit is gone"

                                                    mw "Eh, fuck this place anyways."

                                                    jump powersMonologue

                                                "Hear him out.":
                                                
                                                    mw "What's your problem?"

                                                    jhm "...Kara is not like us, Laura. She's inhuman."

                                                    mw "What does that have to do with wanting to kill her?"

                                                    jhm "She's a threat to all of us. Power like that unchecked?"

                                                    jhm "Why would you ever side with them?"

                                                    menu:

                                                        "Listen to John.":

                                                            mw "...I don't know."

                                                            jhm "Exactly. You don't understand."

                                                            jhm "But understand this."

                                                            "A sharp pain hits my stomach..."

                                                            "...blood"

                                                            jhm "Like I said. It was Kara's life, or both of you."

                                                            "Kara's been struck by another bullet too..."
                                                            
                                                            jhm "I guess then it's your time to die."

                                                            jump mwDeathEnding

                                                        "Shut him up.":

                                                            mw "Because they're just as human if not more-so than us."

                                                            "One last shot to his brain kills him."

                                                            mx "Oh my god..."

                                                            mw "It had to be done..."

                                                            mx "I understand, but also-"

                                                            mw "No...no buts this time."

                                                            mx "What do you mean?"

                                                            mw "Nothing's been getting better. I thought I could fix things, but I can't."

                                                            mx "I see...well...look, if you need some time-"

                                                            mw "I'd suggest you go before I make things worse..."

                                                            mx "...right. Goodbye Lar..."

                                                            mw "Farewell, Kara."

                                                            jump KaraLeaves

                                        "Trust your gut.":

                                            "If there's one thing being in the agency taught me, it's that cogs in the machine follow all orders they're given."

                                            "Three shots...that's all it took to put her down."

                                            "I would shed a tear if I could, but everything in me has broken to the point where that's no longer possible."

                                            jhm "I didn't think you had it in you...but I like your courage."

                                            jhm "Come with me. We have a lot of work to get done."

                                            jump jhmKillMonologue

                                "Fight back.":

                                    mw "No one is going to hurt Kara."

                                    "One blow to the face."

                                    mw "Not you."

                                    "Another one."

                                    mw "Not Monarch."

                                    "A couple finishing ones."

                                    mw "And not anyone else."

                                    menu:

                                        "Offer him mercy.":

                                            "A sharp pain hits my stomach..."

                                            "...blood"

                                            jhm "Like I said. It was Kara's life, or both of you."

                                            "Kara's been struck by another bullet too..."
                                                            
                                            jhm "I guess then it's your time to die."

                                            jump mwDeathEnding

                                        "Finish the job.":

                                            mw "Any last words?"

                                            jhm "The great legend of Jonatham Hanson Marks shall live on as a martyr."

                                            mw "You could've just said 'fuck you'."

                                            jhm "I'll do you one better. A blight on your bloodline for a thousand generations."

                                            mw "Funny. I always thought this bloodline would die with me."

                                            hide john marks

                                            "A few more punches to the head and Marks is dead."

                                            show journalist

                                            mx "Laura...what The HELL?!"

                                            mw "Well, we won't be dealing with those anti-superhumans anymore."

                                            mx "You just killed a man?!"

                                            menu:

                                                "Try and make things right.":

                                                    mw "He was going to kill both of us."

                                                    mx "I mean...wait what?"

                                                    mw "John killed Paul last night too..."

                                                    mx "Holy shit..."

                                                    mw "Yeah...he was threatening to kill you as well."

                                                    mx "I just...wow."

                                                    mw "Yeah...need some time to think?"

                                                    mx "I think I need a break from Grimhel right now."

                                                    mw "I think we both do..."

                                                    mx "No Laura. I mean I have to go..."

                                                    mx "Goodbye."

                                                    hide journalist

                                                    show maslow base

                                                    jump KaraLeaves 
                                                    
                                                "Just continue as is.":

                                                    mw "Yeah, and?"

                                                    mw "You think I'm above killing?"

                                                    mx "I really thought you changed."

                                                    mw "Me? Change? In this shithole? Never in a million years."

                                                    mw "You wanna know what happens when you put a rogue CIA op in a cesspool like Grimhel?"
                                                    
                                                    mw "You amplify the horrors that they've seen in the field to the nth degree."

                                                    mx "Laura...this isn't you."

                                                    menu:

                                                        "Try and apologize.":

                                                            mw "Babe, can we please talk this through...I'm really sorry."

                                                            mx "No, we can't 'talk this through'. And don't 'babe' me, you killed a man and now he's lying on the rug."

                                                            mx "No matter what you're going through you can't...you can't kill people. Period!"

                                                            mw "He was going to hurt you."

                                                            mw "And if he didn't get to hurt you he was going to hurt me."

                                                            mw "I'm sorry...but I did what had to be done."

                                                            mx "I just...need some air"

                                                            mw "Kara wait-"

                                                            mx "Laura...I just need some time alone...please."

                                                            mw "I understand."

                                                            hide journalist

                                                            show maslow base

                                                            jump KaraLeaves 

                                                        "Continue.":

                                                            mw "This? This isn't me? Have you read a single one of my journals?"

                                                            mw "I write about this shit daily."

                                                            mw "Everything I've seen, dreamt, or even let alone thought about...it's all there."

                                                            mx "I...I don't know if I can be with you like this."

                                                            mw "You want to leave then? Fine. Go ahead."

                                                            mx "You can't push people away like this, Laura..."

                                                            mx "I'm leaving Grimhel without you."

                                                            mx "Goodbye."

                                                            hide journalist

                                                            show maslow base

                                                            jump KaraLeaves        

            label rooftops:

                "I follow Gustavo up to the roof of the apartment complex."

                "What I see is...truly horrific."

                gm "I figure this is enough to convince you to get on our side."

                mw "Kara..."

                gm "We made a deal Detective Varkus, and I am a man of my word."

                gm "Kara for Frantic. So can we call it even now?"

                jump punchGus

            label punchGus:

                "..."

                menu:

                    "Gustavo must pay":

                        "A clean strike upon his head"

                        "...and another"

                        "...and another"

                        "...and another"

                        "...and another"

                        "...and another"

                        "...and another"

                        "...and another"

                        "...and another"

                        "...and another"

                        "...and another"

                        "Red...all I see is red."

                        mw "AGHHHHHHHHHHHHHHHHHHHHHHHHHHH!"

                        jump gusDeath

                    "Would Kara have wanted this?":

                        mw "No...no more."

                        mw "I'm done..."

                        mw "I've made many difficult choices in these past few days...but now...maybe the only way out is to not play your game Gustavo."

                        gm "What are you saying?"

                        mw "I'm saying that I'm not giving you what you want."

                        gm "You couldn't possibly know what I wanted."

                        mw "You may be able to take out my business, my job, my colleagues, or my friends."

                        mw "But I'll be damned if I don't take this from you myself."
                        
                        gm "What could that possibly be?"

                        mw "You want to break me. You want me angry, scared, and afraid"

                        mw "...but you know what?"

                        mw "I forgive you."

                        gm "What?!"

                        mw "Forgiveness will never fix Paul, Kara, or anything else that you've taken from me."

                        mw "And for all of that I say fuck you."

                        mw "But today..."

                        mw "...today I forgive you"

                        mw "And I get to keep the one thing you'll never break."

                        mw "So goodbye, Gustavo. I'll see you in hell."

                        jump forgiveness

            label jhmKillMonologue:

                "In the ensuing riots after the election, Grimhel was inevitably torn apart."

                "Martial law was declared. Monarch was authorized to use lethal force."

                "The countless bodies that this conflict created...all of it was unnecessary."

                "I started this case because I believed I had some control over everything."

                "Like I was a great hero who was uncorruptable."

                "But no...I was too naive to see it."

                "All humans have the capacity be corrupted."

                "To be someone incapable of corruption or evil...you'd have to be-"

                return

            label mwDeathEnding:

                "What happened in these past few days?"

                "Was it the tension that got to me?"

                "Or was it there from the start?"

                "The capabilities to become violent."

                "Why did it all have to come to this?"

                "Was it circumstance? Was it fate?"

                "I thought I would be saving Grimhel...but it seems I've only plunged it into more violence."

                "I guess that's the nature of all humans: chaos and violence..."

                "Why, to avoid succumbing to them you'd have to be-"

                return

            label gusDeath:

                "Gustavo's dead...I'm sure of it now."

                "I look out to the skyline to revel in the chaos and bloodshed."

                "In the streets, I see people like me..."

                "Angry about what Monarch has done to them."

                "Scared for their friends and loved ones."

                "...and broken beyond repair"

                "Grimhel is beyond saving...everyone has either become corrupted, killed, or broken."

                "But I guess that's what we all devolve into."

                "At the end of the day, madness is something that we aren't just drawn towards."

                "We're born with it."

                "The voice in your head that tells you to go beyond your limits. Some call that strength. Others call it determination."

                "That is what I call madness."

                "And to refuse its beckoning voice is purely-"

                return

            label forgiveness:

                "Grimhel has been torn apart by the inevitable violence that has ensued."

                "Nothing could have fixed this."

                "So many people were involved to the point where it was bound to explode regardless of the outcome."

                "Many people can be driven."

                "Sometimes by greed. Some by power. Or others by noble intentions."

                "But I like to think that people are driven by one thing; Madness."

                "They either desperately want to escape it, or they revel in its clutches."

                "Those who try to escape it spend their whole lives pretending they're someone else entirely."

                "And those who accept its call are the ones that have nothing left to hide."

                "To deny the call of madness, it's simply-"

                return

            label KaraLeaves:

                "The world is a cruel place not meant for people like Kara."

                "She's sweet, innocent, and oddly uncorruptable...unlike most people in Grimhel."

                "I think that's what really separates us."

                "Kara knows when to quit."

                "I don't know when to stop."

                "Kara is the only person that would be worth calling a superhero."

                "I'm what some would call: 'obsessive' and 'stubborn'."

                "But over the course of these past few days, something broke in me."
                
                "A sense of madness overtook me."
                
                "Grimhel takes people and changes them for the worst."

                "But the madness we live in feels oddly natural."

                "Some would say that if Grimhel didn't make you go mad, that you were simply-"

                return

            label powersMonologue:

                mw "This is something entirely new. What happened?"

                mx "I saw the fear in your eyes when he was threatening you...how scared you truly were."

                mx "That's not something I've seen for awhile."

                mx "Something in you wasn't right when you were holding the gun."

                mx "I knew I had to step in somehow."

                mw "Well...you saved my life...I don't know what else to say..."

                mx "You can think about that when we're on our way out of here."

                "As she says this, Kara starts levitating and picks me up."

                "We fly out of the hole made in the window and soar over Grimhel."

                "While the destruction is saddening, the thought of leaving this place makes me happier than I ever could have imagined."

                "Especially with Kara, the one person I want to spend the rest of my time with."

                "Of all of us, Kara was the most pure; uncorruptable."

                "To see her compared to the rest of us, well by comparison we're-"

                return

    # This ends the game.

    return
