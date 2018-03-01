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

# Log Regression Selector
log_mean_selector = SelectFromModel(clf, threshold="mean")
log_med_selector = SelectFromModel(clf, threshold="median")

X_train_selectmean = log_mean_selector.fit_transform(X_train, y_train)
X_train_selectmed = log_med_selector.fit_transform(X_train, y_train)

clf_mean = LogisticRegression(penalty='l2', C=0.1)
clf_mean.fit(X_train_selectmean, y_train)

clf_med = LogisticRegression(penalty='l2', C=0.1)
clf_med.fit(X_train_selectmed, y_train)

### kNN classifier ###
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# kNN Selector
knn_mean_selector = SelectFromModel(knn, threshold="mean")
knn_mean_selector.fit(X_train, y_train)
knn_med_selector = SelectFromModel(knn, threshold="median")
knn_med_selector.fit(X_train, y_train)

X_train_selectmean = knn_mean_selector.transform(X_train)
X_train_selectmed = knn_med_selector.transform(X_train)

knn_mean = KNeighborsClassifier(n_neighbors=5)
knn_mean.fit(X_train_selectmean, y_train)

knn_med = KNeighborsClassifier(n_neighbors=5)
knn_med.fit(X_train_selectmed, y_train)

### Linear SVC ###
lsvc = LinearSVC(C=0.1)
lsvc.fit(X_train, y_train)

# LSVC Selector
lscv_mean_selector = SelectFromModel(lsvc, threshold="mean")
lscv_med_selector = SelectFromModel(lsvc, threshold="median")

X_train_selectmean = lscv_mean_selector.fit_transform(X_train, y_train)
X_train_selectmed = lscv_med_selector.fit_transform(X_train, y_train)

lsvc_mean = LinearSVC(C=0.1)
lsvc_mean.fit(X_train_selectmean, y_train)

lsvc_med = LinearSVC(C=0.1)
lsvc_med.fit(X_train_selectmed, y_train)

### SVC ###
svc = SVC(probability=True, C=0.1)
svc.fit(X_train, y_train)

# SVC Selector
svc_mean_selector = SelectFromModel(svc, threshold="mean")
svc_med_selector = SelectFromModel(svc, threshold="median")

X_train_selectmean = svc_mean_selector.fit_transform(X_train, y_train)
X_train_selectmed = svc_med_selector.fit_transform(X_train, y_train)

svc_mean = SVC(probability=True, C=0.1)
svc_mean.fit(X_train_selectmean, y_train)

svc_med = SVC(probability=True, C=0.1)
svc_med.fit(X_train_selectmed, y_train)

### Random Forest ###
forest = RandomForestClassifier(criterion="entropy", n_estimators=50, n_jobs=2, max_depth=5, oob_score=True,
                                max_features="auto")
forest.fit(X_train, y_train)

# Random Forest Selector
fr_mean_selector = SelectFromModel(forest, threshold="mean")
fr_med_selector = SelectFromModel(forest, threshold="median")

X_train_selectmean = fr_mean_selector.fit_transform(X_train, y_train)
X_train_selectmed = fr_med_selector.fit_transform(X_train, y_train)

forest_mean = RandomForestClassifier(criterion="entropy", n_estimators=50, n_jobs=2, max_depth=5, oob_score=True,
                                max_features="auto")
forest_mean.fit(X_train_selectmean, y_train)

forest_med = RandomForestClassifier(criterion="entropy", n_estimators=50, n_jobs=2, max_depth=5, oob_score=True,
                                max_features="auto")
forest_med.fit(X_train_selectmed, y_train)

### Decision Tree ###
tree = DecisionTreeClassifier(criterion="entropy", max_depth=5, max_features="auto")
tree.fit(X_train, y_train)

# Decision Tree Selector
tree_mean_selector = SelectFromModel(tree, threshold="mean")
tree_med_selector = SelectFromModel(tree, threshold="median")

X_train_selectmean = tree_mean_selector.fit_transform(X_train, y_train)
X_train_selectmed = tree_med_selector.fit_transform(X_train, y_train)

tree_mean = DecisionTreeClassifier(criterion="entropy", max_depth=5, max_features="auto")
tree_mean.fit(X_train_selectmean, y_train)

tree_med = DecisionTreeClassifier(criterion="entropy", max_depth=5, max_features="auto")
tree_med.fit(X_train_selectmed, y_train)

### SGD ###
sgd = SGDClassifier(loss="log")
sgd.fit(X_train, y_train)

# SVC Selector
sgd_mean_selector = SelectFromModel(sgd, threshold="mean")
sgd_med_selector = SelectFromModel(sgd, threshold="median")

X_train_selectmean = sgd_mean_selector.fit_transform(X_train, y_train)
X_train_selectmed = sgd_med_selector.fit_transform(X_train, y_train)

sgd_mean = SGDClassifier(loss="log")
sgd_mean.fit(X_train_selectmean, y_train)

sgd_med = SGDClassifier(loss="log")
sgd_med.fit(X_train_selectmed, y_train)

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

performance_mean = []
clf_crossval = cross_val_score(clf_mean, X_train_selectmean, y_train, cv=fold_size)
knn_crossval = cross_val_score(knn_mean, X_train_selectmean, y_train, cv=fold_size)
lsvc_crossval = cross_val_score(lsvc_mean, X_train_selectmean, y_train, cv=fold_size)
forest_crossval = cross_val_score(forest_mean, X_train_selectmean, y_train, cv=fold_size)
tree_crossval = cross_val_score(tree_mean, X_train_selectmean, y_train, cv=fold_size)
sgd_crossval = cross_val_score(sgd_mean, X_train_selectmean, y_train, cv=fold_size)
svc_crossval = cross_val_score(svc_mean, X_train_selectmean, y_train, cv=fold_size)

performance_mean.append(clf_crossval.mean())
performance_mean.append(knn_crossval.mean())
performance_mean.append(lsvc_crossval.mean())
performance_mean.append(forest_crossval.mean())
performance_mean.append(tree_crossval.mean())
performance_mean.append(sgd_crossval.mean())
performance_mean.append(svc_crossval.mean())

performance_med = []
clf_crossval = cross_val_score(clf_med, X_train_selectmed, y_train, cv=fold_size)
knn_crossval = cross_val_score(knn_med, X_train_selectmed, y_train, cv=fold_size)
lsvc_crossval = cross_val_score(lsvc_med, X_train_selectmed, y_train, cv=fold_size)
forest_crossval = cross_val_score(forest_med, X_train_selectmed, y_train, cv=fold_size)
tree_crossval = cross_val_score(tree_med, X_train_selectmed, y_train, cv=fold_size)
sgd_crossval = cross_val_score(sgd_med, X_train_selectmed, y_train, cv=fold_size)
svc_crossval = cross_val_score(svc_med, X_train_selectmed, y_train, cv=fold_size)

performance_med.append(clf_crossval.mean())
performance_med.append(knn_crossval.mean())
performance_med.append(lsvc_crossval.mean())
performance_med.append(forest_crossval.mean())
performance_med.append(tree_crossval.mean())
performance_med.append(sgd_crossval.mean())
performance_med.append(svc_crossval.mean())

ax = plt.subplot(111)
ax.bar(learners, performance, width=0.2, color='b', align='center')
ax.bar(learners, performance_mean, width=0.2, color='g', align='center')
ax.bar(learners, performance_med, width=0.2, color='r', align='center')
plt.ylim(dum_crossval.mean(), 0.74)
plt.xticks(y_pos, learners)
plt.ylabel('Cross Val Accuracy')
plt.title('Default Accuracy for Various Models')
plt.legend()
plt.show()

for n, name in enumerate(learners):
    print(name, ":", performance[n])

'''Submit predictions'''
probability = pd.DataFrame(forest.predict_proba(X_test))

pred = pd.Series(probability[1])
sub_file.insert(1, "Pred", pred)

sub_file.to_csv(path_or_buf="submission_seedordinal.csv", index=False)
