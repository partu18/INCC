#!/usr/bin/env python
import pickle
import os
from conf import * 

def loadMetrics(filePath):
  if os.path.isfile(filePath) != True:
    return {}
 
  with open(filePath, 'rb') as fileData:
  	data = pickle.load(fileData)
  	return data

def addMetric(filePath, metric):

  with open(filePath, 'wb') as fileData:
  	pickle.dump(metric, fileData)

def matchedMeasure(timeStamp, mes_times):
  def inRange(a):
    return (a <= timeStamp+EPSILON) and (a >= timeStamp-EPSILON)

  mes_times.sort()

  result = [t for _,t in mes_times if inRange(t)]

  #Chequeamos que no haya mas de dos (y si hay dos menor al mini)
  if len(result) == 1:
    return result[0]
  elif len(result) == 2: #Chequeamos que sean bieeeen cercanos
    if abs(result[0]-result[1]) <= MINI_EPSILON:
      return result[0]
    else: #ERROR
      return float('NaN')
  else: #ERROR
    return float('NaN')
  

def cleanSequence(stimTimes, obtainedTime):
  result = []

  for i in stimTimes:
    result.append(matchedMeasure(i, obtainedTime))

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


