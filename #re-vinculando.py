#re-vinculando

import pyautogui
import time

pyautogui.moveTo(539, -152)
pyautogui.click()
time.sleep(1.5)
pyautogui.press('pagedown')
pyautogui.moveTo(987, -121)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(182, -390)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(173, -372)
pyautogui.click()
time.sleep(0.5)
pyautogui.hotkey('pagedown')
pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down'])
pyautogui.moveTo(111, -373)
pyautogui.click()
pyautogui.hotkey('pagedown')
pyautogui.moveTo(146, -268, duration=0.3)
pyautogui.click()
pyautogui.moveTo(1313, -167, duration=0.3)
pyautogui.click()