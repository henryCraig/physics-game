import pygame

pygame.init()

#Sets the size of our display - (width, height)
#And will display it for a second as well
displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
#Sets the title of the display, basically the title of the game
pygame.display.set_caption("A bit Racey")


black = (0,0,0)
white = (255,255,255)

car_width = 73


#our game clock
clock = pygame.time.Clock()
gameExit = False
carImg = pygame.image.load('BoogerbeingComic.png')

def car(x,y):
    #Apparently blit just draws something to the screen
    gameDisplay.blit(carImg, (x,y))

x = (displayWidth * 0.45)
y = (displayHeight * 0.8)
xChange = 0
carSpeed = 0

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        #print(event)

    #I think if I was going to have it not exit I would rather do the
    #handling of edges up here
    #That way I can just stop the change from happening

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

pygame.quit()
quit()



















#Space
