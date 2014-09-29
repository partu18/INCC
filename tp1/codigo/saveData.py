#!/usr/bin/env python
import pickle
import os



def loadMetrics(filePath):
  if os.path.isfile(filePath) != True:
    empty = {}
    with open(filePath, "wb") as fileData:
      pickle.dump(empty, fileData)
 
  with open(filePath, 'rb') as fileData:
  	data = pickle.load(fileData)
  	return data

def addMetric(id, metric, filePath):
  data = loadMetrics(filePath)
  ids = data.keys()

  if id in ids:
    newId = max(ids) + 1
    print "El id actual " + str(id) + " ya fue utilizado. Se guardara con el id " + str(newId)
  else: 
    newId = id 

  data[newId] = metric
  with open(filePath, 'wb') as fileData:
  	pickle.dump(data, fileData)

def closestOne(timeStamp, obtainedTime):

  x = -1
  for i in obtainedTime

def cleanSequence(stimTimes, obtainedTime):
  result = []

  for i in stimTimes:
    result.append(closestOne(i, obtainedTime))

  return result


def cleanMetric(metric):
  
  print "rightHand"
  print "single Tapping"

  stimTimes = metric.rightHand.singleTapping[0]
  obtainedTime = metric.rightHand.singleTapping[1]

  clenaObtainedTime clanSequence(stimTimes, obtainedTime)

  metric.rightHand.singleTapping[1] = clenaObtainedTime