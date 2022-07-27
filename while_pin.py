# allow user > enter PIn > True 

correct_PIN  = 1234
wrong        = True
attempts     = 1


while wrong:
    user_PIN = int(input("Enter PIN: "))
    print("You used ",attempts, "attempts")
    attempts+=1
    if attempts >=4:
        print("You have used all attempts! ")
        wrong = False    
    elif user_PIN == correct_PIN:
        print("YES!!!")
        wrong = False

    else:
        print("WRONG!!!")


