#ESCRITA_DATA_NASCIMENTO_CENSO

import pyautogui
import time

# seleção Mozila para inserção da data
pyautogui.moveTo(194, -23)
pyautogui.click()
time.sleep(1)

# seleção text box data de nascimento
pyautogui.moveTo(144, -110)
pyautogui.click()
time.sleep(1)

# digitação da data de nascimento
pyautogui.write('26/12/2008')

