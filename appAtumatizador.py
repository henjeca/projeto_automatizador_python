import pyautogui
from time import sleep
import time
import sys






# pyautogui.click(791,600, duration=2)#clicar em meu usuário#
# pyautogui.write("aaa")

# pyautogui.click(792,638, duration=2)#clicar em senha#
# pyautogui.write("123")

# pyautogui.click(806,669, duration=2)#clicar em cadastrar usuário#


print("a")
       
time.sleep(5)

with open('usuários.txt', 'r') as arquivo:
    for linha in arquivo:
       

       nome = linha.split(',')[0]
       pyautogui.click(791,600, duration=2)       
       pyautogui.write(nome)

       senha = linha.split(',')[1]
       pyautogui.click(792,638, duration=2)
       pyautogui.write(senha)
       pyautogui.click(806,669, duration=2)

       pyautogui.click(753,669, duration=2)



