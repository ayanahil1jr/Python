import time

print("\n" * 100)

print("Welcome to my first game!")
time.sleep(2)
print("Have fun")
time.sleep(2)
print("\n" * 100)
while True:
    print("You spawn in a suspicious looking forest.")
    time.sleep(3)
    print("\n" * 100)
    print("You see 2 pathways")
    time.sleep(2)
    print("\n")
    print("right")
    print("left")
    print("\n")
    time.sleep(1)
    location1 = input("Where would you like to go?: ")

    if location1 == "right":
        print("*You chose to walk right*......")
        time.sleep(3)
        print("A Big Bear attacked you and you died!!")
        retry = input("would you like to try again?: ")
        if retry != "yes" and retry != "no":
            print("Invalid input")
            retry = input("would you like to try again?: ")
        if retry == "no":
            break
    elif location1 == "left":
        print("*You chose to walk left*......")
        time.sleep(3)
        print("You chose the right path!!!")
        time.sleep(2)
    elif location1 != "right" and location1 != "left":
        print("Invalid location")
        retry = input("Would you like to try again?: ")
        if retry != "yes" and retry != "no":
          print("Invalid retry option")
        retry = input("Would you like to try again?: ")
        if retry == "no":
             break


    if location1 == "left":
        print("*You keep walking*")
        time.sleep(1)
        print("You see a tree that is awfully waving alot")
        time.sleep(2)
        print("You decide to check it out, but stop before you keep moving")
        time.sleep(3)
        checkOutTree = input("Would you like to check out the tree?: ")

        if checkOutTree == "no":
            print("\n" * 100)
            print("Alright then")
            time.sleep(1)
            break
        if checkOutTree == "yes":
            print("You walk towards the tree...")
            time.sleep(2)
            print("IT GRABS YOU")
            time.sleep(1)
            print("You try to wiggle your way out, but you cant.")
            time.sleep(2)
            print("\n" * 1)
            print("You Fall Unconscious")
            break
