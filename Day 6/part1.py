file = open("Day 6/input.txt", "r")
lines = file.read()

for i, line in enumerate(lines):
    if i > 2:
        fourDigits = [lines[i-3],lines[i-2],lines[i-1],line]
        if any(fourDigits.count(x) > 1 for x in fourDigits) != True:
            print(fourDigits,i)
            break