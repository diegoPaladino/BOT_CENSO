#censo-script-vinculo

import pyautogui
import time

pyautogui.moveTo(189,-257)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(175, -374)
pyautogui.click()
pyautogui.press('down', presses=27)
pyautogui.hotkey('tab')
time.sleep(0.2)
pyautogui.hotkey('esc')
pyautogui.moveTo(111, -373)   
pyautogui.click()
time.sleep(0.3)
pyautogui.hotkey('pagedown')
time.sleep(0.3)
pyautogui.moveTo(146, -268)
pyautogui.click()
time.sleep(0.3)
pyautogui.moveTo(1313, -167)
pyautogui.click()

# voltando a janela do Visual Studio Code
# pyautogui.moveTo(288, -22)
# pyautogui.click()
# time.sleep(0.3)

# play - deixando o cursor do mouse no play
# pyautogui.moveTo(1148, 46)

# PASTA - indo para a pasta do Windows e preparando para o software de vinculo
pyautogui.moveTo(104, -25)
pyautogui.click()
time.sleep(0.2)
pyautogui.press('up',presses=1)

