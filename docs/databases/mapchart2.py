import plotly.express as px
import pandas as pd
import numpy as np

# Laad de dataset
data = pd.read_csv('merged_dataset2_updated.csv')

# Verwijder speciale tekens en converteer de GDP kolom naar numerieke waarden
data['Logged GDP per capita'] = data['Logged GDP per capita'].replace('[\$,]', '', regex=True).astype(float)

# Maak een choropleth-kaart voor de geschaalde logaritmische GDP
fig = px.choropleth(
    data,
    locations='iso_a3',  # Gebruik de kolom met ISO 3166-1 alpha-3 landcodes
    color='Logged GDP per capita',  # Gebruik de geschaalde logaritmische 'GDP' kolom om kleuren te bepalen
    hover_name='Country',  # Toon de landnamen bij hover
    color_continuous_scale=px.colors.sequential.Plasma,  # Kleurschaal
    title='Scaled Logarithmic GDP per capita Around the World'
)

fig.show()
