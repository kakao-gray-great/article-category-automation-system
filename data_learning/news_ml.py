import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer

df = pd.read_csv("./news.tsv", delimiter="\t")
# print(df.head(2))

df['content'] = df['content'].str.replace('[^ ㄱ-ㅣ가-힣-a-zA-Z]+', '', regex=True)
# print(df.head(100))

df = df.fillna(' ')

train_set = df
X = train_set['content']
# print(X)
 
le = LabelEncoder()
y = le.fit_transform(train_set['category'])
# print(y)

# print(le.classes_)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41, shuffle=True)

clf = Pipeline([('vert', TfidfVectorizer()), ('clf', MultinomialNB())])

model = clf.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))

MODEL_NAME = 'model.pkl'

import pickle
pickle.dump(model, open(MODEL_NAME, 'wb'))

loaded_model = pickle.load(open(MODEL_NAME, 'rb'))

pred = loaded_model.predict(X_test)
print(classification_report(y_test, pred))