from Funktsion import *
laused=[]
eesti=[]
vene=[]
while True:
    v=int(input("1-loeme failist\n2-salvestame\n3-kuulamine\n4-tõlk"))
    if v==1:
        laused=loe_failist("Laused.txt")
        for line in laused:
            print(line)
    elif v==2:
        line=input("Lisa laused: ")
        laused.append(line)
        Kirjuta_failisse("Laused.txt", laused)
    elif v==3:
        text=""
        for line in laused:
            text=text+" "+line
        Heli(text, "et")
    elif v==4:
        text=""
        for line in laused:
            tõlk(text,"ru")