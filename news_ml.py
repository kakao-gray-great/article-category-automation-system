import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer

df = pd.read_csv("./news.tsv", delimiter="\t")
print(df.head(2))

df['content'] = df['content'].str.replace('[^ ㄱ-ㅣ가-힣-a-zA-Z]+', '', regex=True)
print(df.head(100))

df = df.fillna(' ')

train_set = df
X = train_set['content']
print(X)

le = LabelEncoder()
Y = le.fit_transform(train_set['category'])
print(Y)

print(le.classes_)