import pygame
import sys
import time
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
            pressedkeys=pygame.key.get_pressed()
            if pressedkeys[pygame.K_SPACE]:
                self.velocity=-7
                ang=10
            else:ang=-10
            self.image=pygame.transform.rotate(self.image,angle=ang)
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

players=player(50,175)
sprite=pygame.sprite.Group()
sprite.add(players)
pipeg=pygame.sprite.Group()
fps=pygame.time.Clock()

while True:
    fps.tick(60.0)
    draw()
    ground_movement()
    sprite.draw(screen)
    sprite.update()
    ctime=pygame.time.get_ticks()

    if gameover==False and move==True:
        if ctime-stime>=1500:
            upy=random.randint(-100,100)
            vpipes=pipe(500,200+upy,position=1)
            upipes=pipe(500,200+upy,position=0)
            pipeg.add(vpipes)
            pipeg.add(upipes)
            stime=ctime
    pipeg.draw(screen)
    pipeg.update()
    pygame.display.update()
    if pygame.sprite.groupcollide(sprite,pipeg,False,False) or players.rect.top<0:
        gameover=True
        gmove=False
        move=False
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN and gameover==False:
            move=True

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()