import pandas as pd
import matplotlib.pyplot as plt

print("Loading dataset...")
df = pd.read_csv('StudentsPerformance.csv')
print("Data loaded successfully!\n")

print("--- First 5 Rows of Data ---")
print(df.head())
print("\n")

df.columns = ['gender', 'race', 'parent_education', 'lunch', 'test_prep', 'math_score', 'reading_score', 'writing_score']


print("--- Quick Score Stats ---")
print(df[['math_score', 'reading_score', 'writing_score']].describe())




df.plot.scatter(x='math_score', y='reading_score', color='purple', alpha=0.5, title='Math vs. Reading Scores')
plt.show()


prep_scores = df.groupby('test_prep')['math_score'].mean()
prep_scores.plot.bar(color=['salmon', 'lightgreen'], title='Average Math Score: No Prep vs. Completed Prep')
plt.ylabel('Average Math Score')
plt.xticks(rotation=0) # Keeps the labels flat and readable
plt.show()


gender_counts = df['gender'].value_counts()
gender_counts.plot.pie(autopct='%1.1f%%', colors=['lightblue', 'pink'], title='Male vs. Female Students')
plt.ylabel('') # Hides the extra side label
plt.show()