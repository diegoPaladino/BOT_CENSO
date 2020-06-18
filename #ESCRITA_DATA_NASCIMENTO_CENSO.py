#ESCRITA_DATA_NASCIMENTO_CENSO

import pyautogui


# seleção Mozila para inserção da data
pyautogui.moveTo(194, -23)
pyautogui.click()

# seleção text box data de nascimento
pyautogui.moveTo(144, -110)
pyautogui.click()

# digitação da data de nascimento
pyautogui.write('26/12/2008')

