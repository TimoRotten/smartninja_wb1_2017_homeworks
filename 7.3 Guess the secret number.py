secret = 7
guess = int(raw_input("Please guess the secret number: "))

if guess == secret:
    print "That's right! You're a psychic from 7th heaven."
else:
    print "Eeh! Wrong. Sorry."