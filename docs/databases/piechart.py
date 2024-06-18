import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('merged_dataset2_updated.csv')

# Define variables of interest and preprocess them
variables = ['Density(P/Km2)', 'Agricultural Land( %)', 'Land Area(Km2)', 'Armed Forces size', 
             'Birth Rate', 'Co2-Emissions', 
             'Fertility Rate', 'Forested Area (%)', 'Gasoline Price', 
             'Gross primary education enrollment (%)', 'Gross tertiary education enrollment (%)', 
             'Infant mortality', 'Life expectancy', 'Maternal mortality ratio', 'Minimum wage', 
             'Logged GDP per capita', 'Social support']

# Function to preprocess columns with special characters and percentages
def preprocess_column(col):
    if df[col].dtype == 'object':  # Only process columns with object dtype
        if '$' in df[col].iloc[0]:  # Check if column contains '$'
            df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)
        elif '%' in df[col].iloc[0]:  # Check if column contains '%'
            df[col] = df[col].replace('%', '', regex=True).astype(float)
        else:
            df[col] = pd.to_numeric(df[col], errors='coerce')

# Preprocess columns with special characters and percentages
for var in variables:
    preprocess_column(var)

# Filter out rows where Logged GDP per capita is NaN or missing
df = df.dropna(subset=['Logged GDP per capita'])

# Define thresholds for GDP per capita to classify countries into three groups
gdp_thresholds = [8, 10]

# Define group labels
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

# Apply categorization to create a new column 'GDP Group'
df['GDP Group'] = df['Logged GDP per capita'].apply(categorize_gdp)

# Count the number of countries in each GDP group
group_counts = df['GDP Group'].value_counts().reset_index()
group_counts.columns = ['GDP Group', 'Count']

# Create a hover text column with list of countries and GDP per capita
df['hover_text'] = df.apply(lambda row: f"{row['Country']} ({row['Logged GDP per capita']})", axis=1)

# Group by GDP Group and aggregate the hover text
hover_texts = df.groupby('GDP Group')['hover_text'].apply(lambda x: '<br>'.join(x)).reset_index()

# Merge group_counts with hover_texts
group_data = pd.merge(group_counts, hover_texts, on='GDP Group')

# Plotting the pie chart with Plotly
fig = px.pie(group_data, values='Count', names='GDP Group', 
             title='Distribution of Countries by GDP Group',
             hover_data={'hover_text': True, 'Count': True},
             labels={'GDP Group': 'GDP Group'},
             category_orders={'GDP Group': [poor_group, middle_group, rich_group]})

fig.update_traces(textinfo='percent+label', pull=[0, 0.1, 0])  # Adjust pull and textinfo for better display

fig.update_layout(showlegend=True)

fig.show()
