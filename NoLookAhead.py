import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
from sklearn.model_selection import cross_val_score


def find_GB_params(X14, y14, X15, y15, X16, y16, X17, y17):
    # Find best hyperparameters of gradient boosted trees using cross validation

    n_est = list(range(100, 700, 50))
    C = [0.001, 0.005, 0.01, 0.015, 0.02, 0.025]
    max_feat = ['auto', 'sqrt']
    depth = [3, 4, 5, 6, 7, 8]

    gbdefault = GradientBoostingClassifier()
    fold_size = 5

    gbdefault.fit(X14, y14)
    f1_2014 = cross_val_score(gbdefault, X14, y14, cv=fold_size, n_jobs=-1, scoring='f1').mean()

    gbdefault.fit(X15, y15)
    f1_2015 = cross_val_score(gbdefault, X15, y15, cv=fold_size, n_jobs=-1, scoring='f1').mean()

    gbdefault.fit(X16, y16)
    f1_2016 = cross_val_score(gbdefault, X16, y16, cv=fold_size, n_jobs=-1, scoring='f1').mean()

    gbdefault.fit(X17, y17)
    f1_2017 = cross_val_score(gbdefault, X17, y17, cv=fold_size, n_jobs=-1, scoring='f1').mean()

    best2014 = f1_2014
    best2015 = f1_2015
    best2016 = f1_2016
    best2017 = f1_2017

    best_n = 0
    best_c = 0
    best_f = ''
    best_d = 0

    for n in n_est:
        for c in C:
            for f in max_feat:
                for d in depth:
                    gb = GradientBoostingClassifier(n_estimators=n, learning_rate=c, max_features=f, max_depth=d,
                                                    random_state=42, verbose=2)
                    gb.fit(X14, y14)
                    f1_2014 = cross_val_score(gbdefault, X14, y14, cv=fold_size, n_jobs=-1, scoring='f1').mean()

                    gb.fit(X15, y15)
                    f1_2015 = cross_val_score(gbdefault, X15, y15, cv=fold_size, n_jobs=-1, scoring='f1').mean()

                    gb.fit(X16, y16)
                    f1_2016 = cross_val_score(gbdefault, X16, y16, cv=fold_size, n_jobs=-1, scoring='f1').mean()

                    gb.fit(X17, y17)
                    f1_2017 = cross_val_score(gbdefault, X17, y17, cv=fold_size, n_jobs=-1, scoring='f1').mean()

                    if f1_2014 >= best2014 and f1_2015 >= best2015 and f1_2016 >= best2016 and f1_2017 >= best2017:
                        best2014 = f1_2014
                        best2015 = f1_2015
                        best2016 = f1_2016
                        best2017 = f1_2017

                        best_n = n
                        best_c = c
                        best_f = f
                        best_d = d

    return best_n, best_c, best_f, best_d, best2014, best2015, best2016, best2017


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
'''
n, c, f, d, bestacc2014, bestacc2015, bestacc2016, bestacc2017 = find_GB_params(X_train_2014, y_train_2014,
                                                                                X_train_2015, y_train_2015,
                                                                                X_train_2016, y_train_2016,
                                                                                X_train_2017, y_train_2017)
print("Best number of estimators found:", n)
print("Best learning rate found:", c)
print("Best max_features found:", f)
print("Best depth found:", d)
print("Best accuracy found 2014: ", bestacc2014)
print("Best accuracy found 2015: ", bestacc2015)
print("Best accuracy found 2016: ", bestacc2016)
print("Best accuracy found 2017: ", bestacc2017)
'''
# Best number of estimators found: 650
# Best learning rate found: 0.025
# Best max_features found: sqrt
# Best depth found: 8
# Best accuracy found 2014:  0.662636118241
# Best accuracy found 2015:  0.678676998677
# Best accuracy found 2016:  0.692299657834
# Best accuracy found 2017:  0.65668215962
gb = GradientBoostingClassifier(n_estimators=200, max_features='sqrt', max_depth=7, random_state=42, learning_rate=0.025)

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

