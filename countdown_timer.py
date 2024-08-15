#COUNTDOWN TIMER 
import time

t = int(input("Enter the countdown time: "))
def countdown(t):
    while t!=0:
        min,sec = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(min,sec)
        print(timer)
        time.sleep(1)
        t-=1
countdown(t)