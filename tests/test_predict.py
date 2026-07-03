#import sys
#import os
#sys.path.append(os.path.abspath(":"))
#sys.path.append("src")
#from predict import predict_message
from src.predict import predict_message

print("="*50)
print("PREDICT TEST")
print("="*50)

messages=[
    "Congratulations! You won a free iPhone.Claim now.",
    "Hi bro,let's meet at 5 pm.",
    "URGENT! Call this number to clain the prize.",
    "win ₹500000 cash now by clicking this link.",
    "Your OTP is 1234567",
    "Happy birthday have a wonderful day",
    "You have won the 1lakh prize amount in lottery."
]

for message in messages:
    result=predict_message(message)

    print("\nMessage:",message)

    print("Prediction:", result["prediction"])
    print("Spam : {results['spam_probability']:.2f}%")
    print("ham : {result['ham_probability']:.2f}%")

print("\nPrediction test completed successfully!")