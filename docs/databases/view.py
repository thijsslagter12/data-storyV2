import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = 'merged_dataset2.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Display the first 5 rows of the DataFrame
print(df.head())