

secret = 7
guess = 0

while True:
    guess = int(raw_input("Please guess the secret number: "))

    if guess == secret:
        print "That's right! You're a psychic from 7th heaven."
        break
    elif guess > secret:
        print "That's wrong. It's the smaller things in life that matter."
    elif guess < secret:
        print "That's wrong. Go bigger or go home!"

