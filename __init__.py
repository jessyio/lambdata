#lambdata: a collection of data science helper functions

import pandas as pd
import numpy as np

TEST = pd.DataFrame(np.ones(10))

#Check a dataframe for nulls, drop them
def df_cleaner(df):
    #clean a DataFrame
    print(df.info())
    df = df.dropna()
    pass #TODO -implement

#Train/validate 20/80 random split function for a dataframe
def train_val(df):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_val, y_train, y_val

#Report a confusion matrix, with labels for easier interpretation
#def confusion_matrix(df):
