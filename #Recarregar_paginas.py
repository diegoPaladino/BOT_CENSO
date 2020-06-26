#Recarregar_paginas

import pyautogui
import time

# recarregando páginas
    # CENSO - Mozilla
pyautogui.moveTo(192, -21)
pyautogui.click()
time.sleep(0.2)
pyautogui.hotkey('f5')
time.sleep(0.2)
    # GEMUL
pyautogui.moveTo(147, -22)
pyautogui.click()
time.sleep(1.5)
pyautogui.hotkey('home')
pyautogui.moveTo(257, 221)
pyautogui.click()
time.sleep(0.2)
pyautogui.moveTo(248, 349)
pyautogui.click()
time.sleep(0.2)

# EXCEL - voltando para o Excel
pyautogui.moveTo(246, -26)
pyautogui.click()
time.sleep(0.2)