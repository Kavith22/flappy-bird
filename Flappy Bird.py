import pygame
import sys
import random 

stime=pygame.time.get_ticks()
screen=pygame.display.set_mode(size=(450,450))
pygame.display.set_caption('Flappy Bird')
bg=pygame.image.load('PyGame/Flappy Bird/Images/Background.png')
background=pygame.transform.scale(bg,(450,450))
ground=pygame.image.load('PyGame/Flappy Bird/Images/Ground.png')

gameover=False
ground_x=0
move=False
gmove=True
animate=True

def draw():
    screen.blit(background,(0,0))
    screen.blit(ground,(ground_x,370))
def ground_movement():
    global ground_x
    global gmove
    if gmove==True:
        ground_x-=2
        if ground_x < -250:
            ground_x=0

images=['PyGame/Flappy Bird/Images/Normal.png', 'PyGame/Flappy Bird/Images/Flat.png','PyGame/Flappy Bird/Images/Down.png']
class restartbutton(pygame.sprite.Sprite):
    def __init__(self,x,y):
        restart=pygame.image.load('PyGame/Flappy Bird/Images/Restart.png')
        self.image=restart
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                restarting()

class player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images=[]
        self.num=0
        for image in images:
            sprites=pygame.image.load(image)
            self.images.append(sprites)
        
        self.image=self.images[self.num]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.velocity=0
    def update(self):
        global gmove
        global gameover

            
        if move==True:
            self.velocity+=0.5
            if self.velocity>5:
                self.velocity=5
            if self.rect.y<335:
                self.rect.y+=self.velocity
            
        if gameover==False:
            if self.num < 2:
                self.num=self.num+1
            else:
                self.num=0
            self.image=self.images[self.num]
            ang=0
            
            if pygame.mouse.get_pressed()[0]==1:
                self.velocity=-7
            self.image=pygame.transform.rotate(self.image,angle=-(self.velocity*2))
        if gameover==True:
            self.image=pygame.transform.rotate(self.image,angle=-90)


class pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        super().__init__()
        pipe=pygame.image.load('PyGame/Flappy Bird/Images/Pipe.png')
        self.image=pipe
        self.rect=self.image.get_rect()
        if position==0:
            self.rect.topleft=(x,y+70)
        else:
            self.image=pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft=(x,y-70)
    def update(self):
        self.rect.x-=3

def restarting():
    global move
    global gameover
    global gmove
    global animate

    move=False
    gameover=False
    animate=True
    gmove=True
    players.rect.x = 50
    players.rect.y = 175
    pipeg.empty()

players=player(50,175)
sprite=pygame.sprite.Group()
sprite.add(players)
pipeg=pygame.sprite.Group()
fps=pygame.time.Clock()
button=restartbutton(225,195)

while True:
    fps.tick(60.0)
    draw()
    ground_movement()
    sprite.draw(screen)
    sprite.update()
    pipeg.draw(screen)
    ctime=pygame.time.get_ticks()
    
    if gameover==False and move==True:
        if ctime-stime>=1500:
            upy=random.randint(-100,100)
            vpipes=pipe(500,200+upy,position=1)
            upipes=pipe(500,200+upy,position=0)
            pipeg.add(vpipes)
            pipeg.add(upipes)
            stime=ctime
        pipeg.update()
    
    if pygame.sprite.groupcollide(sprite,pipeg,False,False) or players.rect.top<0:
        gameover=True
        gmove=False
        button.draw()
    
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN and gameover==False:
            move=True
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()