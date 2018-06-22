import numpy as np
import csv as c
import os

class Obj():
	color = None
	name = None
	def __init__(self, objName):
		self.name = objName
		if (objName == "tree"):
			self.color = (0,255,0)
		elif (objName == "streetLight"):
			self.color = (0,0,255)
		elif (objName == "trafficLight"):
			self.color = (255,0,0)

directoryPath = "/home/augie/Ding/CutFlow"
dataPath = "./raw_xyz.csv"
newPath = "./color.csv"
objs = [Obj("tree"), Obj("streetLight"), Obj("trafficLight")]


original = np.genfromtxt(dataPath, delimiter=",", usecols=(0,1,2))
colorData = []
for i in range(original.shape[0]):
	colorData.append(list(original[i]))
	colorData[i] += [0,0,0]
indexRGB = len(colorData[0]) - 3


for obj in objs:
	for file in os.listdir(directoryPath):
		if file.startswith(obj.name) and file.endswith(".csv"):
			absPath = os.path.join(directoryPath, file)
			data= np.genfromtxt(absPath, delimiter=",")
			lastIndex = data.shape[1]-1
			for i in range(data.shape[0]):
				toColorIndex = int(round(data[i][lastIndex]))
				color = obj.color
				for j in range(3):
					colorData[toColorIndex][indexRGB + j] = color[j]




with open(newPath, "w") as f:
	writer = c.writer(f)
	for i in range(len(colorData)):
		writer.writerow(colorData[i])








