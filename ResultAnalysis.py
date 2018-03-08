import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, GradientBoostingClassifier
import numpy as np

X_train = pd.read_csv("X_train_seedordinal.csv")
y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

X_test = pd.read_csv("X_test_seedordinal.csv")

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"
sub_file = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

# Remove test set results from train set.
X_train_2014 = X_train[X_train["Season"] < 2014]
X_train_2015 = X_train[X_train["Season"] < 2015]
X_train_2016 = X_train[X_train["Season"] < 2016]
X_train_2017 = X_train[X_train["Season"] < 2017]

y_train_2014 = y_train[X_train["Season"] < 2014]
y_train_2015 = y_train[X_train["Season"] < 2015]
y_train_2016 = y_train[X_train["Season"] < 2016]
y_train_2017 = y_train[X_train["Season"] < 2017]

X_test_2014 = X_test[X_test["Season"] == 2014]
X_test_2015 = X_test[X_test["Season"] == 2015]
X_test_2016 = X_test[X_test["Season"] == 2016]
X_test_2017 = X_test[X_test["Season"] == 2017]


# Gradient Boosting for each individual year
gb = GradientBoostingClassifier(n_estimators=300, max_features='auto', max_depth=5, random_state=42, learning_rate=0.01)

gb.fit(X_train_2014, y_train_2014)
y_pred_2014 = pd.DataFrame(gb.predict_proba(X_test_2014))[1]

gb.fit(X_train_2015, y_train_2015)
y_pred_2015 = pd.DataFrame(gb.predict_proba(X_test_2015))[1]

gb.fit(X_train_2016, y_train_2016)
y_pred_2016 = pd.DataFrame(gb.predict_proba(X_test_2016))[1]

gb.fit(X_train_2017, y_train_2017)
y_pred_2017 = pd.DataFrame(gb.predict_proba(X_test_2017))[1]

# Submit
predictions1 = np.append(y_pred_2014, y_pred_2015)
predictions2 = np.append(y_pred_2016, y_pred_2017)
predictions = np.append(predictions1, predictions2)

y_pred = pd.Series(predictions)
sub_file.insert(1, "Pred", y_pred)
sub_file.to_csv(path_or_buf="submission_seedordinal_nobias.csv", index=False)

