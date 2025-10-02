print(
    r""""
                  
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|



                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\ ||
              `>'-.!@%()@'@_%-'_.-o _.|'||                  
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\ /.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'

"""
    """"""
)

print("WELCOME TO TREASURE ISLAND")
ready = input("Are you ready ?").lower()

if ready == "yes":
    print("INSTRUCTION:\nYour mission is to find the treasure.")

    direction = input("Where do you want to go\n  Type 'left' or 'right'?").lower()
    if direction == "left":
        print("you have came to a lake. There is an island in the middle of the lake.")

        choice = input(
            "Type 'wait' to wait for a boat. Type 'swim' to swim across -"
        ).lower()
        if choice == "wait":

            door = input(" You saw a house there is 3 door..\n Which color you want to choose  ? RED YELLOW and BLUE :").lower()
            if door == "yellow":
                print("CONGRATULATIONS \n you win You found a TREASURE WITH FULL OF GOLDS.")
            elif door == "blue" or door == "red":
                print(
                    r""" 
                                         __,,,,_
                            _ __..-;''`--/'/ /.,-`-.
                        (`/' ` |  \/ \/ \/\/ / / / / .-'/`,_
                        /*`\ \   |  \ | \| // // / -.,/_,'-,
                       a /<7' ;  \ \  | ; ||/ /| | \/  |`-/,/-.,_,')
                      /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\/'
                      `-`  f/ ;      / __/ \__ `/ |__/ |
                            `-'      |  -| =|\_  \  |-'|
                                _____/   /_..-' `  ),' /
                            fL ((___ _ _/((___..-'' \_/
                            """
                )

                print("GAME OVER !! you were attack by TIGER")

            else:
                print(" Sorry Invalid color door (not in option)")

        else:
            print("game over!! You were eaten by 'shark' , try again. ")
    else:
        print(
            "GAME OVER !! type only 'left' or 'right' that has been given in the options.\nSTART AGAIN."
        )
else:
    print("Ok !! Than exit the game")
