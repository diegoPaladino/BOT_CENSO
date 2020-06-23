#atualização_de_endereço

import pyautogui
import time


# OPERA - GEMUL - zerando dados
pyautogui.moveTo(145, -23)
pyautogui.click()
time.sleep(0.2)
pyautogui.hotkey('home')

pyautogui.moveTo(119, -684)
pyautogui.click()
time.sleep(0.2)

pyautogui.moveTo(115, -554)
pyautogui.click()
time.sleep(0.2)

# EXCEL - captura de Nº de matrícula no excel para lançamento no Gemul
pyautogui.moveTo(243, -24)
pyautogui.click()
time.sleep(0.2)

pyautogui.moveTo(290, 177)
pyautogui.doubleClick()
time.sleep(0.2)

pyautogui.keyDown('ctrl')
pyautogui.hotkey('c')
pyautogui.keyUp('ctrl')

# OPERA - Cola dos dados no GEMUL
pyautogui.moveTo(145, -23)
pyautogui.click()
time.sleep(0.2)

pyautogui.moveTo(243, -522)
pyautogui.doubleClick()
time.sleep(0.2)

pyautogui.keyDown('ctrl')
pyautogui.hotkey('v')
pyautogui.keyUp('ctrl')

# OPERA - buscando dados de endereço
pyautogui.hotkey('tab')
time.sleep(1.5)

pyautogui.hotkey('pagedown')
pyautogui.moveTo(-12, -293)
pyautogui.click()
time.sleep(0.5)

# EXCEL - Copiando nome para a plataforma Censo no Mozilla
pyautogui.moveTo(244, -23)
pyautogui.click()
time.sleep(0.3)
pyautogui.hotkey('esc')
time.sleep(0.3)
pyautogui.hotkey('right')

# selecionando o nome do aluno no Excel - box
pyautogui.moveTo(257, 181)
pyautogui.click()
time.sleep(0.2)
# copia de nome do aluno na planilha do Excel
pyautogui.dragTo(615, 183, 0.2, button='left')       #deu certo este daqui
pyautogui.hotkey('ctrl','c')

# mudança para a janela do Mozila Firefox (plataforma Censo)
pyautogui.moveTo(193, -23, 0.2)
pyautogui.click()

# seleção do box e cola do nome na plataforma Censo
time.sleep(2)
pyautogui.moveTo(140, -187)
pyautogui.click()
pyautogui.hotkey('ctrl','a')
time.sleep(0.2)
pyautogui.hotkey('ctrl','v')
time.sleep(0.2)


# # volta para a planilha para copiar data de nascimento
pyautogui.moveTo(247, -26)
pyautogui.click()
time.sleep(0.3)
pyautogui.hotkey('esc')
pyautogui.press(['right','right'])

# # copia da data de nascimento
pyautogui.moveTo(257, 181)
pyautogui.click()
time.sleep(0.2)
# copia da data de nascimento do aluno na planilha do Excel
pyautogui.dragTo(615, 183, 0.2, button='left')       #deu certo este daqui
pyautogui.hotkey('ctrl','c')

# indo para o executavel da escrita de data na platafomra Censo
pyautogui.moveTo(291, -25)
pyautogui.click()

# seleção do local onde estão os dados de data de nascimento para substituição
pyautogui.moveTo(634, 46)
pyautogui.click()
pyautogui.moveTo(500, 420)

# tentativa de seleção por 'shift'
pyautogui.click()
pyautogui.keyDown('shift')
pyautogui.press(['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'])
pyautogui.click()
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('esc')

# play
pyautogui.moveTo(1148, 45)
pyautogui.click()

