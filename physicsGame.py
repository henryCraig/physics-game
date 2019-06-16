import pygame


#So one of the early things I'd like to do is to have two characters,
    #The detective and the alien thing/ monster/ etc.
#They will both be moving to the right of the screen
#The alien will be moving faster than the detective
#When the alien hits the detective, the game is over and the player loses
#dealing damage to the alien should slow the alien down as well I think

#otherwise its just a general race against time, which I don't think would be as fun

#Eventually his arm should be able to move around 360 degrees I think?
#That way you can aim for the moving piles overhead


pygame.init()

displayWidth = 1000
displayHeight = 400

#(width,length)
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Physics Game")
gameClock = pygame.time.Clock()

alien = pygame.image.load('BoogerbeingComic.png')
def alien(x,y):
    gameDisplay.blit(alien,(x,y))

gameEnd = False
while gameEnd != True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = True

    alien(0,0)

    pygame.display.update()
    gameClock.tick(60)

pygame.quit()
quit()
