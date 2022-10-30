import pyautogui, time

pyautogui.PAUSE = 1.5
pyautogui.press('win')
pyautogui.write('Login.xlsx')
pyautogui.press('enter')
pyautogui.keyDown('alt')
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.keyUp('alt')

pyautogui.click(x = 388, y = 291)
pyautogui.write('Joao.gabriel')

pyautogui.click(x = 412, y = 335)
pyautogui.write('senhaforte@123')

pyautogui.click(x = 340, y = 475)
