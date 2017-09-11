# coding=utf-8

import random       # random ist ist python selbst integriert (External Libraries)

welcome_message = "Program: Welcome to the lottery numbers generator."
prompt = "Program: Please enter how many random numbers you would like to generate: "


# *****************************************

def generate_numbers(amount):
    lottery_list = []
    for i in range(amount):
        lottery_list.append(random.randint(0, 49))
    return sorted(lottery_list)

# *****************************************
# So werden Zahlen auch doppelt ausgegeben!
# Let's try again!
# while ist die bessere Wahl als for/in


def generate_numbers(amount):
    lottery_list = []
    while len(lottery_list)<amount:
        new_number = random.randint(0, 49)
        if new_number not in lottery_list:
            lottery_list.append(new_number)
    return sorted(lottery_list)


print welcome_message
answer = raw_input(prompt)
try:
    answer = int(answer)
    print generate_numbers(answer)
    print "Program: END"
except ValueError as e:
    print "Input not supported. Please enter numbers only."






