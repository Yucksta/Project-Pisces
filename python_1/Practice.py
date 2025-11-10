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

print("\n\n\n\n\n\n\n\n\n\n\n\n░░░▓▓▓▒░░▓▓▓▒░░▓▒░▓▒░▓▒░▓▒░▓▓▓▓▒░░▓▓▓▒░▓▓▓▓▓▒░░░░░▓▓▓▓▓▒░░░░▓▒▓▒░░░░░▓▒")
print("░░▓▒░░░░▓▒░░▓▒░▓▓▒▓▒░▓▓▒▓▒░▓▒░░░░▓▒░░░░░░▓▒░░░░░░▓▒▓▒▓▒▓▒░░░▓▒▓▒░░░░░░░▓▒")
print("░░▓▒░░░░▓▒░░▓▒░▓▓▓▓▒░▓▓▓▓▒░▓▓▓▒░░▓▒░░░░░░▓▒░░░░░░▓▒▓▓▓▒▓▒░░░▓▒▓▒░░░░░░░░░▓▒")
print("░░▓▒░░░░▓▒░░▓▒░▓▒▓▓▒░▓▒▓▓▒░▓▒░░░░▓▒░░░░░░▓▒░░░░░░▓▒░░▓▒▓▒░░░░░░░░░░░░░░▓▒")
print("░░░▓▓▓▒░░▓▓▓▒░░▓▒░▓▒░▓▒░▓▒░▓▓▓▓▒░░▓▓▓▒░░░▓▒░░░░░░░▓▓▓▓▓▒░░░░▓▒▓▒░DAE░▓▒")

str(input("\n\nStart            "))

score = [0, 0]
who = [1, 2]

def ACSIIcheck ():
    def translate(l, m):
        if l == 1:
            return "░░░░░░░░░░░"
        elif l == 2:
            return "▓▓▓▓▓▓▓▓▓▓▓"
        elif l <= -1:
            if m % 2 == 0:
                return "10101010101"
            else:
                return "01010101010"
        else:
            return "           "

    for x in range(0, 6):
        print("                                     //===========<>===========<>===========<>===========<>===========<>===========<>===========\\\\")
        for y in range(0, 7):
            print("                                     ||" + translate(Board[0][5 - x], y) + "||" + translate(Board[1][5 - x], y) + "||" + translate(Board[2][5 - x], y) + "||" + translate(Board[3][5 - x], y) + "||" + translate(Board[4][5 - x], y) + "||" + translate(Board[5][5 - x], y) + "||" + translate(Board[6][5 - x], y) + "||")
    print("                                     H------1------------2------------3------------4------------5------------6------------7------H")

def wipe ():
    for a in range(0, len(Board)):
        for b in range(0, len(Board[a])):
            Board[a][b] = 0

def verify (col):
    good = False
    for j in range(0, len(Board[col])):
        if Board[col][j] == 0:
            good = True
    return good

def ending (p):
    os.system('clear')

    if p > 0:
        score[p - 1] = score[p - 1] + 1
        ACSIIcheck()
        print("\n\nPlayer " + str(p) + " victory!   P1: " + str(score[0]) + "  P2: " + str(score[1]))
        command = str(input())
        if command == "reset":
            score[0] = 0
            score[1] = 0
        os.system('clear')
    else:
        ACSIIcheck()
        print("Tie!")
        command = str(input())
        if command == "reset":
            score[0] = 0
            score[1] = 0
        os.system('clear')

    wipe()

    if who[1] == 1:
        who[0] = 1
        who[1] = 2
    else:
        who[0] = 2
        who[1] = 1
    

def CHIPplace (col):
    spot = 5
    for i in range(0, 5):
        if Board[col][i] < 1:
            spot = i
            break
    return spot

def WINcheck (player):
    notie = False
    for x in range(0, len(Board)):
        for y in range(0, len(Board[x])):
            if Board[x][y] == 0:
                notie = True

    
    for c in range(0, len(Board)):
        for d in range(0, len(Board[c])):
            if Board[c][d] == player:
                if c < 4:
                    if Board[c + 1][d] == player and Board[c + 2][d] == player and Board[c + 3][d] == player:
                        ending(player)
                        return 1
                if d > 2:
                    if Board[c][d - 1] == player and Board[c][d - 2] == player and Board[c][d - 3] == player:
                        ending(player)
                        return 1
                if d > 2 and c > 2:
                    if Board[c - 1][d - 1] == player and Board[c - 2][d - 2] == player and Board[c - 3][d - 3] == player:
                        ending(player)
                        return 1
                if d > 2 and c < 4:
                    if Board[c + 1][d - 1] == player and Board[c + 2][d - 2] == player and Board[c + 3][d - 3] == player:
                        ending(player)
                        return 1
    
    if notie == False:
        ending(0)
        return 1
    


def PlayerTurn (p):
    prison = True
    reward = 0
    while prison == True:
        UFN = int(input("\n\nPlayer #" + str(p) + ", which column would you like to place your chip? (input 0 to end) "))
        if UFN > 7 or UFN < 0 or verify(UFN - 1) == False:
            print("\nThat isn't an available option!\n")
        else:
            prison = False
            reward = UFN
    return reward

def cycle (sub):
    os.system('clear')
    ACSIIcheck()
    UFN = PlayerTurn(sub)
    if UFN == 0:
        print("\n\n\n\nGame End\n\n\n\n")
        return 15009708323717584011700580106003230035100201178
    Board[UFN - 1][CHIPplace(UFN - 1)] = sub
    e = WINcheck(sub)
    if e == 1:
        return ":("

doorstop = True
while doorstop == True:
    doorstop2 = True
    while True:
        os.system('clear')

        workspace1 = cycle(who[0])

        if workspace1 == 15009708323717584011700580106003230035100201178:
            doorstop = False
            break
        elif workspace1 == ":(":
            break

        os.system('clear')

        workspace2 = cycle(who[1])

        if workspace2 == 15009708323717584011700580106003230035100201178:
            doorstop == False
            break
        elif workspace2 == ":(":
            break