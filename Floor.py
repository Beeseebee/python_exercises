print "Podaj wymiary pokoju"
dlugosc = float(raw_input("D�ugo�� pokoju w cm: "))
szerokosc = float(raw_input("Szeroko�� pokoju w cm: "))
koszt_metra_kw = float(raw_input("Koszt metra kwadratowego w z�: "))
pole_cm = dlugosc * szerokosc
pole_m = pole_cm / 10000.0
koszt_m = pole_m * koszt_metra_kw
print "Potrzebujesz ", pole_cm, " centymetr�w kwadratowych wyk�adziny, czyli ", pole_m, "metr�w kwadratowych wyk�adziny."
print "Ca�kowity koszt wyk�adziny to ", koszt_m, "z�"

