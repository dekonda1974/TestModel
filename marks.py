import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import marks

from sklearn.linear_model import LinearRegression


def marks_prediction(enter_value):
    X = pd.read_csv("x_data_train.csv")
    Y = pd.read_csv("y_data_train.csv")
    

    X = X.values
    Y = Y.values


    model = LinearRegression()
    model.fit(X,Y)

    #X = np.array(ct.fit_transform(X), dtype=np.float64)


    X_test = np.array(enter_value, dtype=np.float64)
    X_test = X_test.reshape((1,-1))

    return model.predict(X_test)[0]
