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
pyautogui.hotkey('right')
    # copiando nome do aluno
pyautogui.


# CENSO - carregando dados na plataforma Censo
pyautogui.moveTo(191, -25)
pyautogui.click()
time.sleep(0.2)
