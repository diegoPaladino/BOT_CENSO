#Cadastro_aluno_Censo

import pyautogui
import time

# OPERA - selecionando o Opera
pyautogui.moveTo(148, -22)
pyautogui.click()
time.sleep(0.2)

# minimizando "Ocorrências"
pyautogui.moveTo(679, 319)
pyautogui.click()
time.sleep(0.2)

# copiando o nome do aluno
    # selecionando nome na barra de nome do aluno
pyautogui.moveTo(280, 438)
pyautogui.click()
pyautogui.mouseDown(button='left')
pyautogui.keyDown('shift')
time.sleep(0.2)
pyautogui.moveTo(603, 438)
pyautogui.click()
pyautogui.keyUp('shift')
    # copiando o nome
pyautogui.keyDown('ctrl')
pyautogui.hotkey('c')
pyautogui.keyUp('ctrl')

# CENSO - Colando na aba do censo
    # selecionando o Mozila
pyautogui.moveTo(192, -20)
pyautogui.click()
time.sleep(0.2)
    # colando na barra de nome, no censo
pyautogui.moveTo(162, -302)
pyautogui.click()
time.sleep(0.2)
pyautogui.keyDown('ctrl')
pyautogui.hotkey('v')
pyautogui.keyUp('ctrl')

