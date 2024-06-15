import plotly.express as px
import pandas as pd

# Laad de dataset
data = pd.read_csv('merged_dataset2.csv')

# Maak een choropleth-kaart
fig = px.choropleth(
    data,
    locations='iso_a3',  # Gebruik de kolom met ISO 3166-1 alpha-3 landcodes
    color='happy Score 2019',       # Gebruik de 'Score' kolom om kleuren te bepalen
    hover_name='Country',# Toon de landnamen bij hover
    color_continuous_scale=px.colors.sequential.Plasma,  # Kleurschaal
    title='Happiness Around the World'
)

fig.show()