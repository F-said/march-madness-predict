import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import log_loss, accuracy_score
from sklearn.neural_network import MLPClassifier


def find_GB_params(X17, y17, Xt17, yt17):
    # Find best hyperparameters of gradient boosted trees using cross validation

    n_est = list(range(100, 150, 5))
    C = [0.1]
    max_feat = ['sqrt']
    depth = [4]

    gbdefault = GradientBoostingClassifier()
    gbdefault.fit(X17, y17)
    y_predict = gbdefault.predict(Xt17)

    best2017 = accuracy_score(yt17, y_predict)
    loss = log_loss(yt17, gbdefault.predict_proba(Xt17))

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
                    y_predict = gb.predict(Xt17)
                    acc_2017 = accuracy_score(yt17, y_predict)

                    if acc_2017 >= best2017:
                        best2017 = acc_2017
                        loss = log_loss(yt17, gb.predict_proba(Xt17))

                        best_n = n
                        best_c = c
                        best_f = f
                        best_d = d

    return best_n, best_c, best_f, best_d, best2017, loss


def find_NN_params(X17, y17, Xt17, yt17):
    hidden_layersize = [(100,), (100, 2), (100, 3), (100,), (200, 2), (200, 3), (300,), (300, 2), (300, 3)]
    activation = ['identity', 'logistic', 'tanh', 'relu']
    solver = ['lbfgs', 'sgd', 'adam']
    alpha = [0.0001, 0.001, 0.01, 0.1]
    learnrate = ['constant', 'invscaling', 'adaptive']

    nndefault = MLPClassifier()
    nndefault.fit(X17, y17)
    y_predict = nndefault.predict(Xt17)

    best2017 = accuracy_score(yt17, y_predict)
    loss = log_loss(yt17, nndefault.predict_proba(Xt17))

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
                        y_predict = nn.predict(Xt17)
                        acc_2017 = accuracy_score(yt17, y_predict)

                        if acc_2017 >= best2017:
                            best2017 = acc_2017
                            loss = log_loss(yt17, gb.predict_proba(Xt17))

                            best_hidden = h
                            best_acti = a
                            best_solv = s
                            best_alpha = al
                            best_learn = l

    return best_hidden, best_acti, best_solv, best_alpha, best_learn, best2017, loss


X_train = pd.read_csv("X_train_seedordinal.csv")
y_train = pd.read_csv("y_train_seedordinal.csv")
y_train = y_train["Result"]

# Remove test set results from train set.
X_train_2017 = X_train[X_train["Season"] < 2017]
y_train_2017 = y_train[X_train["Season"] < 2017]

X_test_2017 = X_train[X_train["Season"] == 2017]
y_test_2017 = y_train[X_train["Season"] == 2017]

submission2017 = pd.read_csv("X_test_seedordinal_2017.csv")

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"
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
n, c, f, d, bestacc2017, loss = find_GB_params(X_train_2017, y_train_2017, X_test_2017, y_test_2017)
print("Best number of estimators found:", n)
print("Best learning rate found:", c)
print("Best max_features found:", f)
print("Best depth found:", d)
print("Best accuracy 2017: ", bestacc2017)
print("log loss: ", loss)
'''
# Best number of estimators found: 100
# Best learning rate found: 0.1
# Best max_features found: sqrt
# Best depth found: 4
# Best accuracy 2017:  0.761194029851
# log loss:  0.561643826124
gb = GradientBoostingClassifier(n_estimators=100, max_features='sqrt', max_depth=4, random_state=42, learning_rate=0.1)
gb.fit(X_train, y_train)
y_pred_2017 = pd.DataFrame(gb.predict_proba(submission2017)).drop(labels=0, axis=1)

# MLP Classifier
h, a, s, al, l, bestacc2017, nnloss = find_NN_params(X_train_2017, y_train_2017, X_test_2017, y_test_2017)
print("Best hidden layer: ", h)
print("Best activation: ", a)
print("Best solver: ", s)
print("Best alpha: ", al)
print("Best learner: ", l)
print("log loss: ", nnloss)
print("Score for nn is : ", bestacc2017)

nn = MLPClassifier(hidden_layer_sizes=h, activation=a, solver=s, alpha=al, learning_rate=l, random_state=42)
nn.fit(X_train_2017, y_train_2017)
nn_predict = nn.predict(X_test_2017)
y_pred_2017_nn = pd.DataFrame(nn.predict_proba(submission2017)).drop(labels=0, axis=1)

# Submit
sub_file.insert(1, "Pred", y_pred_2017)
sub_file.to_csv(path_or_buf="submission_seedordinal_nobias2017_nn.csv", index=False)

