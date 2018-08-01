# -*- coding: utf-8 -*-

bak = float(raw_input("Jaki jest duży bak w samochodzie (w litrach)? "))
poziomPaliwa = float(raw_input("Jaki jest obecnie poziom paliwa w baku (w procentach)? "))
litr = float(raw_input("Ile kilometrów może przejechać samochód na 1 litrze paliwa? "))
zasieg = bak * (poziomPaliwa / 100.0) * litr
print "Możesz przejechać jeszcze", zasieg, "km."
print "Następna stacja jest za 200 km."
if zasieg >= 200:
    print "Możesz zaczekać z tankowaniem do kolejnej stacji."
else:
    print "Zatankuj teraz!"