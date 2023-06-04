print("Welcome to the Treasure Island. Your mission is to find the treasure")

direction = input("Left or right? ")
if direction.lower() == "left":
    travel = input("Swim or wait? ")
    if travel.lower() == "wait":
        door = input("Red, yellow or blue door? ")
        if door.lower() == "yellow":
            print("You Win!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")
