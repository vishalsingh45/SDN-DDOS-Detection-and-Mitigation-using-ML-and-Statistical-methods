#http://rasbt.github.io/mlxtend/user_guide/plotting/plot_decision_regions/
from __future__ import division
import numpy
import os
from sklearn import svm
from collections import deque
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
import numpy as np

data = np.loadtxt(open('result.csv', 'rb'), delimiter=',')

#sfe,ssip,rfip
sfe = 0
ssip = 1
rfip = 2





#Graph1 sfe & ssip
X = data[:, [sfe,ssip]]
y = data[:, 3]
clf = svm.SVC()
clf.fit(X, y)
# Plot Decision Region using mlxtend's awesome plotting function
fig = plt.figure(figsize=(10,8))
fig = plot_decision_regions(X=X,
                      y=y.astype(int),
                      clf=clf,
                      legend=2)
plt.title('SVM DDoS - Decision Region Boundary', size=16)
plt.xlabel('Speed of Flow Entry')
plt.ylabel('Speed of Source IP')
plt.savefig("svm_graph1.png")




#Graph1 sfe & rfip
X = data[:, [sfe,rfip]]
y = data[:, 3]
clf = svm.SVC()
clf.fit(X, y)
# Plot Decision Region using mlxtend's awesome plotting function
fig = plt.figure(figsize=(10,8))
fig = plot_decision_regions(X=X,
                      y=y.astype(int),
                      clf=clf,
                      legend=2)
plt.title('SVM DDoS - Decision Region Boundary', size=16)
plt.xlabel('sfe')
plt.ylabel('rfip')
plt.savefig("svm_graph2.png")
