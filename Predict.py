from sklearn.dummy import DummyClassifier
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC, SVC
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import SelectFromModel
import matplotlib.pyplot as plt

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
fold_size = 100
dum_crossval = cross_val_score(dum, X_train, y_train, cv=fold_size)

'''Learners'''
### Log Regression ###
clf = LogisticRegression(penalty='l2', C=0.1)
clf.fit(X_train, y_train)

### kNN classifier ###
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

### Linear SVC ###
lsvc = LinearSVC(C=0.1)
lsvc.fit(X_train, y_train)

# LSVC Selector
lscv_mean_selector = SelectFromModel(lsvc, threshold="mean")
lscv_med_selector = SelectFromModel(lsvc, threshold="median")

### SVC ###
svc = SVC(probability=True, C=0.1)
svc.fit(X_train, y_train)

### Random Forest ###
forest = RandomForestClassifier(criterion="entropy", n_estimators=50, n_jobs=2, max_depth=5, oob_score=True,
                                max_features="auto")
forest.fit(X_train, y_train)

### Decision Tree ###
tree = DecisionTreeClassifier(criterion="entropy", max_depth=5, max_features="auto")
tree.fit(X_train, y_train)

### SGD ###
sgd = SGDClassifier(loss="log")
sgd.fit(X_train, y_train)

'''KFold Cross-Validator'''
learners = ("LogReg", "kNN", "L-SVC", "RandomF", "Tree", "SGD", "SVC")
y_pos = np.arange(len(learners))
performance = []
clf_crossval = cross_val_score(clf, X_train, y_train, cv=fold_size)
knn_crossval = cross_val_score(knn, X_train, y_train, cv=fold_size)
lsvc_crossval = cross_val_score(lsvc, X_train, y_train, cv=fold_size)
forest_crossval = cross_val_score(forest, X_train, y_train, cv=fold_size)
tree_crossval = cross_val_score(tree, X_train, y_train, cv=fold_size)
sgd_crossval = cross_val_score(sgd, X_train, y_train, cv=fold_size)
svc_crossval = cross_val_score(svc, X_train, y_train, cv=fold_size)

performance.append(clf_crossval.mean())
performance.append(knn_crossval.mean())
performance.append(lsvc_crossval.mean())
performance.append(forest_crossval.mean())
performance.append(tree_crossval.mean())
performance.append(sgd_crossval.mean())
performance.append(svc_crossval.mean())

for n, name in enumerate(learners):
    print(name, ":", performance[n])

'''Submit predictions'''
probability = pd.DataFrame(forest.predict_proba(X_test))

pred = pd.Series(probability[1])
sub_file.insert(1, "Pred", pred)

sub_file.to_csv(path_or_buf="submission_seedordinal.csv", index=False)
