import numpy as np
import pandas as pd

countM=0
countF=0
maggiore=0
count=0

array4 = np.genfromtxt ("file4.csv", delimiter = ",", skip_header = 1)
array4 = array4.astype(int)

for genere in array4:
    if genere[66]==0:
        countM = countM + 1
    elif genere[66]==1:
        countF = countF + 1

if countM > countF:
    maggiore=countF
else:
    maggiore=countM

array4finale = [[0 for y in range(66)] for x in range(maggiore*2)]

countM=0
countF=0

for i in array4:
    if i[66] == 0:
        if countM < maggiore:
            array4finale[count]= i
            countM=countM+1
            count = count + 1
    elif i[66] == 1:
        if countF < maggiore:
            array4finale[count]= i
            countF=countF + 1
            count=count+1

pd.DataFrame(array4finale).to_csv("file4finale.csv")
