import random

number = random.randint(1,10)
guess = input("What's the number?")
guess = int(guess)


def main():
    while guess != number:
        if guess > number:
            print("Too high. Guess lower.")
        elif guess < number:
            print("Too low. Guess higher.")
        elif guess == number:
            print("You Win!")
        else:
            print("Invalid input.")

def play_again():
    repeat = input("Want to play again Yes or No?")
    if repeat == "Yes":
        main()
    elif repeat == "No":
        print("Okay see you later!")
    else:
        print("Invalid input.")


main()
play_again()