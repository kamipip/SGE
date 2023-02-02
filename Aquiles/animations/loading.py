#Gem-Module
import itertools

#Timing Kernel Module
from sys import stdout as terminal
from time import sleep


#S.O Kernel Module
from itertools import cycle
from threading import Thread
import os




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



t = Thread(target=Animation.loading)
t.start()
sleep(5)
done = True


