import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
pkl_filename = "pickle_model.pkl"

df = pd.read_csv("./comments.csv")
print(df)

X_predict = list(df["0"])
print(X_predict)

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

Y_predict=pickle_model.predict(X_predict)
