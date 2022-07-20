
from os import system
import random



lenght  = 50
robotX  = random.randint(1,49)
bombX1  = random.randint(1,49)
bombX2  = random.randint(1,49)
coin1   = random.randint(1,49)
coin2   = random.randint(1,49)
helf    = 5
heeling1= random.randint(1,49)
heeling2=random.randint(1,49)
charge  =100
consum  = 5
steps   =0

################## HP ######################
while helf>=1:
    system("clear")
    if robotX==bombX1 or robotX==bombX2:
        helf-=1
        print("You HP:", helf,"🧡", end="")  
        print()
    if robotX==heeling1 or robotX==heeling2:
        helf+=1
        print("You HP:", helf,"🧡", end="")
        print()
    if helf==0:
        print("🔴🔴🔴 Game over 🔴🔴🔴") 
        break
    
    if robotX==0:
        steps+=1
        print("🤖", end="")
        print()
        print("\n","You lost your robot")
        print()
        break

    if robotX==51:
        print("🤖", end="")
        print()
        print("\n","You lost your robot")
        print()
        break

    if robotX %2==0:
        charge-=consum
        print("🔋","You lose your energy:",charge,end="")
        print("\n")
    if robotX==coin1 or robotX==coin2:
        charge+=consum
        print("🔋","Your energy refill:",charge,end="")
        print("\n")
    if charge==0:
        print("💀💀💀💀 Your battery is dead 💀💀💀💀")
        print("\n")
        break    

############ DRAWING THR MAP #################
    x = 1
    print("\n")
    while x <= lenght:
        if x==robotX:
            print("🤖", end="")
        elif x == bombX1:
            print("💣", end="")
        elif x == bombX2:
            print("💣", end="")
        elif x==heeling1:
            print("🧡",end="")
        elif x==heeling2:
            print("🧡",end="")
        elif x==coin1:
            print("💰",end="")
        elif x==coin2:
            print("💰",end="")
        else:
            print("▪", end="")
        x+=1 
    print("\n")
    
#####################################
    direction = input("(a/d/x?)>") 

    if direction == "a":
        robotX-=1
    if direction == "d":
        robotX+=1
    if direction == "x":
        system("clear")
        print("Thanks for playing")
        break

######################################
