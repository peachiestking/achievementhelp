#Here is where the achievements are stored!
#You can name the achievements whatever, but for simplicity I used numbers.
#I also wrote the names of the achievements next to it.
default persistent.achieve_1 = False #Oh, look at that...
default persistent.achieve_2 = False #Knowledge is power!
default persistent.achieve_3 = False #What does this button do?

################################################################################

label start:

    $ renpy.notify("Achievement unlocked: Oh, look at that...")
    $ persistent.achieve_1 = True

    "Here is the test for the achievements."
    "If you're playing this for the first time, then you should have seen
        'Oh, look at that...' achievement unlocked."

    "At the bottom of the screen, there is a quick menu."
    "Clicking 'Achievements' will bring up the achievements screen."
    "Press Esc to leave."

    "If this is your first time playing, only 1 achievement will be unlocked."
    "By the end of the game, all 3 achievements will be unlocked."

    "Up next is a menu. Either choice will reward you with an achievement!"

    menu:
        "Pick me!":
            $ renpy.notify("Achievement unlocked: What does this button do?")
            $ persistent.achieve_3 = True
            pass
        "No, pick me!":
            $ renpy.notify("Achievement unlocked: What does this button do?")
            $ persistent.achieve_3 = True
            pass
    "Good job!"
#Here, the game will only notify you if you HAVEN'T got the achievement yet.
    if persistent.achieve_2 == False:
        $ renpy.notify("Achievement unlocked: Knowledge is power!")
    else:
        pass
    $ renpy.pause(0.5)
    "Did you notice a pause?"
    "It's on purpose, using Renpy's 'Pause()' function."
    "Waiting a second here means the achievement notification can show
        for 'Knowledge is power!', then the game can end."
    "Unless you already have the achievement, then the notification won't show."
    "The achievement won't be granted until the game sends you to the title screen."

    "If you go to Preferences, then you should see a new button under Display."
    "Clicking this will clear all progress."
    "Seen text, achievements, persistents, etc."
    "There is no way to reverse this. You would have to play the game again and unlock everything again."

    "OK, a small explanation about achievements."
    "I used persistents to define it. This means that it is stored on your device
        so you can pick up at any point and have still have the achievments."
    "This can also being used for remembering endings or something like a
        character death, like in DDLC."
    "By using 'default' we can define the name of the persistent. If you look
        in the files and look in this script.rpy file in Atom or similar, you will
        see what I'm talking about."
    "After defining them, usually like 'persistent.NAME = False', somewhere in
        your code you can use '$ persistent.NAME = True' to change it's value.
        This will be remembered until cleared by you in the Launcher, deletion
        of the persistent file, or you make a button to wipe the file somewhere."
    "In my game, this one, I made an achievements screen which shows which
        achievements have been aquired."
    "This isn't something I'm going to explain just yet."

    "You will now be sent to the Main Menu and be granted the final achievement. I hope this helped!"
    $ persistent.achieve_2 = True

    return

################################################################################

##Ignore this for now.##
label clearProgress:
    $ persistent._clear(progress=True)
    call screen main_menu
##Ignore this for now.##

################################################################################

screen achievementScreen(): #Here is where the achievement screen lies.
    frame:
        padding(10, 10)
        align(0.5, 0.25)

        vbox:
            text "Oh, look at that...": #1
                size 25
                bold True
            if persistent.achieve_1 == True:
                align(1.0, 0.0)
                text "Start a new game!":
                    size 20
                    italic True
            else:
                align(1.0, 0.0)
                text "Locked.":
                    size 20
                    italic True
            text " "

            text "Knowledge is power!": #2
                size 25
                bold True
            if persistent.achieve_2 == True:
                align(1.0, 0.0)
                text "Complete the game for the first time.":
                    size 20
                    italic True
            else:
                align(1.0, 0.0)
                text "Locked.":
                    size 20
                    italic True

            text " "

            text "What does {i}this{/i} button do?": #3
                size 25
                bold True
            if persistent.achieve_3 == True:
                align(1.0, 0.0)
                text "Make a choice!":
                    size 20
                    italic True
            else:
                align(1.0, 0.0)
                text "Locked.":
                    size 20
                    italic True

            text " "

            text "Press ESC to leave.":
                align(0.0, 0.0)
                size 15
                italic True

            if main_menu:
                key "K_ESCAPE" action Hide("achievementScreen")
