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

white = (255,255,255)

#(width,length)
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Physics Game")
gameClock = pygame.time.Clock()

#Alien info
alienImg = pygame.image.load('BoogerbeingComic.png')
def alien(x,y):
    gameDisplay.blit(alienImg,(x,y))
alienX = 0
alienY = 120

#Detective Info
detectiveImg = pygame.image.load('tracerBullet.png')
def detective(x,y):
    gameDisplay.blit(detectiveImg, (x,y))
detectiveX = 810
detectiveY = 270


pianoImg = pygame.image.load('hangingPiano.png')
def piano(x,y):
    gameDisplay.blit(pianoImg, (x,y))

    #This is throwing an error right now, its telling me I'm trying to get it before its referenced?



pianoX = 200
pianoY = 0

catImg = pygame.image.load('hangingCat.png')
def cat(x,y):
    gameDisplay.blit(catImg, (x,y))
catX = 800
catY = 0



angle = 0

gameEnd = False
while gameEnd != True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = True

    gameDisplay.fill(white)

    detective(detectiveX, detectiveY)


    rotated_image = pygame.transform.rotate(pianoImg, angle)
    angle += 1

    gameDisplay.blit(rotated_image, (pianoX, pianoY))


    #Working on getting the center of the top of the image
    #I actually think it wont be too hard, I just need half the center rotation
    #and half the top left corner rotation, should be just fine I think
    w, h = pianoImg.get_size()
    print(w, h)

    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    pianoBox = [pygame.math.Vector2(p) for p in [(pianoX, pianoY), (pianoX + w, pianoY), (pianoX, pianoY), (pianoX, pianoY)]]

    pygame.display.flip()

    cat(catX, catY)

    #Draws the alien to the screen, and slowly moves it across the screen
    alien(alienX,alienY)
    alienX += 0.3

    pygame.display.update()
    gameClock.tick(60)

pygame.quit()
quit()
