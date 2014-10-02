#!/usr/bin/env python
import pickle
import os

WINDOWS = [0.1, 0.9]



def loadMetrics(filePath):
  if os.path.isfile(filePath) != True:
    return {}
 
  with open(filePath, 'rb') as fileData:
  	data = pickle.load(fileData)
  	return data

def addMetric(filePath, metric):

  with open(filePath, 'wb') as fileData:
  	pickle.dump(metric, fileData)

def firstValidMesure(timeStamp, obtainedTime):

  obtainedTime.sort()
  x = -1
  for i in obtainedTime:
    if i >= timeStamp + WINDOWS[1]:
      break
    else:
      if i >= (timeStamp - WINDOWS[0]):
        x = i
        break

  return x

def cleanSequence(stimTimes, obtainedTime):
  result = []

  for i in stimTimes:
    result.append(firstValidMesure(i, obtainedTime))

  return result


def cleanMetric(metrics):
  
  rhMetrics = metrics["RH"]
  lhMetrics = metrics["LH"]
  
  hands = [rhMetrics, lhMetrics]
  
  for metr in hands:

    cleanObtainedTime = cleanSequence(metr["T"]["S"], metr["T"]["M"])
    metr["T"]["M"] = cleanObtainedTime

    cleanObtainedTime = cleanSequence(metr["A"]["S"], metr["A"]["M"])
    metr["A"]["M"] = cleanObtainedTime

    cleanObtainedTime = cleanSequence(metr["D"]["TS"], metr["D"]["TM"])
    metr["D"]["TM"] = cleanObtainedTime

    cleanObtainedTime = cleanSequence(metr["D"]["AS"], metr["D"]["AM"])
    metr["D"]["AM"] = cleanObtainedTime

    cleanObtainedTime = cleanSequence(metr["DT"]["TS"], metr["DT"]["TM"])
    metr["DT"]["TM"] = cleanObtainedTime

    cleanObtainedTime = cleanSequence(metr["DT"]["AS"], metr["DT"]["AM"])
    metr["DT"]["AM"] = cleanObtainedTime

    cleanObtainedTime = cleanSequence(metr["DA"]["TS"], metr["DA"]["TM"])
    metr["DA"]["TM"] = cleanObtainedTime

    cleanObtainedTime = cleanSequence(metr["DA"]["AS"], metr["DA"]["AM"])
    metr["DA"]["AM"] = cleanObtainedTime

  return metrics