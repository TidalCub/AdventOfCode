file = open("input.txt", "r")
lines = file.readlines()

totalCalories = []
cal = 0
for line in lines:
    
    if line == "\n":
        totalCalories.append(cal)
        cal = 0
    else:
        cal += int(line.strip())
        

orderedList = sorted(totalCalories, reverse = True)
topThreeCalories = 0
print(orderedList[0] + orderedList[1] + orderedList[2])