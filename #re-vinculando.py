#re-vinculando

import pyautogui
import time

pyautogui.moveTo(534, -296)
pyautogui.click()
pyautogui.press('pagedown')
pyautogui.moveTo(984, -267)
time.sleep(0.2)
pyautogui.moveTo(181, -373)
pyautogui.click()
pyautogui.moveTo(173, -372)
pyautogui.click()
pyautogui.hotkey('pagedown')
pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down'])
pyautogui.moveTo(111, -373, duration=0.5)
pyautogui.click()
pyautogui.hotkey('pagedown')
pyautogui.moveTo(146, -268, duration=0.5)
pyautogui.click()
pyautogui.moveTo(1313, -167, duration=0.5)
pyautogui.click()