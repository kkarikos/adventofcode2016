stepsNorth = 0
stepsSouth = 0
stepsWest = 0
stepsEast = 0
direction = "N"
directions = ["N", "E", "S", "W"]
visitedLocations = [[0,0]]

def move(step):
    global direction, stepsNorth, stepsEast, stepsWest, stepsSouth

    stepDirection = step[0]
    stepLength = int(step[1:])
    # set direction
    if stepDirection == 'L':
        directionIndex = directions.index(direction) - 1
        if directionIndex < 0:
            directionIndex = len(directions) - 1;
        direction = directions[directionIndex]
    else:
        directionIndex = directions.index(direction) + 1
        if directionIndex >= len(directions):
            directionIndex = 0;
        direction = directions[directionIndex]

    for i in range(0, stepLength):
        if direction == "N":
            stepsNorth += 1
        elif direction == "E":
            stepsEast += 1
        elif direction == "S":
            stepsSouth += 1
        else:
            stepsWest += 1

        currentPosition = [(stepsNorth - stepsSouth), (stepsEast - stepsWest)]
        for pos in visitedLocations:
            if pos[0] == currentPosition[0] and pos[1] == currentPosition[1]:
                print "YAIKES!", currentPosition
                print "Steps: ", (abs(stepsNorth - stepsSouth) + abs(stepsWest - stepsEast))
                return
        visitedLocations.append(currentPosition)

moves = "R4, R5, L5, L5, L3, R2, R1, R1, L5, R5, R2, L1, L3, L4, R3, L1, L1, R2, R3, R3, R1, L3, L5, R3, R1, L1, R1, R2, L1, L4, L5, R4, R2, L192, R5, L2, R53, R1, L5, R73, R5, L5, R186, L3, L2, R1, R3, L3, L3, R1, L4, L2, R3, L5, R4, R3, R1, L1, R5, R2, R1, R1, R1, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3"

for moveDef in moves.split(","):
    move(moveDef.strip())

print "N: ", stepsNorth
print "S: ", stepsSouth
print "W: ", stepsWest
print "E: ", stepsEast
print "Steps: ", (abs(stepsNorth - stepsSouth) + abs(stepsWest - stepsEast))

   
