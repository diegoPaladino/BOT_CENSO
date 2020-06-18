#BOT_PREENCHIMENTO_DATA_NASCIMENTO

import pyautogui
import time


pyautogui.moveTo(134, -722)
pyautogui.click()
time.sleep(0.5)


# copia de nome do aluno na planilha do Excel
pyautogui.dragTo(490, -722, 0.5, button='left')       #deu certo este daqui
pyautogui.hotkey('ctrl','c')

# mudança para a janela do Mozila Firefox (plataforma Censo)
pyautogui.moveTo(193, -23, 0.2)
pyautogui.click()

# seleção do box e cola do nome na plataforma Censo
pyautogui.moveTo(140, -187)
pyautogui.click()
pyautogui.hotkey('ctrl','a')
time.sleep(0.3)
pyautogui.hotkey('ctrl','v')

# inserção (ctrl+v) da data de nascimento na platqaforma Censo
pyautogui.moveTo(247, -26)
pyautogui.click()
time.sleep(0.3)

# volta para a planilha para copiar data de nascimento
pyautogui.hotkey('esc')
pyautogui.press(['right','right'])

# copia da data de nascimento
pyautogui.moveTo(134, -722)
pyautogui.click()
time.sleep(0.5)
pyautogui.dragTo(225, -722, 0.5, button='left')
pyautogui.hotkey('ctrl','c')

# voltando para o Mozila (plataforma Censo)
# pyautogui.hotkey('alt','tab')
# pyautogui.moveTo(144, -113, 0.2)
# pyautogui.click()
# time.sleep(0.5)
# pyautogui.write(a)

