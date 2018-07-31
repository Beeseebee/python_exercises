kwota = float(raw_input("WprowadŸ zap³acon¹ kwotê: "))
if kwota <= 50.0:
    rabat = kwota * 0.10
else:
    rabat = kwota * 0.20
wartosc = kwota - rabat
print "Otrzyma³eœ ", rabat, "rabatu, wiêc wartoœæ po rabacie wynosi", wartosc
