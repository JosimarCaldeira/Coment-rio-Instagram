import time
import random
import pyautogui
import pyperclip
cont=0;
comentario = pyautogui.locateOnScreen('imagem.png')
if comentario:
 def rob():
    left,top = comentario.left,comentario.top
    pyautogui.click(left,top)
    time.sleep(3)
    palavra = palavras()
    pyperclip.copy(palavra)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(50)

 def palavras():
    palavr = ['Determinação','Persistência','comentado']
    palavra = random.choice(palavr)
    return palavra



 while cont<500:
   cont=cont+1
   print(cont)
   rob()

else:
   print('Não achou Nada Mesmo')
   exit()   
  