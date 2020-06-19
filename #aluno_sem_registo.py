#aluno_sem_registo

import pyautogui
import time

# EXCEL - selecionando a janela do Exces
pyautogui.moveTo(244, -21)
pyautogui.click()
time.sleep(0.3)

# selecionando o nome do aluno
pyautogui.press('left')
time.sleep(0.3)

# selecionando a palheta de cores
pyautogui.moveTo(242, -784)
pyautogui.click()
time.sleep(0.3)

# selecionando a cor amarela/alaranjado
pyautogui.moveTo(261, -628)
pyautogui.click()
time.sleep(0.3)

# voltando para a cor verde
pyautogui.press('up')
time.sleep(0.2)

# selecionando a palheta de cores
pyautogui.moveTo(242, -784)
pyautogui.click()
time.sleep(0.3)

# selecionando a cor verde
pyautogui.moveTo(379, -737)
pyautogui.click()
time.sleep(0.3)

# selecionando próximo nome
pyautogui.press(['down', 'down'])

# VSCODE - deixando janela do VSCode selecionada
pyautogui.moveTo(289, -23)
pyautogui.click()

# VSCODE - selecionando aba do software 1
pyautogui.moveTo(457, 45)
pyautogui.click()