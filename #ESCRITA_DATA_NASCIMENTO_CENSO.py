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
pyautogui.write('17/10/2007')
time.sleep(2)

# mandar pesquisar no Censo
pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab'])
pyautogui.hotkey('enter')
time.sleep(0.3)

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

# VSCODE - ida para o software 3
pyautogui.moveTo(991, 44)
pyautogui.click()

# MOZILA - volta para a plataforma Censo para o vinculo do aluno
# pyautogui.moveTo(194, -23)
# pyautogui.click()

# pré-posicionando janela de bots
pyautogui.moveTo()
pyautogui.click()


# GEMUL - Deixa on screen
pyautogui.moveTo(139, -22)
pyautogui.click()


# MOZILA - Deixa posicionado
pyautogui.moveTo(1465, -196)
pyautogui.click()