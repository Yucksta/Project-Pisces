import math
import time
import os

grid = [
    [["R", 1],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["R", 2]],
    [["K", 1],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["K", 2]],
    [["B", 1],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["B", 2]],
    [["M", 1],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["M", 2]],
    [["Q", 1],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["Q", 2]],
    [["B", 1],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["B", 2]],
    [["K", 1],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["K", 2]],
    [["R", 1],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["N", 0],["R", 2]]
]
x = 0
frequency = 1
Maximum = 50
Minimum = 200

while True:
    time.sleep(0.01)
    x = x + frequency
    print("#" * round((Maximum + Minimum) + math.sin(math.radians(x)) * Maximum) + "▓▓▓▓▓▓▓▓▓                           " + "#" * round((Maximum + Minimum) + math.sin(math.radians(x + 180)) * Maximum))
    print("#" * round((Maximum + Minimum) + math.cos(math.radians(x)) * Maximum) + "▒▒▒▒▒▒▒▒▒                           " + "#" * round((Maximum + Minimum) + math.cos(math.radians(x + 180)) * Maximum))
    print("#" * round((Maximum + Minimum) + math.sin(math.radians(x + 180)) * Maximum) + "░░░░░░░░░                           " + "#" * round((Maximum + Minimum) + math.sin(math.radians(x)) * Maximum))
    #print("#" * round((Maximum + Minimum) + math.cos(math.radians(x + 180)) * Maximum) + "                                    " + "#" * round((Maximum + Minimum) + math.cos(math.radians(x)) * Maximum))
    