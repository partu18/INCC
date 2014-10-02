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
        circleDurLeftTime = -1
        arrowDurLeftTime = -1
        usedTime = 0
    
        interval_time = min(DU_arrowTime, DU_circleTime)

        #For preparation
        line.draw()
        win.flip()
        core.wait(2)



        #draw the stimuli and update the window
        circle_stim_times = []
        arrow_stim_times = []
        for i in range(int(DU_repetition_times)):
            core.wait(interval_time)
            circleLeftTime -= interval_time
            arrowLeftTime -= interval_time
            circleDurLeftTime -= interval_time
            arrowDurLeftTime -= interval_time

            # configuramos los duration times
            if circleLeftTime == 0:
                circle_stim_times.append(core.getTime())
                circleDurLeftTime = DU_duration_time
                
            if arrowLeftTime == 0:
                arrow_stim_times.append(core.getTime())
                arrowDurLeftTime = DU_duration_time
            
            # mostramos los que esten con duration time positivos  
            if circleDurLeftTime > 0:
                circleLeftTime = DU_circleTime
                circle.draw()

            if arrowDurLeftTime > 0:
                arrowLeftTime = DU_arrowTime
                arrow.size*= -1 #(hack ;) ) 
                arrow.draw()

            #dibujamos la linea
            line.draw()

            # establecemos el proximo intervalo para el wait
            cdt = circleDurLeftTime if circleDurLeftTime > 0 else max(arrowLeftTime,circleLeftTime,arrowDurLeftTime)
            adt = arrowDurLeftTime if arrowDurLeftTime > 0 else max(arrowLeftTime,circleLeftTime)
            interval_time = min(circleLeftTime,arrowLeftTime,cdt,adt)

                
        user_times = event.getKeys(keyList=NORM_DUAL_KEYLIST, timeStamped = True)
        return stim_times, user_times




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

