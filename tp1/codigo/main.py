#!/usr/bin/env/python
# coding=utf-8
from psychopy import visual, core, event  # import some libraries from PsychoPy
import os
from saveData import addMetric, loadData
from experiments  import arrow_exp, tapping_exp, dual_exp, writeMessage,expStarts, expEnds


#Ventana
mywin = visual.Window(fullscr = True,  monitor="testMonitor", units="deg", color=(255,255,255), colorSpace='rgb255')

#Primer experimento
expStarts(mywin)
tapping_exp(mywin,'r')
expEnds(mywin)


#Segundo experimento
expStarts(mywin)
tapping_exp(mywin,'l')
expEnds(mywin)

#Tercer experimento
expStarts(mywin)
arrow_exp(mywin,'l')
expEnds(mywin)

#Cuarto experimento
expStarts(mywin)
arrow_exp(mywin,'r')
expEnds(mywin)

#Dual (solo y enfatizado)
for i in range(3):
	expStarts(mywin)
	dual_exp(mywin,True)
	expEnds(mywin)

	expStarts(mywin)
	dual_exp(mywin,False) 
	expEnds(mywin)





mywin.close()
core.quit()
