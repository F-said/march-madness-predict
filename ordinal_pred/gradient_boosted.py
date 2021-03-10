import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import log_loss, accuracy_score
from sklearn.neural_network import MLPClassifier


def find_GB_params(x_train, y_train, x_test, y_test):
    """
    Find's the optimal parameters of the grandient boosted model using grid search. Very long. 

    @ postconditions: x_train has same column length as x_test
    @ returns: best node amount, best C-step, best feature classifier, best maximum depth, and log loss
    """
    n_est = list(range(100, 750, 50))
    C = [0.0001, 0.001, 0.01, 0.1, 1]
    max_feat = ['auto', 'sqrt']
    depth = [3, 4, 5, 6, 7, 8]

    gbdefault = GradientBoostingClassifier()
    gbdefault.fit(x_train, y_train)
    y_predict = pd.DataFrame(gbdefault.predict_proba(x_test)).drop(labels=0, axis=1)
    bestloss = log_loss(y_test, y_predict)

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
                    gb.fit(x_train, y_train)
                    y_pred = pd.DataFrame(gb.predict_proba(x_test)).drop(labels=0, axis=1)
                    loss = log_loss(y_test, y_pred)

                    if loss <= bestloss:
                        bestloss = loss
                        best_n = n
                        best_c = c
                        best_f = f
                        best_d = d

    return best_n, best_c, best_f, best_d, bestloss

def count_intersection(x_train, x_test) -> int:
    count = 0
    for index, row in x_test.iterrows():
        X_check = x_train[(x_train["Season"] == row["Season"])]
        if not (X_check[(((x_train["Team1"] == row["Team1"]) & (x_train["Team2"] == row["Team2"])) | ((x_train["Team2"] == row["Team1"]) & (x_train["Team1"] == row["Team2"])))].empty):
            count += 1
    return count 

# Begin model training 
year = "2021"

# pull training data 
X_train = pd.read_csv(year+"\\form_data\X_train_seedordinal.csv").\
    drop(labels="Team1", axis=1).drop(labels="Team2", axis=1)
y_train = pd.read_csv(year+"\\form_data\y_train_seedordinal.csv")
y_train = y_train["Result"]

# Remove test set results from train set to prevent look-ahead bias 
X_train = X_train[X_train["Season"] < 2019].drop(labels="Season", axis=1)
y_train = y_train[X_train["Season"] < 2019]

# Create test set 
X_test = X_train[X_train["Season"] == 2019].drop(labels="Season", axis=1)
y_test = y_train[X_train["Season"] == 2019]

# Replace with stage2 submission file when ready 
# submission2017 = pd.read_csv().drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).drop(labels="Season", axis=1)
sub_file = pd.read_csv(year + "\\unform_data\MSampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

# Make sure no test samples are in train set
try:
    count = count_intersection(X_train, X_test)
    if count > 0:
        raise ValueError(str(count) + " samples are shared amongst data-sets. Will produce biased values.")
except ValueError as e:
    exit(str(e))

# Gradient Boosted Trees Classifier
n, c, f, d, bestloss = find_GB_params(X_train_2017, y_train_2017, X_test_2017, y_test_2017)
print("Best number of estimators found:", n)
print("Best learning rate found:", c)
print("Best max_features found:", f)
print("Best depth found:", d)
print("log loss: ", bestloss)
# Best number of estimators found: 400
# Best learning rate found: 0.01
# Best max_features found: sqrt
# Best depth found: 3
# log loss:  0.532700137888
# Accuracy GB:  0.731343283582
gb = GradientBoostingClassifier(n_estimators=400, max_features='sqrt', max_depth=3, random_state=42, learning_rate=0.01)
gb.fit(X_train, y_train)
y_pred_2017 = pd.DataFrame(gb.predict_proba(sub_file)).drop(labels=0, axis=1)
y_pred = gb.predict(X_test)
print("Accuracy GB: ", accuracy_score(y_test, y_pred))

# Submit
sub_file.insert(1, "Pred", y_pred)
sub_file.to_csv(path_or_buf=year+"\\predictions\submission_seedordinal_gb.csv", index=False)