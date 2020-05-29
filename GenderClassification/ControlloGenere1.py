import numpy as np
import pandas as pd

countM=0
countF=0
maggiore=0
count=0

array1 = np.genfromtxt ("file1.csv", delimiter = ",", skip_header = 1)
array1 = array1.astype(int)

for genere in array1:
    if genere[66]==0:
        countM = countM + 1
    elif genere[66]==1:
        countF = countF + 1

if countM > countF:
    maggiore=countF
else:
    maggiore=countM

array1finale = [[0 for y in range(66)] for x in range(maggiore*2)]

countM=0
countF=0

for i in array1:
    if i[66] == 0:
        if countM < maggiore:
            array1finale[count]= i
            countM=countM+1
            count = count + 1
    elif i[66] == 1:
        if countF < maggiore:
            array1finale[count]= i
            countF=countF + 1
            count=count+1


pd.DataFrame(array1finale).to_csv("file1finale.csv")

