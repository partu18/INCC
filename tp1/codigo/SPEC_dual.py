#!/usr/bin/env/python
from psychopy import visual, core, event  # import some libraries from PsychoPy
import os
from saveData import addMetric, loadData
from constants import * 

#Constants
duration_time = 0.2
interval_time = 0.5
repetition_times = 30/interval_time


#create a window
mywin = visual.Window(fullscr = True,  monitor="testMonitor", units="deg", color=(255,255,255), colorSpace='rgb255')#create some stimuli
circle = visual.ImageStim(win=mywin, image=circle_image_path, pos=(2,0.0))
arrow = visual.ImageStim(win=mywin, image=arrow_image_path, pos=(-2,0.0))
line = visual.ImageStim(win=mywin, image=line_image_path, pos=(0.0,0.0))

circleTime = 0.9
arrowTime = 0.6
circleLeftTime = circleTime
arrowLeftTime = arrowTime
next = 'circle'
current = next

#draw the stimuli and update the window
stim_times = []
for i in range(int(repetition_times)):
        #Escribimos el circulo
        current = next
        if (next == 'circle'):
            arrowLeftTime -= circleLeftTime
            circleLeftTime = circleTime
            if (circleLeftTime < arrowLeftTime):
                next = 'circle'
                interval_time = circleLeftTime
            else:
                next = 'arrow'
                interval_time = arrowLeftTime
            circle.draw()
        else:
            circleLeftTime -= arrowLeftTime
            arrowLeftTime = arrowTime
            if(circleLeftTime < arrowLeftTime):
                next = 'circle'
                interval_time = circleLeftTime
            else:  
                next = 'arrow'
                interval_time = arrowLeftTime
            arrow.size*= -1 #(hack ;) ) 
            arrow.draw()
        line.draw()
        #Enviamos la pantalla con el circulo
        mywin.flip()
        #Tomamos el tiempo en el que fue enviado
        stim_times.append((current, core.getTime()))
        #Lo mostramos por "duration_time" segundos
        core.wait(duration_time)
        #Mandamos pantalla en blanco
        line.draw()
        mywin.flip()
        #Mostramos pantalla en blanco por "interval_time" segundos.
        core.wait(interval_time)
        #Vemos cuando fueron apretadas las teclas
        #Borramos el buffer
        #    event.clearEvents()
        
user_times = event.getKeys(keyList=SPEC_DUAL_KEYLIST, timeStamped = True)
addMetric(result_path, (stim_times, user_times))

mywin.close()
core.quit()
