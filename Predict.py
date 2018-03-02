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
from matplotlib.colors import ListedColormap
from sklearn.model_selection import RandomizedSearchCV
from sklearn import preprocessing

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
#logreg = LogisticRegression()
#log_param_grid = [{'C': [0.01, 0.1, 1], 'class_weight': ['balanced', None], 'penalty': ['l1', 'l2']}]
#clf = GridSearchCV(logreg, log_param_grid)
#clf.fit(X_train, y_train)

### kNN classifier ###
#nearest = KNeighborsClassifier()
#knn_param_grid = [{'n_neighbors': [2, 4, 6, 8], 'weights': ['uniform', 'distance'],
#                   'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']}]
#knn = GridSearchCV(nearest, knn_param_grid)
#knn.fit(X_train, y_train)

### Linear SVC ###
#linsvc = LinearSVC()
#lsvc_param_grid = [{'C': [0.01, 0.1, 1], 'class_weight': ['balanced', None]}]
#lsvc = GridSearchCV(linsvc, lsvc_param_grid)
#lsvc.fit(X_train, y_train)

### SVC ###
#Supportvc = SVC(probability=True)
#svc_param_grid = [{'C': [0.01, 0.1, 1], 'class_weight': ['balanced', None], 'kernel': ['rbf', 'linear', 'poly', 'sigmoid'
#                                                                                           'precomputed']}]
#svc = GridSearchCV(Supportvc, svc_param_grid)
#svc.fit(X_train, y_train)

### Random Forest ###
#randforest = RandomForestClassifier()
#forest_param_grid = {'criterion': ['entropy', 'gini'], 'n_estimators': [50, 100, 150, 200, 500],
#                     'max_depth': [3, 4, 5, 6, 7], 'max_features': ['auto', 'sqrt', 'log2', None]}
#forest = RandomizedSearchCV(randforest, forest_param_grid, cv=100)
#forest.fit(X_train, y_train)
#print(forest.get_params())

### Decision Tree ###
#dtree = DecisionTreeClassifier()
#tree_param_grid = [{'criterion': ['entropy', 'gini'], 'max_depth': [3, 4, 5, 6, 7,
#                   'max_features': ['auto', 'sqrt', 'log2', None]}]
#tree = GridSearchCV(dtree, tree_param_grid)
#tree.fit(X_train, y_train)

### SGD ###
#sgd = SGDClassifier(loss="log")
#sgd.fit(X_train, y_train)

'''KFold Cross-Validator'''
#learners = ("LogReg", "kNN", "L-SVC", "RandomF", "Tree", "SGD", "SVC")
#y_pos = np.arange(len(learners))
#performance = []
#clf_crossval = cross_val_score(clf, X_train, y_train, cv=fold_size)
#knn_crossval = cross_val_score(knn, X_train, y_train, cv=fold_size)
#lsvc_crossval = cross_val_score(lsvc, X_train, y_train, cv=fold_size)
#forest_crossval = cross_val_score(forest, X_train, y_train, cv=fold_size)
#tree_crossval = cross_val_score(tree, X_train, y_train, cv=fold_size)
#sgd_crossval = cross_val_score(sgd, X_train, y_train, cv=fold_size)
#svc_crossval = cross_val_score(svc, X_train, y_train, cv=fold_size)

#performance.append(clf_crossval.mean())
#performance.append(knn_crossval.mean())
#performance.append(lsvc_crossval.mean())
#performance.append(forest_crossval.mean())
#performance.append(tree_crossval.mean())
#performance.append(sgd_crossval.mean())
#performance.append(svc_crossval.mean())

#for n, name in enumerate(learners):
#    print(name, ":", performance[n])

'''Submit predictions'''
#probability = pd.DataFrame(forest.predict_proba(X_test))

#pred = pd.Series(probability[1])
#sub_file.insert(1, "Pred", pred)

#sub_file.to_csv(path_or_buf="submission_seedordinal.csv", index=False)

'''EVERYTHING WILL BE COMMENTED UNTIL I MAKE A PLAN'''
