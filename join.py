import os
import time
import webbrowser
from multiprocessing import Process
from time import sleep


def func1():
    while True:
        webbrowser.open("steam://connect/148.59.74.84")
        time.sleep(3700)
        

def func2():

    second = 0    
    minute = 0    
    hours = 0
    days = 0
        
    while True: 
        print('\t\t\t\t SWAMP CINEMA AFK | UPTIME:  %d Days, %d Hours, %d Minutes, %d Seconds '%(days,hours,minute,second))    
        time.sleep(1)    
        second+=1    
        if(second == 60):    
            second = 0    
            minute+=1   
        if(minute == 60):    
            minute = 0    
            hours+=1;
        if(hours == 24):    
            hours = 0    
            days+=1; 
        os.system('cls')


if __name__ == '__main__':

    proc1 = Process(target=func1)
    proc1.start()

    proc2 = Process(target=func2)
    proc2.start()
        
        

    
