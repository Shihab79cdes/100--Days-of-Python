# Treasure island (LOGIC is bad though but i have fully done by myslef)
print("Welcome to treasure island")
ready = input("Are you ready ?")
mission = input("Your mission is to find the treasure.")
go = input("Where do you want to go \n    Type ''left or 'right'?")

# # step1

if go == "left" or not go == "right":
    print("you've have came to a lake. There is an island in the middle of the lake.")
    came = input("Type 'wait' to wait for a Boat. Type 'swim' to swim across.")

    # step2
    if came == "wait" or not came == "swim":
        door = input("Which door? Red,Blue and yellow :")

        # step3
        if door == "blue" or door == "red" or not door == "yellow":
            print("game over\nyou fail !!")
        else:
            print("you win !!\nCONGRALUTIONS..")

    else:
        print("game over\nyou fail !!.")
else:
    print("game over\nyou fail !!.")
