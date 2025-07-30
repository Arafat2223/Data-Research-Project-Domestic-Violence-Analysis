
# Domestic Violence in Kazakhstan - Data Visualization Project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('domestic_violence_kazakhstan.csv')

# Basic data info
print("Dataset preview:")
print(df.head())
print("\nSummary:")
print(df.describe(include='all'))

# Plot: Total cases per year
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Year', palette='Blues')
plt.title('Number of Domestic Violence Cases Per Year')
plt.ylabel('Number of Cases')
plt.xlabel('Year')
plt.tight_layout()
plt.show()

# Plot: Cases by region
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Region', order=df['Region'].value_counts().index, palette='Greens')
plt.title('Cases by Region')
plt.xlabel('Number of Cases')
plt.ylabel('Region')
plt.tight_layout()
plt.show()

# Pie chart: Type of violence
violence_counts = df['Type_of_Violence'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(violence_counts, labels=violence_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Types of Violence')
plt.tight_layout()
plt.show()

# Bar chart: Reported vs Not Reported
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Reported', palette='Set2')
plt.title('Reported vs Not Reported Cases')
plt.xlabel('Reported')
plt.ylabel('Number of Cases')
plt.tight_layout()
plt.show()
