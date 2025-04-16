import conlib

ask = True

def inputamount():

    while ask:
        answer = input("Enter how much you'd like to convert TO ZAR (in USD) or enter done to exit: ")
        
        if answer.isdigit():
            calculation(int(answer))

        elif answer.lower() == "done":
            print("See you next time!")
            loop=False
            break

        else:
            print("\nPlease enter a numeric value or enter done to exit!\n")

def calculation(answer):
    zar = conlib.conlibrary()    
    con = float(answer)* zar
    print(f"\nYou have R{round(con, 2)}\n")
