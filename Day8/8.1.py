# Puzzle Input
key = '''rect 1x1
rotate row y=0 by 6
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 4
rect 2x1
rotate row y=0 by 5
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 4x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 6
rect 4x1
rotate row y=0 by 4
rotate column x=0 by 1
rect 3x1
rotate row y=0 by 6
rotate column x=0 by 1
rect 4x1
rotate column x=10 by 1
rotate row y=2 by 16
rotate row y=0 by 8
rotate column x=5 by 1
rotate column x=0 by 1
rect 7x1
rotate column x=37 by 1
rotate column x=21 by 2
rotate column x=15 by 1
rotate column x=11 by 2
rotate row y=2 by 39
rotate row y=0 by 36
rotate column x=33 by 2
rotate column x=32 by 1
rotate column x=28 by 2
rotate column x=27 by 1
rotate column x=25 by 1
rotate column x=22 by 1
rotate column x=21 by 2
rotate column x=20 by 3
rotate column x=18 by 1
rotate column x=15 by 2
rotate column x=12 by 1
rotate column x=10 by 1
rotate column x=6 by 2
rotate column x=5 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 35x1
rotate column x=45 by 1
rotate row y=1 by 28
rotate column x=38 by 2
rotate column x=33 by 1
rotate column x=28 by 1
rotate column x=23 by 1
rotate column x=18 by 1
rotate column x=13 by 2
rotate column x=8 by 1
rotate column x=3 by 1
rotate row y=3 by 2
rotate row y=2 by 2
rotate row y=1 by 5
rotate row y=0 by 1
rect 1x5
rotate column x=43 by 1
rotate column x=31 by 1
rotate row y=4 by 35
rotate row y=3 by 20
rotate row y=1 by 27
rotate row y=0 by 20
rotate column x=17 by 1
rotate column x=15 by 1
rotate column x=12 by 1
rotate column x=11 by 2
rotate column x=10 by 1
rotate column x=8 by 1
rotate column x=7 by 1
rotate column x=5 by 1
rotate column x=3 by 2
rotate column x=2 by 1
rotate column x=0 by 1
rect 19x1
rotate column x=20 by 3
rotate column x=14 by 1
rotate column x=9 by 1
rotate row y=4 by 15
rotate row y=3 by 13
rotate row y=2 by 15
rotate row y=1 by 18
rotate row y=0 by 15
rotate column x=13 by 1
rotate column x=12 by 1
rotate column x=11 by 3
rotate column x=10 by 1
rotate column x=8 by 1
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 2
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 14x1
rotate row y=3 by 47
rotate column x=19 by 3
rotate column x=9 by 3
rotate column x=4 by 3
rotate row y=5 by 5
rotate row y=4 by 5
rotate row y=3 by 8
rotate row y=1 by 5
rotate column x=3 by 2
rotate column x=2 by 3
rotate column x=1 by 2
rotate column x=0 by 2
rect 4x2
rotate column x=35 by 5
rotate column x=20 by 3
rotate column x=10 by 5
rotate column x=3 by 2
rotate row y=5 by 20
rotate row y=3 by 30
rotate row y=2 by 45
rotate row y=1 by 30
rotate column x=48 by 5
rotate column x=47 by 5
rotate column x=46 by 3
rotate column x=45 by 4
rotate column x=43 by 5
rotate column x=42 by 5
rotate column x=41 by 5
rotate column x=38 by 1
rotate column x=37 by 5
rotate column x=36 by 5
rotate column x=35 by 1
rotate column x=33 by 1
rotate column x=32 by 5
rotate column x=31 by 5
rotate column x=28 by 5
rotate column x=27 by 5
rotate column x=26 by 5
rotate column x=17 by 5
rotate column x=16 by 5
rotate column x=15 by 4
rotate column x=13 by 1
rotate column x=12 by 5
rotate column x=11 by 5
rotate column x=10 by 1
rotate column x=8 by 1
rotate column x=2 by 5
rotate column x=1 by 5'''

key = '''rect 3x2
rotate column x=0 by 2'''

# Screen is 50 width * 6 height
width = 50
height = 6
screen = [i for i in (("." * width) + "\n")*height]

# ===================================================================================================

# Rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
def rect(a, b):
    for row in range(b):
        for col in range(a):
            screen[col + (51 * row)] = "#"

# Rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels.
# Pixels that would fall off the right end appear at the left end of the row.
def rotaterow(a, b):
    row = screen[a * 51: (a * 51) + width]
    for i in range(width):
        screen[(a * 51) + i] = row[i - b]

# Rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels.
# Pixels that would fall off the bottom appear at the top of the column.
def rotatecol(a, b):
    col = [screen[a + (i * 51): a + ((i * 51) + 1)] for i in range(height)]
    for i in range(height):

# ===================================================================================================

for command in key.split("\n"):
    if "rect" in command:
        a = int(command[command.index(" ") + 1:command.index("x")])
        b = int(command[command.index("x") + 1:])
        rect(a, b)
    elif "rotate" in command:
        a = int(command[command.index("=")+1:command.index(" b")])
        b = int(command[command.index("y ")+2:])
        if "row" in command:
            print(command)
            rotaterow(a, b)
        elif "column" in command:
            rotatecol(a, b)

print(''.join(screen))
