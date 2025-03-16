#zoom de la pagina en 67%

import pyautogui,time

#selecciono la primera opcion
pyautogui.click(x=469, y =318, clicks = 2)#Marvel
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(4)
#rellenamos la segunda pregunta
pyautogui.typewrite("De tal palo tal astilla")
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(4)
#selecciono la tercera respuesta
pyautogui.press('enter')
pyautogui.click(x=518, y =710, clicks = 1)#11 AM
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(4)
#selecciono la cuarta respuesta
pyautogui.typewrite("juan")
pyautogui.hotkey('altright','q')#@
pyautogui.typewrite("gmail.com")
pyautogui.press('tab')
time.sleep(4)

pyautogui.press('enter')

time.sleep(10)

#formulario 2
pyautogui.click(x=478, y =326, clicks = 2)
    
#selecciono la primera opcion
pyautogui.click(x=450, y =371, clicks = 2)#Ambos
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(4)
#rellenamos la segunda pregunta
pyautogui.typewrite("Donde no hay harina todo es mohína")
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(4)
#selecciono la tercera respuesta
pyautogui.press('enter')

pyautogui.click(x=518, y =645, clicks = 1)#9 AM
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(4)
#selecciono la cuarta respuesta
pyautogui.typewrite("Angel")
pyautogui.hotkey('altright','q')#@
pyautogui.typewrite("gmail.com")
pyautogui.press('tab')
time.sleep(4)

pyautogui.press('enter')
