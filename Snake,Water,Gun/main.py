import random

def game(com,player):
    if com == player:
        return None
    
    elif com == 's':
        if player == 'w':
            return False
        else:
            return True

    elif com == 'w':
        if player == 'g':
            return False
        else:
            return True
            
    elif com == 'g':
        if player == 's':
            return False
        else:
            return True    

ran = random.randint(1,3)
player = input("Enter 's' for snake or 'w' for water or 'g' for gun: ")

if ran==1:
    com = "s"
elif ran==2:
    com = "w"
else:
    com = "g"

result = game(com,player)

if result == None:
    print(f"Tie \n you entered {player} and computer entered {com}")
elif result == True:
    print(f"You won \n you entered {player} and computer entered {com}")
else:
    print(f"You lose \n you entered {player} and computer entered {com}")




