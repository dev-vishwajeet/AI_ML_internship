
# Data Cleaning & Preprocessing


# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Create screenshots folder automatically
os.makedirs("screenshots", exist_ok=True)

# -----------------------------------------
# Load Dataset
# -----------------------------------------

df = pd.read_csv("dataset/Titanic-Dataset.csv")

print("Dataset Loaded Successfully!")

# -----------------------------------------
# First 5 Rows
# -----------------------------------------

print("\nFirst 5 Rows:\n")
print(df.head())

# -----------------------------------------
# Dataset Information
# -----------------------------------------

print("\nDataset Information:\n")
print(df.info())

# -----------------------------------------
# Check Missing Values
# -----------------------------------------

print("\nMissing Values:\n")
print(df.isnull().sum())

# -----------------------------------------
# Handle Missing Values
# -----------------------------------------

# Fill missing Age values with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing Embarked values with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin column
df.drop('Cabin', axis=1, inplace=True)

print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# -----------------------------------------
# Convert Categorical Data to Numerical
# -----------------------------------------

label_encoder = LabelEncoder()

df['Sex'] = label_encoder.fit_transform(df['Sex'])
df['Embarked'] = label_encoder.fit_transform(df['Embarked'])

print("\nEncoded Dataset:\n")
print(df.head())

# -----------------------------------------
# Feature Scaling
# -----------------------------------------

scaler = StandardScaler()

df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

print("\nScaled Features:\n")
print(df[['Age', 'Fare']].head())

# -----------------------------------------
# Boxplot for Outlier Detection
# -----------------------------------------

plt.figure(figsize=(8,5))

sns.boxplot(x=df['Fare'])

plt.title("Outlier Detection in Fare")

# Save graph
plt.savefig("screenshots/boxplot.png")

plt.show()

# -----------------------------------------
# Remove Outliers using IQR
# -----------------------------------------

Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['Fare'] >= lower_bound) & (df['Fare'] <= upper_bound)]

print("\nFinal Dataset Shape:")
print(df.shape)

# -----------------------------------------
# Save Cleaned Dataset
# -----------------------------------------

df.to_csv("cleaned_titanic.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")

print("\nTask 1 Completed Successfully!")