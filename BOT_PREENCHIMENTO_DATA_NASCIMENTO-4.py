#BOT_PREENCHIMENTO_DATA_NASCIMENTO

import pyautogui
import time


# selecionar janela do programa secundario para pré-definir a seleção de data
pyautogui.moveTo(775, 44)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(x=499, y=418)
pyautogui.click()


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

# aguardo do tempo necessário para a execução do programa secundário
time.sleep(0.2)
