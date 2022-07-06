# Считать с клавиятуры год рождения человека в 4-х цифрах:
# допускаються значение начиинающиеся с 1900-2022
# вычеслить возрост в годах и вывести
# Оцениваем возраст словами и выводим сообщение :
#            1-3 года  - "baby"
#            4-9 лет   - "kid"
#            10-15 лет - "teen"
#            16-18 лет - "young"
#            19-50 лет - "adult"
#            51 + лет  - "old"
#
####################################################################

present_year=2022
years=int(input("What year you born in?"))
age= present_year -  years
if(age>122):
    print("We regret.Error occurred")
elif(age<=1) and (age<=3):
    print('You are "baby".')
elif(age<=4) or (age<=9):
    print('You are "kid".')
elif (age<=10) or (age<=15):
    print('you are a "teenager".')
elif (age<=16) or (age<=18):
    print('You are "younger".')
elif (age<=19) or(age<=50):
    print('You are "adult".')
elif (age<=51) or (age<=100):
    print('You are "old".')
else:
    print("you can't pass")