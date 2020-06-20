#re-vinculando-II

import pyautogui
import time

#selecionando a 
pyautogui.moveTo(173, -372)
pyautogui.click()
time.sleep(2)
pyautogui.hotkey('pagedown')
pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down'])
pyautogui.moveTo(111, -373)
pyautogui.click()
pyautogui.hotkey('pagedown')
pyautogui.moveTo(146, -268, duration=0.3)
pyautogui.click()
pyautogui.moveTo(1313, -167, duration=0.3)
pyautogui.click()

# VSCODE - selecionando a janela do VSCode
pyautogui.moveTo(288,-22)
pyautogui.click()
pyautogui.moveTo(984, 44)
pyautogui.click()