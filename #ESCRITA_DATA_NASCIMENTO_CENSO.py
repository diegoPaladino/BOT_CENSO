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
pyautogui.write('27/12/2007')

# mandar pesquisar no Censo
pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab'])
pyautogui.hotkey('enter')
time.sleep(1)

# procura pelo nome da mae
pyautogui.moveTo(242, -26, 0.5)
pyautogui.click()
pyautogui.hotkey('esc')
pyautogui.hotkey('left')
# copia de nome da mãe na planilha do Excel
pyautogui.moveTo(134, -722)
pyautogui.click()
time.sleep(0.5)
pyautogui.dragTo(490, -722, 0.5, button='left')       #deu certo este daqui
pyautogui.hotkey('ctrl','c')

# seleção Mozila para inserção do nome da mãe
pyautogui.moveTo(194, -23)
pyautogui.click()
time.sleep(0.3)

# inserção do nome da mãe no campo de pesquisa
pyautogui.press(['pagedown', 'pagedown'])
pyautogui.keyDown('ctrl')
pyautogui.hotkey('f')
pyautogui.keyUp('ctrl')
pyautogui.keyDown('ctrl')
pyautogui.hotkey('v')
pyautogui.keyUp('ctrl')
pyautogui.hotkey('backspace')
