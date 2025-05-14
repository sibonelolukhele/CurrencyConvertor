import conlib

ask = True
count = True

def inputamount():
    ask = True
    count = True
    currencies = ["USD", "ZAR", "EUR", "GBP", "AUD", "NZD", "JPY", "CHF"]

    while ask:

        currency1 = input("select the currency you'd like to convert FROM or input 'exit' to close the app:\n1.USD \n2.ZAR \n3.EUR \n4.GBP \n5.AUD \n6.NZD \n7.JPY \n8.CHF\n:")
        if currency1.upper().strip() in currencies:
            None
        elif currency1.upper().strip() == "EXIT":
            print("See you next time!")
            exit()
        else:
            print("Please enter a valid answer!")
            inputamount()
            

        currency2 = input("select the currency you'd like to convert TO or input 'exit' to close the app:\n1.USD \n2.ZAR \n3.EUR \n4.GBP \n5.AUD \n6.NZD \n7.JPY \nCHF\n:")
        
        if currency2.upper().strip() in currencies:
            None
        elif currency2.upper().strip() == "EXIT":
            print("See you next time!")
            exit()
        else:
            print("Please enter a valid answer!")
            inputamount()
        
        
        while count:
            amount = input(f"Enter the amount in {currency1.upper().strip()} that you'd like to convert to {currency1.upper().strip()} or input 'exit' to close the app: ")

            if amount.isdigit():
                calculation(int(amount), currency1.upper().strip(), currency2.upper().strip())
                count = False

            elif answer.upper().strip() == "EXIT":
                print("See you next time!")
                exit()

            else:
                print("\nPlease enter a numeric value or enter done to exit!\n")
                

def calculation(answer, currency1, currency2):
    currencycon = conlib.conlibrary(currency1, currency2)    
    con = float(answer)* currencycon 
    print(f"\nYou have R{round(con, 2)}\n")
    inputamount()
