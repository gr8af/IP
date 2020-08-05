import simplegui
import random

secret_number = random.randrange(0, 100)
num_range = 100
total_guess = 7
x = 0

# Event Handlers

def new_game():
    print("")
    if (x == 0):
        global secret_number, num_range, total_guess
        num_range = 100
        total_guess = 7
        secret_number = random.randrange(0, num_range)
        
    print("New game. Range is from 0 to "+str(num_range))
    print("Number of remaining guesses is "+str(total_guess))
    print("")
    frame.start()
    
def range100():
    global secret_number, num_range, total_guess, x
    num_range = 100
    total_guess = 7
    secret_number = random.randrange(0, num_range)
    x = 1
    new_game()

def range1000():
    global secret_number, num_range, total_guess, x
    num_range = 1000
    total_guess = 10
    secret_number = random.randrange(0, num_range)
    x = 1
    new_game()

def input_guess(guess):
    global guess_number, secret_number, total_guess, x
    guess_number = int(guess)
    print("Guess was "+ str(guess_number))
    if (total_guess == 0):
        print("You ran out of guesses. The number was "+str(secret_number))
        new_game()
    if (guess_number == secret_number):
        x = 0
        print("Correct!!")
        new_game()
    elif (guess_number > secret_number):
        total_guess -= 1
        print("Number of remaining guesses is "+ str(total_guess))
        print("Lower")
    elif (guess_number < secret_number):
        total_guess -= 1
        print("Number of remaining guesses is "+ str(total_guess))
        print("Higher")
    else:
        print("Bad Input")
    print("")

# Frame

frame = simplegui.create_frame("Guess the Number", 200, 200)

# Register Event Handlers

frame.add_button("Range is [0,100)", range100, 100)
frame.add_button("Range is [0,1000)", range1000, 100)
input_number = frame.add_input("Enter a guess", input_guess, 200)

# Start Frame and game

new_game()
frame.start()