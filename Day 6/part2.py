file = open("Day 6/input.txt", "r")
lines = file.read()

for i, line in enumerate(lines):
    if i > 13:
        a = i-14
        fourDigits = set(lines[a:i])
        if len(fourDigits ) == 14:
            print(i)