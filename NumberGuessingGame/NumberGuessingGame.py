import random


while True:
    attempts = 0

    difficulty = input("Choose difficulty level (easy, medium, hard, impossible): ").lower()

    if difficulty == "easy":
        cap = 50;
    elif difficulty == "medium":
        cap = 100;
    elif difficulty == "hard":
        cap = 200;
    elif difficulty == "impossible":
        cap = 1000;
    
    number = random.randint(1, cap)


    while True:
        guess = input("Guess a number between 1 and " + str(cap) + "" + ": ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break

    playAgain = input("Do you want to play again? (yes/no): ").lower()

    if playAgain == "yes":
        continue
    elif playAgain == "no":
        print("Thanks for playing!")
        break
    

