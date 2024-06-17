import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('merged_dataset2_updated.csv')

# Extract relevant columns
df = df[['Country', 'Logged GDP per capita', 'Social support']]

# Convert to numeric, handling errors if any
df['Logged GDP per capita'] = pd.to_numeric(df['Logged GDP per capita'], errors='coerce')
df['Social support'] = pd.to_numeric(df['Social support'], errors='coerce')

# Drop rows with missing values
df = df.dropna()

# Plotting using seaborn (scatter plot with regression line)
plt.figure(figsize=(10, 6))
sns.regplot(x='Logged GDP per capita', y='Social support', data=df, scatter_kws={'alpha':0.5})
plt.title('Relationship between Logged GDP per capita and Social support')
plt.xlabel('Logged GDP per capita')
plt.ylabel('Social support')
plt.grid(True)
plt.tight_layout()
plt.show()
