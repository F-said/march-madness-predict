from sklearn.feature_selection import RFECV
import pandas as pd
from sklearn.linear_model import LogisticRegression

def select_feats(year: str, x_train, y_train) -> None: 
    """
    Selects the most significant features 
    @postcondition: generate a file containing 
    """
    clf = LogisticRegression(random_state=42, n_jobs=-1)

    selector = RFECV(clf, cv=5)
    selector.fit(x_train, y_train)

    X_train_selected = pd.DataFrame(selector.transform(x_train))
    X_train_selected.to_csv(path_or_buf=year + "\\form_data\X_train_seedordinal_selected.csv", index=False)