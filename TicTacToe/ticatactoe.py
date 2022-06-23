#Game of tictactoe where u can go against other player or vs PC( imposibble to beat)
import random
#first screen of the game
def FirstScreen():
    print("#######################################################################################################################################################################")
    print("#                                                              Welcome to game of TicTacToe                                                                           #")
    print("#                                                                  #Choose ur gamemode#                                                                               #")
    print("#                                             Type P for player vs player or C to go against computer(random)                                                         #")
    print("#######################################################################################################################################################################")
#choosing the game mode
def GameMode():
    while True:
        selection = input()
        if(selection.isupper()):
            selection = selection.lower()
        if(selection == "p") or (selection == "c"):
            return selection
        else:
            print("#                                                  Ur answer was invalid try again                                                                                 #")
#End of the gmae screen
def Finish(whowon):
    print("#######################################################################################################################################################################")
    print("#                                                                                                                                                                     #")
    print("#                                                        WEll PLAYED PLAYER ", whowon,"IS THE WINNER                                                                          #")
    print("#                                                                                                                                                                     #")
    print("#######################################################################################################################################################################")
#function that draws the game
def draw(gamecounter,gamedrawer):
   
    for i in range(9):
        if gamecounter[i] == 0:
            gamedrawer[i] = "*"
        elif gamecounter[i] == 1:
            gamedrawer[i] = "X"
        else:
            gamedrawer[i] = "O"       

    print("#                                                                    ",gamedrawer[0],"#",gamedrawer[1],"#",gamedrawer[2],"                                                                                      #")
    print("#                                                                     #########                                                                                       #")
    print("#                                                                    ",gamedrawer[3],"#",gamedrawer[4],"#",gamedrawer[5],"                                                                                      #")
    print("#                                                                     #########                                                                                       #")
    print("#                                                                    ",gamedrawer[6],"#",gamedrawer[7],"#",gamedrawer[8],"                                                                                      #")       
    print("#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#")
#fucntion that says its a TIE
def Tie():
    print("#######################################################################################################################################################################")
    print("#                                                                                                                                                                     #")
    print("#                                                        WEll PLAYED PLAYER IT'S A TIE                                                                                #")
    print("#                                                                                                                                                                     #")
    print("#######################################################################################################################################################################")
#checks if some1 has won
def check(gamecounter):
    for i in range(3):
        if (gamecounter[i] == gamecounter[i+3]) and (gamecounter[i] == gamecounter[i+6]) and (gamecounter[i]!=0):
            if(gamecounter[i] == 1):
                return 1,1
            else: 
                return 1,2
    for i in range(0,7,3):
        if(gamecounter[i] == gamecounter[i+1]) and (gamecounter[i] == gamecounter[i+2]) and (gamecounter[i] !=0):
            if(gamecounter[i] == 1):
                return 1,1
            else:
                return 1,2           
    if(gamecounter[0] == gamecounter[4]) and (gamecounter[0] == gamecounter[8]) and (gamecounter[0]!=0):
        if(gamecounter[0] == 1):
                return 1,1
        else:
                return 1,2
    if(gamecounter[2] == gamecounter[4]) and (gamecounter[2] == gamecounter[6]) and (gamecounter[2]!=0):
        if(gamecounter[2] == 1):
                return 1,1
        else:
                return 1,2
    return 0,0
#player moves/actions
def move(turn,gamecounter):
    if(turn == 1):
        player = "X"
    else:
        player = "O"

    print("#                                                                      U are",player,"player                                                                                 #")
    print("#                                                              Insert postion of ur with 2 numbers                                                                    #")
    print("#                                                                 First is row secound is column                                                                      #")

    while True:
        column = int(input())
        row = int(input())
        total = (column-1)*3+(row-1)
        if(gamecounter[total] == 0):
            break
        else:
            print("already taken place try another number")

    if (turn == 1):
        gamecounter[total] = 1
    else:
        gamecounter[total] = 2
#Random move PC
def PC(turn,gamecounter):
    if(turn == 1):
        player = "X"
    else:
        player = "PC"

    print("#                                                                      U are",player,"player                                                                                #")
    print("#                                                             Insert postion of ur with 2 numbers                                                                     #")
    print("#                                                                 First is row secound is column                                                                      #")

    while True:
        total = (random.randint(0,9))-1
        if(gamecounter[total] == 0):
            break
        else:
            print("already taken place try another number")

    if (turn == 1):
        gamecounter[total] = 1
    else:
        gamecounter[total] = 2



FirstScreen()
gamemode = GameMode()

#preparations
gamerule = "ITSON"
checker = 0
whowon = 1
turn = 1
moves = 0
gamecounter = []
gamedrawer = []
for i in range(9):
    gamecounter.append(0)

for i in range (9):
    gamedrawer.append("*")

#happy little tree
draw(gamecounter,gamedrawer)

if(gamemode == "p"):
    while gamerule == "ITSON":
        #making the moves
        move(turn,gamecounter)
        moves+=1

        #little happy tree
        draw(gamecounter)

        #check if game still goes on
        checker,whowon = check(gamecounter)
        if(checker == 1):
            gamerule = "GAMEOVER"
        if(moves == 9):
            gamerule = "GAMEOVER"

        if(gamerule == "GAMEOVER"):
            break

        #making the moves
        turn+=1    
        move(turn,gamecounter)
        turn-=1
        moves+=1

        #little happy tree
        draw(gamecounter)

        #check if game still goes on
        checker,whowon = check(gamecounter)
        if(checker == 1):
            gamerule = "GAMEOVER"
    
        if(gamerule == "GAMEOVER"):
            break

    if(moves ==9) and (gamerule != "GAMEOVER"):   
        Tie()
    else:
        Finish(whowon)

if (gamemode == "c"):
    while gamerule == "ITSON":
        #making the moves
        move(turn,gamecounter)
        moves+=1

        #little happy tree
        draw(gamecounter,gamedrawer)

        #check if game still goes on
        checker,whowon = check(gamecounter)
        if(checker == 1):
            gamerule = "GAMEOVER"
        if(moves == 9):
            gamerule == "GAMEOVER"

        if(gamerule == "GAMEOVER"):
            break


        #PC masterrace
        turn+=1    
        PC(turn,gamecounter)
        turn-=1
        moves+=1

        #little happy tree
        draw(gamecounter,gamedrawer)

        #check if game still goes on
        checker,whowon = check(gamecounter)
        if(checker == 1):
            gamerule = "GAMEOVER"
    
        if(gamerule == "GAMEOVER"):
            break

    if(moves ==9) and (gamerule != "GAMEOVER"):   
        Tie()
    else:
        Finish(whowon)