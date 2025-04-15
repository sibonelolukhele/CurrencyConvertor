usd = 1.00
zar = 18.25

print("Welcome to the Currency Converter\n")

answer = input("Enter how much you'd like to convert (in USD): ")
con = float(answer)* zar

print("\nYou have", round(con, 2), "ZAR")
