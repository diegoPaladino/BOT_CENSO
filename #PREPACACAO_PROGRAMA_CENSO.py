#PREPACACAO_PROGRAMA_CENSO

import pyautogui
import time

# MOZILA - mudança para a janela do Mozila Firefox (plataforma Censo) e atualização da janela
pyautogui.moveTo(193, -23, 0.2)
pyautogui.click()
pyautogui.hotkey('f5')

# EXCEL - mudança para a janela do EXCEL e preparo
pyautogui.moveTo(247, -26)
pyautogui.click()
time.sleep(0.3)
pyautogui.hotkey('left')
pyautogui.moveTo()
pyautogui.click(227, 780, 0.3)
pyautogui.click()
pyautogui.hotkey('down')

# VSCODE - Volta à primeira janela - software principal
pyautogui.moveTo(418, 46)
pyautogui.click()

