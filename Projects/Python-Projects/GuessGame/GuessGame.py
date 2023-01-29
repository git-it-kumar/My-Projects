import random  # bring in the random number
import time

number = random.randint(1, 200)  # selecting a random number between 1 and 200

def starts():
    global name
    print("please enter your name:")
    name = input()  # asks for the name
    print("Hello " + name + ", I am thinking of a number between 1 and 200, you have to guess it within 10 attempts")
    time.sleep(.5)
    print("Let's begin!!!")

def guesses():
    guessesNo = 0
    while guessesNo < 10:  # if the number of guesses is less than 10
        time.sleep(.25)
        enter = input("Guess: ")  # inserts the place to enter guess
        try:  # check if a number was entered
            guess = int(enter)  # stores the guess as an integer instead of a string

            if guess <= 200 and guess >= 1:  # if they are in range
                guessesNo = guessesNo + 1  # adds one guess each time the player is wrong
                if guessesNo < 10:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    if guess > number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                if guess == number:
                    break  # if the guess is right, then we are going to jump out of the while block
            if guess > 200 or guess < 1:  # if they aren't in the range
                print("Nah! That's not even in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")

        except:  # if a number wasn't entered
            print("I don't think that " + enter + " is a number. Sorry")

    if guess == number:
        guessesNo = str(guessesNo)
        print('Good job, ' + name + '! You guessed my number in ' + guessesNo + ' guesses!')

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))


playagain = "y"
while playagain == "y" or playagain == "Y":
    starts()
    guesses()
    print("Do you want to play again? If yes, type y and press enter key on your keyboard")
    playagain = input()