from sklearn.feature_selection import RFECV
import pandas as pd
from sklearn.linear_model import LogisticRegression

X_train = pd.read_csv("X_train_seedordinal.csv").drop(labels="Team1", axis=1).drop(labels="Team2", axis=1)\
    .drop(labels="Season", axis=1)
y_train = pd.read_csv("y_train_seedordinal.csv")

clf = LogisticRegression(random_state=42, n_jobs=-1)

selector = RFECV(clf, cv=5)
selector.fit(X_train, y_train)
X_train_selected = pd.DataFrame(selector.transform(X_train))

X_train_selected.to_csv(path_or_buf="X_train_seedordinal_selected.csv", index=False)

