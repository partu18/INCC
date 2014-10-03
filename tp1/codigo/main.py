#!/usr/bin/env/python
# coding=utf-8
import os
from experiments  import *
from random import randint


randid = randint(0,20000) 


#Ventana
mywin = visual.Window(fullscr = True,  monitor="testMonitor", units="deg", color=(255,255,255), colorSpace='rgb255')


writeMessage(mywin,msg = coverMessage)
event.waitKeys(keyList=['return'])

writeMessage(mywin, msg = presentationMessage)
event.waitKeys(keyList=['return'])


#Primer experimento
expStarts(mywin,mcode=1)
tapping_exp(mywin,randid,'r')
expEnds(mywin)


#Segundo experimento
expStarts(mywin,mcode=2)
tapping_exp(mywin,randid,'l')
expEnds(mywin)

#Tercer experimento
expStarts(mywin,mcode=3)
arrow_exp(mywin,randid,'l')
expEnds(mywin)

#Cuarto experimento
expStarts(mywin,mcode=4)
arrow_exp(mywin,randid,'r')
expEnds(mywin)

#Dual (solo y enfatizado)
for i in range(3):
	expStarts(mywin,mcode=5+i)
	dual_exp(mywin,randid,False)
	expEnds(mywin)

	expStarts(mywin,mcode=6+i)
	dual_exp(mywin,randid,True) 
	expEnds(mywin)

writeMessage(mywin, msg = goodbyeMessage(randid))
event.waitKeys(keyList=['return'])





mywin.close()
core.quit()
