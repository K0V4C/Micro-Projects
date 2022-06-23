import random
import turtle
import math

#global varaibles and predifined size of the screen
win_length = 500
win_height = 500
turtles = 8
num_of_runs = 20
turtle.screensize(win_length, win_height)


score = []
for i in range(turtles):
    score.append(0)
#class that contains everything our turtles neeed
class racer:
    turtle_color = ["magenta","black","red","orange","gray","purple","blue","violet"]
    def __init__(self,color,pos):
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape("turtle")
        self.turt.pensize(1)
        self.turt.speed(1)
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)
    def move(self):
        self.turt.pendown()
        r = random.randrange(0,20)
        self.turt.forward(r)
    def reset(self):
        self.turt.pendown()
        self.turt.clear()
        self.turt.hideturtle()
    def get_position(self):
        return self.turt.pos()

#writes end score to file
def write_to_file(score,turtles):
    turtle_color = racer.turtle_color
    with open("scorex.txt","w") as text_file:
        for i in range(turtles):
            text_file.write(turtle_color[i])
            text_file.write(": ")
            text_file.write(str(score[i]))
            text_file.write("\n")
#our Game(Brain) Function
def Game(score):
    turtle_color = racer.turtle_color

    turtle_list = []   

    start = -(win_length/2) + 20
    for i in range(turtles):
        x_position = start + i*(win_length)//turtles
        turtle_list.append(racer(turtle_color[i],(x_position,-300)))
    gamerule = True
    while gamerule:
        for i in range(turtles):
            turtle_list[i].move()

            current_position = turtle_list[i].get_position()
            if(current_position[1] >= 300):
                gamerule=False
                score[i]+=1
                break
    for i in range(turtles):
        turtle_list[i].reset()
    return score  
    
print("would u like to start the game?")
k=input()
run = 0
#main loop of the game
while run<num_of_runs:
    score = Game(score)
    run+=1
write_to_file(score,turtles)
