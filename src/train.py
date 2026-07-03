import pickle
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

from preprocess import clean_text


# ==========================================
# LOAD DATASET
# ==========================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv("data/spam.csv")

df = df.rename(columns={
    "v1": "label",
    "v2": "message"
})

df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})

print(f"Dataset Shape : {df.shape}")

# ==========================================
# PREPROCESSING
# ==========================================

print("\nCleaning Messages...")

df["clean_message"] = df["message"].apply(clean_text)

# ==========================================
# FEATURE EXTRACTION
# ==========================================

print("Creating TF-IDF Features...")

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2),
    max_features=7000,
    min_df=2,
    sublinear_tf=True
)

X = vectorizer.fit_transform(df["clean_message"])

y = df["label"]

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================================
# MODELS TO COMPARE
# ==========================================

models = {
    "Naive Bayes": MultinomialNB(alpha=0.3),

    "Logistic Regression": LogisticRegression(
        random_state=42,
        max_iter=1000
    ),

    "Linear SVM": SVC(
        kernel="linear",
        probability=True,
        random_state=42
    )
}

best_model = None
best_name = ""
best_accuracy = 0

# ==========================================
# TRAIN & EVALUATE
# ==========================================

for name, model in models.items():

    print("\n")
    print("=" * 60)
    print(name)
    print("=" * 60)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print(f"\nAccuracy : {accuracy:.4f}")

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report")
    print(classification_report(y_test, y_pred))

    priority = {
        "Naive Bayes":1,
        "Logistic Regression":2,
        "Linear SVM":3
    }

    if (
        accuracy > best_accuracy or 
        (accuracy == best_accuracy and 
    priority[name] > priority[best_name])
    ):
        best_accuracy = accuracy
        best_model = model
        best_name = name

# ==========================================
# SAVE BEST MODEL
# ==========================================

print("\n")
print("=" * 60)
print("BEST MODEL")
print("=" * 60)

print(f"Model : {best_name}")
print(f"Accuracy : {best_accuracy:.4f}")

with open("models/spam_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("\nBest model saved successfully!")