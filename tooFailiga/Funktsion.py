def loe_failist(fail:str)->str:
    """
    loeme failist
    """
    f=open(fail,"r",encoding="utf-8-sig")
    jarjend=[] 
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def Kirjuta_failisse(fail:str,jarjend:list):
    """
    salvestame
    """
    f=open(fail,"a", encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+"\n")
    f.close()
from gtts import gTTS
import os
def Heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3") 
    os.system("heli.mp3")
def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def tõlk(text:str,keel:str):
    vastus=input("Sisse sõna: ")
    if vastus in text("SõnastikET.txt"):
        vastus.index(text)
        obj=gTTS(text=text,lang=keel,slow=False).save("heli1.mp3")
        os.system("heli1.mp3")

