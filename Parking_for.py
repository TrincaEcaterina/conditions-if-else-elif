

PARKING_PLACES=7
FREE_PLACES=int(input("How many places do you need?"))

print('#'*PARKING_PLACES*5)   
for place_index in range(1, PARKING_PLACES+1): 
    print("|X|", end="") 
print("\n","#"*PARKING_PLACES*5, sep="") 
if 0<FREE_PLACES<2:
      print("You can see your place:")
      print('#'*PARKING_PLACES*5)
      print("|X|"*2,"|    |","|X|"*3,end="")
      print("\n","#"*PARKING_PLACES*5, sep="")
else:
     print("Sorry, we don't have free places for parking")
    

# '\n' - перенести на новую строку
# sep''- пробел или строка необходимую ставить между значениями