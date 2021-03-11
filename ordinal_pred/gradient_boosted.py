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