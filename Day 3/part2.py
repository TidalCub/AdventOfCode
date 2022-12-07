file = open("Day 3/input.txt", "r")
lines = file.readlines()
total = 0
count = 0

tmp = []

for line in lines:
    tmp.append(line.strip())
    if count == 2:
        for item in tmp[0]:
    
            if item in tmp[1] and item in tmp[2]:
                if item.isupper():
                    
                    total += (ord(item)-38)
                    
                elif item.islower():#
                    
                    total += (ord(item)-96)
                break

        tmp = []
        count = 0
        continue

    count+=1
    
print(total)