import os
import subprocess

print("="*50)
print("TRAIN MODEL TEST")
print("="*50)

print("Running train.py...\n")

result=subprocess.run(
    ["python","src/train.py"],
    capture_output=True,
    text=True
)

print(result.stderr)

if result.stderr:
    print("ERROR:")
    print(result.stderr)

print("\nChecking model files...")

if os.path.exists("models/spam_model.pkl"):
    print("✅ spam_model.pkl exists")
else:
    print("✖️ spam_model.pkl NOT found")

if os.path.exists("models/vectorizer.pkl"):
    print("✔️ vectorizer.pkl exists")

else:
    print("❌ vectorizer.pkl NOT found")

print("="*50)
print("TRAIN MODEL TEST")
print("="*50)