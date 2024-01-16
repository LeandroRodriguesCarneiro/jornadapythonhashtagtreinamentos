import pandas as pd
from time import sleep
import pyautogui

df = pd.read_csv('produtos.csv')

pyautogui.PAUSE = 0.5

# abrindo o chrome.
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# abrindo o site.
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# fazendo o código esperar 3 segundos.
sleep(3)

pyautogui.press('tab')
pyautogui.write('teste@teste.com')
pyautogui.press('tab')
pyautogui.write('s3nh4')
pyautogui.press('tab')
pyautogui.press('enter')

sleep(2)
count = 0
# inserindo os produtos.
for row in df.index:
    pyautogui.click(x=908, y=388)
    pyautogui.write(df.loc[row, 'codigo'])
    pyautogui.press('tab')
    pyautogui.write(df.loc[row, 'marca'])
    pyautogui.press('tab')
    pyautogui.write(df.loc[row, 'tipo'])
    pyautogui.press('tab')
    pyautogui.write(str(df.loc[row, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(df.loc[row, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(df.loc[row, 'custo']))
    pyautogui.press('tab')
    if not pd.isna(df.loc[row, 'obs']):
        pyautogui.write(str(df.loc[row, 'obs']))
    if count == 0:
        pyautogui.click(x=862, y=708)
        pyautogui.click(x=862, y=708)
    else:
        pyautogui.click(x=854, y=679)
        pyautogui.click(x=854, y=679)    
    pyautogui.scroll(5000)
    count+=1
    