# 2. order completions? (yes/no - True/False)
#      - select food
#      - confirm order (online)
#      - enter client info
#      - delivery info
#      - payment
#      - delivery (physical)
#      - client satisfied 
#####################



food_1_name= "Pizaa"
food_1_price=75.00
food_1_quantity=1

print("Do you want", food_1_name, "(yes/no)? ")
food_1_confirm=input()

if food_1_confirm== "yes":
    food_1_quantity=int(input("How many?"))
    food_1_cost    = food_1_price * food_1_quantity
    print(food_1_name, "x",food_1_quantity, "=", food_1_cost)

    confirm_order=input("confirm order (yes/no)")
    if confirm_order == "yes":
        client_informations=input("Enter your adress delivery:") and input("Enter your name:")
        payment_method=input("cash or bankcard?")
        if payment_method == 'bankcard':
            bankcard=(input("Enter your bankcard:"))
            print(food_1_quantity,food_1_name,"You payd:",food_1_cost,".",client_informations, ",Yor order will bee an hour.")
            if payment_method =='cash':
                print(food_1_quantity,food_1_name,"You must pay:",food_1_cost,".",client_informations, ",Yor order will bee an hour.")

            confirm_delivery_order=input('have you recived your order? (yes/no)')
            if confirm_delivery_order == 'yes':
                client_satisfactions=int(input('Can you rate the service from 1-10?'))
                print("Thank's for choosing")
            elif confirm_delivery_order == 'no':
                    phone_number=int(input('We are sorry, the courier will contact you in a few minutes.Text your phonenumber:'))

