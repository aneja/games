'''

@author: amitoj
'''
#!/usr/bin/python

import pygame,random,math


def RandColor():
    return(random.randint(0,255),random.randint(0,255),random.randint(0,255))


r1= random.randint(0,255)
r2= random.randint(0,255)
r3= random.randint(0,255)
# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
RANDOM = RandColor()

NUMBALLS=2
SCORE=True




class Ball:
   BallCount = 0
   def __init__(self, x, y, xdirec,ydirec,xd,yd,Ccolor):
       self.x=x
       self.y=y
       self.xdirec=xdirec
       self.ydirec=ydirec
       self.xd=xd
       self.yd=yd
       self.Ccolor=Ccolor
       Ball.BallCount += 1

class Paddle:
   Paddle = 0
   def __init__(self, x, y, xdirec,ydirec,xd,yd,Ccolor):
       self.x=x
       self.y=y
       self.xdirec=xdirec
       self.ydirec=ydirec
       self.xd=xd
       self.yd=yd
       self.Ccolor=Ccolor

class score:
    p1score=0
    p2score=0
    
def GenerateBalls(count):
    bg=[]
    for c in range(0,count):
        b=Ball(random.randint(100,size[0]),random.randint(100,size[1]),random.choice([1,-1]),random.choice([1,-1]),10,10,RandColor()) 
        bg.append(b)
        
    return bg

def wallColl(Ball):
    if (Ball.x>=(size[0]-Ball.xd)):
        Ball.xdirec = Ball.xdirec * -1
        Ball.Ccolor=RandColor()
    if (Ball.x<=1):
        Ball.xdirec = Ball.xdirec * -1
        Ball.Ccolor=RandColor()
    if (Ball.y>=(size[1]-Ball.yd)):
        Ball.ydirec = Ball.ydirec * -1
        Ball.Ccolor=RandColor()
        scores.p1score+=1
        #print(scores.p1score)  
    if (Ball.y<=1):
        Ball.ydirec = Ball.ydirec * -1
        Ball.Ccolor=RandColor()
        scores.p2score+=1
            
    Ball.x=Ball.x+Ball.xdirec
    Ball.y=Ball.y+Ball.ydirec
    
def wallCollP(Paddle):
    if (Paddle.x>=(size[0]-Paddle.xd)):
        Paddle.xdirec = Paddle.xdirec *-1
        Paddle.Ccolor=RandColor()
    if (Paddle.x<=1):
        Paddle.xdirec = Paddle.xdirec *-1
        Paddle.Ccolor=RandColor()
    Paddle.x=Paddle.x+Paddle.xdirec   
def BallColl(bG,a):
    
    bGtemp=list(bG)
    for b1 in bGtemp:
        pA = ((b1.x+b1.xd),(b1.y+b1.yd))
        #print ("A   :")
        #print (pA)
        bGtemp.remove(b1)
        for b2 in bGtemp:
            pB = ((b2.x+b2.xd),(b2.y+b2.yd))
            #print ("B             :")
            #print (pB)
            dist = math.sqrt(pow((pA[0]-pB[0]),2)+pow((pA[1]-pB[1]),2))
            #print (dist)
            
            if dist<(b1.xd):
                a=a+1
                b1.xdirec=b1.xdirec*-1
                b1.ydirec=b1.ydirec*-1
                b2.xdirec=b2.xdirec*-1
                b2.ydirec=b2.ydirec*-1
def BallCollP(bG,a):
    bGtemp=list(bG)
    for b1 in bGtemp:
        pA = ((b1.x+b1.xd),(b1.y+b1.yd))
#         print (pA[1])
#         print (p.y)
#         print (b1.y)
#         
        if(((b1.y==(p.y+p.yd) or b1.y==(p.y))) and(pA[0] in range(p.x,(p.x+p.xd)))):
            b1.ydirec=b1.ydirec*-1
            b1.xdirec=b1.xdirec*1
        if(((b1.y==(p2.y+p2.yd) or b1.y==(p2.y)))and(pA[0] in range(p2.x,(p2.x+p2.xd)))):
            b1.ydirec=b1.ydirec*-1
            b1.xdirec=b1.xdirec*1
    
pygame.init()

scores = score()

font = pygame.font.SysFont("Comic Sans", 72)

# Set the width and height of the screen [width, height]
size = (400, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------

bGroup = GenerateBalls(NUMBALLS)
a=0

p=Paddle(100,100,random.choice([1,-1]),0,100,10,RandColor())

p2=Paddle(100,700,random.choice([1,-1]),0,100,10,RandColor())


while not done:
# --- Main event loop
    keys=pygame.key.get_pressed()
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this looI
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        if keys[pygame.K_SPACE]:
                print("spacebar pressed")
        if keys[pygame.K_RIGHT]:
                print("right pressed")
                p.xdirec=1
                p.x=p.x+p.xdirec
        if keys[pygame.K_LEFT]:
                print("left pressed")
                p.xdirec=-1
                p.x=p.x+p.xdirec
        if keys[pygame.K_d]:
                print("right pressed")
                p2.xdirec=1
                p2.x=p2.x+p2.xdirec
        if keys[pygame.K_a]:
                print("left pressed")
                p2.xdirec=-1
                p2.x=p2.x+p2.xdirec
#          elif event.type == pygame.KEYUP:
#              print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
        elif event.type == pygame.K_0:
            print("User pressed a left button")
            
        elif event.type == pygame.K_d:
            print("User pressed a right button")
        
# --- Game logic should go here
       
    for b in bGroup:
        wallColl(b)
    wallCollP(p)
    wallCollP(p2)
    
    bG = bGroup
    BallColl(bG,a)
    BallCollP(bG,a)
    

# --- Drawing code should go here
# First, clear the screen to white. Don't put other drawing commands
# above this, or they will be erased with this command.
    screen.fill(BLACK)
    
    for b in bGroup:
        pygame.draw.ellipse(screen, b.Ccolor, [b.x,b.y,b.xd,b.yd], 5);
#     p.x=p.x+p.xdirec
#     p2.x=p2.x+p2.xdirec
    pygame.draw.rect(screen, p.Ccolor, [p.x,p.y,p.xd,p.yd], 5);
    pygame.draw.rect(screen, p2.Ccolor, [p2.x,p2.y,p2.xd,p2.yd], 5);
    

    
    myfont = pygame.font.SysFont("Comic Sans MS", 10)
    # apply it to text on a label
#     text = font.render("Player 1 Score : "+str(scores.p1score), True, (0, 128, 0))
#     text2 = font.render("Player 2 Score : "+str(scores.p2score), True, (0, 128, 0))

    label = myfont.render(("Player 1 Score : "+str(scores.p1score)), 1, WHITE)
    label2 = myfont.render(("Player 2 Score : "+str(scores.p2score)), 1, WHITE)
    # put the label object on the screen at point x=100, y=100
    screen.blit(label, (10, 10))
    screen.blit(label2, (10, 750))
    
# --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
# --- Limit to 60 frames per second
    clock.tick(120)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
