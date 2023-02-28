# Lab 1
# Group 3
# Authors: Henry Penas, Anthony Mariscal 
# Date: 02/06/2023


# Current conversion rate: 1 USD to EURO = 0.93

def usd_to_eur(usd):
    return round(usd * 0.93, 2)

def eur_to_usd(eur):
    return round(eur / 0.93, 2)

print("*** This program converts currency between USD and Euros ***")
print("Enter 1 for USD to Euros, 2 for Euros to USD")
option = int(input("Choose your Option: "))

# USD to Euro conversion
if option == 1:
    usd = float(input("Amount USD to Euros: "))
    eur = usd_to_eur(usd)
    print(f"{usd} US Dollars = {eur} Euros")

# Euro to USD conversion
elif option == 2:
    eur = float(input("Amount Euros to USD: "))
    usd = eur_to_usd(eur)
    print(f"{eur} Euros = {usd} US Dollars")

else:
    print("Invalid option, choose 1 or 2")