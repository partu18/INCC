#!/usr/bin/env python

import json

def loadData(filePath):
  print "cargango archivos"
  fileData = open(filePath, 'r')
  data = json.loads(fileData.read())
  return data

def addMetric(filePath, metric):
  data = loadData(filePath)
  print "agregando nueva metrica"
  data.append(metric)
  fileData = open(filePath, 'w')
  fileData.write(json.dumps(data))

addMetric('data.txt', {"partu": 20, "lao": 40})
print loadData('data.txt')
