from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

X_train = pd.read_csv("X_train_tourney.csv")
X_train = X_train.drop(labels="Season", axis=1).drop(labels="Team1", axis=1).drop(labels="Team2", axis=1)
y_train = pd.read_csv("y_train_tourney.csv")

X_test = pd.read_csv("X_test_season.csv")
X_test = X_test.drop(labels="Season", axis=1).drop(labels="Team1", axis=1).drop(labels="Team2", axis=1)
X_test = X_test.fillna(value=0, axis=0)

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"
sub_file = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

'''Logistic Classifier'''
clf = LogisticRegression(penalty="l2", C=0.1)
clf.fit(X_train, y_train)
probability = pd.DataFrame(clf.predict_proba(X_test))

pred = pd.Series(probability[1])
sub_file.insert(1, "Pred", pred)

sub_file.to_csv(path_or_buf="submission_tourney.csv", index=False)
