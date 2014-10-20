import matplotlib.pyplot as plt
from saveData import *
import numpy as np


def plotterVertical(path,hand,task,dualPrefix=''):
	data = loadMetrics('../resultados/'+path)
	
	data  = cleanMetric(data)


	data_stim_times = data[hand][task][dualPrefix+'S']
	data_mes_times = data[hand][task][dualPrefix+'M']

	data_stim_times = data_stim_times[3:len(data_stim_times)] 
	data_mes_times = data_mes_times[3:len(data_mes_times)] 

	#data_stim_times = [a-min(data_stim_times) for a in data_stim_times]
	#data_mes_times = [a-min(data_mes_times) for a in data_mes_times]	
	
	l1 = [0 for a in data_stim_times]
	l2 = [0.03 for a in data_mes_times]

	print data_mes_times

	plt.plot(l1,data_stim_times,'ro',l2,data_mes_times,'bo')
	plt.xlim(-4,4)
	plt.show()

def plotterHorizontal(path,hand,task,dualPrefix=''):
	data = loadMetrics('../resultados/'+path)
	data_stim_times = data[hand][task][dualPrefix+'S']
	data_mes_times = data[hand][task][dualPrefix+'M']

	data_mes_times = [b for a,b in data_mes_times]

	data_stim_times = data_stim_times[3:len(data_stim_times)] 
	data_mes_times = data_mes_times[3:len(data_mes_times)] 
	
	l1 = range(len(data_stim_times))
	l2 = range(len(data_mes_times))

	plt.plot(l1,data_stim_times,'ro',l2,data_mes_times,'bo')
	plt.xlim(0,max(len(data_mes_times),len(data_stim_times)))
	plt.show()
