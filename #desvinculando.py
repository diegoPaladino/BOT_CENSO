#desvinculando

import pyautogui
import time

pyautogui.moveTo(539, -152)
pyautogui.click()
time.sleep(1.5)
pyautogui.press('pagedown')
pyautogui.moveTo(987, -121)
pyautogui.click()
time.sleep(0.5)

# PASTA - indo para a pasta do Windows e preparando para o software de vinculo
pyautogui.moveTo(104, -25)
pyautogui.click()
time.sleep(0.2)
pyautogui.press(['up', 'up', 'up'])
pyautogui.moveTo(193, -25)
pyautogui.click()
pyautogui.moveTo(1469, -168)
pyautogui.click(button='left')






# pyautogui.moveTo(182, -390)
# pyautogui.click()
# pyautogui.moveTo(173, -372)
# pyautogui.click()
# time.sleep(2)
# pyautogui.hotkey('pagedown')
# pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down'])
# pyautogui.moveTo(111, -373)
# pyautogui.click()
# pyautogui.hotkey('pagedown')
# pyautogui.moveTo(146, -268, duration=0.3)
# pyautogui.click()
# pyautogui.moveTo(1313, -167, duration=0.3)
# pyautogui.click()

# # VSCODE - selecionando a janela do VSCode
# pyautogui.moveTo(288,-22)
# pyautogui.click()
# pyautogui.moveTo(984, 44)
# pyautogui.click()
