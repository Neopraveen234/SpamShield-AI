import pickle

with open("models/spam_model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model type:", type(model))
print("Model:", model)
print("Probability enabled:", model.probability)