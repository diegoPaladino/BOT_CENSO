# BOT_EDUCACENSO_2021


# INSTRUCTIONS
# The browser userd its the Mozila Firefox, in the resolution 100% of zoom

# IMPORT LIBRARIES
import pyautogui as p
import time as t
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize 
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize 

usuario = '02124377124'
senha = 'P@ladino804680'

# DECLARATIONS
def logando_censo():
    # selecting Mozila browser
    p.moveTo(x=267, y=-26)
    t.sleep(0.2)
    p.click()
    t.sleep(0.2)
    
    # selecting the user box and writting de user
    p.moveTo(x=578, y=385)
    t.sleep(0.2)
    p.doubleClick()
    t.sleep(0.2)
    p.keyDown('ctrl')
    p.hotkey('a')
    p.keyUp('ctrl')
    t.sleep(0.2)
    p.typewrite("02124377124", interval=0.02)
    # selecting the password box and writting de code of password
    p.hotkey('tab')
    t.sleep(0.2)
    p.hotkey('backspace')
    t.sleep(0.2)
    p.typewrite("P@ladino804680")
    t.sleep(0.2)
    
# def pesquisa_aluno():
    
    


# EXECUTION OF CODE
logando_censo()