import os
import subprocess
from threading import Thread
import time

commands = [
    'git init',
    'git add .',
    'git commit -m "firstcommit"',
    'git branch -M main',
    'git remote add origin https://github.com/bruteforcerxx/ebano.git',
    'git push -f origin main'
]

commands2 = [
    'git add .',
    'git commit -m "firstcommit"',
    'git push -f origin main'
]
cmm = 1

def coms():
    global cmm
    while True:
        time.sleep(1)
        if not cmm:
            break
        print(cmm)

thr1 = Thread(target=coms)
thr1.start()

for c in commands:
    cmm = os.popen(c)
    cmm = cmm.readline()
    print(cmm)

cmm = None
