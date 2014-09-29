for i in range(40):
	menorADiez = ((i * 910) % 600) < 10
	mayorADiez = ((i * 910) % 600) > 590
	if  menorADiez or mayorADiez:
		print i * 910