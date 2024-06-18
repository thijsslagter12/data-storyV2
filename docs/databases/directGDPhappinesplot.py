import pandas as pd
import plotly.express as px
import numpy as np

# Load the dataset
file_path = 'merged_dataset2_updated.csv'
data = pd.read_csv(file_path)

# Calculate the correlation between Ladder score and Logged GDP per capita
correlation = data['Happiness Score 2020'].corr(data['Logged GDP per capita'])

# Calculate the mean GDP per capita and happiness score
mean_gdp = np.mean(data['Logged GDP per capita'])
mean_score = np.mean(data['Happiness Score 2020'])

# Create a scatter plot with tooltips and a mean line
fig = px.scatter(data, x='Logged GDP per capita', y='Happiness Score 2020', hover_name='Country',
                 title=f'<b>Correlation between GDP per capita and Happiness Score</b> (Correlation: {correlation:.2f})',
                 trendline='ols')  # Ordinary Least Squares (OLS) trendline for mean

# Update layout for aesthetics
fig.update_layout(
    title_x=0.5,  # Center title
    title_font_size=24,  # Increase title font size
    yaxis_title='Happiness Score',  # Label y-axis
    showlegend=False  # Hide legend for cleaner look
)

# Show the plot
fig.show()