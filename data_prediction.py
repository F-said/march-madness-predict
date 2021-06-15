import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import log_loss, accuracy_score
from sklearn.neural_network import MLPClassifier

from ordinal_pred import gradient_boosted as gb

# pull training data 
x = pd.read_csv("form_data\X_train_seedordinal.csv").drop(labels="SeedDiff", axis=1)
y = pd.read_csv("form_data\y_train_seedordinal.csv")
y = y["Result"]

# Remove test set results from train set to prevent look-ahead bias 
X_train = x[x["Season"] < 2019]
y_train = y[x["Season"] < 2019]

# Create test set 
X_test = x[x["Season"] == 2019]
y_test = y[x["Season"] == 2019]

# Replace with stage2 submission file when ready 
real_test = pd.read_csv("form_data\X_test_seedordinal.csv").drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).drop(labels="Season", axis=1).drop(labels="SeedDiff", axis=1)
sub_file = pd.read_csv("unform_data\MSampleSubmissionStage2.csv").drop(labels="Pred", axis=1)

# Make sure no test samples are in train set
try:
    count = gb.count_intersection(X_train, X_test)
    if count > 0:
        raise ValueError(str(count) + " samples are shared amongst data-sets. Will produce biased values.")
except ValueError as e:
    exit(str(e))

# Drop season column and teams once finished with comparison 
X_train = X_train.drop(labels="Season", axis=1).\
    drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).drop(labels="WOLDiff", axis=1)
X_test = X_test.drop(labels="Season", axis=1).\
    drop(labels="Team1", axis=1).drop(labels="Team2", axis=1).drop(labels="WOLDiff", axis=1)

print("test print")
# Gradient Boosted Trees Classifier
# n, c, f, d, bestloss = gb.find_GB_params(X_train, y_train, X_test, y_test)
# Accuracy GB:  0.7611940298507462
# Best number of estimators found: 600
# Best learning rate found: 0.01
# Best max_features found: sqrt
# Best depth found: 3
# log loss:  0.49584020630695835
gb = GradientBoostingClassifier(n_estimators=n, max_features=f, max_depth=d, random_state=42, learning_rate=c)
gb.fit(X_train, y_train)
y_pred = gb.predict(X_test)
print("Accuracy GB: ", accuracy_score(y_test, y_pred))

# Submit
y_pred = pd.DataFrame(gb.predict_proba(real_test)).drop(labels=0, axis=1)
sub_file.insert(1, "Pred", y_pred)
sub_file.to_csv(path_or_buf="predictions\submission_seedordinal_gb.csv", index=False)

'''
print("Best number of estimators found:", n)
print("Best learning rate found:", c)
print("Best max_features found:", f)
print("Best depth found:", d)
print("log loss: ", bestloss)
'''
