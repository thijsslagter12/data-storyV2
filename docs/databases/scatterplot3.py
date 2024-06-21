import pandas as pd
import plotly.express as px
import numpy as np

# Load the dataset
file_path = 'merged_dataset2_updated.csv'
data = pd.read_csv(file_path)

# Calculate the correlation between Ladder score and Logged GDP per capita
correlation = data['Social support'].corr(data['Logged GDP per capita'])

# Create a scatter plot with tooltips and a trendline
fig = px.scatter(data, x='Logged GDP per capita', y='Social support', hover_name='Country',
                 title=f'<b>Correlation between GDP per capita and Social support</b> (Correlation: {correlation:.2f})',
                 trendline='ols')

# Update layout for aesthetics
fig.update_layout(
    title_x=0.5,  # Center title
    title_font_size=18,  # Increase title font size
    yaxis_title='Social support',  # Label y-axis
    showlegend=False  # Hide legend for cleaner look
)

# Update the trendline to be red
for trace in fig.data:
    if trace.name == 'trendline':
        trace.line.color = 'red'

# Show the plot
fig.show()
