import pyautogui 
import time

time.sleep(5)
x, y = pyautogui.position()
print('Posição atual: ' + 'x = ' + str(x) + ' y = ' + str(y))

