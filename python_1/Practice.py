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

movement = True
score = [0, 0]

def ACSIIcheck ():
    def translate(l):
        if l == 1:
            return "░░░░░░░░░░░"
        elif l == 2:
            return "▓▓▓▓▓▓▓▓▓▓▓"
        else:
            return "           "

    for x in range(0, 6):
        print("/============<>===========<>===========<>===========<>===========<>===========<>===========/|")
        for y in range(0, 7):
            print("||" + translate(Board[0][5 - x]) + "||" + translate(Board[1][5 - x]) + "||" + translate(Board[2][5 - x]) + "||" + translate(Board[3][5 - x]) + "||" + translate(Board[4][5 - x]) + "||" + translate(Board[5][5 - x]) + "||" + translate(Board[6][5 - x]) + "||")
    print("H------1------------2------------3------------4------------5------------6------------7------H")

def wipe():
    for a in range(0, len(Board)):
        for b in range(0, len(Board[a])):
            Board[a][b] = 0

def verify(col):
    good = False
    for j in range(0, len(Board[col])):
        if Board[col][j] == 0:
            good = True
    return good

def ending(p):
    score[p - 1] = score[p - 1] + 1
    ACSIIcheck()
    print("\n\nPlayer " + str(p) + " victory!   P1: " + str(score[0]) + "  P2: " + str(score[1]))
    command = str(input())
    if command == "reset":
        score[0] = 0
        score[1] = 0
    os.system('clear')
    wipe()

def CHIPplace (col):
    spot = 5
    for i in range(0, 5):
        if Board[col][i] == 0:
            spot = i
            break
    return spot

def WINcheck (player):
    for c in range(0, len(Board)):
        for d in range(0, len(Board[c])):
            if Board[c][d] == player:
                if c < 4:
                    if Board[c + 1][d] == player and Board[c + 2][d] == player and Board[c + 3][d] == player:
                        ending(player)
                if d > 2:
                    if Board[c][d - 1] == player and Board[c][d - 2] == player and Board[c][d - 3] == player:
                        ending(player)
                if d > 2 and c > 2:
                    if Board[c - 1][d - 1] == player and Board[c - 1][d - 2] == player and Board[c - 3][d - 3] == player:
                        ending(player)
                if d > 2 and c < 4:
                    if Board[c + 1][d - 1] == player and Board[c + 2][d - 2] == player and Board[c + 3][d - 3] == player:
                        ending(player)

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

def cycle(sub):
    os.system('clear')
    ACSIIcheck()
    UFN = PlayerTurn(sub)
    if UFN == 0:
        print("\n\n\n\nGame End\n\n\n\n")
        movement = False
        return 5
    Board[UFN - 1][CHIPplace(UFN - 1)] = sub
    WINcheck(sub)

while True:
    workspace1 = cycle(1)
    if workspace1 == 5:
        break
    workspace2 = cycle(2)
    if workspace2 == 5:
        break