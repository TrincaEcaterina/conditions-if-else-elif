# App where:
# IN money amount
# IN currency
# OUT money amount



in_money            =int(input("Enter summa: ")) 
if in_money < 1000000:
   print("You can't exchange amount less than 1000000")
else:
    in_currency      =input("What currency do you want to exchange? ")
    exchange_currency=input("what currency would you like to exchange for? : ")
    data_USD_to_EUR_rate=0.8
    data_EUR_to_USD_rate=1.25
    data_EUR_to_MDL_rate=19.71
    data_USD_to_MDL_rate=19.14

    if in_currency=="USD" and exchange_currency=="EUR":
       out_money= in_money * data_USD_to_EUR_rate
       print("Your amount at today's exchange rate: ",out_money )  
    elif in_currency=="USD" and exchange_currency=="MDL":
        out_money= in_money * data_USD_to_MDL_rate
        print("Your amount at today's exchange rate: ",out_money )
    if in_currency=="EUR" and exchange_currency=="USD":
       out_money=in_money * data_EUR_to_USD_rate
       print("Your amount at today's exchange rate: ",out_money )
    elif in_currency=="EUR" and exchange_currency=="MDL":
        out_money= in_money * data_EUR_to_MDL_rate
        print("Your amount at today's exchange rate: ",out_money )
    

