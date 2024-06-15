import plotly.graph_objs as go
import pandas as pd

# Load the correlation data
df = pd.read_csv('score_correlations.csv')

# Create the bar trace
trace = go.Bar(
    x = df['Variable1'],
    y = df['Correlation']
)

# Create the figure and update layout with titles
fig = go.Figure(trace)
fig.update_layout(
    title='Correlations with Happiness in a country',
    yaxis_title='Correlation with Happiness',
    xaxis_title='Different properties of a country',
        xaxis=dict(
        showgrid=True,  # Add grid lines to x-axis
        gridwidth=1,
        gridcolor='LightGrey'
    ),
    yaxis=dict(
        showgrid=True,  # Add grid lines to y-axis
        gridwidth=1,
        gridcolor='LightGrey'
    )
)

# Display the figure
fig.show()