#!/usr/bin/env/python
# coding=utf-8
import os
from experiments  import *
from saveData  import *
from data  import *
from random import randint


randid = randint(0,20000) 

dual_tasks_order = dual_tasks_AF
if EO_circle_first:
	dual_tasks_order = dual_tasks_TF


#Ventana
mywin = visual.Window(fullscr = True,  monitor="testMonitor", units="deg", color=(255,255,255), colorSpace='rgb255')


writeMessage(mywin,msg = coverMessage)
event.waitKeys(keyList=['return'])

writeMessage(mywin, msg = presentationMessage)
event.waitKeys(keyList=['return'])


#Primer experimento
expStarts(mywin,mcode=1)
s, m = tapping_exp(mywin,randid,'r')
data["RH"]["T"]["S"] = s
data["RH"]["T"]["M"] = m
expEnds(mywin)

# #Segundo experimento
expStarts(mywin,mcode=2)
s, m = tapping_exp(mywin,randid,'l')
data["LH"]["T"]["S"] = s
data["LH"]["T"]["M"] = m
expEnds(mywin)

# #Tercer experimento
expStarts(mywin,mcode=3)
s, m = arrow_exp(mywin,randid,'r')
data["RH"]["A"]["S"] = s
data["RH"]["A"]["M"] = m
expEnds(mywin)

# #Cuarto experimento
expStarts(mywin,mcode=4)
s, m = arrow_exp(mywin,randid,'l')
data["LH"]["A"]["S"] = s
data["LH"]["A"]["M"] = m
expEnds(mywin)

# #Dual (solo y enfatizado)
for i in range(3):
	expStarts(mywin,mcode=5+2*i)
	mts, mas, mtm, mam = dual_exp(mywin,randid,False)
	
	# saving data
	data["RH"][dual_tasks_order[i]]["TS"] = mts
	data["RH"][dual_tasks_order[i]]["TM"] = mtm
	data["RH"][dual_tasks_order[i]]["AS"] = mas
	data["RH"][dual_tasks_order[i]]["AM"] = mam

	expEnds(mywin)

 	expStarts(mywin,mcode=6+2*i)
	mts, mas, mtm, mam = dual_exp(mywin,randid,True) 
	
	# saving data
	data["RH"][dual_tasks_order[i]]["TS"] = mts
	data["RH"][dual_tasks_order[i]]["TM"] = mtm
	data["RH"][dual_tasks_order[i]]["AS"] = mas
	data["RH"][dual_tasks_order[i]]["AM"] = mam

	expEnds(mywin)
	
#saving data in a file 
addMetric(result_path.format(str(randid)),data)

writeMessage(mywin, msg = goodbyeMessage(randid))
event.waitKeys(keyList=['f'])





mywin.close()
core.quit()
