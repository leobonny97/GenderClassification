import numpy as np
import pandas as pd

countM=0
countF=0
maggiore=0
count=0

array6 = np.genfromtxt ("file6.csv", delimiter = ",", skip_header = 1)
array6 = array6.astype(int)

for genere in array6:
    if genere[82]==0:
        countM = countM + 1
    elif genere[82]==1:
        countF = countF + 1

if countM > countF:
    maggiore=countF
else:
    maggiore=countM

array6finale = [[0 for y in range(82)] for x in range(maggiore*2)]

countM=0
countF=0

for i in array6:
    if i[82] == 0:
        if countM < maggiore:
            array6finale[count]= i
            countM=countM+1
            count = count + 1
    elif i[82] == 1:
        if countF < maggiore:
            array6finale[count]= i
            countF=countF + 1
            count=count+1

pd.DataFrame(array6finale).to_csv("file6finale.csv")
