from gtts import gTTS 
import os 
  
mytext   = 'Na minha máquina funciona'
myobj    = gTTS(text=mytext, lang='pt-br', slow=False) 
  
myobj.save("soriano.mp3") 
print("pronto!")
