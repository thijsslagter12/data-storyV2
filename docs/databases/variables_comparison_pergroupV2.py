import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the merged dataset
merged_data = pd.read_csv('merged_dataset2_updated.csv')

# Define variables of interest for correlation analysis
variables = ['Density(P/Km2)', 'Agricultural Land( %)', 'Land Area(Km2)', 'Armed Forces size', 
             'Birth Rate', 'Co2-Emissions', 
             'Fertility Rate', 'Forested Area (%)', 'Gasoline Price', 
             'Gross primary education enrollment (%)', 'Gross tertiary education enrollment (%)', 
             'Infant mortality', 'Life expectancy', 'Maternal mortality ratio', 'Minimum wage', 
             'Logged GDP per capita', 'Social support']

# Function to preprocess columns with special characters and percentages
def preprocess_column(col):
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

# Filter out rows where Logged GDP per capita is NaN or missing
merged_data = merged_data.dropna(subset=['Logged GDP per capita'])

# Define thresholds for GDP per capita to classify countries into three groups
gdp_thresholds = [8, 10]  # Define your thresholds based on your criteria

poor_group = f'Ultra Poor: GDP per capita < {gdp_thresholds[0]}'
middle_group = f'Middle Poor: {gdp_thresholds[0]} <= GDP per capita < {gdp_thresholds[1]}'
rich_group = f'Ultra Rich: GDP per capita >= {gdp_thresholds[1]}'

# Function to categorize GDP per capita into three groups
def categorize_gdp(gdp):
    if gdp < gdp_thresholds[0]:
        return poor_group
    elif gdp < gdp_thresholds[1]:
        return middle_group
    else:
        return rich_group

# Apply the categorization function to create a new column 'GDP Group'
merged_data['GDP Group'] = merged_data['Logged GDP per capita'].apply(categorize_gdp)

# Compute correlations for each group and each variable
correlations = []

for group in [poor_group, middle_group, rich_group]:
    group_data = merged_data[merged_data['GDP Group'] == group]
    group_corr = []
    for var in variables:
        if var in group_data.columns:
            correlation = group_data['Happiness Score 2020'].corr(group_data[var])
            group_corr.append({'Variable': var, 'Correlation': correlation, 'Group': group})
    correlations.extend(group_corr)

# Convert correlations list to DataFrame
correlations_df = pd.DataFrame(correlations)

# Plotting the bar chart
plt.figure(figsize=(12, 8))
sns.barplot(x='Correlation', y='Variable', hue='Group', data=correlations_df, palette='Set2')
plt.title('Correlation of Variables with Happiness Score by grouped GDP countries')
plt.xlabel('Correlation with happiness')
plt.ylabel('Variable')
plt.grid(True)
plt.legend(title='GDP grouped countries', loc='upper right')
plt.tight_layout()
plt.show()
