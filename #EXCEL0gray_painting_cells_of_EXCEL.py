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
time.sleep(0.2)
    # inserindo comentário
pyautogui.moveTo(386, -849)
pyautogui.click()
time.sleep(0.2)
pyautogui.moveTo(402, -812)
pyautogui.click()
time.sleep(0.2)
    # escrevendo comentário
pyautogui.write('fora_prazo_censo')
time.sleep(2)
pyautogui.press(['esc', 'esc', ])
    # selecionando a celula com a situação do aluno
pyautogui.press(['right', 'right', 'right', 'right', 'right', 'right', ])
    # voltando para a aba "Pagina inicial" no Excel
pyautogui.moveTo(7, -855)
pyautogui.click()
time.sleep(0.2)
    # pintando a célula de situação (ATIVO, TRANSFERIDO, ETC)
pyautogui.moveTo(227, -784)
pyautogui.click()
time.sleep(0.3)

# recarregando páginas
    # CENSO - Mozilla
pyautogui.moveTo(192, -21)
pyautogui.click()
time.sleep(0.2)
pyautogui.hotkey('f5')
time.sleep(0.2)
    # GEMUL
pyautogui.moveTo(147, -22)
pyautogui.click()
time.sleep(1.5)
pyautogui.moveTo(257, 221)
pyautogui.click()
time.sleep(0.2)
pyautogui.moveTo(248, 349)
pyautogui.click()
time.sleep(0.2)

# EXCEL - voltando para o Excel
pyautogui.moveTo(246, -26)
pyautogui.click()
time.sleep(0.2)

    