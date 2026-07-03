import pandas as pd

print("="*50)
print("DATASET TEST")
print("="*50)

#LOAD DATASET
df=pd.read_csv("data/spam.csv")

#Basic Information
print(f"Dataset Shape   : {df.shape}")
print(f"Columns    : {list(df.columns)}")

#Missing values
print("\nMissing Values:")
print(df.isnull().sum())

#Duplicate values
duplicates=df.duplicated().sum()
print(f"\nDuplicate Rows    : {duplicates}")

#Class distribution
print("\nClass Distribution:")
print(df['v1'].value_counts())

print("\nDataset successfully.")
print("="*50)