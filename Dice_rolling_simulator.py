import random
def dice_simulate():
    number = random.randint(1,6)
    print(number)
    while(1):
       flag = str(input("Do you want to dice it up again:if yes,Enter 1 and else enter 0"))
       if flag == '1':
         number = random.randint(1,6)
         print(number)
       else:
         print("ending the game")
         return

dice_simulate() 