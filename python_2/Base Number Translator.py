import string
Alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def conv (number):
    if number > 26:
        return "!!"
    else:
        return Alpha[number]

def translate (base, number):
    final = []
    temp = number
    final.append(number % base)
    while (temp > 0):
        if (temp % base >= 10):
            final.append(conv(temp % base - 10))
        else:
            final.append(temp % base)
        temp = temp // base
    res = ""
    for i in range(len(final) - 1, 0, -1):
        res = res + str(final[i])
    print("\n" + str(number) + " --> " + res)

while (True):
    print("\n\n\n\nEnter a base number, then a decimal number to translate. Your input must be a whole number. (Struggles with bases past 36)")
    Sys = (int(input("Base: ")), int(input("Number: ")))
    if (Sys[0] < 2):
        break
    translate(Sys[0], Sys[1])
print("Thanks for testing.")
#At least one comment