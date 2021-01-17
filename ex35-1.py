# Create comments in this source code.
# Draw a map of the game and how you flow through it.
# Sort flow  by asc.



from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bustard!")

def bear_room():
    print("There is bear here.")
    print("The Bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        print("You can select now number: ")
        print("1. Take honey\n2. Taunt bear.")
        choice = input("> ")

        #if choice == "take honey":
        if choice == '1':
            print("You want take honey.")
            dead("The bear looks at you than slaps your face off and his pissed off and chews your leg off.")

        elif choice == "2" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
            print("You are again taunt bear and his pissed off. His take attack you!")
            print("Press \"A\"")
            choice = input("> ")
            if choice == "A" and bear_moved:
                print("Slap bear with lowkick in his leg and second time middle kick in his torso strong . Now bear is down.")
                bear_moved = False
                print("Open the door, press \"D\"")
                choice = input("> ")
                if choice == "D" and not bear_moved:
                    print("Now you can get in gold room")
                    gold_room()
            else:
                print("You are fresh meet of Bear!")
                exit(0)
        else:
            print("I got no idea what that means")

def cthulhu_room():
    print("Here you see the great wvil Cthulhu.")
    print("He, it whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    print("What you gonna do now?\nPres number \"1\" if You gonna flee!\n or press number \"2\" if you gonna stay and fight!")

    choice = input("> ")

    if "1" in choice:
        start()
    elif "2" in choice:
        dead("Well that was tasty.")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your left and right.")
    print("Which one do you takechouse number?")
    print("1. left\n2. right")  # choice of move with numbe.
    choice = input("> ")

    if choice == "1":
        print("You are choice left")
        bear_room()
    elif choice == "2":
        print("You are choice right")
        cthulhu_room()
    else:
        print("Bad choice!")
        dead("You stumble around the room until you strave.")


start() #startuj prgoram prema definisan u funkciji def start():
