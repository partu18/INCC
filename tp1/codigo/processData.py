import os
import math
import matplotlib.pyplot as plt
import numpy as np


from os import listdir
from os.path import isfile, join
from saveData import *
from constants import * 
from math import sqrt,log
from numpy.random import normal,uniform



#Plotting functions
def plotme(data,legend,grid=False,
					   logScale=False,
					   linestyle='',
					   bins_width=10,
					   text_at_pos=('',(0,0),(1,1),10),
					   wantHistogram=False,
					   xlabelName='X axis',
					   ylabelName='Y axis',
					   title='TITLE',
					   quality=200):

	'''
	data --> List of vectors that we want to plot
	legend --> List of names for each vector we want to plot
	logScale --> log_10(i) where i is each element of the array of arrays.

	linestyle -->  'o' => Puntos
					'--' => Linea Rayada
					por defecto => Linea comun

					others : ['-'  | '-.' | ':' | 'None' | ' ' | '']

	bins_width --> Width of the histogram "rectangles"
	text_at_pos --> IF you want to attach text in some (x,y) position. If you recieve a (text,(x,y),(w,z),FZ) will draw an arrow
					starting in (w,z) (where the text with FZ of fontsize will be) and pointing to (x,y) .
	wantHistogram --> If true, will plot a histogram
	xlabelName, ylabelName --> Names for axis
	title --> title of the graphic (it will also be the name of the archive)
	quality --> in DPI's
	'''
	assert(len(data) == len(legend))
	transparency = 0.3

	#Plot each data 
	for i in range(len(data)):
		current_data = data[i]

		#If wanted logScale
		if logScale:
			current_data = [log(current_data[j],10) for j in range(len(current_data))] #log en base 10

		#If you want Histogram a plot
		if wantHistogram:
			plt.hist(current_data, alpha=transparency, histtype= 'stepfilled', normed=True, bins=bins_width, label=legend[i])
		
		else:
			l1 = range(len(current_data))
			plt.plot(l1,current_data,linestyle,label = legend[i])
		transparency += 0.2


	#Settings 
	text,(pos_xA,pos_yA),(pos_xT,pos_yT),fz = text_at_pos

	plt.title(title)
	plt.xlabel(xlabelName)
	plt.ylabel(ylabelName)
	plt.grid(grid)
	plt.annotate(text,fontsize=fz, family='serif', xy=(pos_xA, pos_yA), xytext=(pos_xT, pos_yT),arrowprops=dict(facecolor='black', shrink=0.001))           
	plt.legend()

	
	#Saving Image
	figure = plt.gcf()
	figure.savefig(graphics_path+title, dpi=quality)
	plt.gcf().clear()






#Shared auxiliaries
def getAllResultsFiles():
	def getFilesFromDir(dirPath):
		return [join(dirPath,f) for f in listdir(dirPath) if isfile(join(dirPath,f))]	

	actual_path  = working_directory # /home/user/......../tp1/codigo

	tp1_path = actual_path.split('/') #['',home,user,....,tp1,codigo] 
	tp1_path = tp1_path[0:len(tp1_path)-1] #['',home,user,....,tp1]

	results_path = tp1_path + ['resultados'] #['',home,user,....,tp1,resultados]
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

def initMatrix():

	files_path = getAllResultsFiles()

	matrix = []
	for f in files_path:
		data = loadMetrics(f)
		data = cleanMetric(data)
		
		for p in getAllDataPosibilities():
			(h,t,o) = p
			stim_times = data[h][t][o+'S']
			mes_times = data[h][t][o+'M']
	
			person_id = f.split('/')						#['home','user',........'person_id.data']
			person_id = person_id[len(person_id)-1]			#person_id.data
			person_id = person_id.split('.')[0]  			#person_id

			diff_times = diffBtwTimes(stim_times,mes_times)
			for i in range(len(stim_times)):
				matrix.append([person_id,i,stim_times[i],mes_times[i],diff_times[i],h,t,o])

	return matrix
def matrixToCSV(matrix, writePath):

	with open(writePath, 'wb') as fileData:
		fileData.write("subject id;stim number;stim timeStamp;mesure timeStamp;diff time;hand;type;subtype\n")
		for line in matrix:
			toWrite = ""
			for i in range(len(line)):
				toWrite += str(line[i])
				if i != (len(line)-1):
					toWrite += ";"
			toWrite += '\n'
			fileData.write(toWrite)
def filterData(matrix, filterFunc, dataIndex):

	datos = filter(filterFunc,matrix)
	datos = [line[dataIndex] for line in datos]

	return datos
def average(data):
	if len(data) > 0:
		return sum(data)/float(len(data))
	else:
		return float('NaN')
def variance(data):
	if len(data) > 0:
		p = average(data)
		return sum([(xi - p)**2 for xi in data])/float(len(data))
	else:
		return float('NaN')
def resultPerBlocks(intervalSize):
	matrix = initMatrix()
	result = []
	
	for p in getAllDataPosibilities():
		(h,t,o) = p
		blocks = []

		for i in range(50/intervalSize):
			data = filterData(matrix, (lambda x: (x[4] < 0.3) and (x[1] in range(i*intervalSize,(i+1)*intervalSize)) and (x[5] == h) and (x[6] == t) and (x[7] == o) ), 4)
			blocks.append(data)

		averages = [ average(d) for d in blocks]
		variances = [ variance(d) for d in blocks]
		result.append([averages,variances,p])
	
	return result
def plotAllPosibilitiesPerBlocks(intervalSize):

	for data in resultPerBlocks(intervalSize):
		(h,t,o) = data[2]
		plotme([data[0]],[h+"-"+t+"-"+o],xlabelName=str(intervalSize) + "stims size blocks", ylabelName="block average", title="average-"+h+"-"+t+"-"+o)
		plotme([data[1]],[h+"-"+t+"-"+o],xlabelName=str(intervalSize) + "stims size blocks", ylabelName="block variance", title="variance-"+h+"-"+t+"-"+o)



# Processing functions
def asd():
	alls='*'
	matrix = initMatrix()
	result = []
	interval = 3

	for i in range(80/interval):
		datos = filter(lambda x: (x[4] < 0.3 and x[1] in range(i*interval,(i+1)*interval) and x[5] == "LH" and x[6] == "D" and x[7] == "T"),matrix)
		datos = [e for [_,_,_,_,e,_,_,_] in datos]
		if len(datos) > 0:
			prom  = sum(datos)/float(len(datos))
			result.append(prom)
	#PLOTTING
	l1 = range(len(result))
	plt.plot(l1,result,'ro')
	figure = plt.gcf()
	plt.show()
	#saveFigure(figure,f,h,t,o)
	plt.gcf().clear()



def diffBtwTimes(stim_times,mes_times):
	assert(len(stim_times) == len(mes_times))
	result = []
	for i in range(len(mes_times)):
		if math.isnan(mes_times[i]):
			result.append(EPSILON*2)
		else:
			result.append(stim_times[i] - mes_times[i]) 
			
	return result
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
def stdDeviationAndAverage(ini,fin,diff_times):
	#source : http://en.wikipedia.org/wiki/Standard_deviation
	assert(fin < len(diff_times))
	#Cleaning Nans
	for i in range(ini,fin+1):
		if math.isnan(diff_times[i]):
			diff_times[i] = EPSILON *2


	avg = sum(diff_times[ini:fin+1]) / float(len(diff_times[ini:fin+1]))


 	std_dev_factors  = diff_times[ini:fin+1]
 	
 	for i in range(len(std_dev_factors)):
 			std_dev_factors[i] -= avg
 			std_dev_factors[i] **= 2


 	std_dev = sqrt (sum(std_dev_factors) / float(len(std_dev_factors)))

 	return (avg,std_dev)	


def plotter_for_each_subject():
	files_path = getAllResultsFiles()

	for f in files_path:
		data = loadMetrics(f)
		data = cleanMetric(data)

		for p in getAllDataPosibilities():
			(h,t,o) = p
			stim_times = data[h][t][o+'S']
			mes_times = data[h][t][o+'M']

			#FUNCTION TO PLOT
			###DIFFS###
			#result = diffBtwTimes(stim_times,mes_times)
			#
			#
			#	

			### AVG and STDVAR
			result = []
			diff_times = diffBtwTimes(stim_times,mes_times)
			for ini in range(len(diff_times)-4):
				avg,_ = stdDeviationAndAverage(ini,ini+4,diff_times)
				result.append(avg)
	

			#PLOTTING
			l1 = range(len(result))
			plt.plot(l1,result,'r')
			figure = plt.gcf()
			saveFigure(figure,f,h,t,o)
			plt.gcf().clear()
def plotter_for_all():
	files_path = getAllResultsFiles()

	for p in getAllDataPosibilities():
		result_p = []
		(h,t,o) = p
		stim_times = data[h][t][o+'S']
		mes_times = data[h][t][o+'M']


		for f in files_path:
			data = loadMetrics(f)
			data = cleanMetric(data)

			### AVG and STDVAR
			result_subj = []
			diff_times = diffBtwTimes(stim_times,mes_times)
			for ini in range(len(diff_times)-4):
				avg,_ = stdDeviationAndAverage(ini,ini+4,diff_times)
				result_subj.append(avg)


	

	#PLOTTING
	l1 = range(len(result))
	plt.plot(l1,result,'r')
	figure = plt.gcf()
	saveFigure(figure,f,h,t,o)
	plt.gcf().clear()
def histogram_for_all():
	files_path = getAllResultsFiles()

	for p in getAllDataPosibilities():
		result_p = []
		(h,t,o) = p

		diffs = []
		for f in files_path:
			data = loadMetrics(f)
			data = cleanMetric(data)
			stim_times = data[h][t][o+'S']
			mes_times = data[h][t][o+'M']


			### AVG and STDVAR
			diff_times = diffBtwTimes(stim_times,mes_times)
			for i in diff_times:
				diffs.append(i)

	

	#PLOTTING
	
	fig, ax = plt.subplots()
	print diffs

	p = ax.hist(diffs,facecolor="black")
	plt.xlim(-0.50, 0.60)
	plt.show()

	# figure = plt.gcf()
	# saveFigure(figure,f,h,t,o)
	# plt.gcf().clear()

#Filtering Matrix
def filterMatrix(cond, matrix):
	result = []
	for fila in matrix:
		if cumple(fila,cond):
			result.append(fila)
	return result

def cumple(fila, cond):
	result = True
	for i in range(len(fila)):
		if cond[i] != "*":
			if fila[i] not in cond[i]:
				result = False
	return result

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
