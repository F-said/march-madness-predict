import pandas as pd
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FactorAnalysis

'''FOR SELECTING FEATURES'''

X_train = pd.read_csv("X_train_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)

y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

X_test = pd.read_csv("X_test_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)

# Use PCA to reduce features
pca = PCA()
pca.fit(X_train, y_train)

X_train_pca = pd.DataFrame(pca.transform(X_train))
X_test_pca = pd.DataFrame(pca.transform(X_test))

X_train_pca.to_csv(path_or_buf="X_train_seedordinal_pca.csv", index=False)
X_test_pca.to_csv(path_or_buf="X_test_seedordinal_pca.csv", index=False)

# Use linear regression RFECV to select features
estimator = LogisticRegression()

selector = RFECV(estimator=estimator, cv=100, scoring='accuracy')
selector.fit(X_train, y_train)

print("Optimal number of features :", selector.n_features_)
print(selector.ranking_)

plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross accuracy")
plt.plot(range(1, len(selector.grid_scores_) + 1), selector.grid_scores_)
plt.show()

X_train_sel = pd.DataFrame(selector.transform(X_train))
X_test_sel = pd.DataFrame(selector.transform(X_test))

X_train_sel.to_csv(path_or_buf="X_train_seedordinal_selected.csv", index=False)
X_test_sel.to_csv(path_or_buf="X_test_seedordinal_selected.csv", index=False)