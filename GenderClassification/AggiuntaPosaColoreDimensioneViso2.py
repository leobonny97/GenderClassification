import numpy as np
import pandas as pd

array1 = np.genfromtxt ("file2finaleConEtà.csv", delimiter = ",", skip_header = 1)
array1 = array1.astype(int)

array = np.genfromtxt ("train_gtruth.csv", delimiter = ",", skip_header = 1)
array= array.astype(int)

file = [[0 for y in range(70)] for x in range(array1.shape[0])]


count=0

for (a) in array1:
    for (b) in array:
        if (a[65]) == (b[0]):
            file[count] = a[1:]
            file[count] = np.append(file[count], [b[3]])
            file[count] = np.append(file[count], [b[5]])
            file[count] = np.append(file[count], [b[8]])
            count = count + 1
            print(count)
            break

pd.DataFrame(file).to_csv("file2finaleConEtàPosaColoreDimensioneViso.csv")

