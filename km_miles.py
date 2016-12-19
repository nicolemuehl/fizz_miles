# -*- coding: utf-8 -*-

m = "m"
km = "km"

miles = 0.621371
kilometer = 1.60934

print "Hallo, lass uns spielen!\nWir rechnen heute in Meilen und Kilometer um."

while True:
    chose = raw_input("\nMöchtest du in Kilometer(km) oder Meilen(m) umrechnen?\n")

    if chose == km:
        a = float(raw_input("\nOk, wieviele Meilen hättest du gern in Kilometer angegeben?\n"))
        aa = "\n"+str(a)
        bb = " Meilen sind "
        cc = str(a*kilometer)
        dd = " Kilometer"
        print aa+bb+cc+dd

    elif chose == m:
        b = float(raw_input("\nGut, wieviele Kilometer brauchst du in Meilen umgerechnet?\n"))
        ee = "\n"+str(b)
        ff = " Kilometer sind "
        gg = str(b*kilometer)
        hh = " Meilen"
        print ee+ff+gg+hh

    else:
        print "Falsche Eingabe, du musst km oder m angeben, nicht " + chose + "!"

    ja = "j"
    nein = "n"
    neu = raw_input("\nMöchtest du einen weiteren Wert umrechnen? j/n")
    print neu
    if neu != ja:
        print "\nOk, wir sind fertig, tschüss!"
        break