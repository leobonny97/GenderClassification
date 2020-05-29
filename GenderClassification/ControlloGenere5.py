import numpy as np
import pandas as pd

countM=0
countF=0
maggiore=0
count=0

array5 = np.genfromtxt ("file5.csv", delimiter = ",", skip_header = 1)
array5 = array5.astype(int)

for genere in array5:
    if genere[66]==0:
        countM = countM + 1
    elif genere[66]==1:
        countF = countF + 1

if countM > countF:
    maggiore=countF
else:
    maggiore=countM

array5finale = [[0 for y in range(66)] for x in range(maggiore*2)]

countM=0
countF=0

for i in array5:
    if i[66] == 0:
        if countM < maggiore:
            array5finale[count]= i
            countM=countM+1
            count = count + 1
    elif i[66] == 1:
        if countF < maggiore:
            array5finale[count]= i
            countF=countF + 1
            count=count+1

pd.DataFrame(array5finale).to_csv("file5finale.csv")
