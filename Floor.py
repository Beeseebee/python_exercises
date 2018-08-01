# -*- coding: utf-8 -*-
print "Podaj wymiary pokoju"
dlugosc = float(raw_input("Długość pokoju w cm: "))
szerokosc = float(raw_input("Szerokość pokoju w cm: "))
koszt_metra_kw = float(raw_input("Koszt metra kwadratowego w zł: "))
pole_cm = dlugosc * szerokosc
pole_m = pole_cm / 10000.0
koszt_m = pole_m * koszt_metra_kw
print "Potrzebujesz ", pole_cm, " centymetrów kwadratowych wykładziny, czyli ", pole_m, "metrów kwadratowych wykładziny."
print "Całkowity koszt wykładziny to ", koszt_m, "zł"

