import numpy as np
import pandas as pd

countM=0
countF=0
maggiore=0
count=0

array2 = np.genfromtxt ("file2.csv", delimiter = ",", skip_header = 1)
array2 = array2.astype(int)

for genere in array2:
    if genere[66]==0:
        countM = countM + 1
    elif genere[66]==1:
        countF = countF + 1

if countM > countF:
    maggiore=countF
else:
    maggiore=countM

array2finale = [[0 for y in range(66)] for x in range(maggiore*2)]

countM=0
countF=0

for i in array2:
    if i[66] == 0:
        if countM < maggiore:
            array2finale[count]= i
            countM=countM+1
            count = count + 1
    elif i[66] == 1:
        if countF < maggiore:
            array2finale[count]= i
            countF=countF + 1
            count=count+1

pd.DataFrame(array2finale).to_csv("file2finale.csv")
