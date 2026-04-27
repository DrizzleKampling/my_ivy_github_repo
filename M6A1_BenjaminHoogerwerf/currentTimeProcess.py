# 15.1 Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between zero and one, print the current time, and then exit.
import os
import subprocess
import multiprocessing
import time
import random


# I have NO idea why this doesn't work properly. The program I've written keeps trying to change the system time when all I want to do is READ the system time and print it out. This makes my head hurt.
# I tried consulting the textbook as well as online sources and nothing I tried made it work, so I'm stuck with this.
def getCurrentTime():
    ret = subprocess.getoutput('date -u', shell=True)

    return ret


if __name__ == "__main__":
    time.sleep(random.randint(0, 1))
    getCurrentTime()
    
    time.sleep(random.randint(0, 1))
    getCurrentTime()
    
    time.sleep(random.randint(0, 1))
    getCurrentTime()
