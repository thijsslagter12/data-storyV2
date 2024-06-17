import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
merged_data = pd.read_csv('merged_dataset2_updated.csv')

# Define variables of interest for correlation analysis
variables = ['Density (P/Km2)', 'Agricultural Land( %)', 'Land Area(Km2)', 'Armed Forces size', 
             'Birth Rate', 'Co2-Emissions', 'CPI', 'CPI Change (%)', 'Currency-Code', 
             'Fertility Rate', 'Forested Area (%)', 'Gasoline Price', 
             'Gross primary education enrollment (%)', 'Gross tertiary education enrollment (%)', 
             'Infant mortality', 'Life expectancy', 'Maternal mortality ratio', 'Minimum wage', 'Logged GDP per capita']

# Function to preprocess columns with special characters and percentages
def preprocess_column(col):
    # Remove non-numeric characters ('$' and '%') and convert to numeric
    if merged_data[col].dtype == 'object':  # Only process columns with object dtype
        if '$' in merged_data[col].iloc[0]:  # Check if column contains '$'
            merged_data[col] = merged_data[col].replace('[\$,]', '', regex=True).astype(float)
        elif '%' in merged_data[col].iloc[0]:  # Check if column contains '%'
            merged_data[col] = merged_data[col].replace('%', '', regex=True).astype(float)
        else:
            merged_data[col] = pd.to_numeric(merged_data[col], errors='coerce')

# Preprocess columns with special characters and percentages
for var in variables:
    preprocess_column(var)

# Compute correlations with 'happy Score 2019'
correlations = []
for var in variables:
    if var in merged_data.columns:
        correlation = merged_data['happy Score 2019'].corr(merged_data[var])
        correlations.append({'Variable': var, 'Correlation': correlation})

# Convert correlations list to DataFrame
correlations_df = pd.DataFrame(correlations)

# Sort correlations by absolute value
correlations_df['Correlation'] = correlations_df['Correlation'].astype(float)
correlations_df = correlations_df.sort_values(by='Correlation', key=abs, ascending=False)

# Plotting the correlations using a bar chart
plt.figure(figsize=(12, 8))
plt.barh(correlations_df['Variable'], correlations_df['Correlation'], color='skyblue')
plt.xlabel('Correlation Coefficient with happiness score')
plt.title('Correlations between Variables and Happiness Score (2019)')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

print("Correlation DataFrame:")
print(correlations_df)
