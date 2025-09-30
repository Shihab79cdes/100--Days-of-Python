print("Wecome to Treasure island.")
print("your mission is to find the treasure.")
choice= input('you\'are at a crossroad, where do you want to go?'
'Type "left" or "right".')

if choice =="left":
    choice2=input('You have come to lake.'
        'There is an island in the middle of the lake.'
        'Type "wait" to wait for a boat.'
        'Type "swim" to swim across.')
    if choice2=="wait":

        choice3=input("You arrived at the island unharmed."
        "There is house wtih 3 doors. One red,"
        "One yellow and One blue."
        " Which colour do you choose?")

        if choice3=="red":
            print("It is a room full of fire. Game over")
        elif choice3=="yellow":
            print("You found the treasure you win!")
        elif choice3=="blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("you chose a door that doesn't exit.Game over!")

    else:
        print("You got attacked by angry trout. Game over")
else:
    print("You fell in to a hole. Game over.")
