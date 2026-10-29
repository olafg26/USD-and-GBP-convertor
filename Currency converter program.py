#CURRENCY CHOICE
convertion = input("Are you converting USD or GBP today? ")

#CONDITIONAL BLOCK
if convertion == "USD":

#USD to GBP
    USD = float(input("Enter the amount of USD you want to convert: "))
    USDtoGBP = USD * 0.75
    print(f"Your USD are worth around {USDtoGBP:.2f}GBP.")

#GBP to USD
elif convertion == "GBP":
    GBP = float(input("Enter the amount of GBP you want to convert: "))
    GBPtoUSD = GBP * 1.34
    print(f"Your GBP are worth around {GBPtoUSD:.2f}USD.")

