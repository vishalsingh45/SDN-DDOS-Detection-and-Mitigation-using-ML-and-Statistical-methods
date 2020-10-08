#Accuracy reference: https://github.com/kshitijved/Support_Vector_Machine

from sklearn import svm, datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import tree


from sklearn.model_selection import cross_val_score

#step1: Load the data in numpy array
data = np.loadtxt(open('result.csv', 'rb'), delimiter=',')
X = data[:, 0:3]
y = data[:, 3]

#step2: Split the data to training & test data. Test-size is 0.25(25%) of data
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)


#step3: select the machine learning algorithm

#svm
#clf = svm.SVC()
clf = svm.SVC(kernel="linear",C=0.025)
#clf = tree.DecisionTreeClassifier()

#step4: Train the ML Algo with training data
clf.fit(x_train, y_train)


#step5: Pass the test data for classify or predict
classifier_predictions = clf.predict(x_test)

#step6. Calculate the accuracy from the the prediction result.
print("Accuracy is ", accuracy_score(y_test, classifier_predictions)*100)


#step7. calculate cross validation score
scores = cross_val_score(clf, x_train, y_train, cv=5)
print("cross-validation score",scores.mean())
