import re
file = open("Day 4/input.txt", "r")
lines = file.readlines()
count = 0
for line in lines:
    assignments = re.split(",|-",line.strip())
    #print(assignments)
    if int(assignments[0]) >= int(assignments[2]) and int(assignments[1]) <= int(assignments[3]):
        print(assignments[0],"-",assignments[1], assignments[2],"-",assignments[3],"first")
        count+=1
    
    elif int(assignments[2]) >= int(assignments[0]) and int(assignments[3]) <= int(assignments[1]):
        print(assignments[0],"-",assignments[1], assignments[2],"-",assignments[3],"second")    
        count+= 1
    else:
        print(assignments[0],"-",assignments[1], assignments[2],"-",assignments[3])

print(count)