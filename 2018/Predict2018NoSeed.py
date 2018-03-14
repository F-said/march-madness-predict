import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier

X_train = pd.read_csv("X_train_seedordinal.csv").drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).\
    drop(labels="Season", axis=1).drop(labels="SeedDiff", axis=1)
y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

submission2018 = pd.read_csv("X_test2018.csv").drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).\
    drop(labels="Season", axis=1).drop(labels="SeedDiff", axis=1)

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/2018/"
sub_file = pd.read_csv(path + "SampleSubmissionStage2.csv").drop(labels="Pred", axis=1)

# Gradient Boosted Trees Classifier
gb = GradientBoostingClassifier(n_estimators=500, max_features='sqrt', max_depth=3, learning_rate=0.01)
gb.fit(X_train, y_train)
y_pred = pd.DataFrame(gb.predict_proba(submission2018)).drop(labels=0, axis=1)

# MLP Classifier
nn = MLPClassifier(hidden_layer_sizes=(400,), activation='logistic', solver='sgd', alpha=0.01, learning_rate='adaptive')
nn.fit(X_train, y_train)
y_pred_nn = pd.DataFrame(nn.predict_proba(submission2018)).drop(labels=0, axis=1)

# Submit
sub_file.insert(1, "Pred", y_pred)
sub_file.to_csv(path_or_buf="submission2018gb_noseed.csv", index=False)

sub_file = sub_file.drop(labels="Pred", axis=1)
sub_file.insert(1, "Pred", y_pred_nn)
sub_file.to_csv(path_or_buf="submission2018nn_noseed.csv", index=False)

'''
Two models:
GB with all features except seed
Neural Network with all features except seed 
'''