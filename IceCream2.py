import easygui
smak = easygui.choicebox("Jaki jest Twój ulubiony smak lodów?",
                         choices = ['Waniliowy', 'Czekoladowy', 'Truskawkowy'] )
easygui.msgbox ("Wybra³eœ " + smak)
