import numpy as np

countM=0
countF=0

array1 = np.genfromtxt ("file1.csv", delimiter = ",", skip_header = 1)
array1 = array1.astype(int)

array2 = np.genfromtxt ("file2.csv", delimiter = ",", skip_header = 1)
array2 = array2.astype(int)

for genere in array1:
    if genere[66]==0:
        countM = countM + 1
    elif genere[66]==1:
        countF = countF + 1

print(str(countF)+","+str(countM))

for i in range(0):
    if array1[i][66]==0:
