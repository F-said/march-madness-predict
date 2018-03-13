import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier

X_train = pd.read_csv("X_train_seedordinal.csv").drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).\
    drop(labels="Season", axis=1)
y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

X_train_selected = pd.read_csv("X_train_seedordinal_selected.csv")

submission2018 = pd.read_csv("X_test2018.csv").drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).\
    drop(labels="Season", axis=1)
submission2018_selected = pd.read_csv("X_test2018.csv").drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).\
    drop(labels="Season", axis=1).drop(labels="WOLDiff", axis=1).drop(labels="SAGDiff", axis=1).drop(labels="RPIDiff", axis=1).\
    drop(labels="POMDiff", axis=1).drop(labels="MORDiff", axis=1).drop(labels="DOLDiff", axis=1)

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2018/"
sub_file = pd.read_csv(path + "SampleSubmissionStage2.csv").drop(labels="Pred", axis=1)

# Gradient Boosted Trees Classifier
gb = GradientBoostingClassifier(n_estimators=400, max_features='sqrt', max_depth=3, learning_rate=0.01)
gb.fit(X_train, y_train)
y_pred = pd.DataFrame(gb.predict_proba(submission2018)).drop(labels=0, axis=1)

# Gradient Boosted Trees Classifier with selected features
gbselected = GradientBoostingClassifier(n_estimators=650, max_features='sqrt', max_depth=3, learning_rate=0.01)
gbselected.fit(X_train_selected, y_train)
y_pred_selected = pd.DataFrame(gbselected.predict_proba(submission2018_selected)).drop(labels=0, axis=1)

# MLP Classifier
nn = MLPClassifier(hidden_layer_sizes=(400,), activation='logistic', solver='sgd', alpha=1e-05, learning_rate='constant')
nn.fit(X_train, y_train)
y_pred_nn = pd.DataFrame(nn.predict_proba(submission2018)).drop(labels=0, axis=1)

# MLP Classifier with selected features
nnselected = MLPClassifier(hidden_layer_sizes=(400, 2), activation='logistic', solver='lbfgs', alpha=0.01,
                   learning_rate='adaptive')
nnselected.fit(X_train_selected, y_train)
y_pred_nnselected = pd.DataFrame(nnselected.predict_proba(submission2018_selected)).drop(labels=0, axis=1)

# Submit
sub_file.insert(1, "Pred", y_pred)
sub_file.to_csv(path_or_buf="submission2018gb.csv", index=False)

sub_file = sub_file.drop(labels="Pred", axis=1)
sub_file.insert(1, "Pred", y_pred_selected)
sub_file.to_csv(path_or_buf="submission2018gb_selected.csv", index=False)

sub_file = sub_file.drop(labels="Pred", axis=1)
sub_file.insert(1, "Pred", y_pred_nn)
sub_file.to_csv(path_or_buf="submission2018nn.csv", index=False)

sub_file = sub_file.drop(labels="Pred", axis=1)
sub_file.insert(1, "Pred", y_pred_nnselected)
sub_file.to_csv(path_or_buf="submission2018nn_selected.csv", index=False)

'''
Two models:
GB with Selected features
Neural Network with all features 
'''