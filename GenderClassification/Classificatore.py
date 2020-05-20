import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

array = np.genfromtxt ("file2finale.csv", delimiter = ",", skip_header = 1)
array = array.astype(int)

data = [[0 for y in range(63)] for x in range(array.shape[0])]
genere = ['' for xx in range(array.shape[0])]

count = 0

for i in array:
    data[count]= i[2:66]
    genere[count] = i[67]
    count = count + 1


#suddividiamo il dataset in training set e test set;
X_train, X_test, y_train, y_test = train_test_split(data, genere, test_size=0.3, shuffle=True)

#scegliamo il classificatore che vogliamo utilizzare
classifier = svm.SVC(gamma=0.001)

#alleniamo l'algoritmo utilizzando il training set
classifier.fit(X_train, y_train)

#testiamo i valori del test set e stampiamo i risultati
predicted = classifier.predict(X_test)

#stampiamo la matrice di confusione
print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(y_test, predicted)))
disp = metrics.plot_confusion_matrix(classifier, X_test, y_test)
disp.figure_.suptitle("Confusion Matrix")
print("Confusion matrix:\n%s" % disp.confusion_matrix)
plt.show()

maschi=0
femmine=0
for i in y_test:
    if i==0:
        maschi=maschi+1
    else:
        femmine=femmine+1

