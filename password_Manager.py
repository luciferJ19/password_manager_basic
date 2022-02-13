#! python3
import pygame
import shelve
import time
import os
import sys
import pyperclip
import shutil
try:
    os.makedirs("Data")
except:
    pass
shelfFile = shelve.open(R'Data\sand')
shelfFile['itch'] = 'a4qwe7g@'
shelfFile['instagram'] = 'b7yhu7k$'
shelfFile['facebook'] = 'c3tup4v!'
shelfFile['twitter'] = 'o2iel83@'
shelfFile['google'] = 'g5ort3!!'
shelfFile['paypal'] = 'd9l8bs$k'
shelfFile['stripe'] = 'x0yij!g$'
x = 0
y = " "
while True:
    y = str(input("Enter The Name Of Website\n")).lower()
    if y not in ['itch', 'instagram', 'facebook', 'twitter', 'google', 'paypal','stripe']:
        print("No such password is found\nTry Again for another one")
    else:
        break
pyperclip.copy(shelfFile[y])
print("Copied To Clipboard Successfully!!")
time.sleep(1)
try:
    shutil.rmtree("Data")
except:
    pass
sys.exit()