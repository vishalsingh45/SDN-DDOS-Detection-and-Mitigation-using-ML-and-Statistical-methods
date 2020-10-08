#Accuracy reference: https://github.com/kshitijved/Support_Vector_Machine

from sklearn import svm, datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split



#step1: Load the data in numpy array
data = np.loadtxt(open('result.csv', 'rb'), delimiter=',')


#step2: Split the data to training & test data. Test-size is 0.25(25%) of data
X = data[:, 0:3]
y = data[:, 3]
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)#clf = svm.SVC()


#step3: select the machine learning algorithm

#svm
clf = svm.SVC()
#Decision Tree
#clf = tree.DecisionTreeClassifier()

#step4: Train the ML Algo with training data
clf.fit(x_train, y_train)



#step5: Pass the test data for classify or predict
classifier_predictions = clf.predict(x_test)


#step6. Calculate the Detection Ratio
print("Calculating Detection Ratio & False ")
length = len(y_test)
DD = 0
DN = 0
FD = 0
TN = 0
for i in range(0,length):
    #print("Actual",y_test[i], "prediction", classifier_predictions[i])
    #Calculating DR
    if y_test[i] == 1.0:
        if classifier_predictions[i] == 1.0:
            DD = DD + 1
        else:
            DN = DN + 1
    #calculating FAR
    if y_test[i] == 0.0:
        if classifier_predictions[i] == 1.0:
            FD = FD + 1
        else:
            TN = TN + 1
#print("DD", DD , "DN", DN)
DR = DD / (DD + DN)
print("Detection rate ", DR)


#print("FD", FD , "TN", TN)
FAR = FD / (FD + TN)
print("False Alarm rate ", FAR)
