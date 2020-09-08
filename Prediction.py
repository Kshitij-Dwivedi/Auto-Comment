import pickle
from sklearn.ensemble import RandomForestClassifier
pkl_filename = "pickle_model.pkl"

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

Y_predict=pickle_model.predict(X_predict)
