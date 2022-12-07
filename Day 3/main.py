file = open("Day 3/input.txt", "r")
lines = file.readlines()
total = 0

for line in lines:
    line = line.strip()
    mid = int(len(line)/2)
    firstHalf = line[:mid]
    secondHalf = line[mid:]
    
    for item in firstHalf:
    
        if item in secondHalf:
            if item.isupper():
                print(item, " ", ord(item)-38)
                total += (ord(item)-38)
                
            elif item.islower():#
                print(item, " ", ord(item)-96)
                total += (ord(item)-96)
            break
    

print(total)