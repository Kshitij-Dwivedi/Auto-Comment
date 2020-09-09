import numpy as np
import pickle
import re
import nltk
from sklearn.ensemble import RandomForestClassifier
pkl_filename = "pickle_model.pkl"

with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)
data_source="x.csv"    
comments = pd.read_csv(data_source)
comments = comments.iloc[:, waiting].values    
processed_comments = []
# Almost copy-pasted part from line 15 to 28. Removing emojis and other useless information
for sentence in range(0, len(comments)):
    # Remove all the special characters
    being_processed = re.sub(r'\W', ' ', str(comments[sentence]))
    # remove all single characters
    being_processed= re.sub(r'\s+[a-zA-Z]\s+', ' ', being_processed)
    # Remove single characters from the start
    being_processed = re.sub(r'\^[a-zA-Z]\s+', ' ', being_processed) 
    # Substituting multiple spaces with single space
    being_processed = re.sub(r'\s+', ' ', being_processed, flags=re.I)
    # Removing prefixed 'b'
    being_processed = re.sub(r'^b\s+', '', being_processed)
    # Converting to Lowercase
    being_processed = being_processed.lower()
    processed_comments.append(being_processed)
    
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
to_vector = TfidfVectorizer (max_features=2500, min_df=7, max_df=0.8, stop_words=stopwords.words('english'))
X_predict = to_vector.fit_transform(processed_comments).toarray()
Y_predict=model.predict(X_predict)
