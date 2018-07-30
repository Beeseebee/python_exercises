import random, easygui
sekret = random.randint(1, 99)
propozycja = 0
proba = 0
easygui.msgbox("""AHOJ! Jam jest pirat Robert Straszliwy i mam dla Ciebie zagadkê! Jest ni¹ tajemna liczba od 1 do 99. Na odgadniêcie jej masz 6 prób.""")
while propozycja != sekret and proba < 6:
    propozycja = easygui.integerbox("Jaka to liczba?")
    if propozycja < sekret:
        easygui.msgbox(str(propozycja) + " jest za ma³a, psubracie!")
    elif propozycja > sekret:
        easygui.msgbox(str(propozycja) + " jest za du¿a, szczurze l¹dowy!")
    proba = proba + 1
if propozycja == sekret:
    easygui.msgbox("Stop! Uda³o Ci siê! Odgad³eœ moj¹ tajemn¹ liczbê!")
else:
    easygui.msgbox("Wykorzysta³eœ wszystkie próby! Powodzenia nastêpnym razem. kole¿ko! Tajemna liczba to " + str(sekret))
