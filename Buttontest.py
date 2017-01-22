__author__ = 'Katyana'
import random
import pygame
import sys, time
#import pygame.mixer
#from pygame.locals import *

lines = open('animals.txt').read().splitlines()

pygame.init()
#pygame.mixer.init()

FPS = 60  # frames per second setting
fpsClock = pygame.time.Clock()

#Variables
screen = pygame.display.set_mode((600, 500), 0, 0) #screen size
pygame.display.set_caption('Hello GIsHWheS!') #title
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0

#sound
#blop = pygame.mixer.Sound("blop2.wav")

#icon
iconsurface = pygame.image.load("tinyg.png")
pygame.display.set_icon(iconsurface)

#font stuff
fontObj = pygame.font.SysFont("Consolas", 20) #header
fontObj1 = pygame.font.SysFont("Arial Black", 16) #button and header text
fontObj2 = pygame.font.SysFont("Arial Black", 36) #mascot text
fontObj3 = pygame.font.SysFont("Arial Black", 34) #mascot text2

#header
textSurfaceObj1 = fontObj.render('Welcome to the GIsHWheS random mascot generator!', 1, green)
textRectObj1 = textSurfaceObj1.get_rect()
textRectObj1.center = (300, 40)

#Mascot
textSurfaceObj2 = fontObj2.render('Mascot:', 1, (green))
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (300, 100)

#buttondown
buttondown = pygame.image.load("buttonpressed2.png")
buttondownrect = buttondown.get_rect()
buttondownrect.center = (300, 425)

#too many question marks
marks = pygame.image.load("toomany2.png")
marksrect = marks.get_rect()
marksrect.center = (300, 225)

#main button
buttonup = pygame.image.load("buttonup2.png")
buttonuprect = buttonup.get_rect()
buttonuprect.center = (300, 425)
textSurfaceObj = fontObj1.render("Generate Mascot!", 1, (black))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (300, 425)


def mascotnames():
    myline1 = random.choice(lines)
    myline2 = random.choice(lines)
    textSurfaceObj3 = fontObj3.render(myline1 + "-" + myline2, 1, (green))
    textRectObj3 = textSurfaceObj3.get_rect()
    textRectObj3.center = (300, 150)
    textSurfaceObj4 = fontObj3.render("Name: " + myline1[0:4] + myline2[-3:], 1, green)
    textRectObj4 = textSurfaceObj4.get_rect()
    textRectObj4.center = (300, 200)
    screen.fill(black)
    screen.blit(textSurfaceObj3, textRectObj3)
    screen.blit(textSurfaceObj4, textRectObj4)


def updatebutton():
    screen.blit(buttondown, buttondownrect)
    textSurfaceObj = fontObj1.render("Get me another!", 1, (black))
    textRectObj.center = (305, 425)
    screen.blit(textSurfaceObj, textRectObj)

count = False
while True:
    screen.blit(textSurfaceObj1, textRectObj1)
    screen.blit(buttonup, buttonuprect)
    screen.blit(textSurfaceObj, textRectObj)
    if count is False:
        screen.blit(marks, marksrect)
    if buttonuprect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(buttondown, buttondownrect)
        screen.blit(textSurfaceObj, textRectObj)
        count = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            textSurfaceObj = fontObj1.render("Get me another!", 1, (black))
            textRectObj.center = (305, 425)
            screen.blit(textSurfaceObj, textRectObj)
            screen.blit(textSurfaceObj2, textRectObj2)
            mascotnames()

    pygame.display.update()

