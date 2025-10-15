import os
os.system('clear')
Board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

def clear():
    for a in range(0, len(Board)):
        for b in range(0, len(Board[a])):
            Board[a][b] = 0

def verify(col):
    good = False
    for j in range(0, len(Board[col])):
        if Board[col][j] == 0:
            good = True
    return good

def CHIPplace (col):
    spot = 5
    for i in range(0, 5):
        if Board[col][i] == 0:
            spot = i
            break
    return spot

def WINcheck (player):
    os.system('clear')
    for c in range(0, len(Board)):
        for d in range(0, len(Board[c])):
            if Board[c][d] == player:
                if c < 4:
                    if Board[c + 1][d] == player and Board[c + 2][d] == player and Board[c + 3][d] == player:
                        print("\n\nPlayer " + str(player) + " victory!----\n\n")
                        clear()
                if d > 2:
                    if Board[c][d - 1] == player and Board[c][d - 2] == player and Board[c][d - 3] == player:
                        print("\n\nPlayer " + str(player) + " victory!vvvv\n\n")
                        clear()
                if d > 2 and c > 2:
                    if Board[c - 1][d - 1] == player and Board[c - 1][d - 2] == player and Board[c - 3][d - 3] == player:
                        print("\n\nPlayer " + str(player) + " victory!////\n\n")
                        clear()
                if d > 2 and c < 4:
                    if Board[c + 1][d - 1] == player and Board[c + 2][d - 2] == player and Board[c + 3][d - 3] == player:
                        print("\n\nPlayer " + str(player) + " victory!-/-/\n\n")
                        clear()

def ACSIIcheck ():
    def translate(l):
        if l == 1:
            return "░░░░░"
        elif l == 2:
            return "▓▓▓▓▓"
        else:
            return "     "

    print("---------------------------------------------------")
    for x in range(0, 6):
        for y in range(0, 3):
            print("||" + translate(Board[0][5 - x]) + "||" + translate(Board[1][5 - x]) + "||" + translate(Board[2][5 - x]) + "||" + translate(Board[3][5 - x]) + "||" + translate(Board[4][5 - x]) + "||" + translate(Board[5][5 - x]) + "||" + translate(Board[6][5 - x]) + "||")
        print("---------------------------------------------------")

def PlayerTurn(p):
    prison = True
    reward = 0
    while prison == True:
        UFN = int(input("\n\nPlayer" + str(p) + ", which column would you like to place your chip? (input 0 to end) "))
        if UFN > 7 or UFN < 0 or verify(UFN - 1) == False:
            print("\nThat isn't an available option!\n")
        else:
            prison = False
            reward = UFN
    return reward

while True:
    ACSIIcheck()
    UFN1 = PlayerTurn(1)
    if UFN1 == 0:
        print("\n\n\n\nGame End\n\n\n\n")
        break
    Board[UFN1 - 1][CHIPplace(UFN1 - 1)] = 1
    WINcheck(1)
    ACSIIcheck()
    UFN2 = PlayerTurn(2)
    if UFN2 == 0:
        print("\n\n\n\nGame End\n\n\n\n")
        break
    Board[UFN2 - 1][CHIPplace(UFN2 - 1)] = 2
    WINcheck(2)