#EXCEL0gray_painting_cells_of_EXCEL

import pyautogui
import time

# selecionando nome do aluno
pyautogui.moveTo(246, -29)
pyautogui.click()
time.sleep(0.3)
    # selecionando celula com nome do aluno
pyautogui.hotkey('esc')
pyautogui.press('left')
    # pintando a celula com nome do aluno
pyautogui.moveTo(227, -784)
pyautogui.click()
time.sleep(0.3)
    # selecionando a celula com a situação do aluno
pyautogui.press(['right', 'right', 'right', 'right', 'right', 'right', ])
pyautogui.moveTo(227, -784)
pyautogui.click()
time.sleep(0.3)