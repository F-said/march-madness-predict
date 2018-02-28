from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.feature_selection import VarianceThreshold

X_train = pd.read_csv("X_train_tourney.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1).drop(labels="AstDiff", axis=1).drop(labels="BlkDiff", axis=1).drop(labels="DRDiff", axis=1).\
    drop(labels="FGA3Diff", axis=1).drop(labels="FGADiff", axis=1).drop(labels="FGM3Diff", axis=1).drop(labels="FGMDiff", axis=1).\
    drop(labels="FTADiff", axis=1).drop(labels="FTMDiff", axis=1).drop(labels="ORDiff", axis=1).drop(labels="PFDiff", axis=1).\
    drop(labels="ScoreDiff", axis=1).drop(labels="StlDiff", axis=1).drop(labels="TODiff", axis=1)

y_train = pd.read_csv("y_train_tourney.csv")

X_test = pd.read_csv("X_test_season.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1).drop(labels="AstDiff", axis=1).drop(labels="BlkDiff", axis=1).drop(labels="DRDiff", axis=1).\
    drop(labels="FGA3Diff", axis=1).drop(labels="FGADiff", axis=1).drop(labels="FGM3Diff", axis=1).drop(labels="FGMDiff", axis=1).\
    drop(labels="FTADiff", axis=1).drop(labels="FTMDiff", axis=1).drop(labels="ORDiff", axis=1).drop(labels="PFDiff", axis=1).\
    drop(labels="ScoreDiff", axis=1).drop(labels="StlDiff", axis=1).drop(labels="TODiff", axis=1)

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"
sub_file = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

'''Logistic Classifier'''
clf = LogisticRegression(penalty='l2', C=0.1)
clf.fit(X_train, y_train)
probability = pd.DataFrame(clf.predict_proba(X_test))

'''Submit predictions'''
pred = pd.Series(probability[1])
sub_file.insert(1, "Pred", pred)

sub_file.to_csv(path_or_buf="submission_tourney.csv", index=False)
