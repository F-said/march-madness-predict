from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, RandomizedSearchCV, GridSearchCV
from sklearn.feature_selection import SelectFromModel
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import preprocessing

'''FOR TUNING HYPERPARAMETERS AND SUBMITTING PREDICTIONS'''
'''NOT FINAL SUBMISSION SELECTION SUNDAY'''

X_train = pd.read_csv("X_train_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)


y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

X_test = pd.read_csv("X_test_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"
sub_file = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

'''Dummy Classifier to get Baseline'''
dum = DummyClassifier(strategy="uniform")
dum.fit(X_train, y_train)
fold_size = 10
dum_crossval = cross_val_score(dum, X_train, y_train, cv=fold_size)

'''Learners
### Log Regression ###
clf = LogisticRegression(C=0.1)
bag_log = BaggingClassifier(base_estimator=clf, n_estimators=50, n_jobs=-1, oob_score=True, random_state=42, verbose=2)
bag_log.fit(X_train_feat6, y_train)

bag_log_crossval = cross_val_score(bag_log, X_train_feat6, y_train, cv=fold_size)

### kNN classifier ###
knn = KNeighborsClassifier(algorithm='kd_tree', n_neighbors=50)
bag_knn = BaggingClassifier(base_estimator=knn, n_estimators=50, n_jobs=-1, oob_score=True, random_state=42, verbose=2)
bag_knn.fit(X_train_feat5, y_train)

bag_knn_crossval = cross_val_score(bag_knn, X_train_feat5, y_train, cv=fold_size)
'''

### SVC ###
svc = SVC()
svc.fit(X_train, y_train)

svc_crossval = cross_val_score(svc, X_train, y_train, cv=fold_size)

### Random Forest ###
forest = RandomForestClassifier(criterion="entropy", n_estimators=50, n_jobs=-1, max_depth=5, oob_score=True,
                                max_features="sqrt", random_state=42, verbose=2)
forest.fit(X_train, y_train)

forest_crossval = cross_val_score(forest, X_train, y_train, cv=fold_size)

'''KFold Cross Val Accuracy
print("bag_log Feat 6 CV Score: ", bag_log_crossval.mean())
print("bag_knn Feat 5 CV Score: ", bag_knn_crossval.mean())
'''
print("Forest Feat 7 CV Score: ", forest_crossval.mean())

'''Submit predictions'''
probability = pd.DataFrame(forest.predict_proba(X_test))

pred = pd.Series(probability[1])
sub_file.insert(1, "Pred", pred)

sub_file.to_csv(path_or_buf="submission_seedordinal.csv", index=False)


