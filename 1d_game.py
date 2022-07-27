from os import system
import random



########### VARIABLES #################
w = int(random.randint(1,10))    #bomb
x = int(random.randint(1,10))



while True:
    system('clear')
################ MAP ############
    print()
    n=1
    
    while n <= 10:
    
        if n == w:
            print( "🚤", end="" )
        
        elif n == x:
            print( "💣", end="" )
        else:
            print( "~", end="" )
        n += 1
    print()
   
################ MAP ############


############# ITERACTION ############
    
    diretion = input ("Enter direction (a,d):")
    if diretion == 'a':
        w-=1
    elif diretion == 'd':
        w +=1
    
    if w == x:
        print("BOOOOOOOOM!")
        break
    if w == 0:
        n+=1
        print("\n","You lost your boat")
        break

    if w==11:
        n+=1
        print("\n","You lost your boat")
        break


    