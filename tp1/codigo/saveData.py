#!/usr/bin/env python

import json

def loadData(filePath):
  with open(filePath, 'r') as fileData:
  	data = json.loads(fileData.read())
  	return data

def addMetric(filePath, metric):
  data = loadData(filePath)
  data.append(metric)
  with open(filePath, 'w') as fileData:
  	fileData.write(json.dumps(data))

