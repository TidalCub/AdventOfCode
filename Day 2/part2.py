file = open("Day 2/input.txt", "r")
lines = file.readlines()

winningPair = {"A":"B", "B":"C", "C":"A"}

drawPair = {"A":"A", "B":"B", "C":"C"}

losePair = {"A":"C", "B":"A", "C":"B"}

shapeValue = {"A":1,"B":2,"C":3}

score = 0
for line in lines:
    opponentMove = (line.strip()).split(" ")[0]
    outCome = (line.strip()).split(" ")[1]
    
    if outCome.upper() == "X":
        score += 0 + shapeValue[losePair[opponentMove]]
        print(f"{opponentMove} Lose, play: {losePair[opponentMove]}")
    elif outCome.upper() == "Y":
        score += 3 + shapeValue[drawPair[opponentMove]]
        print(f"{opponentMove} Draw, play: {drawPair[opponentMove]}")
    elif outCome.upper() == "Z":
        score += 6 + shapeValue[winningPair[opponentMove]]
        print(f"{opponentMove} Win, play: {winningPair[opponentMove]}")
     

print(score)

#A = Rock. B = Papper, C = Siccors
#X = Lose, Y = Draw, Z = Win