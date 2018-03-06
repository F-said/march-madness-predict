import pandas as pd
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

'''FOR SELECTING FEATURES'''

X_train = pd.read_csv("X_train_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)

y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

X_test = pd.read_csv("X_test_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)

# Use linear regression RFECV to select features
estimator = LogisticRegression()

selector = RFECV(estimator=estimator, cv=10, scoring='accuracy')
selector.fit(X_train, y_train)

print("Optimal number of features :", selector.n_features_)

plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross accuracy")
plt.plot(range(1, len(selector.grid_scores_) + 1), selector.grid_scores_)
plt.show()

X_train = pd.DataFrame(selector.transform(X_train))
X_test = pd.DataFrame(selector.transform(X_test))
X_train.to_csv(path_or_buf="X_train_seedordinal_selected.csv", index=False)
X_test.to_csv(path_or_buf="X_test_seedordinal_selected.csv", index=False)