print "Podaj wymiary pokoju"
dlugosc = float(raw_input("D³ugoœæ pokoju w cm: "))
szerokosc = float(raw_input("Szerokoœæ pokoju w cm: "))
koszt_metra_kw = float(raw_input("Koszt metra kwadratowego w z³: "))
pole_cm = dlugosc * szerokosc
pole_m = pole_cm / 10000.0
koszt_m = pole_m * koszt_metra_kw
print "Potrzebujesz ", pole_cm, " centymetrów kwadratowych wyk³adziny, czyli ", pole_m, "metrów kwadratowych wyk³adziny."
print "Ca³kowity koszt wyk³adziny to ", koszt_m, "z³"

