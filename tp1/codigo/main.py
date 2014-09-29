#!/usr/bin/env/python
from psychopy import visual, core, event  # import some libraries from PsychoPy
import os
from saveData import addMetric, loadData
from experiments  import arrow_exp, tapping_exp, dual_exp


mywin = visual.Window(fullscr = True,  monitor="testMonitor", units="deg", color=(255,255,255), colorSpace='rgb255')

#tapping_exp(mywin,'r')
#tapping_exp(mywin,'l')
#arrow_exp(mywin,'l')
arrow_exp(mywin,'r')
dual_exp(mywin,True)
dual_exp(mywin,False) 


mywin.close()
core.quit()
