import os
import math
import matplotlib.pyplot as plt
import numpy as np

from os import listdir
from os.path import isfile, join
from saveData import *
from constants import * 
from math import sqrt	




#Shared auxiliaries
def getAllResultsFiles():
	def getFilesFromDir(dirPath):
		return [join(dirPath,f) for f in listdir(dirPath) if isfile(join(dirPath,f))]	

	actual_path  = working_directory # /home/user/......../tp1/codigo

	tp1_path = actual_path.split('/') #['',home,user,....,tp1,codigo] 
	tp1_path = tp1_path[0:len(tp1_path)-1] #['',home,user,....,tp1]

	results_path = tp1_path + ['resultados2'] #['',home,user,....,tp1,resultados]
	results_path = '/'.join(results_path) # /home/user/......../tp1/resultados

	return getFilesFromDir(results_path)

def getAllDataPosibilities():
	result = []
	for hand in HANDS:
		for task in TASKS:
				obj = ''
				if 'D' in task: # Si es dual task
					obj = 'A'+obj
					result.append((hand,task,obj))
					obj = obj.replace('A','T')
				result.append((hand,task,obj))
	return result

def saveFigure(figure, file_path, h, t, o):
	#Saving plot	
	person_id = file_path.split('/')					#['home','user',........'person_id.data']
	person_id = person_id[len(person_id)-1]		#person_id.data
	person_id = person_id.split('.')[0]  		#person_id


	name = person_id+'_'+h+'_'+t
	if o != '':
		name = name + '_' + o


	#Creating directory (ES UN HACK PORQUE ESTOY APURADOO!! )
	user_graphics_path = working_directory + '/../graficos/' + person_id
	if not os.path.exists(user_graphics_path):
		os.makedirs(user_graphics_path)

	os.chdir(user_graphics_path)
	figure.savefig(name, dpi=100)




# Processing functions
def diffBtwTimes(stim_times,mes_times):
	assert(len(stim_times) == len(mes_times))
	return [stim_times[i] - mes_times[i] for i in range(len(stim_times))]

def successesAndFails(ini, fin, mes_times):
	#The fin index is included in the interval.
	assert(fin < len(mes_times))
	successes = 0
	fails = 0
	for i in range(ini,fin+1):
		if math.isnan(mes_times[i]):
			fails +=1
		else:
			successes +=1

	return (successes,fails)

def stdDeviationAndAverage(ini,fin,mes_times):
	#source : http://en.wikipedia.org/wiki/Standard_deviation
	assert(fin < len(mes_times))
	#Cleaning Nans
	mes_times = [t for t in mes_times if not math.isnan(t)]

	avg = sum(mes_times) / float(len(mes_times))


 	std_dev_factors  = mes_times[:]
 	
 	for i in range(len(std_dev_factors)):
 			std_dev_factors[i] -= avg
 			std_dev_factors[i] **= 2


 	std_dev = sqrt (sum(std_dev_factors) / float(len(std_dev_factors)))

 	return (avg,std_dev)	




def plotter():
	files_path = getAllResultsFiles()

	for f in files_path:
		data = loadMetrics(f)
		data = cleanMetric(data)

		for p in getAllDataPosibilities():
			(h,t,o) = p
			stim_times = data[h][t][o+'S']
			mes_times = data[h][t][o+'M']

			#FUNCTION TO PLOT
			result = diffBtwTimes(stim_times,mes_times)

			#PLOTTING
			l1 = range(len(result))
			plt.plot(l1,result,'ro')
			figure = plt.gcf()
			saveFigure(figure,f,h,t,o)
			plt.gcf().clear()

			





#EXAMPLES
def plotterVertical(path,hand,task,dualPrefix=''):
	data = loadMetrics('../resultados/'+path)
	
	data  = cleanMetric(data) #No deberia hacerlo denntro de load metrics esto ???


	data_stim_times = data[hand][task][dualPrefix+'S']
	data_mes_times = data[hand][task][dualPrefix+'M']

	data_stim_times = data_stim_times[3:len(data_stim_times)] 
	data_mes_times = data_mes_times[3:len(data_mes_times)] 
	
	l1 = [0 for a in data_stim_times]		
	l2 = [0.03 for a in data_mes_times]

	result = diffBtwTimes(data_stim_times, data_mes_times) 
	

	result = [t * 100 for t in result]

	plt.plot(l1,result,'ro')
	
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
