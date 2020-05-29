import numpy as np
import pandas as pd

countM=0
countF=0
maggiore=0
count=0

array1 = np.genfromtxt ("file1.csv", delimiter = ",", skip_header = 1)
array1 = array1.astype(int)

array2 = np.genfromtxt ("file2.csv", delimiter = ",", skip_header = 1)
array2 = array2.astype(int)

array3 = np.genfromtxt ("file3.csv", delimiter = ",", skip_header = 1)
array3 = array3.astype(int)

array4 = np.genfromtxt ("file4.csv", delimiter = ",", skip_header = 1)
array4 = array4.astype(int)

array5 = np.genfromtxt ("file5.csv", delimiter = ",", skip_header = 1)
array5 = array5.astype(int)

array6 = np.genfromtxt ("file6.csv", delimiter = ",", skip_header = 1)
array6 = array6.astype(int)

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
array2finale = [[0 for y in range(66)] for x in range(maggiore*2)]
array3finale = [[0 for y in range(66)] for x in range(maggiore*2)]
array4finale = [[0 for y in range(66)] for x in range(maggiore*2)]
array5finale = [[0 for y in range(66)] for x in range(maggiore*2)]
array6finale = [[0 for y in range(66)] for x in range(maggiore*2)]

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

countM=0
countF=0
count=0

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
            count = count + 1


countM=0
countF=0
count=0

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
            count = count + 1

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

countM=0
countF=0
count=0

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
            count = count + 1

countM=0
countF=0
count=0

for i in array6:
    if i[66] == 0:
        if countM < maggiore:
            array6finale[count]= i
            countM=countM+1
            count = count + 1
    elif i[66] == 1:
        if countF < maggiore:
            array6finale[count]= i
            countF=countF + 1
            count = count + 1

pd.DataFrame(array1finale).to_csv("file1finale.csv")
pd.DataFrame(array2finale).to_csv("file2finale.csv")
pd.DataFrame(array3finale).to_csv("file3finale.csv")
pd.DataFrame(array4finale).to_csv("file4finale.csv")
pd.DataFrame(array5finale).to_csv("file5finale.csv")
pd.DataFrame(array6finale).to_csv("file6finale.csv")