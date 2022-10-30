import pyautogui

pyautogui.PAUSE = 3
pyautogui.press('win')
pyautogui.write('Login.xlsx')
pyautogui.press('enter')

pyautogui.click(x = 382, y = 334)
pyautogui.write('Joao.gabriel')

pyautogui.click(x = 356, y = 384)
pyautogui.write('senhaforte@123')

pyautogui.click(x = 340, y = 475)
