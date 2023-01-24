from hammer import gavel
import os

greet = "! WELCOME TO THE SILENT AUCTION PROGRAM !"
section = "-" * 65
win_section = "=" * 65
auction_run = True
person = {}
people = []

print(section)
print(greet.center(len(section)))
print(gavel)
print(section)

while auction_run:
    name_valid = False
    bid_valid = False

    while not name_valid:
        name = input("Your name: ")
        if name.isalpha():
            name_valid = True
        else:
             print("The name is not written in the correct format, please try again.")


    while not bid_valid:
        bid = input("What is your offer in dollars? ")
        if bid.isdigit():
            bid_valid = True
        else:
            print("The offer is not written in the correct format, please try again.") 

    person[name] = bid
    people.append(person)

    another_person = input("\nSomeone else with an offer? 'Yes' or another sign for 'no': ")
    if another_person == "yes":
        auction_run
        print(section)
    else:
        print("End of auction..")
        auction_run = False


max = 0
winner = ""
for dict in people:
    for key, value in dict.items():
        if int(value) > max:
            max = int(value)
            winner = key

os.system("cls")
print(gavel)
print(win_section)
print(f"The winner is {winner} with an offer {max} dollar.".center(len(win_section)))
print(win_section)