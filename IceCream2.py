import easygui
smak = easygui.choicebox("Jaki jest Tw�j ulubiony smak lod�w?",
                         choices = ['Waniliowy', 'Czekoladowy', 'Truskawkowy'] )
easygui.msgbox ("Wybra�e� " + smak)
