print "Policzmy razem Twoje pieni�dze!"
liczba50 = float(raw_input("Podaj liczb� 50-grosz�wek: "))
liczba20 = float(raw_input("Podaj liczb� 20-grosz�wek: "))
liczba10 = float(raw_input("Podaj liczb� 10-grosz�wek: "))
liczba5 = float(raw_input("Podaj liczb� 5-grosz�wek: "))
razem50 = liczba50 * 0.5
razem20 = liczba20 * 0.2
razem10 = liczba10 * 0.1
razem5 = liczba5 * 0.05
wartosc_monet = razem50 + razem20 + razem10 + razem5
print "Obecnie masz: ", wartosc_monet, "z�"
                           
