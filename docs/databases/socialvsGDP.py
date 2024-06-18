import pandas as pd
import plotly.express as px
from scipy.stats import pearsonr
from plotly.subplots import make_subplots

# Load the dataset
df = pd.read_csv('merged_dataset2_updated.csv')

# Extract relevant columns
df = df[['Country', 'Logged GDP per capita', 'Social support', 'Happiness Score 2020']]

# Convert to numeric, handling errors if any
df['Logged GDP per capita'] = pd.to_numeric(df['Logged GDP per capita'], errors='coerce')
df['Social support'] = pd.to_numeric(df['Social support'], errors='coerce')
df['Happiness Score 2020'] = pd.to_numeric(df['Happiness Score 2020'], errors='coerce')

# Drop rows with missing values
df = df.dropna()

# Compute correlation coefficients
corr_social_support, _ = pearsonr(df['Social support'], df['Happiness Score 2020'])
corr_gdp, _ = pearsonr(df['Logged GDP per capita'], df['Happiness Score 2020'])

# Create interactive scatter plot for Social Support vs Happiness Score
fig1 = px.scatter(df, x='Social support', y='Happiness Score 2020', 
                  title='Social Support vs Happiness Score 2020',
                  labels={'Social support': 'Social support', 'Happiness Score 2020': 'Happiness Score 2020'},
                  hover_name='Country', hover_data={'Happiness Score 2020': ':.2f', 'Social support': ':.2f'})

fig1.update_traces(marker=dict(color='blue'))


# Create interactive scatter plot for Logged GDP per capita vs Happiness Score
fig2 = px.scatter(df, x='Logged GDP per capita', y='Happiness Score 2020', 
                  title='Logged GDP per capita vs Happiness Score 2020',
                  labels={'Logged GDP per capita': 'Logged GDP per capita', 'Happiness Score 2020': 'Happiness Score 2020'},
                  hover_name='Country', hover_data={'Happiness Score 2020': ':.2f', 'Logged GDP per capita': ':.2f'})

fig2.update_traces(marker=dict(color='green'))


# Combine the two figures into a single plot
combined_fig = make_subplots(rows=1, cols=2, subplot_titles=("Social Support vs Happiness Score", "GDP per capita vs Happiness Score"))
for trace in fig1.data:
    combined_fig.add_trace(trace, row=1, col=1)
for trace in fig2.data:
    combined_fig.add_trace(trace, row=1, col=2)

# Update x-axis and y-axis titles for each subplot
combined_fig.update_xaxes(title_text="Social Support", row=1, col=1)
combined_fig.update_yaxes(title_text="Happiness Score", row=1, col=1)
combined_fig.update_xaxes(title_text="GDP per capita", row=1, col=2)
combined_fig.update_yaxes(title_text="Happiness Score", row=1, col=2)

# Calculate relative position for annotations
x_annotation1 = 0.95 # Adjust as needed
x_annotation2 = 11.3  # Adjust as needed
y_annotation = 1.05   # Adjust as needed

# Calculate relative font size
font_size = 20  # Adjust as needed

# Add textbox annotations at the top center of each subplot
combined_fig.add_annotation(
    text=f'Correlation: {corr_social_support:.2f}',
    xref='paper', yref='paper',
    x=x_annotation1, y=y_annotation,
    showarrow=False,
    font=dict(size=font_size, color='black'),
    align='left', bgcolor='rgba(255, 255, 255, 0.5)',
    row=1, col=1
)

combined_fig.add_annotation(
    text=f'Correlation: {corr_gdp:.2f}',
    xref='paper', yref='paper',
    x=x_annotation2, y=y_annotation,
    showarrow=False,
    font=dict(size=font_size, color='black'),
    align='left', bgcolor='rgba(255, 255, 255, 0.5)',
    row=1, col=2
)


# Update layout with centered and larger title
combined_fig.update_layout(
    title_text='Impact of Social Support and GDP per capita on Happiness in 2020',
    title_x=0.5,  # Center title horizontally
    title_y=0.95,  # Position title slightly above the plots
    title_font=dict(size=20),  # Increase font size
    showlegend=False
)
# Show the combined figure
combined_fig.show()
