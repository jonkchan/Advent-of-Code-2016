# Puzzle Input
# key = '''R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1'''
key = 'R2, R2, R2'
key = [i.replace(' ','') for i in key.split(',')]


xCord, yCord = 0, 0
counter = 0

for index, direct in enumerate(key):

    if index % 4 == 0:
        if direct[0] == 'L':
            xCord -= int(direct[1])
        elif direct[0] == 'R':
            xCord += int(direct[1])

    elif index % 4 == 1:
        if direct[0] == 'L':
            yCord -= int(direct[1])
        elif direct[0] == 'R':
            yCord += int(direct[1])

    elif index % 4 == 2:
        if direct[0] == 'L':
            yCord -= int(direct[1])
        elif direct[0] == 'R':
            yCord += int(direct[1])

    elif index % 4 == 3:
        if direct[0] == 'L':
            yCord -= int(direct[1])
        elif direct[0] == 'R':
            yCord += int(direct[1])

print(xCord, yCord)

