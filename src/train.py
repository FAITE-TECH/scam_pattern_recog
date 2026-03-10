import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from src.preprocess import clean_text

df = pd.read_csv("../dataset/spam.csv", encoding="latin-1")

df = df[["v1","v2"]]
df.columns = ["label","text"]

df["label"] = df["label"].map({"ham":0, "spam":1})

df["clean"] = df["text"].astype(str).apply(clean_text)

vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["clean"])
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open("../models/model.pkl","wb"))
pickle.dump(vectorizer, open("../models/vectorizer.pkl","wb"))

print("Model trained and saved")