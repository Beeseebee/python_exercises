import easygui
imieNazw = easygui.enterbox("Podaj imiê i nazwisko")
adres = easygui.enterbox("Podaj adres")
kodMiasto = easygui.enterbox("Podaj kod pocztowy i miasto")
dane = imieNazw + "\n" + adres + "\n" + kodMiasto
easygui.msgbox(dane, "Oto Twoje dane:")

