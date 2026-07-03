import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from src.history import get_all_predictions

rows=get_all_predictions()

print("\n=========DATABASE===========")

for row in rows:
    print(row)

