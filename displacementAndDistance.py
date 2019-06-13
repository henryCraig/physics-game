#https://www.physicsclassroom.com

#Scalars -  are quantities that are fully described by a magnitude (or numerical value) alone.
#Vectors -  are quantities that are fully described by both a magnitude and a direction.

#It might take me a little while to get to problems that apply in the real world

#distance - is a scalar quantity that refers to "how much ground an object has covered" during its motion.
#displacement -  is a vector quantity that refers to "how far out of place an object is"; it is the object's overall change in position.
#Basicallty someone can move a lot, meaning they moved a great distance but their displacement may be very small
#Someone pacing for example can have a much greater distance moved than their displacement

#So maybe for displacement I can print ------>
#Like that
#and for each 10 ft I can add a "-"



import random

def testDistanceAndDisplacement():

    displacement = 0
    distance = 0

    for x in range(4):
        randMoveAmount = random.randint(1,10)
        randDirection = random.randint(0,1)


        if randDirection == 0:
            tokenAmount = randMoveAmount
            randMoveAmount *= 10

            print ("Right", randMoveAmount)
            print(("-" * (tokenAmount)) + ">")

            distance += randMoveAmount
            displacement += randMoveAmount
        else:
            tokenAmount = randMoveAmount
            randMoveAmount *= 10

            print ("Left", randMoveAmount)
            print("<" + ("-" * (tokenAmount)))

            distance += randMoveAmount
            displacement -= randMoveAmount

    displacement = abs(displacement)

    displacementGuess = input("Displacement? ")
    distanceGuess = input("Distance? ")

    if int(displacementGuess) == displacement:
        print("Correct!  The answer is: ", displacement)
    else:
        print("Sorry, good try though.  The correct answer is: ", displacement)

    if int(distanceGuess) == distance:
        print("Correct!  The answer is: ", distance)
    else:
        print("Sorry, good try though.  The correct answer is: ", distance)



testDistanceAndDisplacement()
















#Space
