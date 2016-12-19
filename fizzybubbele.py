# -*- coding: utf-8 -*-

zahl = int(raw_input("Heute spielen wir FizzyBubbele!\nSuch dir eine Zahl zwischen 1 und 100 aus: \n" ))
x = 100

for z in range(0,100):
    if zahl == z:
        print "\nDu hast dein Ende vor der Zeit gewählt..."
        break
    elif zahl > x:
        print "Das wars, deine Zahl war zu hoch!..."
        break
    elif (z + 1) % 3 != 0 and (z + 1) % 5 != 0:
        print z + 1
    elif (z + 1) % 3 == 0 and (z + 1) % 5 == 0:
        print "FizzyBubbele"
    elif (z + 1) % 3 == 0:
        print "Fizzy"
    elif (z + 1) % 5 == 0:
        print "Bubbele"

