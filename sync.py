import random
import numpy as np

def FloatToPecentage(num):
    return "%.15f%%" % (num * 100)

dataDict = []
for i in range(0, 10000):
    dataList = []
    for j in range(0, 6):
        dataList.append(random.randint(1, 22))
    dataDict.append(dataList)

dataComDict = []
for date in range(1, 23):
    dataComList = []
    for m in range(0, 7):
        dataComList.append(m + date)
    dataComDict.append(dataComList)

comCountList = []
for dataList in dataDict:
    for dataComList in dataComDict:
        comCount = len([val for val in dataList if val in dataComList])
        if comCount > 0:
            comCountList.append((comCount))

comCountDict = {}
for count in comCountList:
    comCountDict[count] = comCountDict[count] + 1 if count in comCountDict else 1

sum = 0
for item in comCountDict:
    sum = sum + comCountDict[item]

for count in range(1, 7):
    temp = 0
    for i in range(count, 7):
        p = comCountDict[i]
        temp = temp + p
    print(str(count) + '   :   ' + str(FloatToPecentage(temp/sum)))
    print(' ')
