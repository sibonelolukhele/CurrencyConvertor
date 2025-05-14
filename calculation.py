import conlib

ask = True
count = True

def inputamount():
    a = True
    b = True
    c = True 
    d = True

    currencies = ["USD", "ZAR", "EUR", "GBP", "AUD", "NZD", "JPY", "CHF"]

    while a:

        while b:
            currency1 = input("\nselect the currency you'd like to convert FROM or input 'exit' to close the app:\n1.USD \n2.ZAR \n3.EUR \n4.GBP \n5.AUD \n6.NZD \n7.JPY \n8.CHF\n:")
            if currency1.upper().strip() in currencies:
                b = False
                None
            elif currency1.upper().strip() == "EXIT":
                print("\nSee you next time!\n")
                exit()
            else:
                print("Please enter a valid answer!")
                
            
        while c:
            currency2 = input("\nselect the currency you'd like to convert TO or input 'exit' to close the app:\n1.USD \n2.ZAR \n3.EUR \n4.GBP \n5.AUD \n6.NZD \n7.JPY \n8.CHF\n:")
            
            if currency2.upper().strip() in currencies:
                c = False
                None
            elif currency2.upper().strip() == "EXIT":
                print("\nSee you next time!\n")
                exit()
            else:
                print("Please enter a valid answer!")
                
        
        
        while d:
            amount = input(f"Enter the amount in {currency1.upper().strip()} that you'd like to convert to {currency1.upper().strip()} or input 'exit' to close the app: ")

            if amount.isdigit():
                calculation(int(amount), currency1.upper().strip(), currency2.upper().strip())
                d = False
            elif amount.upper().strip() == "EXIT":
                print("\nSee you next time!\n")
                exit()

            else:
                print("\nPlease enter a numeric value or enter done to exit!\n")


def calculation(answer, currency1, currency2):
    currencycon = conlib.conlibrary(currency1, currency2)    
    con = float(answer)* currencycon 
    print(f"\nYou have {round(con, 2)} {currency2}\n")
    inputamount()
