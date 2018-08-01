# -*- coding: utf-8 -*-
plec = raw_input("Podaj swoją płeć: ('chłopak' lub 'dziewczyna') ")
if plec == 'dziewczyna':
    wiek = float(raw_input("Podaj swój wiek: "))
    if 10 <= wiek <= 12:
        print "Kwalifikujesz się do drużyny."
    else:
        print "Nie kwalifikujesz się do drużyny."
else:
    print "Nie kwalifikujesz się do drużyny."
