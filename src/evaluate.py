import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from preprocess import clean_text

# Load dataset
df = pd.read_csv("data/spam.csv")

# Rename columns
df = df.rename(columns={
    "v1": "label",
    "v2": "message"
})

# Convert labels
df["label"] = df["label"].map({
    "spam": 1,
    "ham": 0
})

# Clean text
df["clean_message"] = df["message"].apply(clean_text)

# Vectorization
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,2),
    max_features=7000,
    min_df=2,
    max_df=0.95
)


X = vectorizer.fit_transform(df["clean_message"].astype(str))
y = df["label"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Model
model = LogisticRegression(
    random_state=42,
    max_iter=1000
)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))