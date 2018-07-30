print "Policzmy razem Twoje pieni¹dze!"
liczba50 = float(raw_input("Podaj liczbê 50-groszówek: "))
liczba20 = float(raw_input("Podaj liczbê 20-groszówek: "))
liczba10 = float(raw_input("Podaj liczbê 10-groszówek: "))
liczba5 = float(raw_input("Podaj liczbê 5-groszówek: "))
razem50 = liczba50 * 0.5
razem20 = liczba20 * 0.2
razem10 = liczba10 * 0.1
razem5 = liczba5 * 0.05
wartosc_monet = razem50 + razem20 + razem10 + razem5
print "Obecnie masz: ", wartosc_monet, "z³"
                           
