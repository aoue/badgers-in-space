import pygame
import sys
from pygame.locals import *
from time import sleep
import math


#settings
pygame.init()
pygame.display.set_caption('Badgers in space')
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
background = pygame.image.load('C:\\Users\\Aaja\\Desktop\\code\\programs\\badgers in space\\images\\space.jpg') #Years later, I now see this won't work on computer's without the exact pathing. At least it shows willing.
font = pygame.font.SysFont('Calibri', 25)
keys = [False, False, False, False]
white = (255,255,255)

##music*************
track2 = pygame.mixer.music.load('C:\\Users\\Aaja\\Desktop\\code\\programs\\badgers in space\\music\\track2.mp3')
sacrificeSong = pygame.mixer.music.load('C:\\Users\\Aaja\\Desktop\\code\\programs\\badgers in space\\music\\sacrificeSong.mp3')
pygame.mixer.music.play(-1)
musicCounter = 1
whichSong = 1
##******************





class Player(object):
    #collision, the player's side 
    def __init__(self,x,y, name):        
        self.x = x
        self.y = y
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 200
        
        
    #rotation
    def draw(self,screen):
        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1]-(self.x+32),position[0]-(self.y+26))
        playerrot = pygame.transform.rotate(self.image, 360-angle*57.29)
        playerpos1 = (self.y-playerrot.get_rect().width/2, self.x-playerrot.get_rect().height/2)
        screen.blit(playerrot, playerpos1)
       
    #moving
    def move_x(self, dx):
        self.x += dx
        self.rect.x = self.x
    def move_y(self, dy):
        self.y += dy
        self.rect.y = self.y

        
player = Player(200,400,'C:\\Users\\Aaja\\Desktop\\code\\programs\\badgers in space\\images\\player.png')  







while 1:

    screen.blit(background, (0,0))

    #rotating player to face mouse
    player.draw(screen)

    #text
    screen.blit(font.render('Press q to quit', True, white), (0,0))
    screen.blit(font.render('M to toggle music', True, white), (0, 20))
    screen.blit(font.render('N to change tracks', True, white), (0, 40))
    
    pygame.display.flip()

    ###keyboard commands###
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            #press q to quit
            if event.key == pygame.K_q:
                print('You quit the game.')
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                
            #press m to toggle music, 1 = on, 0 = 0ff
            elif event.key == pygame.K_m:
                if musicCounter == 1:
                    print('Music off.')
                    pygame.mixer.music.stop()
                    musicCounter = musicCounter - 1
                else:
                    print('Music on.')
                    pygame.mixer.music.play(-1)
                    musicCounter = musicCounter + 1
                    
            #press n to switch the song back and forth,
            elif event.key == pygame.K_n:
                if whichSong == 1:
                    pygame.mixer.music.load('C:\\Users\\Aaja\\Desktop\\code\\programs\\badgers in space\\music\\track2.mp3')
                    pygame.mixer.music.play(-1)
                    whichSong = whichSong - 1
                else:
                    sacrificeSong = pygame.mixer.music.load('C:\\Users\\Aaja\\Desktop\\code\\programs\\badgers in space\\music\\sacrificeSong.mp3')
                    pygame.mixer.music.play(-1)
                    whichSong = whichSong + 1


                    
    ##movement##
                    
        
        
        #
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        #
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
                
    #adjust x and y      
    if keys[0]:
        player.move_x(-1)
    elif keys[2]:
        player.move_x(+1)
    if keys[1]:
        player.move_y(-1)
    elif keys[3]:
        player.move_y(+1)
    
