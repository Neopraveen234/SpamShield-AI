import pickle

from src.preprocess import clean_text

# Load trained model
with open("models/spam_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def predict_message(text):
    """
    Predict whether a message is Spam or Ham.

    Returns:
    {
        "prediction": "spam" or "ham",
        "spam_probability": float,
        "ham_probability": float
    }
    """

    # Clean input text
    cleaned_text = clean_text(text)

    # Convert text into vector
    text_vector = vectorizer.transform([cleaned_text])

    # Predict class
    prediction = model.predict(text_vector)[0]

    # Prediction probabilities
    probability = model.predict_proba(text_vector)[0]

    return {
        "prediction": "spam" if prediction == 1 else "ham",
        "spam_probability": probability[1] * 100,
        "ham_probability": probability[0] * 100
    }