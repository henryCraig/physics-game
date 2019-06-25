import pygame
import time


pygame.init()

#Sets the size of our display - (width, height)
#And will display it for a second as well
displayWidth = 800
displayHeight = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("A bit Racey")                                       #Sets the title of the display, basically the title of the game
clock = pygame.time.Clock()




#our game clock


carImg = pygame.image.load('racecar.png')

def car(x,y):
    #Apparently blit just draws something to the screen
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.tff', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()                                                     #Our game loop is in here for some reason

def crash():
    message_display('You Crashed')

def game_loop():
    x = (displayWidth * 0.45)
    y = (displayHeight * 0.8)

    xChange = 0

    gameExit = False


    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xChange = -5
            elif event.key == pygame.K_RIGHT:
                xChange = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xChange = 0

        x += xChange

        gameDisplay.fill(white)
        car(x,y)

        if x > displayWidth - car_width or x < 0:
            gameExit = True

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()



















#Space
