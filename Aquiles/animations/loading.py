#Gem-Module
import itertools

#Timing Kernel Module
from sys import stdout as terminal
from time import sleep


#S.O Kernel Module
from itertools import cycle
from threading import Thread
import os

from art import *

from pyfiglet import Figlet


#Super Class Responsible to every animations in the test module
#Class Animation

done = False



class Animation():

    def loading():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            terminal.write('\r...' + c)
            terminal.flush()
            sleep(0.1)
        terminal.write('\rTest Complete!  🐕 ✔️✔️✔️')
        terminal.flush()

    def personal_write():
        #random = art("random")
        #tprint("random")

        f = Figlet(font='slant')
        word = 'HELLO'
        curr_word = ''
        for char in word:
            os.system('reset') #assuming the platform is linux, clears the screen
            curr_word += char;
            print (f.renderText(curr_word))
            sleep(1)
       



t = Thread(target=Animation.loading)
t.start()
sleep(5)
done = True


