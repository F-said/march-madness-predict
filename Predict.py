from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score

X_train = pd.read_csv("X_train_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)

y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

X_test = pd.read_csv("X_test_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"
sub_file = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

'''Logistic Classifier'''
clf = LogisticRegression(penalty='l2', C=0.1)
clf.fit(X_train, y_train)

'''Knn Classifier'''
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

'''Linear SVC Classifier'''
lsvc = LinearSVC(C=0.1)
lsvc.fit(X_train, y_train)

'''KFold Cross-Validator'''
crossval = cross_val_score(clf, X_train, y_train, cv=100)
print("Logistic Regression Accuracy: ", crossval.mean())

crossval = cross_val_score(knn, X_train, y_train, cv=100)
print("Logistic Knn: ", crossval.mean())

crossval = cross_val_score(lsvc, X_train, y_train, cv=100)
print("Logistic Knn: ", crossval.mean())


'''Submit predictions'''
probability = pd.DataFrame(clf.predict_proba(X_test))

pred = pd.Series(probability[1])
sub_file.insert(1, "Pred", pred)

sub_file.to_csv(path_or_buf="submission_seedordinal.csv", index=False)
