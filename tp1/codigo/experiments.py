#!/usr/bin/env/python
# coding=utf-8
from psychopy import visual, core, event  # import some libraries from PsychoPy
#from saveData import addMetric, loadData
from constants import *
from conf import *


#experiments
def arrow_exp(win, randid ,hand='r'):
        if hand == 'l':
                keylist = LH_ARROWS_KEYLIST
        else:
                keylist = RH_ARROWS_KEYLIST

        #Create our stimuli
        arrow = visual.ImageStim(win=win, image=arrow_image_path, pos=ST_arrow_pos)

        stim_times = []
        for i in range(int(SA_repetition_times)):
                #Escribimos el circulo 
                arrow.size*= -1 #(hack ;) ) 
                arrow.draw()
                #Enviamos la pantalla con el circulo
                win.flip()
                #Tomamos el tiempo en el que fue enviado
                stim_times.append(core.getTime())
                #Lo mostramos por "SA_duration_time" segundos
                core.wait(SA_duration_time)
                #Mandamos pantalla en blanco
                win.flip()
                #Mostramos pantalla en blanco por "SA_interval_time" segundos.
                core.wait(SA_interval_time)
                #Vemos cuando fueron apretadas las teclas
                
        user_times = event.getKeys(keyList=keylist, timeStamped = True)
        #addMetric(result_path, (stim_times, user_times))

def tapping_exp(win, randid ,hand='r'):
        if hand == 'l': 
                keylist = LH_TAPPING_KEYLIST
        else:
                keylist = RH_TAPPING_KEYLIST
         
        #create some stimuli
        circle = visual.ImageStim(win=win, image=circle_image_path, pos=SA_circle_pos)

        #draw the stimuli and update the window
        stim_times = []
        for i in range(int(ST_repetition_times)):
                #Escribimos el circulo 
                circle.draw()
                #Enviamos la pantalla con el circulo
                win.flip()
                #Tomamos el tiempo en el que fue enviado
                stim_times.append(core.getTime())
                #Lo mostramos por "ST_duration_time" segundos
                core.wait(ST_duration_time)
                #Mandamos pantalla en blanco
                win.flip()
                #Mostramos pantalla en blanco por "ST_interval_time" segundos.
                core.wait(ST_interval_time)

        #Vemos cuando fueron apretadas las teclas        
        user_times = event.getKeys(keyList=LH_TAPPING_KEYLIST, timeStamped = True)
        #addMetric(result_path, (stim_times, user_times))

def dual_exp(win, randid ,inverted=False):
        if inverted:
                Keylist = INV_DUAL_KEYLIST
                circle = visual.ImageStim(win=win, image=circle_image_path, pos=DUN_circle_pos)
                arrow = visual.ImageStim(win=win, image=arrow_image_path, pos=DUN_arrow_pos)

        else:
                keylist = NORM_DUAL_KEYLIST
                circle = visual.ImageStim(win=win, image=circle_image_path, pos=DUI_circle_pos)
                arrow = visual.ImageStim(win=win, image=arrow_image_path, pos=DUI_arrow_pos)

        line = visual.ImageStim(win=win, image=line_image_path, pos=DU_line_pos)



        circleLeftTime = DU_circleTime
        arrowLeftTime = DU_arrowTime
    
        next = 'circle'
        current = next
        
        #For preparation
        line.draw()
        win.flip()
        core.wait(2)



        #draw the stimuli and update the window
        stim_times = []
        for i in range(int(DU_repetition_times)):
                #Escribimos el circulo
                current = next
                if (next == 'circle'):
                    arrowLeftTime -= circleLeftTime
                    circleLeftTime = DU_circleTime
                    if (circleLeftTime < arrowLeftTime):
                        next = 'circle'
                        interval_time = circleLeftTime
                    else:
                        next = 'arrow'
                        interval_time = arrowLeftTime
                    circle.draw()
                else:
                    circleLeftTime -= arrowLeftTime
                    arrowLeftTime = DU_arrowTime
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
                win.flip()
                #Tomamos el tiempo en el que fue enviado
                stim_times.append((current, core.getTime()))
                #Lo mostramos por "duration_time" segundos
                core.wait(DU_duration_time)
                #Mandamos pantalla en blanco
                line.draw()
                win.flip()
                #Mostramos pantalla en blanco por "interval_time" segundos.
                core.wait(DU_interval_time)
                #Vemos cuando fueron apretadas las teclas
                #Borramos el buffer
                #    event.clearEvents()
                
        user_times = event.getKeys(keyList=NORM_DUAL_KEYLIST, timeStamped = True)
        #addMetric(result_path, (stim_times, user_times))









#Additional functions
def writeMessage(win, mcode=None, msg=None, height=1):
        if msg is None:
            msg = messages[mcode-1]
        
        text = visual.TextStim(win,text = msg, color='black', height=height, wrapWidth = 40)
        text.draw()
        win.flip()

def say321(win):
    writeMessage(win,msg = "3", height=10)
    core.wait(1)
    writeMessage(win,msg = "2", height=10)
    core.wait(1)
    writeMessage(win,msg = "1", height=10)
    core.wait(1)
    win.flip()
    core.wait(1)

def expStarts(win, mcode):

    writeMessage(win,mcode)
    event.waitKeys(keyList=['return'])
    say321(win)

def expEnds(win):
    core.wait(1)
    writeMessage(win,msg=endMessage, height = 3)
    core.wait(3)

