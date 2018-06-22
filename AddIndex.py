import numpy as np
import csv as c
dataPath = "./raw_xyz.csv"
newPath = "./new.csv"
cols = (0,1,2,3)




data= np.genfromtxt(dataPath, delimiter=",", usecols=cols)


with open(newPath, "w") as f:
	writer = c.writer(f)
	for i in range(data.shape[0]):
		tmp = list(data[i])
		tmp.append(i)
		writer.writerow(tmp)






