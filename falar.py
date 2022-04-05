#falar.py

#pip install pywin32

import win32com.client as win32

speaker = win32.Dispatch("SAPI.SpVoice")
frase = "o rato roeu a roupa do rei de roma"
#print(frase.split("r"))
#speaker.Speak(frase.split("r"))
speaker.Speak(frase)
