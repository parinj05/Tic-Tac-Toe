def print_board(Board):
    print(Board[6]+'|'+Board[7]+'|'+Board[8])
    print('-'+'+'+'-'+'+'+'-')
    print(Board[3]+'|'+Board[4]+'|'+Board[5])
    print('-'+'+'+'-'+'+'+'-')
    print(Board[0]+'|'+Board[1]+'|'+Board[2])

def game():
    player='X'
    count=0
    position=' '
    Board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print("Welcome to Tic Tac Toe")
    for i in range(10):

        position = input("It's "+ player + "'s turn." + "Where do you want to place your move? ")
        count+=1
        
        if int(position)>0 and int(position)<10:
            if Board[int(position)-1]==' ':
                Board[int(position)-1]=player
                print_board(Board)
            else: 
                print("Space not empty.")
                continue
        else:
            print("Not a valid position.")
            continue

        if count>=5:
            if Board[0]==player and Board[1]==player and Board[2]==player:
                print("***"+player+" won. Game over***")
                game_continue()
                break    
            elif Board[3]==player and Board[4]==player and Board[5]==player:
                print("***"+player+" won. Game over***")
                game_continue() 
                break
            elif Board[6]==player and Board[7]==player and Board[8]==player:
                print("***"+player+" won. Game over***")
                game_continue()
                break 
            elif Board[0]==player and Board[3]==player and Board[6]==player:
                print("***"+player+" won. Game over***")
                game_continue() 
                break
            elif Board[1]==player and Board[4]==player and Board[7]==player:
                print("***"+player+" won. Game over***")
                game_continue() 
                break    
            elif Board[2]==player and Board[5]==player and Board[8]==player:
                print("***"+player+" won. Game over***")
                game_continue() 
                break
            elif Board[0]==player and Board[4]==player and Board[8]==player:
                print("***"+player+" won. Game over***")
                game_continue() 
                break    
            elif Board[2]==player and Board[4]==player and Board[6]==player:
                print("***"+player+" won. Game over***")
                game_continue() 
                break

        if count==9:
            print("***TIE. Game Over***")
            game_continue()

        if count==1 or count==3 or count==5 or count==7 or count==9:
            player = 'O'
        elif count==2 or count==4 or count==6 or count==8:
            player = 'X'

def game_continue():
    choice = ''
    choice=input("Do you want to continue (Y/N): ")
    if choice=='Y' or choice=='y':
        game()
    elif choice=='N' or choice=='n':
        exit()
                
game()