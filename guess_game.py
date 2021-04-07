from random import randint

guesses = []
finished = False
Actual = None
val1 = None
val2 = None
diff1 = None
diff2 = None
trials = 0

Actual = randint(0, 101)
Actual
# print("Actual", Actual)

valid = False

print("\n")
print("**************************************")
print("*           GAME STARTED             *")
print("**************************************", "\n")
while finished == False:

    user_input = input("Please Enter a number from 1 to 100: ")
    print("\n")

    Guess = user_input

    while valid == False:
        if Guess == '':
            Guess = input(
                "YOU DIDN'T ENTER ANY THING, Please Enter a value from 1 to 100: ")

        elif Guess.isalpha():
            Guess = input(
                "YOU DIDN'T ENTER A NUMERIC VALUE, Please Enter a value from 1 to 100: ")
        else:
            valid == True
            break

    Guess = int(Guess)
    while Guess < 1 or Guess > 100:
        Guess = int(
            input("OUT OF BOUNDARIES, Please Enter a value from 1 to 100: "))
    trials = trials + 1
    guesses.append(Guess)

    print("**********************************************************")
    print('------- You are in the trial number: {} -------'.format(trials))
    print('------- Your guesses is/are: {} --------'.format(guesses))
    print("**********************************************************")
    print("\n")

    # Change None to Correct Boolean between
    if guesses[-1] == Actual or diff1 == Actual or diff2 == Actual:
        print("Wow, you've guessed Correctly this time")  # Fix
        # Put function that calculate the Real Number of Guesses
        print('You have guessed it in {} times'.format(trials))
        print("\n")
        print("##################### END OF THE GAME ####################")
        finished == False
        break

    if len(guesses) == 1:
        pass
    else:
        val1 = guesses[-1]
        val2 = guesses[-2]
        diff1 = Actual - val1
        diff2 = Actual - val2

        # print("value1: ", val1)
        # print("value2: ", val2)
        # print("diff1: ", diff1)
        # print("diff2: ", diff2)

        if abs(diff1) < abs(diff2) and not (guesses[-1] == Actual or diff1 == Actual or diff2 == Actual):
            print('       Come on, you are closer to target       ')
            print("\n")

        elif abs(diff1) > abs(diff2) and not (guesses[-1] == Actual or diff1 == Actual or diff2 == Actual):
            print('       Keep your Attention, you are far from the target        ')
            print("\n")

        elif abs(diff1) == abs(diff2) and not (guesses[-1] == Actual or diff1 == Actual or diff2 == Actual):
            print('       You are still at the same distance       ')
            print("\n")

        elif guesses[-1] == Actual or diff1 == Actual or diff2 == Actual:
            print("**********************************************************")
            print("Wow, you've guessed Correctly this time")  # Fix
            # Put function that calculate the Real Number of Guesses
            print('You have guessed it in {} times'.format(trials))
            finished = True
            print("**********************************************************")
            print("##################### END OF THE GAME ####################")
            break
