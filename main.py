import pyautogui
import time

#https://clientes.morar.com.br/Login.aspx
login = '18001715795'
password = 'Denizegatinha@2027'

pyautogui.press('win')
time.sleep(4)

pyautogui.write('chorme')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('https://clientes.morar.com.br/Login.aspx')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.write(login)
time.sleep(3)
pyautogui.press('tab')
time.sleep(3)
pyautogui.write(password)
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=629, y=451)
time.sleep(3)
pyautogui.press(['down', 'down', 'down','down'])
time.sleep(3)
pyautogui.click(x=1129, y=624)
time.sleep(3)
pyautogui.click(x=673, y=290)
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=91, y=196)
time.sleep(3)
pyautogui.click(x=242, y=312)
time.sleep(3)
pyautogui.write('Boleto do ITBI de Agosto/2025')
time.sleep(3)

pyautogui.press('enter')

print('Script executado com sucesso!!')



