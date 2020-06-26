#Transferidos_conferencia

import pyautogui
import time

# EXCEL - selecionando Excel
pyautogui.moveTo(244, -21)
pyautogui.click()
time.sleep(0.2)

pyautogui.moveTo(169, -720)
pyautogui.doubleClick()
time.sleep(0.2)

# copiando 
pyautogui.keyDown('ctrl')
pyautogui.hotkey('c')
pyautogui.keyUp('ctrl')

# GEMUL - Alternando para o Gemul
pyautogui.moveTo(139, -21)
pyautogui.click()
time.sleep(0.2)
    # selecionando barra de Nº de matrícula
pyautogui.moveTo(301, 378)
pyautogui.click()
time.sleep(0.2)
    # colando Nº de matrícula
pyautogui.keyDown('ctrl')
pyautogui.hotkey('v')
pyautogui.keyUp('ctrl')
pyautogui.hotkey('tab')
time.sleep(1.5)

# movendo para dados / "ocorrencias"
pyautogui.moveTo(682, 324)
pyautogui.click()
time.sleep(0.2)

# EXCEL - Copiando dados para carregar na plataforma do Censo
pyautogui.moveTo(242, -15)
pyautogui.click()
time.sleep(0.2)
pyautogui.hotkey('esc')
pyautogui.hotkey('tab')
    # selecionando o nome do aluno no Excel - box
pyautogui.moveTo(134, -722)
pyautogui.click()
time.sleep(0.2)
    # copia de nome do aluno na planilha do Excel
pyautogui.dragTo(490, -722, 0.2, button='left')       #deu certo este daqui
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

# inserção (ctrl+v) da data de nascimento na plataforma Censo
pyautogui.moveTo(247, -26)
pyautogui.click()
time.sleep(0.3)

# volta para a planilha para copiar data de nascimento
pyautogui.hotkey('esc')
pyautogui.press(['right','right'])

# copia da data de nascimento
pyautogui.moveTo(134, -722)
pyautogui.click()
time.sleep(0.2)
pyautogui.dragTo(225, -722, 0.5, button='left')
pyautogui.hotkey('ctrl','c')

# indo para o executavel da escrita de data na platafomra Censo
pyautogui.moveTo(291, -25)
pyautogui.click()

# seleção do local onde estão os dados de data de nascimento para substituição
pyautogui.moveTo(775, 44)
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