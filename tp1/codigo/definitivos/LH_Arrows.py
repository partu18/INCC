#!/usr/bin/env/python
from psychopy import visual, core, event  # import some libraries from PsychoPy
import os
from saveData import addMetric, loadData
working_directory = os.getcwd()
from constants import *

#Times
duration_time = 0.1
interval_time = 0.4
repetition_times = 15


#create a window
mywin = visual.Window([1200,700], monitor="testMonitor", units="deg", color=(255,255,255), colorSpace='rgb255')

#create our stimuli
arrow = visual.ImageStim(win=mywin, image=arrow_image_path, pos=(-0.0,0.0))


stim_times = []

for i in range(repetition_times):
        #Escribimos el circulo 
        arrow.size*= -1 #(hack ;) ) 
        arrow.draw()
        #Enviamos la pantalla con el circulo
        mywin.flip()
        #Tomamos el tiempo en el que fue enviado
        stim_times.append(core.getTime())
        #Lo mostramos por "duration_time" segundos
        core.wait(duration_time)
        #Mandamos pantalla en blanco
        mywin.flip()
        #Mostramos pantalla en blanco por "interval_time" segundos.
        core.wait(interval_time)
        #Vemos cuando fueron apretadas las teclas
        
user_times = event.getKeys(keyList=LH_ARROWS_KEYLIST, timeStamped = True)
addMetric(result_path, (stim_times, user_times))

mywin.close()
core.quit()
