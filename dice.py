import random
sides = 6
dices = 1
while 1==1:
    rolls = []
    output = ""
    for i in range(dices):
        r = random.randint(1, sides)
        rolls.append(r)
        output = output + str(r) + " "
    rolls.sort()
    x = input("Roll is: "+output+" . Change Dices (D"+str(dices)+") or Sides (S"+str(sides)+") or STOP or Enter > ")
    if x == "STOP":
        quit()
    if x.startswith("D"):
        if x[1:].isdigit():
            dices = int(x[1:])
        else:
            print ("Somthing wrong. Try D1")
    if x.startswith("S"):
        if x[1:].isdigit():
            sides = int(x[1:])
        else:
            print ("Somthing wrong. Try S1")
