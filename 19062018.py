#guessing the number game

#get the user to guess a number
guess_number = int(input("Guess a number between 1 - 10"))

#check if the number is equal to the actual number which we will assume to be 5
#if the number is correct display a correct guess message
#else display a wrong message

if guess_number < 5:
    print("")