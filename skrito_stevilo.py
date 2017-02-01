secret = 22

guess = int(raw_input("Guess the secret number"))

if guess == secret:
    print "Congratulations! You guessed it. Secret guess is " +str(guess)

else:
    print "Sorry your guess is incorrect!"