kwota = float(raw_input("Wprowad� zap�acon� kwot�: "))
if kwota <= 50.0:
    rabat = kwota * 0.10
else:
    rabat = kwota * 0.20
wartosc = kwota - rabat
print "Otrzyma�e� ", rabat, "rabatu, wi�c warto�� po rabacie wynosi", wartosc
