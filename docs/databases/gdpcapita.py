import pandas as pd

# Load merged_dataset2.csv and 2020 report dataset
merged_data_path = 'merged_dataset2.csv'
data_2020_path = '2020_happiness_report.csv'

merged_data = pd.read_csv(merged_data_path)
data_2020 = pd.read_csv(data_2020_path)

# Clean up column names by stripping any whitespace
merged_data.columns = merged_data.columns.str.strip()
data_2020.columns = data_2020.columns.str.strip()

# Merge datasets on 'Country' (ensure 'Country' exists in both)
merged_data = pd.merge(merged_data, data_2020[['Country', 'Logged GDP per capita 2020', 'Social support', 'Happiness Score 2020']], on='Country', how='left')

merged_data.drop(columns=['GDP'], inplace=True)

# Save updated dataset to CSV
merged_data.to_csv('merged_dataset2_updated.csv', index=False)

print("Social support and Logged GDP per capita columns added and saved to merged_dataset2_updated.csv")
