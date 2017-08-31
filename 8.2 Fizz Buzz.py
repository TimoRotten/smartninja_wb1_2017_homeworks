

try:
    input = int(raw_input("Select a number between 1 and 100: "))
    for num in range(1, input+1):
        if num % 3 and num % 5 == 0:
            print "fizzbuzz"
        elif num % 3 == 0:
            print "fizz"
        elif num % 5 == 0:
            print "buzz"
        else:
            print num
except:
    print "That wasn't a number. You killed it. Nice work."
