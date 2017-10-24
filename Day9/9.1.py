key = '''A(1x5)BC'''
output = ""

for index, item in enumerate(key):
    switch = 0
    if switch != 0:
        pass
    else:
        if item != "(":
            output += item
        else:
            length = int(key[index + 1])
            mult = int(key[index + 3])
            print(length, mult)
            output += key[index + 5 * length] * mult
            switch = length
        switch -= 1
print(output)
