# -*- coding: cp1250 -*-
import random
sekret = random.randint(1, 99)
propozycja = 0
proba = 0
print "Ahoj! Jam jest pirat Robert Straszliwy i mam dla Ciebie zagadk�!"
print "Jest ni� tajemna liczba od 1 do 99. Na odgadni�cie jej masz 6 pr�b."
while propozycja != sekret and proba < 6:
    propozycja = input("Jaka to liczba?")
    if propozycja < sekret:
        print "Za ma�a, psubracie!"
    elif propozycja > sekret:
        print "Za du�a, szczurze l�dowy!"

    proba = proba + 1

if propozycja == sekret:
    print "Stop! Uda�o Ci si�! Odgad�e� moj� tajemn� liczb�!"
else:
    print "Wykorzysta�e� wszystkie pr�by! Powodzenia nast�pnym razem, kole�ko!"
    print "Tajemna licza to", sekret
