# -*- coding: cp1250 -*-
import random
sekret = random.randint(1, 99)
propozycja = 0
proba = 0
print "Ahoj! Jam jest pirat Robert Straszliwy i mam dla Ciebie zagadkę!"
print "Jest nią tajemna liczba od 1 do 99. Na odgadnięcie jej masz 6 prób."
while propozycja != sekret and proba < 6:
    propozycja = input("Jaka to liczba?")
    if propozycja < sekret:
        print "Za mała, psubracie!"
    elif propozycja > sekret:
        print "Za duża, szczurze lądowy!"

    proba = proba + 1

if propozycja == sekret:
    print "Stop! Udało Ci się! Odgadłeś moją tajemną liczbę!"
else:
    print "Wykorzystałeś wszystkie próby! Powodzenia następnym razem, koleżko!"
    print "Tajemna licza to", sekret
