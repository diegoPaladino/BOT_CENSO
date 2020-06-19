#aluno_sem_registo

import pyautogui
import time

# selecionando a janela EXCEL
pyautogui.moveTo(240, -25)
pyautogui.click()
# selecinando a célula com nome do aluno
pyautogui.hotkey('left')
time.sleep(0.3)
# pintando de amarelo o nome do aluno
pyautogui.moveTo(244, -781)
pyautogui.click()
time.sleep(0.3)
pyautogui.moveTo(260, -626)
pyautogui.click()
# voltando a cor para "verde"
pyautogui.press('up')
pyautogui.moveTo(244, -781)
pyautogui.click()
time.sleep(0.3)
pyautogui.moveTo(379, -735)
pyautogui.click()
# indo para próximo nome após aluno não cadastrado
pyautogui.press(['down', 'down'])
# VSCODE - selecionando janela com software 1 - 
pyautogui.moveTo(292, -26)
pyautogui.click()
pyautogui.moveTo(406, 44)
pyautogui.click()