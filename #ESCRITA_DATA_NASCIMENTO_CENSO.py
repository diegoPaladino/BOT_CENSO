#ESCRITA_DATA_NASCIMENTO_CENSO

import pyautogui
import time

# seleção Mozila para inserção da data
pyautogui.moveTo(194, -23)
pyautogui.click()
time.sleep(0.3)

# seleção text box data de nascimento
pyautogui.moveTo(144, -110)
pyautogui.click()
time.sleep(0.3)

# digitação da data de nascimento
pyautogui.write('01/01/2009')

# mandar pesquisar no Censo
pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab', ])
pyautogui.hotkey('enter')
time.sleep(2)
pyautogui.press(['pagedown', 'pagedown'])