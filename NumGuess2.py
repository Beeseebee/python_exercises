import random, easygui
sekret = random.randint(1, 99)
propozycja = 0
proba = 0
easygui.msgbox("""AHOJ! Jam jest pirat Robert Straszliwy i mam dla Ciebie zagadk�! Jest ni� tajemna liczba od 1 do 99. Na odgadni�cie jej masz 6 pr�b.""")
while propozycja != sekret and proba < 6:
    propozycja = easygui.integerbox("Jaka to liczba?")
    if propozycja < sekret:
        easygui.msgbox(str(propozycja) + " jest za ma�a, psubracie!")
    elif propozycja > sekret:
        easygui.msgbox(str(propozycja) + " jest za du�a, szczurze l�dowy!")
    proba = proba + 1
if propozycja == sekret:
    easygui.msgbox("Stop! Uda�o Ci si�! Odgad�e� moj� tajemn� liczb�!")
else:
    easygui.msgbox("Wykorzysta�e� wszystkie pr�by! Powodzenia nast�pnym razem. kole�ko! Tajemna liczba to " + str(sekret))
