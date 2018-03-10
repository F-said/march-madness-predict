import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import numpy as np
from sklearn.calibration import CalibratedClassifierCV


def find_GB_params(X14, y14, X15, y15, X16, y16, X17, y17):
    # 760 calculations of GB
    # This is going to take disgustingly long
    # Use mean difference on predictions with 0.33 log loss to find best hyperparameters of gradient boosted trees
    y_close = pd.read_csv("submission_seedordinal_logloss33.csv")
    y_close = y_close["Pred"]

    n_est = list(range(100, 1000, 50))
    C = [0.0001, 0.001, 0.01, 0.1]
    max_feat = ['sqrt', 'auto']
    depth = list(range(3, 8))

    min = 1
    best_n = 0
    best_c = 0
    best_f = ''
    best_d = 0

    for n in n_est:
        for c in C:
            for f in max_feat:
                for d in depth:
                    gb = GradientBoostingClassifier(n_estimators=n, learning_rate=c, max_features=f, max_depth=d, random_state=42)

                    gb.fit(X14, y14)
                    y_2014 = pd.DataFrame(gb.predict_proba(X14))[1]

                    gb.fit(X15, y15)
                    y_2015 = pd.DataFrame(gb.predict_proba(X15))[1]

                    gb.fit(X16, y16)
                    y_2016 = pd.DataFrame(gb.predict_proba(X16))[1]

                    gb.fit(X17, y17)
                    y_2017 = pd.DataFrame(gb.predict_proba(X17))[1]

                    predi = np.append(y_2014, y_2015)
                    ctions = np.append(y_2016, y_2017)
                    concat_pred = np.append(predi, ctions)
                    full_predict = pd.Series(concat_pred)

                    meandiff = abs((y_close.subtract(full_predict)).mean())
                    if meandiff < min:
                        min = meandiff
                        best_n = n
                        best_c = c
                        best_f = f
                        best_d = d

    return best_n, best_c, best_f, best_d


X_train = pd.read_csv("X_train_seedordinal.csv")
y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

X_test = pd.read_csv("X_test_seedordinal.csv")

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"
sub_file = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

'''
# How many test set examples are in the training set?
count = 0
X_train_lookahead = X_train[X_train["Season"] >= 2014]
X_test_lookahead = X_test[X_test["Season"] >= 2014]

for index, row in X_test_lookahead.iterrows():
    X_check = X_train_lookahead[(X_train_lookahead["Season"] == row["Season"])]
    if not (X_check[(((X_train_lookahead["Team1"] == row["Team1"]) & (X_train_lookahead["Team2"] == row["Team2"])) |
                     ((X_train_lookahead["Team2"] == row["Team1"]) & (X_train_lookahead["Team1"] == row["Team2"])))].empty):
        count += 1

print("Number of test samples in train samples:", count)
# 268 Samples are shared between test set and train set 
'''

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
n, c, f, d = find_GB_params(X_train_2014, y_train_2014, X_train_2015, y_train_2015, X_train_2016, y_train_2016, X_train_2017, y_train_2017)
gb = GradientBoostingClassifier(n_estimators=n, max_features=f, max_depth=d, random_state=42, learning_rate=c)

gb.fit(X_train_2014, y_train_2014)
y_pred_2014 = pd.DataFrame(gb.predict_proba(X_test_2014))[1]

gb.fit(X_train_2015, y_train_2015)
y_pred_2015 = pd.DataFrame(gb.predict_proba(X_test_2015))[1]

gb.fit(X_train_2016, y_train_2016)
y_pred_2016 = pd.DataFrame(gb.predict_proba(X_test_2016))[1]

gb.fit(X_train_2017, y_train_2017)
y_pred_2017 = pd.DataFrame(gb.predict_proba(X_test_2017))[1]

# Random Forest for each individual year
forest = RandomForestClassifier(n_jobs=-1, n_estimators=250, criterion='gini', max_features='sqrt', max_depth=5,
                                random_state=42, oob_score=True)
cal_forest = CalibratedClassifierCV(base_estimator=forest)
cal_forest.fit(X_train, y_train)

cal_forest.fit(X_train_2014, y_train_2014)
y_pred_2014_forest = pd.DataFrame(cal_forest.predict_proba(X_test_2014))[1]

cal_forest.fit(X_train_2015, y_train_2015)
y_pred_2015_forest = pd.DataFrame(cal_forest.predict_proba(X_test_2015))[1]

cal_forest.fit(X_train_2016, y_train_2016)
y_pred_2016_forest = pd.DataFrame(cal_forest.predict_proba(X_test_2016))[1]

cal_forest.fit(X_train_2017, y_train_2017)
y_pred_2017_forest = pd.DataFrame(cal_forest.predict_proba(X_test_2017))[1]

# Submit
predictions1 = np.append(y_pred_2014, y_pred_2015)
predictions2 = np.append(y_pred_2016, y_pred_2017)
predictions = np.append(predictions1, predictions2)
y_pred = pd.Series(predictions)

sub_file.insert(1, "Pred", y_pred)
sub_file.to_csv(path_or_buf="submission_seedordinal_nobias.csv", index=False)

