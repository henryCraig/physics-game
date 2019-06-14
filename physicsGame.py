import pygame

pygame.init()

displayWidth = 1000
displayHeight = 400

#(width,length)
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Physics Game")
gameClock = pygame.time.Clock()


gameEnd = False
while gameEnd != True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = True

    pygame.display.update()
    gameClock.tick(60)

pygame.quit()
quit()
