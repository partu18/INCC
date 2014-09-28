#!/usr/bin/env/python
from psychopy import visual, core  # import some libraries from PsychoPy

    #create a window
mywin = visual.Window([1200,700], monitor="testMonitor", units="deg", color=(255,255,255), colorSpace='rgb255')

#create some stimuli
circle = visual.ImageStim(win=mywin, image='../images/circle.png', pos=(0.0,0.0))
#arrow = visual.ImageStim(win=mywin, image='../images/arrow.png', pos=(-0.0,0.0))
#line = visual.ImageStim(win=mywin, image='../images/line.png', pos=(0.0,0.0))

#draw the stimuli and update the window
for i in range(0,3000,20):
  if ((i % 500 ) == 0):
    circle.draw()
    mywin.flip()

mywin.close()
core.quit()

#pause, so you get a chance to see it!
#core.wait(5.0)

# 500
# 720
