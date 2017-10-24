key = '''A(1x5)BC(3x3)XYZ'''

output = ""
timer = 0

for index, item in enumerate(key):
    if timer > 0:
        timer -= 1
    else:
        print(timer, item)
        if item != "(":
            output += item
        else:
            length = int(key[index + 1])
            mult = int(key[index + 3])
            output += key[index + 5: index + 5 +length] * mult
            timer = length + 4
    print(output)
print(len(output))
