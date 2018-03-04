from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, RandomizedSearchCV, GridSearchCV
from sklearn.feature_selection import SelectFromModel
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import preprocessing


def feature_importance(X, y, classifier):
    classifier.fit(X, y)

    # Assess feature importance
    importances = forest.feature_importances_
    indices = np.argsort(importances)[::-1]
    for f in range(X_train.shape[1]):
        print("%2d) %-*s %f" % (f + 1, 30, list(X)[indices[f]], importances[indices[f]]))


X_train = pd.read_csv("X_train_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)

y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

X_test = pd.read_csv("X_test_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"
sub_file = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

'''
Data Visualized to better understand features
feature_g = ["WOLDiff", "WLKDiff", "SAGDiff", "RPIDiff", "POMDiff", "MORDiff", "DOLDiff", "COLDiff", "SeedDiff"]
colors = ["Red", "Blue"]

for i, name in enumerate(feature_g):
    j = 1
    while j + 1 <= len(feature_g):
        if feature_g[i] is not feature_g[j]:
            plt.scatter(X_train[feature_g[i]], X_train[feature_g[j]], c=colors, alpha=.5, label=y_train)
            plt.xlabel(feature_g[i])
            plt.ylabel(feature_g[j])
            plt.legend(["Won", "Lost"])
            j += 1
            plt.show()
        else:
            j += 1
            
After looking at all possible two-dimensional datasets, I see that a clear classification is not possible with 2d
data 
'''

'''Dummy Classifier to get Baseline'''
dum = DummyClassifier(strategy="uniform")
dum.fit(X_train, y_train)
fold_size = 100
dum_crossval = cross_val_score(dum, X_train, y_train, cv=fold_size)

'''Learners'''
### Log Regression ###
clf = LogisticRegression(C=0.0001)

bag_log = BaggingClassifier(base_estimator=clf, n_estimators=50, n_jobs=-1, oob_score=True, random_state=42, verbose=2)
bag_log.fit(X_train, y_train)

### kNN classifier ###
knn = KNeighborsClassifier(algorithm='kd_tree', n_neighbors=50)

bag_knn = BaggingClassifier(base_estimator=knn, n_estimators=50, n_jobs=-1, oob_score=True, random_state=42, verbose=2)
bag_knn.fit(X_train, y_train)

### Random Forest ###
forest = RandomForestClassifier(criterion="entropy", n_estimators=150, n_jobs=-1, max_depth=5, oob_score=True,
                                max_features="auto", random_state=42, verbose=2)
print("Random Forest Feature Importance")
feature_importance(X_train, y_train, forest)

t = float(input("input thresh:"))

selection = SelectFromModel(estimator=forest, threshold=t)
selection.fit(X_train, y_train)
X_train_selected_forest = selection.transform(X_train)
X_test_selected_forest = selection.transform(X_test)

forest.fit(X_train_selected_forest, y_train)


'''KFold Cross-Validator'''
learners = ("LogReg", "kNN", "RandomF")
y_pos = np.arange(len(learners))
performance = []
performance_train = []

bag_log_crossval = cross_val_score(bag_log, X_train, y_train, cv=fold_size)
bag_knn_crossval = cross_val_score(bag_knn, X_train, y_train, cv=fold_size)
forest_crossval = cross_val_score(forest, X_train_selected_forest, y_train, cv=fold_size)

performance.append(bag_log_crossval.mean())
performance.append(bag_knn_crossval.mean())
performance.append(forest_crossval.mean())

performance_train.append(bag_log.score(X_train, y_train))
performance_train.append(bag_knn.score(X_train, y_train))
performance_train.append(forest.score(X_train_selected_forest, y_train))

for n, name in enumerate(learners):
    print(name, "train:", performance_train[n])
    print(name, "cv:", performance[n], "\n")

'''Submit predictions'''
probability = pd.DataFrame(bag_log.predict_proba(X_test))

pred = pd.Series(probability[1])
sub_file.insert(1, "Pred", pred)

sub_file.to_csv(path_or_buf="submission_seedordinal.csv", index=False)

