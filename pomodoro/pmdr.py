"""this is my first pomodoro program"""
import time
from os import system, name
import winsound 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
clear()

#bell = 'bell.mp3'
session = 0
check = 0 
br = 0

for hour in range(24):
    for mins in range (60):
        if session < 1:
            session +=1
            check = session
            print (session)
            for sec in range (60):
                print (hour, ':' , mins, ':', sec)
                time.sleep(1)
        else:
            print ('session end')
            winsound.PlaySound('hey',winsound.SND_FILENAME)
            
            break
    break

if check == session:
    for hour in range(24):
        for mins in range (60):
            if br < 1:
                br +=1
                print (br)
                for sec in range (60):
                    print (hour, ':' , mins, ':', sec)
                    time.sleep(1)
            else:
                print ('break end')
            
                break
        break

print('hi')
