import pygame
import sys

screen=pygame.display.set_mode(size=(450,450))
pygame.display.set_caption('Flappy Bird')
bg=pygame.image.load('PyGame/Flappy Bird/Images/Background.png')
background=pygame.transform.scale(bg,(450,450))
ground=pygame.image.load('PyGame/Flappy Bird/Images/Ground.png')

ground_x=0


def draw():
    screen.blit(background,(0,0))
    screen.blit(ground,(ground_x,370))

def ground_movement():
    global ground_x
    ground_x-=0.2
    if ground_x < -250:
        ground_x=0
images=['PyGame/Flappy Bird/Images/Normal.png', 'PyGame/Flappy Bird/Images/Flat.png','PyGame/Flappy Bird/Images/Down.png']
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images=[]
        self.num=0
        for image in images:
            sprites=pygame.image.load(image)
            self.images.append(sprites)
        
        self.image=self.images[self.num]
        self.rect=self.image.get_rect()
        self.rect.center=(50,175)
    def update(self):
        if self.num < 2:
            self.num=self.num+1
        else:
            self.num=0
        self.image=self.images[self.num]
    
    
players=player()
sprite=pygame.sprite.Group()
sprite.add(players)

while True:
    draw()
    ground_movement()
    sprite.draw(screen)
    sprite.update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()