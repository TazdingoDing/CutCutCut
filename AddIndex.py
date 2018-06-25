import numpy as np
import csv as c
import os
dataPath = os.path.join(os.getcwd(),"Original.csv")
newPath = os.path.join(os.getcwd(),"CutThis.csv")

data= np.genfromtxt(dataPath, delimiter=",")
with open(newPath, "w") as f:
	writer = c.writer(f)
	for i in range(data.shape[0]):
		tmp = list(data[i])
		tmp.append(i)
		writer.writerow(tmp)

print "done"
