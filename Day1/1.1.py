# Puzzle Input
key = '''R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1'''
key = [i.replace(' ','') for i in key.split(',')]

# Starting Coordinates are 0,0
xIndex, yIndex = 0, 0

# Starting Orientation is North
compass = "N"

for i in key:

    # Direction: North
    if compass == "N":
        if i[0] == "L":
            compass = "W"
            xIndex -= int(i[1:])
        elif i[0] == "R":
            compass = "E"
            xIndex += int(i[1:])

    # Direction: South
    elif compass == "S":
        if i[0] == "L":
            compass = "E"
            xIndex += int(i[1:])
        elif i[0] == "R":
            compass = "W"
            xIndex -= int(i[1:])

    # Direction: West
    elif compass == "W":
        if i[0] == "L":
            compass = "S"
            yIndex -= int(i[1:])
        elif i[0] == "R":
            compass = "N"
            yIndex += int(i[1:])

    # Direction: East
    elif compass == "E":
        if i[0] == "L":
            compass = "N"
            yIndex += int(i[1:])
        elif i[0] == "R":
            compass = "S"
            yIndex -= int(i[1:])

# Print the absolute distance
print(abs(xIndex) + abs(yIndex))
