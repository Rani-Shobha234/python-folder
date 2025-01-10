def play_game():
    """
    Assume that you have stucked in a dark room and play this game to come out.
    """
    playing = True
    current_room = "room1"

    while playing:
        if current_room == "room1":
            print("\n Your eyes are blur,Everythings seems black,you realise you are in a dark room,to the north.")
            print("To the south, you see a crumbled_door.you have no choice you should face it.")
            choice = input("Which way do you go? (north/south): ").lower()

            if choice == "north":
                current_room = "dark_room"
            elif choice == "south":
                current_room = "crumbled_door"
            else:
                print("Invalid choice. You remain in the dark room.")

        elif current_room == "dark_room":
            print("\nThe place grows darker as you move deeper. You hear a low growl.")
            print("You can try to **sneak** past or **fight** the creature.")
            choice = input("What do you do? (sneak/fight): ").lower()

            if choice == "sneak":
                print("You move silently through the undergrowth and avoid the creature.")
                current_room = "room3"
            elif choice == "fight":
                print("You bravely face the creature, but it's too strong! Game Over.")
                playing = False
            else:
                print("Invalid choice. You hesitate, and the creature attacks!")
                playing = False

        elif current_room == "crumbled_door":
            print("\nThe room2 is dilapidated, but you see a flickering light inside.")
            print("Do you **enter** the room2 or **turn back**?")
            choice = input("What do you do? (enter/turn back): ").lower()

            if choice == "enter":
                print("You enter the room and found a Mystery box.")
                print("A box filled with lots of gold and gems with a map.")
                print("To read the map, you must find the find mirror and read using mirror because the map is tricky .")
                current_room = "room1"  # Return to the clearing
            elif choice == "turn back":
                current_room = "room1"
            else:
                print("Invalid choice. You hesitate and decide to stay put.")

        elif current_room == "room3":
            print("\nYou've found a room3.")
            print("Do you **enter** the room or **turn back**?")
            choice = input("What do you do? (enter/turn back): ").lower()

            if choice == "enter":
                print("Finallyyy you find a mirror and use to reach destination.")
                print("You've reached your destination! Congratulations, you win!")
                playing = False
            elif choice == "turn back":
                current_room = "dark_room"
            else:
                print("Invalid choice. You hesitate and decide to stay put.")

play_game()