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
pyautogui.moveTo(111, -373, duration=0.5)
pyautogui.click()
pyautogui.hotkey('pagedown')
pyautogui.moveTo(146, -268, duration=0.5)
pyautogui.click()
pyautogui.moveTo(1313, -167, duration=0.5)
pyautogui.click()
