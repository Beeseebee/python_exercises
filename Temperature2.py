import easygui
easygui.msgbox("Program konwertuj¹cy temperaturê ze stopni Fahrenheita na stopnie Celsjusza")
temperatura = easygui.enterbox("WprowadŸ temperaturê w stopniach Fahrenheita:")
fahrenheity = float(temperatura)
celsjusze = (fahrenheity - 32) * 5.0 / 9
easygui.msgbox("To " + str(celsjusze) + " stopni Celsjusza")
