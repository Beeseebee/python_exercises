import easygui
smak = easygui.buttonbox("Jaki jest Tw�j ulubiony smak lod�w?",
                        choices = ['Waniliowe', 'Czekoladowe', 'Truskawkowe'] )
easygui.msgbox ("Wybra�e� " + smak)
