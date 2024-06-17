import pandas as pd
import plotly.express as px
import numpy as np

# Load the dataset
file_path = '2019.csv'
data = pd.read_csv(file_path)

# Calculate the correlation between Ladder score and Logged GDP per capita
correlation = data['Score'].corr(data['GDP per capita'])

# Calculate the mean GDP per capita and happiness score
mean_gdp = np.mean(data['GDP per capita'])
mean_score = np.mean(data['Score'])

# Create a scatter plot with tooltips and a mean line
fig = px.scatter(data, x='GDP per capita', y='Score', hover_name='Country or region',
                 title=f'<b>Correlation between GDP per capita and Happiness Score</b> (C: {correlation:.2f})',
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
