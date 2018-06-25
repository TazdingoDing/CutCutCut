import numpy as np
import csv as c
import os

class Obj():
	color = None
	name = None
	tag = 0
	def __init__(self, objName):
		self.name = objName
		if (objName == "SLA"):
			self.tag = 1
			self.color = (255,255,255)
		elif (objName == "SLB"):
			self.tag = 2
			self.color = (255,255,255)
		elif (objName == "TL"):
			self.tag = 3
			self.color = (255,0,0)
		elif (objName == "MTL"):
			self.tag = 4
			self.color = (255,0,0)
		elif (objName == "STL"):
			self.tag = 5
			self.color = (255,255,128)
		elif (objName == "SS"):
			self.tag = 6
			self.color = (0,128,255)
		elif (objName == "LS"):
			self.tag = 7
			self.color = (0,128,255)
		elif (objName == "Pedestrian"):
			self.tag = 8
			self.color = (128,255,0)
		elif (objName == "Tree"):
			self.tag = 9
			self.color = (0,255,0)
		elif (objName == "Building"):
			self.tag = 10
			self.color = (128,128,128)
		elif (objName == "Car"):
			self.tag = 11
			self.color = (64,64,64)
		elif (objName == "Bus"):
			self.tag = 12
			self.color = (64,64,64)
		else:
			self.tag = 0
			self.color = (0,0,0)

directoryPath = os.getcwd()
dataPath = os.path.join(directoryPath,"Original.csv")
newPath = os.path.join(directoryPath,"Color.csv")
items = ["SLA","SLB","TL","MTL","STL","SS","LS","Pedestrian","Tree","Building","Car","Bus"]
objs = [Obj(item) for item in items]


print "loading file..."
original = np.genfromtxt(dataPath, delimiter=",")
colorData = []
for i in range(original.shape[0]):
	tmp = list(original[i]) + [0,0,0,0]
	colorData.append(tmp)
#tag r g b
indexTag = len(colorData[0]) - 4
indexRGB = len(colorData[0]) - 3

print "mapping..."
for obj in objs:
	for f in os.listdir(directoryPath):
		if f.startswith(obj.name) and f.endswith(".csv"):
			absPath = os.path.join(directoryPath, f)
			data= np.genfromtxt(absPath, delimiter=",")
			lastIndex = data.shape[1]-1
			for i in range(data.shape[0]):
				#which point
				toColorIndex = int(round(data[i][lastIndex]))
				colorData[toColorIndex][indexTag] = obj.tag
				color = obj.color
				for j in range(3):
					colorData[toColorIndex][indexRGB + j] = color[j]
	
print "writing..."

with open(newPath, "w") as f:
	writer = c.writer(f)
	for i in range(len(colorData)):
		writer.writerow(colorData[i])


print "done"







