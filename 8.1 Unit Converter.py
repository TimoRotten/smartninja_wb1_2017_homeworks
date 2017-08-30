symbol = "*"

print symbol*80
print "Hello fellow Conversion Lover. You give kilometers, I give miles. Let's do this!"
print symbol*80

try:
    while True:
        input_km = int(raw_input("Please enter the amount of kilometers you want to convert: "))

        result = input_km * 0.621371

        print symbol*28
        print input_km, "km equate to", result, "mi"
        print symbol*28

        repeat = str(raw_input("Wanna convert more? (Y/N) "))
        if repeat == "N":
            print symbol * 7
            print "Bye Bye"
            print symbol * 7
            break
except:
    print symbol * 66
    print "Wrong input. Can't...process...Error! Error! (Insert numbers only)"
    print symbol * 66
