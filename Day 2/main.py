file = open("Day 2/input.txt", "r")
lines = file.readlines()

winningPair = {"A":"Y", "B":"Z", "C":"X"}
drawPair = {"A":"X", "B":"Y", "C":"Z"}
shapeValue = {"X":1,"Y":2,"Z":3}

score = 0
for line in lines:
    opponentMove = (line.strip()).split(" ")[0]
    yourMove = (line.strip()).split(" ")[1]
    
    if winningPair[opponentMove] == yourMove:
        score += 6 + shapeValue[yourMove]
    elif drawPair[opponentMove] == yourMove:
        score += 3 + shapeValue[yourMove]   
    else:
        score += 0 + shapeValue[yourMove] 
    
print(score)

#A = Rock. B = Papper, C = Siccors
#X = Rock, Y = Papper, Z = Siccors