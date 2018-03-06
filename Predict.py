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

X_train = pd.read_csv("X_train_seedordinal_selected.csv")

y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

X_test = pd.read_csv("X_test_seedordinal_selected.csv")

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"
sub_file = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

fold_size = 10

'''Learners'''
### Log Regression ###
# Hyperparameters found using gridsearch
clf = LogisticRegression(C=0.001)

bag_log = BaggingClassifier(base_estimator=clf, n_estimators=50, n_jobs=-1, oob_score=True, random_state=42)
bag_log.fit(X_train, y_train)

bag_log_crossval = cross_val_score(bag_log, X_train, y_train, cv=fold_size)

### kNN classifier ###
# Hyperparameters found using gridsearch
knn = KNeighborsClassifier(algorithm='ball_tree', n_neighbors=17)
knn.fit(X_train, y_train)

knn_crossval = cross_val_score(knn, X_train, y_train, cv=fold_size)

### SVC ###
# Hyperparameters found using gridsearch
svc = SVC(C=0.001, kernel='linear', probability=True, random_state=42)
svc.fit(X_train, y_train)

svc_crossval = cross_val_score(svc, X_train, y_train, cv=fold_size)

### Random Forest ###
forest = RandomForestClassifier(criterion='entropy', max_depth=5, max_features='auto', n_estimators=150, oob_score=True)
forest.fit(X_train, y_train)

forest_crossval = cross_val_score(forest, X_train, y_train, cv=fold_size)

'''KFold Cross Val Accuracy'''
print("bag_log CV Score: ", bag_log_crossval.mean())
print("knn CV Score: ", knn_crossval.mean())
print("Svc CV Score: ", svc_crossval.mean())
print("Forest CV Score: ", forest_crossval.mean())

'''Submit predictions'''
probability = pd.DataFrame(forest.predict_proba(X_test))

pred = pd.Series(probability[1])
sub_file.insert(1, "Pred", pred)

sub_file.to_csv(path_or_buf="submission_seedordinal.csv", index=False)


