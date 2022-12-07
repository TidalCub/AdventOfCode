import re
file = open("Day 5/input.txt", "r")
lines = file.readlines()

stacks = [["[R]","[G]","[J]","[B]","[T]","[V]","[Z]"],
["[J]","[R]","[V]","[L]"],
["[S]","[Q]","[F]"],
["[Z]","[M]","[N]","[L]","[F]","[V]","[Q]","[G]"],
["[R]","[Q]","[T]","[J]","[C]","[S]","[M]","[W]"],
["[S]","[W]","[T]","[C]","[H]","[F]"],
["[D]","[Z]","[C]","[V]","[F]","[N]","[J]"],
["[L]","[G]","[Z]","[D]","[W]","[R]","[F]","[Q]"],
["[J]","[B]","[W]","[V]","[P]"]]

for line in lines:
    if "move" in line:
        move = line.split()[1]
        moveFrom = line.split()[3]
        moveTo = line.split()[5]
        res = (stacks[int(moveFrom)-1][-int(move):])
        #res.reverse()

        stacks[int(moveTo)-1] = stacks[int(moveTo)-1] + res
        keep = len(stacks[int(moveFrom)-1]) - int(move)
        stacks[int(moveFrom)-1] = stacks[int(moveFrom)-1][:keep]
        

top = ""
for a in range(0,9):
    print(stacks[a])
    top = top + stacks[a][(len(stacks[a]))-1]

print(top)
        


