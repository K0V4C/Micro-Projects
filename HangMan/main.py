import turtle
import random
import math

#intruduction screen
def FirstScreen():
    caster = turtle.Turtle()

    caster.color('deep pink')
    style = ('Courier', 20, 'italic')
    caster.write('Welcome to game of hangman,type in any key to continue', font=style, align='center')
    caster.hideturtle()

    i = input()
    caster.clear()
#clears console
def Refresh():
    #clear junk of console
    import os
    clear = lambda: os.system('cls')
    clear()
#chooses a word for the game
def WordPicker():
    arr = []
    len = 0
    files = open("words.txt","r")
    for line in files:
        arr.append(line)
        len+=1
    randline = random.randrange(0,len-1)
    files.close()
    return (arr[randline],randline,len)
#shows the blanks
def show(blanks,length):
    for i in range(len(blanks)):
        print(blanks[i], end =" ") 
#player move
def move(word):
    print("If you would like to try a whole word type in W, otherwise type in L to try for a letter")
    while True:
        choice = input()
        if(choice.islower()):
            choice = choice.upper()
        if (choice == "L") or(choice == "W"):
            break
    if(choice == "L"):
        letter = input()
        if(letter.isupper()):
            letter = letter.lower()
        return (letter,True)
    else:
        guess = input()
        counter = 0
        for i in range (len(guess)):
            if guess[i] == word[i]:
                counter+=1

        if counter == len(word)-1:
            return ("0",False)
#checker
def checker(letter,letters,blanks,length,mistakes):
    switch = 0
    for i in range(length-1):
        if(letter == letters[i]):
            blanks[i] = letter
            switch = 1
    if(switch == 1):
        return (mistakes,blanks)
    else:
        #drawing current state of the game
        draw(mistakes+1)
        return (mistakes+1,blanks)
#is it over
def isItOver(mistakes,blanks,length):
    counter = 0
    if mistakes == 6:
        return False
    for i in range(length-1):
        if(blanks[i] == "_"):
            counter+=1
    if (counter == 0):
        return False
    else:
        return True
#end screen
def Finish(mistakes,word):
    if(mistakes == 6):
        print("Better luck next time")
        print("word has been ",word)
        return 0
    else:
        print("You've won")
        return 1
#hangpole
def set_up_draw():
    bob = turtle.Turtle()
    bob.pensize(3)
    bob.shape("turtle")
    bob.color("red")
    bob.hideturtle()
    bob.penup()
    bob.setpos(-100,-300)
    bob.pendown()
    bob.setheading(0)
    bob.forward(200)
    bob.setheading(180)
    bob.forward(100)
    bob.right(90)
    bob.forward(600)
    bob.right(90)
    bob.forward(200)
    bob.right(90)
    bob.forward(100)
#if u make a mistake body part is added
def draw(mistakes):
    master = turtle.Turtle()
    master.pensize(3)
    master.shape("turtle")
    master.color("black")
    master.hideturtle()
    if (mistakes == 1): 
        master.penup()
        master.setpos(200,200)
        master.setheading(270)
        master.pendown()
        #1st mistake
        master.color("black")
        master.penup()
        master.setpos(150,150)
        master.setheading(270)
        master.pendown()
        master.circle(50)
    if (mistakes == 2): 
        #2nd mistake
        master.penup()
        master.setpos(200,100)
        master.setheading(270)
        master.pendown()
        master.forward(200)

    if (mistakes == 3): 
        #3rd mistake
        master.penup()
        master.setpos(200,-100)
        master.setheading(270)
        master.pendown()
        master.right(30)
        master.forward(70)
        master.left(30)
        master.forward(70)
        master.setheading(90)
        master.penup()
        master.forward(70)
        master.right(30)
        master.forward(70)

    if (mistakes == 4): 
        #4th mistake
        master.penup()
        master.setpos(200,-100)
        master.pendown()
        master.setheading(270)
        master.left(30)
        master.forward(70)
        master.right(30)
        master.forward(70)
        master.setheading(90)
        master.penup()
        master.forward(70)
        master.left(30)
        master.forward(70)
        master.setheading(90)
        master.forward(130)

    if (mistakes == 5):
        #5th
        master.penup()
        master.setpos(200,30)
        master.pendown()
        master.setheading(270)
        master.pendown()
        master.right(30)
        master.forward(70)
        master.setheading(90)
        master.right(30)
        master.forward(70)

    if (mistakes == 6):
        #final
        master.penup()
        master.setpos(200,30)
        master.pendown()
        master.setheading(270)
        master.left(30)
        master.forward(70)
        master.setheading(90)
        master.left(30)
        master.forward(70)


Refresh()
FirstScreen()
pos = 0
lenn = 0
word , pos , lenn = WordPicker()


#makes word into chars
letters = []
length = len(word)

for i in range(length-1):
    letters.append(word[i])

#blank array
blanks = []
for i in range(length-1):
    blanks.append("_")

mistakes = 0

#draws hanging pole
set_up_draw()

#main coindition
gamerule = True

#main body of the game
while gamerule:
    #shows how many blanks are left
    show(blanks,length)

    #user input 
    letter,gamerule = move(word)
    #checks if the letter is in the array and all the postiuons where it is are marked or if it's missed makes a move
    if gamerule:
        mistakes,blanks = checker(letter,letters,blanks,length,mistakes)

    #makes sure game is on
    if gamerule:
        gamerule = isItOver(mistakes,blanks,length)

show(blanks,length)
print()
Finish(mistakes,word)