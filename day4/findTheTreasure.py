import random

treasureMap = [["a", "b", "c"], ["d", "f", "g"], ["h", "i", "j"]]

randomVertical = random.randint(0, 2)
randomHorizontal = random.randint(0, 2)
#print(randomVertical, randomHorizontal)

treasureLocation = treasureMap[randomVertical][randomHorizontal]

position = input("Give position by first giving vertical line number and then horizontal number. \nFor example 23 would be the letter b\n")
vertical = int(position[0]) - 1
horizontal = int(position[1]) - 1
chosenPosition = treasureMap[vertical][horizontal]
#print(chosenPosition)

if treasureLocation == chosenPosition:
    print("You found the treasure!!!")
else:
    print("You didn't find anything")

treasureMap[vertical][horizontal] = "X"

#print(treasureLocation)
print(treasureMap[0])
print(treasureMap[1])
print(treasureMap[2])