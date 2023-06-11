
import random

def Chosen(who, num):  
    if(num == 1):    
        print(who + "Rock") 
    elif(num == 2):      
        print(who + "Paper")
    elif(num == 3):    
        print(who + "Scissors")        
    else:        
        print("Invalid. Try again.")
        
def winner(num, comp):   
    if((num == 1 and comp == 3) or (num == 2 and comp == 1) or (num == 3 and comp == 2)):    
        print("You have won this round!")    
        return 1  
    elif((num == 3 and comp == 1) or (num == 1 and comp == 2) or (num == 2 and comp == 3)):  
        print("The computer has won this round!")       
        return 2   
    else:        
        print("It's a draw. Try again")  
        return 3 

you = 0
computer = 0

for i in range(3):
    print("Choose a number: ") 
    num = int(input("1. Rock 2.Paper 3.Scissors: "))

    Chosen("You have chosen ", num)
    if(num >=1 and num <=3): 
        comp = random.randint(1,3)   
        Chosen("The computer has chosen ", comp)    
        player = winner(num, comp)

        if(player == 1):
            you = you + 1
        elif(player == 2):
            computer = computer + 1
        
if(you == computer):
    print("It's a draw")
elif(you > computer):
    print("You have won the game")
else:
    print("The computer has won the game")
