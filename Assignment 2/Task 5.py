print("\tWelcome to No guessing Game")
guess = 0
while guess != 6:
    guess = int(input("Guess the number.\nHints: No is single digit:- "))
    if guess == 6:
        print("Your guessed no is correct")
        break
    