from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import pandas as pd
from sklearn.calibration import CalibratedClassifierCV

'''For Model Selection'''
'''Suffering from look ahead bias as game results are already included in train set.'''
'''Creates overfit predictions that will be used to train 'no look ahead bias' model'''

X_train_selected = pd.read_csv("X_train_seedordinal_selected.csv")
X_train = pd.read_csv("X_train_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)

y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

X_test_selected = pd.read_csv("X_test_seedordinal_selected.csv")
X_test = pd.read_csv("X_test_seedordinal.csv").drop(labels="Season", axis=1).drop(labels="Team1", axis=1).\
    drop(labels="Team2", axis=1)

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"
sub_file = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

'''Learners'''
### Random Forest ###
forest = RandomForestClassifier(n_jobs=-1, n_estimators=500, criterion='gini', max_features='sqrt', max_depth=5,
                                random_state=42, oob_score=True)
forest.fit(X_train, y_train)

cal_forest = CalibratedClassifierCV(base_estimator=forest, cv='prefit')
cal_forest.fit(X_train, y_train)

### Gradient Boosting ###
gb = GradientBoostingClassifier(n_estimators=5000, max_features='sqrt', max_depth=5, random_state=42, learning_rate=0.01)
gb.fit(X_train, y_train)
y_pred = gb.predict(X_test)

'''Submit predictions and actual results for log loss function'''
results = pd.Series(y_pred)
sub_file_res = sub_file.copy()
sub_file_res.insert(1, "Results", results)
sub_file_res.to_csv(path_or_buf="results_seedordinal.csv", index=False)

probability = pd.DataFrame(gb.predict_proba(X_test))
pred = pd.Series(probability[1])
sub_file.insert(1, "Pred", pred)
sub_file.to_csv(path_or_buf="submission_seedordinal.csv", index=False)



