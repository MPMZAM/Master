print("Welcome To Secret Island Game")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print(r"""
        Will You Find The Key For The Treasure
                             _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
""")
print()
input_1 = input("There Is Two Doors In Front You: a Red Door 🔴 and the other door is Blue 🔵 (Please Type Red Or Blue)\n").lower()
print()
if input_1 == "red":
    print("Great You Entered The Room!")
    print()
    input_2 = input("""There are Three Presents: The First is a Red Present 🔴 
                          The Second is a Blue Present 🔵
                          The Third is a Yellow Present 🟡
                    
Choose one of them (Type Red or Blue Or Yellow)
""").lower()
    print()
    if input_2 == "red":
        print("This Present is Full of Spiders! 🕷🕷🕷")
        print()
        print()
    elif input_2 == "blue":
        print("This Present is Full Of Snakes! 🐍🐍🐍")
        print()
        print()
    elif input_2 == "yellow":
        print("You won! The Present Contains The Key Of The Treasure 🔑🔑🔑")
        print()
        print()
    else:
        print("Invalid Choice!")
        print()
        print()
elif input_1 == "blue":
    print("You Entered The Wrong Room and The Crocodiles ate You 🐊🐊🐊")
    print()
    print()
else:
    print("Invalid Choice!")
    print()
    print()