import numpy as np
import pandas as pd

countM=0
countF=0
maggiore=0
count=0

array3 = np.genfromtxt ("file3.csv", delimiter = ",", skip_header = 1)
array3 = array3.astype(int)

array4 = np.genfromtxt ("file4.csv", delimiter = ",", skip_header = 1)
array4 = array4.astype(int)

for genere in array3:
    if genere[66]==0:
        countM = countM + 1
    elif genere[66]==1:
        countF = countF + 1

if countM > countF:
    maggiore=countF
else:
    maggiore=countM

array3finale = [[0 for y in range(66)] for x in range(maggiore*2)]
array4finale = [[0 for y in range(66)] for x in range(maggiore*2)]

countM=0
countF=0

for i in array3:
    if i[66] == 0:
        if countM < maggiore:
            array3finale[count]= i
            countM=countM+1
            count = count + 1
    elif i[66] == 1:
        if countF < maggiore:
            array3finale[count]= i
            countF=countF + 1
            count=count+1

countM=0
countF=0
count=0

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
            count = count + 1

pd.DataFrame(array3finale).to_csv("file3finale.csv")
pd.DataFrame(array4finale).to_csv("file4finale.csv")
