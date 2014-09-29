#!/usr/bin/env python
  
import pickle
import os

def loadData(filePath):
  if os.path.isfile(filePath) != True:
    with open(filePath, 'w') as fileData:
      fileData.write("{}")    
 
  with open(filePath, 'r') as fileData:
  	data = pickle.load(fileData.read())
  	return data

def addMetric(id, filePath, metric):
  data = loadData(filePath)
  ids = data.keys()
  print ids
  if id in ids:
    newId = max(ids) + 1
    print "El id actual " + id + " ya fue utilizado. Se guardara con el id " + newId
  else: 
    newId = id 

  data[newId] = metric
  with open(filePath, 'w') as fileData:
  	fileData.write(pickle.dump(data))

