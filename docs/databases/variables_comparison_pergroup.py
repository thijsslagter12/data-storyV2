import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
merged_data = pd.read_csv('merged_dataset2_updated.csv')

# Define variables of interest for correlation analysis
variables = ['Density(P/Km2)', 'Agricultural Land( %)', 'Land Area(Km2)', 'Armed Forces size', 
             'Birth Rate', 'Co2-Emissions', 
             'Fertility Rate', 'Forested Area (%)', 'Gasoline Price', 
             'Gross primary education enrollment (%)', 'Gross tertiary education enrollment (%)', 
             'Infant mortality', 'Life expectancy', 'Maternal mortality ratio', 'Minimum wage', 'Logged GDP per capita 2020']

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

# Define thresholds for GDP per capita to classify countries into three groups
gdp_thresholds = [8, 10]  # Define your thresholds based on your criteria

# Function to categorize GDP per capita into three groups
def categorize_gdp(gdp):
    if gdp < gdp_thresholds[0]:
        return 'Ultra Poor'
    elif gdp < gdp_thresholds[1]:
        return 'Middle Poor'
    else:
        return 'Ultra Rich'

# Apply the categorization function to create a new column 'GDP Group'
merged_data['GDP Group'] = merged_data['Logged GDP per capita 2020'].apply(categorize_gdp)

# Compute correlations for each group and each variable
correlations = []

for group in ['Ultra Poor', 'Middle Poor', 'Ultra Rich']:
    group_data = merged_data[merged_data['GDP Group'] == group]
    group_corr = []
    for var in variables:
        if var in group_data.columns:
            correlation = group_data['Happiness Score 2020'].corr(group_data[var])
            group_corr.append({'Variable': var, 'Correlation': correlation, 'Group': group})
    correlations.extend(group_corr)

# Convert correlations list to DataFrame
correlations_df = pd.DataFrame(correlations)

# Plotting the correlations using a bar chart for each group
fig, axs = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

for i, group in enumerate(['Ultra Poor', 'Middle Poor', 'Ultra Rich']):
    group_corr_df = correlations_df[correlations_df['Group'] == group].sort_values(by='Correlation', key=abs, ascending=False)

    bars = axs[i].barh(range(len(group_corr_df)), group_corr_df['Correlation'], color='skyblue')
    axs[i].set_xlabel('Correlation Coefficient with Happiness Score 2020')
    axs[i].set_title(f'Correlations for {group} Group')
    axs[i].grid(axis='x', linestyle='--', alpha=0.7)

    # Set y-axis ticks and labels for the first plot only
    axs[i].set_yticks(range(len(group_corr_df)))
    axs[i].set_yticklabels(group_corr_df['Variable'])

    # Annotate bars with correlation values
    for j, bar in enumerate(bars):
        axs[i].annotate(f'{bar.get_width():.2f}', xy=(bar.get_width(), bar.get_y() + bar.get_height() / 2),
                        xytext=(5, 0), textcoords='offset points', ha='left', va='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()
