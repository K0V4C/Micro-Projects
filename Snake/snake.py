import pygame
import random
#Snake class
class Snake:
    #snake class variables used to save snakes current and  before postions
    body = []
    before = []
    #inital properties of snake object
    def __init__(self,pos,color,surface):
        self.eaten = 0
        self.GameOver = 1
        self.surface = surface
        self.pos = pos
        self.color = color
        self.head = Cube(self.pos,self.color,self.surface)
        self.body.append(self.head)
        self.before.append((self.pos))

        self.diry = 1
        self.dirx = 0
    
    #draws all positions of snake cubes
    def drawSnake(self):
        for i , c in enumerate(self.body):
            if i == 0:
                c.draw(1)
            else:
                c.draw()
    #movement function of snake
    def move(self):
        #gets all events and says how to move next
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if (self.dirx == 0):
                    if event.key == pygame.K_LEFT:
                        self.diry = 0
                        self.dirx = -1
                    if event.key == pygame.K_RIGHT:
                        self.diry = 0
                        self.dirx = 1
                if(self.diry == 0):
                    if event.key == pygame.K_UP:
                        self.diry = -1
                        self.dirx = 0
                    if event.key == pygame.K_DOWN:
                        self.diry = 1
                        self.dirx = 0
            if event.type == pygame.QUIT:
                self.GameOver = 0

        #determines next postion of snake 
        for i,c in enumerate(self.body):
            if i==0:
                
                x = c.pos[0]+(self.dirx*25)
                y = c.pos[1]+(self.diry*25)
            
                if (c.pos[0]==food.pos[0])and(c.pos[1]==food.pos[1]):
                    self.eat(i)
                    self.eaten = 1

                if (x <= 500) and (y <= 500) and (x>0) and (y>0):
                    c.pos = (x,y)
                if (x > 500) or (y > 500) or (x<0) or (y<0):
                    self.GameOver = 0
            else:

                if (x <= 500) and (y <= 500) and (x>0) and (y>0):
                    c.pos = pos
            #element who was secound gets position of first and so on
            pos = self.before[i]

        #chehcks if snake hit herself
        self.check()
        #copys all before positions of snake segments 
        for i,c in enumerate(self.body):
             self.before[i] = c.pos
            
            
    #collision with food
    def eat(self,i):
        self.segment = Cube(self.body[i].pos,self.color,self.surface)
        self.body.append(self.segment)
        self.before.append(self.pos)
    #checks if snake has eaten herself
    def check(self):
        for i ,c in enumerate(self.body):
            print(self.head.pos)

            if (self.head.pos == self.before[i]):
                self.GameOver = 0


#Cube class
class Cube:
    cube_thicness = 24
    #inital proterties of all cubes
    def __init__(self,pos,color,surface):
        self.surface = surface
        self.color = color
        self.pos = pos
    #when called  draws the cubes
    def draw(self,eyes = 0):
        c = self.color
        if eyes == 1:
            c = (155,155,155)
        pygame.draw.rect(self.surface,c,(self.pos[0],self.pos[1],self.cube_thicness,self.cube_thicness))

#generates random food location
def generateFoodLocation():
    global rows
    x = random.randrange(rows)*25+1
    y = random.randrange(rows)*25+1
    
    return (x,y)

#drawing function of the game
def draw():
    global width ,heigth,surface,rows,snake

    #makes background white
    surface.fill((255,255,255))
    
    gap = heigth // rows
    for i in range(rows):
        start = i*gap
        #vertical lines
        pygame.draw.line(surface , (0,0,255),(start,0),(start,heigth))
        #horizontal lines
        pygame.draw.line(surface , (0,0,255),(0,start),(width,start))

    snake.drawSnake()
    food.draw(0)

    pygame.display.update()

# main function of the gmae
def main():
    global width ,heigth,surface,rows,snake,food
    rows = 20
    width = 500
    heigth = width
    #creating surface
    surface = pygame.display.set_mode((width,heigth))
    #creating clock
    c = pygame.time.Clock()
    #creating snake object
    start_pos_x = 1
    start_pos_y = 1
    snake_color = (125,125,125)
    snake = Snake((start_pos_x,start_pos_y),snake_color,surface)
    running = True
    food = Cube(generateFoodLocation(),(0,255,0),surface)
    while running:
        pygame.time.delay(50)
        c.tick(8)

        if snake.eaten == 1:
            food = Cube(generateFoodLocation(),(0,255,0),surface)
            snake.eaten = 0
        #draws the game
        draw()
        #checks for player movement and moves the snake
        snake.move()

        #if snake hit a wall or her self game ends
        if snake.GameOver == 0:
            running = False


#start of the gmae
main()
