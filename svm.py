from __future__ import division
import numpy
import os
from sklearn import svm
from collections import deque
from sklearn import tree



class SVM:

    def __init__(self):
        """
        train the model from generated training data in generate-data folder
        """
        data = numpy.loadtxt(open('result.csv', 'rb'), delimiter=',', dtype='str')
        #Support_Vector_Machine
        #self.svm = svm.SVC()
        # Decision tree
        self.svm = tree.DecisionTreeClassifier()
        self.svm.fit(data[:, 0:3], data[:, 3])


    def classify(self, data):
        fparams = numpy.zeros((1, 3))
        fparams[:,0] = data[0]
        fparams[:,1] = data[1]
        fparams[:,2] = data[2]
        prediction = self.svm.predict(fparams)
        print("SVM input data", data , "prediction result ", prediction)
        return prediction
