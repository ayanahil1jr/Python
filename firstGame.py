import time

print("\n" * 100)

print("Welcome to my first game!")
time.sleep(2)
print("Have fun")
time.sleep(2)
print("\n" * 100)
while True:
    print("You spawn in a suspicious looking forest.")
    time.sleep(2)
    print("\n" * 100)
    print("You see 2 pathways")
    time.sleep(1)
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
        break
    elif location1 != "right" and location1 != "left":
        print("Invalid location")
        retry = input("Would you like to try again?: ")
        if retry != "yes" and retry != "no":
          print("Invalid retry option")
        retry = input("Would you like to try again?: ")
        if retry == "no":
             break