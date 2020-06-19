#censo-script-vinculo

import pyautogui
import time

pyautogui.moveTo(190, -368)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(175, -374, duration=0.5)
pyautogui.click()
pyautogui.hotkey('pagedown')
pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down'])
pyautogui.hotkey('tab')
pyautogui.moveTo(111, -373, duration=0.5)
pyautogui.click()
pyautogui.hotkey('pagedown')
time.sleep(0.3)
pyautogui.moveTo(146, -268, duration=0.5)
pyautogui.click()
pyautogui.moveTo(1313, -167, duration=0.5)
pyautogui.click()

# voltando a janela do Visual Studio Code
pyautogui.moveTo(288, -22)
pyautogui.click()

# play - deixando o cursor do mouse no play
pyautogui.moveTo(1148, 46)
