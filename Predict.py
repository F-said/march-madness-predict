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


'''
def feature_importance(X, y, classifier):
    classifier.fit(X, y)

    # Assess feature importance
    importances = forest.feature_importances_
    indices = np.argsort(importances)[::-1]
    for f in range(X_train.shape[1]):
        print("%2d) %-*s %f" % (f + 1, 30, list(X)[indices[f]], importances[indices[f]]))
'''


X_train_feat9 = pd.read_csv("X_train_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)
X_train_feat8 = X_train_feat9.drop(labels="DOLDiff", axis=1)
X_train_feat7 = X_train_feat8.drop(labels="COLDiff", axis=1)
X_train_feat6 = X_train_feat7.drop(labels="RPIDiff", axis=1)
X_train_feat5 = X_train_feat6.drop(labels="SeedDiff", axis=1)
X_train_feat4 = X_train_feat5.drop(labels="WOLDiff", axis=1)
X_train_feat3 = X_train_feat4.drop(labels="MORDiff", axis=1)
X_train_feat2 = X_train_feat3.drop(labels="WLKDiff", axis=1)
X_train_feat1 = X_train_feat2.drop(labels="POMDiff", axis=1)

y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

X_test_feat9 = pd.read_csv("X_test_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)
X_test_feat8 = X_test_feat9.drop(labels="DOLDiff", axis=1)
X_test_feat7 = X_test_feat8.drop(labels="COLDiff", axis=1)
X_test_feat6 = X_test_feat7.drop(labels="RPIDiff", axis=1)
X_test_feat5 = X_test_feat6.drop(labels="SeedDiff", axis=1)
X_test_feat4 = X_test_feat5.drop(labels="WOLDiff", axis=1)
X_test_feat3 = X_test_feat4.drop(labels="MORDiff", axis=1)
X_test_feat2 = X_test_feat3.drop(labels="WLKDiff", axis=1)
X_test_feat1 = X_test_feat2.drop(labels="POMDiff", axis=1)

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
dum.fit(X_train_feat9, y_train)
fold_size = 100
dum_crossval = cross_val_score(dum, X_train_feat9, y_train, cv=fold_size)

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

### Random Forest ###
forest = RandomForestClassifier(criterion="entropy", n_estimators=50, n_jobs=-1, max_depth=5, oob_score=True,
                                max_features="auto", random_state=42, verbose=2)
forest.fit(X_train_feat7, y_train)

forest_crossval = cross_val_score(forest, X_train_feat7, y_train, cv=fold_size)

'''KFold Cross Val Accuracy
print("bag_log Feat 6 CV Score: ", bag_log_crossval.mean())
print("bag_knn Feat 5 CV Score: ", bag_knn_crossval.mean())
print("Forest Feat 7 CV Score: ", forest_crossval.mean())
'''

'''Submit predictions'''
probability = pd.DataFrame(forest.predict_proba(X_test_feat7))

pred = pd.Series(probability[1])
sub_file.insert(1, "Pred", pred)

sub_file.to_csv(path_or_buf="submission_seedordinal.csv", index=False)


