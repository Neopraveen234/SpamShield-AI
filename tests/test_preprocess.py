import sys
from pathlib import Path

#Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.preprocess import clean_text
print("="*50)
print("DATASET TEST")
print("="*50)

test_messages=[
    "HellonWorld!!",
    "FREE MONEY!!!",
    "Congratunations!!!",
    "https://google.com",
    "Hello!!!$$$ WIN NOW!!!",
    "Python is Awesome!!!",
    "1234567890",
    "Hi!!! How are you???",
]

for msg in test_messages:
    print(f"\nOriginal : {msg}")
    print(f"Cleaned : {clean_text(msg)}")



print("\nPreprecessing test completed succesfullly.")
