# coding=utf-8

import random

welcome_message = "Program: Welcome to the lottery numbers generator."
prompt = "Program: Please enter how many random numbers you would like to generate: "

print welcome_message
answer = raw_input(prompt)
try:
    answer = int(answer)
    print sorted(random.sample(range(1, 50), answer))
    print "Program: END"
except ValueError as e:
    print "Input not supported. Please enter numbers only."


