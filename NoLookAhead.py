import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import log_loss, accuracy_score
from sklearn.neural_network import MLPClassifier


def find_GB_params(X17, y17, Xt17, yt17):
    n_est = list(range(100, 750, 50))
    C = [0.0001, 0.001, 0.01, 0.1, 1]
    max_feat = ['auto', 'sqrt']
    depth = [3, 4, 5, 6, 7, 8]

    gbdefault = GradientBoostingClassifier()
    gbdefault.fit(X17, y17)
    y_predict = pd.DataFrame(gbdefault.predict_proba(Xt17)).drop(labels=0, axis=1)
    bestloss = log_loss(yt17, y_predict)

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
                    gb.fit(X17, y17)
                    y_pred = pd.DataFrame(gb.predict_proba(Xt17)).drop(labels=0, axis=1)
                    loss = log_loss(yt17, y_pred)

                    if loss <= bestloss:
                        bestloss = loss
                        best_n = n
                        best_c = c
                        best_f = f
                        best_d = d

    return best_n, best_c, best_f, best_d, bestloss


def find_NN_params(X17, y17, Xt17, yt17):
    hidden_layersize = [(100,), (100, 2), (100, 3), (100, 4), (200,), (200, 2), (200, 3), (200, 4), (300,), (300, 2),
                        (300, 3), (300, 4), (400,), (400, 2), (400, 3), (400, 4)]
    activation = ['logistic']
    solver = ['lbfgs', 'sgd', 'adam']
    alpha = [0.00001, 0.0001, 0.001, 0.01]
    learnrate = ['constant', 'invscaling', 'adaptive']

    nndefault = MLPClassifier()
    nndefault.fit(X17, y17)
    y_predict = pd.DataFrame(nndefault.predict_proba(Xt17)).drop(labels=0, axis=1)
    bestloss = log_loss(yt17, y_predict)

    best_hidden = (100,)
    best_acti = ''
    best_solv = ''
    best_alpha = 0
    best_learn = ''

    for h in hidden_layersize:
        for a in activation:
            for s in solver:
                for al in alpha:
                    for l in learnrate:
                        nn = MLPClassifier(hidden_layer_sizes=h, activation=a, solver=s, alpha=al, learning_rate=l,
                                           verbose=2)
                        nn.fit(X17, y17)
                        y_pred_NN = pd.DataFrame(nn.predict_proba(Xt17)).drop(labels=0, axis=1)

                        if y_pred_NN is not np.NaN:
                            loss = log_loss(yt17, y_pred_NN)

                            if loss <= bestloss:
                                bestloss = loss
                                best_hidden = h
                                best_acti = a
                                best_solv = s
                                best_alpha = al
                                best_learn = l

    return best_hidden, best_acti, best_solv, best_alpha, best_learn, bestloss


X_train = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2018/X_train_seedordinal.csv").\
    drop(labels="Team1", axis=1).drop(labels="Team2", axis=1)
y_train = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2018/y_train_seedordinal.csv")
y_train = y_train["Result"]

X_train_selected = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2018/X_train_seedordinal_selected.csv")

# Remove test set results from train set.
X_train_2017 = X_train[X_train["Season"] < 2017].drop(labels="Season", axis=1).drop(labels="COLDiff", axis=1)
X_train_2017_selected = X_train_selected[X_train["Season"] < 2017]
y_train_2017 = y_train[X_train["Season"] < 2017]

X_test_2017 = X_train[X_train["Season"] == 2017].drop(labels="Season", axis=1).drop(labels="COLDiff", axis=1)
X_test_2017_selected = X_train_selected[X_train["Season"] == 2017]
y_test_2017 = y_train[X_train["Season"] == 2017]


submission2017 = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2017/X_test_seedordinal_2017.csv").drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).\
    drop(labels="Season", axis=1).drop(labels="COLDiff", axis=1)
submission2017_selected = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2017/X_test_seedordinal_2017.csv").drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).\
    drop(labels="Season", axis=1).drop(labels="WOLDiff", axis=1).drop(labels="SAGDiff", axis=1).drop(labels="RPIDiff", axis=1).\
    drop(labels="POMDiff", axis=1).drop(labels="MORDiff", axis=1).drop(labels="DOLDiff", axis=1)

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2017/"
sub_file = pd.read_csv(path + "SampleSubmission2017.csv").drop(labels="Pred", axis=1)

# Make sure no test samples are in train set
'''
count = 0
for index, row in X_test_2017.iterrows():
    X_check = X_train_2017[(X_train_2017["Season"] == row["Season"])]
    if not (X_check[(((X_train_2017["Team1"] == row["Team1"]) & (X_train_2017["Team2"] == row["Team2"])) |
                     ((X_train_2017["Team2"] == row["Team1"]) & (X_train_2017["Team1"] == row["Team2"])))].empty):
        count += 1
print("Number of test samples in train samples:", count)
# Number of shared samples: 0 
'''

# Gradient Boosted Trees Classifier
'''
n, c, f, d, bestloss = find_GB_params(X_train_2017, y_train_2017, X_test_2017, y_test_2017)
print("Best number of estimators found:", n)
print("Best learning rate found:", c)
print("Best max_features found:", f)
print("Best depth found:", d)
print("log loss: ", bestloss)
'''
# Best number of estimators found: 400
# Best learning rate found: 0.01
# Best max_features found: sqrt
# Best depth found: 3
# log loss:  0.536202519508
# Accuracy GB:  0.731343283582
gb = GradientBoostingClassifier(n_estimators=400, max_features='sqrt', max_depth=3, random_state=42, learning_rate=0.01)
gb.fit(X_train_2017, y_train_2017)
y_pred_2017 = pd.DataFrame(gb.predict_proba(submission2017)).drop(labels=0, axis=1)
y_pred = gb.predict(X_test_2017)
print("Accuracy GB: ", accuracy_score(y_test_2017, y_pred))

# Gradient Boosted Trees Classifier with selected features
# 2017 Log loss 0.499839
# 2017 Log Loss 0.570161
'''
n, c, f, d, bestloss = find_GB_params(X_train_2017_selected, y_train_2017, X_test_2017_selected, y_test_2017)
print("Best number of estimators found:", n)
print("Best learning rate found:", c)
print("Best max_features found:", f)
print("Best depth found:", d)
print("log loss: ", bestloss)
'''
# Best number of estimators found: 650
# Best learning rate found: 0.01
# Best max_features found: sqrt
# Best depth found: 3
# log loss:  0.529722770014
# Accuracy GB:  0.731343283582
gbselected = GradientBoostingClassifier(n_estimators=650, max_features='sqrt', max_depth=3, random_state=42, learning_rate=0.01)
gbselected.fit(X_train_2017_selected, y_train_2017)
y_pred_2017_selected = pd.DataFrame(gbselected.predict_proba(submission2017_selected)).drop(labels=0, axis=1)
y_pred_selected = gbselected.predict(X_test_2017_selected)
print("Accuracy GB Selected: ", accuracy_score(y_test_2017, y_pred_selected))

# MLP Classifier
# 2017 Log Loss 0.550211
# 2017 Log Loss 0.546570
'''
h, a, s, al, l, nnloss = find_NN_params(X_train_2017, y_train_2017, X_test_2017, y_test_2017)
print("Best hidden layer: ", h)
print("Best activation: ", a)
print("Best solver: ", s)
print("Best alpha: ", al)
print("Best learner: ", l)
print("log loss: ", nnloss)
'''
# Best hidden layer:  (400,)
# Best activation:  logistic
# Best solver:  sgd
# Best alpha:  1e-05
# Best learner:  constant
# log loss:  0.532383554317
# Accuracy NN:  0.716417910448
nn = MLPClassifier(hidden_layer_sizes=(400,), activation='logistic', solver='sgd', alpha=1e-05, learning_rate='constant',
                   random_state=42)
nn.fit(X_train_2017, y_train_2017)
y_pred_2017_nn = pd.DataFrame(nn.predict_proba(submission2017)).drop(labels=0, axis=1)
y_pred_NN = nn.predict(X_test_2017)
print("Accuracy NN: ", accuracy_score(y_test_2017, y_pred_NN))

# MLP Classifier with selected features
'''
h, a, s, al, l, nnloss = find_NN_params(X_train_2017_selected, y_train_2017, X_test_2017_selected, y_test_2017)
print("Best hidden layer: ", h)
print("Best activation: ", a)
print("Best solver: ", s)
print("Best alpha: ", al)
print("Best learner: ", l)
print("log loss: ", nnloss)
'''
# Best hidden layer:  (400, 2)
# Best activation:  logistic
# Best solver:  lbfgs
# Best alpha:  0.01
# Best learner:  adaptive
# log loss:  0.517196819861
nnselected = MLPClassifier(hidden_layer_sizes=(400, 2), activation='logistic', solver='lbfgs', alpha=0.01,
                           learning_rate='adaptive', random_state=42)
nnselected.fit(X_train_2017_selected, y_train_2017)
y_pred_2017_nn_selected = pd.DataFrame(nnselected.predict_proba(submission2017_selected)).drop(labels=0, axis=1)
y_pred_NN_selected = nnselected.predict(X_test_2017_selected)
print("Accuracy NN Selected: ", accuracy_score(y_test_2017, y_pred_NN_selected))

# Submit
sub_file.insert(1, "Pred", y_pred_2017_nn)
sub_file.to_csv(path_or_buf="submission_seedordinal_nobias2017_nn.csv", index=False)

sub_file = sub_file.drop(labels="Pred", axis=1)
sub_file.insert(1, "Pred", y_pred_2017)
sub_file.to_csv(path_or_buf="submission_seedordinal_nobias2017_gb.csv", index=False)

sub_file = sub_file.drop(labels="Pred", axis=1)
sub_file.insert(1, "Pred", y_pred_2017_nn_selected)
sub_file.to_csv(path_or_buf="submission_seedordinal_nobias2017_nnselected.csv", index=False)

sub_file = sub_file.drop(labels="Pred", axis=1)
sub_file.insert(1, "Pred", y_pred_2017_selected)
sub_file.to_csv(path_or_buf="submission_seedordinal_nobias2017_gbselected.csv", index=False)

