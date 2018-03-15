import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import log_loss, accuracy_score
from sklearn.neural_network import MLPClassifier

X_train = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2018/X_train_seedordinal.csv").\
    drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).drop(labels="SeedDiff", axis=1)
y_train = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2018/y_train_seedordinal.csv")
y_train = y_train["Result"]

# Remove test set results from train set.
X_train_2016 = X_train[X_train["Season"] < 2016].drop(labels="Season", axis=1)
y_train_2016 = y_train[X_train["Season"] < 2016]

X_test_2016 = X_train[X_train["Season"] == 2016].drop(labels="Season", axis=1)
y_test_2016 = y_train[X_train["Season"] == 2016]

submission2016 = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2016/X_test_seedordinal_2016.csv").\
    drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).drop(labels="Season", axis=1).drop(labels="SeedDiff", axis=1)
submission2016_selected = pd.read_csv("/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2016/X_test_seedordinal_2016.csv")\
    .drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).drop(labels="Season", axis=1).drop(labels="WOLDiff", axis=1).\
    drop(labels="SAGDiff", axis=1).drop(labels="RPIDiff", axis=1).drop(labels="POMDiff", axis=1).drop(labels="MORDiff", axis=1).\
    drop(labels="DOLDiff", axis=1)

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2016/"
sub_file = pd.read_csv(path + "SampleSubmission2016.csv").drop(labels="Pred", axis=1)

# Gradient Boosted Trees Classifier
'''
n, c, f, d, bestloss = find_GB_params(X_train_2016, y_train_2016, X_test_2016, y_test_2016)
print("Best number of estimators found:", n)
print("Best learning rate found:", c)
print("Best max_features found:", f)
print("Best depth found:", d)
print("log loss: ", bestloss)
'''
# Best number of estimators found: 500
# Best learning rate found: 0.01
# Best max_features found: sqrt
# Best depth found: 3
# log loss:  0.532682820466
# Accuracy GB:  0.731343283582
gb = GradientBoostingClassifier(n_estimators=500, max_features='sqrt', max_depth=3, random_state=42, learning_rate=0.01)
gb.fit(X_train_2016, y_train_2016)
y_pred_2016 = pd.DataFrame(gb.predict_proba(submission2016)).drop(labels=0, axis=1)
y_pred = gb.predict(X_test_2016)
print("Accuracy GB: ", accuracy_score(y_test_2016, y_pred))

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
# Best alpha:  0.01
# Best learner:  adaptive
# log loss:  0.519840999951
# Accuracy NN:  0.716417910448
nn = MLPClassifier(hidden_layer_sizes=(400,), activation='logistic', solver='sgd', alpha=0.01, learning_rate='adaptive',
                   random_state=42)
nn.fit(X_train_2016, y_train_2016)
y_pred_2016_nn = pd.DataFrame(nn.predict_proba(submission2016)).drop(labels=0, axis=1)
y_pred_NN = nn.predict(X_test_2016)
print("Accuracy NN: ", accuracy_score(y_test_2016, y_pred_NN))

# Submit
sub_file.insert(1, "Pred", y_pred_2016_nn)
sub_file.to_csv(path_or_buf="submission_seedordinal_noseed2016_nn.csv", index=False)

sub_file = sub_file.drop(labels="Pred", axis=1)
sub_file.insert(1, "Pred", y_pred_2016)
sub_file.to_csv(path_or_buf="submission_seedordinal_noseed2016_gb.csv", index=False)

'''
Accuracies
Accuracy GB no seed:  0.716417910448
Accuracy NN no seed:  0.746268656716

Log Loss for 2016
GB: 0.588127
NN: 0.546141
'''