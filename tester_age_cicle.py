from random import randint

n=1

while n<=20:
    age=randint(-1,150)
    print("The age:",age,"years.")
    if age>122:
        print("We regret.Error occurred")
    elif age<=1 and age<=3:
        print('You are "baby".')
    elif age<=4 and age<=9:
        print('You are "kid".')
    elif age<=10 and age<=15:
        print('you are a "teenager".')
    elif age<=16 and age<=18:
        print('You are "younger".')
    elif age<=19 and age<=50:
        print('You are "adult".')
    elif age<=51 and age<=100:
        print('You are "old".')
    else:
        print("You can't pass")
    print()
    n+=1

