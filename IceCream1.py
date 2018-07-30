import easygui
smak = easygui.buttonbox("Jaki jest Twój ulubiony smak lodów?",
                        choices = ['Waniliowe', 'Czekoladowe', 'Truskawkowe'] )
easygui.msgbox ("Wybra³eœ " + smak)
