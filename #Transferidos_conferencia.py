#Transferidos_conferencia

import pyautogui
import time

# EXCEL - selecionando Excel
pyautogui.moveTo(244, -21)
pyautogui.click()
time.sleep(0.2)

pyautogui.moveTo(169, -720)
pyautogui.doubleClick()
time.sleep(0.2)

# copiando 
pyautogui.keyDown('ctrl')
pyautogui.hotkey('c')
pyautogui.keyUp('ctrl')

# GEMUL - Alternando para o Gemul
pyautogui.moveTo(139, -21)
pyautogui.click()
time.sleep(0.2)
    # selecionando barra de Nº de matrícula
pyautogui.moveTo(139, -21)
pyautogui.click()
time.sleep(0.2)
    # colando Nº de matrícula
pyautogui.keyDown('ctrl')
pyautogui.hotkey('v')
pyautogui.keyUp('ctrl')
pyautogui.hotkey('tab')


