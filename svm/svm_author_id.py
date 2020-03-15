#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# features_train = features_train[:len(features_train)//100]
# labels_train = labels_train[:len(labels_train)//100]
print("is this working")
clf = svm.SVC(kernel="rbf", C=10000)
print("created classifier")
clf.fit(features_train, labels_train)
print("fit classifier")
pred = clf.predict(features_test)
print("10:", pred[10])
print("26:", pred[26])
print("50:", pred[50])
print("made prediction")
chris_count = 0
for elem in pred:
	if elem == 1:
		chris_count += 1
print("chris_count:", chris_count)
print(accuracy_score(pred, labels_test))

#########################################################
### your code goes here ###

#########################################################


