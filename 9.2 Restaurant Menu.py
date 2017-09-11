# coding=utf-8

filename = "menu.txt"

print "Welcome to your Daily Menu program."
print "*"*50

menu = {}

while True:
    daily_menu = str(raw_input("Please enter the menu of today: "))
    daily_price = float(raw_input("Please enter the price of today's menu: "))
    print "*" * 50
    print "Your menu of today is %s and costs %d€." % (daily_menu, daily_price)
    print "*" * 50
    menu[daily_menu] = daily_price

    new_menu = str(raw_input("Would you like to add another menu to your list? (Y/N): "))
    if new_menu.lower() == "n" or new_menu.lower() == "no":
        break

print "*"*50

with open("menu.txt", "w+") as menu_file:
    print "Your daily menu:"
    for item in menu:
        print "- %s: %d€" % (item, menu[item])
        menu_file.write("- %s: %d€" % (item, menu[item]) + "\n")

print "Thank you. See you tomorrow."
