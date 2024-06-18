import pandas as pd

# Load merged_dataset2.csv and filtered Gini dataset
merged_data_path = 'merged_dataset2_updated.csv'
gini_path = 'gini-coefficient-vs-gdp-per-capita-pip.csv'

# Load datasets
merged_data = pd.read_csv(merged_data_path)
gini_data = pd.read_csv(gini_path)

# Filter out rows where Gini coefficient is not available
gini_data_filtered = gini_data.dropna(subset=['Gini coefficient'])

# Convert 'Year' column to datetime if it's in string format
if isinstance(gini_data_filtered['Year'].iloc[0], str):
    gini_data_filtered['Year'] = pd.to_datetime(gini_data_filtered['Year'], format='%Y')

# Find most recent year where Gini coefficient is available for each country
most_recent_year = gini_data_filtered.loc[gini_data_filtered.groupby('Country')['Year'].idxmax()]

# Merge datasets on 'Country' (ensure 'Country' exists in both)
merged_data_with_gini = pd.merge(merged_data, most_recent_year[['Country', 'Gini coefficient']], on='Country', how='left')

# Save updated dataset to CSV
merged_data_with_gini.to_csv('merged_dataset2_updated.csv', index=False)

print("Merged dataset with Gini coefficient added and saved to merged_dataset_with_gini.csv")
