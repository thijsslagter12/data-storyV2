import pandas as pd

# Load merged_dataset2.csv and 2020 report dataset
merged_data_path = 'merged_dataset2.csv'
data_2020_path = '2020_happiness_report.csv'

merged_data = pd.read_csv(merged_data_path)
data_2020 = pd.read_csv(data_2020_path)

# Clean up column names by stripping any whitespace
merged_data.columns = merged_data.columns.str.strip()
data_2020.columns = data_2020.columns.str.strip()

# Merge datasets on 'Country'
merged_data = pd.merge(merged_data, data_2020[['Country', 'Logged GDP per capita']], on='Country', how='inner')

# Replace 'GDP' column with 'Logged GDP per capita'
merged_data['GDP'] = data_2020['Logged GDP per capita']

merged_data.drop(columns=['GDP'], inplace=True)

# Save updated dataset to CSV
merged_data.to_csv('merged_dataset2_updated.csv', index=False)


print("GDP column updated and saved to merged_dataset2_updated.csv")


