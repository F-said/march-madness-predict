import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import log_loss, accuracy_score
from sklearn.neural_network import MLPClassifier

X_train = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2018/X_train_seedordinal.csv").\
    drop(labels="Team1", axis=1).drop(labels="Team2", axis=1)
y_train = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2018/y_train_seedordinal.csv")
y_train = y_train["Result"]

X_train_selected = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2017/X_train_seedordinal_selected.csv")

# Remove test set results from train set.
X_train_2016 = X_train[X_train["Season"] < 2016].drop(labels="Season", axis=1)
X_train_2016_selected = X_train_selected[X_train["Season"] < 2016]
y_train_2016 = y_train[X_train["Season"] < 2016]

X_test_2016 = X_train[X_train["Season"] == 2016].drop(labels="Season", axis=1)
X_test_2016_selected = X_train_selected[X_train["Season"] == 2016]
y_test_2016 = y_train[X_train["Season"] == 2016]

submission2016 = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2016/X_test_seedordinal_2016.csv").\
    drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).drop(labels="Season", axis=1)
submission2016_selected = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2016/X_test_seedordinal_2016.csv")\
    .drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).drop(labels="Season", axis=1).drop(labels="WOLDiff", axis=1).\
    drop(labels="SAGDiff", axis=1).drop(labels="RPIDiff", axis=1).drop(labels="POMDiff", axis=1).drop(labels="MORDiff", axis=1).\
    drop(labels="DOLDiff", axis=1)

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2016/"
sub_file = pd.read_csv(path + "SampleSubmission2016.csv").drop(labels="Pred", axis=1)

# Make sure no test samples are in train set
'''
count = 0
for index, row in X_test_2016.iterrows():
    X_check = X_train_2016[(X_train_2016["Season"] == row["Season"])]
    if not (X_check[(((X_train_2016["Team1"] == row["Team1"]) & (X_train_2016["Team2"] == row["Team2"])) |
                     ((X_train_2016["Team2"] == row["Team1"]) & (X_train_2016["Team1"] == row["Team2"])))].empty):
        count += 1
print("Number of test samples in train samples:", count)
# Number of shared samples: 0 
'''

# Gradient Boosted Trees Classifier
'''
n, c, f, d, bestloss = find_GB_params(X_train_2016, y_train_2016, X_test_2016, y_test_2016)
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
# log loss:  0.532700137888
# Accuracy GB:  0.731343283582
gb = GradientBoostingClassifier(n_estimators=400, max_features='sqrt', max_depth=3, random_state=42, learning_rate=0.01)
gb.fit(X_train_2016, y_train_2016)
y_pred_2016 = pd.DataFrame(gb.predict_proba(submission2016)).drop(labels=0, axis=1)
y_pred = gb.predict(X_test_2016)
print("Accuracy GB: ", accuracy_score(y_test_2016, y_pred))

# Gradient Boosted Trees Classifier with selected features
'''
n, c, f, d, bestloss = find_GB_params(X_train_2016_selected, y_train_2016, X_test_2016_selected, y_test_2016)
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
gbselected.fit(X_train_2016_selected, y_train_2016)
y_pred_2016_selected = pd.DataFrame(gbselected.predict_proba(submission2016_selected)).drop(labels=0, axis=1)
y_pred_selected = gbselected.predict(X_test_2016_selected)
print("Accuracy GB Selected: ", accuracy_score(y_test_2016, y_pred_selected))

# MLP Classifier
'''
h, a, s, al, l, nnloss = find_NN_params(X_train_2016, y_train_2016, X_test_2016, y_test_2016)
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
nn.fit(X_train_2016, y_train_2016)
y_pred_2016_nn = pd.DataFrame(nn.predict_proba(submission2016)).drop(labels=0, axis=1)
y_pred_NN = nn.predict(X_test_2016)
print("Accuracy NN: ", accuracy_score(y_test_2016, y_pred_NN))

# MLP Classifier with selected features
'''
h, a, s, al, l, nnloss = find_NN_params(X_train_2016_selected, y_train_2016, X_test_2016_selected, y_test_2016)
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
# Accuracy NN Selected:  0.671641791045
nnselected = MLPClassifier(hidden_layer_sizes=(400, 2), activation='logistic', solver='lbfgs', alpha=0.01,
                           learning_rate='adaptive', random_state=42)
nnselected.fit(X_train_2016_selected, y_train_2016)
y_pred_2016_nn_selected = pd.DataFrame(nnselected.predict_proba(submission2016_selected)).drop(labels=0, axis=1)
y_pred_NN_selected = nnselected.predict(X_test_2016_selected)
print("Accuracy NN Selected: ", accuracy_score(y_test_2016, y_pred_NN_selected))

# Submit
sub_file.insert(1, "Pred", y_pred_2016_nn)
sub_file.to_csv(path_or_buf="submission_seedordinal_nobias2016_nn.csv", index=False)

sub_file = sub_file.drop(labels="Pred", axis=1)
sub_file.insert(1, "Pred", y_pred_2016)
sub_file.to_csv(path_or_buf="submission_seedordinal_nobias2016_gb.csv", index=False)

sub_file = sub_file.drop(labels="Pred", axis=1)
sub_file.insert(1, "Pred", y_pred_2016_nn_selected)
sub_file.to_csv(path_or_buf="submission_seedordinal_nobias2016_nnselected.csv", index=False)

sub_file = sub_file.drop(labels="Pred", axis=1)
sub_file.insert(1, "Pred", y_pred_2016_selected)
sub_file.to_csv(path_or_buf="submission_seedordinal_nobias2016_gbselected.csv", index=False)

'''
Accuracies
Accuracy GB:  0.671641791045
Accuracy GB Selected:  0.686567164179
Accuracy NN:  0.731343283582
Accuracy NN Selected:  0.761194029851

Log Loss for 2016
GB: 0.590293
GB Selected: 0.570161
NN: 0.546570
NN Selected: 0.649092
'''