
def cordinador(time1, time2, durationTime):
	for i in range(40):
		menorADiez = ((i * time1) % time2) < durationTime
		mayorADiez = ((i * time1) % time2) > time2 - durationTime
		if  menorADiez or mayorADiez:
			print i * time1